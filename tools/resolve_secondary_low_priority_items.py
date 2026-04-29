from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
RUN_DATE = "2026-04-29"


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, "", {}):
        return []
    return [value]


def slug_from_link(value: str) -> str:
    value = str(value or "").strip()
    if value.startswith("[[") and value.endswith("]]"):
        return value[2:-2].split("|", 1)[0].strip()
    return value


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


def render_refs(slugs: list[str]) -> str:
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
        url = meta.get("collection_url") or meta.get("source_url") or ""
        lines.append(f"| [{idx}] | [[{slug}|{title}]] | {publisher} | {date} | {url} |")
    lines.append("")
    return "\n".join(lines)


def update_page(category: str, slug: str, sources: list[str], body: str, extra: dict[str, Any] | None = None) -> None:
    path = WIKI_DIR / category / f"{slug}.md"
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    meta.update(extra or {})
    meta["status"] = meta.get("status") or "active"
    meta["updated"] = RUN_DATE
    meta["source_count"] = len(sources)
    meta["sources"] = [f"[[{source}]]" for source in sources]
    path.write_text(post_with(meta, f"{body.rstrip()}\n\n{render_refs(sources)}"), encoding="utf-8")


def normalize_remaining_generated_phrases() -> int:
    replacements = {
        "This source was generated from `raw/case-documents/2025-04-17_opa_parsarad-nemesis-indictment.md` and corrected to reflect the actual DOJ announcement rather than the page chrome that had been ingested previously.": "The `raw_path` metadata points to the corrected Parsarad/Nemesis indictment digest; this record now reflects the actual DOJ announcement rather than previously ingested page chrome.",
        "This source was generated from `raw/press-releases/2026-04-17_justice-gov_administrator-of-nemesis-market-charged-for-role-operating-darknet-marketplace.md` and corrected to reflect the actual DOJ press-release content.": "The `raw_path` metadata points to the corrected Nemesis Market DOJ press-release digest; this record now reflects the public charging announcement content.",
    }
    changed = 0
    for path in SOURCES_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in replacements.items():
            updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


