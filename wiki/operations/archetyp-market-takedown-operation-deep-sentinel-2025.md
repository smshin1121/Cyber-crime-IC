---
type: operation
title: "Archetyp Market Takedown (Operation Deep Sentinel, 2025-06-11 to 2025-06-13)"
title_ko: "Archetyp Market 단속 (Operation Deep Sentinel, 2025-06-11~2025-06-13)"
aliases:
  - "Operation Deep Sentinel"
  - "Archetyp Market takedown"
  - "Archetyp dark-web drug marketplace takedown 2025"
case_id: CYB-2025-210
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - infrastructure-seizure
  - asset-freeze
outcome: success
timeframe:
  announced: 2025-06-16
  start: 2025-06-11
  end: 2025-06-13
  ongoing: false
crime_type: "[[dark-web-ic]]"
crime_types:
  - "[[dark-web-ic]]"
  - "[[drug-trafficking]]"
  - "[[money-laundering-ic]]"
target_entity: "Archetyp Market — longest-running dark-web drug marketplace, operating 5+ years; 600,000+ users worldwide; EUR 250 million+ total transaction volume; 17,000+ listings including cocaine, MDMA, amphetamines, and synthetic opioids (notably fentanyl)"
lead_agency: "[[germany-bka]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[romania]]"
  - "[[spain]]"
  - "[[sweden]]"
  - "[[united-states]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[dutch-police]]"
  - "[[romanian-police]]"
  - "[[spain-national-police]]"
  - "[[sweden-police]]"
  - "[[us-doj]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
organizations:
  - "[[germany-bka]]"
  - "[[dutch-police]]"
  - "[[romanian-police]]"
  - "[[spain-national-police]]"
  - "[[sweden-police]]"
  - "[[us-doj]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
mechanisms_used:
  - "[[european-investigation-order]]"
  - "[[mlat-process]]"
  - "[[eurojust-coordination-meeting]]"
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
legal_basis:
  - "German lead investigation under the Prosecutor General's Office Frankfurt am Main — Cyber Crime Centre (Generalstaatsanwaltschaft Frankfurt am Main — ZIT) and the Federal Criminal Police Office (Bundeskriminalamt / BKA)"
  - "Eurojust coordination of mutual legal assistance and European Investigation Orders during action days and preliminary investigations"
  - "Per-country domestic search-and-arrest warrants executed under the lead authority's domestic procedural code"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Administrator (30-year-old German national) arrested in Barcelona, Spain"
    - "Platform infrastructure (hosted in the Netherlands) taken offline"
    - "1 moderator + 6 highest vendors targeted in Germany and Sweden (specific arrest counts not enumerated)"
    - "EUR 7,800,000 in assets seized"
    - "~300 officers deployed across the 5 EU jurisdictions"
    - "Underlying disrupted marketplace: 600,000+ users worldwide; EUR 250 million+ transaction volume; 17,000+ listings; 5+ years of operation"
    - "Drugs categorised: cocaine, MDMA, amphetamines, synthetic opioids (notably fentanyl)"
    - "Operation public-information site: www.operation-deepsentinel.com"
edges:
  - source_actor: germany-bka
    target_actor: spain-national-police
    cooperation_type: arrest_assistance
    legal_basis: european-investigation-order
    direction: directed
  - source_actor: germany-bka
    target_actor: dutch-police
    cooperation_type: infrastructure_seizure_assistance
    legal_basis: european-investigation-order
    direction: directed
  - source_actor: germany-bka
    target_actor: sweden-police
    cooperation_type: vendor_targeting_assistance
    legal_basis: european-investigation-order
    direction: directed
  - source_actor: europol-ec3
    target_actor: germany-bka
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: eurojust
    target_actor: germany-bka
    cooperation_type: judicial_coordination
    legal_basis: european-investigation-order
    direction: undirected
  - source_actor: us-doj
    target_actor: germany-bka
    cooperation_type: info_sharing
    legal_basis: bilateral
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "specific arrest counts beyond the administrator (1 moderator + 6 vendors targeted; the cited release does not enumerate how many of these were arrested vs subjected to other measures)"
  - "specific Romania-side action detail"
  - "specific cryptocurrency totals seized vs other assets within the EUR 7.8M seizure"
  - "indictment counts in any jurisdiction (the cited release describes pre-indictment action-day events)"
