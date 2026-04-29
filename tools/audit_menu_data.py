from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
WORKSPACE = ROOT / "_workspace"

MENU_CATEGORIES = [
    "operations",
    "organizations",
    "countries",
    "cases",
    "legal-frameworks",
    "mechanisms",
    "crime-types",
    "concepts",
    "procedures",
    "challenges",
    "sources",
]

PLACEHOLDER_PATTERNS = (
    "structural placeholder",
    "to be expanded",
    "auto-created",
    "expand with verified sources",
    "should be expanded",
    "should be refined",
    "source-derived",
    "generated from",
)

REQUIRED_METADATA = {
    "operations": ("operation_role", "participating_countries", "source_count"),
    "organizations": ("org_type", "jurisdiction", "source_count"),
    "countries": ("legal_system", "ic_capacity", "treaty_memberships", "source_count"),
    "cases": ("source_count", "sources"),
    "legal-frameworks": ("framework_type", "status", "source_count"),
    "mechanisms": ("source_count",),
    "crime-types": ("source_count",),
    "concepts": ("source_count",),
    "procedures": ("source_count",),
    "challenges": ("source_count",),
    "sources": ("collection_url", "publisher", "source_type"),
}


@dataclass(frozen=True)
class MenuRow:
    category: str
    slug: str
    title: str
    score: int
    source_count: int
    reference_count: int
    body_words: int
    status: str
    issues: list[str]


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def wikilink_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        return text[2:-2].split("|", 1)[0].strip()
    return text


def word_count(text: str) -> int:
    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", r"\2 \1", text)
    text = re.sub(r"https?://\S+", " ", text)
    return len(re.findall(r"[A-Za-z0-9가-힣][A-Za-z0-9가-힣'(),./:%+-]*", text))


def strip_references(body: str) -> str:
    match = re.search(r"^## References\b", body, re.I | re.M)
    return body[: match.start()] if match else body


def count_reference_rows(body: str) -> int:
    match = re.search(r"^## References\b", body, re.I | re.M)
    tail = body[match.start() :] if match else body
    return len(re.findall(r"^\|\s*\[?\d+\]?\s*\|", tail, re.M))


def declared_source_count(meta: dict[str, Any]) -> int:
    try:
        return int(meta.get("source_count") or 0)
    except Exception:
        return 0


def source_slugs(meta: dict[str, Any]) -> list[str]:
    return [wikilink_slug(item) for item in as_list(meta.get("sources")) if wikilink_slug(item)]


def missing_required(meta: dict[str, Any], category: str) -> list[str]:
    missing: list[str] = []
    for key in REQUIRED_METADATA.get(category, ()):
        value = meta.get(key)
        if value in (None, "", [], {}):
            missing.append(key)
    return missing


def source_link_issues(meta: dict[str, Any]) -> list[str]:
    missing: list[str] = []
    for slug in source_slugs(meta):
        if slug.startswith("http"):
            continue
        if not (SOURCES_DIR / f"{slug}.md").exists():
            missing.append(slug)
    return missing


def is_absorbed_wrapper(meta: dict[str, Any]) -> bool:
    return str(meta.get("status") or "").strip().lower() == "absorbed"


def audit_page(path: Path, category: str) -> MenuRow:
    post = frontmatter.load(path)
    meta = post.metadata
    body = post.content or ""
    title = str(meta.get("title") or path.stem)
    status = str(meta.get("status") or "").strip().lower()
    body_without_refs = strip_references(body)
    body_words = word_count(body_without_refs)
    source_count = declared_source_count(meta)
    reference_count = count_reference_rows(body)
    lower_scan = f"{title}\n{body_without_refs}".lower()

    issues: list[str] = []
    score = 0

    if status == "stub":
        issues.append("status_stub")
        score += 50

    placeholder_hits = sum(lower_scan.count(pattern) for pattern in PLACEHOLDER_PATTERNS)
    if placeholder_hits:
        issues.append(f"placeholder_language:{placeholder_hits}")
        score += min(35, 15 + placeholder_hits * 5)

    if category != "sources" and not is_absorbed_wrapper(meta):
        if source_count == 0 and reference_count == 0:
            issues.append("no_sources")
            score += 20
        elif source_count == 0 and reference_count > 0:
            issues.append(f"source_count_missing_refs:{reference_count}")
            score += 12

        if body_words < 50:
            issues.append(f"very_thin_body:{body_words}")
            score += 20
        elif body_words < 140:
            issues.append(f"thin_body:{body_words}")
            score += 10

    if category == "sources":
        raw_path = str(meta.get("raw_path") or "").strip()
        collection_url = str(meta.get("collection_url") or meta.get("source_url") or meta.get("url") or "").strip()
        if not collection_url:
            issues.append("source_missing_collection_url")
            score += 20
        if raw_path and not (ROOT / raw_path).exists():
            issues.append("source_raw_path_missing_file")
            score += 15
        if not raw_path and body_words < 80:
            issues.append(f"source_thin_record:{body_words}")
            score += 12

    if reference_count and source_count and reference_count != source_count:
        issues.append(f"source_count_mismatch:{source_count}!={reference_count}")
        score += 10

    missing_meta = missing_required(meta, category)
    if missing_meta:
        issues.append("missing_metadata:" + ",".join(missing_meta))
        score += min(18, len(missing_meta) * 6)

    missing_sources = source_link_issues(meta)
    if missing_sources:
        issues.append("missing_source_pages:" + ",".join(missing_sources[:5]))
        score += min(20, len(missing_sources) * 5)

    if category in {"legal-frameworks", "mechanisms", "crime-types", "concepts"} and body_words < 220:
        issues.append(f"menu_core_page_underbuilt:{body_words}")
        score += 12

    if category == "countries" and status != "stub":
        unknowns = len(re.findall(r"\bunknown\b", body_without_refs, re.I))
        if unknowns >= 5:
            issues.append(f"country_many_unknowns:{unknowns}")
            score += min(12, unknowns)

    return MenuRow(
        category=category,
        slug=path.stem,
        title=title,
        score=score,
        source_count=source_count,
        reference_count=reference_count,
        body_words=body_words,
        status=status,
        issues=issues,
    )


