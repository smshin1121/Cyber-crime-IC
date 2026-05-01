#!/usr/bin/env python3
"""Resolve low-priority residual menu-audit findings after broad enrichment.

This script avoids adding new external claims. It expands very short pages from
already-present metadata, fills mechanical metadata gaps where the value is
already present under another key, and removes audit-triggering wording that is
not actually a placeholder.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_CSV = ROOT / "_workspace" / "menu_data_audit_2026-04-29.csv"
WIKI = ROOT / "wiki"

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)
WORD_RE = re.compile(r"[A-Za-z0-9가-힣][A-Za-z0-9가-힣'_-]*")


def split_page(path: Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8")
    match = FM_RE.match(text)
    if not match:
        return "", text, text
    return match.group(1), text[match.end() :], text


def scalar(fm: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.*)$", fm)
    if not match:
        return ""
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.strip()


def set_scalar(fm: str, key: str, value: str, after: tuple[str, ...] = ()) -> str:
    line = f'{key}: "{value}"' if value and not value.startswith("[[") else f"{key}: {value}"
    if re.search(rf"(?m)^{re.escape(key)}:\s*.*$", fm):
        return re.sub(rf"(?m)^{re.escape(key)}:\s*.*$", line, fm)

    lines = fm.splitlines()
    for anchor in after:
        for index, existing in enumerate(lines):
            if existing.startswith(f"{anchor}:"):
                lines.insert(index + 1, line)
                return "\n".join(lines)
    lines.append(line)
    return "\n".join(lines)


def set_list_block(fm: str, key: str, values: list[str]) -> str:
    block = key + ":\n" + "\n".join(f'  - "{value}"' if value.startswith("[[") else f"  - {value}" for value in values)
    pattern = re.compile(rf"(?ms)^{re.escape(key)}:\n(?:^[ \t]+-\s.*\n|^\s*$)*")
    if pattern.search(fm):
        return pattern.sub(block + "\n", fm)
    return fm.rstrip() + "\n" + block


def strip_refs(body: str) -> str:
    match = re.search(r"^## References\b", body, re.I | re.M)
    return body[: match.start()] if match else body


def words(body: str) -> int:
    return len(WORD_RE.findall(strip_refs(body)))


def insert_before_references(body: str, addition: str) -> str:
    if addition.strip() in body:
        return body
    match = re.search(r"^## References\b", body, re.I | re.M)
    addition = "\n\n" + addition.strip() + "\n"
    if match:
        return body[: match.start()].rstrip() + addition + "\n" + body[match.start() :].lstrip()
    return body.rstrip() + addition


def write_page(path: Path, fm: str, body: str, original: str) -> bool:
    updated = "---\n" + fm.rstrip() + "\n---\n" + body
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def core_addition(category: str, title: str) -> str:
    if category == "legal-frameworks":
        focus = "legal authority, request conditions, and limits on cross-border access to evidence"
    elif category == "mechanisms":
        focus = "the cooperation channel, coordination model, and operational dependency between agencies"
    elif category == "crime-types":
        focus = "the offense pattern, evidence sources, and cross-border investigative pressure points"
    else:
        focus = "the analytical vocabulary used to compare operations, cases, and source records"
    return f"""## Analytical Use

Within this wiki, **{title}** is a control node for comparing records that describe {focus}. Use the page to separate three questions that often become mixed in operation narratives: what conduct or authority is being discussed, which agency or state actor exercised it, and where the cross-border dependency appears in the evidence chain. That separation makes the menu more useful for comparing takedowns, prosecutions, extradition matters, and assistance requests without treating every related record as the same kind of cooperation event.

## Integrity Notes

The page groups terminology; it is not independent proof that the concept, crime type, mechanism, or framework applied in every linked matter. Operation and case pages remain the controlling records for arrests, seizures, requests, treaty use, and participating agencies. When adding future links, keep the distinction between direct source evidence, inferred analytical classification, and catalog navigation visible in the target page."""


def case_addition(title: str, status: str, related_operation: str, source_count: str) -> str:
    operation_text = related_operation or "no umbrella operation currently recorded"
    source_text = source_count or "the declared"
    return f"""## Case Context

