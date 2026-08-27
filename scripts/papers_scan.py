#!/usr/bin/env python3
"""Check the publication register against the links file, the PDFs and the reviews.

Four places have to agree about which papers exist, and the eLibrary item id is
what ties them together:

    pdf/pdf_links.txt        one item.asp?id=<id> URL per line
    pdf/elibrary_<id>_*.pdf  the downloaded file
    _data/papers.yml         the register - the copy of record
    _reviews/<slug>.md       the write-up, matched through its paper_link

eLibrary is behind a session, so none of this can be re-fetched: when the register
and the disk disagree, the register is what a human has to fix. This script only
reports; it never deletes a PDF or edits the register.

Usage:
    python scripts/papers_scan.py
    python scripts/papers_scan.py --extract ../paper-text   # pdftotext for unreviewed papers
    python scripts/papers_scan.py --json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = ROOT / "pdf"
LINKS_FILE = PDF_DIR / "pdf_links.txt"
REGISTER = ROOT / "_data" / "papers.yml"
REVIEWS_DIR = ROOT / "_reviews"

ID_IN_URL = re.compile(r"[?&]id=(\d+)")
ID_IN_PDF = re.compile(r"^elibrary_(\d+)_\d+\.pdf$", re.IGNORECASE)
FRONT_MATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def _utf8_stdout() -> None:
    """Windows consoles default to cp1252, which cannot print Cyrillic titles."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def load_register() -> list[dict]:
    if not REGISTER.exists():
        sys.exit(f"missing {REGISTER.relative_to(ROOT)}")
    data = yaml.safe_load(REGISTER.read_text(encoding="utf-8")) or []
    if not isinstance(data, list):
        sys.exit("_data/papers.yml must contain a list")
    return data


def load_links() -> dict[str, str]:
    """Item id -> URL, from the hand-maintained links file."""
    if not LINKS_FILE.exists():
        return {}
    found = {}
    for line in LINKS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = ID_IN_URL.search(line)
        if match:
            found[match.group(1)] = line
    return found


def load_pdfs() -> dict[str, list[Path]]:
    """Item id -> every PDF on disk carrying that id.

    More than one is normal after a re-download: eLibrary mints a fresh second
    number each time, so the same paper arrives as a differently named file.
    """
    by_id: dict[str, list[Path]] = defaultdict(list)
    for path in sorted(PDF_DIR.glob("*.pdf")):
        match = ID_IN_PDF.match(path.name)
        if match:
            by_id[match.group(1)].append(path)
    return by_id


def load_reviews() -> dict[str, list[str]]:
    """Item id -> review slugs that cite it (both language versions)."""
    by_id: dict[str, list[str]] = defaultdict(list)
    for path in sorted(REVIEWS_DIR.glob("*.md")):
        match = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
        if not match:
            continue
        data = yaml.safe_load(match.group(1))
        if not isinstance(data, dict) or data.get("published") is False:
            continue
        link = str(data.get("paper_link") or "")
        found = ID_IN_URL.search(link)
        if found:
            by_id[found.group(1)].append(path.stem)
    return by_id


