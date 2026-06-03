#!/usr/bin/env python3
"""Cross-post a published article to VK (personal wall) and/or Telegram.

Designed to run from a manual GitHub Actions workflow. Secrets are read from the
environment; nothing here is specific to CI, so it can also be run locally:

    VK_ACCESS_TOKEN=... TELEGRAM_BOT_TOKEN=... TELEGRAM_CHAT_ID=@channel \\
        python scripts/social_post.py --targets vk telegram --dry-run

Only Russian, non-translation articles are eligible (matching how the VK
content is authored today).
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

try:  # ensure Cyrillic output works on consoles that default to cp1252
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):  # pragma: no cover - older/odd streams
    pass

ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = ROOT / "_articles"
CONFIG = ROOT / "_config.yml"
VK_API_VERSION = "5.199"


def _site_url() -> str:
    """Base public URL from _config.yml (url + baseurl), without trailing slash."""
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}
    url = (cfg.get("url") or "").rstrip("/")
    baseurl = (cfg.get("baseurl") or "").rstrip("/")
    return f"{url}{baseurl}"


def _front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    _, _, rest = text.partition("---\n")
    fm, sep, _ = rest.partition("\n---")
    if not sep:
        return {}
    return yaml.safe_load(fm) or {}


def _is_eligible(meta: dict) -> bool:
    """Russian originals only — skip English files and translations."""
    return meta.get("lang", "ru") == "ru" and not meta.get("translation_of")


def _article_url(path: Path) -> str:
    """Public URL from the collection permalink `/blog/:path/`."""
    rel = path.relative_to(ARTICLES_DIR).with_suffix("")
    return f"{_site_url()}/blog/{rel.as_posix()}/"


def _resolve_article(arg: str | None) -> Path:
    if arg:
        path = (ROOT / arg).resolve() if not Path(arg).is_absolute() else Path(arg)
        if not path.is_file():
            raise SystemExit(f"Article not found: {arg}")
        meta = _front_matter(path)
        if not _is_eligible(meta):
            raise SystemExit(f"{arg} is not a Russian original (lang/translation_of).")
        return path

    # Default: most recent Russian original by date.
    candidates: list[tuple[str, Path]] = []
    for path in ARTICLES_DIR.rglob("*.md"):
        meta = _front_matter(path)
        if _is_eligible(meta):
            candidates.append((str(meta.get("date", "")), path))
    if not candidates:
        raise SystemExit("No eligible Russian articles found.")
    return max(candidates, key=lambda item: item[0])[1]


def _post(url: str, data: dict) -> dict:
    body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers={"User-Agent": "social-post"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def post_vk(title: str, summary: str, link: str, dry_run: bool, env: dict) -> None:
    token = env.get("VK_ACCESS_TOKEN")
    if not token:
        raise SystemExit("VK_ACCESS_TOKEN is not set.")
    message = f"{title}\n\n{summary}".strip()
    params = {
        "access_token": token,
        "v": VK_API_VERSION,
        "message": message,
        "attachments": link,
        "from_group": "0",
    }
    owner_id = env.get("VK_OWNER_ID")
    if owner_id:
        params["owner_id"] = owner_id  # omit -> posts to the token owner's wall
    if dry_run:
        print(f"[dry-run] VK wall.post -> owner={owner_id or 'self'}\n{message}\n{link}")
        return
    result = _post("https://api.vk.com/method/wall.post", params)
    if "error" in result:
        raise SystemExit(f"VK error: {result['error']}")
    print(f"VK: posted (post_id={result.get('response', {}).get('post_id')})")


def post_telegram(title: str, summary: str, link: str, dry_run: bool, env: dict) -> None:
    token = env.get("TELEGRAM_BOT_TOKEN")
    chat_id = env.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        raise SystemExit("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set.")
    text = f"<b>{title}</b>\n\n{summary}\n\n{link}".strip()
    params = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": "false",
    }
    if dry_run:
        print(f"[dry-run] Telegram sendMessage -> {chat_id}\n{text}")
        return
    result = _post(f"https://api.telegram.org/bot{token}/sendMessage", params)
    if not result.get("ok"):
        raise SystemExit(f"Telegram error: {result}")
    print("Telegram: posted")


def main() -> int:
    import os

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article", help="Path to the article (default: latest RU original).")
    parser.add_argument(
        "--targets",
        nargs="+",
        choices=["vk", "telegram"],
        default=["vk", "telegram"],
    )
    parser.add_argument("--dry-run", action="store_true", help="Print, do not call APIs.")
    args = parser.parse_args()

    path = _resolve_article(args.article)
    meta = _front_matter(path)
    title = str(meta.get("title", "")).strip()
    summary = str(meta.get("summary", "")).strip()
    link = _article_url(path)
    print(f"Article: {path.relative_to(ROOT)}\nTitle: {title}\nURL: {link}\n")

    if "vk" in args.targets:
        post_vk(title, summary, link, args.dry_run, os.environ)
    if "telegram" in args.targets:
        post_telegram(title, summary, link, args.dry_run, os.environ)
    return 0


if __name__ == "__main__":
    sys.exit(main())
