from __future__ import annotations

import argparse
import copy
import csv
import json
import re
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

import frontmatter

from enrich_targeted_content_from_sources import (
    CASES_DIR,
    ENRICHMENT_RE,
    OPS_DIR,
    ROOT,
    SOURCES_DIR,
    WIKI_DIR,
    as_list,
    build_enrichment,
    clean_text,
    fact_pool,
    has_placeholder_language,
    parse_reference_rows,
    source_records,
    split_frontmatter,
    strip_references,
    wikilink_slug,
)


AUDIT_PATH = ROOT / "_workspace" / "content_depth_audit_2026-04-26.csv"
REPORT_PATH = WIKI_DIR / "analysis" / "low-priority-integrity-repair-2026-04-26.md"
TODAY = "2026-04-26"

SOURCE_URL_KEYS = (
    "collection_url",
    "source_url",
    "url",
    "canonical_url",
    "final_url",
)

LOW_CONFIDENCE_FACT_PATTERNS = (
    "...",
    "press release",
    "news press release",
    "share facebook",
    "secure .gov websites",
    "a .gov website belongs",
    "lock locked padlock",
    "share sensitive information",
    "main office",
    "federal courthouse",
    "related content",
    "linked source material",
    "follow-on operation catalog record",
    "operation-side pointer",
    "source summary",
    "updated january",
    "updated february",
    "updated march",
    "updated april",
    "updated may",
    "updated june",
    "updated july",
    "updated august",
    "updated september",
    "updated october",
    "updated november",
    "updated december",
    "topics cybercrime",
    "component usao",
    "components criminal",
)


@dataclass
class RepairResult:
    category: str
    slug: str
    changed: bool = False
    placeholder_replaced: bool = False
    source_count_fixed: bool = False
    source_links_added: int = 0
    crime_links_added: int = 0
    title_fixed: bool = False
    operation_name_fixed: bool = False
    generated_phrase_fixed: bool = False


def normalize_url(value: Any) -> str:
    text = str(value or "").strip()
    text = re.sub(r"[)>.,;]+$", "", text)
    text = text.rstrip("/")
    return text.lower()


def build_source_url_map() -> dict[str, str]:
    url_map: dict[str, str] = {}
    for path in SOURCES_DIR.glob("*.md"):
        try:
            post = frontmatter.load(path)
        except Exception:
            continue
        for key in SOURCE_URL_KEYS:
            url = normalize_url(post.metadata.get(key))
            if url and url not in url_map:
                url_map[url] = path.stem
    return url_map


def page_path(category: str, slug: str) -> Path:
    if category == "operations":
        return OPS_DIR / f"{slug}.md"
    return CASES_DIR / f"{slug}.md"


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def issue_values(issues: str, prefix: str) -> list[str]:
    values: list[str] = []
    for issue in str(issues or "").split(";"):
        issue = issue.strip()
        if issue.startswith(prefix):
            values.append(issue[len(prefix) :])
    return values


def link_value(slug: str) -> str:
    return f"[[{slug}]]"


def ensure_list_link(meta: dict[str, Any], key: str, slug: str) -> bool:
    link = link_value(slug)
    values = as_list(meta.get(key))
    if any(wikilink_slug(value) == slug for value in values):
        return False
    if key not in meta or meta.get(key) in (None, ""):
        meta[key] = []
    elif not isinstance(meta[key], list):
        meta[key] = [meta[key]]
    meta[key].append(link)
    return True


def source_slugs(meta: dict[str, Any]) -> list[str]:
    return [wikilink_slug(value) for value in as_list(meta.get("sources")) if wikilink_slug(value)]


def repair_sources(meta: dict[str, Any], body: str, url_map: dict[str, str]) -> tuple[bool, int]:
    refs = parse_reference_rows(body)
    existing = source_slugs(meta)
    target_count = len(refs) if refs else len(existing)
    fixed = False
    if target_count and str(meta.get("source_count") or "") != str(target_count):
        meta["source_count"] = target_count
        fixed = True
    return fixed, 0


