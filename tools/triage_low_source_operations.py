from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
import re

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
OUT_DIR = ROOT / "wiki" / "analysis"
OUT_PATH = OUT_DIR / "operation-low-source-triage-2026-04-22.md"
MIN_SOURCES = 5

FOLLOW_ON_HINTS = (
    "sentenced",
    "pleads guilty",
    "pleaded guilty",
    "indicted",
    "charged",
    "convicted",
    "arraigned",
    "extradited",
)


@dataclass(frozen=True)
class TriageRow:
    slug: str
    title: str
    status: str
    source_count: int | None
    references_count: int
    operation_role: str
    countries: int
    related_cases: int
    related_operations: int
    parent_operation: str
    bucket: str
    notes: tuple[str, ...]


def load_paths() -> list[Path]:
    return [p for p in sorted(OPS_DIR.glob("*.md")) if p.name != "_index.md"]


def count_references(body: str) -> int:
    if "## References" not in body:
        return 0
    tail = body.split("## References", 1)[1]
    return len(re.findall(r"^\|\s*\[?\d+\]?\s*\|", tail, re.M))


def _as_list(value: object) -> list[object]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def title_looks_procedural(title: str) -> bool:
    lower = title.lower()
    return any(hint in lower for hint in FOLLOW_ON_HINTS)


def classify(post: frontmatter.Post, slug: str, body: str, refs: int) -> TriageRow:
    meta = post.metadata
    title = str(meta.get("title") or slug)
    status = str(meta.get("status") or "")
    source_count_raw = meta.get("source_count")
    source_count = int(source_count_raw) if source_count_raw not in (None, "") else None
    operation_role = str(meta.get("operation_role") or "")
    countries = len(_as_list(meta.get("participating_countries")))
    related_cases = len(_as_list(meta.get("related_cases")))
    related_operations = len(_as_list(meta.get("related_operations")))
    parent_operation = str(meta.get("parent_operation") or "")
    notes: list[str] = []

    if status == "absorbed":
        return TriageRow(
            slug, title, status, source_count, refs, operation_role, countries,
            related_cases, related_operations, parent_operation, "absorbed", tuple(notes)
        )

    if source_count is None:
        notes.append("missing_source_count")
    elif source_count != refs:
        notes.append(f"source_count_mismatch:{source_count}!={refs}")

    if refs == 0:
        notes.append("missing_visible_references")

    if source_count is not None and source_count >= MIN_SOURCES:
        bucket = "metadata_repair" if notes else "meets_threshold"
        return TriageRow(
            slug, title, status, source_count, refs, operation_role, countries,
            related_cases, related_operations, parent_operation, bucket, tuple(notes)
        )

    if operation_role == "follow-on" and related_cases and countries <= 1:
        bucket = "merge_into_case"
        notes.append("follow_on_with_case_anchor")
    elif operation_role == "follow-on" and parent_operation:
        bucket = "merge_into_parent"
        notes.append("follow_on_with_parent_operation")
    elif slug.startswith("operation-us-v-") and related_cases:
        bucket = "merge_into_case"
        notes.append("operation_us_v_case_duplicate")
    elif title_looks_procedural(title) and related_cases:
        bucket = "merge_into_case"
        notes.append("procedural_title_with_case_anchor")
    elif countries >= 2 and operation_role == "umbrella":
        bucket = "retain_and_enrich"
        notes.append("multinational_umbrella")
    elif countries >= 2:
        bucket = "retain_and_enrich"
        notes.append("multinational_but_thin")
    elif notes:
        bucket = "metadata_repair"
    else:
        bucket = "high_risk_review"
        if countries <= 1:
            notes.append("single_country_low_source")
        if title_looks_procedural(title):
            notes.append("procedural_title")

    return TriageRow(
        slug, title, status, source_count, refs, operation_role, countries,
        related_cases, related_operations, parent_operation, bucket, tuple(notes)
    )


