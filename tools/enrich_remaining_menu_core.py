from __future__ import annotations

from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
RUN_DATE = "2026-04-29"


def source_meta(slug: str) -> dict[str, Any]:
    path = SOURCES_DIR / f"{slug}.md"
    if not path.exists():
        raise FileNotFoundError(path)
    return frontmatter.load(path).metadata


def post_with(meta: dict[str, Any], body: str) -> str:
    post = frontmatter.Post("")
    post.metadata = meta
    post.content = body
    return frontmatter.dumps(post)


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
        publisher = meta.get("publisher") or meta.get("collection_source") or ""
        date = meta.get("publish_date") or meta.get("created") or ""
        url = meta.get("collection_url") or meta.get("source_url") or meta.get("url") or ""
        lines.append(f"| [{idx}] | [[{slug}|{title}]] | {publisher} | {date} | {url} |")
    lines.append("")
    return "\n".join(lines)


def update_wiki_page(category: str, slug: str, meta_updates: dict[str, Any], body: str, sources: list[str]) -> None:
    path = WIKI_DIR / category / f"{slug}.md"
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    meta.update(meta_updates)
    meta["updated"] = RUN_DATE
    meta["source_count"] = len(sources)
    meta["sources"] = [f"[[{source}]]" for source in sources]
    text = "\n".join([body.rstrip(), "", render_references(sources)])
    path.write_text(post_with(meta, text), encoding="utf-8")


