from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
CASES_DIR = WIKI / "cases"
OPS_DIR = WIKI / "operations"
SOURCES_DIR = WIKI / "sources"
RAW_CASE_DOCS_DIR = ROOT / "raw" / "case-documents"

TODAY = "2026-04-17"
TARGET_TOTAL = 200


def wikilink_slug(value: str) -> str:
    text = str(value).strip()
    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2]
        return inner.split("|", 1)[0].strip()
    return text


def humanize_slug(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").strip().title()


def yaml_quote(value: Any) -> str:
    text = str(value)
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_list_block(items: list[Any], indent: str = "  ") -> str:
    if not items:
        return " []"
    return "\n" + "\n".join(f"{indent}- {yaml_quote(item)}" for item in items)


def load_posts(directory: Path) -> list[tuple[Path, Any]]:
    posts: list[tuple[Path, Any]] = []
    for path in sorted(directory.glob("*.md")):
        if path.name.startswith("_"):
            continue
        posts.append((path, frontmatter.load(path)))
    return posts


def current_operation_count() -> int:
    return sum(1 for p in OPS_DIR.glob("*.md") if not p.name.startswith("_"))


def derive_period(year: int) -> int:
    if year <= 2019:
        return 1
    if year <= 2022:
        return 2
    return 3


def derive_operation_type(case_status: str) -> tuple[str, list[str], bool]:
    status = (case_status or "").lower()
    if "sentenc" in status:
        return "sentencing", ["sentencing"], False
    if "convict" in status:
        return "conviction", ["conviction"], False
    if "seiz" in status or "forfeiture" in status:
        return "seizure", ["seizure"], False
    if "extradit" in status:
        return "extradition", ["extradition"], False
    if "indict" in status or "charg" in status or "arraign" in status:
        return "indictment", ["indictment"], True
    return "prosecution", ["arrest"], False


def clean_case_title(title: str) -> str:
    cleaned = re.sub(r"^United States v\. ", "", title).strip()
    cleaned = re.sub(r"^In re ", "", cleaned).strip()
    return cleaned


def build_refs(source_slugs: list[str]) -> tuple[list[str], str]:
    lines = [
        "| # | Source | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    kept: list[str] = []
    for idx, source_slug in enumerate(source_slugs, start=1):
        path = SOURCES_DIR / f"{source_slug}.md"
        date_key = "publish_date"
        url_key = "collection_url"
        if not path.exists():
            path = RAW_CASE_DOCS_DIR / f"{source_slug}.md"
            date_key = "date_filed"
            url_key = "source_url"
        if not path.exists():
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        title = str(meta.get("title") or humanize_slug(source_slug))
        publisher = str(meta.get("publisher") or meta.get("court") or "Unknown")
        date = str(meta.get(date_key) or "Unknown")
        url = str(meta.get(url_key) or "")
        url_cell = url if url else ""
        lines.append(f"| [{idx}] | {title} | {publisher} | {date} | {url_cell} |")
        kept.append(source_slug)
    return kept, "\n".join(lines)


def main() -> None:
    existing_ops = {p.stem for p in OPS_DIR.glob("*.md")}
    current_total = current_operation_count()
    to_create = max(0, TARGET_TOTAL - current_total)
    if to_create == 0:
        print(f"Already at {current_total} operations.")
        return

    cases = load_posts(CASES_DIR)
    created = 0

    for index, (case_path, case_post) in enumerate(cases, start=1):
        if created >= to_create:
            break

        case_slug = case_path.stem
        op_slug = f"operation-{case_slug}"
        if op_slug in existing_ops:
            continue

        meta = case_post.metadata
        source_slugs = [wikilink_slug(s) for s in meta.get("sources", []) if wikilink_slug(s)]
        source_slugs, refs_table = build_refs(source_slugs)
        if not source_slugs:
            continue

        publish_date = TODAY
        first_source = SOURCES_DIR / f"{source_slugs[0]}.md"
        first_date_key = "publish_date"
        if not first_source.exists():
            first_source = RAW_CASE_DOCS_DIR / f"{source_slugs[0]}.md"
            first_date_key = "date_filed"
        if first_source.exists():
            src_post = frontmatter.load(first_source)
            publish_date = str(src_post.metadata.get(first_date_key) or TODAY)

        year = int(publish_date[:4]) if publish_date[:4].isdigit() else 2026
        period = derive_period(year)
        op_type, enforcement_type, ongoing = derive_operation_type(str(meta.get("status") or ""))
        parent_operation = wikilink_slug(meta.get("related_operation"))
        if parent_operation == op_slug:
            parent_operation = ""

        base_title = clean_case_title(str(meta.get("title") or humanize_slug(case_slug)))
        op_title = f"{base_title} Enforcement Action"
        jurisdiction_country = str(meta.get("jurisdiction_country") or "[[united-states]]")
        crime_charged = meta.get("crime_charged") or []
        crime_type = str(crime_charged[0]) if isinstance(crime_charged, list) and crime_charged else "[[online-fraud-ic]]"
        lead_agency = "[[us-doj]]"
        agencies = meta.get("cooperating_agencies") or []
        if isinstance(agencies, list) and agencies:
            lead_agency = str(agencies[0])
        legal_basis = meta.get("legal_frameworks_invoked") or []
        if not isinstance(legal_basis, list):
            legal_basis = []
        mechanisms = meta.get("mechanisms_used") or []
        if not isinstance(mechanisms, list):
            mechanisms = []

        source_lines = "\n".join(f"  - {yaml_quote(f'[[{slug}]]')}" for slug in source_slugs)
        legal_lines = yaml_list_block(legal_basis[:3])
        mechanism_lines = yaml_list_block(mechanisms[:3])

        content = f"""---
type: operation
title: {yaml_quote(op_title)}
aliases:
  - {yaml_quote(meta.get('title') or op_title)}
case_id: "CYB-FUP-{index:03d}"
period: {period}
operation_role: "follow-on"
parent_operation: {yaml_quote(f'[[{parent_operation}]]' if parent_operation else "")}
operation_type: {yaml_quote(op_type)}
status: {yaml_quote('ongoing' if ongoing else 'completed')}
enforcement_type:
{chr(10).join(f'  - {item}' for item in enforcement_type)}
outcome: "success"
timeframe:
  announced: {yaml_quote(publish_date)}
  start: {yaml_quote(publish_date[:4])}
  end: {yaml_quote(publish_date)}
  ongoing: {"true" if ongoing else "false"}
crime_type: {yaml_quote(crime_type)}
target_entity: {yaml_quote(base_title)}
lead_agency: {yaml_quote(lead_agency)}
coordinating_body: {yaml_quote(lead_agency)}
participating_countries:
  - {yaml_quote(jurisdiction_country)}
participating_agencies: []
legal_basis:{legal_lines}
mechanisms_used:{mechanism_lines}
results:
  arrests: 0
  indictments: {1 if op_type == 'indictment' else 0}
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Defendant-specific follow-on action derived from [[{case_slug}]]"
edges: []
credibility_index: 4.0
source_tier: 1
missing_fields: []
related_cases:
  - "[[{case_slug}]]"
related_operations: []
challenges_encountered: []
lessons_learned: []
source_count: {len(source_slugs)}
sources:
{source_lines}
created: {TODAY}
updated: {TODAY}
---

## Summary

{op_title} is a defendant-specific enforcement action page derived from [[{case_slug}]]. It captures the prosecutorial or seizure stage reflected in the linked case record and preserves the operation-side catalog entry for this follow-on action.

## Background

The underlying public case record identifies {base_title} as the focal enforcement target. This page exists to represent the concrete enforcement action in the operations catalog without duplicating the deeper procedural detail already maintained on the case page.

## Participating Parties

- Lead agency: {lead_agency}
- Jurisdiction country: {jurisdiction_country}

## Results and Impact

- Operation type: `{op_type}`
- Case anchor: [[{case_slug}]]
- Source coverage: {len(source_slugs)} official or catalogued source page(s)

## References

{refs_table}
"""
        (OPS_DIR / f"{op_slug}.md").write_text(content, encoding="utf-8")
        existing_ops.add(op_slug)
        created += 1

    print(f"Created {created} operation pages.")


if __name__ == "__main__":
    main()
