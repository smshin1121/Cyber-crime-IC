from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
LEGAL_DIR = WIKI_DIR / "legal-frameworks"
SOURCES_DIR = WIKI_DIR / "sources"
RAW_DIR = ROOT / "raw" / "source-digests"
RUN_DATE = "2026-04-29"


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def post_with(meta: dict[str, Any], body: str) -> str:
    post = frontmatter.Post("")
    post.metadata = meta
    post.content = body
    return frontmatter.dumps(post)


def ensure_source(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    raw_rel = f"raw/source-digests/{slug}.md"
    raw_path = ROOT / raw_rel
    source_path = SOURCES_DIR / f"{slug}.md"
    digest = entry["summary"]

    raw_meta = {
        "type": "raw-source",
        "title": entry["title"],
        "source_url": entry["url"],
        "publisher": entry["publisher"],
        "publish_date": entry["date"],
        "ingest_date": RUN_DATE,
        "storage_mode": "source-digest",
        "text_status": "summarized",
        "copyright_policy": "summary-only",
        "harvest_status": "manual_digest",
        "word_count": word_count(digest),
    }
    raw_body = "\n".join(["## Source Digest", "", digest, ""])
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_text(post_with(raw_meta, raw_body), encoding="utf-8")

    source_meta = {
        "type": "source",
        "title": entry["title"],
        "raw_path": raw_rel,
        "source_type": entry["source_type"],
        "publisher": entry["publisher"],
        "author": "",
        "publish_date": entry["date"],
        "ingest_date": RUN_DATE,
        "language": "en",
        "reliability": entry.get("reliability", "high"),
        "credibility": "confirmed",
        "sensitivity": "public",
        "pages_updated": entry.get("pages_updated", []),
        "key_findings": [digest],
        "collection_url": entry["url"],
        "created": RUN_DATE,
        "text_status": "summarized",
        "storage_mode": "source-digest",
        "word_count": word_count(digest),
        "copyright_policy": "summary-only",
    }
    body = "\n".join(
        [
            "## Source Summary",
            "",
            digest,
            "",
            "## Relevance to IC",
            "",
            "This source is used to support legal-framework menu pages that explain how statutes, treaties, executive agreements, or data-protection instruments affect cybercrime investigation and cross-border evidence cooperation.",
            "",
        ]
    )
    source_path.write_text(post_with(source_meta, body), encoding="utf-8")
    return slug


SOURCES = {
    "uscode-1030": {
        "slug": "2026-04-29_uscode-house-gov_18-usc-1030-computer-fraud-and-abuse-act",
        "title": "18 U.S.C. 1030 - Fraud and related activity in connection with computers",
        "publisher": "Office of the Law Revision Counsel, U.S. House of Representatives",
        "date": "2026-04-18",
        "url": "https://uscode.house.gov/view.xhtml?req=%28title%3A18+section%3A1030+edition%3Aprelim%29",
        "source_type": "legal-text",
        "summary": "The current U.S. Code page for 18 U.S.C. 1030 sets out the federal computer-intrusion offences commonly known as the Computer Fraud and Abuse Act. It is the principal U.S. charging reference for unauthorized access, exceeding authorized access, computer damage, credential abuse, and related fraud conduct.",
    },
    "uscode-1343": {
        "slug": "2026-04-29_uscode-house-gov_18-usc-1343-wire-fraud",
        "title": "18 U.S.C. 1343 - Fraud by wire, radio, or television",
        "publisher": "Office of the Law Revision Counsel, U.S. House of Representatives",
        "date": "2026-04-14",
        "url": "https://uscode.house.gov/view.xhtml?req=%28title%3A18+section%3A1343+edition%3Aprelim%29",
        "source_type": "legal-text",
        "summary": "The current U.S. Code page for 18 U.S.C. 1343 defines the federal wire-fraud offence for schemes using interstate or foreign wire, radio, or television communications. In cybercrime records it often appears as the charging bridge for online fraud, BEC, marketplace, credential, and platform-abuse cases.",
    },
    "uscode-1962": {
        "slug": "2026-04-29_uscode-house-gov_18-usc-1962-rico",
        "title": "18 U.S.C. 1962 - RICO prohibited activities",
        "publisher": "Office of the Law Revision Counsel, U.S. House of Representatives",
        "date": "2026-04-29",
        "url": "https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section1962",
        "source_type": "legal-text",
        "summary": "18 U.S.C. 1962 is the core RICO prohibited-activities provision, targeting enterprise conduct involving a pattern of racketeering activity or unlawful debt. In cybercrime cooperation records it is most relevant where prosecutors characterize a cyber-enabled fraud or marketplace group as an enterprise rather than as isolated transactions.",
    },
    "uscode-1956": {
        "slug": "2026-04-29_uscode-house-gov_18-usc-1956-money-laundering",
        "title": "18 U.S.C. 1956 - Laundering of monetary instruments",
        "publisher": "Office of the Law Revision Counsel, U.S. House of Representatives",
        "date": "2026-04-14",
        "url": "https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section1956",
        "source_type": "legal-text",
        "summary": "18 U.S.C. 1956 is a principal U.S. money-laundering statute for transactions involving proceeds of specified unlawful activity. It is frequently relevant to cybercrime cases involving cryptocurrency flows, mule networks, fraud proceeds, darknet markets, and asset tracing.",
    },
    "uscode-1957": {
        "slug": "2026-04-29_uscode-house-gov_18-usc-1957-monetary-transactions",
        "title": "18 U.S.C. 1957 - Monetary transactions in criminally derived property",
        "publisher": "Office of the Law Revision Counsel, U.S. House of Representatives",
        "date": "2025-06-21",
        "url": "https://uscode.house.gov/view.xhtml?req=%28title%3A18+section%3A1957+edition%3Aprelim%29",
        "source_type": "legal-text",
        "summary": "18 U.S.C. 1957 covers monetary transactions above the statutory threshold involving criminally derived property from specified unlawful activity. It complements section 1956 in cybercrime cases where proceeds move through banks, exchanges, or other financial channels.",
    },
    "uscode-841": {
        "slug": "2026-04-29_uscode-house-gov_21-usc-841-controlled-substances",
        "title": "21 U.S.C. 841 - Prohibited acts involving controlled substances",
        "publisher": "Office of the Law Revision Counsel, U.S. House of Representatives",
        "date": "2026-04-14",
        "url": "https://uscode.house.gov/view.xhtml?req=%28title%3A21+section%3A841+edition%3Aprelim%29",
        "source_type": "legal-text",
        "summary": "21 U.S.C. 841 is a core Controlled Substances Act offence provision covering manufacture, distribution, dispensing, and possession with intent to distribute controlled or counterfeit substances. It is relevant to darknet-market and online-pharmacy records where cyber infrastructure enables drug trafficking.",
    },
    "uscode-922": {
        "slug": "2026-04-29_uscode-house-gov_18-usc-922-firearms-unlawful-acts",
        "title": "18 U.S.C. 922 - Firearms unlawful acts",
        "publisher": "Office of the Law Revision Counsel, U.S. House of Representatives",
        "date": "2025-10-02",
        "url": "https://uscode.house.gov/view.xhtml?edition=prelim&f=treesort&num=0&req=%28title%3A18+section%3A922+edition%3Aprelim%29+OR+%28granuleid%3AUSC-prelim-title18-section922%29",
        "source_type": "legal-text",
        "summary": "18 U.S.C. 922 contains federal firearms unlawful-act provisions, including restrictions on interstate commerce, prohibited persons, stolen firearms, altered serial numbers, and machineguns. It appears in cybercrime-adjacent records where online conduct intersects with weapons, trafficking, threats, or proceeds.",
    },
    "uscode-924": {
        "slug": "2026-04-29_uscode-house-gov_18-usc-924-firearms-penalties",
        "title": "18 U.S.C. 924 - Firearms penalties",
        "publisher": "Office of the Law Revision Counsel, U.S. House of Representatives",
        "date": "2026-04-15",
        "url": "https://uscode.house.gov/view.xhtml?edition=prelim&f=treesort&jumpTo=true&num=0&req=title%3A18+section%3A924",
        "source_type": "legal-text",
        "summary": "18 U.S.C. 924 sets penalties and related provisions for federal firearms offences. In this corpus it functions as an ancillary legal-framework node for cyber-enabled cases where weapons charges accompany online fraud, drug, threat, or marketplace conduct.",
    },
    "cloud-act": {
        "slug": "2026-04-29_justice-gov_cloud-act-executive-agreements",
        "title": "Regarding CLOUD Act Executive Agreements",
        "publisher": "U.S. Department of Justice",
        "date": "2023-10-01",
        "url": "https://www.justice.gov/es/node/1397306",
        "source_type": "official-guidance",
        "summary": "DOJ guidance explains that CLOUD Act executive agreements remove legal restrictions so covered providers in one country can comply with qualifying lawful orders for electronic data issued by the other country. The Office of International Affairs serves as the U.S. Designated Authority under these agreements.",
    },
    "us-uk-cloud": {
        "slug": "2026-04-29_justice-gov_us-uk-data-access-agreement-enters-force",
        "title": "Landmark U.S.-UK Data Access Agreement Enters into Force",
        "publisher": "U.S. Department of Justice",
        "date": "2022-10-03",
        "url": "https://www.justice.gov/archives/opa/pr/landmark-us-uk-data-access-agreement-enters-force",
        "source_type": "press-release",
        "summary": "DOJ announced that the U.S.-UK Data Access Agreement entered into force on 3 October 2022. The agreement, authorized by the CLOUD Act, permits service providers in one country to respond to qualifying lawful orders for electronic data issued by the other country, improving timeliness compared with ordinary MLA channels.",
    },
    "us-australia-mlat": {
        "slug": "2026-04-29_congress-gov_us-australia-mlat-treaty-document-105-27",
        "title": "Treaty with Australia on Mutual Assistance in Criminal Matters",
        "publisher": "Congress.gov",
        "date": "1997-09-18",
        "url": "https://www.congress.gov/treaty-document/105th-congress/27/document-text",
        "source_type": "treaty-document",
        "summary": "Senate Treaty Document 105-27 transmits the U.S.-Australia Mutual Assistance in Criminal Matters treaty, signed in Washington on 30 April 1997. The document describes broad assistance including testimony, records, locating persons, transfers in custody, searches and seizures, restitution, asset immobilization, and forfeiture-related support.",
    },
    "us-germany-mlat": {
        "slug": "2026-04-29_congress-gov_us-germany-mlat-treaty-document-108-27",
        "title": "Mutual Legal Assistance Treaty with Germany",
        "publisher": "Congress.gov",
        "date": "2004-11-16",
        "url": "https://www.congress.gov/treaty-document/108th-congress/27/document-text",
        "source_type": "treaty-document",
        "summary": "Senate Treaty Document 108-27 transmits the U.S.-Germany Mutual Legal Assistance Treaty, signed on 14 October 2003. The document frames the treaty as a modern criminal-assistance channel for investigations and proceedings, including document production, testimony, evidence, and related assistance.",
    },
    "us-japan-mlat": {
        "slug": "2026-04-29_congress-gov_us-japan-mlat-treaty-document-108-12",
        "title": "Mutual Legal Assistance Treaty with Japan",
        "publisher": "Congress.gov",
        "date": "2003-11-24",
        "url": "https://www.congress.gov/treaty-document/108th-congress/12/document-text",
        "source_type": "treaty-document",
        "summary": "Senate Treaty Document 108-12 transmits the U.S.-Japan Mutual Legal Assistance Treaty, signed on 5 August 2003. It describes assistance such as testimony, statements, examination of persons or items, locating persons or items, government records, custody transfers, forfeiture support, and other assistance agreed by central authorities.",
    },
    "us-netherlands-mlat": {
        "slug": "2026-04-29_congress-gov_us-netherlands-mlat-eu-executive-report-110-13",
        "title": "Mutual Legal Assistance Agreement between the United States and the Netherlands",
        "publisher": "Congress.gov",
        "date": "2008-09-23",
        "url": "https://www.congress.gov/committee-report/110th-congress/executive-report/13/1",
        "source_type": "executive-report",
        "summary": "Senate Executive Report 110-13 covers U.S.-EU mutual legal assistance instruments and includes the U.S.-Netherlands agreement applying the 2003 U.S.-EU MLA framework to the 1981 U.S.-Netherlands criminal-assistance treaty. It supports treating the Netherlands page as an MLA framework node rather than a generic country link.",
    },
    "korea-us-mlat": {
        "slug": "2026-04-29_congress-gov_korea-us-mlat-treaty-document-104-1",
        "title": "Treaty with the Republic of Korea on Mutual Legal Assistance in Criminal Matters",
        "publisher": "Congress.gov",
        "date": "1995-01-12",
        "url": "https://www.congress.gov/treaty-document/104th-congress/1/document-text",
        "source_type": "treaty-document",
        "summary": "Senate Treaty Document 104-1 transmits the U.S.-Republic of Korea Mutual Legal Assistance Treaty, signed at Washington on 23 November 1993. The document lists assistance including testimony, documents and evidence, service, locating persons or items, custody transfers, searches and seizures, forfeiture assistance, and other lawful assistance.",
    },
    "korea-china-mlat": {
        "slug": "2026-04-29_nanet-go-kr_korea-china-mlat-foreign-law-index",
        "title": "Korea-China Mutual Judicial Assistance in Criminal Matters listing",
        "publisher": "National Assembly Library of Korea",
        "date": "2026-04-29",
        "url": "https://lnp.nanet.go.kr/foreignlaw/foreignIndex/foreignIndexView.do?cn=TLAW1201300205",
        "source_type": "treaty-index",
        "reliability": "medium",
        "summary": "The National Assembly Library foreign-law index lists the Treaty between the Republic of Korea and the People's Republic of China on Mutual Judicial Assistance in Criminal Matters. The listing verifies the treaty as a Korea-China criminal-assistance framework, while the page should later be supplemented with direct treaty text and entry-into-force details.",
    },
    "singapore-pdpa": {
        "slug": "2026-04-29_pdpc-gov-sg_personal-data-protection-act-overview",
        "title": "PDPA Overview",
        "publisher": "Personal Data Protection Commission Singapore",
        "date": "2023-10-01",
        "url": "https://www.pdpc.gov.sg/overview-of-pdpa/the-legislation/personal-data-protection-act.",
        "source_type": "official-guidance",
        "summary": "Singapore's Personal Data Protection Commission explains that the Personal Data Protection Act provides a baseline standard for protection of personal data in Singapore while allowing organizations to collect, use, and disclose data for legitimate and reasonable purposes. It is relevant to cybercrime cooperation where investigations interact with data-protection duties.",
    },
}


PAGES = {
    "computer-fraud-and-abuse-act": {
        "title": "Computer Fraud and Abuse Act",
        "framework_type": "national-legislation",
        "status": "in-force",
        "sources": ["uscode-1030"],
        "summary": "The Computer Fraud and Abuse Act page tracks 18 U.S.C. 1030 as the primary U.S. federal computer-intrusion statute used in cybercrime prosecutions.",
        "ic": "For international cooperation, the CFAA matters because many cross-border investigations require a U.S. charging anchor for unauthorized access, botnet activity, credential theft, malware deployment, or computer damage. The statute helps frame dual-criminality discussions when suspects, victims, infrastructure, or evidence are outside the United States.",
    },
    "wire-fraud-statute": {
        "title": "Wire Fraud Statute",
        "framework_type": "national-legislation",
        "status": "in-force",
        "sources": ["uscode-1343"],
        "summary": "The wire-fraud statute page tracks 18 U.S.C. 1343 as a recurring U.S. charging basis for cyber-enabled fraud schemes.",
        "ic": "Wire fraud is useful in the corpus because online fraud almost always uses interstate or foreign communications. The provision therefore appears in BEC, marketplace, identity-theft, credential, and platform-fraud records where foreign victims, suspects, payment flows, or service providers create an international-evidence problem.",
    },
    "rico": {
        "title": "RICO",
        "framework_type": "national-legislation",
        "status": "in-force",
        "sources": ["uscode-1962"],
        "summary": "The RICO page tracks 18 U.S.C. 1962 as a U.S. enterprise-liability framework for patterns of racketeering activity.",
        "ic": "RICO is relevant when a cybercrime group is treated as a durable enterprise rather than as a single incident. That framing can support broader conspiracy, forfeiture, and extradition narratives in cases involving distributed administrators, vendors, money mules, or infrastructure operators.",
    },
    "money-laundering-statutes": {
        "title": "Money Laundering Statutes",
        "framework_type": "national-legislation",
        "status": "in-force",
        "sources": ["uscode-1956", "uscode-1957"],
        "summary": "This page groups the principal U.S. money-laundering statutes used in cybercrime matters, especially 18 U.S.C. 1956 and 1957.",
        "ic": "Money-laundering charges are central to international cybercrime cooperation because proceeds often move through exchanges, banks, shell accounts, mule networks, and cross-border cryptocurrency services. These statutes support asset tracing, seizure, forfeiture, and mutual assistance requests tied to financial evidence.",
    },
    "controlled-substances-act": {
        "title": "Controlled Substances Act",
        "framework_type": "national-legislation",
        "status": "in-force",
        "sources": ["uscode-841"],
        "summary": "This page tracks the Controlled Substances Act offence provisions most often appearing in darknet-market and online drug-distribution records.",
        "ic": "The statute is not cyber-specific, but it becomes internationally relevant when drug distribution is enabled by darknet markets, encrypted communications, cryptocurrency payments, postal logistics, or cross-border suppliers. It often sits beside digital-evidence, marketplace, and money-laundering mechanisms.",
    },
    "firearms-offenses": {
        "title": "Firearms Offenses",
        "framework_type": "national-legislation",
        "status": "in-force",
        "sources": ["uscode-922", "uscode-924"],
        "summary": "This page groups U.S. federal firearms offence references that appear as ancillary charges in cybercrime-adjacent records.",
        "ic": "Firearms charges are not a cybercrime framework by themselves. They matter here when online conduct intersects with weapons trafficking, darknet markets, threats, drug distribution, or proceeds. Their presence affects extradition, detention, sentencing, and forfeiture context in some source-backed records.",
    },
    "us-uk-cloud-act-agreement": {
        "title": "US-UK CLOUD Act Agreement",
        "framework_type": "executive-agreement",
        "status": "in-force",
        "sources": ["cloud-act", "us-uk-cloud"],
        "summary": "The U.S.-UK CLOUD Act Agreement is the first operational bilateral data-access agreement under the U.S. CLOUD Act.",
        "ic": "Its main cooperation value is direct, faster access to qualifying electronic evidence held by covered providers, while preserving designated-authority review and rule-of-law safeguards. It complements, rather than eliminates, ordinary MLA channels for requests outside the agreement's scope.",
    },
    "us-australia-mlat": {
        "title": "US-Australia Mutual Assistance Treaty",
        "framework_type": "bilateral-treaty",
        "status": "in-force",
        "sources": ["us-australia-mlat"],
        "summary": "The U.S.-Australia MLAT page records the bilateral treaty channel for criminal mutual assistance between the two countries.",
        "ic": "For cybercrime cases, the treaty is relevant to evidence production, search and seizure, custody transfer, asset restraint, forfeiture support, and other formal assistance when police-to-police or provider channels are insufficient for admissible evidence.",
    },
    "us-germany-mlat": {
        "title": "US-Germany Mutual Legal Assistance Treaty",
        "framework_type": "bilateral-treaty",
        "status": "in-force",
        "sources": ["us-germany-mlat"],
        "summary": "The U.S.-Germany MLAT page records the bilateral criminal-assistance treaty transmitted to the U.S. Senate in 2004.",
        "ic": "Germany appears frequently in infrastructure, malware, marketplace, and ransomware matters. A dedicated MLAT page helps distinguish formal evidence channels from Europol, Eurojust, JIT, and police-coordination mechanisms used in the same operations.",
    },
    "us-japan-mlat": {
        "title": "US-Japan Mutual Legal Assistance Treaty",
        "framework_type": "bilateral-treaty",
        "status": "in-force",
        "sources": ["us-japan-mlat"],
        "summary": "The U.S.-Japan MLAT page records the bilateral criminal-assistance treaty signed in 2003 and considered by the U.S. Senate as Treaty Document 108-12.",
        "ic": "The treaty matters for cybercrime cooperation because Japan is a recurring partner in malware, marketplace, infostealer, and infrastructure investigations where evidence or provider data may need formal criminal-assistance handling.",
    },
    "us-netherlands-mlat": {
        "title": "US-Netherlands Mutual Legal Assistance Framework",
        "framework_type": "bilateral-treaty",
        "status": "in-force",
        "sources": ["us-netherlands-mlat"],
        "summary": "The U.S.-Netherlands MLAT page records the bilateral treaty framework as updated through the U.S.-EU mutual legal assistance instruments.",
        "ic": "The Netherlands is a frequent hosting, infrastructure, and law-enforcement partner in cybercrime takedowns. This page separates the formal MLA framework from Dutch police cooperation, Europol coordination, and private-provider evidence channels.",
    },
    "korea-us-mlat": {
        "title": "Korea-US Mutual Legal Assistance Treaty",
        "framework_type": "bilateral-treaty",
        "status": "in-force",
        "sources": ["korea-us-mlat"],
        "summary": "The Korea-US MLAT page records the bilateral criminal-assistance treaty signed at Washington on 23 November 1993.",
        "ic": "For Korean cybercrime cooperation, the treaty is the formal route for admissible criminal evidence and assistance when direct provider requests, police-to-police coordination, or informal intelligence exchange are not enough. It is especially relevant to U.S.-hosted platforms and service providers.",
    },
    "korea-china-mlat": {
        "title": "Korea-China Mutual Judicial Assistance Treaty",
        "framework_type": "bilateral-treaty",
        "status": "in-force",
        "sources": ["korea-china-mlat"],
        "summary": "The Korea-China MLAT page records the bilateral criminal-assistance framework between the Republic of Korea and the People's Republic of China.",
        "ic": "This framework is relevant because many Korea-facing cybercrime records involve Chinese territory, suspects, telecom infrastructure, scam compounds, or proceeds movement. The current page verifies the treaty's existence but flags that direct treaty text should be ingested for article-level analysis.",
    },
    "singapore-personal-data-protection-act": {
        "title": "Singapore Personal Data Protection Act",
        "framework_type": "national-legislation",
        "status": "in-force",
        "sources": ["singapore-pdpa"],
        "summary": "The Singapore PDPA page records the data-protection baseline that applies alongside cybercrime and electronic-evidence cooperation involving Singapore.",
        "ic": "The PDPA is not a criminal-assistance treaty, but it affects how personal data is collected, used, disclosed, and protected. It is relevant to cooperation records involving Singapore-based providers, financial data, cyber incident response, and public-private information exchange.",
    },
    "african-union-convention-cybersecurity": {
        "title": "African Union Convention on Cyber Security and Personal Data Protection",
        "framework_type": "regional-agreement",
        "status": "in-force",
        "sources": ["existing:2026-04-17_au-int_malabo-convention-status"],
        "summary": "This page is a compatibility record for the African Union Convention on Cyber Security and Personal Data Protection, commonly called the Malabo Convention.",
        "ic": "The Convention matters as Africa's regional framework linking cybersecurity, cybercrime, electronic transactions, and personal-data protection. In this wiki it should be read together with [[malabo-convention]], which carries the main treaty analysis.",
    },
    "first-additional-protocol-xenophobia": {
        "title": "First Additional Protocol to the Budapest Convention (CETS 189)",
        "framework_type": "protocol",
        "status": "in-force",
        "sources": ["existing:2003-01-28_coe-int_treaty-text-and-status-chart"],
        "summary": "CETS 189 is the First Additional Protocol to the Budapest Convention, extending the cybercrime treaty framework to racist and xenophobic acts committed through computer systems.",
        "ic": "The protocol is relevant to international cooperation because it demonstrates that Budapest-based harmonization can extend beyond core computer offences. Its uneven ratification also shows that substantive-law harmonization remains politically sensitive where expression offences and constitutional protections diverge.",
    },
    "malabo-convention": {
        "title": "African Union Malabo Convention",
        "framework_type": "regional-agreement",
        "status": "in-force",
        "sources": ["existing:2026-04-17_au-int_malabo-convention-status", "existing:2026-04-17_dataprotection-africa_au-s-malabo-convention-set-to-enter-force"],
        "summary": "The Malabo Convention is the African Union's regional convention on cyber security and personal data protection.",
        "ic": "It is relevant to the wiki because it provides a regional alternative and complement to Budapest-style harmonization, especially for African cybercrime capacity-building, data-protection, and national-law alignment. The page should remain conservative about current party counts unless synchronized with the AU treaty status page.",
    },
}


def source_slug(source_key: str) -> str:
    if source_key.startswith("existing:"):
        return source_key.split(":", 1)[1]
    return SOURCES[source_key]["slug"]


def references_table(source_keys: list[str]) -> str:
    lines = ["| # | Source | Publisher | Date | URL |", "|---|--------|-----------|------|-----|"]
    for idx, key in enumerate(source_keys, start=1):
        if key.startswith("existing:"):
            slug = source_slug(key)
            meta = frontmatter.load(SOURCES_DIR / f"{slug}.md").metadata
            title = str(meta.get("title") or slug)
            publisher = str(meta.get("publisher") or "")
            date = str(meta.get("publish_date") or "")
            url = str(meta.get("collection_url") or meta.get("source_url") or meta.get("url") or "")
        else:
            entry = SOURCES[key]
            slug = entry["slug"]
            title = entry["title"]
            publisher = entry["publisher"]
            date = entry["date"]
            url = entry["url"]
        lines.append(f"| {idx} | [[{slug}|{title.replace('|', '\\|')}]] | {publisher} | {date} | {url.replace('|', '%7C')} |")
    return "\n".join(lines)


def update_page(slug: str, data: dict[str, Any]) -> None:
    path = LEGAL_DIR / f"{slug}.md"
    post = frontmatter.load(path)
    meta = dict(post.metadata)
    refs = data["sources"]
    meta.update(
        {
            "type": "legal-framework",
            "title": data["title"],
            "status": data["status"],
            "framework_type": data["framework_type"],
            "updated": RUN_DATE,
            "source_count": len(refs),
            "sources": [f"[[{source_slug(key)}]]" for key in refs],
        }
    )
    meta.setdefault("created", "2026-04-26")
    meta.setdefault("scope", {"international_cooperation": True, "evidence": "varies", "substantive_law": "varies"})

    body = "\n".join(
        [
            "## Summary",
            "",
            data["summary"],
            "",
            "This record was expanded during the 2026-04-29 menu-data audit to replace link-preservation placeholder text with a source-backed, menu-ready explanation. It is intentionally concise: the page explains why the framework matters to the cybercrime international-cooperation corpus and points to the authoritative source records used for deeper verification.",
            "",
            "## International-Cooperation Relevance",
            "",
            data["ic"],
            "",
            "The practical question for this wiki is not merely whether the framework exists, but how it affects cross-border evidence, extradition or surrender, provider disclosure, asset restraint, seizure, forfeiture, or dual-criminality analysis. Pages that cite this framework should still be checked against their own operation or case sources before asserting that a particular request, warrant, or treaty channel was used.",
            "",
            "## Corpus Use",
            "",
            "Use this page as a normalized menu node for records that need a stable legal-framework link. Where an operation page cites the framework in metadata, the operation page remains the controlling record for facts such as countries involved, agencies, dates, and enforcement outcomes.",
            "",
            "## Data Quality Notes",
            "",
            "The references below are sufficient to remove the structural stub status. Article-by-article analysis, reservations, implementation status, and current party counts should be added only from direct official legal texts or depositary status pages.",
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
    created_sources = 0
    for key, entry in SOURCES.items():
        entry["pages_updated"] = [slug for slug, page in PAGES.items() if key in page["sources"]]
        ensure_source(entry)
        created_sources += 1

    updated_pages = 0
    for slug, data in PAGES.items():
        update_page(slug, data)
        updated_pages += 1
        print(f"updated legal-framework/{slug}.md")

    print(f"source pages written: {created_sources}")
    print(f"legal framework pages updated: {updated_pages}")


if __name__ == "__main__":
    main()
