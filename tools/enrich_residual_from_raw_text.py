from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import frontmatter

from enrich_targeted_content_from_sources import (
    CASES_DIR,
    OPS_DIR,
    ROOT,
    SOURCES_DIR,
    clean_text,
    split_frontmatter,
    strip_references,
    wikilink_slug,
)


AUDIT_PATH = ROOT / "_workspace" / "content_depth_audit_2026-04-26.csv"
REPORT_PATH = ROOT / "wiki" / "analysis" / "residual-raw-text-enrichment-2026-04-26.md"
DEFAULT_RUN_DATE = "2026-04-27"
START = "<!-- RAW_TEXT_HIGHLIGHTS_START -->"
END = "<!-- RAW_TEXT_HIGHLIGHTS_END -->"
ASSESSMENT_START = "<!-- CANONICAL_ASSESSMENT_START -->"
ASSESSMENT_END = "<!-- CANONICAL_ASSESSMENT_END -->"
ASSESSMENT_RE = re.compile(rf"\n?{re.escape(ASSESSMENT_START)}.*?{re.escape(ASSESSMENT_END)}\n?", re.S)
GENERIC_PATTERNS = (
    "recorded as a case based on the linked source set",
    "recorded as a operation based on the linked source set",
    "recorded as an operation based on the linked source set",
    "defendant-specific enforcement action page derived from",
    "follow-on operation catalog record tied to",
    "<!-- raw_text_highlights_start -->",
)

OFFICIAL_DOMAINS = (
    "justice.gov",
    "fbi.gov",
    "ice.gov",
    "secretservice.gov",
    "treasury.gov",
    "europol.europa.eu",
    "eurojust.europa.eu",
    "bka.de",
    "incibe.es",
    "interpol.int",
    "nationalcrimeagency.gov.uk",
    "bsi.bund.de",
    "policia.es",
    "police.uk",
    "gov.uk",
    "cert.pl",
    "politie.nl",
    "polizei.de",
)

KEYWORDS = (
    " announced ",
    " charged ",
    " indicted ",
    " arrested ",
    " sentenced ",
    " seized ",
    " takedown ",
    " dismantled ",
    " disrupted ",
    " operation ",
    " investigation ",
    " law enforcement ",
    " international ",
    " extradition ",
    " assistance ",
    " victims ",
    " domains ",
    " servers ",
    " malware ",
    " ransomware ",
    " darknet ",
    " dark web ",
    " fraud ",
    " laundering ",
    " cryptocurrency ",
    " ddos ",
)

BOILERPLATE = (
    "here's how you know",
    ".gov website belongs",
    "lock locked padlock",
    "secure .gov websites",
    "share sensitive information",
    "doj menu",
    "main menu",
    "about the district",
    "meet the first assistant",
    "former united states attorneys",
    "privacy program",
    "justice manual",
    "photo galleries",
    "for immediate release",
    "press release",
    "share facebook",
    "linkedin",
    "email",
    "contact",
    "main office",
    "federal courthouse",
    "related content",
    "attorneys business opportunities",
    "meet the united states attorney",
    "combating anti-semitism",
    "topic cybercrime component",
    "release darknet drug trafficker",
    "public information officer",
    "updated ",
    "topic ",
    "component ",
    "attorney programs",
    "victim witness assistance",
    "community outreach",
    "project safe childhood",
    "project safe neighborhoods",
    "skip to content",
    "quick exit",
    "cymraeg",
    "show submenu",
    "we-megamenu",
    "learn more about ice",
    "ice check-in",
    "news about hsi",
    "enforcement and removal operations",
    "student and exchange visitor program",
    "report a crime",
    "reporting sars",
    "this is archived content",
    "i am pleased to be joined",
    "made the announcement",
    "linked source material",
    "follow-on operation catalog record",
    "operation-side pointer",
    "source summary",
)

DATE_LINK_RE = re.compile(
    r"^(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2},\s+\d{4}\b",
    re.I,
)


@dataclass
class Result:
    category: str
    slug: str
    changed: bool
    highlights: int
    official_sources: int


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def page_path(category: str, slug: str) -> Path:
    return (OPS_DIR if category == "operations" else CASES_DIR) / f"{slug}.md"


def is_official_url(url: str) -> bool:
    host = urlparse(str(url or "")).netloc.lower()
    return any(host == domain or host.endswith("." + domain) for domain in OFFICIAL_DOMAINS)


def source_meta(slug: str) -> tuple[dict[str, Any], str]:
    seen: set[str] = set()
    current = slug
    fallback: tuple[dict[str, Any], str] = ({}, "")
    while current and current not in seen:
        seen.add(current)
        path = SOURCES_DIR / f"{current}.md"
        if not path.exists():
            return fallback
        post = frontmatter.load(path)
        meta = post.metadata
        content = post.content or ""
        fallback = (meta, content)
        if meta.get("raw_path"):
            return meta, content
        duplicate = wikilink_slug(meta.get("duplicate_of"))
        if not duplicate:
            return meta, content
        current = duplicate
    return fallback


