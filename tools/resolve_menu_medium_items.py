from __future__ import annotations

from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
RUN_DATE = "2026-04-29"


def post_with(meta: dict[str, Any], body: str) -> str:
    post = frontmatter.Post("")
    post.metadata = meta
    post.content = body
    return frontmatter.dumps(post)


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


def domain(url: str) -> str:
    return urlparse(url).netloc.removeprefix("www.")


SOURCE_URLS: dict[str, dict[str, str]] = {
    "2024-10-15-interpol-operation-orion-international": {
        "collection_url": "https://www.interpol.int/en/News-and-Events/News/2024/20-rescued-144-arrested-in-major-child-abuse-operation-across-South-America",
        "publisher": "INTERPOL",
    },
    "2024-12-02-digwatch-interpol-korea-5500-arrests": {
        "collection_url": "https://dig.watch/updates/interpol-and-south-korea-lead-operation-arresting-over-5500-cybercrime-suspects",
        "publisher": "Digital Watch Observatory",
    },
    "2025-03-24-africanews-operation-red-card": {
        "collection_url": "https://www.africanews.com/2025/03/24/cybercrime-crackdown-306-arrested-in-africa-wide-operation/",
        "publisher": "Africanews",
    },
    "2025-04-01-interpol-operation-secure-infostealer": {
        "collection_url": "https://www.interpol.int/en/News-and-Events/News/2025/20-000-malicious-IPs-and-domains-taken-down-in-INTERPOL-infostealer-crackdown",
        "publisher": "INTERPOL",
        "publish_date": "2025-06-11",
    },
    "2025-04-04-europol-operation-stream-kidflix": {
        "collection_url": "https://securityaffairs.com/176154/cyber-crime/europol-led-op-shuts-down-csam-platform-kidflix.html",
        "publisher": "Security Affairs",
    },
    "2025-04-07-korea-npa-operation-cyber-guardian": {
        "collection_url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156682866",
        "publisher": "Korean National Police Agency / Korea Policy Briefing",
    },
    "2025-05-22-europol-endgame-follow-up": {
        "collection_url": "https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-follow-leads-to-five-detentions-and-interrogations-well-server-takedowns",
        "publisher": "Europol",
        "publish_date": "2025-04-09",
        "duplicate_of": "[[2025-04-09_europol-europa-eu_operation-endgame-follow-up-leads-to-five-detentions-and-interrogations-as-well]]",
    },
    "2025-05-28-thehackernews-danabot-malware": {
        "collection_url": "https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html",
        "publisher": "The Hacker News",
        "duplicate_of": "[[2025-05-28_thehackernews-com_us-dismantles-danabot-malware-network]]",
    },
    "europol-doublevpn-takedown": {
        "collection_url": "https://www.europol.europa.eu/media-press/newsroom/news/coordinated-action-cuts-access-to-vpn-service-used-ransomware-groups",
        "publisher": "Europol",
    },
}


def update_source_url(slug: str, data: dict[str, str]) -> None:
    path = SOURCES_DIR / f"{slug}.md"
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    url = data["collection_url"]
    meta["collection_url"] = url
    meta["collection_domain"] = domain(url)
    meta["publisher"] = data.get("publisher", meta.get("publisher", ""))
    if data.get("publish_date"):
        meta["publish_date"] = data["publish_date"]
    if data.get("duplicate_of"):
        meta["duplicate_of"] = data["duplicate_of"]
        meta["duplicate_reason"] = "menu_medium_url_resolution"
    meta["updated"] = RUN_DATE
    path.write_text(post_with(meta, post.content or ""), encoding="utf-8")

    raw_rel = str(meta.get("raw_path") or "")
    if raw_rel:
        raw_path = ROOT / raw_rel
        if raw_path.exists():
            raw_post = frontmatter.load(raw_path)
            raw_meta = dict(raw_post.metadata)
            raw_meta["collection_url"] = url
            raw_meta["final_url"] = url
            raw_meta["collection_domain"] = domain(url)
            raw_meta["collection_source"] = meta.get("publisher", "")
            if data.get("publish_date"):
                raw_meta["publish_date"] = data["publish_date"]
            raw_path.write_text(post_with(raw_meta, raw_post.content or ""), encoding="utf-8")


