from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
OPS_DIR = WIKI_DIR / "operations"
CASES_DIR = WIKI_DIR / "cases"
SOURCES_DIR = WIKI_DIR / "sources"
RAW_DIR = ROOT / "raw"
WORKSPACE = ROOT / "_workspace"
DEFAULT_QUEUE = WORKSPACE / "content_enrichment_queue_2026-04-26.csv"
REPORT_PATH = WIKI_DIR / "analysis" / "targeted-content-enrichment-2026-04-26.md"

START_MARKER = "<!-- SOURCE_ENRICHMENT_START -->"
END_MARKER = "<!-- SOURCE_ENRICHMENT_END -->"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
REFS_RE = re.compile(r"^## (References|참고문헌)\b", re.I | re.M)
ENRICHMENT_RE = re.compile(
    rf"\n?{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}\n?",
    re.DOTALL,
)

PLACEHOLDER_PATTERNS = (
    "source-derived",
    "structured placeholder",
    "should be expanded",
    "should be refined",
    "procedural enrichment",
    "case page generated from",
    "page generated from",
    "official action title from the source corpus",
    "no visible cross-border mechanism is documented",
    "not treated as a separate international-cooperation operation",
)

QUALITY_SECTION_PATTERNS = {
    "timeline": re.compile(r"^## .*?(Timeline|Proceedings|Operational Timeline)", re.I | re.M),
    "ic": re.compile(r"^## .*?(International Cooperation|Cooperation|Participating)", re.I | re.M),
    "legal": re.compile(r"^## .*?(Legal|Law|Framework|Analysis)", re.I | re.M),
    "evidence": re.compile(r"^## .*?(Evidence|Attribution|Forensics)", re.I | re.M),
    "results": re.compile(r"^## .*?(Results|Impact|Outcomes)", re.I | re.M),
    "sources": re.compile(r"^## .*?(Source Coverage|References)", re.I | re.M),
}

BOILERPLATE_PATTERNS = (
    "here's how you know",
    "a .gov website belongs",
    "secure .gov websites use https",
    "the site is secure",
    "share sensitive information only",
    "source was generated from",
    "make the raw corpus addressable",
    "domestic-only",
    "has been absorbed",
    "no visible cross-border mechanism",
    "not treated as a separate",
    "structured placeholder",
    "should be enriched",
    "should be refined",
    "may still be needed",
)


@dataclass(frozen=True)
class SourceRecord:
    slug: str
    title: str
    publisher: str
    date: str
    url: str
    facts: list[str]
    word_count: int


@dataclass(frozen=True)
class EnrichmentResult:
    slug: str
    category: str
    path: Path
    recommendation: str
    source_records: int
    facts_used: int
    placeholder_replaced: bool
    changed: bool


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def wikilink_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        return text[2:-2].split("|", 1)[0].strip()
    return text


def wikilink_label(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2]
        if "|" in inner:
            return inner.split("|", 1)[1].strip()
        text = inner
    text = text.strip("'\"")
    slug_labels = {
        "bec-ic": "BEC",
        "malware-ic": "malware",
        "ransomware-ic": "ransomware",
        "dark-web-ic": "dark web",
        "csam-ic": "CSAM",
        "online-fraud-ic": "online fraud",
        "hacking-ic": "hacking",
        "drug-trafficking-ic": "drug trafficking",
        "money-laundering-ic": "money laundering",
        "informal-cooperation": "informal cooperation",
        "mutual-legal-assistance": "mutual legal assistance",
    }
    if text in slug_labels:
        return slug_labels[text]
    text = re.sub(r"[-_]+", " ", text)
    return " ".join(part.capitalize() for part in text.split()) if text else ""


def clean_text(text: Any, limit: int = 360) -> str:
    value = str(text or "")
    value = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", value)
    value = re.sub(r"\[\[([^\]]+)\]\]", lambda m: wikilink_label(m.group(0)), value)
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"<https?://[^>]+>", "", value)
    value = re.sub(r"https?://\S+", "", value)
    value = value.replace("''", "'")
    value = re.sub(r"^#+\s*", "", value)
    value = re.sub(r"\s+", " ", value).strip(" -\t\r\n")
    if len(value) > limit:
        truncated = value[:limit].strip()
        sentence_end = max(truncated.rfind("."), truncated.rfind("!"), truncated.rfind("?"))
        if sentence_end >= 120:
            value = truncated[: sentence_end + 1]
        else:
            value = truncated.rsplit(" ", 1)[0].rstrip(" ,;:")
            if value and value[-1] not in ".!?":
                value += "."
    return value


