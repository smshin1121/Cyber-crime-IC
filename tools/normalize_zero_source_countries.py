from __future__ import annotations

from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
COUNTRIES_DIR = ROOT / "wiki" / "countries"
RUN_DATE = "2026-05-03"

UNSUPPORTED_FIELDS = {
    "bilateral_agreements",
    "central_authority",
    "cooperation_assessment",
    "cybercrime_legislation",
    "key_agencies",
    "notable_cases",
}


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, "", {}):
        return []
    return [value]


def operation_links(meta: dict[str, Any]) -> list[str]:
    return [str(item) for item in as_list(meta.get("operations_participated")) if str(item).strip()]


def render_operations_table(ops: list[str]) -> str:
    if not ops:
        return "No operation backlinks are currently recorded for this country node."
    lines = ["| Linked operation | Verification role |", "|---|---|"]
    for op in ops[:20]:
        lines.append(
            f"| {op} | Relationship edge retained from operation/case metadata; use the operation page and its references for claim-level verification. |"
        )
    if len(ops) > 20:
        lines.append(f"| ... | {len(ops) - 20} additional operation links retained in frontmatter. |")
    return "\n".join(lines)


def normalized_body(title: str, ops: list[str]) -> str:
    return f"""## Summary

{title} is retained as a country navigation and relationship node for the cybercrime international-cooperation corpus. This page is an assessment-control record because the repository does not currently link a country-specific source page for this jurisdiction.

## Verification Status

No direct country-profile source is linked in this repository for this page. As of {RUN_DATE}, legal-system, central-authority, treaty-membership, cybercrime-capacity, and national-agency claims are marked `not-assessed` rather than inferred from geography, operation participation, or prior unsourced prose.

## Corpus Relationships

{render_operations_table(ops)}

## Follow-up Source Targets

The next reliable sources for this page are official national police or prosecutor cybercrime pages, justice-ministry mutual-assistance pages, Budapest Convention or UN treaty-status records, and primary operation releases naming the country. Until those are linked, use this page for navigation and relationship tracing only; do not use it as authority for legal-system detail, MLAT performance, 24/7 contact availability, or national cyber-investigative maturity.
"""


def normalize(path: Path) -> bool:
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    if int(meta.get("source_count") or 0) != 0:
        return False

    title = str(meta.get("title") or path.stem.replace("-", " ").title())
    ops = operation_links(meta)

    for field in UNSUPPORTED_FIELDS:
        meta.pop(field, None)

    meta["type"] = "country"
    meta["title"] = title
    meta["status"] = "needs-official-source-ingestion"
    meta["updated"] = RUN_DATE
    meta["last_verified"] = RUN_DATE
    meta["source_count"] = 0
    meta["sources"] = []
    meta["legal_system"] = "not-assessed"
    meta["ic_capacity"] = "not-assessed"
    meta["treaty_memberships"] = ["not-assessed"]
    meta["assessment_confidence"] = "limited"
    meta["verification_scope"] = "country profile not verified beyond linked operation/source relationships"
    if ops:
        meta["operations_participated"] = ops

    post.metadata = meta
    post.content = normalized_body(title, ops).rstrip() + "\n"
    path.write_text(frontmatter.dumps(post), encoding="utf-8")
    return True


def main() -> None:
    changed: list[str] = []
    for path in sorted(COUNTRIES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        if normalize(path):
            changed.append(path.stem)
    print(f"Normalized {len(changed)} zero-source country profiles")
    for slug in changed:
        print(f"- {slug}")


if __name__ == "__main__":
    main()