def repair_crime_links(meta: dict[str, Any], category: str, issues: str) -> int:
    added = 0
    for slug in issue_values(issues, "possible_crime_type_mismatch:"):
        if category == "cases":
            added += int(ensure_list_link(meta, "crime_charged", slug))
            added += int(ensure_list_link(meta, "key_legal_issues", slug))
        else:
            added += int(ensure_list_link(meta, "crime_types", slug))
    return added


def repaired_enforcement_title(title: str) -> str:
    if title.endswith(" Follow-on Enforcement Action"):
        return title[: -len(" Follow-on Enforcement Action")] + " Follow-On Action"
    if title.endswith(" Follow-On Enforcement Action"):
        return title[: -len(" Follow-On Enforcement Action")] + " Follow-On Action"
    if title.endswith(" Enforcement Action"):
        return title[: -len(" Enforcement Action")] + " Follow-On Action"
    return title.replace(" Enforcement Action", " Follow-On Action")


def repair_title_and_body(meta: dict[str, Any], body: str, issues: str) -> tuple[bool, bool, str]:
    title_fixed = False
    operation_name_fixed = False
    title = str(meta.get("title") or "")

    if "generated_enforcement_title" in issues:
        if "Enforcement Action" in title:
            new_title = repaired_enforcement_title(title)
            meta["title"] = new_title
            title_fixed = True
            body = body.replace(title, new_title)
        body = body.replace(
            "defendant-specific enforcement action page",
            "follow-on operation catalog record",
        )
        body = body.replace(
            "enforcement action page derived from",
            "follow-on operation catalog record tied to",
        )
        summary = str(meta.get("summary") or "")
        summary = summary.replace(
            "defendant-specific enforcement action page",
            "follow-on operation catalog record",
        )
        summary = summary.replace(
            "enforcement action page derived from",
            "follow-on operation catalog record tied to",
        )
        if summary != str(meta.get("summary") or ""):
            meta["summary"] = summary

    title_ko = str(meta.get("title_ko") or "")
    if "unresolved_operation_name" in issues or title_ko.startswith("공식 작전명 없음"):
        if title_ko.startswith("怨듭떇") or title_ko.startswith("공식 작전명 없음"):
            alias = ""
            aliases = as_list(meta.get("aliases"))
            if aliases:
                alias = clean_text(aliases[0], limit=80)
            suffix = f"; alias: {alias}" if alias else ""
            meta["title_ko"] = f"{clean_text(meta.get('title') or title, limit=160)} (공식 작전명 미확인{suffix})"
            operation_name_fixed = True

    source_count = meta.get("source_count")
    if source_count:
        body = re.sub(
            r"Source coverage:\s+\d+\s+official or catalogued source page\(s\)",
            f"Source coverage: {source_count} official or catalogued source page(s)",
            body,
        )

    if title_fixed:
        summary = str(meta.get("summary") or "")
        if title in summary:
            meta["summary"] = summary.replace(title, str(meta.get("title") or title))
        else:
            meta["summary"] = summary.replace("enforcement action page", "follow-on operation catalog record")
    return title_fixed, operation_name_fixed, body


def normalize_generated_phrases(meta: dict[str, Any], body: str) -> tuple[bool, str]:
    replacements = (
        (
            "is recorded as a case based on the linked source set.",
            "is documented in the linked source material.",
        ),
        (
            "is recorded as an operation based on the linked source set.",
            "is documented in the linked source material.",
        ),
        (
            "is recorded as a operation based on the linked source set.",
            "is documented in the linked source material.",
        ),
        (
            "defendant-specific enforcement action page derived from",
            "follow-on operation catalog record tied to",
        ),
        (
            "The supporting source set includes",
            "Available source coverage includes",
        ),
        (
            "It captures the prosecutorial or seizure stage reflected in the linked case record and preserves the operation-side catalog entry for this follow-on action.",
            "It preserves the operation-side pointer for the related case record.",
        ),
    )
    changed = False
    for old, new in replacements:
        if old in body:
            body = body.replace(old, new)
            changed = True
        summary = str(meta.get("summary") or "")
        if old in summary:
            meta["summary"] = summary.replace(old, new)
            changed = True
    return changed, body


