#!/usr/bin/env python3
"""Report which projects have unwritten changes since their last article.

Every article carries a `source_rev` in its front matter: the commit that article
covers up to. The delta worth writing about is therefore `source_rev..HEAD`, and
this script computes it for each project so "what is new since I last wrote"
stops being a judgement call.

Two things it deliberately does NOT do:

  * It does not treat commit count as importance. Forks and shared repos are full
    of other people's commits; the `yours` column and the ownership warnings are
    the numbers to read.
  * It does not read the diffs. Use `--dump-diff DIR` and hand the files to the
    local model instead of pulling them into an assistant's context.

Local repository paths live in scripts/repos.local.yml, which is git-ignored so
that machine-specific paths never reach the public repo. See repos.example.yml.

Usage:
    python scripts/project_scan.py
    python scripts/project_scan.py --json
    python scripts/project_scan.py --dump-diff ../scratch/diffs
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "_articles"
PROJECTS_FILE = ROOT / "_data" / "projects.yml"
CONFIG_FILE = Path(__file__).resolve().parent / "repos.local.yml"

FRONT_MATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


# --------------------------------------------------------------------------- io


def _utf8_stdout() -> None:
    """Windows consoles default to cp1252, which cannot print Cyrillic titles."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def read_front_matter(path: Path) -> dict:
    """Parse a Markdown file's YAML front matter, mirroring tests/test_content_unit.py."""
    match = FRONT_MATTER_RE.match(path.read_text(encoding="utf-8"))
    if not match:
        return {}
    data = yaml.safe_load(match.group(1))
    return data if isinstance(data, dict) else {}


