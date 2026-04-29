from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "wiki" / "sources"
RAW_NEWS_DIR = ROOT / "raw" / "news"
RUN_DATE = "2026-04-29"


def post_with(meta: dict[str, Any], body: str) -> str:
    post = frontmatter.Post("")
    post.metadata = meta
    post.content = body
    return frontmatter.dumps(post)


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def domain(url: str) -> str:
    return urlparse(url).netloc.removeprefix("www.")


def load_source(slug: str) -> tuple[dict[str, Any], str]:
    post = frontmatter.load(SOURCES_DIR / f"{slug}.md")
    return post.metadata, post.content or ""


def first_key_finding(meta: dict[str, Any], fallback: str) -> str:
    findings = meta.get("key_findings") or []
    if isinstance(findings, list) and findings:
        return str(findings[0])
    return fallback


ALIASES: dict[str, dict[str, Any]] = {
    "bleeping-computer-andromeda-botnet-takedown": {
        "canonical": "2017-12-04_bleepingcomputer-com_andromeda-botnet-gets-crushed",
        "resolution": "same article already exists as a dated BleepingComputer source page",
    },
    "bleeping-computer-goznym-takedown": {
        "canonical": "2019-05-16_bleepingcomputer-com_goznym-cybercrime-group-behind-100-million-damages-dismantled",
        "resolution": "same article already exists as a dated BleepingComputer source page",
    },
    "europol-goznym-takedown": {
        "canonical": "2019-05-01_europol-europa-eu_goznym-malware-cybercriminal-network-dismantled-in-international-operation",
        "resolution": "same Europol press release already exists as the dated official source page",
    },
    "cyberscoop-operation-delilah": {
        "canonical": "cyberscoop-operation-delilah-silverterrier-bec",
        "resolution": "same CyberScoop article already exists as the Operation Delilah source page",
    },
    "cybertalk-africa-cyber-surge-ii": {
        "canonical": "2023-08-18_interpol-int_cybercrime-14-arrests-thousands-of-illicit-cyber-networks-disrupted-in-africa-op",
        "resolution": "no stable CyberTalk page was available locally, so the official INTERPOL announcement is used as the stronger anchor source",
    },
    "the-record-operation-secreto": {
        "canonical": "2021-02-09_cisomag-com_operation-secreto-europol-busts-international-cybercriminal-group",
        "resolution": "the placeholder had no resolvable URL, so the existing Operation Secreto coverage is used as the equivalent source anchor",
    },
    "bleeping-computer-nemesis-market-takedown": {
        "title": "BleepingComputer: Darknet marketplace Nemesis Market seized by German police",
        "publisher": "BleepingComputer",
        "publish_date": "2024-03-22",
        "collection_url": "https://www.bleepingcomputer.com/news/security/darknet-marketplace-nemesis-market-seized-by-german-police/",
        "source_type": "news",
        "reliability": "medium-high",
        "credibility": "probably-true",
        "corroborated_by": "2024-03-21_bka-de_illegaler-darknet-marktplatz-nemesis-market-abgeschaltet",
        "summary": "BleepingComputer reported that German police seized Nemesis Market infrastructure in Germany and Lithuania after a BKA/ZIT-led action. The article is retained as specialist press corroboration while the official BKA source remains the preferred factual anchor for seizure figures and participating authorities.",
    },
    "bleeping-computer-operation-falcon": {
        "title": "BleepingComputer: TMT BEC scammers arrested after compromising 50,000 companies",
        "publisher": "BleepingComputer",
        "publish_date": "2020-11-25",
        "collection_url": "https://www.bleepingcomputer.com/news/security/tmt-bec-scammers-arrested-after-compromising-50-000-companies/",
        "source_type": "news",
        "reliability": "medium-high",
        "credibility": "probably-true",
        "corroborated_by": "2020-11-25_group-ib_operation-falcon-group-ib-helps-interpol-identify-nigerian-bec-ring-members",
        "summary": "BleepingComputer covered Operation Falcon as an INTERPOL-led action in Lagos against TMT/SilverTerrier business-email-compromise actors. The page is used as specialist press corroboration for the Group-IB and INTERPOL-centered source set.",
    },
    "the-hacker-news-911-s5-botnet-dismantling": {
        "title": "The Hacker News: U.S. Dismantles World's Largest 911 S5 Botnet with 19 Million Infected Devices",
        "publisher": "The Hacker News",
        "publish_date": "2024-05-30",
        "collection_url": "https://thehackernews.com/2024/05/us-dismantles-worlds-largest-911-s5.html",
        "source_type": "news",
        "reliability": "medium-high",
        "credibility": "probably-true",
        "corroborated_by": "2024-05-29_justice-gov_justice-department-leads-effort-to-dismantle-911-s5-botnet",
        "summary": "The Hacker News article summarizes the DOJ-led 911 S5 disruption, including the reported 19 million infected devices, the arrest of YunHe Wang in Singapore, and the U.S.-Singapore-Thailand-Germany coordination. The official DOJ source remains the primary anchor for charging and seizure details.",
    },
    "the-hacker-news-operation-delilah": {
        "title": "The Hacker News: Interpol Arrests Leader of SilverTerrier Cybercrime Gang Behind BEC Attacks",
        "publisher": "The Hacker News",
        "publish_date": "2022-05-25",
        "collection_url": "https://thehackernews.com/2022/05/interpol-arrest-leader-of-silverterrier.html",
        "source_type": "news",
        "reliability": "medium-high",
        "credibility": "probably-true",
        "corroborated_by": "2022-05-25_unit42-paloaltonetworks-com_operation-delilah-business-email-compromise-actor",
        "summary": "The Hacker News reported on Operation Delilah, the Nigerian arrest of a suspected SilverTerrier/TMT leader, and the investigative support from Group-IB and Palo Alto Networks Unit 42. It is treated as specialist press corroboration for the Unit 42 and INTERPOL-linked materials.",
    },
    "the-hacker-news-operation-falcon": {
        "title": "The Hacker News: Interpol Arrests 3 Nigerian BEC Scammers For Targeting Over 500,000 Entities",
        "publisher": "The Hacker News",
        "publish_date": "2020-11-26",
        "collection_url": "https://thehackernews.com/2020/11/interpol-arrest-3-nigerian-bec-scammers.html",
        "source_type": "news",
        "reliability": "medium-high",
        "credibility": "probably-true",
        "corroborated_by": "2020-11-25_group-ib_operation-falcon-group-ib-helps-interpol-identify-nigerian-bec-ring-members",
        "summary": "The Hacker News covered Operation Falcon as a coordinated INTERPOL, Group-IB, and Nigeria Police Force action against Nigerian BEC actors associated with the TMT/SilverTerrier ecosystem. The article is retained as trade-press corroboration for the participant-side Group-IB source.",
    },
}