related_cases:
  []
related_operations:
  - "[[operation-raptor]]"
  - "[[150-arrested-in-dark-web-drug-bust-as-police-seize-eur-26-million]]"
  - "[[operation-owners-of-empire-market-charged-in-chicago-with-operating-430-million-dark-web-marketplace]]"
  - "[[xss-is-cybercrime-forum-takedown-2025]]"
challenges_encountered:
  []
lessons_learned:
  - "First wiki record of Operation Deep Sentinel as a discrete operation-name and the most fully-articulated Germany-Spain-Netherlands-Sweden-Romania-US 6-jurisdiction darknet-marketplace takedown architecture in the corpus."
  - "Demonstrates explicit Eurojust EIO + MLA coordination as a discrete IC mechanism class for darknet-marketplace takedowns — a structurally similar pattern to [[eurojust-100m-crypto-investment-fraud-takedown-2025|the 2025-09 €100M crypto-investment-fraud takedown]] (Eurojust EAW + EIO + freezing-order coordination), applied here to drug-marketplace infrastructure."
  - "Establishes the German lead-jurisdiction + Spanish arrest-jurisdiction + Dutch infrastructure-hosting-jurisdiction triplet as a routine pattern for EU-led darknet-marketplace takedowns: the German federal-prosecution architecture (ZIT Frankfurt am Main + BKA), the Spanish ability to apprehend German-national operators within Schengen, and the Dutch hosting infrastructure that has historically been a darknet-server preferred-location."
  - "US partner cooperation (HSI + IRS-CI + USDOJ) without action-day arrests demonstrates the analytical-support + intelligence-sharing pattern that complements EU JIT-anchored darknet enforcement, as recorded for [[operation-raptor|Operation Raptor]] and other prior dark-web takedowns."
source_count: 1
sources:
  - "[[2025-06-16_europol_europe-wide-takedown-archetyp-dark-web-drug-market]]"
summary: "Operation Deep Sentinel was a 6-jurisdiction darknet-marketplace takedown executed during 11-13 June 2025, led by German authorities (Generalstaatsanwaltschaft Frankfurt am Main — ZIT + BKA), with 5-EU-state plus US partnership (Germany, Netherlands, Romania, Spain, Sweden, US-HSI/IRS-CI/USDOJ) coordinated by Europol EC3 and Eurojust (mutual legal assistance + European Investigation Order coordination during the action days). The operation took offline the longest-running dark-web drug marketplace, Archetyp Market, which had operated for 5+ years with 600,000+ users, EUR 250 million+ in transaction volume, and 17,000+ listings including fentanyl and other synthetic opioids. The 30-year-old German-national administrator was arrested in Barcelona, Spain; the Netherlands-hosted infrastructure was taken offline; one moderator and six highest vendors were targeted in Germany and Sweden; EUR 7.8 million in assets were seized; approximately 300 officers were deployed across the EU jurisdictions."
created: 2026-05-09
updated: 2026-05-09
---
## Summary

Between **11 and 13 June 2025**, German-led law enforcement, with the support of authorities in the **Netherlands, Romania, Spain, Sweden, the United States, Europol, and Eurojust**, executed **Operation Deep Sentinel** — a 6-jurisdiction darknet-marketplace takedown that **shut down Archetyp Market**, the longest-running dark-web drug marketplace. The platform's infrastructure (hosted in the Netherlands) was taken offline; its **30-year-old German-national administrator** was arrested in **Barcelona, Spain**; one moderator and six of the marketplace's highest vendors were targeted in **Germany and Sweden**; **EUR 7.8 million** in assets were seized; and approximately **300 officers** were deployed across the 5 EU jurisdictions.

## Background

Archetyp Market operated as a drug marketplace for over **five years**, amassing **more than 600,000 users worldwide** with a total transaction volume of **at least EUR 250 million**. With **over 17,000 listings**, it was one of the few darknet markets that allowed the sale of **fentanyl and other highly potent synthetic opioids**. The cited Europol release places Archetyp Market alongside Dream Market and Silk Road in scale and reputation. The drug categories explicitly recorded in the release include cocaine, MDMA, amphetamines, and synthetic opioids.

