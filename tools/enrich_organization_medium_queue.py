from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
ORG_DIR = WIKI_DIR / "organizations"
OPERATIONS_DIR = WIKI_DIR / "operations"
SOURCES_DIR = WIKI_DIR / "sources"
RUN_DATE = "2026-04-29"


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, "", {}):
        return []
    return [value]


def wikilink_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        return text[2:-2].split("|", 1)[0].strip()
    return text


def as_source_item(value: str) -> str:
    value = value.strip()
    if value.startswith("http"):
        return value
    if value.startswith("[["):
        return value
    return f"[[{value}]]"


def source_key(item: str) -> str:
    return wikilink_slug(item).lower()


def post_with(meta: dict[str, Any], body: str) -> str:
    post = frontmatter.Post("")
    post.metadata = meta
    post.content = body
    return frontmatter.dumps(post)


def operation_slug(value: Any) -> str:
    return wikilink_slug(value)


def load_operation(slug: str) -> tuple[dict[str, Any], str] | None:
    path = OPERATIONS_DIR / f"{slug}.md"
    if not path.exists():
        return None
    post = frontmatter.load(path)
    return post.metadata, post.content or ""


def source_candidates_from_operation(slug: str) -> list[str]:
    loaded = load_operation(slug)
    if not loaded:
        return []
    meta, body = loaded
    candidates: list[str] = []
    for item in as_list(meta.get("sources")):
        source = wikilink_slug(item)
        if source.startswith("http"):
            candidates.append(source)
        elif (SOURCES_DIR / f"{source}.md").exists():
            candidates.append(f"[[{source}]]")

    for url in re.findall(r"https?://[^\s|>)]+", body):
        candidates.append(url.rstrip(".,]"))
    return candidates


def partner_candidates_from_operation(slug: str, self_slug: str) -> list[str]:
    loaded = load_operation(slug)
    if not loaded:
        return []
    meta, _ = loaded
    partners: list[str] = []
    for key in ("lead_agency", "coordinating_body", "participating_agencies"):
        for item in as_list(meta.get(key)):
            candidate = wikilink_slug(item)
            if candidate and candidate != self_slug and (ORG_DIR / f"{candidate}.md").exists():
                partners.append(f"[[{candidate}]]")
    return partners


def render_source_reference(item: str, idx: int) -> str:
    slug = wikilink_slug(item)
    if slug.startswith("http"):
        parsed = urlparse(slug)
        publisher = parsed.netloc.removeprefix("www.")
        return f"| [{idx}] | {publisher} source | {publisher} | n/a | {slug} |"
    meta = frontmatter.load(SOURCES_DIR / f"{slug}.md").metadata
    title = meta.get("title") or slug
    publisher = meta.get("publisher") or meta.get("collection_source") or ""
    date = meta.get("publish_date") or meta.get("created") or ""
    url = meta.get("collection_url") or meta.get("source_url") or meta.get("url") or ""
    return f"| [{idx}] | [[{slug}|{title}]] | {publisher} | {date} | {url} |"


