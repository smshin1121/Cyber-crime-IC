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
SOURCES_DIR = WIKI_DIR / "sources"

TARGET_CATEGORIES = ("legal-frameworks", "mechanisms", "crime-types", "concepts")
INCOMING_CATEGORIES = ("operations", "cases", "sources", "organizations", "countries")


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
            matched_targets = sorted(linked & target_slugs)
            if not matched_targets:
                continue
            try:
                post = frontmatter.load(path)
                meta = post.metadata
            except Exception:
                meta = {}
            srcs = source_slugs(meta)
            if category == "sources":
                srcs = [path.stem] + srcs
            page = IncomingPage(
                category=category,
                slug=path.stem,
                title=str(meta.get("title") or path.stem),
                sources=srcs,
            )
            for slug in matched_targets:
                incoming_by_slug[slug].append(page)
    for pages in incoming_by_slug.values():
        pages.sort(
            key=lambda item: (
                0 if item.category in {"operations", "cases"} else 1,
                item.category,
                item.slug,
            )
        )
    return incoming_by_slug


def collect_reference_sources(incoming: list[IncomingPage], limit: int) -> list[str]:
    seen: set[str] = set()
    refs: list[str] = []
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


TERM_ALIASES = {
    "access-device-fraud": ("access device fraud", "credit card fraud", "stolen access device", "carding"),
    "asset-freezing": ("asset freeze", "asset freezing", "freezing assets", "restraint of assets"),
    "bank-fraud-ic": ("bank fraud", "online banking fraud", "banking fraud"),
    "counterfeit-goods": ("counterfeit goods", "counterfeit currency", "counterfeit products"),
    "cryptocurrency-seizure": ("cryptocurrency seizure", "seized cryptocurrency", "crypto seizure", "forfeiture of cryptocurrency"),
    "dark-web-ic": ("dark web", "darknet", "tor hidden service", "dark web marketplace"),
    "domain-seizure": ("domain seizure", "domains seized", "domain names seized", "seize domains"),
    "drug-trafficking": ("drug trafficking", "controlled substances", "darknet drug", "fentanyl trafficking"),
    "electronic-evidence": ("electronic evidence", "digital evidence", "stored computer data"),
    "eu-policy-cycle": ("eu policy cycle", "empact"),
    "eurojust-coordination-meeting": ("coordination meeting", "coordination centre", "eurojust"),
    "european-investigation-order": ("european investigation order", " eio "),
    "extradition": ("extradition", "extradited", "extradite"),
    "harmonization-of-cybercrime-laws": ("harmonization of cybercrime laws", "harmonised cybercrime", "harmonized criminal law"),
    "identity-theft": ("identity theft", "stolen identities", "aggravated identity theft"),
    "interpol-asean-desk": ("interpol asean", "asean desk", "asean cyber"),
    "interpol-i24-7": ("i-24/7", "i24/7", "interpol global police communications"),
    "marketplace-admin-liability": ("marketplace administrator", "administrator of", "marketplace admin"),
    "organized-crime-ic": ("organized crime", "organised crime", "criminal network"),
    "search-seizure": ("search and seizure", "searches and seizures", "searched and seized"),
    "sinkholing": ("sinkholing", "sinkhole", "sinkholed"),
}


def direct_term_sources(slug: str, title: str, limit: int) -> list[str]:
    aliases = list(TERM_ALIASES.get(slug, ()))
    clean_title = title.replace("??", " ").replace("IC Perspective", "").strip().lower()
    aliases.extend([slug.replace("-", " "), clean_title])
    aliases = [alias.lower().strip() for alias in aliases if alias and len(alias.strip()) >= 4]
    refs: list[str] = []
    seen: set[str] = set()
    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
            post = frontmatter.load(path)
            meta = post.metadata
        except Exception:
            continue
        if not source_url(meta):
            continue
        haystack = "\n".join(
            [
                path.stem.lower(),
                str(meta.get("title") or "").lower(),
                " ".join(str(item).lower() for item in as_list(meta.get("key_findings"))),
                (post.content or "")[:3000].lower(),
            ]
        )
        if not any(alias in haystack for alias in aliases):
            continue
        if path.stem in seen:
            continue
        seen.add(path.stem)
        refs.append(path.stem)
        if len(refs) >= limit:
            break
    return refs


