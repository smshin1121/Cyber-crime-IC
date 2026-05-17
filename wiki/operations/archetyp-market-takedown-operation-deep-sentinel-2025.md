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

related_operations:
  - "[[operation-raptor]]"
  - "[[150-arrested-in-dark-web-drug-bust-as-police-seize-eur-26-million]]"
  - "[[operation-owners-of-empire-market-charged-in-chicago-with-operating-430-million-dark-web-marketplace]]"
  - "[[xss-is-cybercrime-forum-takedown-2025]]"
  - "[[us-colombia-versus-project-darknet-marketplace-schmitz-extradition-2026]]"
challenges_encountered:

lessons_learned:
  - "First wiki record of Operation Deep Sentinel as a discrete operation-name and the most fully-articulated Germany-Spain-Netherlands-Sweden-Romania-US 6-jurisdiction darknet-marketplace takedown architecture in the corpus."
  - "Demonstrates explicit Eurojust EIO + MLA coordination as a discrete IC mechanism class for darknet-marketplace takedowns — a structurally similar pattern to [[eurojust-100m-crypto-investment-fraud-takedown-2025|the 2025-09 €100M crypto-investment-fraud takedown]] (Eurojust EAW + EIO + freezing-order coordination), applied here to drug-marketplace infrastructure."
  - "Establishes the German lead-jurisdiction + Spanish arrest-jurisdiction + Dutch infrastructure-hosting-jurisdiction triplet as a routine pattern for EU-led darknet-marketplace takedowns: the German federal-prosecution architecture (ZIT Frankfurt am Main + BKA), the Spanish ability to apprehend German-national operators within Schengen, and the Dutch hosting infrastructure that has historically been a darknet-server preferred-location."
  - "US partner cooperation (HSI + IRS-CI + USDOJ) without action-day arrests demonstrates the analytical-support + intelligence-sharing pattern that complements EU JIT-anchored darknet enforcement, as recorded for [[operation-raptor|Operation Raptor]] and other prior dark-web takedowns."
source_count: 2
sources:
  - "[[2025-06-16_europol_europe-wide-takedown-archetyp-dark-web-drug-market]]"
  - "[[2025-06-16_bka-de_archetyp-market-abgeschaltet-betreiber-festgenommen]]"
summary: "Operation Deep Sentinel was a 6-jurisdiction darknet-marketplace takedown executed during 11-13 June 2025, led by German authorities (Generalstaatsanwaltschaft Frankfurt am Main — ZIT + BKA), with 5-EU-state plus US partnership (Germany, Netherlands, Romania, Spain, Sweden, US-HSI/IRS-CI/USDOJ) coordinated by Europol EC3 and Eurojust (mutual legal assistance + European Investigation Order coordination during the action days). The operation took offline the longest-running dark-web drug marketplace, Archetyp Market, which had operated for 5+ years with 600,000+ users, EUR 250 million+ in transaction volume, and 17,000+ listings including fentanyl and other synthetic opioids. The 30-year-old German-national administrator was arrested in Barcelona, Spain; the Netherlands-hosted infrastructure was taken offline; one moderator and six highest vendors were targeted in Germany and Sweden; EUR 7.8 million in assets were seized; approximately 300 officers were deployed across the EU jurisdictions."
created: 2026-05-09
updated: 2026-05-17
---
## Summary

Between **11 and 13 June 2025**, German-led law enforcement, with the support of authorities in the **Netherlands, Romania, Spain, Sweden, the United States, Europol, and Eurojust**, executed **Operation Deep Sentinel** — a 6-jurisdiction darknet-marketplace takedown that **shut down Archetyp Market**, the longest-running dark-web drug marketplace. The platform's infrastructure (hosted in the Netherlands) was taken offline; its **30-year-old German-national administrator** was arrested in **Barcelona, Spain**; one moderator and six of the marketplace's highest vendors were targeted in **Germany and Sweden**; **EUR 7.8 million** in assets were seized; and approximately **300 officers** were deployed across the 5 EU jurisdictions.

