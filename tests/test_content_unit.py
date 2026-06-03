from __future__ import annotations

from pathlib import Path
import re

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_FILE = ROOT / "_data" / "projects.yml"
ARTICLES_DIR = ROOT / "_articles"
ARTICLE_FILES = sorted(ARTICLES_DIR.rglob("*.md"))


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _front_matter(path: Path) -> dict:
    text = _read_text(path)
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    assert match, f"{path.relative_to(ROOT)} must start with YAML front matter"
    data = yaml.safe_load(match.group(1))
    assert isinstance(data, dict), f"{path.relative_to(ROOT)} front matter must be a mapping"
    return data


def _projects() -> list[dict]:
    data = yaml.safe_load(_read_text(PROJECTS_FILE))
    assert isinstance(data, list), "_data/projects.yml must contain a list of projects"
    return data


def _articles() -> list[tuple[Path, dict]]:
    return [(path, _front_matter(path)) for path in ARTICLE_FILES]


@pytest.mark.unit
def test_project_slugs_are_unique() -> None:
    slugs = [project["slug"] for project in _projects()]
    assert len(slugs) == len(set(slugs)), "Project slugs must stay unique"


@pytest.mark.unit
def test_projects_have_required_contract_fields() -> None:
    for project in _projects():
        assert project.get("slug"), "Each project needs a slug"
        assert project.get("name"), f"{project!r} must have a machine-readable name"
        assert project.get("title"), f"{project!r} must have a public title"
        assert project.get("description"), f"{project['slug']} must have a description"
        assert isinstance(project.get("stack"), list) and project["stack"], (
            f"{project['slug']} must declare a non-empty stack"
        )
        assert project.get("repo") or project.get("demo"), (
            f"{project['slug']} must have at least one public link"
        )
        for key in ("repo", "demo"):
            if project.get(key):
                assert str(project[key]).startswith("https://"), (
                    f"{project['slug']} {key} link must use https"
                )
        if project.get("repo_label"):
            assert project.get("repo"), f"{project['slug']} repo_label needs a repo URL"
        if project.get("demo_label"):
            assert project.get("demo"), f"{project['slug']} demo_label needs a demo URL"


@pytest.mark.unit
def test_articles_reference_existing_projects() -> None:
    known_projects = {project["slug"] for project in _projects()}
    for path, meta in _articles():
        assert meta.get("project") in known_projects, (
            f"{path.relative_to(ROOT)} points to an unknown project slug"
        )


@pytest.mark.unit
def test_articles_have_required_metadata() -> None:
    for path, meta in _articles():
        for field in ("title", "project", "date", "lang", "summary", "tags"):
            assert meta.get(field), f"{path.relative_to(ROOT)} is missing '{field}'"
        assert meta["lang"] in {"ru", "en"}, (
            f"{path.relative_to(ROOT)} has unsupported lang '{meta['lang']}'"
        )
        assert isinstance(meta["tags"], list) and meta["tags"], (
            f"{path.relative_to(ROOT)} must keep a non-empty tags list"
        )


@pytest.mark.unit
def test_translation_links_point_to_existing_articles() -> None:
    article_names = {path.name for path in ARTICLE_FILES}
    for path, meta in _articles():
        source = meta.get("translation_of")
        if source:
            assert source in article_names, (
                f"{path.relative_to(ROOT)} points to missing translation source '{source}'"
            )