PAGE_UPDATES: list[dict[str, Any]] = [
    {
        "category": "mechanisms",
        "slug": "24-7-network",
        "sources": ["2026-04-17_coe-int_about-the-convention-budapest-convention", "2003-01-28_coe-int_treaty-text-and-status-chart"],
        "body": """## Summary

The 24/7 network is the urgent-contact mechanism associated with cybercrime cooperation frameworks such as the Budapest Convention. It exists because volatile electronic evidence can disappear faster than formal mutual-assistance channels can operate.

## Cooperation Use

In wiki classification, the 24/7 network should be used for preservation, urgent points of contact, and rapid coordination before a full evidence-production request is ready. It is not itself a warrant, subpoena, or MLAT return channel. A 24/7 contact can help identify the correct authority, preserve data, or route an urgent request, while later production still depends on domestic law, treaty channels, provider process, or a court order.

## Boundary Notes

Use [[emergency-data-preservation]] for the procedural act of preserving data, [[mutual-legal-assistance]] or [[mlat-process]] for formal evidence transfer, and [[direct-provider-request]] when the request is made to a provider under applicable domestic or cross-border provider-access rules.
""",
    },
    {
        "category": "mechanisms",
        "slug": "interpol-i-grip",
        "sources": ["2024-06-18_interpol_operation-first-light-2024", "2024-11-27_interpol-int-fr_operation-haechi-v-5500-arrests"],
        "body": """## Summary

INTERPOL's I-GRIP framing is used in this corpus for rapid intervention against cyber-enabled financial crime, especially when funds can still be frozen, recalled, or traced shortly after a fraud event.

## Cooperation Use

The strongest linked examples are Operation First Light and HAECHI-series records. Those operations show a financial-disruption pattern: local reports and bank data identify fraud flows, INTERPOL coordination helps connect jurisdictions, and participating authorities move quickly to intercept proceeds or arrest suspects. The mechanism should be read as rapid operational coordination rather than a substitute for domestic seizure law.

## Boundary Notes

Use this page when the source explicitly emphasizes INTERPOL rapid intervention or financial recovery coordination. Use [[asset-freezing]] for legal restraint of funds, [[money-mule-networks]] for the cash-out layer, and [[public-private-cooperation]] when banks or payment platforms are the main cooperation channel.
""",
    },
    {
        "category": "mechanisms",
        "slug": "europol-jit",
        "sources": ["2015-06-01_europol-europa-eu_major-cybercrime-ring-dismantled-by-joint-investigation-team", "europol-zeusspyeye-joint-investigation-team-takedown"],
        "body": """## Summary

Europol JIT is retained as a compatibility page for joint-investigation-team references that specifically appear in Europol cybercrime records. The broader mechanism page is [[joint-investigation-team]], but this page helps older operation records resolve a Europol-specific shorthand.

## Cooperation Use

The Zeus/SpyEye record shows why a JIT matters in cybercrime: suspects, malware infrastructure, victims, bank records, and money mules can be spread across several states. A joint investigation team can reduce repeated request cycles by letting participating authorities exchange information and coordinate investigative steps under an agreed legal framework.

## Boundary Notes

Use this page for Europol-linked JIT shorthand. Use [[j-cat]] for the standing EC3 operational taskforce, [[eurojust-coordination-meeting]] for judicial coordination, and [[mlat-process]] where there is no JIT and evidence still moves through formal assistance.
""",
    },
    {
        "category": "mechanisms",
        "slug": "mlat-process",
        "sources": ["2026-04-29_congress-gov_us-australia-mlat-treaty-document-105-27", "2026-04-29_congress-gov_korea-us-mlat-treaty-document-104-1"],
        "body": """## Summary

The MLAT process is the formal mutual legal assistance workflow for requesting evidence, service, search, seizure, testimony, or other judicial assistance from another state. In cybercrime it remains important where provider data, bank records, seized devices, or witness evidence must be obtained through another sovereign's legal system.

## Cooperation Use

MLAT requests are slower than informal police-to-police coordination, but they can produce evidence with clearer admissibility and judicial authority. The treaty examples linked here show the state-to-state basis for assistance. In practice, investigators may use preservation, informal deconfliction, or direct provider channels first, then submit an MLAT package for production, search, or admissible records.

## Boundary Notes

Use this page when the source is about formal assistance. Use [[informal-cooperation]] for intelligence sharing, [[emergency-data-preservation]] for preserving data before production, and [[direct-provider-request]] for provider-facing request paths.
""",
    },
    {
        "category": "procedures",
        "slug": "extradition-request",
        "sources": ["2026-04-29_congress-gov_korea-us-mlat-treaty-document-104-1", "2024-11-18_bleepingcomputer_us-charges-phobos-ransomware-admin-after-south-korea-extradition"],
        "body": """## Summary

An extradition request is the formal procedure by which one state asks another to arrest and surrender a person for prosecution or sentence enforcement. In cybercrime, extradition is often the step that turns a public indictment into a case that can actually proceed in the charging court.

## Cooperation Use

The request must usually identify charges, facts, identity, treaty basis, and supporting judicial material. Practical issues include provisional arrest, dual criminality, nationality restrictions, specialty, human-rights objections, and local litigation. Cybercrime cases add timing pressure because suspects may move between jurisdictions and because digital evidence can be handled separately from custody.

## Boundary Notes

Use this procedure page for the request workflow. Use [[extradition]] for the broader cooperation mechanism, [[dual-criminality]] for offense matching, and [[specialty-principle]] for limits on prosecuting a surrendered person beyond the extradited offenses.
""",
    },
    {
        "category": "procedures",
        "slug": "emergency-data-preservation",
        "sources": ["2026-04-17_coe-int_about-the-convention-budapest-convention", "2022-05-12_coe-int_second-additional-protocol-cets-no-224", "2026-04-29_justice-gov_cloud-act-executive-agreements"],
        "body": """## Summary

Emergency data preservation is the procedure used to prevent volatile electronic evidence from being deleted, overwritten, or moved before investigators can obtain it through the proper legal channel.

## Cooperation Use

Preservation is not the same as disclosure. A preservation request or order keeps data available while investigators prepare a domestic warrant, production order, MLAT request, executive-agreement request, or other lawful access process. In cross-border cases, preservation can be decisive because logs, subscriber records, cloud data, and transaction traces may have short retention periods.

## Boundary Notes

Use this page for preservation steps. Use [[electronic-evidence]] for the evidence category, [[24-7-network]] for urgent contact routing, [[mlat-process]] for formal evidence transfer, and [[cloud-act]] or [[us-uk-cloud-act-agreement]] where the source concerns a specific provider-data access framework.
""",
    },
    {
        "category": "legal-frameworks",
        "slug": "cloud-act",
        "sources": ["2026-04-29_justice-gov_cloud-act-executive-agreements", "2026-04-29_justice-gov_us-uk-data-access-agreement-enters-force"],
        "body": """## Summary

The CLOUD Act is a U.S. legal framework relevant to provider-held electronic evidence and executive agreements for cross-border data access. In this corpus it is treated as an evidence-access framework, not as a general cybercrime offense statute.

## Cooperation Use

The DOJ sources explain the role of executive agreements in allowing qualifying foreign partners to make direct requests to covered service providers under defined safeguards. The framework matters for cybercrime because provider-held account, traffic, subscriber, and content data can be central to attribution and victim identification.

## Boundary Notes

Use this page for CLOUD Act framework references. Use [[us-uk-cloud-act-agreement]] for the specific U.S.-UK agreement, [[electronic-evidence]] for the evidence category, and [[mlat-process]] when the source concerns traditional mutual assistance rather than a direct provider-access route.
""",
    },
    {
        "category": "legal-frameworks",
        "slug": "second-additional-protocol",
        "sources": ["2022-05-12_coe-int_second-additional-protocol-cets-no-224", "2025-01-01_coe-int_chart-of-signatures-and-ratifications-of-treaty-185-224"],
        "body": """## Summary

The Second Additional Protocol to the Budapest Convention addresses enhanced cooperation and disclosure of electronic evidence. It is relevant to cybercrime cases because provider data and cross-border preservation often become the bottleneck in fast-moving investigations.

## Cooperation Use

The protocol is used in this repository as a legal-framework node for improved disclosure channels, emergency cooperation, and structured electronic-evidence cooperation. It should not be treated as self-executing in every jurisdiction; implementation and availability depend on each state's ratification status and domestic law.

## Boundary Notes

Use this page when a source discusses the protocol itself. Use [[budapest-convention]] for the base treaty, [[emergency-data-preservation]] for preservation procedure, and [[direct-provider-request]] where the source turns on provider-facing requests.
""",
    },
    {
        "category": "crime-types",
        "slug": "csam-ic",
        "sources": ["2024-09-26_interpol-int_20-rescued-144-arrested-in-major-child-abuse-operation-across-south-america", "2025-04-04_securityaffairs-com_operation-stream-kidflix", "2025-04-07_korea-npa_operation-cyber-guardian-asia-csam"],
        "body": """## Summary

CSAM international-cooperation cases involve online distribution, production, possession, streaming, or platform facilitation of child sexual abuse material where offenders, victims, platforms, payment systems, or hosting infrastructure cross borders.

## Cooperation Use

Operation Orion International, Operation Stream/Kidflix, and Operation Cyber Guardian show three recurring patterns: victim identification across countries, platform or server takedown, and coordinated arrests based on shared intelligence. These cases often require rapid provider data, device forensics, cryptocurrency or payment tracing, child-protection coordination, and careful handling of victim-identifying material.

## Boundary Notes

Use this page where CSAM is the principal crime type. Use [[dark-web-ic]] when the record is mainly about darknet marketplace infrastructure, [[electronic-evidence]] for provider/device evidence, and [[interpol-icse-database]] where the source specifically concerns victim-identification data sharing.
""",
    },
    {
        "category": "concepts",
        "slug": "dual-criminality",
        "sources": ["2026-04-29_congress-gov_korea-us-mlat-treaty-document-104-1", "2026-04-29_congress-gov_us-australia-mlat-treaty-document-105-27"],
        "body": """## Summary

Dual criminality is the requirement, common in extradition and some assistance contexts, that the conduct underlying a request be criminal in both the requesting and requested states.

## Cooperation Use

In cybercrime, dual criminality can be straightforward for fraud, malware deployment, unauthorized access, and CSAM, but harder where countries define data offenses, platform liability, speech offenses, or encryption-related conduct differently. The concept is therefore important when a page analyzes whether a suspect can be surrendered or whether a coercive assistance request can be executed.

## Boundary Notes

Use this page for offense-matching analysis. Use [[extradition-request]] for the procedural request, [[specialty-principle]] for post-surrender limits, and [[harmonization-of-cybercrime-laws]] when the focus is aligning domestic laws to reduce these conflicts.
""",
    },
    {
        "category": "concepts",
        "slug": "specialty-principle",
        "sources": ["2026-04-29_congress-gov_korea-us-mlat-treaty-document-104-1", "2024-11-18_bleepingcomputer_us-charges-phobos-ransomware-admin-after-south-korea-extradition"],
        "body": """## Summary

The specialty principle limits how a requesting state may prosecute or punish a person after extradition. In general, the surrendered person may be tried for the offenses for which extradition was granted, unless the requested state consents to additional charges or another exception applies.

## Cooperation Use

Cybercrime indictments can include overlapping computer-fraud, wire-fraud, money-laundering, sanctions, identity-theft, and conspiracy counts. Specialty matters because prosecutors must align the case they plan to try with the offenses approved by the requested state. It can also affect superseding indictments and follow-on charges.

## Boundary Notes

Use this concept when a record discusses post-extradition charging limits. Use [[dual-criminality]] for offense matching before surrender and [[extradition-request]] for the request procedure.
""",
    },
    {
        "category": "concepts",
        "slug": "territoriality-principle",
        "sources": ["2026-04-29_uscode-house-gov_18-usc-1030-computer-fraud-and-abuse-act", "2026-04-29_uscode-house-gov_18-usc-1343-wire-fraud"],
        "body": """## Summary

The territoriality principle links jurisdiction to conduct, infrastructure, victims, effects, or evidence located inside a state's territory. In cybercrime it is often complicated by distributed routing and cloud infrastructure.

## Cooperation Use

A state may assert territorial jurisdiction because a victim system, bank, server, provider, or criminal act is located domestically. That does not eliminate the need for cooperation when other parts of the case are abroad. The principle is therefore useful for distinguishing domestic charging authority from the international evidence steps needed to prove the case.

## Boundary Notes

Use this page when the source turns on domestic location. Use [[effects-doctrine]] for domestic harm from foreign conduct and [[extraterritorial-jurisdiction]] for broader assertions of authority beyond territory.
""",
    },
    {
        "category": "concepts",
        "slug": "nationality-principle",
        "sources": ["2026-04-29_congress-gov_korea-us-mlat-treaty-document-104-1", "2026-04-29_uscode-house-gov_18-usc-1030-computer-fraud-and-abuse-act"],
        "body": """## Summary

The nationality principle links jurisdiction to the nationality of the suspect or, in some contexts, the victim. It matters in cybercrime because suspects often operate abroad while retaining legal ties to a home state.

## Cooperation Use

Some states prefer to prosecute their nationals domestically rather than extradite them. Others may use nationality as an additional basis for jurisdiction where domestic victims or infrastructure are harder to identify. This can create cooperation choices: extradition, domestic prosecution after evidence sharing, or parallel proceedings.

## Boundary Notes

Use this concept when nationality drives jurisdiction or custody strategy. Use [[extradition-practice]] for practical surrender issues and [[ne-bis-in-idem]] when parallel proceedings raise double-prosecution concerns.
""",
    },
    {
        "category": "concepts",
        "slug": "ne-bis-in-idem",
        "sources": ["2026-04-29_congress-gov_korea-us-mlat-treaty-document-104-1", "2026-04-29_congress-gov_us-australia-mlat-treaty-document-105-27"],
        "body": """## Summary

Ne bis in idem is the principle that a person should not be prosecuted or punished twice for the same conduct after a final resolution, subject to the exact rule adopted in the relevant legal system.

## Cooperation Use

Cybercrime cases can produce parallel investigations because victims, servers, financial accounts, and suspects are spread across countries. The principle matters when deciding which jurisdiction should prosecute, whether evidence should be shared for a separate proceeding, and whether a prior judgment blocks later charges.

## Boundary Notes

Use this page for double-prosecution concerns. Use [[jurisdictional-conflicts]] when the problem is broader overlap between states and [[specialty-principle]] when the issue arises after extradition.
""",
    },
    {
        "category": "challenges",
        "slug": "data-sovereignty",
        "sources": ["2026-04-29_justice-gov_cloud-act-executive-agreements", "2022-05-12_coe-int_second-additional-protocol-cets-no-224"],
        "body": """## Summary

Data sovereignty is the challenge created when data relevant to an investigation is stored, controlled, routed, or legally protected in a jurisdiction different from the investigating authority.

## Cooperation Use

Cybercrime investigations often need provider-held content, subscriber records, traffic data, logs, cloud backups, or payment records. Those records may be physically stored in one state, controlled by a provider in another, and relevant to victims in several more. Data-sovereignty concerns shape whether investigators use MLAT, direct provider requests, CLOUD Act executive agreements, emergency preservation, or local partner action.

## Boundary Notes

Use this challenge page when legal control over data is the bottleneck. Use [[electronic-evidence]] for the evidence type and [[jurisdictional-conflicts]] when overlapping legal demands or blocking laws create direct conflict.
""",
    },
    {
        "category": "challenges",
        "slug": "jurisdictional-conflicts",
        "sources": ["2026-04-29_justice-gov_cloud-act-executive-agreements", "2026-04-17_coe-int_about-the-convention-budapest-convention"],
        "body": """## Summary

Jurisdictional conflicts arise when more than one state has a plausible claim to investigate, prosecute, demand data, restrain assets, or control a suspect in the same cybercrime matter.

## Cooperation Use

Conflicts can involve overlapping victim states, infrastructure states, suspect nationality, provider location, and data-protection law. They can delay evidence access, complicate extradition, or force prosecutors to choose between parallel proceedings and a lead-jurisdiction model. Formal treaties, executive agreements, and coordination bodies reduce but do not remove these conflicts.

## Boundary Notes

Use this page for overlapping authority problems. Use [[data-sovereignty]] when the core issue is data control and [[extraterritorial-jurisdiction]] when the page focuses on one state's legal reach.
""",
    },
]