def render(rows: list[TriageRow]) -> str:
    triaged = [r for r in rows if r.bucket not in {"meets_threshold", "absorbed"}]
    by_bucket: dict[str, list[TriageRow]] = defaultdict(list)
    for row in triaged:
        by_bucket[row.bucket].append(row)

    counts = Counter(row.bucket for row in triaged)

    lines = [
        "---",
        "title: Operation Low-Source Triage (2026-04-22)",
        "type: analysis",
        "created: 2026-04-22",
        "updated: 2026-04-22",
        'summary: "Repository-wide triage of operation pages below the 5-source minimum, grouped into merge, enrich, repair, and manual-review buckets."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This report classifies operation pages that remain below the `5`-source minimum into action buckets rather than treating every low-source page the same way.",
        "",
        "## Bucket Counts",
        "",
        f"- merge_into_case: **{counts['merge_into_case']}**",
        f"- merge_into_parent: **{counts['merge_into_parent']}**",
        f"- retain_and_enrich: **{counts['retain_and_enrich']}**",
        f"- metadata_repair: **{counts['metadata_repair']}**",
        f"- high_risk_review: **{counts['high_risk_review']}**",
        "",
        "## Bucket Meanings",
        "",
        "- `merge_into_case`: operation page is likely a thin follow-on wrapper around an existing case page.",
        "- `merge_into_parent`: operation page looks subordinate to a stronger parent operation and probably should not stand alone.",
        "- `retain_and_enrich`: operation appears materially multinational or umbrella-like, but does not yet meet the source threshold.",
        "- `metadata_repair`: `source_count` or `## References` is missing, inconsistent, or structurally broken.",
        "- `high_risk_review`: page does not clearly qualify for retention or merger and should be reviewed manually before trust is implied.",
        "",
    ]

    showcase_order = [
        "merge_into_case",
        "merge_into_parent",
        "retain_and_enrich",
        "metadata_repair",
        "high_risk_review",
    ]
    limits = {
        "merge_into_case": 40,
        "merge_into_parent": 25,
        "retain_and_enrich": 40,
        "metadata_repair": 25,
        "high_risk_review": 40,
    }

    for bucket in showcase_order:
        items = sorted(
            by_bucket[bucket],
            key=lambda r: (
                999 if r.source_count is None else r.source_count,
                r.countries,
                r.slug,
            ),
        )
        lines.extend(
            [
                f"## {bucket}",
                "",
                f"Count: **{len(items)}**",
                "",
                "| Operation | Sources | Refs | Role | Countries | Notes |",
                "|---|---:|---:|---|---:|---|",
            ]
        )
        for row in items[:limits[bucket]]:
            sc = "?" if row.source_count is None else str(row.source_count)
            notes = ", ".join(row.notes[:4])
            role = row.operation_role or "?"
            lines.append(
                f"| [[{row.slug}]] | {sc} | {row.references_count} | {role} | {row.countries} | {notes} |"
            )
        if len(items) > limits[bucket]:
            lines.append(f"| ... | ... | ... | ... | ... | {len(items) - limits[bucket]} more |")
        lines.append("")

    lines.extend(
        [
            "## Recommended First Batch",
            "",
            "1. Merge obvious `operation-us-v-*` and single-country follow-on pages into case records.",
            "2. Repair metadata mismatches before making trust judgments on pages that already claim higher source density.",
            "3. Preserve genuinely multinational umbrella operations and enrich them toward the 5-source floor.",
            "4. Review the remaining high-risk single-source pages one family at a time rather than one page at a time.",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> None:
    rows: list[TriageRow] = []
    for path in load_paths():
        post = frontmatter.load(path)
        body = post.content or ""
        refs = count_references(body)
        rows.append(classify(post, path.stem, body, refs))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(render(rows), encoding="utf-8")
    triaged = [r for r in rows if r.bucket not in {"meets_threshold", "absorbed"}]
    counts = Counter(r.bucket for r in triaged)
    print(f"Wrote triage report to {OUT_PATH}")
    for key in ("merge_into_case", "merge_into_parent", "retain_and_enrich", "metadata_repair", "high_risk_review"):
        print(f"{key}: {counts[key]}")


if __name__ == "__main__":
    main()
