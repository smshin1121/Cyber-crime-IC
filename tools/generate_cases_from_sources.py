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
GENERIC_NAME_TOKENS = {
    "man", "woman", "national", "defendant", "defendants", "offender", "offenders",
    "trafficker", "developer", "administrator", "administrators", "citizen", "citizens",
    "teenager", "teenagers", "member", "members", "exchange", "marketplace", "drug",
    "dark", "web", "darknet", "market", "county", "district", "charges", "charged",
    "sentenced", "guilty", "pleads", "pleaded", "convicted", "hacking", "seizure",
    "ransomware", "affiliates", "across", "continents", "travel", "child", "offense",
    "offence", "official", "operator", "operators", "trafficking", "conspiracy",
}


CASE_PATTERNS = [
    re.compile(r"^(United States v\.|U\.S\. v\.|In re )", re.I),
    re.compile(r"\b(indicted|charged|sentenced|convicted|plea|complaint|judgment|forfeiture)\b", re.I),
]


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"\b(united states v|u s v|in re|sentencing|indictment|complaint|judgment|plea|charged|convicted|sentenced|et al|aka)\b", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def unwrap_source_name(source_slug: str) -> str:
    parts = source_slug.split("_", 2)
    if len(parts) == 3:
        return parts[2]
    return source_slug


def extract_case_title(title: str, source_slug: str) -> str:
    source_name = unwrap_source_name(source_slug)
    source_name = source_name.replace("-", " ")
    source_name = re.sub(r"\s+", " ", source_name).strip()
    if re.match(r"^united states v ", source_name, re.I):
        names = re.sub(r"^united states v ", "", source_name, flags=re.I).strip()
        return f"United States v. {names.title()}"
    if re.match(r"^in re ", source_name, re.I):
        names = re.sub(r"^in re ", "", source_name, flags=re.I).strip()
        return f"In re {names.title()}"
    if CASE_PATTERNS[0].search(title):
        return title.strip()
    return ""


def title_from_defendants(names: list[str]) -> str:
    cleaned: list[str] = []
    for name in names:
        text = str(name).strip()
        if not text:
            continue
        words = re.findall(r"[A-Za-z]+", text.lower())
        if len(words) < 2:
            continue
        if any(word in GENERIC_NAME_TOKENS for word in words):
            continue
        cleaned.append(text)
    if not cleaned:
        return ""
    if len(cleaned) == 1:
        return f"United States v. {cleaned[0]}"
    if len(cleaned) == 2:
        return f"United States v. {cleaned[0]} and {cleaned[1]}"
    return f"United States v. {', '.join(cleaned[:-1])}, and {cleaned[-1]}"


def clean_summary(title: str, source_slug: str, findings: list[object]) -> str:
    for finding in findings:
        text = str(finding).strip()
        if not text:
            continue
        if "[[" in text or "Enforcement Action is" in text or text.startswith("{"):
            continue
        return text
    return f"{title} is a source-derived case page generated from [[{source_slug}]]."


def existing_case_context() -> tuple[set[str], list[str], set[str]]:
    slugs: set[str] = set()
    titles: list[str] = []
    source_slugs: set[str] = set()
    for path in CASES_DIR.glob("*.md"):
        if path.name.startswith("_"):
            continue
        slugs.add(path.stem)
        post = frontmatter.load(path)
        titles.append(norm(str(post.metadata.get("title") or "")))
        for src in post.metadata.get("sources", []) or []:
            text = str(src)
            if text.startswith("[[") and text.endswith("]]"):
                source_slugs.add(text[2:-2].split("|", 1)[0].strip())
    return slugs, titles, source_slugs


def infer_status(text: str) -> str:
    lowered = text.lower()
    if "sentenc" in lowered:
        return "sentenced"
    if "convict" in lowered:
        return "convicted"
    if "plea" in lowered or "pleads guilty" in lowered:
        return "pleaded guilty"
    if "forfeiture" in lowered or "seizure" in lowered:
        return "seizure ordered"
    if "indict" in lowered:
        return "indicted"
    if "charg" in lowered or "complaint" in lowered:
        return "charged"
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
    ]
    for needle, crime in mapping:
        if needle in lowered and crime not in crimes:
            crimes.append(crime)
    if not crimes:
        crimes.append("[[online-fraud-ic]]")
    return crimes


def infer_jurisdiction(publisher: str) -> tuple[str, str]:
    match = re.search(r"\(([^)]+)\)", publisher)
    if match:
        inner = match.group(1).strip()
        if "district" in inner.lower():
            return f"U.S. District Court, {inner}", "[[united-states]]"
    if "secret service" in publisher.lower():
        return "U.S. federal prosecution (district not specified in source)", "[[united-states]]"
    return "U.S. federal prosecution (district not specified in source)", "[[united-states]]"


def parse_defendants(title: str) -> list[str]:
    cleaned = re.sub(r"^(United States v\.|U\.S\. v\.|In re )", "", title, flags=re.I).strip()
    cleaned = re.sub(r"\(.*?\)", "", cleaned).strip()
    cleaned = cleaned.replace(" et al.", "")
    parts = re.split(r",| and ", cleaned)
    names: list[str] = []
    for part in parts:
        name = part.strip(" -")
        if len(name.split()) >= 2:
            names.append(name)
    return names[:4]


