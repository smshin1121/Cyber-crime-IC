"""Audit public wiki outputs against the international-cooperation scope rule.

Public event records are limited to international-cooperation material. For
operations and cases, that means at least two real country slugs in structured
metadata. This audit checks that generated/public surfaces do not expose
non-qualifying operations, cases, or sources.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
DOCS_DIR = ROOT / "docs"
TOOLS_DIR = ROOT / "tools"

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from ic_scope import country_count, public_wiki_include  # noqa: E402
from operation_scope import operation_scope  # noqa: E402

CATEGORIES = {
    "operations": "operation",
    "cases": "case",
    "sources": "source",
}

INDEX_ROW_RE = re.compile(r"^\|.*?\[\[([^\]|#]+)", re.M)


def load_meta(path: Path) -> dict[str, Any]:
    try:
        return dict(frontmatter.load(path).metadata)
    except Exception:
        return {}


@lru_cache(maxsize=None)
def wiki_files(category: str) -> dict[str, tuple[Path, dict[str, Any]]]:
    cat_dir = WIKI_DIR / category
    rows: dict[str, tuple[Path, dict[str, Any]]] = {}
    if not cat_dir.is_dir():
        return rows
    for path in sorted(cat_dir.glob("*.md")):
        if path.name.startswith("_"):
            continue
        rows[path.stem] = (path, load_meta(path))
    return rows


def public_slugs(category: str) -> set[str]:
    out: set[str] = set()
    for slug, (path, meta) in wiki_files(category).items():
        if public_wiki_include(path, meta, WIKI_DIR):
            out.add(slug)
    return out


def category_index_slugs(category: str) -> set[str]:
    path = WIKI_DIR / category / "_index.md"
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8", errors="replace")
    return {match.group(1).strip() for match in INDEX_ROW_RE.finditer(text)}


def docs_html_slugs(category: str) -> set[str]:
    docs_dir = DOCS_DIR / "wiki" / category
    if not docs_dir.is_dir():
        return set()
    return {path.stem for path in docs_dir.glob("*.html")}


def search_index_slugs(category: str) -> set[str]:
    path = DOCS_DIR / "search-index.json"
    if not path.exists():
        return set()
    rows = json.loads(path.read_text(encoding="utf-8"))
    return {
        str(row.get("slug") or "")
        for row in rows
        if row.get("category") == category and row.get("slug")
    }


def cosmos_slugs(page_type: str) -> set[str]:
    path = ROOT / "cosmos" / "data.json"
    if not path.exists():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    return {
        str(node.get("id") or "")
        for node in data.get("nodes", [])
        if node.get("type") == page_type and node.get("id")
    }


def compare_surface(
    category: str,
    label: str,
    actual: set[str],
    expected: set[str],
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    extra = sorted(actual - expected)
    missing = sorted(expected - actual)
    if extra:
        issues.append({
            "category": category,
            "surface": label,
            "kind": "non_public_slugs_visible",
            "count": len(extra),
            "sample": extra[:20],
        })
    if missing:
        issues.append({
            "category": category,
            "surface": label,
            "kind": "public_slugs_missing",
            "count": len(missing),
            "sample": missing[:20],
        })
    return issues


def audit_event_country_threshold(
    category: str,
    public_records: set[str],
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    files = wiki_files(category)
    bad: list[str] = []
    for slug in sorted(public_records):
        path, meta = files[slug]
        if country_count(meta, WIKI_DIR) < 2:
            bad.append(slug)
    if bad:
        issues.append({
            "category": category,
            "surface": "scope",
            "kind": "public_event_country_count_lt_2",
            "count": len(bad),
            "sample": bad[:20],
        })
    return issues


def main() -> int:
    issues: list[dict[str, Any]] = []
    expected_by_category: dict[str, set[str]] = {}

    for category, page_type in CATEGORIES.items():
        expected = public_slugs(category)
        expected_by_category[category] = expected
        surfaces = {
            "wiki_index": category_index_slugs(category),
            "docs_html": docs_html_slugs(category),
            "search_index": search_index_slugs(category),
            "cosmos": cosmos_slugs(page_type),
        }
        for label, actual in surfaces.items():
            issues.extend(compare_surface(category, label, actual, expected))

    for event_category in ("operations", "cases"):
        issues.extend(
            audit_event_country_threshold(
                event_category,
                expected_by_category[event_category],
            )
        )

    op_files = wiki_files("operations")
    scope_counts = Counter()
    for slug in expected_by_category["operations"]:
        _path, meta = op_files[slug]
        scope_counts[operation_scope(meta)] += 1

    print("tools/audit_public_ic_scope.py")
    for category in CATEGORIES:
        total = len(wiki_files(category))
        public = len(expected_by_category[category])
        print(f"  {category}: public {public} / total {total} / excluded {total - public}")
    print(f"  public operation scopes: {dict(sorted(scope_counts.items()))}")

    if issues:
        print("\n  Scope violations:")
        for issue in issues:
            print(
                "  - {category}:{surface}:{kind} count={count} sample={sample}".format(
                    **issue
                )
            )
        return 1

    print("  result: OK - no non-IC records are exposed on public wiki surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