def extracted_text(raw_path: str) -> str:
    path = ROOT / raw_path
    if not path.exists():
        return ""
    try:
        post = frontmatter.load(path)
        text = post.content or ""
    except Exception:
        text = path.read_text(encoding="utf-8", errors="replace")
    marker = re.search(r"^## Extracted Text\s*$", text, re.M)
    if marker:
        return text[marker.end() :].strip()
    return ""


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text)
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]


def is_substantive(sentence: str) -> bool:
    cleaned = clean_text(sentence, limit=360)
    if len(cleaned) < 75 or len(cleaned) > 360:
        return False
    if cleaned.startswith("(") or re.match(r"^(and|or|but|for|to|as well as)\s+", cleaned, re.I):
        return False
    if cleaned.endswith(" U.S.") or cleaned.endswith(" by U.S."):
        return False
    low = f" {cleaned.lower()} "
    if any(pattern in low for pattern in BOILERPLATE):
        return False
    if DATE_LINK_RE.match(cleaned):
        return False
    return any(keyword in low for keyword in KEYWORDS)


def source_highlights(slug: str, limit: int) -> tuple[list[str], str, str]:
    meta, _content = source_meta(slug)
    url = str(meta.get("collection_url") or meta.get("source_url") or meta.get("final_url") or "")
    if not is_official_url(url):
        return [], "", ""
    raw_path = str(meta.get("raw_path") or "")
    if not raw_path:
        return [], "", ""
    text = extracted_text(raw_path)
    if not text:
        return [], "", ""

    highlights: list[str] = []
    seen: set[str] = set()
    for sentence in split_sentences(text):
        cleaned = clean_text(sentence, limit=340)
        if not is_substantive(cleaned):
            continue
        key = re.sub(r"[^a-z0-9]+", "", cleaned.lower())[:180]
        if key in seen:
            continue
        seen.add(key)
        highlights.append(cleaned)
        if len(highlights) >= limit:
            break
    publisher = str(meta.get("publisher") or meta.get("collection_source") or "official source")
    date = str(meta.get("publish_date") or "")
    return highlights, publisher, date


def build_block(meta: dict[str, Any], per_source_limit: int, total_limit: int) -> tuple[str, int, int]:
    lines = [START, "", "## Raw Source Highlights", ""]
    count = 0
    official_sources = 0
    for item in as_list(meta.get("sources")):
        slug = wikilink_slug(item)
        if not slug:
            continue
        highlights, publisher, date = source_highlights(slug, per_source_limit)
        if not highlights:
            continue
        official_sources += 1
        prefix = publisher
        if date:
            prefix += f", {date}"
        for highlight in highlights:
            lines.append(f"- {prefix}: {highlight}")
            count += 1
            if count >= total_limit:
                lines.extend(["", END])
                return "\n".join(lines) + "\n", count, official_sources
    lines.extend(["", END])
    return "\n".join(lines) + "\n", count, official_sources


