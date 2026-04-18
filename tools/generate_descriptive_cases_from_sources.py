from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
CASES_DIR = ROOT / "wiki" / "cases"
SOURCES_DIR = ROOT / "wiki" / "sources"
TODAY = "2026-04-18"
TRUSTED_HOSTS = (
    "justice.gov",
    "fbi.gov",
    "secretservice.gov",
    "europol.europa.eu",
    "interpol.int",
    "eurojust.europa.eu",
    "rcmp-grc.gc.ca",
    "afp.gov.au",
    "police.gov.sg",
    "unodc.org",
    "ice.gov",
    "reuters.com",
    "therecord.media",
    "bleepingcomputer.com",
    "thehackernews.com",
    "helpnetsecurity.com",
    "rferl.org",
    "sbs.com.au",
    "cyberscoop.com",
    "gbhackers.com",
    "web.archive.org",
)
ALLOWED_RELIABILITY = {"high", "medium"}
ALLOWED_CREDIBILITY = {"confirmed", "credible", "verified", "high", "medium", ""}
ACTION_RE = re.compile(
    r"\b(charged|indicted|sentenced|convicted|pleads guilty|pleaded guilty|arrested|extradited|seized|forfeiture|admits|admitted|found guilty|detained|jailed|imprisoned)\b",
    re.I,
)
SKIP_RE = re.compile(
    r"\b(report|guidance|profile|annual|remarks|statement|welcomes|network strengthens|page not found|ccips|unit|task force|operation [a-z]+$)\b",
    re.I,
)
GENERIC_NAME_TOKENS = {
    "man", "woman", "national", "defendant", "defendants", "offender", "offenders",
    "trafficker", "developer", "administrator", "administrators", "citizen", "citizens",
    "teenager", "teenagers", "member", "members", "exchange", "marketplace", "drug",
    "dark", "web", "darknet", "market", "county", "district", "charges", "charged",
    "sentenced", "guilty", "pleads", "pleaded", "convicted", "hacking", "seizure",
    "ransomware", "affiliates", "across", "continents", "travel", "child", "offense",
    "official", "operator", "operators", "trafficking", "conspiracy", "leader",
}


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def unwrap_source_name(source_slug: str) -> str:
    parts = source_slug.split("_", 2)
    return parts[2] if len(parts) == 3 else source_slug


def title_from_source_slug(source_slug: str) -> str:
    source_name = unwrap_source_name(source_slug).replace("-", " ")
    source_name = re.sub(r"\s+", " ", source_name).strip()
    if re.match(r"^united states v ", source_name, re.I):
        return "United States v. " + re.sub(r"^united states v ", "", source_name, flags=re.I).title()
    if re.match(r"^in re ", source_name, re.I):
        return "In re " + re.sub(r"^in re ", "", source_name, flags=re.I).title()
    return ""


def existing_context() -> tuple[set[str], set[str], set[str], set[str]]:
    slugs: set[str] = set()
    title_norms: set[str] = set()
    used_sources: set[str] = set()
    defendant_norms: set[str] = set()
    for path in CASES_DIR.glob("*.md"):
        if path.name.startswith("_"):
            continue
        slugs.add(path.stem)
        post = frontmatter.load(path)
        meta = post.metadata
        title_norms.add(norm(str(meta.get("title") or "")))
        for src in meta.get("sources", []) or []:
            text = str(src)
            if text.startswith("[[") and text.endswith("]]"):
                used_sources.add(text[2:-2].split("|", 1)[0].strip())
        for row in meta.get("defendants", []) or []:
            if isinstance(row, dict):
                name = str(row.get("name") or "").strip()
                if name:
                    defendant_norms.add(norm(name))
    return slugs, title_norms, used_sources, defendant_norms


