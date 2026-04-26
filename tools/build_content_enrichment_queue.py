from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT / "_workspace"
REPORT_PATH = ROOT / "wiki" / "analysis" / "content-enrichment-queue-2026-04-26.md"


def has_issue(row: dict[str, Any], prefix: str) -> bool:
    return any(str(issue).startswith(prefix) for issue in row.get("issues", []))


def recommendation(row: dict[str, Any]) -> str:
    if has_issue(row, "duplicate_source_url_refs"):
        return "dedupe_same_url_references_then_enrich"
    if has_issue(row, "source_rich_thin_body") and row.get("source_words", 0) >= 1200:
        return "enrich_from_existing_raw_sources"
    if row.get("placeholder_hits", 0):
        return "replace_placeholder_or_absorb_wrapper"
    if has_issue(row, "possible_crime_type_mismatch"):
        return "manual_crime_type_review"
    return "manual_review"


def load_rows(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return list(data.get("rows") or data.get("pages") or [])
    return list(data)


def sort_key(row: dict[str, Any]) -> tuple[int, int, int, str]:
    source_rich = 1 if has_issue(row, "source_rich_thin_body") else 0
    return (
        -int(row.get("score") or 0),
        -source_rich,
        -int(row.get("source_words") or 0),
        str(row.get("slug") or ""),
    )


def select_rows(rows: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    candidates = [
        row
        for row in rows
        if int(row.get("score") or 0) >= 45
        or has_issue(row, "source_rich_thin_body")
        or has_issue(row, "duplicate_source_url_refs")
    ]
    return sorted(candidates, key=sort_key)[:limit]


def write_csv(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "rank",
                "category",
                "slug",
                "title",
                "score",
                "source_count",
                "references_count",
                "body_words",
                "source_words",
                "recommendation",
                "issues",
            ]
        )
        for idx, row in enumerate(rows, 1):
            writer.writerow(
                [
                    idx,
                    row.get("category", ""),
                    row.get("slug", ""),
                    row.get("title", ""),
                    row.get("score", 0),
                    row.get("source_count", 0),
                    row.get("references_count", 0),
                    row.get("body_words", 0),
                    row.get("source_words", 0),
                    recommendation(row),
                    "; ".join(row.get("issues", [])),
                ]
            )


def render_report(rows: list[dict[str, Any]], total_rows: int) -> str:
    lines = [
        "---",
        "title: Content Enrichment Queue (2026-04-26)",
        "type: analysis",
        "created: 2026-04-26",
        "updated: 2026-04-26",
        'summary: "Prioritized queue for enriching source-rich, thin, placeholder, or duplicate-reference operation and case pages."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This queue converts the content-depth audit into an execution list. It is ordered to fix pages where existing sources already contain enough material before searching for new sources.",
        "",
        f"- Audited operation/case pages: **{total_rows}**",
        f"- Queue size: **{len(rows)}**",
        "",
        "## Top Queue",
        "",
        "| Rank | Page | Type | Score | Sources | Body words | Source words | Recommendation | Issues |",
        "|---:|---|---|---:|---:|---:|---:|---|---|",
    ]
    for idx, row in enumerate(rows, 1):
        issues = ", ".join(row.get("issues", [])[:5])
        lines.append(
            f"| {idx} | [[{row.get('slug', '')}]] | {str(row.get('category', ''))[:-1]} | {row.get('score', 0)} | {row.get('source_count', 0)} | {row.get('body_words', 0)} | {row.get('source_words', 0)} | {recommendation(row)} | {issues} |"
        )

    lines.extend(
        [
            "",
            "## Execution Rules",
            "",
            "1. Fix `duplicate_source_url_refs` before counting a page as source-rich.",
            "2. For `enrich_from_existing_raw_sources`, use already collected raw/source text first.",
            "3. For `replace_placeholder_or_absorb_wrapper`, decide whether the page is a real case/operation or a wrapper that should point to a canonical record.",
            "4. For `manual_crime_type_review`, do not change taxonomy without source-backed review.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a prioritized content enrichment queue from content-depth audit JSON.")
    parser.add_argument("--input", default="_workspace/content_depth_audit_2026-04-26.json")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--csv", default="_workspace/content_enrichment_queue_2026-04-26.csv")
    parser.add_argument("--report", default=str(REPORT_PATH.relative_to(ROOT)))
    args = parser.parse_args()

    input_path = ROOT / args.input
    rows = load_rows(input_path)
    queue = select_rows(rows, args.limit)
    csv_path = ROOT / args.csv
    report_path = ROOT / args.report
    write_csv(queue, csv_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(queue, len(rows)), encoding="utf-8")
    print(f"CSV: {csv_path}")
    print(f"Report: {report_path}")
    print(f"Audited pages: {len(rows)}")
    print(f"Queue size: {len(queue)}")


if __name__ == "__main__":
    main()