## Participating Parties

| Country | Lead Authority |
|---|---|
| Germany | Prosecutor General's Office Frankfurt am Main — Cyber Crime Centre (Generalstaatsanwaltschaft Frankfurt am Main — ZIT); [[germany-bka\|Federal Criminal Police Office (Bundeskriminalamt / BKA)]] |
| Netherlands | [[dutch-police\|National Police of the Netherlands (Politie)]] |
| Romania | [[romanian-police\|Romanian Police (Poliția Română)]] |
| Spain | [[spain-national-police\|National Police (Policía Nacional)]] |
| Sweden | [[sweden-police\|Swedish Police Authority (Polismyndigheten)]] |
| United States | Homeland Security Investigations (HSI), IRS Criminal Investigation (IRS-CI), [[us-doj\|US Department of Justice (USDOJ)]] |
| Coordinating | [[europol-ec3\|Europol European Cybercrime Centre (EC3)]] (coordination meetings); [[eurojust\|Eurojust]] (MLA + European Investigation Orders during action days and preliminary investigations) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| (multi-year preliminary phase) | German-led investigation: technical-architecture mapping, financial-flow tracing, digital forensic analysis | Europol 2025-06-16 |
| (date not enumerated) | Eurojust coordination meetings; multiple Europol EC3 meetings | Europol 2025-06-16 |
| 2025-06-11 to 2025-06-13 | Coordinated action days across Germany, Netherlands, Romania, Spain, Sweden; ~300 officers deployed; admin arrested in Barcelona; NL infrastructure taken offline; 1 moderator + 6 highest vendors targeted; EUR 7.8M seized | Europol 2025-06-16 |
| 2025-06-16 | Public announcement; seizure banner published on the now-defunct marketplace | Europol 2025-06-16 |

## Results and Impact

- **Administrator arrested** (30-year-old German national, Barcelona, Spain).
- **Platform infrastructure taken offline** (NL-hosted).
- **1 moderator + 6 highest vendors targeted** in Germany and Sweden.
- **EUR 7,800,000 in assets seized.**
- **~300 officers deployed** across 5 EU jurisdictions.
- **Disrupted marketplace**: 600,000+ users worldwide; EUR 250M+ transaction volume; 17,000+ listings.

## Cooperation Mechanisms Used

The cited release describes three discrete IC mechanism classes for this operation:

1. **Eurojust mutual-legal-assistance + European Investigation Order coordination** during action days and preliminary investigations — the foundational judicial-cooperation instrument for the multi-jurisdiction action.
2. **Europol EC3 coordination meetings** for cross-jurisdiction information exchange and analytical support.
3. **US partner contribution without action-day arrests** — HSI + IRS-CI + USDOJ provided analytical and intelligence support to the EU-led action without an action-day US arrest, demonstrating the EU-JIT-anchored + US-analytical-support pattern.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited Europol release among the participating jurisdictions or the underlying user/vendor cohort. The case is recorded in the wiki for the 6-jurisdiction darknet-marketplace takedown architecture and the Eurojust EIO + MLA mechanism class. Korean exposure to Archetyp Market is *likely* present given the global 600,000+ user scale but is not enumerated in this source.

## Contradictions & Open Questions

- The cited release does not enumerate the specific arrest counts beyond the administrator (1 moderator + 6 vendors targeted; how many were arrested vs subjected to other measures is not specified).
- Specific Romania-side operational detail is not enumerated.
- Cryptocurrency-vs-other-asset breakdown within the EUR 7.8M seizure is not enumerated.
- Indictment counts in any jurisdiction are not enumerated in the cited release.
- The specific alias of the German-national administrator (third-party reporting cites "ASNT" but this is not in the primary Europol release).

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-06-16_europol_europe-wide-takedown-archetyp-dark-web-drug-market\|Europe-wide takedown hits longest-standing dark web drug market]] | Europol | 2025-06-16 | https://www.europol.europa.eu/media-press/newsroom/news/europe-wide-takedown-hits-longest-standing-dark-web-drug-market |