def candidate_sources(limit: int) -> list[tuple[Path, object]]:
    existing_slugs, title_norms, used_sources, defendant_norms = existing_context()
    rows: list[tuple[int, Path, object]] = []
    for path in SOURCES_DIR.glob("*.md"):
        if path.name.startswith("_"):
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        title = str(meta.get("title") or "").strip()
        url = str(meta.get("collection_url") or "").lower()
        if not any(host in url for host in TRUSTED_HOSTS):
            continue
        if not ACTION_RE.search(title) or SKIP_RE.search(title):
            continue
        source_title_norm = norm(title)
        if source_title_norm in title_norms:
            continue
        formal_title = title_from_source_slug(path.stem)
        if formal_title and norm(formal_title) in title_norms:
            continue
        reliability = str(meta.get("reliability") or "").strip().lower()
        credibility = str(meta.get("credibility") or "").strip().lower()
        if reliability not in ALLOWED_RELIABILITY or credibility not in ALLOWED_CREDIBILITY:
            continue
        score = 0
        if not any(host in url for host in TRUSTED_HOSTS):
            continue
        if any(host in url for host in ("justice.gov", "fbi.gov", "secretservice.gov", "ice.gov")):
            score += 5
        defendant_names = [str(v).strip() for v in (meta.get("defendant_names") or []) if str(v).strip()]
        if defendant_names:
            score += 3
        if "united-states-v-" in path.stem or "_in-re-" in path.stem:
            score += 2
        rows.append((score, path, post))
    rows.sort(key=lambda row: (-row[0], row[1].name))
    return [(path, post) for _, path, post in rows[:limit]]


def build_slug(title: str, source_slug: str, existing_slugs: set[str]) -> str:
    base = slugify(title)[:110] or slugify(source_slug)
    slug = base
    idx = 2
    while slug in existing_slugs:
        slug = f"{base}-{idx}"
        idx += 1
    return slug


def infer_status(text: str) -> str:
    lowered = text.lower()
    if "sentenc" in lowered:
        return "sentenced"
    if "convict" in lowered or "found guilty" in lowered:
        return "convicted"
    if "plead" in lowered or "pleads guilty" in lowered:
        return "pleaded guilty"
    if "forfeiture" in lowered or "seized" in lowered:
        return "seizure ordered"
    if "indict" in lowered:
        return "indicted"
    if "charg" in lowered:
        return "charged"
    if "extradit" in lowered:
        return "extradited"
    return "prosecuted"


def infer_case_type(status: str) -> str:
    return "seizure" if "seizure" in status else "prosecution"


def infer_crimes(text: str) -> list[str]:
    lowered = text.lower()
    crimes: list[str] = []
    mapping = [
        ("drug", "[[drug-trafficking]]"),
        ("narcotic", "[[drug-trafficking]]"),
        ("ransomware", "[[ransomware-ic]]"),
        ("malware", "[[malware-ic]]"),
        ("botnet", "[[malware-ic]]"),
        ("bank", "[[bank-fraud-ic]]"),
        ("wire fraud", "[[online-fraud-ic]]"),
        ("identity", "[[carding-fraud-ic]]"),
        ("card", "[[carding-fraud-ic]]"),
        ("darknet", "[[online-fraud-ic]]"),
        ("dark web", "[[online-fraud-ic]]"),
        ("money laundering", "[[money-laundering-ic]]"),
        ("bec", "[[bec-ic]]"),
        ("phishing", "[[online-fraud-ic]]"),
        ("cyber", "[[online-fraud-ic]]"),
        ("hack", "[[malware-ic]]"),
    ]
    for needle, crime in mapping:
        if needle in lowered and crime not in crimes:
            crimes.append(crime)
    return crimes or ["[[online-fraud-ic]]"]


def infer_jurisdiction(publisher: str, url: str) -> tuple[str, str]:
    match = re.search(r"\(([^)]+)\)", publisher)
    if match and "district" in match.group(1).lower():
        return f"U.S. District Court, {match.group(1).strip()}", "[[united-states]]"
    if "europol" in url or "interpol" in url or "eurojust" in url:
        return "International law enforcement action (multi-jurisdictional)", "[[international]]"
    return "U.S. federal prosecution (district not specified in source)", "[[united-states]]"