## Background

### Modus operandi

Archetyp Market operated as a **Tor-hidden-service** (.onion) escrow-style darknet drug marketplace following the classic Silk Road/AlphaBay/Dream-Market architecture. Buyers and vendors registered pseudonymous accounts; vendors paid the marketplace a listing/commission fee and used the platform's built-in escrow (cryptocurrency held by the marketplace until buyer confirms receipt). Listings spanned **cocaine, MDMA, amphetamines, and synthetic opioids — notably fentanyl** — distinguishing Archetyp from competitors that voluntarily prohibited high-potency synthetic-opioid listings. Order fulfilment was executed by physical-mail dead-drops from vendors to buyers. Settlement was **Monero (XMR)** by default for buyer privacy (the cited BKA release confirms Monero as the operational settlement currency), with the platform's admin and vendor commissions captured in the same crypto layer. The admin alias **"ASNT"** (named in the BKA release) is the only operator handle publicly disclosed.

### Victim profile and impact

Unlike fraud marketplaces, the immediate "victim" framing on Archetyp is the **public-health and overdose harm** generated by enabling at-scale, low-friction sale of fentanyl and other synthetic opioids globally. The cited Europol release does not enumerate overdose-death attribution figures or victim casualty counts; the harm vector is implicit from the listing-mix and the **600,000+ user worldwide** scale. A secondary victim class is the broader **drug-control regime**: the marketplace materially undercut national drug-enforcement controls across the EU, US, and beyond. The 17,000+ listings represent the supply-side inventory available to those 600,000 users.

### Financial flow

Across the platform's 5+ years of operation, **EUR 250 million+** in total transaction volume passed through Archetyp's escrow. Crypto-economic structure: (1) buyer funds Monero into platform-held escrow address, (2) vendor ships product, (3) buyer releases escrow, (4) platform retains commission, (5) vendor withdraws net to vendor-controlled wallet, (6) admin extracts platform commission as operator income. The 2025-06 action-day seizure totalled **EUR 7.8 million** in assets — a small fraction of total flow, indicating that the bulk of historical flow was extracted, off-ramped, or laundered before action day. The release does not enumerate the breakdown between Monero, Bitcoin, fiat, or non-crypto assets within the EUR 7.8M figure.

### Criminal organization structure