def existing_stub_targets() -> list[Path]:
    paths: list[Path] = []
    for category in TARGET_CATEGORIES:
        for path in sorted((WIKI_DIR / category).glob("*.md")):
            if path.name.startswith("_"):
                continue
            try:
                post = frontmatter.load(path)
            except Exception:
                continue
            if str(post.metadata.get("status") or "").strip().lower() == "stub":
                paths.append(path)
    return paths


def category_for_path(path: Path) -> str:
    return path.parent.name


def infer_framework_type(slug: str, title: str) -> str:
    lower = f"{slug} {title}".lower()
    if "mlat" in lower:
        return "bilateral-treaty"
    if "cloud" in lower and "agreement" in lower:
        return "executive-agreement"
    if "convention" in lower:
        return "convention"
    if "act" in lower or "statute" in lower or "rico" in lower or "offenses" in lower:
        return "national-legislation"
    return "legal-basis"


def infer_crime_category(slug: str) -> str:
    if any(token in slug for token in ("malware", "ddos", "hacking", "trojan", "infrastructure", "forum")):
        return "cyber-dependent"
    if any(token in slug for token in ("fraud", "laundering", "identity", "drug", "counterfeit", "stalking", "organized")):
        return "cyber-enabled"
    if "csam" in slug:
        return "content-related"
    return "cybercrime-related"


def references_table(refs: list[str]) -> str:
    lines = [
        "| # | Source | Publisher | Date | URL |",
        "|---|--------|-----------|------|-----|",
    ]
    for idx, slug in enumerate(refs, start=1):
        meta = source_meta(slug)
        title = str(meta.get("title") or slug).replace("|", "\\|")
        publisher = str(meta.get("publisher") or "").replace("|", "\\|")
        date = str(meta.get("publish_date") or meta.get("date") or "").replace("|", "\\|")
        url = source_url(meta).replace("|", "%7C")
        lines.append(f"| {idx} | [[{slug}|{title}]] | {publisher} | {date} | {url} |")
    return "\n".join(lines)


def relation_table(incoming: list[IncomingPage], limit: int = 12) -> str:
    lines = [
        "| Record | Type | Why it matters here |",
        "|---|---|---|",
    ]
    for page in incoming[:limit]:
        if page.category == "operations":
            why = "Operation record using this menu node in its legal, crime-type, or cooperation metadata."
        elif page.category == "cases":
            why = "Case record using this node for charging, offence, evidence, or subject-matter classification."
        elif page.category == "sources":
            why = "Source record that explicitly mentions or classifies the node."
        else:
            why = "Context record linked to this node."
        lines.append(f"| [[{page.slug}|{page.title.replace('|', '\\|')}]] | {page.category[:-1]} | {why} |")
    return "\n".join(lines)


