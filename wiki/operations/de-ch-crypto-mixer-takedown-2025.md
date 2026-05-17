---
type: operation
title: "Cryptomixer Takedown / Operation Olympia (DE-CH, 24-28 November 2025)"
title_ko: "Cryptomixer 단속 / Operation Olympia (독일-스위스, 2025-11-24~2025-11-28)"
aliases:
  - "Operation Olympia"
  - "Eurojust DE-CH Crypto Mixer Takedown 2025"
  - "Germany Switzerland Cryptocurrency Mixer Action"
  - "Cryptomixer takedown"
  - "cryptomixer.io takedown"
case_id: CYB-2025-013
period: 3
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - seizure
  - takedown
  - asset_freeze
outcome: partial
timeframe:
  announced: 2025-11-26
  start: 2025-11-24
  end: 2025-11-28
  ongoing: false
crime_type: "[[money-laundering-ic]]"
target_entity: "Cryptomixer (cryptomixer.io) — hybrid clear-web + dark-web cryptocurrency mixing service active since 2016 that processed over EUR 1.3 billion in Bitcoin laundering for ransomware groups, underground economy forums, dark web markets, drug traffickers, weapons traffickers, and payment-card fraudsters"
lead_agency: "[[eurojust]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[germany]]"
  - "[[switzerland]]"
participating_agencies:
  - "[[eurojust]]"
  - "[[europol-ec3]]"
  - "[[germany-bka]]"
legal_basis:
  - "[[budapest-convention]]"
  - "[[mutual-legal-assistance]]"
mechanisms_used:
  - "[[mutual-legal-assistance|MLAT Process]]"
  - "[[europol-jit|Joint Investigation Team]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 3
  domains_seized: 1
  cryptocurrency_seized: "EUR 25,000,000+ in Bitcoin"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "3 servers seized in Switzerland"
    - "cryptomixer.io clearnet domain seized"
    - "12+ TB of operational data confiscated"
    - "Cryptomixer service active since 2016"
    - "Lifetime laundering volume: EUR 1.3 billion+ in Bitcoin mixed through the service"
    - "Splash banner placed on cryptomixer.io after takedown"
edges:
  - source_actor: Germany
    target_actor: Switzerland
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: undirected
  - source_actor: Eurojust
    target_actor: Germany
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: directed
  - source_actor: Eurojust
    target_actor: Switzerland
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: directed
  - source_actor: Europol
    target_actor: Germany
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: directed
credibility_index: 3.5
source_tier: 1
missing_fields:
  - "specific operator names (no arrests enumerated; Cryptomixer operator identity not in primary releases)"
  - "indictments (none enumerated post-takedown as of cited Europol release)"
  - "specific legal basis for Switzerland-Germany cooperation (Eurojust-Switzerland bilateral agreement assumed but not confirmed in the cited releases)"
related_operations:
  - "[[cryptex-pm2btc-sanctions]]"
  - "[[2bagoldmule-qqaazz]]"
  - "[[operation-final-exchange-bka-russian-crypto-exchanges-2024]]"
challenges_encountered:
  - "[[data-sovereignty]]"
lessons_learned:
  - "Bilateral DE-CH cooperation under Eurojust coordination can deliver significant cryptocurrency seizures even where one participant (Switzerland) is outside the EU"
source_count: 6
sources:
  - "[[2025-12-01-eurojust-de-ch-crypto-mixer-takedown]]"
  - "[[2025-12-01_coindesk-com_cryptomixer-takedown]]"
  - "[[2025-12-01_amlintelligence-com_cryptomixer-used-to-mix-13bn-in-bitcoin]]"
  - "[[2025-12-02_techradar-com_huge-cryptomixer-takedown-sees-feds-seize-over-usd30milion]]"
  - "[[2025-12-01_heise-de_illegaler-cryptomixer-von-strafverfolgern-zerschlagen]]"
  - "[[2025-11-26_europol_cryptomixer-operation-olympia-takedown]]"
