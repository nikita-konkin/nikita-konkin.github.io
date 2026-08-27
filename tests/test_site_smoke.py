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
    ROOT / "tags.html",
    ROOT / "about.md",
    ROOT / "404.md",
    ROOT / "en" / "index.html",
    ROOT / "en" / "blog.html",
    ROOT / "en" / "projects.html",
    ROOT / "en" / "tags.html",
    ROOT / "en" / "about.md",
    ROOT / "en" / "404.html",
]
TEMPLATE_FILES = [
    ROOT / "_includes" / "site_header.html",
    ROOT / "_includes" / "article_card.html",
    ROOT / "_includes" / "page_landing.html",
    ROOT / "_includes" / "page_projects.html",
    ROOT / "_includes" / "page_blog.html",
    ROOT / "_layouts" / "article.html",
]
DATA_FILES = [
    ROOT / "_config.yml",
    ROOT / "_data" / "projects.yml",
]
TRANSLATED_PAGE_PAIRS = [
    (ROOT / "index.html", ROOT / "en" / "index.html", "/en/", "/"),
    (ROOT / "blog.html", ROOT / "en" / "blog.html", "/en/blog/", "/blog/"),
    (ROOT / "projects.html", ROOT / "en" / "projects.html", "/en/projects/", "/projects/"),
    (ROOT / "tags.html", ROOT / "en" / "tags.html", "/en/tags/", "/tags/"),
    (ROOT / "about.md", ROOT / "en" / "about.md", "/en/about/", "/about/"),
    (ROOT / "404.md", ROOT / "en" / "404.html", "/en/404.html", "/404.html"),
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
        assert meta.get("lang") in {"ru", "en"}, (
            f"{path.relative_to(ROOT)} must declare ru/en language metadata"
        )
        assert meta.get("translation_url"), (
            f"{path.relative_to(ROOT)} must expose a translation_url for the header switch"
        )


@pytest.mark.smoke
def test_page_translation_pairs_are_reciprocal() -> None:
    for ru_path, en_path, ru_translation_url, en_translation_url in TRANSLATED_PAGE_PAIRS:
        ru_meta = _front_matter(ru_path)
        en_meta = _front_matter(en_path)
        assert ru_meta["lang"] == "ru", f"{ru_path.relative_to(ROOT)} must stay Russian"
        assert en_meta["lang"] == "en", f"{en_path.relative_to(ROOT)} must stay English"
        assert ru_meta["translation_url"] == ru_translation_url, (
            f"{ru_path.relative_to(ROOT)} must point to {ru_translation_url}"
        )
        assert en_meta["translation_url"] == en_translation_url, (
            f"{en_path.relative_to(ROOT)} must point back to {en_translation_url}"
        )


@pytest.mark.smoke
def test_homepage_sections_match_navigation_anchors() -> None:
    homepage = _read_text(ROOT / "_includes" / "page_landing.html")
    header = _read_text(ROOT / "_includes" / "site_header.html")
    sections = ("approach", "featured-work", "writing", "contact")
    for section in sections:
        assert f'id="{section}"' in homepage, f"page_landing.html must expose #{section}"
        assert f'href="#{section}"' in header, f"site header must link to #{section}"


@pytest.mark.smoke
def test_public_sources_do_not_contain_common_mojibake_markers() -> None:
    for path in [*PUBLIC_PAGES, *TEMPLATE_FILES, *DATA_FILES]:
        text = _read_text(path)
        assert not any(marker in text for marker in MOJIBAKE_MARKERS), (
            f"{path.relative_to(ROOT)} contains mojibake markers from broken UTF-8 text"
        )


@pytest.mark.smoke
def test_projects_include_exposes_tag_filter_hooks() -> None:
    text = _read_text(ROOT / "_includes" / "page_projects.html")
    for marker in ("data-tag-filter", "data-project-list", "data-tag-card", "data-tag-chip"):
        assert marker in text, (
            f"page_projects.html lost the '{marker}' hook the tag filter depends on"
        )


@pytest.mark.smoke
def test_tag_hub_pages_reuse_the_project_list() -> None:
    for path in (ROOT / "tags.html", ROOT / "en" / "tags.html"):
        assert "page_projects.html" in _read_text(path), (
            f"{path.relative_to(ROOT)} must render the shared project list to stay a real tag hub"
        )