def body_for(category: str, slug: str, title: str, incoming: list[IncomingPage], refs: list[str]) -> str:
    op_count = sum(1 for page in incoming if page.category == "operations")
    case_count = sum(1 for page in incoming if page.category == "cases")
    source_count = sum(1 for page in incoming if page.category == "sources")
    examples = ", ".join(f"[[{page.slug}|{page.title}]]" for page in incoming[:4])
    if not examples:
        examples = "no directly linked operation or case records"

    if category == "legal-frameworks":
        summary = (
            f"{title} is a legal-framework node used by the wiki to connect cybercrime cooperation records to "
            "the statutes, treaties, agreements, or charging bases that appear in source-backed operation and case pages."
        )
        relevance = (
            "For international-cooperation analysis, this node should be read as a routing and classification layer: "
            "it identifies where a record depends on formal legal authority, extradition or MLA compatibility, charging statutes, "
            "or a domestic legal basis used alongside cross-border investigative cooperation."
        )
        caution = (
            "This page does not replace a full doctrinal treatment of the instrument. It records how the current corpus uses the node and flags where a direct treaty text, statute text, or official explanatory source should be added later."
        )
    elif category == "mechanisms":
        summary = (
            f"{title} is a cooperation or enforcement mechanism node used to classify how cybercrime matters move across borders, "
            "from evidence handling and police coordination to seizure, takedown, extradition, or public-private disruption work."
        )
        relevance = (
            "Mechanism pages are important because the same operation can involve several procedural layers: urgent preservation, intelligence exchange, formal MLA, joint coordination, infrastructure seizure, and post-takedown remediation."
        )
        caution = (
            "The examples below show corpus usage. They should not be read as proof that every listed operation used the mechanism in exactly the same formal legal posture."
        )
    elif category == "crime-types":
        summary = (
            f"{title} is a crime-type node used to group source-backed operations and cases by the cybercrime conduct at issue."
        )
        relevance = (
            "Crime-type grouping supports comparison across jurisdictions: it shows which offences repeatedly require cross-border evidence, platform cooperation, asset tracing, extradition, or synchronized enforcement."
        )
        caution = (
            "Classification is source-driven. A page may be linked here because the conduct, charge, target service, or operational objective fits the category even when the source uses a different label."
        )
    else:
        summary = (
            f"{title} is a concept node used to normalize recurring technical, legal, or operational terminology across the wiki."
        )
        relevance = (
            "Concept pages connect case-specific facts to reusable analytical vocabulary, making it easier to compare records that use different labels for similar infrastructure, tools, groups, or jurisdictional principles."
        )
        caution = (
            "The page is corpus-grounded and should be expanded with direct technical or legal references when used for specialist analysis."
        )

    return "\n".join(
        [
            "## Summary",
            "",
            summary,
            "",
            f"Current corpus coverage links this node to **{op_count} operation records**, **{case_count} case records**, and **{source_count} source records**. Representative linked records include: {examples}.",
            "",
            "## International-Cooperation Relevance",
            "",
            relevance,
            "",
            "## Corpus Links",
            "",
            relation_table(incoming),
            "",
            "## Data Quality Notes",
            "",
            caution,
            "",
            "This page was expanded from a structural link-preservation stub during the 2026-04-29 menu-data audit. The references below are drawn from already ingested source pages attached to linked operations, cases, or source records.",
            "",
            "## References",
            "",
            references_table(refs),
            "",
        ]
    )


def write_page(path: Path, incoming: list[IncomingPage], refs: list[str]) -> None:
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    category = category_for_path(path)
    slug = path.stem
    title = str(meta.get("title") or slug)

    meta["status"] = "corpus-linked"
    meta["updated"] = "2026-04-29"
    meta["source_count"] = len(refs)
    meta["sources"] = [f"[[{slug}]]" for slug in refs]

    if category == "legal-frameworks":
        meta.setdefault("framework_type", infer_framework_type(slug, title))
        meta.setdefault("scope", {"international_cooperation": True, "evidence": "varies", "substantive_law": "varies"})
    elif category == "mechanisms":
        meta.setdefault("mechanism_type", "cooperation-or-enforcement-mechanism")
    elif category == "crime-types":
        meta.setdefault("category", infer_crime_category(slug))
        meta.setdefault("broadly_criminalized", "varies-by-jurisdiction")
    elif category == "concepts":
        meta.setdefault("concept_type", "corpus-normalization-node")

    post.metadata = meta
    post.content = body_for(category, slug, title, incoming, refs)
    path.write_text(frontmatter.dumps(post), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Expand menu stubs using existing corpus backlinks and source pages.")
    parser.add_argument("--limit", type=int, default=60)
    parser.add_argument("--refs", type=int, default=4)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    targets = existing_stub_targets()
    target_slugs = {path.stem.lower() for path in targets}
    incoming_index = build_incoming_index(target_slugs)

    enriched = 0
    skipped = defaultdict(int)
    for path in targets:
        if enriched >= args.limit:
            break
        incoming = incoming_index.get(path.stem.lower(), [])
        direct_refs = direct_term_sources(path.stem, str(frontmatter.load(path).metadata.get("title") or path.stem), args.refs)
        refs = []
        seen_refs: set[str] = set()
        for slug in direct_refs + collect_reference_sources(incoming, args.refs):
            if slug in seen_refs:
                continue
            seen_refs.add(slug)
            refs.append(slug)
            if len(refs) >= args.refs:
                break
        if not refs:
            if not incoming:
                skipped["no_incoming"] += 1
            skipped["no_reference_sources"] += 1
            continue
        if not args.dry_run:
            write_page(path, incoming, refs)
        enriched += 1
        print(f"{'would enrich' if args.dry_run else 'enriched'} {path.parent.name}/{path.name}: incoming={len(incoming)} refs={len(refs)}")

    print(f"enriched: {enriched}")
    for reason, count in sorted(skipped.items()):
        print(f"skipped_{reason}: {count}")


if __name__ == "__main__":
    main()