created: 2026-04-14
updated: 2026-05-17
operation_role: umbrella
parent_operation: ""
summary: "Operation Olympia (24-28 November 2025) was the joint German-Swiss takedown of Cryptomixer (cryptomixer.io) — a hybrid clear-web + dark-web cryptocurrency mixing service active since 2016 that had laundered over EUR 1.3 billion in Bitcoin for ransomware groups, dark web markets, drug traffickers, weapons traffickers, and payment-card fraudsters. Lead authorities: German BKA + Frankfurt am Main Prosecutor General's Office Cyber Crime Centre (ZIT); Zurich City Police (Stadtpolizei Zürich); Zurich Cantonal Police (Kantonspolizei Zürich); Public Prosecutor's Office Zurich (Staatsanwaltschaft Zürich). Europol coordination via the Joint Cybercrime Action Taskforce (J-CAT) at Europol HQ The Hague + on-the-spot cybercrime expert support and forensic assistance during the action days. Eurojust judicial coordination. Action-day seizures: 3 servers in Switzerland, the cryptomixer.io clearnet domain, 12+ TB of operational data, and EUR 25 million+ worth of Bitcoin. Splash banner placed on cryptomixer.io after takedown. Predecessor in same Europol-supported mixer-takedown chronology: Chipmixer (March 2023)."
jurisdictions:
  - "[[germany]]"
  - "[[switzerland]]"
organizations:
  - "[[eurojust]]"
  - "[[europol-ec3]]"
crime_types:
  - "[[money-laundering-ic]]"
  - "[[bec-ic]]"
  - "[[ransomware-ic]]"
  - "[[dark-web-ic]]"
---
## Summary

On **1 December 2025**, [[eurojust|Eurojust]] announced that authorities from [[germany|Germany]] and [[switzerland|Switzerland]], together with Eurojust and [[europol-ec3|Europol]], had taken down a cryptocurrency mixing service suspected of being used by criminals to launder the proceeds of drug trafficking, weapons trafficking, online fraud, and other cybercrimes. During an action week, **more than EUR 25 million in cryptocurrency was seized and three servers were taken down**.

The Eurojust release does not name the service, the action lead in either country, or the number of arrests. The operation fits the continuing EU-Switzerland cryptocurrency-laundering enforcement pattern, but the available source set does not link it to a publicly named campaign.

> [!note] Unnamed operation
> The mixing service and the operation itself are unnamed in the Eurojust press release. The wiki slug `de-ch-crypto-mixer-takedown-2025` is descriptive only. If a name surfaces in follow-up reporting, this page should be renamed.

## Background

### Modus operandi (the crime)

**Cryptomixer (cryptomixer.io)** was a hybrid clear-web + dark-web Bitcoin mixing ("tumbling") service that operated **continuously from 2016 through November 2025** — making it one of the longest-running mixers ever taken down by EU law enforcement. The service pooled inbound BTC deposits from many separate criminal customers, severed the on-chain trace by mixing through a large pool of operator-controlled wallets, then redistributed clean-output BTC to destination addresses selected by the customer. Cryptomixer accepted customer payments **without KYC/AML controls**, charged a percentage fee per mix (the operator-retained margin is the criminal monetisation), and offered customer-configurable time-delay and output-split options to defeat blockchain-analytics clustering. The service was reachable both via clear-web (`cryptomixer.io`) and a parallel Tor hidden-service address — a hybrid posture intended to maximise inbound customer reach while preserving deniability for the operators.

### Victim profile and impact

The mixer itself does not have first-order direct victims — its harm is **downstream-enabling**: it functions as the laundering choke-point that converts criminal-source BTC into spendable BTC for the predicate offenders. Per the Europol release, customer-criminals using Cryptomixer ran predicate offences across:

- **Ransomware payments** (named explicitly — Cryptomixer was identified as a routine laundering venue for ransomware operators receiving victim-paid BTC ransoms)
- **Underground economy forums** (carding markets, credential markets, stolen-data resale)
- **Dark web marketplaces** (drug trafficking, weapons trafficking)
- **Online fraud / BEC** (business-email-compromise proceeds, investment fraud, romance fraud)
- **Payment-card fraud** (post-theft cashout cycles)

The second-order victim pool is therefore the global ransomware-victim and fraud-victim populations whose paid-out BTC passed through Cryptomixer between 2016 and 2025 — *highly likely* (≥80%) numbering in the tens of thousands across jurisdictions, though no per-victim enumeration is provided in the cited Europol release.

### Financial flow

Lifetime laundering volume through Cryptomixer: **over EUR 1.3 billion in Bitcoin** (Europol-attributed figure as of the November 2025 takedown). The 12+ TB of operational data seized from the three Swiss servers contains the transaction graph linking inbound deposits → mixed-pool → outbound clean-side addresses, and *highly likely* (≥80%) will be the primary evidence base for ongoing follow-on investigations against Cryptomixer customers downstream. **EUR 25 million-equivalent in Bitcoin** was directly seized on the action day. Per AML Intelligence reporting, the on-chain volume figure (~USD 1.5 billion) places Cryptomixer in the same volume-tier as previously dismantled mixers such as **ChipMixer** (March 2023, EUR 90 million seized at takedown) and **Tornado Cash** (sanctioned 2022), though the per-incident seizure ratio (EUR 25M / EUR 1.3B = ~1.9%) reflects the structural difficulty of recovering already-laundered cryptocurrency.

### Criminal organisation structure

The cited Eurojust and Europol releases **do not enumerate Cryptomixer's operator identities, organisational headcount, or hierarchical structure**. The infrastructure footprint — 3 servers in Switzerland, 1 clearnet domain, 12+ TB operational data — is consistent with a small-to-mid-size technical operator team (likely <10 core operators) rather than a large hierarchical OCG. The Swiss server-hosting plus German-prosecutorial nexus suggests the operator(s) may have had ties to either jurisdiction, though no arrests were announced on the action day. **No indictments enumerated** post-takedown as of the cited releases — see gap notes in Contradictions.

### Operational geography (LE side)

Switzerland's role as a global financial hub and the location of the so-called "Crypto Valley" in Zug make it a high-relevance host or operating jurisdiction for cryptocurrency-asset service providers. Germany's prosecutorial cybercrime infrastructure — particularly the [[germany-frankfurt-prosecutor|ZIT Frankfurt]] — is a major continental European centre for cryptocurrency takedowns.

## Participating Parties

| Country | Role |
|---------|------|
| [[germany]] | Co-lead enforcement; the public source does not identify whether ZIT Frankfurt, BKA, or another German authority led the national component |
| [[switzerland]] | Co-lead enforcement; the public source does not identify whether fedpol or another Swiss authority led the national component |

| Coordinating Body | Role |
|-------------------|------|
| [[eurojust]] | Judicial coordination, including DE-CH bilateral judicial cooperation |
| [[europol-ec3]] | Operational and analytical support |

> [!note] Source gap
> The Eurojust release does not specify which German or Swiss agencies led their respective national components. The public record supports Swiss involvement in asset freezing and server seizure, while finer agency attribution remains unavailable from the cited release.

## Legal Framework

- **[[budapest-convention|Budapest Convention]]**: Both Germany (party 2009) and Switzerland (party 2011) are parties, providing the multilateral framework for cross-border preservation, search and seizure, and MLA.
- **National money laundering statutes**: German Strafgesetzbuch (StGB) §§ 261; Swiss Criminal Code (StGB/CP) art. 305bis.

## Operational Timeline

| Date | Event |
|------|-------|
| (Pre-2025) | Investigation initiated; specific start date undisclosed |
| Action week 2025 | Coordinated DE-CH seizure of 3 servers and EUR 25M+ in cryptocurrency |
| 2025-12-01 | Eurojust announces the takedown via press release |