def is_boilerplate(text: str) -> bool:
    low = text.lower()
    return any(pattern in low for pattern in BOILERPLATE_PATTERNS + PLACEHOLDER_PATTERNS)


def sentence_split(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9가-힣][A-Za-z0-9가-힣'.,:%$€£-]*", text))


def split_frontmatter(text: str) -> tuple[str, str]:
    match = FM_RE.match(text)
    if not match:
        return "", text
    return text[: match.end()], text[match.end() :]


def strip_references(body: str) -> tuple[str, str]:
    match = REFS_RE.search(body)
    if not match:
        return body.rstrip(), ""
    return body[: match.start()].rstrip(), body[match.start():].lstrip()


def existing_quality_sections(body: str) -> set[str]:
    return {name for name, pattern in QUALITY_SECTION_PATTERNS.items() if pattern.search(body)}


def has_placeholder_language(body: str) -> bool:
    low = body.lower()
    return any(pattern in low for pattern in PLACEHOLDER_PATTERNS)


def extract_section(content: str, heading: str) -> str:
    pattern = re.compile(rf"^## {re.escape(heading)}\s*\n(.*?)(?=^##\s+|\Z)", re.I | re.M | re.S)
    match = pattern.search(content)
    return match.group(1).strip() if match else ""


def parse_reference_rows(body: str) -> list[dict[str, str]]:
    _, refs = strip_references(body)
    rows: list[dict[str, str]] = []
    for line in refs.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 4 or cells[0].lower() in {"#", "[#]"}:
            continue
        title = cells[1] if len(cells) >= 2 else ""
        publisher = cells[2] if len(cells) >= 3 else ""
        date = cells[3] if len(cells) >= 4 else ""
        url = cells[4] if len(cells) >= 5 else ""
        url_match = re.search(r"https?://[^\s)>]+", url)
        rows.append(
            {
                "title": re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title),
                "publisher": publisher,
                "date": date,
                "url": url_match.group(0) if url_match else url,
            }
        )
    return rows


def load_raw_summary(source_post: frontmatter.Post) -> list[str]:
    raw_path = source_post.metadata.get("raw_path")
    if not raw_path:
        return []
    path = ROOT / str(raw_path)
    if not path.exists():
        return []
    try:
        raw_post = frontmatter.load(path)
    except Exception:
        return []
    summary = extract_section(raw_post.content or "", "Summary")
    if not summary:
        return []
    facts: list[str] = []
    for sentence in sentence_split(summary):
        cleaned = clean_text(sentence)
        if len(cleaned) >= 55 and not is_boilerplate(cleaned):
            facts.append(cleaned)
    return facts[:3]


def source_facts_from_post(post: frontmatter.Post) -> list[str]:
    facts: list[str] = []
    for item in as_list(post.metadata.get("key_findings")):
        candidates = sentence_split(str(item))
        if not candidates:
            candidates = [str(item)]
        for candidate in candidates:
            cleaned = clean_text(candidate)
            if len(cleaned) >= 45 and not is_boilerplate(cleaned):
                facts.append(cleaned)

    for heading in ("Source Summary", "Summary", "Why this source matters"):
        section = extract_section(post.content or "", heading)
        for sentence in sentence_split(section):
            cleaned = clean_text(sentence)
            if len(cleaned) >= 55 and not is_boilerplate(cleaned):
                facts.append(cleaned)
        if facts:
            break

    facts.extend(load_raw_summary(post))
    return dedupe_texts(facts, limit=8)


