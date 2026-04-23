from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import json
import re
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
SOURCES_DIR = ROOT / "wiki" / "sources"
OUT_DIR = ROOT / "wiki" / "analysis"
OUT_MD = OUT_DIR / "multicountry-low-source-survey-2026-04-22.md"
OUT_JSON = OUT_DIR / "multicountry-low-source-survey-2026-04-22.json"
TODAY = "2026-04-22"
MIN_SOURCES = 5

# Keep the list explicit and stable so the survey can be repeated consistently.
PRIORITY_COUNTRIES: list[dict[str, Any]] = [
    {
        "slug": "germany",
        "label": "Germany",
        "domains": ["bka.de", "bsi.bund.de", "bundesanwaltschaft.de", "justiz.de"],
        "query_terms": ["BKA", "Bundeskriminalamt", "cybercrime", "botnet", "darknet"],
    },
    {
        "slug": "france",
        "label": "France",
        "domains": ["interieur.gouv.fr", "gendarmerie.interieur.gouv.fr", "legifrance.gouv.fr"],
        "query_terms": ["gendarmerie", "police judiciaire", "cybercriminalite", "rancongiciel"],
    },
    {
        "slug": "united-kingdom",
        "label": "United Kingdom",
        "domains": ["nationalcrimeagency.gov.uk", "gov.uk", "cps.gov.uk", "judiciary.uk"],
        "query_terms": ["NCA", "ransomware", "fraud", "cyber crime", "court"],
    },
    {
        "slug": "netherlands",
        "label": "Netherlands",
        "domains": ["politie.nl", "om.nl", "rechtspraak.nl"],
        "query_terms": ["politie", "openbaar ministerie", "cybercrime", "botnet"],
    },
    {
        "slug": "belgium",
        "label": "Belgium",
        "domains": ["police.be", "justitie.belgium.be", "cybersecuritybelgium.be"],
        "query_terms": ["federal computer crime unit", "FCCU", "cybercrime", "parket"],
    },
    {
        "slug": "spain",
        "label": "Spain",
        "domains": ["policia.es", "guardiacivil.es", "interior.gob.es", "fiscal.es"],
        "query_terms": ["Policia Nacional", "Guardia Civil", "ciberdelincuencia", "fraude online"],
    },
    {
        "slug": "italy",
        "label": "Italy",
        "domains": ["poliziadistato.it", "interno.gov.it", "giustizia.it"],
        "query_terms": ["Polizia Postale", "cybercrime", "dark web", "ransomware"],
    },
    {
        "slug": "japan",
        "label": "Japan",
        "domains": ["npa.go.jp", "moj.go.jp", "mofa.go.jp", "nisc.go.jp"],
        "query_terms": ["cybercrime", "National Police Agency", "joint operation", "ransomware"],
    },
    {
        "slug": "south-korea",
        "label": "South Korea",
        "domains": ["police.go.kr", "spo.go.kr", "kisa.or.kr", "moj.go.kr"],
        "query_terms": ["cyber", "joint investigation", "voice phishing", "ransomware", "dark web"],
    },
    {
        "slug": "canada",
        "label": "Canada",
        "domains": ["rcmp-grc.gc.ca", "justice.gc.ca", "cyber.gc.ca"],
        "query_terms": ["RCMP", "cybercrime", "ransomware", "fraud", "darknet"],
    },
]

BACKBONE_SOURCES: list[dict[str, Any]] = [
    {
        "label": "Europol",
        "domains": ["europol.europa.eu"],
        "query_terms": ["Europol", "operation", "cybercrime", "ransomware", "darknet"],
    },
    {
        "label": "Eurojust",
        "domains": ["eurojust.europa.eu"],
        "query_terms": ["Eurojust", "judicial cooperation", "joint investigation team", "cybercrime"],
    },
    {
        "label": "INTERPOL",
        "domains": ["interpol.int"],
        "query_terms": ["INTERPOL", "operation", "cybercrime", "fraud", "malware"],
    },
    {
        "label": "Council of Europe",
        "domains": ["coe.int"],
        "query_terms": ["Octopus", "Budapest Convention", "cybercrime profile"],
    },
    {
        "label": "Open Research",
        "domains": ["arxiv.org", "usenix.org", "dl.acm.org"],
        "query_terms": ["botnet", "malware", "ransomware", "takedown", "paper"],
    },
]

SEARCHABLE_BUCKETS = {"retain_and_enrich", "high_risk_review"}


@dataclass
class OperationRecord:
    slug: str
    title: str
    source_count: int
    references_count: int
    bucket: str
    operation_role: str
    participating_countries: list[str]
    participating_agencies: list[str]
    source_slugs: list[str]
    current_domains: list[str]
    current_publishers: list[str]
    current_doj_sources: int
    current_us_sources: int
    target_countries: list[dict[str, Any]]
    survey_queries: list[str]
    notes: list[str]


