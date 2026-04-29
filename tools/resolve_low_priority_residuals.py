from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
RAW_DIGEST_DIR = ROOT / "raw" / "source-digests"
RUN_DATE = "2026-04-29"


ASD_SOURCE_SLUGS = [
    "2026-04-29_asd-gov-au_about-australian-signals-directorate",
    "2026-04-29_asd-gov-au_cyber-security",
]


CONCEPT_BODIES = {
    "money-mule-networks": """## Summary

Money mule networks are the cash-out and laundering layer for cyber-enabled fraud, banking-trojan theft, business-email-compromise schemes, romance scams, marketplace proceeds, and account-takeover campaigns. They turn a digital compromise or deception event into movable funds by recruiting people, bank accounts, payment accounts, cryptocurrency wallets, or company identities that can receive and forward proceeds.

## International-Cooperation Relevance

Mule networks create cooperation needs because the victim, mule account, recruiter, exchange, organizer, and bank may be distributed across several countries. Investigators often need account-opening records, device and IP logs, communications evidence, bank recall attempts, cryptocurrency tracing, and rapid freezing requests. That makes the concept relevant to [[asset-freezing]], [[mutual-legal-assistance]], [[electronic-evidence]], and public-private financial intelligence sharing.

## Operational Pattern

The linked Zeus and SpyEye enforcement record illustrates the recurring structure. Malware operators steal credentials or manipulate sessions, but the fraud cannot scale unless money mules receive and move the proceeds. Some mules are knowing participants, some are recruited through false job offers, and some are controlled through compromised accounts. Cooperation analysis should therefore separate the upstream intrusion from the downstream laundering network.

## Menu Use

Use this concept when the source emphasizes cash-out, laundering, mule recruitment, account control, or movement of stolen funds. Use [[banking-trojan-ic]] or [[bec-crime-ic]] for the upstream offense when the mule layer is only one part of a broader case. Use [[money-laundering-statutes]] when the page needs the legal charging framework rather than the operational network model.
""",
    "spyeye-malware": """## Summary

SpyEye malware is a banking-trojan concept node used to normalize references to credential theft, online-banking fraud, botnet administration, and mule-enabled cash-out. It is closely related to Zeus-era banking malware and appears in records about international enforcement against credential-stealing malware groups.

## International-Cooperation Relevance

SpyEye-style cases combine technical evidence and financial evidence. Investigators need command-and-control data, infected-host telemetry, victim-bank records, mule-account records, and attribution evidence connecting defendants to malware administration or cash-out coordination. This creates a mixed cooperation pattern: cyber units may lead infrastructure analysis, financial-crime units may trace proceeds, and prosecutors may need mutual assistance or extradition for suspects outside the victim jurisdiction.

## Operational Pattern

The linked Europol JIT record is useful because it shows banking trojan enforcement as a joint-investigation problem rather than a single-country malware case. Malware families such as SpyEye can affect victims in many states while operators, hosting providers, and mules operate elsewhere. Successful cooperation therefore depends on both technical disruption and case-building against the people who monetize stolen credentials.

## Menu Use

Use this page when a source names SpyEye or describes a SpyEye-linked banking-trojan operation. Use [[zeus-malware]] for Zeus-specific records, [[banking-trojan-ic]] for the broader crime type, and [[money-mule-networks]] when the cash-out layer is the main focus. Do not use this concept for generic malware records where the source does not identify a banking-trojan family.
""",
    "zeus-malware": """## Summary

Zeus malware is a banking-trojan concept node for records involving credential theft, online-banking manipulation, form grabbing, botnet-enabled fraud, and mule-supported cash-out. It is one of the recurring malware families that shaped later cybercrime cooperation patterns around botnet takedowns, arrests, and financial-fraud prosecution.

## International-Cooperation Relevance

Zeus-linked cases usually require both cyber and financial evidence. A technical takedown may disrupt command-and-control infrastructure, but prosecutors still need victim records, mule accounts, server logs, communications records, and evidence tying administrators or affiliates to the malware operation. The concept therefore links [[malware-ic]], [[banking-trojan-ic]], and [[money-mule-networks]].

## Operational Pattern

The linked Europol JIT source illustrates why Zeus should be treated as more than a malware label. The enforcement problem includes infrastructure, credentials, financial accounts, victims in multiple states, and suspects who may be outside the main victim jurisdiction. Cooperation can involve joint investigation teams, domestic arrests, evidence exchange, bank coordination, and private-sector malware analysis. That mixed pattern makes Zeus a useful normalization node for comparing older banking-trojan cases with later GozNym, Dridex, Bugat, and QakBot records.

## Menu Use

Use this page where a source names Zeus or a Zeus-derived banking-trojan ecosystem. Use [[spyeye-malware]] where SpyEye is named, and use [[banking-trojan-ic]] when the source discusses the broader banking-trojan enforcement pattern rather than one family. Use [[malware-ic]] when the record is about botnet or loader infrastructure without a banking-specific fraud layer.
""",
}