def source_records(meta: dict[str, Any], body: str) -> list[SourceRecord]:
    ref_rows = parse_reference_rows(body)
    records: list[SourceRecord] = []
    seen: set[str] = set()
    for idx, item in enumerate(as_list(meta.get("sources"))):
        slug = wikilink_slug(item)
        if not slug or slug in seen:
            continue
        seen.add(slug)
        path = SOURCES_DIR / f"{slug}.md"
        fallback = ref_rows[idx] if idx < len(ref_rows) else {}
        if path.exists():
            try:
                post = frontmatter.load(path)
            except Exception:
                post = frontmatter.Post({}, "")
            source_meta = post.metadata
            records.append(
                SourceRecord(
                    slug=slug,
                    title=str(source_meta.get("title") or fallback.get("title") or slug),
                    publisher=str(source_meta.get("publisher") or source_meta.get("collection_source") or fallback.get("publisher") or ""),
                    date=str(source_meta.get("publish_date") or fallback.get("date") or ""),
                    url=str(source_meta.get("collection_url") or fallback.get("url") or ""),
                    facts=source_facts_from_post(post),
                    word_count=int(source_meta.get("word_count") or 0),
                )
            )
        else:
            records.append(
                SourceRecord(
                    slug=slug,
                    title=str(fallback.get("title") or slug),
                    publisher=str(fallback.get("publisher") or ""),
                    date=str(fallback.get("date") or ""),
                    url=str(fallback.get("url") or ""),
                    facts=[],
                    word_count=0,
                )
            )

    if records:
        return records

    for row in ref_rows:
        records.append(
            SourceRecord(
                slug="",
                title=row.get("title", ""),
                publisher=row.get("publisher", ""),
                date=row.get("date", ""),
                url=row.get("url", ""),
                facts=[],
                word_count=0,
            )
        )
    return records


def dedupe_texts(values: list[str], limit: int) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for value in values:
        cleaned = clean_text(value)
        if not cleaned or is_boilerplate(cleaned):
            continue
        key = re.sub(r"[^a-z0-9가-힣]+", "", cleaned.lower())[:160]
        if key in seen:
            continue
        seen.add(key)
        output.append(cleaned)
        if len(output) >= limit:
            break
    return output


def fact_pool(records: list[SourceRecord]) -> list[str]:
    facts: list[str] = []
    for record in records:
        facts.extend(record.facts)
    return dedupe_texts(facts, limit=12)


def fmt_list(values: list[Any], limit: int = 14) -> str:
    labels = [wikilink_label(value) for value in values if wikilink_label(value)]
    labels = dedupe_texts(labels, limit=limit)
    if not labels:
        return ""
    if len(labels) == 1:
        return labels[0]
    if len(labels) == 2:
        return f"{labels[0]} and {labels[1]}"
    suffix = "" if len(labels) <= limit else f", plus {len(labels) - limit} more"
    return ", ".join(labels[:limit]) + suffix


def result_lines(meta: dict[str, Any]) -> list[str]:
    results = meta.get("results") if isinstance(meta.get("results"), dict) else {}
    lines: list[str] = []
    numeric_labels = {
        "arrests": "arrests",
        "indictments": "indictments",
        "servers_seized": "servers seized",
        "domains_seized": "domains seized",
        "decryption_keys_recovered": "decryption keys recovered",
        "victims_notified": "victims notified",
    }
    for key, label in numeric_labels.items():
        value = results.get(key)
        if value not in (None, "", 0, "0"):
            lines.append(f"{value} {label}")
    crypto = results.get("cryptocurrency_seized")
    if crypto:
        lines.append(f"cryptocurrency seizure reported as {crypto}")
    for item in as_list(results.get("other")):
        cleaned = clean_text(item, limit=180)
        if cleaned:
            lines.append(cleaned)
    return dedupe_texts(lines, limit=8)


def timeline_lines(meta: dict[str, Any], records: list[SourceRecord]) -> list[str]:
    timeframe = meta.get("timeframe") if isinstance(meta.get("timeframe"), dict) else {}
    lines: list[str] = []
    for key, label in (("start", "activity or investigation start"), ("announced", "public announcement"), ("end", "reported enforcement endpoint")):
        value = timeframe.get(key)
        if value:
            lines.append(f"{value}: {label}.")
    source_dates = sorted({record.date for record in records if record.date})[:5]
    for date in source_dates:
        publishers = sorted({record.publisher for record in records if record.date == date and record.publisher})
        if publishers:
            lines.append(f"{date}: public source coverage from {', '.join(publishers[:4])}.")
    return dedupe_texts(lines, limit=8)


