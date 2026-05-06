"""International-cooperation visibility rules for the public wiki.

The public corpus is scoped to records with at least two real countries.
Operation files remain in the repository for traceability, but public indexes,
search, statistics, and graph exports should only include records that meet
this rule or directly support a qualifying operation.
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import frontmatter

PSEUDO_COUNTRY_SLUGS = {
    "international",
    "global",
    "worldwide",
    "european-union",
}

_LINK_RE = re.compile(r"\[\[([^\]|#]+)")


def normalize_slug(value: Any) -> str:
    text = str(value or "").strip().strip("\"'")
    match = _LINK_RE.search(text)
    if match:
        text = match.group(1)
    else:
        text = text.split("|", 1)[0]
    text = text.replace("\\", "/").split("/")[-1]
    if text.endswith(".md"):
        text = text[:-3]
    return text.strip()


@lru_cache(maxsize=None)
def valid_country_slugs(wiki_dir_text: str) -> frozenset[str]:
    countries_dir = Path(wiki_dir_text) / "countries"
    if not countries_dir.is_dir():
        return frozenset()
    return frozenset(
        path.stem
        for path in countries_dir.glob("*.md")
        if not path.name.startswith("_") and path.stem not in PSEUDO_COUNTRY_SLUGS
    )


def _as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, "", {}):
        return []
    return [value]


def country_slugs(meta: dict[str, Any], wiki_dir: Path) -> set[str]:
    valid = valid_country_slugs(str(wiki_dir))
    found: set[str] = set()
    for field in ("participating_countries", "jurisdictions"):
        for item in _as_list(meta.get(field)):
            slug = normalize_slug(item)
            if slug in valid:
                found.add(slug)
    for item in _as_list(meta.get("jurisdiction_country")):
        slug = normalize_slug(item)
        if slug in valid:
            found.add(slug)
    return found


def country_count(meta: dict[str, Any], wiki_dir: Path) -> int:
    return len(country_slugs(meta, wiki_dir))


def is_international_operation(meta: dict[str, Any], wiki_dir: Path) -> bool:
    return country_count(meta, wiki_dir) >= 2


@lru_cache(maxsize=None)
def _operation_is_public(wiki_dir_text: str, slug: str) -> bool:
    path = Path(wiki_dir_text) / "operations" / f"{slug}.md"
    if not path.exists():
        return False
    try:
        meta = dict(frontmatter.load(path).metadata)
    except Exception:
        return False
    return is_international_operation(meta, Path(wiki_dir_text))


def _linked_operation_slugs(meta: dict[str, Any]) -> set[str]:
    slugs: set[str] = set()
    for field in ("related_operation", "related_operations", "parent_operation"):
        for item in _as_list(meta.get(field)):
            slug = normalize_slug(item)
            if slug:
                slugs.add(slug)
    return slugs


def is_international_case(meta: dict[str, Any], wiki_dir: Path) -> bool:
    if country_count(meta, wiki_dir) >= 2:
        return True
    return any(_operation_is_public(str(wiki_dir), slug) for slug in _linked_operation_slugs(meta))


@lru_cache(maxsize=None)
def _public_source_slugs(wiki_dir_text: str) -> frozenset[str]:
    wiki_dir = Path(wiki_dir_text)
    source_slugs: set[str] = set()
    for category in ("operations", "cases"):
        cat_dir = wiki_dir / category
        if not cat_dir.is_dir():
            continue
        for path in cat_dir.glob("*.md"):
            if path.name.startswith("_"):
                continue
            try:
                meta = dict(frontmatter.load(path).metadata)
            except Exception:
                continue
            if category == "operations":
                include = is_international_operation(meta, wiki_dir)
            else:
                include = is_international_case(meta, wiki_dir)
            if not include:
                continue
            for item in _as_list(meta.get("sources")):
                slug = normalize_slug(item)
                if slug:
                    source_slugs.add(slug)
    return frozenset(source_slugs)


def is_public_source(slug: str, wiki_dir: Path) -> bool:
    return slug in _public_source_slugs(str(wiki_dir))


def public_wiki_include(path: Path, meta: dict[str, Any], wiki_dir: Path) -> bool:
    """Return True when a page belongs in public wiki indexes/exports."""
    try:
        rel = path.relative_to(wiki_dir)
    except ValueError:
        return True
    if len(rel.parts) < 2:
        return True
    category = rel.parts[0]
    if category == "operations":
        return is_international_operation(meta, wiki_dir)
    if category == "cases":
        return is_international_case(meta, wiki_dir)
    if category == "sources":
        return is_public_source(path.stem, wiki_dir)
    return True