## Results and Impact

| Metric | Value |
|--------|-------|
| Cryptocurrency seized | **EUR 25 million** (more than) |
| Servers seized | **3** |
| Arrests | undisclosed |
| Indictments | undisclosed |

The seizure is one of the larger disclosed EU-Switzerland cryptocurrency seizures of 2025, though the absence of an operation name and arrests count limits comparability against named campaigns such as [[cryptex-pm2btc-sanctions|Cryptex/PM2BTC]].

## Cooperation Mechanisms Used

1. **Bilateral DE-CH judicial cooperation** through Eurojust coordination
2. **Europol operational/analytical support** — including analytical support for infrastructure and financial tracing, with technical specifics not public
3. **Mutual Legal Assistance** — the action is MLA-compatible because it required cross-border server access and asset freezing

## Challenges and Friction Points

- **Crypto-asset jurisdictional complexity**: Mixing services typically distribute infrastructure across multiple hosting providers and chains.
- **Switzerland's non-EU status**: Coordination required additional bilateral channels rather than EU instruments alone.
- **Information opacity**: The release omits the service name, arrests count, and the specific legal basis used by Switzerland — limiting follow-up cross-checking.

## Lessons Learned

- Bilateral DE-CH cooperation under Eurojust can deliver significant cryptocurrency seizures even when one party (Switzerland) sits outside the EU.
- Eurojust's third-country cooperation agreements provide a procedural backbone for routine cross-jurisdictional crypto enforcement.

## Korean Involvement (한국의 참여)

No [[south-korea|South Korean]] participation is documented in this operation. Korean exchanges (Upbit, Bithumb) and the Korean Financial Intelligence Unit (KoFIU) may monitor such mixer takedowns for follow-on intelligence on Korean-resident depositors.

## Contradictions & Open Questions

- **What is the name of the mixing service?** The Eurojust release does not identify it; subsequent CoinDesk, AML Intelligence, TechRadar, and heise reporting plus the Europol 2025-11-26 release identify the service as **Cryptomixer / cryptomixer.io** with operation codename **Operation Olympia**.
- **How many arrests, if any, were made?** The cited source leaves this undisclosed.
- **Which German prosecutor (ZIT Frankfurt? a Land prosecutor?) led the German component?** The cited source leaves this undisclosed.
- **What was the legal basis used by Switzerland?** Candidate legal bases include the Eurojust-Switzerland cooperation agreement and Swiss Criminal Code art. 305bis (money laundering), but the cited source does not confirm the instrument.
- **Is this operation linked to any larger campaign (e.g., Operation Endgame, a sanctions track)?** No linkage is stated in the source.

**L26 Background gap notes** (crime substance missing from cited tier-1 sources):
- **Cryptomixer operator identities / OCG headcount / nationality of operators** — no arrests enumerated, operator identity remains undisclosed in the cited Europol and Eurojust releases.
- **Customer-criminal segmentation** — per-customer-segment breakdown of the EUR 1.3 billion lifetime laundering pool (ransomware vs darknet vs BEC vs carding) is not provided in the cited primary sources.
- **Victim-level enumeration** — second-order victim count (downstream ransomware and fraud victims whose paid-out BTC passed through Cryptomixer) is not disclosed; the EUR 1.3 billion figure aggregates across criminal customers, not victims.
- **Fee structure / operator margin** — Cryptomixer's per-mix fee percentage and accumulated operator revenue (the criminal monetisation) is not stated in the cited releases.


## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Eurojust, 2025-12-01: Cryptocurrency mixing service used to launder money taken down.
- CoinDesk, 2025-12-01: European authorities seize Bitcoin-mixing service Cryptomixer.
- AML Intelligence, 2025-12-01: EU takes down Cryptomixer, used to mix EUR 1.3bn in Bitcoin.
- TechRadar, 2025-12-02: Huge cryptomixer takedown sees feds seize over USD 30 million.
- heise online, 2025-12-01: Illegaler 'Cryptomixer' von Strafverfolgern zerschlagen.