def wikilink_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2]
        return inner.split("|", 1)[0].strip()
    return text


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def count_references(body: str) -> int:
    if "## References" not in body:
        return 0
    tail = body.split("## References", 1)[1]
    return len(re.findall(r"^\|\s*\[?\d+\]?\s*\|", tail, re.M))


def title_looks_procedural(title: str) -> bool:
    lower = title.lower()
    return any(
        hint in lower
        for hint in (
            "sentenced",
            "pleads guilty",
            "pleaded guilty",
            "indicted",
            "charged",
            "convicted",
            "arraigned",
            "extradited",
        )
    )


def classify_bucket(meta: dict[str, Any], slug: str, title: str, refs: int) -> tuple[str, list[str]]:
    status = str(meta.get("status") or "")
    source_count = int(meta.get("source_count") or 0)
    operation_role = str(meta.get("operation_role") or "")
    countries = len(as_list(meta.get("participating_countries")))
    related_cases = len(as_list(meta.get("related_cases")))
    parent_operation = str(meta.get("parent_operation") or "")
    notes: list[str] = []

    if status == "absorbed":
        return "absorbed", notes

    if source_count >= MIN_SOURCES:
        return "meets_threshold", notes

    if operation_role == "follow-on" and related_cases and countries <= 1:
        notes.append("follow_on_with_case_anchor")
        return "merge_into_case", notes
    if operation_role == "follow-on" and parent_operation:
        notes.append("follow_on_with_parent_operation")
        return "merge_into_parent", notes
    if slug.startswith("operation-us-v-") and related_cases:
        notes.append("operation_us_v_case_duplicate")
        return "merge_into_case", notes
    if title_looks_procedural(title) and related_cases:
        notes.append("procedural_title_with_case_anchor")
        return "merge_into_case", notes
    if countries >= 2:
        notes.append("multinational_or_cross_border")
        return "retain_and_enrich", notes

    notes.append("single_country_or_sparse")
    return "high_risk_review", notes


def load_source_meta(slug: str) -> dict[str, Any] | None:
    path = SOURCES_DIR / f"{slug}.md"
    if not path.exists():
        return None
    try:
        return dict(frontmatter.load(path).metadata)
    except Exception:
        return None


def normalize_domain(url: str) -> str:
    text = str(url or "").strip()
    match = re.search(r"https?://([^/\s]+)", text)
    if match:
        host = match.group(1).lower()
    else:
        host = text.lower()
    return host.removeprefix("www.")


def collect_current_sources(source_slugs: list[str]) -> tuple[list[str], list[str], int, int]:
    domains: list[str] = []
    publishers: list[str] = []
    doj_sources = 0
    us_sources = 0
    for slug in source_slugs:
        meta = load_source_meta(slug)
        if not meta:
            continue
        publisher = str(meta.get("publisher") or "").strip()
        url = str(meta.get("collection_url") or meta.get("source_url") or "").strip()
        domain = normalize_domain(url)
        if domain:
            domains.append(domain)
        if publisher:
            publishers.append(publisher)
        combined = f"{publisher} {domain}".lower()
        if "justice.gov" in combined or "doj" in combined or "usao" in combined:
            doj_sources += 1
        if any(token in combined for token in ("justice.gov", ".gov", "fbi.gov", "ice.gov")):
            us_sources += 1
    return sorted(set(domains)), sorted(set(publishers)), doj_sources, us_sources


def make_country_queries(op: OperationRecord, country: dict[str, Any]) -> list[str]:
    title_query = f"\"{op.title}\""
    slug_terms = op.slug.replace("-", " ")
    query_terms = " ".join(country["query_terms"][:3])
    queries = []
    for domain in country["domains"][:2]:
        queries.append(f"site:{domain} {title_query}")
        queries.append(f"site:{domain} \"{slug_terms}\" {query_terms}")
    return queries


def make_backbone_queries(op: OperationRecord) -> list[str]:
    title_query = f"\"{op.title}\""
    slug_terms = op.slug.replace("-", " ")
    queries = []
    for source in BACKBONE_SOURCES:
        for domain in source["domains"][:1]:
            queries.append(f"site:{domain} {title_query}")
            queries.append(f"site:{domain} \"{slug_terms}\" {' '.join(source['query_terms'][:2])}")
    return queries


def target_countries_for_operation(participating_countries: list[str]) -> list[dict[str, Any]]:
    matched: list[dict[str, Any]] = []
    slugs = set(participating_countries)
    for country in PRIORITY_COUNTRIES:
        if country["slug"] in slugs:
            matched.append(country)

    if matched:
        return matched

    # If the operation does not include one of the 10 target countries,
    # still route it through the same country set for diversification.
    return PRIORITY_COUNTRIES[:4]