def source_coverage_lines(records: list[SourceRecord]) -> list[str]:
    lines: list[str] = []
    for record in records[:8]:
        bits = []
        if record.publisher:
            bits.append(record.publisher)
        if record.date:
            bits.append(record.date)
        descriptor = ", ".join(bits) if bits else "source"
        title = clean_text(record.title, limit=150)
        if title:
            lines.append(f"{descriptor}: {title}.")
    return dedupe_texts(lines, limit=8)


def cooperation_lines(meta: dict[str, Any], category: str) -> list[str]:
    lines: list[str] = []
    lead = wikilink_label(meta.get("lead_agency"))
    coord = wikilink_label(meta.get("coordinating_body"))
    if lead and coord and lead != coord:
        lines.append(f"Lead agency is {lead}, with coordination attributed to {coord}.")
    elif lead:
        lines.append(f"Lead agency is {lead}.")
    elif coord:
        lines.append(f"Coordination body is {coord}.")

    countries = fmt_list(as_list(meta.get("participating_countries")) or as_list(meta.get("jurisdictions")), limit=16)
    if countries:
        lines.append(f"Participating or affected jurisdictions recorded in metadata: {countries}.")

    agencies = fmt_list(as_list(meta.get("participating_agencies")) or as_list(meta.get("cooperating_agencies")), limit=12)
    if agencies:
        lines.append(f"Named agencies and partners include {agencies}.")

    ic = meta.get("ic_elements") if isinstance(meta.get("ic_elements"), dict) else {}
    for key, label in (
        ("mlat_requests", "MLAT or formal assistance"),
        ("evidence_from_abroad", "evidence from abroad"),
        ("foreign_arrests", "foreign arrests"),
        ("asset_freezing", "asset freezing"),
    ):
        values = fmt_list(as_list(ic.get(key)), limit=10)
        if values:
            lines.append(f"{label}: {values}.")
    if ic.get("extradition"):
        lines.append(f"Extradition element: {clean_text(ic.get('extradition'), limit=180)}.")

    mechanisms = fmt_list(as_list(meta.get("mechanisms_used")), limit=8)
    if mechanisms:
        lines.append(f"Recorded cooperation mechanisms include {mechanisms}.")

    if not lines and category == "cases":
        jurisdiction = clean_text(meta.get("jurisdiction"), limit=160)
        if jurisdiction:
            lines.append(f"The case is recorded in {jurisdiction}; no separate foreign-assistance detail is captured in the current metadata.")
    return dedupe_texts(lines, limit=8)


def legal_lines(meta: dict[str, Any], category: str) -> list[str]:
    lines: list[str] = []
    crimes = fmt_list(as_list(meta.get("crime_types")) or as_list(meta.get("crime_type")) or as_list(meta.get("crime_charged")), limit=8)
    if crimes:
        lines.append(f"Recorded crime classification: {crimes}.")
    enforcement = fmt_list(as_list(meta.get("enforcement_type")), limit=8)
    if enforcement:
        lines.append(f"Recorded enforcement posture: {enforcement}.")
    basis = fmt_list(as_list(meta.get("legal_basis")) or as_list(meta.get("legal_frameworks_invoked")), limit=8)
    if basis:
        lines.append(f"Legal or procedural basis recorded in metadata: {basis}.")
    case_type = clean_text(meta.get("case_type") or meta.get("operation_type"), limit=80)
    status = clean_text(meta.get("status"), limit=80)
    if case_type or status:
        lines.append(f"The record is categorized as {case_type or category.rstrip('s')} with status {status or 'not specified'}.")
    related = fmt_list(as_list(meta.get("related_cases")) or as_list(meta.get("related_operations")) or as_list(meta.get("related_operation")), limit=8)
    if related:
        lines.append(f"Related legal or operational records: {related}.")
    return dedupe_texts(lines, limit=8)


def evidence_lines(records: list[SourceRecord], facts: list[str]) -> list[str]:
    lines = facts[:8]
    if not lines:
        rich_records = [record for record in records if record.word_count]
        for record in rich_records[:5]:
            lines.append(f"{record.publisher or record.title} has a parsed source text of {record.word_count} words available for further review.")
    return dedupe_texts(lines, limit=8)