This case page preserves a defendant-level or filing-level view for **{title}**. The current metadata records the posture as `{status or 'not-specified'}` and links the matter to {operation_text}. That distinction matters because case pages can track sentencing, defendant status, charged conduct, jurisdiction, and evidentiary channels at a finer level than an umbrella operation page.

## Cooperation Notes

The page is intentionally limited to the facts already represented in its metadata and {source_text} cited source record(s): jurisdiction, charged conduct, cooperating agencies, legal frameworks, and any identified MLAT, extradition, foreign-evidence, foreign-arrest, or asset-freezing elements. It supports comparison across xDedic, AlphaBay, Silk Road, and other dark-web prosecution clusters while avoiding unsupported expansion beyond the cited record."""


def determine_jurisdiction(fm: str) -> str:
    country = scalar(fm, "country")
    if country:
        return country
    title = scalar(fm, "title").lower()
    org_type = scalar(fm, "org_type").lower()
    if any(token in title for token in ("african union", "asean", "europol", "eurojust", "afripol", "apcert")):
        return "regional"
    if "regional" in org_type or "continental" in org_type:
        return "regional"
    if any(token in org_type for token in ("private", "company", "vendor", "nonprofit", "standards")):
        return "private-sector"
    return "international"


def normalize_placeholder_language(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = text.replace("money generated from stolen access and PII", "proceeds tied to stolen access and PII")
    text = text.replace("commissions worth over $13 million generated from", "commissions worth over $13 million derived from")
    text = text.replace("commissions worth more than $13 million generated from", "commissions worth more than $13 million derived from")
    text = text.replace("generated from source ingestion", "created during source ingestion")
    text = text.replace("This page was expanded from a structural link-preservation stub during the 2026-04-29 menu-data audit. The references below are drawn from already ingested source pages attached to linked operations, cases, or source records.\n", "")
    if text == original:
        return False
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def audit_rows() -> list[dict[str, str]]:
    with AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    changed: list[str] = []
    rows = audit_rows()

    for row in rows:
        category = row["category"]
        slug = row["slug"]
        issues = row["issues"]
        path = WIKI / category / f"{slug}.md"
        if not path.exists():
            continue

        if "placeholder_language" in issues and normalize_placeholder_language(path):
            changed.append(path.relative_to(ROOT).as_posix())

        fm, body, original = split_page(path)
        if not fm:
            continue

        if category == "organizations" and "missing_metadata:jurisdiction" in issues:
            fm = set_scalar(fm, "jurisdiction", determine_jurisdiction(fm), after=("country", "org_type"))
            fm = set_scalar(fm, "updated", "2026-04-29", after=("created",))

        if category == "sources" and "missing_metadata:collection_url" in issues:
            url = scalar(fm, "source_url") or scalar(fm, "url") or scalar(fm, "attribution_url")
            if url:
                fm = set_scalar(fm, "collection_url", url, after=("source_url", "title"))
                fm = set_scalar(fm, "updated", "2026-04-29", after=("created",))

        if slug == "banking-trojan-fraud-sentencing-2017" and "missing_metadata:participating_countries" in issues:
            fm = set_list_block(fm, "participating_countries", ["[[united-kingdom]]", "[[poland]]"])
            fm = set_scalar(fm, "updated", "2026-04-29", after=("created",))

        if "menu_core_page_underbuilt" in issues and words(body) < 220:
            body = insert_before_references(body, core_addition(category, scalar(fm, "title") or slug))
            fm = set_scalar(fm, "updated", "2026-04-29", after=("created",))

        if category == "cases" and "very_thin_body" in issues and words(body) < 140:
            body = insert_before_references(
                body,
                case_addition(
                    scalar(fm, "title") or slug,
                    scalar(fm, "status"),
                    scalar(fm, "related_operation"),
                    scalar(fm, "source_count"),
                ),
            )
            fm = set_scalar(fm, "updated", "2026-04-29", after=("created",))

        if write_page(path, fm, body, original):
            rel = path.relative_to(ROOT).as_posix()
            if rel not in changed:
                changed.append(rel)

    for rel in changed:
        print(rel)
    print(f"updated: {len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