def build_case_slug(title: str, source_slug: str, existing_slugs: set[str]) -> str:
    lowered = title.lower()
    if lowered.startswith("in re "):
        base = "in-re-" + slugify(re.sub(r"^in re ", "", title, flags=re.I))
    else:
        base = "us-v-" + slugify(re.sub(r"^(United States v\.|U\.S\. v\.)", "", title, flags=re.I))
    base = re.sub(r"-sentenced?$|-charged$|-indicted$|-complaint$|-judgment$|-forfeiture$", "", base)
    base = re.sub(r"-et-al$", "", base).strip("-")
    slug = base[:90]
    if slug not in existing_slugs:
        return slug
    fallback = slugify(source_slug.split("_", 2)[-1])[:100]
    if fallback and fallback not in existing_slugs:
        return fallback
    i = 2
    while f"{slug}-{i}" in existing_slugs:
        i += 1
    return f"{slug}-{i}"


def candidate_sources(limit: int) -> list[tuple[Path, any]]:
    existing_slugs, existing_titles, used_sources = existing_case_context()
    rows: list[tuple[int, Path, any]] = []
    for path in SOURCES_DIR.glob("*.md"):
        if path.name.startswith("_") or path.stem in used_sources:
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        source_slug = path.stem
        raw_title = str(meta.get("title") or "")
        title = extract_case_title(raw_title, source_slug)
        if not title:
            title = title_from_defendants([str(v) for v in (meta.get("defendant_names") or [])])
        if not title:
            continue
        raw_path = str(meta.get("raw_path") or "")
        publisher = str(meta.get("publisher") or "")
        score = 0
        if CASE_PATTERNS[0].search(raw_title) or "united-states-v-" in source_slug or "_in-re-" in source_slug:
            score += 5
        if CASE_PATTERNS[1].search(raw_title):
            score += 3
        if "raw/case-documents/" in raw_path:
            score += 4
        if any(x in publisher.lower() for x in ["justice", "doj", "court", "secret service"]):
            score += 2
        if not score:
            continue
        title_norm = norm(title)
        if any(title_norm and (title_norm in ext or ext in title_norm) for ext in existing_titles):
            continue
        rows.append((score, path, post))
    rows.sort(key=lambda x: (-x[0], x[1].name))
    return [(path, post) for _, path, post in rows[:limit]]


def create_case(path: Path, post, existing_slugs: set[str]) -> Path | None:
    meta = post.metadata
    source_slug = path.stem
    title = extract_case_title(str(meta.get("title") or "").strip(), source_slug)
    if not title:
        title = title_from_defendants([str(v) for v in (meta.get("defendant_names") or [])])
    if not title:
        return None

    slug = build_case_slug(title, path.stem, existing_slugs)
    existing_slugs.add(slug)
    raw_path = str(meta.get("raw_path") or "")
    publisher = str(meta.get("publisher") or "")
    publish_date = str(meta.get("publish_date") or TODAY)
    summary = clean_summary(title, source_slug, meta.get("key_findings", []) or [])
    status = infer_status(f"{title} {summary}")
    case_type = infer_case_type(status)
    crimes = infer_crimes(f"{title} {summary}")
    jurisdiction, jurisdiction_country = infer_jurisdiction(publisher)
    defendants = parse_defendants(title)
    if not defendants:
        defendants = [title]

    related_operation = f"[[operation-{slug}]]"
    cooperating = ["[[us-doj]]"]
    lower_blob = f"{title} {summary} {publisher}".lower()
    if "secret service" in lower_blob:
        cooperating.append("[[us-secret-service]]")
    if "fbi" in lower_blob:
        cooperating.append("[[fbi-cyber-division]]")
    if "europol" in lower_blob:
        cooperating.append("[[europol-ec3]]")

    case_post = frontmatter.Post(
        {
            "type": "case",
            "title": title,
            "case_number": str(meta.get("case_number") or f"Source-derived from {source_slug}"),
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
            "related_operation": related_operation,
            "ic_elements": {
                "mlat_requests": [],
                "extradition": "",
                "evidence_from_abroad": [],
                "foreign_arrests": [],
                "asset_freezing": [],
            },
            "cooperating_agencies": cooperating,
            "legal_frameworks_invoked": ["[[mutual-legal-assistance]]"] if "international" in lower_blob or "foreign" in lower_blob else ["[[informal-cooperation]]"],
            "mechanisms_used": ["[[mutual-legal-assistance]]"] if "international" in lower_blob or "foreign" in lower_blob else ["[[informal-cooperation]]"],
            "key_legal_issues": crimes[:1],
            "precedent_value": "Source-derived candidate case page; analytical significance requires further enrichment from primary filings.",
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
            f"This case page was generated from [[{source_slug}]] and should be expanded with primary-court detail where available.\n\n"
            "## International Cooperation Elements\n\n"
            "The currently collected source indicates a transnational cybercrime enforcement context, but the specific cross-border mechanisms still need case-level enrichment.\n\n"
            "## Legal Analysis\n\n"
            "The present page is a structured placeholder built from source metadata and should be refined as additional filings or official summaries are collected.\n\n"
            "## References\n\n"
            "| # | Source | Publisher | Date | URL |\n"
            "|---|---|---|---|---|\n"
            f"| 1 | {title} | {publisher} | {publish_date} | {meta.get('collection_url') or ''} |\n"
        ),
    )
    target = CASES_DIR / f"{slug}.md"
    target.write_text(frontmatter.dumps(case_post), encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    existing_slugs, _, _ = existing_case_context()
    created = 0
    for path, post in candidate_sources(args.limit):
        if create_case(path, post, existing_slugs):
            created += 1
    print(f"Created {created} new case pages from sources.")


if __name__ == "__main__":
    main()
