from __future__ import annotations

from pathlib import Path
import re

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PAGES = [
    ROOT / "index.html",
    ROOT / "blog.html",
    ROOT / "projects.html",
    ROOT / "about.md",
    ROOT / "404.md",
]
TEMPLATE_FILES = [
    ROOT / "_includes" / "site_header.html",
    ROOT / "_includes" / "article_card.html",
    ROOT / "_layouts" / "article.html",
]
DATA_FILES = [
    ROOT / "_config.yml",
    ROOT / "_data" / "projects.yml",
]
MOJIBAKE_MARKERS = ("Ð", "Ñ", "â€”", "â†’", "â€œ", "â€", "Â«", "Â»", "ï¸")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _front_matter(path: Path) -> dict:
    text = _read_text(path)
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    assert match, f"{path.relative_to(ROOT)} must keep YAML front matter"
    return yaml.safe_load(match.group(1))


@pytest.mark.smoke
def test_public_pages_have_title_and_description() -> None:
    for path in PUBLIC_PAGES:
        meta = _front_matter(path)
        assert meta.get("title"), f"{path.relative_to(ROOT)} needs a title"
        assert meta.get("description"), f"{path.relative_to(ROOT)} needs a description"


@pytest.mark.smoke
def test_homepage_sections_match_navigation_anchors() -> None:
    homepage = _read_text(ROOT / "index.html")
    header = _read_text(ROOT / "_includes" / "site_header.html")
    sections = ("approach", "featured-work", "writing", "contact")
    for section in sections:
        assert f'id="{section}"' in homepage, f"index.html must expose #{section}"
        assert f'href="#{section}"' in header, f"site header must link to #{section}"


@pytest.mark.smoke
def test_public_sources_do_not_contain_common_mojibake_markers() -> None:
    for path in [*PUBLIC_PAGES, *TEMPLATE_FILES, *DATA_FILES]:
        text = _read_text(path)
        assert not any(marker in text for marker in MOJIBAKE_MARKERS), (
            f"{path.relative_to(ROOT)} contains mojibake markers from broken UTF-8 text"
        )