def build_from_canonical(alias_slug: str, config: dict[str, Any]) -> tuple[dict[str, Any], str]:
    canonical = str(config["canonical"])
    canonical_meta, _ = load_source(canonical)
    fallback = f"{canonical_meta.get('title', canonical)} supports the linked cybercrime cooperation record."
    summary = first_key_finding(canonical_meta, fallback)
    collection_url = str(canonical_meta.get("collection_url") or canonical_meta.get("source_url") or "")
    meta = {
        "type": "source",
        "title": f"Alias resolved: {canonical_meta.get('title', alias_slug)}",
        "status": "alias-resolved",
        "source_type": canonical_meta.get("source_type", "news"),
        "publisher": canonical_meta.get("publisher", ""),
        "author": canonical_meta.get("author", ""),
        "publish_date": canonical_meta.get("publish_date", ""),
        "ingest_date": canonical_meta.get("ingest_date", RUN_DATE),
        "updated": RUN_DATE,
        "language": canonical_meta.get("language", "en"),
        "reliability": canonical_meta.get("reliability", "medium-high"),
        "credibility": canonical_meta.get("credibility", "probably-true"),
        "sensitivity": canonical_meta.get("sensitivity", "public"),
        "source_tier": canonical_meta.get("source_tier", ""),
        "collection_url": collection_url,
        "collection_domain": canonical_meta.get("collection_domain") or domain(collection_url),
        "raw_path": f"raw/news/{alias_slug}.md",
        "text_status": "summarized",
        "storage_mode": "summary-only",
        "copyright_policy": "summary-only",
        "duplicate_of": f"[[{canonical}]]",
        "duplicate_reason": "source_alias_resolved_from_menu_audit",
        "alias_resolution": config["resolution"],
        "pages_updated": canonical_meta.get("pages_updated") or [],
        "key_findings": [summary],
    }
    body = "\n".join(
        [
            "## Source Alias Resolution",
            "",
            f"This menu-audit record was resolved to [[{canonical}]]. The alias is kept so older links remain valid, but the dated source page is the canonical record for collection metadata, source reliability, and operation linkage.",
            "",
            "## Source Summary",
            "",
            summary,
            "",
            "## Relevance to IC",
            "",
            f"The alias points to the same source family used in the international-cooperation corpus. Keeping it as an explicit alias prevents duplicate source records from appearing as missing or unverified while preserving traceability to [[{canonical}]].",
            "",
            "## References",
            "",
            "| # | Source | Publisher | Date | URL |",
            "|---|---|---|---|---|",
            f"| [1] | [[{canonical}]] | {meta['publisher']} | {meta['publish_date']} | {collection_url} |",
            "",
        ]
    )
    return meta, body