def load_operation_record(path: Path) -> OperationRecord:
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    body = post.content or ""
    slug = path.stem
    title = str(meta.get("title") or slug)
    refs = count_references(body)
    source_count = int(meta.get("source_count") or 0)
    bucket, notes = classify_bucket(meta, slug, title, refs)
    countries = [wikilink_slug(v) for v in as_list(meta.get("participating_countries")) if wikilink_slug(v)]
    agencies = [wikilink_slug(v) for v in as_list(meta.get("participating_agencies")) if wikilink_slug(v)]
    source_slugs = [wikilink_slug(v) for v in as_list(meta.get("sources")) if wikilink_slug(v)]
    current_domains, current_publishers, current_doj_sources, current_us_sources = collect_current_sources(source_slugs)
    targets = target_countries_for_operation(countries)

    queries: list[str] = []
    for country in targets:
        queries.extend(make_country_queries(
            OperationRecord(
                slug=slug,
                title=title,
                source_count=source_count,
                references_count=refs,
                bucket=bucket,
                operation_role=str(meta.get("operation_role") or ""),
                participating_countries=countries,
                participating_agencies=agencies,
                source_slugs=source_slugs,
                current_domains=current_domains,
                current_publishers=current_publishers,
                current_doj_sources=current_doj_sources,
                current_us_sources=current_us_sources,
                target_countries=[],
                survey_queries=[],
                notes=notes.copy(),
            ),
            country,
        ))
    queries.extend(make_backbone_queries(
        OperationRecord(
            slug=slug,
            title=title,
            source_count=source_count,
            references_count=refs,
            bucket=bucket,
            operation_role=str(meta.get("operation_role") or ""),
            participating_countries=countries,
            participating_agencies=agencies,
            source_slugs=source_slugs,
            current_domains=current_domains,
            current_publishers=current_publishers,
            current_doj_sources=current_doj_sources,
            current_us_sources=current_us_sources,
            target_countries=[],
            survey_queries=[],
            notes=notes.copy(),
        )
    ))

    if current_doj_sources:
        notes.append(f"doj_heavy:{current_doj_sources}")
    if not countries:
        notes.append("missing_participating_countries")
    if refs != source_count:
        notes.append(f"source_mismatch:{source_count}!={refs}")

    return OperationRecord(
        slug=slug,
        title=title,
        source_count=source_count,
        references_count=refs,
        bucket=bucket,
        operation_role=str(meta.get("operation_role") or ""),
        participating_countries=countries,
        participating_agencies=agencies,
        source_slugs=source_slugs,
        current_domains=current_domains,
        current_publishers=current_publishers,
        current_doj_sources=current_doj_sources,
        current_us_sources=current_us_sources,
        target_countries=targets,
        survey_queries=queries[:18],
        notes=sorted(set(notes)),
    )


def priority_score(record: OperationRecord) -> tuple[int, int, int, str]:
    target_hits = len(record.target_countries)
    return (
        0 if record.bucket == "retain_and_enrich" else 1,
        record.source_count,
        -target_hits,
        record.slug,
    )