def high_confidence_fact(text: str) -> bool:
    cleaned = clean_text(text, limit=260)
    if len(cleaned) < 55:
        return False
    if cleaned[:1].islower():
        return False
    low = cleaned.lower()
    if low.startswith(
        (
            "and ",
            "or ",
            "to ",
            "of ",
            "for ",
            "both ",
            "was ",
            "is ",
            "has ",
            "resident ",
            "selling ",
            "scheduled ",
            "convicted",
            "through ",
            "years ago ",
            "cooperation with ",
            "interagency ",
        )
    ):
        return False
    return not any(pattern in low for pattern in LOW_CONFIDENCE_FACT_PATTERNS)


def has_low_confidence_text(text: str) -> bool:
    low = text.lower()
    return any(pattern in low for pattern in LOW_CONFIDENCE_FACT_PATTERNS)


def has_fragment_summary(text: str) -> bool:
    return bool(
        re.search(
            r"linked source set\.\s+(?:[a-z]|and\b|or\b|to\b|of\b|for\b|both\b|was\b|is\b|has\b|resident\b|selling\b|scheduled\b|convicted\b|through\b|years ago\b|cooperation with\b|interagency\b)",
            text,
        )
    )


def safe_source_records(meta: dict[str, Any], body: str):
    records = source_records(meta, body)
    return [
        replace(record, facts=[fact for fact in record.facts if high_confidence_fact(fact)])
        for record in records
    ]


def safe_summary_text(meta: dict[str, Any], category: str, records) -> str:
    title = clean_text(meta.get("title"), limit=180)
    publishers = sorted({record.publisher for record in records if record.publisher})
    source_phrase = f" The supporting source set includes {', '.join(publishers[:4])}." if publishers else ""
    facts = fact_pool(records)
    if facts:
        return clean_text(
            f"{title} is recorded as a {category.rstrip('s')} based on the linked source set. {facts[0]}{source_phrase}",
            limit=520,
        )
    return clean_text(
        f"{title} is recorded as a {category.rstrip('s')} based on the linked source set.{source_phrase}",
        limit=520,
    )


def safe_replacement_body(meta: dict[str, Any], category: str, records) -> tuple[str, int]:
    summary = safe_summary_text(meta, category, records)
    enrichment, facts_used = build_enrichment(meta, category, records, "")
    enrichment = enrichment.replace("<!-- SOURCE_ENRICHMENT_START -->\n", "").replace(
        "\n<!-- SOURCE_ENRICHMENT_END -->", ""
    )
    lines = ["## Summary", "", summary, "", enrichment.strip()]
    return "\n".join(lines).rstrip() + "\n", facts_used


def remove_low_confidence_bullets(body: str) -> str:
    lines = body.splitlines()
    cleaned: list[str] = []
    for line in lines:
        if line.lstrip().startswith("- ") and has_low_confidence_text(line):
            continue
        bullet_text = line.lstrip()[2:].strip() if line.lstrip().startswith("- ") else ""
        if bullet_text and bullet_text[:1].islower():
            continue
        cleaned.append(line)
    return "\n".join(cleaned) + ("\n" if body.endswith("\n") else "")


def yaml_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if value is None:
        return '""'
    return json.dumps(str(value), ensure_ascii=False)


def field_pattern(key: str) -> re.Pattern[str]:
    return re.compile(rf"(?m)^{re.escape(key)}:[^\n]*\n(?:^[ \t]+[^\n]*\n)*")


def insert_frontmatter_field(fm_text: str, text: str) -> str:
    source_match = re.search(r"(?m)^source_count:\s*", fm_text)
    if source_match:
        return fm_text[: source_match.start()] + text + fm_text[source_match.start() :]
    end = fm_text.rfind("\n---")
    if end == -1:
        return fm_text + text
    return fm_text[:end] + "\n" + text.rstrip() + fm_text[end:]