def summary_from_findings(title: str, source_slug: str, findings: list[object]) -> str:
    for finding in findings:
        text = str(finding).strip()
        if text and not text.startswith("{") and "[[" not in text:
            return text
    return f"{title} is a source-derived case page generated from [[{source_slug}]]."


def create_case(path: Path, post: object, existing_slugs: set[str]) -> Path | None:
    meta = post.metadata
    source_slug = path.stem
    title = str(meta.get("title") or "").strip()
    if not title:
        return None
    slug = build_slug(title, source_slug, existing_slugs)
    existing_slugs.add(slug)
    publisher = str(meta.get("publisher") or "")
    url = str(meta.get("collection_url") or "")
    publish_date = str(meta.get("publish_date") or TODAY)
    summary = summary_from_findings(title, source_slug, meta.get("key_findings", []) or [])
    status = infer_status(title + " " + summary)
    case_type = infer_case_type(status)
    crimes = infer_crimes(title + " " + summary)
    jurisdiction, jurisdiction_country = infer_jurisdiction(publisher, url)
    defendant_names = [str(v).strip() for v in (meta.get("defendant_names") or []) if str(v).strip()]
    defendants = defendant_names or [title]

    cooperating = ["[[us-doj]]"] if "justice.gov" in url else []
    if "fbi.gov" in url:
        cooperating.append("[[fbi-cyber-division]]")
    if "secretservice.gov" in url:
        cooperating.append("[[us-secret-service]]")
    if "europol" in url:
        cooperating.append("[[europol-ec3]]")
    if "interpol" in url:
        cooperating.append("[[interpol]]")
    cooperating = list(dict.fromkeys(cooperating))

    case_post = frontmatter.Post(
        {
            "type": "case",
            "title": title,
            "case_number": f"Source-derived from {source_slug}",
            "jurisdiction": jurisdiction,
            "jurisdiction_country": jurisdiction_country,
            "case_type": case_type,
            "status": status,
            "crime_charged": crimes,
            "defendants": [
                {
                    "name": name,
                    "nationality": "Unknown",
                    "status": status,
                    "sentence": "",
                    "location_at_arrest": "",
                }
                for name in defendants
            ],
            "related_operation": f"[[operation-{slug}]]",
            "ic_elements": {
                "mlat_requests": [],
                "extradition": "",
                "evidence_from_abroad": [],
                "foreign_arrests": [],
                "asset_freezing": [],
            },
            "cooperating_agencies": cooperating,
            "legal_frameworks_invoked": ["[[informal-cooperation]]"],
            "mechanisms_used": ["[[informal-cooperation]]"],
            "key_legal_issues": crimes[:1],
            "precedent_value": "Source-derived official action page; procedural enrichment from primary filings may still be needed.",
            "source_count": 1,
            "sources": [f"[[{source_slug}]]"],
            "created": TODAY,
            "updated": TODAY,
            "summary": summary,
        },
        (
            "## Summary\n\n"
            f"{summary}\n\n"
            "## Facts\n\n"
            f"This case page was generated from [[{source_slug}]] and reflects an official action title from the source corpus.\n\n"
            "## International Cooperation Elements\n\n"
            "This source-derived page should be enriched with case-level cooperation detail if primary filings or fuller official narratives are collected.\n\n"
            "## Legal Analysis\n\n"
            "The present page is a structured placeholder built from source metadata and may require refinement from primary filings.\n\n"
            "## References\n\n"
            "| # | Source | Publisher | Date | URL |\n"
            "|---|---|---|---|---|\n"
            f"| 1 | {title} | {publisher} | {publish_date} | {url} |\n"
        ),
    )
    target = CASES_DIR / f"{slug}.md"
    target.write_text(frontmatter.dumps(case_post), encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=250)
    args = parser.parse_args()

    existing_slugs, _, _, _ = existing_context()
    created = 0
    for path, post in candidate_sources(args.limit):
        if create_case(path, post, existing_slugs):
            created += 1
    print(f"Created {created} descriptive case pages from official sources.")


if __name__ == "__main__":
    main()