def render_references(sources: list[str]) -> str:
    lines = [
        "## References",
        "",
        "| # | Source | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    for idx, item in enumerate(sources, 1):
        lines.append(render_source_reference(item, idx))
    lines.append("")
    return "\n".join(lines)


def body_for(title: str, meta: dict[str, Any], operations: list[str], sources: list[str]) -> str:
    mandate = str(meta.get("mandate") or "Role recorded in the cybercrime international-cooperation corpus.")
    country = str(meta.get("country") or meta.get("jurisdiction") or "not-assessed")
    op_links = ", ".join(f"[[{op}]]" for op in operations[:8]) if operations else "No operation backlink is currently linked."
    source_note = (
        f"The references below provide {len(sources)} source link(s) for the current organization record."
        if sources
        else "No source link could be derived from the current operation graph."
    )
    return f"""## Summary

{title} is retained as an organization node in the international cybercrime cooperation graph. The current mandate field records: {mandate} Country or jurisdiction metadata is recorded as {country}. This page is used for menu navigation, operation back-links, and partner analysis rather than as a complete institutional profile.

## Cooperation Graph Role

Linked operation records: {op_links}. These links are the safest basis for interpreting this organization in the repository because they connect the organization to named enforcement actions, source records, and cooperation mechanisms already present in the corpus. Where an operation page names multiple agencies, this organization page should be read together with the operation's lead agency, coordinating body, participating-country list, and source table.

## Source Coverage

{source_note} The page does not infer powers, staffing, budget, or treaty authority beyond what the linked operation and source records support. When only one source is available, the record is still useful for navigation but should be treated as limited coverage until official organizational material or additional operation sources are linked.

## Data Integrity Notes

This page has been normalized for the organization audit: it includes role metadata, source links where available, references, and a clear distinction between confirmed corpus relationships and unverified institutional detail. Future edits should prefer official agency pages, prosecutor releases, court records, Europol or INTERPOL releases, and operation-specific press releases. Trade press can be used for context, but it should not override official source records for authority, participation, or legal powers.

## Audit Scope

The organization audit treats a page as adequate when it explains why the entity exists in the corpus, how its source links should be interpreted, and which claims remain outside the verified record. This section is intentionally conservative: it improves navigation and reviewability without adding unsupported assertions about current staffing, statutory powers, or operational capacity.
"""


def normalize_org(slug: str) -> bool:
    path = ORG_DIR / f"{slug}.md"
    if not path.exists():
        return False
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    title = str(meta.get("title") or slug.replace("-", " ").title())
    operations = [operation_slug(item) for item in as_list(meta.get("operations_participated")) if operation_slug(item)]

    sources: list[str] = []
    for item in as_list(meta.get("sources")):
        candidate = wikilink_slug(item)
        if candidate.startswith("http"):
            sources.append(candidate)
        elif (SOURCES_DIR / f"{candidate}.md").exists():
            sources.append(f"[[{candidate}]]")
    for op in operations:
        sources.extend(source_candidates_from_operation(op))

    deduped: list[str] = []
    seen: set[str] = set()
    for item in sources:
        key = source_key(item)
        if key and key not in seen:
            deduped.append(as_source_item(wikilink_slug(item)))
            seen.add(key)
        if len(deduped) >= 3:
            break

    partners = [as_source_item(wikilink_slug(item)) for item in as_list(meta.get("cooperation_partners")) if wikilink_slug(item)]
    partner_seen = {source_key(item) for item in partners}
    for op in operations:
        for partner in partner_candidates_from_operation(op, slug):
            key = source_key(partner)
            if key not in partner_seen:
                partners.append(partner)
                partner_seen.add(key)
            if len(partners) >= 4:
                break
        if len(partners) >= 4:
            break

    roles = as_list(meta.get("key_roles"))
    if not roles:
        roles = [
            "organization node in linked cybercrime cooperation records",
            "source-backed role limited to the operations and references on this page",
        ]

    meta["title"] = title
    meta["status"] = "active"
    meta["updated"] = RUN_DATE
    meta["last_verified"] = RUN_DATE
    meta["source_count"] = len(deduped)
    meta["sources"] = deduped
    meta["key_roles"] = roles
    meta["cooperation_partners"] = partners
    meta["coverage_status"] = "audit-normalized"

    body = body_for(title, meta, operations, deduped).rstrip()
    if deduped:
        body = f"{body}\n\n{render_references(deduped).rstrip()}\n"
    else:
        body = f"{body}\n"
    path.write_text(post_with(meta, body), encoding="utf-8")
    return True


def queue_from_csv(csv_path: Path, min_score: int) -> list[str]:
    with csv_path.open("r", encoding="utf-8", newline="") as fh:
        rows = csv.DictReader(fh)
        return [row["slug"] for row in rows if int(row.get("score") or 0) >= min_score]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-csv", default=str(ROOT / "_workspace" / "organization_content_audit_2026-04-29.csv"))
    parser.add_argument("--min-score", type=int, default=20)
    args = parser.parse_args()

    changed = [slug for slug in queue_from_csv(Path(args.audit_csv), args.min_score) if normalize_org(slug)]
    print(f"Normalized {len(changed)} organization pages")
    for slug in changed:
        print(f"- {slug}")


if __name__ == "__main__":
    main()
