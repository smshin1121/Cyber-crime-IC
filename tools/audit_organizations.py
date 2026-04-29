from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
ORG_DIR = ROOT / "wiki" / "organizations"
WORKSPACE = ROOT / "_workspace"
ANALYSIS_DIR = ROOT / "wiki" / "analysis"
DEFAULT_DATE = "2026-04-29"

PLACEHOLDER_PATTERNS = (
    "structural placeholder",
    "created during the",
    "expand with verified sources",
    "placeholder for",
    "stub",
)


@dataclass(frozen=True)
class OrgRow:
    slug: str
    title: str
    status: str
    org_type: str
    source_count: int
    sources_len: int
    operations_len: int
    partners_len: int
    roles_len: int
    mechanisms_len: int
    body_words: int
    has_references: bool
    score: int
    issues: list[str]


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def int_value(value: Any) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def word_count(text: str) -> int:
    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", r"\2 \1", text)
    text = re.sub(r"https?://\S+", " ", text)
    return len(re.findall(r"[A-Za-z0-9가-힣][A-Za-z0-9가-힣'’.,:%/+-]*", text))


def audit_org(path: Path) -> OrgRow:
    post = frontmatter.load(path)
    meta = post.metadata
    body = post.content or ""
    lower = body.lower()
    title = str(meta.get("title") or path.stem)
    status = str(meta.get("status") or "").strip()
    org_type = str(meta.get("org_type") or "").strip()
    source_count = int_value(meta.get("source_count"))
    sources_len = len(as_list(meta.get("sources")))
    operations_len = len(as_list(meta.get("operations_participated")))
    partners_len = len(as_list(meta.get("cooperation_partners")))
    roles_len = len(as_list(meta.get("key_roles")))
    mechanisms_len = len(as_list(meta.get("mechanisms_operated")))
    body_words = word_count(body)
    has_references = "## References" in body

    score = 0
    issues: list[str] = []
    if status.lower() == "stub":
        score += 35
        issues.append("status_stub")
    if source_count == 0 and sources_len == 0:
        score += 25
        issues.append("no_sources")
    elif source_count < 2 and sources_len < 2:
        score += 10
        issues.append("low_sources")
    if body_words < 120:
        score += 20
        issues.append(f"thin_body:{body_words}")
    elif body_words < 300:
        score += 8
        issues.append(f"moderate_body:{body_words}")
    if any(pattern in lower for pattern in PLACEHOLDER_PATTERNS):
        score += 15
        issues.append("placeholder_language")
    if not has_references:
        score += 8
        issues.append("missing_references_section")
    if not org_type:
        score += 6
        issues.append("missing_org_type")
    if operations_len == 0:
        score += 6
        issues.append("no_operation_backlinks")
    if roles_len == 0 and mechanisms_len == 0:
        score += 6
        issues.append("thin_role_metadata")
    if partners_len == 0:
        score += 2
        issues.append("no_partner_metadata")

    return OrgRow(
        slug=path.stem,
        title=title,
        status=status,
        org_type=org_type,
        source_count=source_count,
        sources_len=sources_len,
        operations_len=operations_len,
        partners_len=partners_len,
        roles_len=roles_len,
        mechanisms_len=mechanisms_len,
        body_words=body_words,
        has_references=has_references,
        score=score,
        issues=issues,
    )


def audit_all() -> list[OrgRow]:
    return [
        audit_org(path)
        for path in sorted(ORG_DIR.glob("*.md"))
        if not path.name.startswith("_")
    ]


def render_report(rows: list[OrgRow], run_date: str) -> str:
    ordered = sorted(rows, key=lambda row: (-row.score, row.slug))
    high = [row for row in rows if row.score >= 45]
    medium = [row for row in rows if 20 <= row.score < 45]
    issue_counts = Counter(issue.split(":", 1)[0] for row in rows for issue in row.issues)

    lines = [
        "---",
        f"title: Organization Content Audit ({run_date})",
        "type: analysis",
        f"created: {run_date}",
        f"updated: {run_date}",
        'summary: "Audit of organization pages for stubs, source coverage, role metadata, and operation backlinks."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        f"- Organization pages audited: **{len(rows)}**",
        f"- High priority (`score >= 45`): **{len(high)}**",
        f"- Medium priority (`20-44`): **{len(medium)}**",
        f"- Stub pages: **{sum(1 for row in rows if row.status.lower() == 'stub')}**",
        f"- Pages without source metadata: **{sum(1 for row in rows if row.source_count == 0 and row.sources_len == 0)}**",
        f"- Pages without operation backlinks: **{sum(1 for row in rows if row.operations_len == 0)}**",
        "",
        "## Issue Counts",
        "",
        "| Issue | Count |",
        "|---|---:|",
    ]
    for issue, count in issue_counts.most_common():
        lines.append(f"| {issue} | {count} |")

    lines.extend(
        [
            "",
            "## Top 100 Priority Queue",
            "",
            "| Rank | Organization | Score | Sources | Operations | Body words | Issues |",
            "|---:|---|---:|---:|---:|---:|---|",
        ]
    )
    for idx, row in enumerate(ordered[:100], 1):
        issues = ", ".join(row.issues)
        lines.append(
            f"| {idx} | [[{row.slug}]] | {row.score} | {max(row.source_count, row.sources_len)} | {row.operations_len} | {row.body_words} | {issues} |"
        )
    return "\n".join(lines) + "\n"


def write_outputs(rows: list[OrgRow], run_date: str) -> None:
    WORKSPACE.mkdir(parents=True, exist_ok=True)
    json_path = WORKSPACE / f"organization_content_audit_{run_date}.json"
    csv_path = WORKSPACE / f"organization_content_audit_{run_date}.csv"
    report_path = ANALYSIS_DIR / f"organization-content-audit-{run_date}.md"

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


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit organization wiki page depth and metadata.")
    parser.add_argument("--date", default=DEFAULT_DATE)
    args = parser.parse_args()
    rows = audit_all()
    write_outputs(rows, args.date)
    print(f"Audited {len(rows)} organization pages")
    print(f"High priority: {sum(1 for row in rows if row.score >= 45)}")
    print(f"Medium priority: {sum(1 for row in rows if 20 <= row.score < 45)}")


if __name__ == "__main__":
    main()