def audit_all() -> list[MenuRow]:
    rows: list[MenuRow] = []
    for category in MENU_CATEGORIES:
        directory = WIKI_DIR / category
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name.startswith("_"):
                continue
            rows.append(audit_page(path, category))
    rows.sort(key=lambda row: (-row.score, row.category, row.slug))
    return rows


def render_report(rows: list[MenuRow], run_date: str) -> str:
    by_category = defaultdict(list)
    for row in rows:
        by_category[row.category].append(row)

    issue_counts = Counter(issue.split(":", 1)[0] for row in rows for issue in row.issues)
    high = [row for row in rows if row.score >= 50]
    medium = [row for row in rows if 25 <= row.score < 50]

    lines = [
        "---",
        f"title: Menu Data Audit ({run_date})",
        "type: analysis",
        f"created: {run_date}",
        f"updated: {run_date}",
        'summary: "Repository-wide audit of data quality for top navigation and supporting wiki menu categories."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This audit checks each menu category for structural stubs, placeholder prose, thin records, source/reference count mismatches, and missing core metadata. It complements the operation/case depth audit, organization audit, source corpus audit, link checker, and integrity audit.",
        "",
        f"- Pages audited: **{len(rows)}**",
        f"- High priority (`score >= 50`): **{len(high)}**",
        f"- Medium priority (`25-49`): **{len(medium)}**",
        "",
        "## Menu Summary",
        "",
        "| Menu | Pages | High | Medium | Top issue count |",
        "|---|---:|---:|---:|---:|",
    ]

    for category in MENU_CATEGORIES:
        cat_rows = by_category.get(category, [])
        cat_high = sum(1 for row in cat_rows if row.score >= 50)
        cat_medium = sum(1 for row in cat_rows if 25 <= row.score < 50)
        cat_issues = sum(len(row.issues) for row in cat_rows)
        lines.append(f"| {category} | {len(cat_rows)} | {cat_high} | {cat_medium} | {cat_issues} |")

    lines.extend(["", "## Issue Counts", "", "| Issue | Count |", "|---|---:|"])
    for issue, count in issue_counts.most_common():
        lines.append(f"| {issue} | {count} |")

    lines.extend(
        [
            "",
            "## Top 120 Queue",
            "",
            "| Rank | Page | Menu | Score | Sources | Refs | Body words | Issues |",
            "|---:|---|---|---:|---:|---:|---:|---|",
        ]
    )
    for idx, row in enumerate(rows[:120], start=1):
        issues = ", ".join(row.issues[:6])
        lines.append(
            f"| {idx} | [[{row.slug}]] | {row.category} | {row.score} | {row.source_count} | {row.reference_count} | {row.body_words} | {issues} |"
        )

    lines.extend(
        [
            "",
            "## Remediation Rules",
            "",
            "1. Treat top-navigation categories before supporting-only categories when scores tie.",
            "2. Replace structural stubs with source-backed summaries before adding new pages.",
            "3. Do not infer legal status, treaty participation, or agency authority without a cited source.",
            "4. Keep absorbed operation wrappers lightweight unless they need to carry unique evidence or procedural context.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_outputs(rows: list[MenuRow], run_date: str) -> None:
    WORKSPACE.mkdir(parents=True, exist_ok=True)
    json_path = WORKSPACE / f"menu_data_audit_{run_date}.json"
    csv_path = WORKSPACE / f"menu_data_audit_{run_date}.csv"
    report_path = WIKI_DIR / "analysis" / f"menu-data-audit-{run_date}.md"

    json_path.write_text(json.dumps([asdict(row) for row in rows], ensure_ascii=False, indent=2), encoding="utf-8")
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            data = asdict(row)
            data["issues"] = "; ".join(row.issues)
            writer.writerow(data)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(rows, run_date), encoding="utf-8")
    print(f"JSON: {json_path}")
    print(f"CSV: {csv_path}")
    print(f"Report: {report_path}")
    print(f"Audited {len(rows)} menu pages")
    print(f"High priority: {sum(1 for row in rows if row.score >= 50)}")
    print(f"Medium priority: {sum(1 for row in rows if 25 <= row.score < 50)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit data quality across wiki menu categories.")
    parser.add_argument("--date", default="2026-04-29")
    args = parser.parse_args()
    write_outputs(audit_all(), args.date)


if __name__ == "__main__":
    main()