def set_scalar_field(fm_text: str, key: str, value: Any) -> str:
    line = f"{key}: {yaml_scalar(value)}"
    if re.search(rf"(?m)^{re.escape(key)}:\s*", fm_text):
        return re.sub(rf"(?m)^{re.escape(key)}:\s*.*$", line, fm_text, count=1)
    return insert_frontmatter_field(fm_text, line + "\n")


def set_list_field(fm_text: str, key: str, values: list[Any]) -> str:
    lines = [f"{key}:"]
    for value in values:
        lines.append(f"  - {yaml_scalar(value)}")
    block = "\n".join(lines) + "\n"
    pattern = field_pattern(key)
    if pattern.search(fm_text):
        return pattern.sub(block, fm_text, count=1)
    return insert_frontmatter_field(fm_text, block)


def sync_frontmatter_text(
    fm_text: str,
    original_meta: dict[str, Any],
    meta: dict[str, Any],
    summary: str | None,
    touch_updated: bool,
) -> str:
    changed_scalar_keys = (
        "title",
        "title_ko",
        "source_count",
        "case_number",
        "precedent_value",
        "summary",
        "updated",
    )
    list_keys = ("sources", "crime_charged", "key_legal_issues", "crime_types")

    if touch_updated:
        meta["updated"] = TODAY
    if summary:
        meta["summary"] = summary
        if str(meta.get("case_number") or "").startswith("Source-derived from"):
            meta["case_number"] = "Not specified in available source metadata"
        if str(meta.get("precedent_value") or "").startswith("Source-derived official action page"):
            meta["precedent_value"] = "Official source-backed record; further primary filings can refine procedural detail."

    for key in changed_scalar_keys:
        if key in meta and meta.get(key) != original_meta.get(key):
            fm_text = set_scalar_field(fm_text, key, meta.get(key))

    for key in list_keys:
        if key in meta and as_list(meta.get(key)) != as_list(original_meta.get(key)):
            fm_text = set_list_field(fm_text, key, as_list(meta.get(key)))

    return fm_text


def repair_placeholder_body(
    meta: dict[str, Any],
    category: str,
    body: str,
    issues: str,
) -> tuple[bool, str, str | None, int]:
    body_without_refs, refs = strip_references(body)
    body_without_refs = ENRICHMENT_RE.sub("\n", body_without_refs).rstrip()
    generated_repair_body = "linked source set" in body_without_refs and "## Source Coverage" in body_without_refs
    needs_placeholder_repair = "placeholder_language" in issues and has_placeholder_language(body_without_refs)
    needs_low_confidence_repair = generated_repair_body and has_low_confidence_text(body_without_refs)
    needs_fragment_repair = generated_repair_body and has_fragment_summary(body_without_refs)
    if not (needs_placeholder_repair or needs_low_confidence_repair or needs_fragment_repair):
        return False, body, None, 0

    records = safe_source_records(meta, body)
    new_pre_refs, facts_used = safe_replacement_body(meta, category, records)
    summary = safe_summary_text(meta, category, records)
    new_body = new_pre_refs
    if refs:
        new_body += "\n" + refs.rstrip() + "\n"
    return True, new_body, summary, facts_used


def repair_row(row: dict[str, str], url_map: dict[str, str], dry_run: bool) -> RepairResult:
    category = row["category"]
    slug = row["slug"]
    issues = row.get("issues", "")
    path = page_path(category, slug)
    result = RepairResult(category=category, slug=slug)
    if not path.exists():
        return result

    original_text = path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(original_text)
    original_body = body
    post = frontmatter.load(path)
    original_meta = copy.deepcopy(post.metadata)
    meta = copy.deepcopy(post.metadata)

    if "source_count_mismatch" in issues:
        source_count_fixed, source_links_added = repair_sources(meta, body, url_map)
        result.source_count_fixed = source_count_fixed
        result.source_links_added = source_links_added
    result.crime_links_added = repair_crime_links(meta, category, issues)

    title_fixed, operation_name_fixed, body = repair_title_and_body(meta, body, issues)
    result.title_fixed = title_fixed
    result.operation_name_fixed = operation_name_fixed
    generated_phrase_fixed, body = normalize_generated_phrases(meta, body)
    result.generated_phrase_fixed = generated_phrase_fixed

    placeholder_replaced, body, summary, _facts_used = repair_placeholder_body(meta, category, body, issues)
    result.placeholder_replaced = placeholder_replaced
    body = remove_low_confidence_bullets(body)

    touch_updated = meta != original_meta or body != original_body or summary is not None
    fm_text = sync_frontmatter_text(fm_text, original_meta, meta, summary, touch_updated)
    new_text = fm_text + body
    if not new_text.endswith("\n"):
        new_text += "\n"

    result.changed = new_text != original_text
    if result.changed and not dry_run:
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return result