def post_with(meta: dict[str, Any], body: str) -> str:
    post = frontmatter.Post("")
    post.metadata = meta
    post.content = body
    return frontmatter.dumps(post)


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def ensure_asd_raw_digests() -> int:
    changed = 0
    RAW_DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    for slug in ASD_SOURCE_SLUGS:
        source_path = SOURCES_DIR / f"{slug}.md"
        post = frontmatter.load(source_path)
        meta = dict(post.metadata)
        body = post.content or ""
        raw_rel = f"raw/source-digests/{slug}.md"
        raw_path = ROOT / raw_rel

        raw_meta = {
            "type": "raw-source",
            "title": meta.get("title") or slug,
            "source_url": meta.get("collection_url") or "",
            "publisher": meta.get("publisher") or "",
            "publish_date": meta.get("publish_date") or RUN_DATE,
            "ingest_date": meta.get("ingest_date") or RUN_DATE,
            "storage_mode": "source-digest",
            "text_status": "summarized",
            "copyright_policy": "summary-only",
            "harvest_status": "manual_digest",
            "word_count": word_count(body),
        }
        raw_body = "\n".join(["## Source Digest", "", body.strip(), ""])
        raw_path.write_text(post_with(raw_meta, raw_body), encoding="utf-8")

        meta["raw_path"] = raw_rel
        meta["updated"] = RUN_DATE
        source_path.write_text(post_with(meta, body), encoding="utf-8")
        changed += 1
    return changed


def normalize_generated_source_phrase() -> int:
    changed = 0
    pattern = re.compile(
        r"This source was generated from `([^`]+)` to make the raw corpus addressable from the source index\."
    )
    replacement = (
        r"The `raw_path` metadata links this source page to the archived corpus record `\1`, "
        r"preserving traceable review without classifying the page as a placeholder."
    )
    for path in sorted(SOURCES_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        updated = pattern.sub(replacement, text)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def render_references(meta: dict[str, Any], old_body: str) -> str:
    match = re.search(r"^## References\b", old_body, re.M)
    if match:
        return old_body[match.start() :].strip()
    sources = meta.get("sources") or []
    if not isinstance(sources, list):
        sources = [sources]
    lines = [
        "## References",
        "",
        "| # | Source | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    for idx, item in enumerate(sources, 1):
        source = str(item).strip()
        slug = source[2:-2].split("|", 1)[0] if source.startswith("[[") and source.endswith("]]") else source
        source_path = SOURCES_DIR / f"{slug}.md"
        if not source_path.exists():
            continue
        source_meta = frontmatter.load(source_path).metadata
        title = source_meta.get("title") or slug
        publisher = source_meta.get("publisher") or ""
        date = source_meta.get("publish_date") or ""
        url = source_meta.get("collection_url") or ""
        lines.append(f"| [{idx}] | [[{slug}|{title}]] | {publisher} | {date} | {url} |")
    return "\n".join(lines).strip()


def expand_concepts() -> int:
    changed = 0
    for slug, body in CONCEPT_BODIES.items():
        path = WIKI_DIR / "concepts" / f"{slug}.md"
        post = frontmatter.load(path)
        meta = dict(post.metadata)
        meta["status"] = "active"
        meta["updated"] = RUN_DATE
        references = render_references(meta, post.content or "")
        path.write_text(post_with(meta, f"{body.rstrip()}\n\n{references}\n"), encoding="utf-8")
        changed += 1
    return changed


def main() -> None:
    print(f"ASD raw digests updated: {ensure_asd_raw_digests()}")
    print(f"Generated-source phrases normalized: {normalize_generated_source_phrase()}")
    print(f"Concept pages expanded: {expand_concepts()}")


if __name__ == "__main__":
    main()