def summary_text(meta: dict[str, Any], category: str, records: list[SourceRecord], facts: list[str]) -> str:
    existing = clean_text(meta.get("summary"), limit=420)
    if existing and not is_boilerplate(existing):
        return existing
    title = clean_text(meta.get("title"), limit=180)
    source_phrase = ""
    if records:
        publishers = sorted({record.publisher for record in records if record.publisher})
        if publishers:
            source_phrase = f" The supporting source set includes {', '.join(publishers[:4])}."
    fact = facts[0] if facts else ""
    if fact:
        return clean_text(f"{title} is recorded as a {category.rstrip('s')} based on the linked source set. {fact}{source_phrase}", limit=520)
    return clean_text(f"{title} is recorded as a {category.rstrip('s')} based on the linked source set.{source_phrase}", limit=520)


def build_enrichment(meta: dict[str, Any], category: str, records: list[SourceRecord], existing_body: str) -> tuple[str, int]:
    facts = fact_pool(records)
    existing = existing_quality_sections(existing_body)
    sections: list[tuple[str, list[str]]] = []

    source_lines = source_coverage_lines(records)
    if source_lines:
        sections.append(("Source Coverage", source_lines))

    timeline = timeline_lines(meta, records)
    if timeline and "timeline" not in existing:
        sections.append(("Operational Timeline", timeline))

    cooperation = cooperation_lines(meta, category)
    if cooperation and "ic" not in existing:
        sections.append(("International Cooperation Details", cooperation))

    legal = legal_lines(meta, category)
    if legal and "legal" not in existing:
        sections.append(("Legal and Procedural Posture", legal))

    evidence = evidence_lines(records, facts)
    if evidence and "evidence" not in existing:
        sections.append(("Evidence and Attribution Notes", evidence))

    results = result_lines(meta)
    if results and "results" not in existing:
        sections.append(("Results and Impact", results))

    if not sections:
        sections.append(("Source Coverage", source_lines or evidence or legal or cooperation))

    lines = [START_MARKER]
    for heading, bullets in sections:
        if not bullets:
            continue
        lines.extend(["", f"## {heading}", ""])
        for bullet in bullets:
            lines.append(f"- {bullet}")
    lines.extend(["", END_MARKER])
    return "\n".join(lines).strip() + "\n", len(facts)


def build_replacement_body(meta: dict[str, Any], category: str, records: list[SourceRecord]) -> tuple[str, int]:
    facts = fact_pool(records)
    summary = summary_text(meta, category, records, facts)
    lines = ["## Summary", "", summary, ""]
    enrichment, facts_used = build_enrichment(meta, category, records, "")
    enrichment = enrichment.replace(START_MARKER + "\n", "").replace("\n" + END_MARKER, "")
    lines.append(enrichment.strip())
    return "\n".join(line for line in lines if line is not None).rstrip() + "\n", facts_used


def update_frontmatter_text(fm_text: str, summary: str | None) -> str:
    if not fm_text:
        return fm_text
    if re.search(r"(?m)^updated:\s*", fm_text):
        fm_text = re.sub(r"(?m)^updated:\s*.*$", "updated: 2026-04-26", fm_text)
    else:
        fm_text = fm_text.replace("\n---\n", "\nupdated: 2026-04-26\n---\n", 1)
    if summary:
        escaped = json.dumps(summary, ensure_ascii=False)
        if re.search(r"(?m)^summary:\s*", fm_text):
            fm_text = re.sub(r"(?m)^summary:\s*.*$", f"summary: {escaped}", fm_text)
        else:
            fm_text = fm_text.replace("\n---\n", f"\nsummary: {escaped}\n---\n", 1)
        fm_text = re.sub(
            r'(?m)^case_number:\s*"Source-derived from [^"]*"\s*$',
            'case_number: "Not specified in available source metadata"',
            fm_text,
        )
        fm_text = re.sub(
            r'(?m)^precedent_value:\s*"Source-derived official action page; procedural enrichment from primary filings may still be needed\."\s*$',
            'precedent_value: "Official source-backed record; further primary filings can refine procedural detail."',
            fm_text,
        )
    return fm_text