OPERATION_SOURCE_FIXES = {
    "dridex-operations": [
        "2015-10-13_justice-gov_bugat-botnet-administrator-arrested-and-malware-disabled",
        "2015-10-13_fbi-gov_bugat-botnet-administrator-arrested-and-malware-disabled",
        "2019-12-05_justice-gov_russian-national-charged-with-decade-long-series-of-hacking-and-bank-fraud",
        "2019-12-05_home-treasury-gov_treasury-sanctions-evil-corp-the-russia-based-cybercriminal-group-behind-dridex",
        "2019-12-05_nca-newsroom-prgloo-com_international-law-enforcement-operation-exposes-the-world-s-most-harmful-cyber-c",
    ],
    "myanmar-kokang-scam-compound-crackdown": [
        "2023-11-20_voanews-com_myanmar-rebel-offensive-helps-china-s-cybercrime-crackdown",
        "2023-11-21_news-cgtn-com_31-000-telecom-scam-suspects-handed-over-to-china-by-myanmar",
    ],
    "operation-heart-blocker": [
        "2025-01-29_sdtx_heartsender-seizure",
        "2025-01-30_cyberscoop-com_department-of-justice-partners-with-dutch-police-to-break-up-heartsender-network",
        "2025-01-30_hackread-com_heartsender-cybercrime-network-dismantled-in-joint-us-dutch-operation",
        "2025-05-28_krebsonsecurity-com_pakistan-arrests-21-in-heartsender-malware-service",
    ],
    "operation-kraken-ghost-platform": ["2024-09-18_afp-gov-au_afp-operation-kraken-charges-alleged-head-of-global-organised-crime-app"],
    "bali-villa-cybercrime-raid-2024": [
        "2024-06-28_aljazeera-com_indonesia-says-will-deport-103-taiwanese-suspected-of-cybercrimes-in-bali",
        "2024-06-28_therecord-media_indonesia-arrests-over-100-foreigners-in-bali-suspected-of-participating-in-cybe",
        "2024-06-29_taipeitimes-com_103-taiwanese-detained-in-bali-cybercrime-raid",
    ],
    "bidencash-takedown": [
        "2025-06-04_justice-gov_in-re-seizure-of-bidencash-marketplace-domains-and-cryptocurrency",
        "2025-06-01_thehackernews-com_doj-seizes-145-domains-tied-to-bidencash-marketplace",
        "2025-06-01_therecord-media_us-and-netherlands-take-down-bidencash-cybercrime-marketplace-infrastructure",
        "2025-06-06_helpnetsecurity-com_bidencash-marketplace-domains-seized-in-coordinated-international-action",
    ],
    "operation-onymous": [
        "2014-11-06_fbi-gov_operator-of-silk-road-2-0-website-charged-in-manhattan-federal-court",
        "2014-11-06_ice-gov_international-probe-leads-to-the-arrest-of-the-alleged-operator-of-silk-road-2-0",
        "2015-01-01_swansea-ac-uk_gdpo-situation-analysis-operation-onymous",
        "2026-04-17_en-wikipedia-org_operation-onymous",
    ],
    "trickbot-operations": [
        "2020-10-12_cyberscoop-com_cyber-command-microsoft-take-action-against-trickbot",
        "2020-10-20_blogs-microsoft-com_an-update-on-disruption-of-trickbot",
        "2023-09-07_justice-gov_multiple-foreign-nationals-charged-in-connection-with-trickbot-malware-and-conti",
        "2024-01-01_bleepingcomputer-com_russian-trickbot-malware-dev-sentenced-to-64-months-in-prison",
    ],
}


def update_operation_sources() -> int:
    changed = 0
    for slug, sources in OPERATION_SOURCE_FIXES.items():
        path = WIKI_DIR / "operations" / f"{slug}.md"
        if not path.exists():
            continue
        post = frontmatter.load(path)
        meta = dict(post.metadata)
        meta["sources"] = [f"[[{source}]]" for source in sources]
        meta["source_count"] = len(sources)
        meta["updated"] = RUN_DATE
        path.write_text(post_with(meta, post.content or ""), encoding="utf-8")
        changed += 1
    return changed


def main() -> None:
    print(f"Remaining generated phrases normalized: {normalize_remaining_generated_phrases()}")
    for item in PAGE_UPDATES:
        update_page(item["category"], item["slug"], item["sources"], item["body"])
        print(f"updated {item['category']}/{item['slug']}")
    print(f"operation source metadata fixed: {update_operation_sources()}")


if __name__ == "__main__":
    main()
