from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
COUNTRIES_DIR = WIKI_DIR / "countries"
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


def post_with(meta: dict[str, Any], body: str) -> str:
    post = frontmatter.Post("")
    post.metadata = meta
    post.content = body
    return frontmatter.dumps(post)


def source_meta(slug: str) -> dict[str, Any]:
    path = SOURCES_DIR / f"{slug}.md"
    if not path.exists():
        raise FileNotFoundError(path)
    return frontmatter.load(path).metadata


def render_references(slugs: list[str]) -> str:
    if not slugs:
        return ""
    lines = [
        "## References",
        "",
        "| # | Source | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    for idx, slug in enumerate(slugs, 1):
        meta = source_meta(slug)
        title = meta.get("title") or slug
        publisher = meta.get("publisher") or meta.get("collection_source") or ""
        date = meta.get("publish_date") or meta.get("created") or ""
        url = meta.get("collection_url") or meta.get("source_url") or meta.get("url") or ""
        lines.append(f"| [{idx}] | [[{slug}|{title}]] | {publisher} | {date} | {url} |")
    lines.append("")
    return "\n".join(lines)


def normalize_body(title: str, source_slugs: list[str]) -> str:
    source_note = (
        "The linked source coverage below is operation-specific. It can support the existence of a country-operation relationship, but it is not enough by itself to verify the country's cybercrime statute, central authority, 24/7 contact point, or treaty posture."
        if source_slugs
        else "No country-specific source page is currently linked in this repository for this country record."
    )
    return f"""## Summary

{title} is retained as a country navigation and relationship node for the international cybercrime cooperation corpus. This page is now an assessment-control record rather than an unsupported country profile: it separates known wiki relationships from legal, institutional, and treaty claims that still require official country-specific sourcing.

## Verification Status

{source_note} As of {RUN_DATE}, unsupported fields are marked `not-assessed` rather than inferred from region, language, or participation in a single operation. That preserves menu integrity by preventing the country index from implying verified cooperation capacity where the corpus does not yet contain enough evidence.

## Follow-up Source Targets

The next reliable sources for this page are official national police or prosecutor cybercrime pages, justice-ministry mutual-assistance pages, Budapest Convention or UN treaty-status records, and primary operation releases naming the country. Until those are linked, use this page for navigation and relationship tracing only. Do not use it as authority for legal-system detail, MLAT performance, 24/7 contact availability, or national cyber-investigative maturity.
"""


def normalize_country(slug: str) -> bool:
    path = COUNTRIES_DIR / f"{slug}.md"
    if not path.exists():
        return False
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    title = str(meta.get("title") or slug.replace("-", " ").title())
    raw_sources = [wikilink_slug(item) for item in as_list(meta.get("sources")) if wikilink_slug(item)]
    existing_sources = [slug for slug in raw_sources if (SOURCES_DIR / f"{slug}.md").exists()]
    unresolved_sources = [slug for slug in raw_sources if slug not in existing_sources]

    meta["type"] = "country"
    meta["title"] = title
    meta["status"] = "needs-official-source-ingestion"
    meta["updated"] = RUN_DATE
    meta["last_verified"] = RUN_DATE
    meta["legal_system"] = meta.get("legal_system") or "not-assessed"
    meta["ic_capacity"] = meta.get("ic_capacity") or "not-assessed"
    if meta.get("treaty_memberships") in (None, "", [], {}):
        meta["treaty_memberships"] = ["not-assessed"]
    meta["source_count"] = len(existing_sources)
    meta["sources"] = [f"[[{source}]]" for source in existing_sources]
    meta["assessment_confidence"] = "limited"
    meta["verification_scope"] = "country profile not verified beyond linked operation/source relationships"
    if unresolved_sources:
        meta["unresolved_source_refs"] = unresolved_sources

    body = normalize_body(title, existing_sources).rstrip()
    refs = render_references(existing_sources)
    if refs:
        body = f"{body}\n\n{refs.rstrip()}\n"
    else:
        body = f"{body}\n"
    path.write_text(post_with(meta, body), encoding="utf-8")
    return True


def load_country_queue(csv_path: Path, min_score: int) -> list[str]:
    with csv_path.open("r", encoding="utf-8", newline="") as fh:
        rows = csv.DictReader(fh)
        slugs = [
            row["slug"]
            for row in rows
            if row.get("category") == "countries" and int(row.get("score") or 0) >= min_score
        ]
    return slugs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-csv", default=str(ROOT / "_workspace" / "menu_data_audit_2026-04-29.csv"))
    parser.add_argument("--min-score", type=int, default=25)
    args = parser.parse_args()

    slugs = load_country_queue(Path(args.audit_csv), args.min_score)
    changed = [slug for slug in slugs if normalize_country(slug)]
    print(f"Normalized {len(changed)} country menu records")
    for slug in changed:
        print(f"- {slug}")


if __name__ == "__main__":
    main()
