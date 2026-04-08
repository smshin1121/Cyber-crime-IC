"""
Wiki health check / lint tool.
Detects data consistency issues across all wiki pages.
"""
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import frontmatter

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"


def lint_all() -> list[dict[str, Any]]:
    """Run all lint checks and return list of issues."""
    issues: list[dict[str, Any]] = []

    all_pages = _load_all_pages()
    all_slugs = {p["slug"] for p in all_pages}

    for page in all_pages:
        # 1. source_count vs actual references
        issues.extend(_check_source_count(page))

        # 2. Reference numbering continuity
        issues.extend(_check_ref_numbering(page))

        # 3. Broken wikilinks
        issues.extend(_check_wikilinks(page, all_slugs))

        # 4. Missing dates in frontmatter
        issues.extend(_check_dates(page))

        # 5. Generic/placeholder titles in references
        issues.extend(_check_ref_titles(page))

        # 6. Empty required sections
        issues.extend(_check_empty_sections(page))

    # Cross-page checks
    issues.extend(_check_bidirectional_links(all_pages))

    return issues


def _load_all_pages() -> list[dict]:
    """Load all wiki pages with metadata and content."""
    pages = []
    for md in WIKI_DIR.rglob("*.md"):
        if md.name.startswith("_"):
            continue
        try:
            post = frontmatter.load(md)
            cat = md.parent.name if md.parent != WIKI_DIR else None
            pages.append({
                "path": md,
                "slug": md.stem,
                "category": cat,
                "meta": post.metadata,
                "content": post.content,
            })
        except Exception as e:
            pages.append({
                "path": md,
                "slug": md.stem,
                "category": None,
                "meta": {},
                "content": "",
                "parse_error": str(e),
            })
    return pages


def _check_source_count(page: dict) -> list[dict]:
    """Check source_count matches actual reference table rows."""
    issues = []
    meta = page["meta"]
    content = page["content"]
    declared = meta.get("source_count")
    if declared is None:
        return issues

    # Count reference rows
    actual = len(re.findall(r'^\|\s*\[\d+\]\s*\|', content, re.MULTILINE))

    if actual > 0 and actual != declared:
        issues.append({
            "severity": "HIGH",
            "type": "source_count_mismatch",
            "file": str(page["path"].relative_to(WIKI_DIR)),
            "detail": f"source_count={declared} but {actual} refs in table",
        })
    return issues


def _check_ref_numbering(page: dict) -> list[dict]:
    """Check reference numbers are sequential [1], [2], [3]..."""
    issues = []
    content = page["content"]
    refs = re.findall(r'^\|\s*\[(\d+)\]\s*\|', content, re.MULTILINE)
    if not refs:
        return issues

    nums = [int(r) for r in refs]
    expected = list(range(1, len(nums) + 1))
    if nums != expected:
        issues.append({
            "severity": "MEDIUM",
            "type": "ref_numbering",
            "file": str(page["path"].relative_to(WIKI_DIR)),
            "detail": f"Expected {expected} but got {nums}",
        })
    return issues


def _check_wikilinks(page: dict, all_slugs: set) -> list[dict]:
    """Check for wikilinks pointing to non-existent pages."""
    issues = []
    content = page["content"]
    links = re.findall(r'\[\[([^\]|]+)', content)
    for link in links:
        slug = link.strip().split("/")[-1]
        if slug not in all_slugs and slug != "_index":
            issues.append({
                "severity": "LOW",
                "type": "broken_wikilink",
                "file": str(page["path"].relative_to(WIKI_DIR)),
                "detail": f"[[{link}]] → no page found for '{slug}'",
            })
    return issues


def _check_dates(page: dict) -> list[dict]:
    """Check for missing created/updated dates."""
    issues = []
    meta = page["meta"]
    ptype = meta.get("type", "")
    if not ptype or ptype in ("overview", "category-index"):
        return issues
    if not meta.get("created"):
        issues.append({
            "severity": "LOW",
            "type": "missing_created",
            "file": str(page["path"].relative_to(WIKI_DIR)),
            "detail": "No 'created' date in frontmatter",
        })
    return issues


def _check_ref_titles(page: dict) -> list[dict]:
    """Check for generic/placeholder reference titles."""
    issues = []
    content = page["content"]
    generics = re.findall(
        r'^\|\s*\[\d+\]\s*\|\s*(Source \d+|N/A|Unknown|#\S+)\s*\|',
        content,
        re.MULTILINE,
    )
    if generics:
        issues.append({
            "severity": "MEDIUM",
            "type": "generic_ref_title",
            "file": str(page["path"].relative_to(WIKI_DIR)),
            "detail": f"Generic titles: {generics[:3]}",
        })
    return issues


def _check_empty_sections(page: dict) -> list[dict]:
    """Check for empty body sections."""
    issues = []
    content = page["content"]
    # Find ## headers followed by another ## header or end with nothing between
    empty = re.findall(
        r'^(## .+)\n+(?=## |\Z)',
        content,
        re.MULTILINE,
    )
    if empty:
        issues.append({
            "severity": "LOW",
            "type": "empty_section",
            "file": str(page["path"].relative_to(WIKI_DIR)),
            "detail": f"Empty sections: {[e.strip() for e in empty[:3]]}",
        })
    return issues


def _check_bidirectional_links(all_pages: list[dict]) -> list[dict]:
    """Spot-check bidirectional link consistency for operations."""
    issues = []
    ops = [p for p in all_pages if p["meta"].get("type") == "operation"]
    orgs = {
        p["slug"]: p for p in all_pages
        if p["meta"].get("type") == "organization"
    }

    for op in ops:
        meta = op["meta"]
        agencies = meta.get("participating_agencies", [])
        if not isinstance(agencies, list):
            continue
        for agency_ref in agencies:
            slug = str(agency_ref).strip("[]\"' ")
            if slug in orgs:
                org_meta = orgs[slug]["meta"]
                org_ops = org_meta.get("operations_participated", [])
                op_slug = op["slug"]
                if isinstance(org_ops, list):
                    org_ops_slugs = [str(o).strip("[]\"' ") for o in org_ops]
                    if op_slug not in org_ops_slugs:
                        issues.append({
                            "severity": "HIGH",
                            "type": "missing_backlink",
                            "file": str(orgs[slug]["path"].relative_to(WIKI_DIR)),
                            "detail": (
                                f"Operation [[{op_slug}]] lists [[{slug}]] as participant"
                                f" but org page lacks backlink"
                            ),
                        })
    return issues


def main() -> None:
    print("=" * 60)
    print("  Wiki Health Check (Lint)")
    print("=" * 60)

    issues = lint_all()

    by_severity = defaultdict(list)
    for issue in issues:
        by_severity[issue["severity"]].append(issue)

    for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        group = by_severity.get(sev, [])
        if group:
            print(f"\n  [{sev}] -{len(group)} issues")
            for i in group[:20]:
                print(f"    {i['type']}: {i['file']}")
                print(f"      {i['detail']}")
            if len(group) > 20:
                print(f"    ... and {len(group) - 20} more")

    total = len(issues)
    print(f"\n  Total issues: {total}")
    print(f"    CRITICAL: {len(by_severity.get('CRITICAL', []))}")
    print(f"    HIGH: {len(by_severity.get('HIGH', []))}")
    print(f"    MEDIUM: {len(by_severity.get('MEDIUM', []))}")
    print(f"    LOW: {len(by_severity.get('LOW', []))}")
    print("Done.")


if __name__ == "__main__":
    main()