def load_config(path: Path | None = None) -> dict:
    config_file = path or CONFIG_FILE
    if not config_file.exists():
        sys.exit(
            f"Missing {config_file}.\n"
            f"Copy scripts/repos.example.yml to scripts/repos.local.yml and point it\n"
            f"at your local clones."
        )
    data = yaml.safe_load(config_file.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else {}


def load_project_slugs() -> list[str]:
    data = yaml.safe_load(PROJECTS_FILE.read_text(encoding="utf-8")) or []
    return [p["slug"] for p in data if isinstance(p, dict) and p.get("slug")]


# -------------------------------------------------------------------------- git


def git(repo: Path, *args: str) -> tuple[int, str]:
    """Run a git command, returning (returncode, stripped stdout)."""
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode, (proc.stdout or "").strip()


def rev_exists(repo: Path, rev: str) -> bool:
    code, _ = git(repo, "cat-file", "-e", f"{rev}^{{commit}}")
    return code == 0


def commits(repo: Path, rev_range: str, author: str | None) -> list[dict]:
    args = ["log", rev_range, "--no-merges", "--date=short", "--format=%H%x1f%h%x1f%ad%x1f%an%x1f%s"]
    if author:
        args.append(f"--author={author}")
    code, out = git(repo, *args)
    if code != 0 or not out:
        return []
    rows = []
    for line in out.splitlines():
        parts = line.split("\x1f")
        if len(parts) == 5:
            rows.append(dict(zip(("sha", "short", "date", "author", "subject"), parts)))
    return rows


# ---------------------------------------------------------------------- scanning


def normalize_clones(value) -> dict[str, str]:
    """A project maps either to a single clone, or to several named ones.

    Tea Taste is split across an API and a frontend repository, so one project can
    legitimately have more than one source of changes. A bare string keeps the
    simple single-repo case unchanged; the empty key marks it.
    """
    if isinstance(value, str):
        return {"": value}
    if isinstance(value, dict):
        return {str(name): str(path) for name, path in value.items()}
    return {}


def normalize_anchor(rev) -> dict[str, str]:
    """`source_rev` mirrors the clone map: one SHA, or one per named clone."""
    if isinstance(rev, str):
        return {"": rev}
    if isinstance(rev, dict):
        return {str(name): str(sha) for name, sha in rev.items()}
    return {}


def newest_anchor_per_project() -> dict[str, dict]:
    """Latest article per project that declares a source_rev.

    Only Russian originals are considered: translations describe the same change,
    so counting them would just pick an arbitrary one of the pair.
    """
    anchors: dict[str, dict] = {}
    for path in sorted(ARTICLES_DIR.glob("*/*.md")):
        fm = read_front_matter(path)
        slug, rev, date = fm.get("project"), fm.get("source_rev"), fm.get("date")
        if not slug or not rev or fm.get("lang") != "ru" or fm.get("translation_of"):
            continue
        current = anchors.get(slug)
        if current is None or str(date) > str(current["date"]):
            # `rev` stays as parsed: a string for one clone, a mapping for several.
            anchors[slug] = {"rev": rev, "date": str(date), "article": path.relative_to(ROOT).as_posix()}
    return anchors


def scan(config: dict, author: str | None, all_authors: bool) -> list[dict]:
    repos = config.get("repos") or {}
    owner = (config.get("owner") or "").lower()
    anchors = newest_anchor_per_project()

    results = []
    for slug in load_project_slugs():
        row: dict = {"project": slug, "status": "", "new": None, "yours": None,
                     "anchor": None, "anchor_date": None, "latest": None,
                     "warnings": [], "commits": [], "clones": []}

        clones = normalize_clones(repos.get(slug))
        if not clones:
            row["status"] = "no local clone"
            results.append(row)
            continue

        anchor = anchors.get(slug)
        if anchor:
            row["anchor_date"] = anchor["date"]
            row["article"] = anchor["article"]
        revs = normalize_anchor(anchor["rev"]) if anchor else {}

        total_new = total_mine = 0
        anchor_labels, scanned = [], 0

        for name, raw_path in clones.items():
            # Only name the clone when there is more than one; otherwise the label
            # just repeats the project name that print_table already prints.
            label = name if name else slug
            prefix = f"{label}: " if name else ""
            part: dict = {"clone": label, "status": "", "new": None, "yours": None, "anchor": None}
            repo = Path(raw_path).expanduser()

            if not (repo / ".git").is_dir():
                part["status"] = "path missing"
                row["warnings"].append(f"{prefix}{repo} is not a git repository")
                row["clones"].append(part)
                continue

            # Ownership guard. Note this only catches repos owned by someone else;
            # a fork pushed under your own handle looks legitimate here and is
            # caught by the authorship ratio below instead.
            _, origin = git(repo, "remote", "get-url", "origin")
            part["origin"] = origin
            if owner and origin and owner not in origin.lower():
                row["warnings"].append(f"{prefix}origin is not yours ({origin}) - verify before writing")

            rev = revs.get(name) or (revs.get("") if len(clones) == 1 else None)
            if not rev:
                part["status"] = "no anchor"
                row["warnings"].append(f"{prefix}no article declares a source_rev for this clone")
                row["clones"].append(part)
                continue

            if not rev_exists(repo, rev):
                part["status"] = "anchor missing"
                row["warnings"].append(
                    f"{prefix}{rev[:7]} is not in this repo - history rewritten, or wrong clone"
                )
                row["clones"].append(part)
                continue

            every = commits(repo, f"{rev}..HEAD", None)
            mine = commits(repo, f"{rev}..HEAD", None if all_authors else author)
            for commit in mine:
                commit["clone"] = label

            part.update(anchor=rev[:7], new=len(every), yours=len(mine),
                        status="up to date" if not mine else "ready",
                        path=str(repo), rev=rev)
            anchor_labels.append(rev[:7])
            total_new += len(every)
            total_mine += len(mine)
            scanned += 1
            row["commits"].extend(mine)
            row["clones"].append(part)

            if every and mine and len(mine) / len(every) < 0.25:
                row["warnings"].append(
                    f"{prefix}only {len(mine)} of {len(every)} commits are yours - likely a fork"
                )

        if not scanned:
            row["status"] = "no anchor" if not revs else "path missing"
            results.append(row)
            continue

        row["commits"].sort(key=lambda c: c["date"], reverse=True)
        row["anchor"] = anchor_labels[0] if len(anchor_labels) == 1 else f"{len(anchor_labels)} clones"
        row["new"], row["yours"] = total_new, total_mine
        row["latest"] = row["commits"][0]["date"] if row["commits"] else None
        row["status"] = "up to date" if not total_mine else "ready"
        results.append(row)
    return results


# ----------------------------------------------------------------------- output


def print_table(rows: list[dict]) -> None:
    head = f"{'PROJECT':<30} {'ANCHOR':<9} {'ANCHORED':<11} {'NEW':>4} {'YOURS':>6}  {'LATEST':<11} STATUS"
    print(head)
    print("-" * len(head))
    for r in rows:
        print(
            f"{r['project'][:30]:<30} "
            f"{(r['anchor'] or '-'):<9} "
            f"{(r['anchor_date'] or '-'):<11} "
            f"{('-' if r['new'] is None else r['new']):>4} "
            f"{('-' if r['yours'] is None else r['yours']):>6}  "
            f"{(r['latest'] or '-'):<11} "
            f"{r['status']}"
        )

    ready = [r for r in rows if r["status"] == "ready"]
    if ready:
        print("\nUnwritten work:")
        for r in ready:
            print(f"\n  {r['project']}  ({r['yours']} of {r['new']} commits yours, since {r['anchor_date']})")
            multi = len([c for c in r["clones"] if c.get("rev")]) > 1
            for c in r["commits"][:8]:
                where = f"{c['clone']}: " if multi else ""
                print(f"    {c['short']}  {c['date']}  {where}{c['subject'][:64 - len(where)]}")
            if len(r["commits"]) > 8:
                print(f"    ... and {len(r['commits']) - 8} more")

    warned = [r for r in rows if r["warnings"]]
    if warned:
        print("\nWarnings:")
        for r in warned:
            for w in r["warnings"]:
                print(f"  {r['project']}: {w}")


def dump_diffs(rows: list[dict], config: dict, out_dir: Path, author: str | None, all_authors: bool) -> None:
    """Write each project's pending diff to a file, ready for local_digest.

    Kept out of the table output on purpose: these files are large, and the whole
    point is that the local model reads them instead of an assistant's context.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    for row in rows:
        if row["status"] != "ready":
            continue
        for part in row["clones"]:
            if part["status"] != "ready":
                continue
            args = ["log", "-p", f"{part['rev']}..HEAD", "--no-merges", "--date=short",
                    "--format=%n=== %h %ad %an%n%s%n%b%n"]
            if not all_authors and author:
                args.append(f"--author={author}")
            code, out = git(Path(part["path"]), *args)
            if code != 0 or not out:
                continue
            stem = row["project"] if part["clone"] == row["project"] else f"{row['project']}.{part['clone']}"
            target = out_dir / f"{stem}.diff"
            target.write_text(out, encoding="utf-8")
            print(f"  wrote {target.name}  ({len(out):,} chars, ~{len(out) // 4:,} tokens)")


def write_notes(article: Path, config: dict, author: str | None, all_authors: bool) -> int:
    """Record which commits a post was written from, into notes/<slug>.md.

    `source_rev` says what a post covers up to; `source_from` says where it starts.
    Between them they pin an exact range, so this file is derived, not maintained
    by hand - regenerate it rather than editing it. It is excluded from the build.
    """
    fm = read_front_matter(article)
    slug = fm.get("project")
    if not slug:
        sys.exit(f"{article} declares no project")
    if not fm.get("source_from"):
        sys.exit(f"{article} declares no source_from, so its range has no start")

    clones = normalize_clones((config.get("repos") or {}).get(slug))
    if not clones:
        sys.exit(f"no local clone configured for {slug}")

    starts = normalize_anchor(fm["source_from"])
    ends = normalize_anchor(fm.get("source_rev"))

    lines = [
        f"# {fm.get('title', article.stem)}",
        "",
        f"Post: `{article.relative_to(ROOT).as_posix()}`  ",
        f"Project: `{slug}`",
        "",
        "Commits this post was written from. Generated by",
        "`python scripts/project_scan.py --notes <article>`; do not edit by hand.",
        "",
    ]

    total = 0
    for name, raw_path in clones.items():
        key = name if name in starts else ""
        start, end = starts.get(key), ends.get(key) or "HEAD"
        if not start:
            continue
        repo = Path(raw_path).expanduser()
        if not (repo / ".git").is_dir():
            continue
        rows = commits(repo, f"{start}..{end}", None if all_authors else author)
        label = name or slug
        lines.append(f"## {label}")
        lines.append("")
        lines.append(f"`{start[:7]}..{end[:7]}` - {len(rows)} commit(s)")
        lines.append("")
        for row in rows:
            lines.append(f"- `{row['short']}` {row['date']} - {row['subject']}")
        lines.append("")
        total += len(rows)

    target = ROOT / "notes" / f"{article.stem}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {target.relative_to(ROOT).as_posix()}  ({total} commits)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--config", metavar="FILE", help="use an alternate repo map (default: scripts/repos.local.yml)")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--author", help="override the author filter (matches name or email substring)")
    parser.add_argument("--all-authors", action="store_true", help="count everyone's commits, not just yours")
    parser.add_argument("--dump-diff", metavar="DIR", help="write pending diffs here for local digesting")
    parser.add_argument("--notes", metavar="ARTICLE", help="record the commits an article was written from")
    args = parser.parse_args()
    _utf8_stdout()

    config = load_config(Path(args.config) if args.config else None)
    author = args.author or config.get("author")

    if args.notes:
        return write_notes(Path(args.notes).resolve(), config, author, args.all_authors)
    rows = scan(config, author, args.all_authors)

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        print_table(rows)

    if args.dump_diff:
        print(f"\nDiffs for local digesting:")
        dump_diffs(rows, config, Path(args.dump_diff), author, args.all_authors)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
