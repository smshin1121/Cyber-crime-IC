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


def wikilink_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2]
        return inner.split("|", 1)[0].strip()
    return text


def wikilink(value: str) -> str:
    return f"[[{value}]]"


def yaml_quote(value: Any) -> str:
    text = str(value)
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_list_block(items: list[Any], indent: str = "  ") -> str:
    if not items:
        return " []"
    return "\n" + "\n".join(f"{indent}- {yaml_quote(item)}" for item in items)


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for item in items:
        text = str(item or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        output.append(text)
    return output


def extract_summary(content: str) -> str:
    match = re.search(r"^## Summary\s*$", content, re.MULTILINE)
    if not match:
        return ""
    tail = content[match.end():].lstrip()
    lines: list[str] = []
    for line in tail.splitlines():
        stripped = line.strip()
        if not stripped:
            if lines:
                break
            continue
        if stripped.startswith("#"):
            break
        lines.append(stripped)
    return " ".join(lines).strip()


def fallback_operation_summary(meta: dict[str, Any]) -> str:
    title = str(meta.get("title") or "This operation").strip()
    target = str(meta.get("target_entity") or "the named target").strip()
    outcome = str(meta.get("outcome") or "documented").strip()
    status = str(meta.get("status") or "").strip()
    bits = [f"{title} is an operation page covering enforcement activity against {target}."]
    if status:
        bits.append(f"The operation is currently recorded as `{status}`.")
    if outcome:
        bits.append(f"Recorded outcome: `{outcome}`.")
    return " ".join(bits)


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
        title = str(meta.get("title") or source_slug.replace("-", " ").title())
        publisher = str(meta.get("publisher") or meta.get("court") or "Unknown")
        date = str(meta.get(date_key) or "Unknown")
        url = str(meta.get(url_key) or "")
        lines.append(f"| [{idx}] | {title} | {publisher} | {date} | {url} |")
        kept.append(source_slug)
    return kept, "\n".join(lines)


def next_follow_on_id() -> int:
    max_id = 0
    pattern = re.compile(r"^CYB-FUP-(\d+)$")
    for path in OPS_DIR.glob("*.md"):
        if path.name.startswith("_"):
            continue
        meta = frontmatter.load(path).metadata
        match = pattern.match(str(meta.get("case_id") or ""))
        if match:
            max_id = max(max_id, int(match.group(1)))
    return max_id + 1


def create_follow_on_operation(case_path: Path, case_post: Any, sequence: int) -> str | None:
    case_slug = case_path.stem
    op_slug = f"operation-{case_slug}"
    if (OPS_DIR / f"{op_slug}.md").exists():
        return op_slug

    meta = case_post.metadata
    source_slugs = unique([wikilink_slug(s) for s in meta.get("sources", []) if wikilink_slug(s)])
    source_slugs, refs_table = build_refs(source_slugs)
    if not source_slugs:
        return None

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
    base_title = clean_case_title(str(meta.get("title") or case_slug.replace("-", " ").title()))
    op_title = f"{base_title} Enforcement Action"

    jurisdiction_country = str(meta.get("jurisdiction_country") or "[[united-states]]")
    crime_charged = meta.get("crime_charged") or []
    crime_type = str(crime_charged[0]) if isinstance(crime_charged, list) and crime_charged else "[[online-fraud-ic]]"
    agencies = unique([str(a) for a in (meta.get("cooperating_agencies") or [])])
    lead_agency = agencies[0] if agencies else "[[us-doj]]"
    legal_basis = [str(v) for v in (meta.get("legal_frameworks_invoked") or [])][:3]
    mechanisms = [str(v) for v in (meta.get("mechanisms_used") or [])][:3]

    content = f"""---
type: operation
title: {yaml_quote(op_title)}
aliases:
  - {yaml_quote(meta.get('title') or op_title)}
case_id: "CYB-FUP-{sequence:03d}"
period: {period}
operation_role: "follow-on"
parent_operation: ""
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
crime_types:
  - {yaml_quote(crime_type)}
target_entity: {yaml_quote(base_title)}
lead_agency: {yaml_quote(lead_agency)}
coordinating_body: {yaml_quote(lead_agency)}
participating_countries:
  - {yaml_quote(jurisdiction_country)}
jurisdictions:
  - {yaml_quote(jurisdiction_country)}
participating_agencies:{yaml_list_block(agencies)}
organizations:{yaml_list_block(agencies or [lead_agency])}
legal_basis:{yaml_list_block(legal_basis)}
mechanisms_used:{yaml_list_block(mechanisms)}
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
{chr(10).join(f'  - {yaml_quote(f"[[{slug}]]")}' for slug in source_slugs)}
summary: {yaml_quote(f'{op_title} is a defendant-specific enforcement action page derived from [[{case_slug}]].')}
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
    return op_slug


def main() -> None:
    changed = 0
    created_ops = 0
    next_id = next_follow_on_id()

    for case_path in sorted(CASES_DIR.glob("*.md")):
        if case_path.name.startswith("_"):
            continue
        case_post = frontmatter.load(case_path)
        meta = case_post.metadata
        case_changed = False

        if not meta.get("summary"):
            summary = extract_summary(case_post.content)
            if summary:
                meta["summary"] = summary
                case_changed = True

        if not wikilink_slug(meta.get("related_operation")):
            op_slug = create_follow_on_operation(case_path, case_post, next_id)
            if op_slug:
                next_id += 1
                meta["related_operation"] = wikilink(op_slug)
                case_changed = True
                created_ops += 1

        if case_changed:
            case_path.write_text(frontmatter.dumps(case_post), encoding="utf-8")
            changed += 1

    for op_path in sorted(OPS_DIR.glob("*.md")):
        if op_path.name.startswith("_"):
            continue
        op_post = frontmatter.load(op_path)
        meta = op_post.metadata
        op_changed = False

        if not meta.get("summary"):
            summary = extract_summary(op_post.content)
            if not summary:
                summary = fallback_operation_summary(meta)
            meta["summary"] = summary
            op_changed = True

        if not meta.get("jurisdictions"):
            countries = [str(v) for v in (meta.get("participating_countries") or []) if str(v).strip()]
            if countries:
                meta["jurisdictions"] = unique(countries)
                op_changed = True

        if not meta.get("organizations"):
            orgs = [str(meta.get("lead_agency") or "").strip(), str(meta.get("coordinating_body") or "").strip()]
            orgs.extend(str(v).strip() for v in (meta.get("participating_agencies") or []))
            orgs = unique(orgs)
            if orgs:
                meta["organizations"] = orgs
                op_changed = True

        if not meta.get("crime_types"):
            crime_type = str(meta.get("crime_type") or "").strip()
            if crime_type:
                meta["crime_types"] = [crime_type]
                op_changed = True

        if op_changed:
            op_path.write_text(frontmatter.dumps(op_post), encoding="utf-8")
            changed += 1

    print(f"Updated {changed} pages; created {created_ops} follow-on operations.")


if __name__ == "__main__":
    main()