The platform was operated by a single **administrator** ("ASNT", 30-year-old German national, arrested in Barcelona), supported by **at least one moderator** and a vendor cohort whose **six highest-revenue vendors** were targeted in Germany and Sweden. The BKA release confirms **7 arrests in Sweden** (corresponding to the moderator + 6 highest vendors). The vendor cohort itself spanned an unenumerated number of additional smaller-volume sellers (Archetyp's 17,000+ listings imply hundreds of active vendors at minimum). The German criminal charge — **§§ 29a, 30a Betäubungsmittelgesetz** (gang-mode unauthorized trafficking of narcotics in non-minor quantity) — treats the admin–moderator–vendor structure as a *Bande* (gang) for German narcotics-law purposes. The cited Europol release places Archetyp Market alongside Dream Market and Silk Road in scale and reputation.

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

## German-Side Detail (BKA + ZIT Frankfurt am Main)

The BKA + Generalstaatsanwaltschaft Frankfurt am Main (ZIT) joint release on the same day (2025-06-16) confirms and extends the operational picture:

- **Administrator's alias confirmed by tier-1 source**: "ASNT" (the Europol release does not name the alias; BKA names it from the German side).
- **Charges (German criminal code)**: bandenmaessiges unerlaubtes Handeltreiben mit Betaeubungsmitteln in nicht geringer Menge unter Paragraphen 29a, 30a Betaeubungsmittelgesetz (BtMG) — gang-mode unauthorized trafficking of narcotics in non-minor quantity.
- **Search-and-seizure locations beyond Europol enumeration**: admin residence in Barcelona + one object each in Hannover, Landkreis Minden-Luebbecke, and Bucharest; plus a further 20 objects in Germany (Nordrhein-Westfalen × 2, Niedersachsen × 2, Hessen × 1, Baden-Wuerttemberg × 1) and additional searches in Sweden.
- **Sweden arrest count**: BKA explicitly states "Sieben weitere Personen wurden in Schweden festgenommen" — 7 arrests in Sweden (where the Europol release described 1 moderator + 6 vendors "targeted").
- **Additional seizures** (other suspects beyond admin): 47 smartphones, 45 computers/notebooks, narcotics, and further assets — in addition to the admin's 8 mobiles + 4 computers + 34 data carriers.
- **9 German police forces enumerated**: Polizeipraesidium Bielefeld, Polizeipraesidium Bonn, Kriminalkommissariat Bruchsal, Polizeidirektion Darmstadt-Dieburg, Polizeidirektion Hannover, Kreispolizeibehoerde Minden-Luebbecke, Zentrale Kriminalinspektion Oldenburg, Polizeidirektion Osnabrueck, Polizeipraesidium Recklinghausen.
- **International partners enumerated with local names**: Niederlande (Politie), Rumaenien (Inspectoratul General al Politiei Romane / IGPR), Schweden (Polisen), Spanien (Policia Nacional), USA (USDOJ + HSI + IRS-CI).
- **Cooperation framing (verbatim)**: "Den durch die ZIT und das BKA koordinierten Massnahmen im Zuge der internationalen Operation 'Deep Sentinel' gegen den 'Archetyp Market' gingen langwierige und aufwaendige verdeckte Ermittlungen in den beteiligten Staaten voraus, welche von Europol und Eurojust unterstuetzt wurden."

## Contradictions & Open Questions

- BKA states 7 arrests in Sweden; Europol release framed this as "1 moderator + 6 highest vendors targeted" — *likely* consistent (7 total), but the Europol "targeted" language did not specify arrest vs other measure. BKA's "festgenommen" resolves this as arrest.
- Specific Romania-side operational detail: BKA names one search object in Bucharest but does not enumerate Romania-side arrests.
- Cryptocurrency-vs-other-asset breakdown within the EUR 7.8M seizure is not enumerated in either release.
- Indictment counts in any jurisdiction are not enumerated in the cited releases (pre-indictment action-day events).
- The 8th arrest figure (some secondary reporting cites "8 suspects total") is consistent with 1 admin (Spain) + 7 (Sweden) = 8 across the action days; this is not framed as a single total in either tier-1 release.
- **L26 gap — Victim impact quantification:** Neither cited tier-1 release enumerates overdose deaths, hospital admissions, or other public-health casualty attribution for fentanyl/synthetic-opioid product sold via Archetyp Market; the victim impact is implicit from the listing-mix and 600,000-user scale.
- **L26 gap — Financial flow forensics:** The EUR 7.8M action-day seizure breakdown (Monero vs Bitcoin vs fiat vs other assets), the off-ramp jurisdictions, and the laundering venues for historical flow (EUR 250M+) are not enumerated in the cited releases.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-06-16_europol_europe-wide-takedown-archetyp-dark-web-drug-market\|Europe-wide takedown hits longest-standing dark web drug market]] | Europol | 2025-06-16 | https://www.europol.europa.eu/media-press/newsroom/news/europe-wide-takedown-hits-longest-standing-dark-web-drug-market |
| [2] | [[2025-06-16_bka-de_archetyp-market-abgeschaltet-betreiber-festgenommen\|Darknet-Handelsplattform "Archetyp Market" abgeschaltet – Betreiber identifiziert und festgenommen]] | Bundeskriminalamt (BKA) / Generalstaatsanwaltschaft Frankfurt am Main — ZIT | 2025-06-16 | https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2025/Presse2025/250616_Archetyp_abgeschaltet.html |