PAGES: list[dict[str, Any]] = [
    {
        "category": "mechanisms",
        "slug": "j-cat",
        "sources": [
            "2026-04-17_europol-europa-eu_european-cybercrime-centre-structure-and-collaboration",
            "2017-12-04_europol-europa-eu_andromeda-botnet-dismantled-in-international-cyber-operation",
            "2016-01-13_welivesecurity_global-operation-against-dd4bc-results-in-arrests",
        ],
        "meta": {
            "status": "active",
            "participants": {
                "type": "mixed",
                "count": "standing taskforce; membership varies by operation",
                "notable_members": ["[[europol-ec3]]", "[[fbi-cyber-division]]", "[[uk-nca]]"],
            },
            "operations_using": ["[[andromeda-botnet-takedown]]", "[[operation-pleiades]]", "[[ramnit-botnet-takedown]]"],
        },
        "body": """## Summary

J-CAT, the Joint Cybercrime Action Taskforce, is recorded in this wiki as an operational coordination mechanism housed with Europol's European Cybercrime Centre. It is not a treaty channel and it does not replace domestic warrants, MLAT requests, or production orders. Its value is the ability to put cybercrime investigators, analysts, and liaison partners into the same operational rhythm before, during, and after an action day.

## Operational Role

The source corpus shows J-CAT most clearly in malware and extortion operations where the same infrastructure, victims, or suspects touch several jurisdictions. The Andromeda source names EC3, J-CAT, Eurojust, the FBI, German authorities, Belarusian action, and Microsoft support in a single takedown narrative. Operation Pleiades adds the DDoS extortion pattern: a victim-facing case may start in one jurisdiction, but operational progress depends on rapid intelligence sharing, suspect localization, and parallel enforcement coordination.

## Data Integrity Notes

For menu classification, use this page for the standing Europol-hosted operational taskforce. Use [[joint-investigation-team]] when the record is about a formal JIT, [[eurojust-coordination-meeting]] when the record turns on judicial coordination, and [[mutual-legal-assistance]] when the issue is evidence production through formal treaty channels. J-CAT should be treated as an intelligence-led coordination layer rather than as a self-standing legal authority.
""",
    },
    {
        "category": "mechanisms",
        "slug": "empact",
        "sources": [
            "2021-06-30_eurojust_coordinated-action-cuts-access-vpn-service-used-ransomware-groups",
            "2022-01-18_europol-europa-eu_unhappy-new-year-for-cybercriminals-as-vpnlab-net-goes-offline",
            "2025-01-30_justice-gov_cracked-and-nulled-marketplaces-disrupted-international-cyber-operation",
        ],
        "meta": {
            "status": "active",
            "operations_using": ["[[doublevpn-takedown]]", "[[vpnlab-takedown]]", "[[operation-talent]]"],
        },
        "body": """## Summary

EMPACT is the EU policy-cycle framework used to organize priority action against serious and organized crime, including cybercrime. In this repository it is treated as a coordination umbrella, not as an evidence-gathering instrument. It helps explain why separate national actions can appear as one joined campaign when Europol, Eurojust, EU member states, and selected third-country partners align priorities around a specific threat.

## Operational Role

The DoubleVPN and VPNLab records show the EMPACT pattern in infrastructure disruption. Eurojust's DoubleVPN source places the action inside the EMPACT framework and describes judicial coordination meetings and an action-day coordination centre. Europol's VPNLab source likewise links the operation to the EMPACT priority on attacks against information systems. Those records show that EMPACT can connect policy priority setting to concrete seizures, server takedowns, and follow-on investigative exploitation.

## Data Integrity Notes

Use EMPACT when the source explicitly frames an action as part of the EU policy-cycle priority structure. Do not use it as a substitute for the specific operational mechanism. In a single case, EMPACT may coexist with [[eurojust-coordination-meeting]], [[domain-seizure]], [[search-seizure]], [[asset-freezing]], or a formal [[joint-investigation-team]]. The menu distinction matters because EMPACT answers the strategic-coordination question, while the other mechanism pages answer the legal or technical execution question.
""",
    },
    {
        "category": "crime-types",
        "slug": "ddos-ic",
        "sources": [
            "fbi-international-ddos-for-hire-sweep",
            "cyberscoop-international-ddos-for-hire-sweep",
            "2024-12-11_europol-europa-eu_law-enforcement-shuts-down-27-ddos-booters-ahead-of-annual-christmas-attacks",
            "2024-09-01_justice-gov_law-enforcement-seizes-9-ddos-for-hire-webpages",
        ],
        "meta": {
            "status": "active",
            "typical_ic_challenges": ["rapid attribution", "booter-service user identification", "server and domain seizure timing"],
            "typical_mechanisms": ["[[domain-seizure]]", "[[search-seizure]]", "[[mutual-legal-assistance]]", "[[j-cat]]"],
            "key_organizations": ["[[fbi]]", "[[europol-ec3]]", "[[eurojust]]"],
        },
        "body": """## Summary

DDoS international-cooperation cases usually involve services, infrastructure, customers, and victims spread across multiple jurisdictions. The operational target is often a booter or stresser platform rather than a single attack event. This means investigators need to preserve provider data, seize domains or servers, identify paying customers, and notify victims quickly enough to keep the service from reconstituting.

## Cooperation Pattern

The 2016 international DDoS-for-hire sweep shows the older pattern: arrests and interviews of users, disruption of service providers, and public messaging aimed at deterrence. Later Operation PowerOFF sources show a more industrialized model in which law enforcement repeatedly seizes booter domains, replaces them with seizure banners, and uses customer records for follow-on prevention or prosecution. In both patterns, attribution is only one part of the case. Payment trails, account records, domain registration data, hosting logs, and victim impact are usually needed to make the enforcement action usable in court.

## Menu Use

Use this crime-type page when the source record is about DDoS extortion, booter services, stresser marketplaces, or DDoS-for-hire infrastructure. Use [[cybercrime-infrastructure-ic]] for broader infrastructure takedowns where DDoS is only one service among many, and use [[extortion-ic]] when the dominant conduct is ransom demand or coercion rather than traffic flooding.
""",
    },
    {
        "category": "crime-types",
        "slug": "malware-ic",
        "sources": [
            "2024-05-30_europol-europa-eu_largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem",
            "2021-01-27_europol-europa-eu_world-s-most-dangerous-malware-emotet-disrupted-through-global-action",
            "2023-08-30_eurojust-europa-eu_qakbot-malware-network-dismantled",
            "2026-04-18_justice-gov_justice-department-seizes-domains-behind-major-information-stealing-malware-operation",
        ],
        "meta": {
            "status": "active",
            "typical_ic_challenges": ["botnet infrastructure spans jurisdictions", "malware families rebrand or modularize", "technical remediation must align with legal seizure"],
            "typical_mechanisms": ["[[sinkholing]]", "[[domain-seizure]]", "[[search-seizure]]", "[[public-private-cooperation]]"],
            "key_organizations": ["[[europol-ec3]]", "[[fbi]]", "[[eurojust]]", "[[shadowserver]]"],
        },
        "body": """## Summary

Malware operations in this wiki cover botnets, loaders, banking trojans, infostealers, remote-access tools, and malware-enabled proxy services where cross-border coordination is necessary to identify operators, seize infrastructure, notify victims, or neutralize command-and-control systems. The cooperation problem is technical and legal at the same time: investigators need lawful access to servers and domains, while defenders need enough telemetry to prevent reinfection or migration to replacement infrastructure.

## Cooperation Pattern

Emotet, QakBot, and Operation Endgame illustrate the recurring pattern. Authorities coordinate search and seizure steps across countries, technical partners help map the malware ecosystem, and judicial or prosecutorial channels prepare the action-day package. In mature takedowns, the goal is not only to arrest operators. It is also to interrupt delivery chains, redirect or seize domains, preserve evidence, and create follow-on leads for affiliates, customers, or money-laundering services.

## Menu Use

Use this page when the principal target is malware deployment or malware infrastructure. Use [[banking-trojan-ic]] when the malware is specifically tied to online-banking theft, [[ransomware-ic]] when encryption and extortion dominate the record, and [[cybercrime-infrastructure-ic]] when the source is mainly about hosting, proxy, VPN, marketplace, or access-broker infrastructure that supports multiple crime types.
""",
    },
    {
        "category": "crime-types",
        "slug": "banking-trojan-ic",
        "sources": [
            "2019-05-01_europol-europa-eu_goznym-malware-cybercriminal-network-dismantled-in-international-operation",
            "2015-10-13_justice-gov_bugat-botnet-administrator-arrested-and-malware-disabled",
            "2015-06-27_thehackernews-com_europol-arrests-gang-behind-zeus-and-spyeye-banking-malware",
            "2019-12-05_thehackernews-com_fbi-puts-5-million-bounty-on-russian-hackers-behind-dridex-banking-malware",
        ],
        "meta": {
            "status": "active",
            "typical_ic_challenges": ["credential theft evidence", "money mule networks", "victims and banks in several countries"],
            "typical_mechanisms": ["[[mutual-legal-assistance]]", "[[extradition]]", "[[asset-freezing]]", "[[public-private-cooperation]]"],
            "key_organizations": ["[[europol-ec3]]", "[[fbi]]", "[[uk-nca]]", "[[eurojust]]"],
        },
        "body": """## Summary

Banking-trojan cooperation cases focus on malware designed to steal online-banking credentials, manipulate sessions, or support fraudulent transfers. These cases frequently combine cyber intrusion evidence with financial-crime evidence. The malware operator, botnet administrator, money mule recruiter, cash-out layer, victim bank, and hosting provider may all sit in different countries.

## Cooperation Pattern

GozNym, Bugat/Dridex, Zeus, and SpyEye records show why banking-trojan cases often require several cooperation tracks at once. Technical disruption can neutralize botnet infrastructure, but prosecution usually also needs victim-bank records, account-opening evidence, payment traces, and evidence tying defendants to malware administration or mule management. Public-private support matters because banks and security companies often detect command-and-control infrastructure and money-mule patterns before a formal action day.

## Menu Use

Use this page where the malware's primary purpose is online-banking theft or unauthorized funds transfer. Use [[malware-ic]] for broader malware families and [[money-mule-networks]] when the source mainly documents recruitment, account control, or laundering after the initial credential theft. The distinction prevents the same operation from being reduced to either a purely technical botnet case or a purely financial-fraud case.
""",
    },
    {
        "category": "crime-types",
        "slug": "cybercrime-forum-ic",
        "sources": [
            "2015-07-15_fbi-gov_cyber-criminal-forum-taken-down",
            "2015-07-15_justice-gov_darkode-forum-dismantled-w-d-pa",
            "2018-02-07_justice-gov_thirty-six-defendants-indicted-for-alleged-roles-in-transnational-criminal-organ",
            "2025-01-30_justice-gov_cracked-and-nulled-marketplaces-disrupted-international-cyber-operation",
        ],
        "meta": {
            "status": "active",
            "typical_ic_challenges": ["undercover access", "forum identity attribution", "parallel arrests and searches"],
            "typical_mechanisms": ["[[search-seizure]]", "[[domain-seizure]]", "[[extradition]]", "[[joint-investigation-team]]"],
            "key_organizations": ["[[fbi]]", "[[usdoj]]", "[[europol-ec3]]"],
        },
        "body": """## Summary

Cybercrime forum cases target online communities that broker malware, stolen credentials, payment-card data, hacking services, tutorials, or access to compromised systems. The cooperation challenge is different from a single-victim intrusion case. Investigators must attribute screen names to people, preserve private-message and transaction records, coordinate arrests before administrators warn members, and handle evidence from servers, payment systems, and undercover accounts.

## Cooperation Pattern

Darkode, Infraud, and Operation Talent show three useful patterns. Darkode was an invitation-only forum case with international undercover and takedown work. Infraud was treated as a transnational criminal organization with defendants and infrastructure distributed across countries. Operation Talent reflects the newer model of marketplace and forum disruption where domains, servers, and user databases become evidence for later actions. In each pattern, timing matters because a forum can migrate quickly once administrators detect law-enforcement interest.

## Menu Use

Use this page when the source focuses on a forum, marketplace community, or criminal service board. Use [[dark-web-ic]] where the main fact is Tor or darknet marketplace access, and use [[cybercrime-infrastructure-ic]] where the primary target is hosting, proxying, VPN, botnet, or malware delivery infrastructure rather than the social marketplace layer.
""",
    },
    {
        "category": "crime-types",
        "slug": "cybercrime-infrastructure-ic",
        "sources": [
            "2024-05-30_europol-europa-eu_largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem",
            "2022-01-18_europol-europa-eu_unhappy-new-year-for-cybercriminals-as-vpnlab-net-goes-offline",
            "2021-06-30_eurojust_coordinated-action-cuts-access-vpn-service-used-ransomware-groups",
            "2024-05-29_justice-gov_justice-department-leads-effort-to-dismantle-911-s5-botnet",
        ],
        "meta": {
            "status": "active",
            "typical_ic_challenges": ["service migration", "domain and server control", "customer attribution", "parallel victim notification"],
            "typical_mechanisms": ["[[domain-seizure]]", "[[search-seizure]]", "[[sinkholing]]", "[[asset-freezing]]"],
            "key_organizations": ["[[europol-ec3]]", "[[eurojust]]", "[[fbi]]", "[[usdoj]]"],
        },
        "body": """## Summary

Cybercrime infrastructure disruption covers actions against the services that make other crimes scalable: botnet loaders, proxy networks, bulletproof VPNs, credential shops, hosting clusters, malware-delivery domains, and command-and-control systems. The target is often not a single criminal group. It is an enabling service used by many customers, affiliates, or downstream actors.

## Cooperation Pattern

Operation Endgame, VPNLab, DoubleVPN, and the 911 S5 botnet action show the common sequence. Investigators map the infrastructure, identify legal control points, prepare seizure or disruption orders in several jurisdictions, and coordinate an action day that prevents administrators from moving domains, servers, or customer data. Evidence value is high because seized customer records can generate follow-on cases against ransomware groups, fraud actors, malware operators, or access brokers.

## Menu Use

Use this page when the source is mainly about infrastructure-as-a-service for cybercrime. If the source is about a specific malware family, use [[malware-ic]]. If it is about DDoS-for-hire, use [[ddos-ic]]. If it is about a forum where criminals trade services, use [[cybercrime-forum-ic]]. The infrastructure page should remain the cross-cutting menu node for services that support multiple criminal markets.
""",
    },
    {
        "category": "concepts",
        "slug": "extraterritorial-jurisdiction",
        "sources": [
            "2026-04-29_uscode-house-gov_18-usc-1030-computer-fraud-and-abuse-act",
            "2026-04-29_uscode-house-gov_18-usc-1343-wire-fraud",
            "2026-04-29_justice-gov_cloud-act-executive-agreements",
        ],
        "meta": {
            "status": "active",
            "summary": "Extraterritorial jurisdiction is a state's assertion of legal authority over conduct, persons, evidence, or effects connected to another territory.",
        },
        "body": """## Summary

Extraterritorial jurisdiction is the basis on which a state applies domestic law to conduct, actors, infrastructure, evidence, or effects connected to another country. In cybercrime records it matters because an intrusion can be launched abroad, routed through third-country infrastructure, affect victims in several states, and generate evidence held by providers outside the investigating state.

## Cooperation Relevance

The concept should not be treated as a shortcut around international cooperation. Even where a domestic statute reaches foreign conduct, investigators may still need MLAT requests, executive agreements, preservation requests, search warrants, extradition, or local partner action to obtain evidence and custody. The U.S. source set illustrates the distinction. Computer-fraud and wire-fraud statutes can support charges involving interstate or foreign communications, while CLOUD Act executive-agreement material concerns cross-border access to provider-held data under a specific legal arrangement.

## Menu Use

Use this concept where the main issue is the reach of domestic law beyond territorial borders. Use [[effects-doctrine]] when the asserted connection is harm or impact inside the forum state. Use [[territoriality-principle]] when infrastructure, suspect conduct, or victims are located inside the prosecuting state. Use [[jurisdictional-conflicts]] when overlapping claims create conflict between states or between investigative demands and local law.
""",
    },
    {
        "category": "concepts",
        "slug": "effects-doctrine",
        "sources": [
            "2026-04-29_uscode-house-gov_18-usc-1030-computer-fraud-and-abuse-act",
            "2026-04-29_uscode-house-gov_18-usc-1343-wire-fraud",
            "2024-05-29_justice-gov_justice-department-leads-effort-to-dismantle-911-s5-botnet",
        ],
        "meta": {
            "status": "active",
            "summary": "The effects doctrine links jurisdiction to harmful effects experienced inside the forum state, even when parts of the conduct occurred elsewhere.",
        },
        "body": """## Summary

The effects doctrine is a jurisdictional idea used when conduct outside a state's territory produces legally relevant harm inside that state. In cybercrime, this is common: malware infrastructure may be administered abroad, customers may be distributed globally, and the victims or financial losses may appear in the forum state.

## Cooperation Relevance

The doctrine helps explain why a state may open a case or bring charges, but it does not remove the need for cooperation. A forum state may have victims, banks, government systems, or service providers affected by the conduct, while suspects, servers, domain registrars, and cryptocurrency exchanges sit elsewhere. The 911 S5 record is a practical example of this structure: U.S. victims and fraud losses were central to the case, yet the disruption required coordination with Singapore, Thailand, Germany, and U.S. agencies. Statutory hooks such as computer-fraud and wire-fraud provisions can provide the domestic charging theory, while mutual assistance and coordinated seizures provide the operational path.

## Menu Use

Use this concept when a record turns on domestic harm from foreign or distributed conduct. Use [[extraterritorial-jurisdiction]] for the broader legal reach question and [[territoriality-principle]] when the relevant conduct or infrastructure is physically inside the forum state.
""",
    },
    {
        "category": "organizations",
        "slug": "fbi",
        "sources": [
            "2016-12-09_fbi-gov_international-cyber-sweep-nets-ddos-attackers",
            "2024-05-29_fbi-gov_how-to-identify-and-remove-vpn-applications-that-contain-911-s5-backdoors",
            "fbi-operation-shrouded-horizon",
        ],
        "meta": {
            "jurisdiction": "United States",
            "key_roles": ["cybercrime investigations", "international liaison", "infrastructure seizure support", "victim notification"],
        },
        "body": """## Summary

FBI is retained as the shorthand organization page for records that name the Federal Bureau of Investigation without specifying a subunit. The more detailed cybercrime unit page remains [[fbi-cyber-division]], but this page now carries enough source-backed metadata for menu navigation and legacy backlinks.

## International Cooperation Role

The FBI appears across DDoS, malware, darknet, botnet, and fraud records as a U.S. investigative agency with both domestic field-office capacity and international liaison reach. The source set links it to Operation Shrouded Horizon, DDoS-for-hire enforcement, and victim guidance after the 911 S5 disruption. Use this page where the record names FBI generally; use a more specific page when the source identifies a field office, Cyber Division, or task-force component.
""",
    },
    {
        "category": "organizations",
        "slug": "usdoj",
        "sources": [
            "2024-05-29_justice-gov_justice-department-leads-effort-to-dismantle-911-s5-botnet",
            "2019-05-16_justice-gov_goznym-cyber-criminal-network-operating-out-of-europe-targeting-american-entitie",
            "2025-01-30_justice-gov_cracked-and-nulled-marketplaces-disrupted-international-cyber-operation",
        ],
        "meta": {
            "jurisdiction": "United States",
            "key_roles": ["federal prosecution", "international evidence coordination", "public charging announcements", "asset forfeiture"],
        },
        "body": """## Summary

US DOJ is the shorthand page for the United States Department of Justice. The canonical organization page remains [[us-doj]], but this record is kept for operation pages and source imports that used the older abbreviated slug.

## International Cooperation Role

The DOJ source set shows federal prosecution and public action-day coordination in botnet, malware, cybercrime forum, and financial-fraud cases. DOJ records often provide the clearest public basis for charges, forfeiture allegations, extradition posture, and foreign partner participation. Use this shorthand page for legacy links; use [[us-doj]] when editing new pages or when a source specifically refers to the Department rather than an imported abbreviation.
""",
    },
    {
        "category": "organizations",
        "slug": "kaspersky-lab",
        "sources": [
            "2015-04-13_kaspersky-com_kaspersky-lab-joins-forces-with-interpol-industry-and-law-enforcement-partners-to-disrupt-simda-botnet",
            "2023-08-18_kaspersky_assists-interpol-in-operation-to-disrupt-cybercrime-in-african-countries",
            "2025-04-01_kaspersky-com_kaspersky-supports-interpol-operation-secure",
        ],
        "meta": {
            "jurisdiction": "Private-sector cybersecurity vendor; multinational technical support role",
            "country": "multinational",
            "key_roles": ["threat intelligence", "malware analysis", "private-sector support to INTERPOL operations"],
        },
        "body": """## Summary

Kaspersky Lab appears in this wiki as a private-sector cybersecurity company that provides threat intelligence and malware-analysis support to law-enforcement operations. The page is not used to describe a state authority; it is used to capture private-sector technical participation.

## International Cooperation Role

The source corpus links Kaspersky to Simda, Africa Cyber Surge II, and Operation Secure. In these records the company contributes intelligence, malware or infrastructure analysis, and operational support to INTERPOL-led or multi-partner actions. When using this page, distinguish technical support from legal authority: Kaspersky can supply intelligence and analysis, but arrests, searches, seizures, and evidence production remain with public authorities and courts.
""",
    },
    {
        "category": "organizations",
        "slug": "shadowserver",
        "sources": [
            "2016-11-30_europol-europa-eu_avalanche-network-dismantled-in-international-cyber-operation",
            "2019-05-16_justice-gov_goznym-cyber-criminal-network-operating-out-of-europe-targeting-american-entitie",
            "2026-03-12_justice-gov_authorities-dismantle-global-malicious-proxy-service-deployed-malware-and-defrauded",
        ],
        "meta": {
            "jurisdiction": "Private-sector nonprofit technical community; international support role",
            "country": "international",
            "key_roles": ["sinkholing support", "victim notification data", "botnet and proxy-infrastructure telemetry"],
        },
        "body": """## Summary

Shadowserver is represented as a nonprofit technical partner supporting botnet, malware, proxy, and abuse-infrastructure disruption. It is not a law-enforcement body; its role is technical measurement, sinkhole support, abuse reporting, and victim-notification data.

## International Cooperation Role

Avalanche, GozNym, and malicious proxy-service records show why a neutral technical partner can matter in cross-border operations. Public authorities may obtain the legal authority for seizures or arrests, while organizations such as Shadowserver help transform seized or sinkholed infrastructure into actionable remediation data. Use this page when the record emphasizes technical disruption or post-takedown notification rather than prosecution.
""",
    },
    {
        "category": "organizations",
        "slug": "ncfta",
        "sources": [
            "fbi-operation-shrouded-horizon",
            "2015-07-15_fbi-gov_cyber-criminal-forum-taken-down",
            "2019-05-16_justice-gov_goznym-cyber-criminal-network-operating-out-of-europe-targeting-american-entitie",
        ],
        "meta": {
            "jurisdiction": "United States public-private partnership",
            "key_roles": ["public-private intelligence sharing", "case support", "industry liaison"],
        },
        "body": """## Summary

NCFTA is the National Cyber-Forensics and Training Alliance, represented here as a U.S.-based public-private collaboration body. It is used in the wiki where sources describe industry, law-enforcement, and analytical collaboration around cybercrime investigations.

## International Cooperation Role

The strongest local source link is Operation Shrouded Horizon, where NCFTA appears in the public-private support environment around the Darkode forum takedown. GozNym material also illustrates the broader need for financial-sector and technical-sector cooperation in malware-enabled bank fraud. Use this page for the collaboration body, not for a law-enforcement agency or prosecutorial authority.
""",
    },
    {
        "category": "organizations",
        "slug": "nigeria-police-force",
        "sources": [
            "2020-11-01_interpol-int_three-arrested-as-interpol-group-ib-and-the-nigeria-police-force-disrupt-prol",
            "2020-11-25_group-ib_operation-falcon-group-ib-helps-interpol-identify-nigerian-bec-ring-members",
            "2022-05-25_interpol-int_suspected-head-of-cybercrime-gang-arrested-in-nigeria",
        ],
        "meta": {
            "jurisdiction": "Nigeria",
            "key_roles": ["domestic arrests", "cybercrime unit execution", "INTERPOL-supported BEC investigations"],
        },
        "body": """## Summary

Nigeria Police Force is the national police organization of Nigeria. In this wiki it is most visible through INTERPOL-supported operations against business-email-compromise and SilverTerrier/TMT actors.

## International Cooperation Role

Operation Falcon and Operation Delilah show the same cooperation model from two angles. INTERPOL and private-sector partners supplied intelligence and coordination, while Nigerian police executed domestic investigative and arrest steps in Lagos and related locations. This page should be used when the source names the national police body; use a more specific cybercrime-unit page only when the source identifies that unit directly.
""",
    },
    {
        "category": "organizations",
        "slug": "afripol",
        "sources": [
            "2023-08-18_interpol-int_cybercrime-14-arrests-thousands-of-illicit-cyber-networks-disrupted-in-africa-op",
            "2023-08-18_group-ib-com_africa-cyber-surge-ii",
            "2023-06-30_coe-int_glacy-supports-interpol-s-africa-cyber-surge-operation-ii",
        ],
        "meta": {
            "jurisdiction": "African Union member-state police cooperation",
            "key_roles": ["continental police coordination", "joint cyber operations with INTERPOL", "capacity building"],
        },
        "body": """## Summary

AFRIPOL is the African Union's continental police cooperation mechanism. In the cybercrime corpus it appears most often with INTERPOL in Africa-wide operations that combine coordination, capacity building, and action against compromised infrastructure or online-fraud networks.

## International Cooperation Role

Africa Cyber Surge II is the clearest source-backed example. INTERPOL and AFRIPOL coordinated activity across 25 African countries, supported by private-sector intelligence and donor-funded capacity-building programs. The record should be read as regional coordination rather than as a single-country investigation. Use AFRIPOL when the source frames an action through the African Union or continental police-cooperation layer; use the national police page when the source identifies a specific executing country.
""",
    },
    {
        "category": "organizations",
        "slug": "uk-metropolitan-police",
        "sources": [
            "europol-operation-pleiades",
            "europol-rex-mundi-hacking-group-takedown",
        ],
        "meta": {
            "jurisdiction": "United Kingdom; Greater London policing jurisdiction",
            "key_roles": ["local and specialist police support", "cyber extortion investigation support", "UK-facing victim coordination"],
        },
        "body": """## Summary

The Metropolitan Police Service is London's police service. In this repository it mainly acts as the parent entry for London Metropolitan Police cybercrime participation references and for [[uk-met-police-cyber|Metropolitan Police Cyber Crime Unit]].

## Cybercrime Cooperation Role

The source corpus connects the Met to cross-border cybercrime cases through Europol-coordinated operations. Operation Pleiades identifies UK Metropolitan Police support in the DD4BC DDoS-for-Bitcoin extortion case. The Rex Mundi source records London Metropolitan Police participation in a year-long investigation that moved from a UK victim company to arrests in France and Thailand with Europol and J-CAT coordination.

## IC Relevance

Use this parent page when a source names the Metropolitan Police Service or London Metropolitan Police without identifying a cyber-specific unit. Use [[uk-met-police-cyber]] for cyber unit details and [[uk-nca]] where the case is led by the UK's national serious and organized crime agency.
""",
    },
]


def main() -> None:
    for page in PAGES:
        update_wiki_page(
            category=page["category"],
            slug=page["slug"],
            meta_updates=page["meta"],
            body=page["body"],
            sources=page["sources"],
        )
        print(f"updated {page['category']}/{page['slug']}")


if __name__ == "__main__":
    main()
