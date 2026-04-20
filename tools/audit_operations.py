from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
OUT_DIR = ROOT / "wiki" / "analysis"
OUT_PATH = OUT_DIR / "operation-audit-queue-2026-04.md"

FOLLOW_ON_TITLE_HINTS = [
    "sentenced",
    "pleads guilty",
    "pleaded guilty",
    "indicted",
    "charged",
    "convicted",
    "arraigned",
]

HEDGING_PATTERNS = [
    "likely",
    "almost certainly",
    "probably",
    "appears to",
    "suggests",
    "unclear",
    "not stated",
]

ENCODING_ARTIFACT_PATTERN = re.compile(r"\?\?|占|癤|�")


@dataclass
class AuditRow:
    slug: str
    title: str
    score: int
    source_count: int
    operation_role: str
    countries: int
    reasons: list[str]


def load_operation_paths() -> list[Path]:
    return [
        path
        for path in sorted(OPS_DIR.glob("*.md"))
        if not path.name.startswith("_")
    ]


def has_references_section(body: str) -> bool:
    return "## References" in body


def has_quality_sections(body: str) -> bool:
    required = ["## Summary", "## Participating Parties", "## Results"]
    return sum(1 for item in required if item in body) >= 2


def count_hedging(body: str) -> int:
    lower = body.lower()
    return sum(lower.count(pattern) for pattern in HEDGING_PATTERNS)


def is_domestic_follow_on(meta: dict) -> bool:
    if str(meta.get("operation_role") or "") != "follow-on":
        return False
    countries = meta.get("participating_countries") or []
    return len(countries) == 1 and str(countries[0]).strip() == "[[united-states]]"


def title_looks_procedural(title: str) -> bool:
    lower = title.lower()
    return any(hint in lower for hint in FOLLOW_ON_TITLE_HINTS)


def audit_operation(path: Path) -> AuditRow:
    post = frontmatter.load(path)
    meta = post.metadata
    body = post.content or ""
    title = str(meta.get("title") or path.stem)
    score = 0
    reasons: list[str] = []

    source_count = int(meta.get("source_count") or 0)
    if source_count < 5:
        gap = 5 - source_count
        score += min(20, gap * 4)
        reasons.append(f"low_sources:{source_count}")

    if not has_references_section(body):
        score += 12
        reasons.append("missing_references_section")

    if not has_quality_sections(body):
        score += 10
        reasons.append("thin_body_structure")

    hedging = count_hedging(body)
    if hedging >= 4:
        score += min(18, hedging * 2)
        reasons.append(f"heavy_hedging:{hedging}")

    if is_domestic_follow_on(meta):
        score += 25
        reasons.append("domestic_follow_on")

    if title_looks_procedural(title):
        score += 8
        reasons.append("procedural_title")

    countries = meta.get("participating_countries") or []
    if len(countries) <= 1 and str(meta.get("operation_role") or "") == "umbrella":
        score += 8
        reasons.append("single_country_umbrella")

    related_cases = meta.get("related_cases") or []
    related_operations = meta.get("related_operations") or []
    if not related_cases and not related_operations:
        score += 6
        reasons.append("weak_connectivity")

    legal_basis = meta.get("legal_basis") or []
    mechanisms = meta.get("mechanisms_used") or []
    if not legal_basis or not mechanisms:
        score += 6
        reasons.append("thin_cooperation_metadata")

    if ENCODING_ARTIFACT_PATTERN.search(body):
        score += 6
        reasons.append("encoding_artifacts")

    return AuditRow(
        slug=path.stem,
        title=title,
        score=score,
        source_count=source_count,
        operation_role=str(meta.get("operation_role") or ""),
        countries=len(countries),
        reasons=reasons,
    )


def render(rows: list[AuditRow]) -> str:
    high = [row for row in rows if row.score >= 35]
    medium = [row for row in rows if 20 <= row.score < 35]
    low = [row for row in rows if row.score < 20]

    lines = [
        "---",
        "title: Operation Audit Queue (April 2026)",
        "type: analysis",
        "created: 2026-04-19",
        "updated: 2026-04-19",
        'summary: "Priority queue for human-style review of all operation pages, ranked by source density, structure, international-cooperation fit, and content risk."',
        "source_count: 0",
        "---",
        "## Method",
        "",
        "This queue ranks every operation page for manual review using the following signals:",
        "",
        "- source density below the project minimum",
        "- missing `## References` section",
        "- thin body structure",
        "- domestic-only follow-on pattern",
        "- procedural title pattern",
        "- heavy hedging or uncertainty language",
        "- weak connectivity to cases or parent operations",
        "- thin legal/cooperation metadata",
        "- visible encoding artifacts",
        "",
        "## Queue Summary",
        "",
        f"- Total operations audited: **{len(rows)}**",
        f"- High priority (`score >= 35`): **{len(high)}**",
        f"- Medium priority (`20-34`): **{len(medium)}**",
        f"- Lower priority (`< 20`): **{len(low)}**",
        "",
        "## Top 150 Review Queue",
        "",
        "| Rank | Operation | Score | Sources | Role | Countries | Risk signals |",
        "|---|---|---:|---:|---|---:|---|",
    ]

    for idx, row in enumerate(rows[:150], start=1):
        reasons = ", ".join(row.reasons[:6])
        role = row.operation_role or "?"
        lines.append(
            f"| {idx} | [[{row.slug}]] | {row.score} | {row.source_count} | {role} | {row.countries} | {reasons} |"
        )

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- A high score does not automatically mean deletion. It means the page should be read and judged by a human-style audit standard first.",
            "- Domestic follow-on operations remain valid candidates for conversion into case-only records or for absorption into umbrella operations.",
            "- Source-dense pages can still rank high when their prose is weak, heavily hedged, or structurally malformed.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = [audit_operation(path) for path in load_operation_paths()]
    rows.sort(key=lambda row: (-row.score, row.source_count, row.slug))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(render(rows), encoding="utf-8")
    print(f"Wrote audit queue to {OUT_PATH}")
    print(f"Audited {len(rows)} operations")
    print(f"High priority: {sum(1 for row in rows if row.score >= 35)}")


if __name__ == "__main__":
    main()