def digest(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            sha.update(block)
    return sha.hexdigest()


def scan() -> dict:
    register = load_register()
    links, pdfs, reviews = load_links(), load_pdfs(), load_reviews()

    by_id = {str(entry.get("id")): entry for entry in register if entry.get("id") is not None}
    problems: list[str] = []
    notes: list[str] = []

    if len(by_id) != len(register):
        problems.append(f"register has {len(register)} entries but only {len(by_id)} distinct ids")

    # Register vs the links file.
    for item_id in sorted(set(links) - set(by_id)):
        problems.append(f"{item_id}: in pdf_links.txt but not in the register")
    for item_id in sorted(set(by_id) - set(links)):
        if by_id[item_id].get("pdf"):
            notes.append(f"{item_id}: registered with a PDF but absent from pdf_links.txt")

    # Register vs the PDFs on disk.
    for item_id in sorted(set(pdfs) - set(by_id)):
        problems.append(f"{item_id}: PDF on disk but not in the register")

    duplicates = []
    for item_id, paths in sorted(pdfs.items()):
        if len(paths) > 1:
            hashes = {digest(p) for p in paths}
            duplicates.append({
                "id": item_id,
                "files": [p.name for p in paths],
                "identical": len(hashes) == 1,
            })

    rows = []
    for entry in register:
        item_id = str(entry.get("id"))
        declared = entry.get("pdf")
        on_disk = [p.name for p in pdfs.get(item_id, [])]

        state = "reviewed" if entry.get("review") else ("ready" if declared else "link only")
        if declared and declared not in on_disk:
            problems.append(f"{item_id}: register names {declared}, which is not in pdf/")
            state = "pdf missing"
        if not declared and on_disk:
            problems.append(f"{item_id}: {on_disk[0]} is on disk but the register says pdf: null")

        cited = reviews.get(item_id, [])
        if entry.get("review") and not cited:
            problems.append(f"{item_id}: register names review {entry['review']}, but no review cites this id")
        if cited and not entry.get("review"):
            problems.append(f"{item_id}: cited by {', '.join(cited)} but the register says review: null")

        missing = [f for f in ("venue", "year") if entry.get(f) in (None, "")]
        if missing and not entry.get("review"):
            notes.append(f"{item_id}: register has no {' or '.join(missing)}")

        rows.append({
            "id": item_id,
            "state": state,
            "title": entry.get("title") or "",
            "pdf": declared,
            "review": entry.get("review"),
            "incomplete": missing,
        })

    return {"rows": rows, "problems": problems, "notes": notes,
            "duplicates": duplicates, "counts": {
                "registered": len(register), "links": len(links),
                "pdf_ids": len(pdfs), "reviewed": sum(1 for r in rows if r["state"] == "reviewed"),
            }}


def extract(out_dir: Path, only_unreviewed: bool = True) -> None:
    """Run pdftotext so the local model can read the papers - it refuses binary."""
    register = {str(e.get("id")): e for e in load_register()}
    pdfs = load_pdfs()
    out_dir.mkdir(parents=True, exist_ok=True)
    done = 0
    for item_id, paths in sorted(pdfs.items()):
        entry = register.get(item_id, {})
        if only_unreviewed and entry.get("review"):
            continue
        source = PDF_DIR / (entry.get("pdf") or paths[0].name)
        if not source.exists():
            source = paths[0]
        target = out_dir / f"{source.stem}.txt"
        result = subprocess.run(
            ["pdftotext", "-enc", "UTF-8", str(source), str(target)],
            capture_output=True, text=True,
        )
        if result.returncode == 0 and target.exists():
            print(f"  {source.name} -> {target.name}  ({target.stat().st_size:,} bytes)")
            done += 1
        else:
            print(f"  {source.name}: pdftotext failed - {result.stderr.strip()[:80]}")
    print(f"\n{done} file(s) extracted into {out_dir}")


def report(result: dict) -> None:
    counts = result["counts"]
    print(f"{counts['registered']} registered - {counts['reviewed']} reviewed, "
          f"{counts['links']} link(s) on file, {counts['pdf_ids']} paper(s) with a PDF\n")

    head = f"{'ID':<10} {'STATE':<12} {'REVIEW':<34} TITLE"
    print(head)
    print("-" * (len(head) + 22))
    for row in result["rows"]:
        print(f"{row['id']:<10} {row['state']:<12} {(row['review'] or '-'):<34} {row['title'][:44]}")

    if result["duplicates"]:
        print("\nDuplicate downloads:")
        for dup in result["duplicates"]:
            same = "byte-identical" if dup["identical"] else "DIFFERENT CONTENT - check before deleting"
            print(f"  {dup['id']}: {same}")
            for name in dup["files"]:
                print(f"    {name}")

    if result["problems"]:
        print("\nProblems:")
        for problem in result["problems"]:
            print(f"  {problem}")

    if result["notes"]:
        print("\nIncomplete metadata (fill in by hand - eLibrary cannot be fetched):")
        for note in result["notes"]:
            print(f"  {note}")

    if not result["problems"]:
        print("\nNo problems found.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--extract", metavar="DIR", help="pdftotext the unreviewed papers into DIR")
    parser.add_argument("--all", action="store_true", help="with --extract, include already-reviewed papers")
    args = parser.parse_args()
    _utf8_stdout()

    result = scan()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        report(result)

    if args.extract:
        print(f"\nExtracting text for local digesting:")
        extract(Path(args.extract), only_unreviewed=not args.all)

    return 1 if result["problems"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