def source_meta(slug: str) -> dict[str, Any]:
    return frontmatter.load(SOURCES_DIR / f"{slug}.md").metadata


def render_references(slugs: list[str]) -> str:
    lines = [
        "## References",
        "",
        "| # | Source | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    for idx, slug in enumerate(slugs, 1):
        meta = source_meta(slug)
        title = meta.get("title") or slug
        publisher = meta.get("publisher") or ""
        date = meta.get("publish_date") or meta.get("created") or ""
        url = meta.get("collection_url") or ""
        lines.append(f"| [{idx}] | [[{slug}|{title}]] | {publisher} | {date} | {url} |")
    lines.append("")
    return "\n".join(lines)


def update_page(category: str, slug: str, body: str, sources: list[str], extra_meta: dict[str, Any] | None = None) -> None:
    path = WIKI_DIR / category / f"{slug}.md"
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    meta.update(extra_meta or {})
    meta["updated"] = RUN_DATE
    meta["status"] = meta.get("status") or "active"
    meta["source_count"] = len(sources)
    meta["sources"] = [f"[[{source}]]" for source in sources]
    text = "\n".join([body.rstrip(), "", render_references(sources)])
    path.write_text(post_with(meta, text), encoding="utf-8")


CORE_UPDATES: list[dict[str, Any]] = [
    {
        "category": "crime-types",
        "slug": "cyberstalking-ic",
        "sources": [
            "2024-07-10_secretservice_pernicious-cyberstalker-sentenced-9-years-unrelenting-harassment-former-roommate",
            "2024-07-11_justice-gov-opa_former-computer-privacy-consultant-convicted-cyberstalking",
            "2026-04-18_justice-gov_former-privacy-consultant-convicted-cyberstalking-campaign-against-former-roommate-her",
        ],
        "meta": {
            "typical_ic_challenges": ["provider-held evidence", "victim safety coordination", "cross-platform attribution"],
            "typical_mechanisms": ["[[electronic-evidence]]", "[[direct-provider-request]]", "[[mutual-legal-assistance]]"],
        },
        "body": """## Summary

Cyberstalking covers repeated online or electronic communications, threats, harassment, coercion, impersonation, and related misuse of digital platforms against specific victims. In the international-cooperation corpus it is usually not a large multinational takedown category, but it still matters for evidence and classification because offenders often use platform accounts, cloud services, messaging providers, anonymization tools, or out-of-district infrastructure.

## Cooperation Pattern

The linked cyberstalking sources show a victim-centered investigative pattern. Investigators need to preserve account data, attribute accounts to a person, connect online conduct to real-world threats or coercion, and protect victims while a case is pending. Cross-border cooperation becomes relevant when the service provider, suspect, victim, or data store is outside the investigating district or country. In those settings, the legal route may be a domestic warrant to a provider, a direct provider request, an emergency disclosure request, or formal mutual assistance.

## Menu Use

Use this category for stalking, coercive harassment, sextortion-like harassment, and threat campaigns directed at identifiable victims. Use [[extortion-ic]] when the dominant feature is a payment demand, [[online-fraud-ic]] when deception for money is central, and [[csam-ic]] when production, distribution, or possession of abuse material is the core offense.
""",
    },
    {
        "category": "crime-types",
        "slug": "hacking-ic",
        "sources": ["2025-03-05-doj-isoon-chinese-hackers-charges", "2026-03-12-eurojust-proxy-service-takedown"],
        "meta": {
            "typical_ic_challenges": ["state sheltering", "proxy infrastructure", "victim and evidence distribution"],
            "typical_mechanisms": ["[[electronic-evidence]]", "[[domain-seizure]]", "[[extradition]]", "[[mutual-legal-assistance]]"],
        },
        "body": """## Summary

Hacking and computer intrusion cover unauthorized access to computers, networks, accounts, devices, and data. In international-cooperation analysis this category includes financially motivated intrusion, contractor or state-directed intrusion, credential theft, vulnerability exploitation, and infrastructure abuse used to hide the actor's location.

## Cooperation Pattern

The cooperation problem depends on the actor model. Criminal intrusion cases may progress through provider records, seized servers, exchange records, extradition, and coordinated searches. State-directed or state-sheltered cases are harder: public charges may identify actors and infrastructure, but custody and evidence collection can be blocked by the suspect's location or by the sponsoring state's non-cooperation. Proxy-service takedowns add a second pattern, where the immediate target is infrastructure used by many intruders rather than one intrusion crew.

## Menu Use

Use this category when unauthorized access is the core conduct. Use [[malware-ic]] when the record focuses on malware deployment or botnet infrastructure, [[cybercrime-infrastructure-ic]] when the main target is a criminal enabling service, and [[data-sovereignty]] or [[jurisdictional-conflicts]] where the central issue is legal conflict over data access rather than the intrusion itself.
""",
    },
]


CONCEPT_TEXT: dict[str, str] = {
    "cobalt-strike": """## Summary

Cobalt Strike is a dual-use adversary-simulation framework that appears in the corpus because criminal actors abuse cracked or unauthorized copies as command-and-control tooling. The menu node helps separate the tool from a specific malware family or threat group.

## International-Cooperation Relevance

Operation Morpheus-style records show why a dual-use tool can become a cooperation issue. The legal target is not the legitimate security product; it is the unauthorized infrastructure and criminal use pattern around servers, licenses, payloads, and operators. Investigators need hosting records, server seizures, malware telemetry, and private-sector analysis to distinguish legitimate testing from criminal deployment.

## Menu Use

Use this page when a source explicitly turns on Cobalt Strike infrastructure, beacons, cracked copies, or law-enforcement disruption of unauthorized servers. Use [[malware-ic]] for the broader malware case and [[cybercrime-infrastructure-ic]] when Cobalt Strike is only one component in a larger hosting or loader ecosystem.
""",
    "eu-member-states": """## Summary

EU Member States is a corpus-normalization concept for records that rely on European Union member-state participation, legal coordination, or policy-cycle framing. It is not an organization page and should not be used as a substitute for [[europol-ec3]], [[eurojust]], or a named national authority.

## International-Cooperation Relevance

Many Europol and Eurojust records refer to member states collectively when an operation involves several EU countries. That phrasing matters because it can signal access to EU coordination structures, shared policy priorities, and recurring judicial or police cooperation workflows. It does not identify every participating agency, so country and organization pages remain necessary for specific attribution.

## Menu Use

Use this concept when a source describes EU-wide or EU member-state participation without enough detail to name every national body. Use country pages for specific jurisdictions and mechanism pages such as [[empact]], [[eurojust-coordination-meeting]], or [[european-investigation-order]] when the source identifies the legal or operational channel.
""",
    "extradition-practice": """## Summary

Extradition practice covers the operational reality of moving a suspect from one jurisdiction to another for prosecution. It is related to extradition law, but this concept is used for the practical cooperation issues: arrest timing, provisional arrest, dual criminality, nationality bars, assurances, custody transfer, and delays caused by local litigation.

## International-Cooperation Relevance

Cybercrime cases frequently identify suspects in countries different from the prosecuting forum. Even where charges are strong, a case may depend on whether the custodial state will arrest, hold, and surrender the suspect. Extradition practice therefore connects legal-framework pages to case outcomes. It also affects operational sequencing because public indictments, sanctions, domain seizures, and arrest announcements may be timed around custody risk.

## Menu Use

Use this concept where a page discusses surrender of a person, provisional arrest, extradition litigation, or custody transfer. Use [[extradition]] for the mechanism page and [[dual-criminality]] where the issue is whether the conduct is criminal in both states.
""",
    "harmonization-of-cybercrime-laws": """## Summary

Harmonization of cybercrime laws refers to the alignment of substantive offenses, procedural powers, and cooperation tools across jurisdictions. The concept is especially important for cybercrime because evidence, victims, infrastructure, and suspects often cross borders faster than domestic legal categories.

## International-Cooperation Relevance

Harmonization reduces friction in mutual assistance, extradition, preservation, and joint operations. If two states define unauthorized access, malware misuse, fraud, or data-production powers very differently, cooperation can slow down or fail. Treaties and regional instruments do not make national law identical, but they create shared minimum concepts that investigators and prosecutors can use when mapping a case across borders.

## Menu Use

Use this concept when a source discusses alignment of cybercrime statutes, procedural powers, treaty implementation, or capacity-building around legal reform. Use [[budapest-convention]] for the treaty page and [[dual-criminality]] when the practical issue is matching offenses for extradition or mutual assistance.
""",
    "money-mule-networks": """## Summary

Money mule networks are the cash-out and laundering layer for cyber-enabled fraud, banking-trojan theft, business-email-compromise schemes, romance scams, and marketplace proceeds. They turn digital compromise or deception into movable funds by recruiting people or accounts that receive, withdraw, convert, or forward criminal proceeds.

## International-Cooperation Relevance

Mule networks create cooperation needs because the victim, mule account, recruiter, exchange, and organizer may sit in different countries. Cases often require bank records, account-opening data, communications evidence, cryptocurrency tracing, and rapid freezing or recall attempts. This makes the concept relevant to [[asset-freezing]], [[mutual-legal-assistance]], and public-private financial intelligence sharing.

## Menu Use

Use this concept when the source emphasizes cash-out, laundering, mule recruitment, account control, or movement of stolen funds. Use [[banking-trojan-ic]] or [[bec-crime-ic]] for the upstream offense when the mule layer is only one part of a broader case.
""",
    "spyeye-malware": """## Summary

SpyEye malware is a banking-trojan concept node used to normalize references to credential theft, online-banking fraud, botnet administration, and mule-enabled cash-out. It is closely related to Zeus-era banking malware and appears in records about international enforcement against credential-stealing malware groups.

## International-Cooperation Relevance

SpyEye-style cases combine technical and financial evidence. Investigators need malware infrastructure data, victim-bank records, account-control evidence, and often cross-border suspect or mule information. The concept helps connect malware pages to banking-fraud and money-mule pages without treating every record as a generic intrusion case.

## Menu Use

Use this page when a source names SpyEye or describes a SpyEye-linked banking-trojan operation. Use [[zeus-malware]] for Zeus-specific records, [[banking-trojan-ic]] for the broader crime type, and [[money-mule-networks]] when the cash-out layer is the main focus.
""",
    "zeus-malware": """## Summary

Zeus malware is a banking-trojan concept node for records involving credential theft, online-banking manipulation, and botnet-enabled fraud. It is one of the recurring malware families that shaped later cybercrime cooperation patterns around botnet takedowns, arrests, and financial-fraud prosecution.

## International-Cooperation Relevance

Zeus-linked cases usually require both cyber and financial evidence. A technical takedown may disrupt command-and-control infrastructure, but prosecutors still need victim records, mule accounts, server logs, and evidence tying administrators or affiliates to the malware operation. The concept therefore links [[malware-ic]], [[banking-trojan-ic]], and [[money-mule-networks]].

## Menu Use

Use this page where a source names Zeus or a Zeus-derived banking-trojan ecosystem. Use [[spyeye-malware]] where SpyEye is named, and use [[banking-trojan-ic]] when the source discusses the broader banking-trojan enforcement pattern rather than one family.
""",
}


def update_concepts() -> None:
    for slug, body in CONCEPT_TEXT.items():
        path = WIKI_DIR / "concepts" / f"{slug}.md"
        post = frontmatter.load(path)
        sources = [wikilink_slug(item) for item in as_list(post.metadata.get("sources")) if wikilink_slug(item)]
        sources = [source for source in sources if (SOURCES_DIR / f"{source}.md").exists()]
        update_page("concepts", slug, body, sources, {"status": "active"})


def main() -> None:
    for slug, data in SOURCE_URLS.items():
        update_source_url(slug, data)
        print(f"resolved source URL {slug}")
    for page in CORE_UPDATES:
        update_page(page["category"], page["slug"], page["body"], page["sources"], page.get("meta", {}))
        print(f"enriched {page['category']}/{page['slug']}")
    update_concepts()
    print("enriched concept medium items")


if __name__ == "__main__":
    main()
