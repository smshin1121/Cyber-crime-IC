from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import frontmatter

import audit_content_depth as depth


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
WORKSPACE = ROOT / "_workspace"
REPORT_DIR = ROOT / "wiki" / "analysis"
DEFAULT_DATE = "2026-04-27"


def is_absorbed(meta: dict[str, Any]) -> bool:
    return str(meta.get("status") or "").strip().lower() == "absorbed"


def issue_text(row: depth.DepthRow) -> str:
    return "; ".join(row.issues)


def recommendation(row: depth.DepthRow) -> str:
    issues = issue_text(row)
    if row.source_count < 5:
        return "raise_source_floor_then_enrich"
    if "raw_available_underused" in issues:
        return "enrich_from_existing_raw_sources"
    if "high_source_to_body_gap" in issues:
        return "expand_source_backed_operation_detail"
    if "possible_crime_type_mismatch" in issues:
        return "manual_taxonomy_review_after_enrichment"
    return "canonical_refresh_from_existing_sources"


def sort_key(row: depth.DepthRow) -> tuple[int, int, int, int, str]:
    issues = issue_text(row)
    needs_raw = 1 if "raw_available_underused" in issues else 0
    gap = 1 if "high_source_to_body_gap" in issues else 0
    low_source = 1 if row.source_count < 5 else 0
    return (-low_source, -needs_raw, -gap, -row.source_words, row.slug)


def collect_rows() -> list[depth.DepthRow]:
    rows: list[depth.DepthRow] = []
    for path in sorted(OPS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        try:
            meta = frontmatter.load(path).metadata
        except Exception as exc:
            print(f"skip parse error: {path}: {exc}", file=sys.stderr)
            continue
        if is_absorbed(meta):
            continue
        rows.append(depth.audit_page(path, "operations"))
    return sorted(rows, key=sort_key)


def write_csv(rows: list[depth.DepthRow], path: Path) -> None:
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
                    row.category,
                    row.slug,
                    row.title,
                    row.score,
                    row.source_count,
                    row.references_count,
                    row.body_words,
                    row.source_words,
                    recommendation(row),
                    issue_text(row),
                ]
            )


def write_json(rows: list[depth.DepthRow], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "rows": [
                    {
                        "category": row.category,
                        "slug": row.slug,
                        "title": row.title,
                        "score": row.score,
                        "source_count": row.source_count,
                        "references_count": row.references_count,
                        "body_words": row.body_words,
                        "source_words": row.source_words,
                        "recommendation": recommendation(row),
                        "issues": row.issues,
                    }
                    for row in rows
                ]
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def render_report(rows: list[depth.DepthRow], run_date: str) -> str:
    issue_counts: Counter[str] = Counter()
    rec_counts: Counter[str] = Counter()
    for row in rows:
        rec_counts[recommendation(row)] += 1
        for issue in row.issues:
            issue_counts[issue.split(":", 1)[0]] += 1

    lines = [
        "---",
        f"title: Canonical Operation Enrichment Queue ({run_date})",
        "type: analysis",
        f"created: {run_date}",
        f"updated: {run_date}",
        'summary: "Full canonical-operation queue for source-backed content enrichment."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This queue covers every non-absorbed operation page. Absorbed follow-on wrappers are excluded so the pass enriches canonical operation records only.",
        "",
        f"- Canonical operation rows: **{len(rows)}**",
        f"- Rows with content-depth issues: **{sum(1 for row in rows if row.issues)}**",
        f"- Rows below 5-source floor: **{sum(1 for row in rows if row.source_count < 5)}**",
        f"- Rows with source/body gap: **{sum(1 for row in rows if 'high_source_to_body_gap' in issue_text(row))}**",
        f"- Rows with underused raw/source text: **{sum(1 for row in rows if 'raw_available_underused' in issue_text(row))}**",
        "",
        "## Recommendation Counts",
        "",
        "| Recommendation | Count |",
        "|---|---:|",
    ]
    for rec, count in sorted(rec_counts.items()):
        lines.append(f"| {rec} | {count} |")

    if issue_counts:
        lines.extend(["", "## Issue Counts", "", "| Issue | Count |", "|---|---:|"])
        for issue, count in sorted(issue_counts.items()):
            lines.append(f"| {issue} | {count} |")

    lines.extend(
        [
            "",
            "## Full Queue",
            "",
            "| Rank | Page | Sources | Body words | Source words | Recommendation | Issues |",
            "|---:|---|---:|---:|---:|---|---|",
        ]
    )
    for idx, row in enumerate(rows, 1):
        issues = issue_text(row) or "-"
        lines.append(
            f"| {idx} | [[{row.slug}]] | {row.source_count} | {row.body_words} | {row.source_words} | {recommendation(row)} | {issues} |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a full enrichment queue for canonical operation pages.")
    parser.add_argument("--date", default=DEFAULT_DATE)
    parser.add_argument("--csv", default="")
    parser.add_argument("--json", default="")
    parser.add_argument("--report", default="")
    args = parser.parse_args()

    rows = collect_rows()
    csv_path = ROOT / (args.csv or f"_workspace/canonical_operation_enrichment_queue_{args.date}.csv")
    json_path = ROOT / (args.json or f"_workspace/canonical_operation_enrichment_queue_{args.date}.json")
    report_path = ROOT / (args.report or f"wiki/analysis/canonical-operation-enrichment-queue-{args.date}.md")

    write_csv(rows, csv_path)
    write_json(rows, json_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(rows, args.date), encoding="utf-8", newline="\n")

    print(f"Canonical operation rows: {len(rows)}")
    print(f"CSV: {csv_path}")
    print(f"JSON: {json_path}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