def render_report(results: list[RepairResult], dry_run: bool) -> str:
    changed = [result for result in results if result.changed]
    lines = [
        "---",
        "title: Low-Priority Wiki Integrity Repair (2026-04-26)",
        "type: analysis",
        "created: 2026-04-26",
        "updated: 2026-04-26",
        'summary: "Execution report for repairing low-priority wiki integrity and placeholder-language audit findings."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This pass uses `_workspace/content_depth_audit_2026-04-26.csv` to repair residual low-priority wiki integrity findings after the targeted enrichment queue was cleared.",
        "",
        f"- Mode: **{'dry-run' if dry_run else 'write'}**",
        f"- Audit rows processed: **{len(results)}**",
        f"- Pages changed: **{len(changed)}**",
        f"- Placeholder bodies replaced: **{sum(1 for result in results if result.placeholder_replaced)}**",
        f"- Source-count fields fixed: **{sum(1 for result in results if result.source_count_fixed)}**",
        f"- Source links added from reference URLs: **{sum(result.source_links_added for result in results)}**",
        f"- Crime classification links added: **{sum(result.crime_links_added for result in results)}**",
        f"- Generated operation titles repaired: **{sum(1 for result in results if result.title_fixed)}**",
        f"- Unresolved operation-name labels repaired: **{sum(1 for result in results if result.operation_name_fixed)}**",
        f"- Generated prose phrases normalized: **{sum(1 for result in results if result.generated_phrase_fixed)}**",
        "",
        "## Changed Pages",
        "",
        "| Page | Type | Placeholder | Source Count | Source Links | Crime Links | Title | Operation Name | Prose |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for result in changed:
        lines.append(
            f"| [[{result.slug}]] | {result.category[:-1]} | {'yes' if result.placeholder_replaced else 'no'} | {'yes' if result.source_count_fixed else 'no'} | {result.source_links_added} | {result.crime_links_added} | {'yes' if result.title_fixed else 'no'} | {'yes' if result.operation_name_fixed else 'no'} | {'yes' if result.generated_phrase_fixed else 'no'} |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Repair low-priority wiki integrity findings from the content-depth audit.")
    parser.add_argument("--audit", default=str(AUDIT_PATH.relative_to(ROOT)))
    parser.add_argument("--report", default=str(REPORT_PATH.relative_to(ROOT)))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    rows = load_rows(ROOT / args.audit)
    actionable = rows
    url_map = build_source_url_map()
    results = [repair_row(row, url_map, dry_run=args.dry_run) for row in actionable]

    report = render_report(results, args.dry_run)
    report_path = ROOT / args.report
    if not args.dry_run:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8", newline="\n")

    print(f"Audit rows processed: {len(results)}")
    print(f"Pages changed: {sum(1 for result in results if result.changed)}")
    print(f"Placeholder bodies replaced: {sum(1 for result in results if result.placeholder_replaced)}")
    print(f"Source-count fields fixed: {sum(1 for result in results if result.source_count_fixed)}")
    print(f"Source links added from reference URLs: {sum(result.source_links_added for result in results)}")
    print(f"Crime classification links added: {sum(result.crime_links_added for result in results)}")
    print(f"Generated operation titles repaired: {sum(1 for result in results if result.title_fixed)}")
    print(f"Unresolved operation-name labels repaired: {sum(1 for result in results if result.operation_name_fixed)}")
    print(f"Generated prose phrases normalized: {sum(1 for result in results if result.generated_phrase_fixed)}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