def remove_existing(body: str) -> str:
    return re.sub(rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?", "\n", body, flags=re.S).strip() + "\n"


def split_assessment(body: str) -> tuple[str, str]:
    match = ASSESSMENT_RE.search(body)
    if not match:
        return body, ""
    block = match.group(0).strip()
    cleaned = body[: match.start()] + "\n" + body[match.end() :]
    return cleaned.strip(), block


def update_frontmatter_date(fm_text: str, updated_date: str = DEFAULT_RUN_DATE) -> str:
    if not fm_text:
        return fm_text
    if re.search(r"(?m)^updated:\s*", fm_text):
        return re.sub(r"(?m)^updated:\s*.*$", f"updated: {updated_date}", fm_text, count=1)
    return fm_text.replace("\n---\n", f"\nupdated: {updated_date}\n---\n", 1)


def target_rows(path: Path, min_score: int) -> list[dict[str, str]]:
    rows = list(csv.DictReader(path.open("r", encoding="utf-8", newline="")))
    return [
        row
        for row in rows
        if int(row.get("score") or 0) >= min_score
        and re.search(r"raw_available_underused|high_source_to_body_gap|missing_quality_sections", row.get("issues", ""))
    ]


def generic_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for category, directory in (("operations", OPS_DIR), ("cases", CASES_DIR)):
        for path in sorted(directory.glob("*.md")):
            text = path.read_text(encoding="utf-8", errors="replace").lower()
            if any(pattern in text for pattern in GENERIC_PATTERNS):
                rows.append({"category": category, "slug": path.stem})
    return rows


def load_queue_rows(path: Path) -> list[dict[str, str]]:
    return [
        {"category": row.get("category", ""), "slug": row.get("slug", "")}
        for row in csv.DictReader(path.open("r", encoding="utf-8", newline=""))
        if row.get("category") and row.get("slug")
    ]


def enrich_row(row: dict[str, str], dry_run: bool, per_source_limit: int, total_limit: int, updated_date: str) -> Result:
    category = row["category"]
    slug = row["slug"]
    path = page_path(category, slug)
    if not path.exists():
        return Result(category, slug, False, 0, 0)
    original = path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(original)
    post = frontmatter.load(path)
    block, highlights, official_sources = build_block(post.metadata, per_source_limit, total_limit)
    had_existing = START in body and END in body
    body_without_refs, refs = strip_references(body)
    body_without_refs = remove_existing(body_without_refs) if had_existing or highlights else body_without_refs
    body_without_refs, assessment = split_assessment(body_without_refs)
    if not highlights:
        if not had_existing:
            return Result(category, slug, False, 0, official_sources)
        new_body = body_without_refs.rstrip()
        if assessment:
            new_body += "\n\n" + assessment.rstrip()
        if refs:
            new_body += "\n\n" + refs.rstrip()
        new_text = update_frontmatter_date(fm_text, updated_date=updated_date) + new_body + "\n"
        if not new_text.endswith("\n"):
            new_text += "\n"
        changed = new_text != original
        if changed and not dry_run:
            path.write_text(new_text, encoding="utf-8", newline="\n")
        return Result(category, slug, changed, 0, official_sources)
    new_body = body_without_refs.rstrip() + "\n\n" + block.rstrip()
    if assessment:
        new_body += "\n\n" + assessment.rstrip()
    if refs:
        new_body += "\n\n" + refs.rstrip()
    new_text = update_frontmatter_date(fm_text, updated_date=updated_date) + new_body
    if not new_text.endswith("\n"):
        new_text += "\n"
    changed = new_text != original
    if changed and not dry_run:
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return Result(category, slug, changed, highlights, official_sources)


def render_report(results: list[Result], dry_run: bool, run_date: str, title: str) -> str:
    changed = [result for result in results if result.changed]
    with_highlights = [result for result in results if result.highlights]
    lines = [
        "---",
        f"title: {title}",
        "type: analysis",
        f"created: {run_date}",
        f"updated: {run_date}",
        'summary: "Execution report for adding official-source raw text highlights to residual content-depth pages."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        f"- Mode: **{'dry-run' if dry_run else 'write'}**",
        f"- Target rows processed: **{len(results)}**",
        f"- Pages changed: **{len(changed)}**",
        f"- Pages with raw-source highlights after execution: **{len(with_highlights)}**",
        f"- Raw-source highlight bullets after execution: **{sum(result.highlights for result in with_highlights)}**",
        f"- Pages with official raw sources used: **{sum(1 for result in with_highlights if result.official_sources)}**",
        "",
        "## Pages With Raw Highlights",
        "",
        "| Page | Type | Highlights | Official Sources | Changed this run |",
        "|---|---|---:|---:|---:|",
    ]
    for result in with_highlights:
        lines.append(
            f"| [[{result.slug}]] | {result.category[:-1]} | {result.highlights} | {result.official_sources} | {'yes' if result.changed else 'no'} |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Add official-source raw text highlights to residual content-depth pages.")
    parser.add_argument("--audit", default=str(AUDIT_PATH.relative_to(ROOT)))
    parser.add_argument("--report", default=str(REPORT_PATH.relative_to(ROOT)))
    parser.add_argument("--queue", default="")
    parser.add_argument("--title", default="Residual Raw Text Enrichment (2026-04-26)")
    parser.add_argument("--date", default=DEFAULT_RUN_DATE)
    parser.add_argument("--min-score", type=int, default=22)
    parser.add_argument("--per-source-limit", type=int, default=3)
    parser.add_argument("--total-limit", type=int, default=9)
    parser.add_argument("--all-generic", action="store_true", help="Process all pages that still contain generated linked-source-set prose.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.queue:
        rows = load_queue_rows(ROOT / args.queue)
    else:
        rows = generic_rows() if args.all_generic else target_rows(ROOT / args.audit, args.min_score)
    results = [enrich_row(row, args.dry_run, args.per_source_limit, args.total_limit, args.date) for row in rows]
    report = render_report(results, args.dry_run, args.date, args.title)
    report_path = ROOT / args.report
    if not args.dry_run:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8", newline="\n")

    print(f"Target rows processed: {len(results)}")
    print(f"Pages changed: {sum(1 for result in results if result.changed)}")
    print(f"Pages with raw-source highlights: {sum(1 for result in results if result.highlights)}")
    print(f"Raw-source highlight bullets: {sum(result.highlights for result in results if result.highlights)}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
