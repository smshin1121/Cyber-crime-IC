from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
COUNTRIES_DIR = WIKI_DIR / "countries"
SOURCES_DIR = WIKI_DIR / "sources"
RUN_DATE = "2026-04-29"

INCOMING_CATEGORIES = ("operations", "cases", "sources", "organizations")


@dataclass(frozen=True)
class IncomingPage:
    category: str
    slug: str
    title: str
    sources: list[str]


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


def source_slugs(meta: dict[str, Any]) -> list[str]:
    return [wikilink_slug(item) for item in as_list(meta.get("sources")) if wikilink_slug(item)]


def source_meta(slug: str) -> dict[str, Any]:
    path = SOURCES_DIR / f"{slug}.md"
    if not path.exists():
        return {}
    try:
        return frontmatter.load(path).metadata
    except Exception:
        return {}


def source_url(meta: dict[str, Any]) -> str:
    return str(meta.get("collection_url") or meta.get("source_url") or meta.get("url") or "").strip()


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9가-힣][A-Za-z0-9가-힣'(),./:%+-]*", text))


def strip_refs(body: str) -> str:
    match = re.search(r"^## References\b", body, re.I | re.M)
    return body[: match.start()] if match else body


def candidate_country_paths() -> list[Path]:
    out: list[Path] = []
    for path in sorted(COUNTRIES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        status = str(meta.get("status") or "").lower()
        source_count = int(meta.get("source_count") or 0)
        body_words = word_count(strip_refs(post.content or ""))
        if status == "stub" or (source_count == 0 and body_words < 140):
            out.append(path)
    return out


def build_incoming_index(target_slugs: set[str]) -> dict[str, list[IncomingPage]]:
    link_pattern = re.compile(r"\[\[([^\]|#]+)")
    incoming_by_slug: dict[str, list[IncomingPage]] = defaultdict(list)
    for category in INCOMING_CATEGORIES:
        directory = WIKI_DIR / category
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name.startswith("_"):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            linked = {match.group(1).strip().lower() for match in link_pattern.finditer(text)}
            matched = sorted(linked & target_slugs)
            if not matched:
                continue
            try:
                post = frontmatter.load(path)
                meta = post.metadata
            except Exception:
                meta = {}
            srcs = source_slugs(meta)
            if category == "sources":
                srcs = [path.stem] + srcs
            page = IncomingPage(category, path.stem, str(meta.get("title") or path.stem), srcs)
            for slug in matched:
                incoming_by_slug[slug].append(page)
    for pages in incoming_by_slug.values():
        pages.sort(key=lambda item: (0 if item.category in {"operations", "cases"} else 1, item.category, item.slug))
    return incoming_by_slug


def direct_country_sources(path: Path, title: str, limit: int) -> list[str]:
    slug = path.stem.lower()
    words = {slug, slug.replace("-", " "), title.lower()}
    candidates: list[str] = []
    for source_path in sorted(SOURCES_DIR.glob("*.md")):
        if source_path.name.startswith("_"):
            continue
        name = source_path.stem.lower()
        if not any(word and word in name for word in words):
            continue
        meta = source_meta(source_path.stem)
        if not meta or not source_url(meta):
            continue
        publisher = str(meta.get("publisher") or "").lower()
        source_title = str(meta.get("title") or "").lower()
        officialish = any(token in publisher for token in ("council of europe", "interpol", "government", "ministry", "police", "unodc", "african union"))
        profileish = any(token in source_title or token in name for token in ("country", "profile", "octopus", "cybercrime", "official", "national"))
        if officialish or profileish:
            candidates.append(source_path.stem)
            if len(candidates) >= limit:
                break
    return candidates


def collect_refs(path: Path, title: str, incoming: list[IncomingPage], limit: int) -> list[str]:
    seen: set[str] = set()
    refs: list[str] = []
    for slug in direct_country_sources(path, title, limit):
        if slug not in seen:
            seen.add(slug)
            refs.append(slug)
    for page in incoming:
        for slug in page.sources:
            if slug in seen:
                continue
            meta = source_meta(slug)
            if not meta or not source_url(meta):
                continue
            seen.add(slug)
            refs.append(slug)
            if len(refs) >= limit:
                return refs
    return refs


def references_table(refs: list[str]) -> str:
    lines = ["| # | Source | Publisher | Date | URL |", "|---|--------|-----------|------|-----|"]
    for idx, slug in enumerate(refs, start=1):
        meta = source_meta(slug)
        title = str(meta.get("title") or slug).replace("|", "\\|")
        publisher = str(meta.get("publisher") or "").replace("|", "\\|")
        date = str(meta.get("publish_date") or meta.get("date") or "").replace("|", "\\|")
        url = source_url(meta).replace("|", "%7C")
        lines.append(f"| {idx} | [[{slug}|{title}]] | {publisher} | {date} | {url} |")
    return "\n".join(lines)


def relation_table(incoming: list[IncomingPage]) -> str:
    lines = ["| Record | Type | Corpus role |", "|---|---|---|"]
    for page in incoming[:12]:
        role = "Linked country in an operation or case record."
        if page.category == "sources":
            role = "Source page mentioning or classifying the country."
        elif page.category == "organizations":
            role = "Organization page connected to this jurisdiction."
        lines.append(f"| [[{page.slug}|{page.title.replace('|', '\\|')}]] | {page.category[:-1]} | {role} |")
    return "\n".join(lines)


def update_country(path: Path, incoming: list[IncomingPage], refs: list[str]) -> None:
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    title = str(meta.get("title") or path.stem.replace("-", " ").title())
    op_count = sum(1 for page in incoming if page.category == "operations")
    case_count = sum(1 for page in incoming if page.category == "cases")
    source_count = sum(1 for page in incoming if page.category == "sources")

    meta["type"] = "country"
    meta["title"] = title
    meta["status"] = "corpus-linked"
    meta["updated"] = RUN_DATE
    meta["source_count"] = len(refs)
    meta["sources"] = [f"[[{slug}]]" for slug in refs]
    meta.setdefault("legal_system", "unknown")
    meta.setdefault(
        "ic_capacity",
        {
            "rating": "not-assessed",
            "digital_forensics": "not-assessed",
            "avg_mlat_response_days": "not-assessed",
        },
    )
    if not meta.get("treaty_memberships"):
        meta["treaty_memberships"] = [
            {
                "framework": "[[budapest-convention]]",
                "status": "not-assessed",
                "date": "",
                "reservations": [],
            }
        ]
    meta.setdefault("operations_participated", [])
    meta.setdefault("key_agencies", [])

    examples = ", ".join(f"[[{page.slug}|{page.title}]]" for page in incoming[:4]) if incoming else "no linked operation or case records"
    body = "\n".join(
        [
            "## Summary",
            "",
            f"{title} is maintained as a country node for the cybercrime international-cooperation corpus. The current page is source-backed only to the level shown in the references below; it does not infer treaty status, cybercrime-unit authority, or MLAT performance beyond the collected sources.",
            "",
            f"Current corpus coverage links this country to **{op_count} operation records**, **{case_count} case records**, and **{source_count} source records**. Representative linked records include: {examples}.",
            "",
            "## International-Cooperation Relevance",
            "",
            "Country pages support comparison across legal systems, treaty channels, cybercrime capacity, and enforcement track records. For this jurisdiction, the current data should be treated as a routing layer: it shows where the country appears in the corpus and which sources are available for verification.",
            "",
            "## Corpus Links",
            "",
            relation_table(incoming) if incoming else "No operation, case, source, or organization backlinks were found in the current corpus.",
            "",
            "## Data Quality Notes",
            "",
            "This page was expanded from a thin or structural record during the 2026-04-29 menu-data audit. Fields marked `not-assessed` mean the repository has not yet ingested enough direct legal or government material to assign a reliable value. Future work should prefer treaty depositary pages, official cybercrime legislation, central-authority guidance, and named law-enforcement unit sources.",
            "",
            "## References",
            "",
            references_table(refs),
            "",
        ]
    )
    post.metadata = meta
    post.content = body
    path.write_text(frontmatter.dumps(post), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Expand thin country pages using existing corpus links and source pages.")
    parser.add_argument("--limit", type=int, default=60)
    parser.add_argument("--refs", type=int, default=4)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    targets = candidate_country_paths()
    incoming_index = build_incoming_index({path.stem.lower() for path in targets})
    enriched = 0
    skipped = defaultdict(int)
    for path in targets:
        if enriched >= args.limit:
            break
        post = frontmatter.load(path)
        title = str(post.metadata.get("title") or path.stem.replace("-", " ").title())
        incoming = incoming_index.get(path.stem.lower(), [])
        refs = collect_refs(path, title, incoming, args.refs)
        if not refs:
            skipped["no_reference_sources"] += 1
            continue
        if not args.dry_run:
            update_country(path, incoming, refs)
        enriched += 1
        print(f"{'would enrich' if args.dry_run else 'enriched'} countries/{path.name}: incoming={len(incoming)} refs={len(refs)}")
    print(f"enriched: {enriched}")
    for reason, count in sorted(skipped.items()):
        print(f"skipped_{reason}: {count}")


if __name__ == "__main__":
    main()