def render_markdown(records: list[OperationRecord]) -> str:
    target_records = [r for r in records if r.bucket in SEARCHABLE_BUCKETS and r.source_count < MIN_SOURCES]
    target_records.sort(key=priority_score)
    bucket_counts = Counter(r.bucket for r in target_records)
    doj_heavy = sum(1 for r in target_records if r.current_doj_sources > 0)
    matched_priority = sum(1 for r in target_records if any(c["slug"] in r.participating_countries for c in PRIORITY_COUNTRIES))
    country_counts = Counter(
        country["label"]
        for record in target_records
        for country in record.target_countries
    )

    lines = [
        "---",
        'title: "Multi-Country Low-Source Operation Survey (2026-04-22)"',
        "type: analysis",
        "created: 2026-04-22",
        "updated: 2026-04-22",
        'summary: "Survey queue for operation pages below the 5-source floor, prioritised for non-DOJ enrichment across 10 target countries plus backbone regional sources."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This survey isolates operation pages that still sit below the `5`-source floor and should be enriched rather than passed.",
        "Pages already at `5+` sources are excluded from the search queue.",
        "The search strategy is intentionally non-US-first to reduce current DOJ concentration.",
        "",
        "## Survey Rules",
        "",
        "- Scope: `wiki/operations/*.md` only.",
        "- Pass condition: `source_count >= 5`.",
        "- Search buckets: `retain_and_enrich`, `high_risk_review`.",
        "- Country frame: Germany, France, United Kingdom, Netherlands, Belgium, Spain, Italy, Japan, South Korea, Canada.",
        "- Backbone supplementation: Europol, Eurojust, INTERPOL, Council of Europe, and open research (papers).",
        "- `insane-search` usage: query templates are written for blocked-site retrieval via Jina, TLS impersonation, or browser fallback when ordinary fetches fail.",
        "",
        "## Queue Snapshot",
        "",
        f"- Target operations below threshold: **{len(target_records)}**",
        f"- `retain_and_enrich`: **{bucket_counts['retain_and_enrich']}**",
        f"- `high_risk_review`: **{bucket_counts['high_risk_review']}**",
        f"- Operations already carrying at least one DOJ source: **{doj_heavy}**",
        f"- Operations directly matching one or more target countries: **{matched_priority}**",
        "",
        "## Target Country Coverage",
        "",
        "| Country | Assigned operations |",
        "|---|---:|",
    ]

    for label, count in sorted(country_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| {label} | {count} |")

    lines.extend(
        [
            "",
            "## Priority Queue",
            "",
            "| Operation | Sources | Bucket | Priority countries | Current source domains | Notes |",
            "|---|---:|---|---|---|---|",
        ]
    )

    for record in target_records:
        priority_countries = ", ".join(country["label"] for country in record.target_countries[:4]) or "-"
        domains = ", ".join(record.current_domains[:4]) or "-"
        notes = ", ".join(record.notes[:4]) or "-"
        lines.append(
            f"| [[{record.slug}]] | {record.source_count} | {record.bucket} | {priority_countries} | {domains} | {notes} |"
        )

    lines.extend(
        [
            "",
            "## Search Playbook",
            "",
            "Use the queries below with normal web search first. If the source is blocked, run the same URL through `insane-search` fallbacks in this order: Jina Reader -> curl_cffi TLS impersonation -> Playwright/browser fallback.",
            "",
        ]
    )

    for record in target_records:
        lines.extend(
            [
                f"## {record.slug}",
                "",
                f"- Title: **{record.title}**",
                f"- Current source count: **{record.source_count}** / {MIN_SOURCES}",
                f"- Bucket: `{record.bucket}`",
                f"- Participating countries: {', '.join(record.participating_countries) or 'none recorded'}",
                f"- Participating agencies: {', '.join(record.participating_agencies[:8]) or 'none recorded'}",
                f"- Current domains: {', '.join(record.current_domains) or 'none recorded'}",
                f"- Priority countries: {', '.join(country['label'] for country in record.target_countries)}",
                f"- Search notes: {', '.join(record.notes) or 'none'}",
                "",
                "Query set:",
            ]
        )
        for query in record.survey_queries:
            lines.append(f"- `{query}`")
        lines.append("")

    return "\n".join(lines) + "\n"


def render_json(records: list[OperationRecord]) -> dict[str, Any]:
    target_records = [r for r in records if r.bucket in SEARCHABLE_BUCKETS and r.source_count < MIN_SOURCES]
    target_records.sort(key=priority_score)
    return {
        "generated_at": TODAY,
        "min_sources": MIN_SOURCES,
        "priority_countries": [country["slug"] for country in PRIORITY_COUNTRIES],
        "operations": [
            {
                "slug": record.slug,
                "title": record.title,
                "source_count": record.source_count,
                "references_count": record.references_count,
                "bucket": record.bucket,
                "operation_role": record.operation_role,
                "participating_countries": record.participating_countries,
                "participating_agencies": record.participating_agencies,
                "current_domains": record.current_domains,
                "current_publishers": record.current_publishers,
                "current_doj_sources": record.current_doj_sources,
                "current_us_sources": record.current_us_sources,
                "target_countries": [country["slug"] for country in record.target_countries],
                "target_domains": {
                    country["slug"]: country["domains"]
                    for country in record.target_countries
                },
                "queries": record.survey_queries,
                "notes": record.notes,
            }
            for record in target_records
        ],
    }


def main() -> None:
    records = [
        load_operation_record(path)
        for path in sorted(OPS_DIR.glob("*.md"))
        if not path.name.startswith("_")
    ]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(render_markdown(records), encoding="utf-8")
    OUT_JSON.write_text(json.dumps(render_json(records), ensure_ascii=False, indent=2), encoding="utf-8")
    target_records = [r for r in records if r.bucket in SEARCHABLE_BUCKETS and r.source_count < MIN_SOURCES]
    print(f"WROTE {OUT_MD}")
    print(f"WROTE {OUT_JSON}")
    print(f"TARGET_OPERATIONS {len(target_records)}")
    print(f"DOJ_HEAVY {sum(1 for r in target_records if r.current_doj_sources > 0)}")


if __name__ == "__main__":
    main()