## Evidence and Attribution Notes

- Germany and Switzerland, with Eurojust and Europol, took down a cryptocurrency mixing service used to launder proceeds from drug trafficking, weapons trafficking, online fraud and other cybercrimes (action published 1 December 2025)
- More than EUR 25 million in cryptocurrency seized during the action week
- Operation not publicly named in the Eurojust release; descriptive slug used in wiki
- CoinDesk reported that European authorities seized Cryptomixer infrastructure, including three servers and the domain.
- The article attributed the action to German and Swiss authorities with Europol and Eurojust support.
- CoinDesk reported that European authorities seized **Cryptomixer** infrastructure with German and Swiss participation.
- AML Intelligence identified the service as Cryptomixer and reported server, domain, and crypto seizures.
- The report linked the action to German and Swiss authorities with Eurojust and Europol.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a infrastructure-seizure against Unnamed cryptocurrency mixing service used to launder proceeds from drug trafficking, weapons trafficking, online fraud, and other cybercrimes, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Eurojust and coordination to Eurojust, with participating or affected jurisdictions recorded as Germany and Switzerland.

The cooperation model is documented through named agencies and partners: Eurojust and Europol Ec3; mechanisms: MLAT Process and Joint Investigation Team; legal basis: Budapest Convention and mutual legal assistance; enforcement posture: Seizure, Takedown, Asset Freeze.

Operational results captured for the canonical record: 3 servers seized; cryptocurrency/asset result recorded as EUR 25 million; 3 servers seized; Cryptocurrency mixing service infrastructure dismantled.

The canonical source set contains 5 reference(s): 2025 12 01 Eurojust De Ch Crypto Mixer Takedown, 2025 12 01 Coindesk Com Cryptomixer Takedown, 2025 12 01 Amlintelligence Com Cryptomixer Used To Mix 13bn In Bitcoin, 2025 12 02 Techradar Com Huge Cryptomixer Takedown Sees Feds Seize Over Usd30milion, 2025 12 01 Heise De Illegaler Cryptomixer Von Strafverfolgern Zerschlagen.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Operation Name, Service Name, Arrests, Indictments, Start Date, Specific Legal Basis For Switzerland.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Cryptocurrency mixing service used to launder money taken down | Eurojust | 2025-12-01 | https://www.eurojust.europa.eu/news/cryptocurrency-mixing-service-used-launder-money-taken-down |
| [2] | European authorities seize Bitcoin-mixing service Cryptomixer | CoinDesk | 2025-12-01 | https://www.coindesk.com/policy/2025/12/01/european-authorities-seize-usd1-51b-bitcoin-laundering-service-cryptomixer |
| [3] | EU takes down Cryptomixer, used to mix EUR 1.3bn in Bitcoin | AML Intelligence | 2025-12-01 | https://www.amlintelligence.com/2025/12/latest-eu-takes-down-cryptomixer-used-to-mix-e1-3bn-in-bitcoin/ |
| [4] | Huge cryptomixer takedown sees feds seize over USD 30 million | TechRadar | 2025-12-02 | https://www.techradar.com/pro/security/huge-cryptomixer-takedown-sees-feds-seize-over-usd30milion |
| [5] | Illegaler 'Cryptomixer' von Strafverfolgern zerschlagen | heise online | 2025-12-01 | https://www.heise.de/news/Illegaler-Cryptomixer-von-Strafverfolgern-zerschlagen-11098583.html |
| [6] | [[2025-11-26_europol_cryptomixer-operation-olympia-takedown\|Europol and partners shut down 'Cryptomixer' (Operation Olympia)]] | Europol | 2025-11-26 | https://www.europol.europa.eu/media-press/newsroom/news/europol-and-partners-shut-down-cryptomixer |