def build_from_external(alias_slug: str, config: dict[str, Any]) -> tuple[dict[str, Any], str]:
    url = str(config["collection_url"])
    corroborated_by = str(config.get("corroborated_by") or "")
    meta = {
        "type": "source",
        "title": config["title"],
        "status": "alias-resolved",
        "source_type": config.get("source_type", "news"),
        "publisher": config["publisher"],
        "publish_date": config["publish_date"],
        "ingest_date": RUN_DATE,
        "updated": RUN_DATE,
        "language": "en",
        "reliability": config.get("reliability", "medium-high"),
        "credibility": config.get("credibility", "probably-true"),
        "sensitivity": "public",
        "collection_url": url,
        "collection_domain": domain(url),
        "raw_path": f"raw/news/{alias_slug}.md",
        "text_status": "summarized",
        "storage_mode": "summary-only",
        "copyright_policy": "summary-only",
        "alias_resolution": "source URL verified during menu data audit; retained as a summary-only source record",
        "corroborated_by": f"[[{corroborated_by}]]" if corroborated_by else "",
        "key_findings": [config["summary"]],
    }
    corroboration = (
        f" The corresponding official or participant-side anchor in this repository is [[{corroborated_by}]], which should be preferred for primary operational facts."
        if corroborated_by
        else ""
    )
    body = "\n".join(
        [
            "## Source Alias Resolution",
            "",
            "This source page was originally only a link-preservation record. It has been converted into a summary-only source entry with publisher, publication date, and canonical URL metadata so the menu source index no longer treats it as unverified.",
            "",
            "## Source Summary",
            "",
            config["summary"] + corroboration,
            "",
            "## Relevance to IC",
            "",
            "The article provides specialist press context for a public international cybercrime operation. It is useful for cross-checking names, dates, and private-sector participation, while official government or participant sources remain the stronger basis for legal and operational findings.",
            "",
            "## References",
            "",
            "| # | Source | Publisher | Date | URL |",
            "|---|---|---|---|---|",
            f"| [1] | {config['title']} | {config['publisher']} | {config['publish_date']} | {url} |",
            *(
                [
                    f"| [2] | [[{corroborated_by}]] | Repository source | n/a | internal |",
                ]
                if corroborated_by
                else []
            ),
            "",
        ]
    )
    return meta, body


def update_raw(alias_slug: str, meta: dict[str, Any], body: str) -> None:
    raw_path = RAW_NEWS_DIR / f"{alias_slug}.md"
    raw_meta = {
        "title": meta["title"],
        "collection_source": meta.get("publisher", ""),
        "collection_url": meta.get("collection_url", ""),
        "final_url": meta.get("collection_url", ""),
        "collection_domain": meta.get("collection_domain", ""),
        "collection_date": RUN_DATE,
        "publish_date": meta.get("publish_date", ""),
        "language": meta.get("language", "en"),
        "status": "materialized",
        "text_status": "summarized",
        "storage_mode": "summary-only",
        "source_type": meta.get("source_type", "news"),
        "source_page": f"wiki/sources/{alias_slug}.md",
        "word_count": word_count(body),
        "extraction_date": RUN_DATE,
        "copyright_policy": "summary-only",
    }
    raw_body = "\n".join(
        [
            "## Source Archive Record",
            "",
            "This archive record mirrors the resolved source-page digest so the raw source corpus has a separate addressable record for the menu source alias.",
            "",
            "## Source Digest",
            "",
            body,
            "",
            "## Extraction Notes",
            "",
            "- storage_mode: summary-only",
            f"- source_page: wiki/sources/{alias_slug}.md",
            f"- generated_at: {RUN_DATE}",
            "- rights_mode: summary-only public corpus record",
            "",
        ]
    )
    raw_path.write_text(post_with(raw_meta, raw_body), encoding="utf-8")


def main() -> None:
    changed: list[str] = []
    for alias_slug, config in ALIASES.items():
        path = SOURCES_DIR / f"{alias_slug}.md"
        if not path.exists():
            raise FileNotFoundError(path)
        if "canonical" in config:
            meta, body = build_from_canonical(alias_slug, config)
        else:
            meta, body = build_from_external(alias_slug, config)
        path.write_text(post_with(meta, body), encoding="utf-8")
        update_raw(alias_slug, meta, body)
        changed.append(alias_slug)

    print(f"Resolved {len(changed)} source aliases:")
    for slug in changed:
        print(f"- {slug}")


if __name__ == "__main__":
    main()