def page_path(category: str, slug: str) -> Path:
    directory = OPS_DIR if category == "operations" else CASES_DIR
    return directory / f"{slug}.md"


def load_queue(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def enrich_row(row: dict[str, str], dry_run: bool = False) -> EnrichmentResult:
    category = row["category"]
    slug = row["slug"]
    path = page_path(category, slug)
    text = path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(text)
    post = frontmatter.load(path)
    meta = post.metadata
    body_without_refs, refs = strip_references(body)
    body_without_refs = ENRICHMENT_RE.sub("\n", body_without_refs).rstrip()
    records = source_records(meta, body)
    placeholder_replaced = has_placeholder_language(body_without_refs)

    if placeholder_replaced:
        new_pre_refs, facts_used = build_replacement_body(meta, category, records)
    else:
        enrichment, facts_used = build_enrichment(meta, category, records, body_without_refs)
        new_pre_refs = (body_without_refs.rstrip() + "\n\n" + enrichment).strip() + "\n"

    summary = summary_text(meta, category, records, fact_pool(records)) if placeholder_replaced else None
    new_text = update_frontmatter_text(fm_text, summary) + new_pre_refs
    if refs:
        new_text += "\n" + refs.rstrip() + "\n"

    changed = new_text != text
    if changed and not dry_run:
        path.write_text(new_text, encoding="utf-8", newline="\n")

    return EnrichmentResult(
        slug=slug,
        category=category,
        path=path,
        recommendation=row.get("recommendation", ""),
        source_records=len(records),
        facts_used=facts_used,
        placeholder_replaced=placeholder_replaced,
        changed=changed,
    )


def render_report(results: list[EnrichmentResult], dry_run: bool) -> str:
    changed = [result for result in results if result.changed]
    placeholder = [result for result in results if result.placeholder_replaced]
    no_facts = [result for result in results if result.facts_used == 0]
    lines = [
        "---",
        "title: Targeted Content Enrichment (2026-04-26)",
        "type: analysis",
        "created: 2026-04-26",
        "updated: 2026-04-26",
        'summary: "Execution report for enriching all pages selected by the content enrichment queue."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This report records the targeted enrichment pass over every page selected in `_workspace/content_enrichment_queue_2026-04-26.csv`.",
        "",
        f"- Mode: **{'dry-run' if dry_run else 'write'}**",
        f"- Queue entries processed: **{len(results)}**",
        f"- Pages changed: **{len(changed)}**",
        f"- Placeholder bodies replaced: **{len(placeholder)}**",
        f"- Pages without extracted source facts: **{len(no_facts)}**",
        "",
        "## Processed Pages",
        "",
        "| Page | Type | Recommendation | Sources read | Facts used | Placeholder replaced | Changed |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for result in results:
        lines.append(
            f"| [[{result.slug}]] | {result.category[:-1]} | {result.recommendation} | {result.source_records} | {result.facts_used} | {'yes' if result.placeholder_replaced else 'no'} | {'yes' if result.changed else 'no'} |"
        )
    if no_facts:
        lines.extend(["", "## Follow-Up Needed", ""])
        for result in no_facts:
            lines.append(f"- [[{result.slug}]] has no extracted source-page facts; review source linkage manually.")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich all pages in the targeted content enrichment queue from existing source pages.")
    parser.add_argument("--queue", default=str(DEFAULT_QUEUE.relative_to(ROOT)))
    parser.add_argument("--report", default=str(REPORT_PATH.relative_to(ROOT)))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    queue_path = ROOT / args.queue
    rows = load_queue(queue_path)
    results = [enrich_row(row, dry_run=args.dry_run) for row in rows]

    report = render_report(results, args.dry_run)
    report_path = ROOT / args.report
    if not args.dry_run:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8", newline="\n")

    print(f"Queue entries processed: {len(results)}")
    print(f"Pages changed: {sum(1 for result in results if result.changed)}")
    print(f"Placeholder bodies replaced: {sum(1 for result in results if result.placeholder_replaced)}")
    print(f"Pages without extracted source facts: {sum(1 for result in results if result.facts_used == 0)}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
