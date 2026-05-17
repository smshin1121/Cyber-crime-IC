---
type: operation
title: "Operation Endgame — Phase 2 (Ransomware Kill Chain Disruption)"
aliases:
  - "Operation Endgame Phase 2"
  - "Endgame Phase 2 May 2025"
operation_type: infrastructure-seizure
status: completed
case_id: CYB-2025-006
period: 3
enforcement_type:
  - seizure
  - takedown
  - asset_freeze
outcome: success
credibility_index: 2.28
source_tier: 2
edges:
  - source_actor: Europol
    target_actor: "German BKA"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: Eurojust
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
missing_fields: ""
timeframe:
  announced: 2025-05-23
  start: 2025-05-19
  end: 2025-05-22
  ongoing: false
crime_type: "[[ransomware-ic]]"
target_entity: "Initial-access malware infrastructure (Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, Warmcookie)"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[canada]]"
  - "[[denmark]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[canada-rcmp]]"
  - "[[denmark-police]]"
  - "[[france-national-police]]"
  - "[[france-gendarmerie]]"
  - "[[france-junalco]]"
  - "[[germany-bka]]"
  - "[[germany-frankfurt-prosecutor]]"
  - "[[netherlands-politie]]"
  - "[[uk-nca]]"
  - "[[fbi-cyber-division]]"
  - "[[us-secret-service]]"
  - "[[us-dcis]]"
  - "[[us-doj]]"
legal_basis:
  - "[[budapest-convention]]"
  - "[[mutual-legal-assistance]]"
  - "domestic cybercrime seizure and asset-freeze authorities"
mechanisms_used:
  - "[[europol-jit]]"
  - "[[mlat-process]]"
  - "[[informal-cooperation]]"
  - "[[public-private-cooperation]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 300
  domains_seized: 650
  cryptocurrency_seized: "EUR 3.5 million (this phase); EUR 21.2 million+ (total Operation Endgame)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "20 international arrest warrants issued"
    - "18 suspects added to EU Most Wanted list"
related_cases:
  - "[[us-v-stepanov-danabot]]"
related_operations:
  - "[[operation-endgame-phase1]]"
  - "[[operation-us-v-stepanov-danabot]]"
  - "[[operation-endgame-phase3]]"
  - "[[rcmp-cit-v-canada-endgame-surrey-malware-loader-arrest-2025]]"
challenges_encountered:

lessons_learned:
  - "Infrastructure-focused operations can achieve massive scale (300 servers, 650 domains) even without immediate arrests"
  - "International arrest warrants and EU Most Wanted listings create sustained pressure on fugitives"
  - "Cumulative cryptocurrency seizures (EUR 21.2M+) demonstrate the financial disruption potential of sustained campaigns"
source_count: 6
sources:
  - "[[2025-05-23-europol-operation-endgame-phase2]]"
  - "[[2025-05-28-thehackernews-danabot-malware]]"
  - "[[2025-05-22_europol-europa-eu_operation-endgame-follow-up-leads-to-detentions-and-server-takedowns]]"
  - "[[2024-05-29_fbi-gov_operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-o]]"
  - "[[2024-05-30_europol-europa-eu_largest-ever-operation-against-botnets-operation-endgame]]"
  - "[[2024-05-30_krebsonsecurity-com_operation-endgame-hits-malware-delivery-platforms]]"
created: 2026-04-08
updated: 2026-05-17
operation_role: umbrella
parent_operation: ""
summary: "**Operation Endgame Phase 2** was the second major phase of the international campaign against ransomware-enabling infrastructure, conducted between 19 and 22 May 2025. The operation achieved an unprecedented scale of infrastructure disruption: **300 servers taken down**, **650 domains neutralized**, and **EUR 3.5 million in cryptocurrency seized** (bringing total Operation Endgame seizures to over EUR 21.2 million)."
jurisdictions:
  - "[[canada]]"
  - "[[denmark]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[canada-rcmp]]"
  - "[[denmark-police]]"
  - "[[france-national-police]]"
  - "[[france-gendarmerie]]"
  - "[[france-junalco]]"
  - "[[germany-bka]]"
  - "[[germany-frankfurt-prosecutor]]"
  - "[[netherlands-politie]]"
  - "[[uk-nca]]"
  - "[[fbi-cyber-division]]"
  - "[[us-secret-service]]"
  - "[[us-dcis]]"
  - "[[us-doj]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
---
## Summary

**Operation Endgame Phase 2** was the second major phase of the international campaign against ransomware-enabling infrastructure, conducted between 19 and 22 May 2025. The operation achieved an unprecedented scale of infrastructure disruption: **300 servers taken down**, **650 domains neutralized**, and **EUR 3.5 million in cryptocurrency seized** (bringing total Operation Endgame seizures to over EUR 21.2 million).

While no physical arrests were made during this phase, **20 international arrest warrants** were issued and **18 suspects** were added to the **EU Most Wanted list**, creating sustained pressure on identified actors. The operation targeted initial-access malware families — Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, and Warmcookie — that form the beginning of the ransomware attack chain.

## Background

(This section describes the **crime substance** — modus operandi, victim profile + impact, financial flow, and criminal organisation structure of the seven malware families disrupted in Phase 2. Operation context belongs in the Summary; cross-phase comparison appears under Operational Timeline / Results.)

### Modus operandi — initial-access malware as the ransomware kill chain

Phase 2 targeted seven malware families that occupy the **initial-access stage** of the ransomware kill chain: **Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, and Warmcookie**. These are not themselves ransomware — they are the entry-and-foothold tools that ransomware affiliates rent or deploy to compromise corporate networks. The typical delivery sequence (verbatim where the cited tier-1 release narrates it; otherwise reflecting the established pattern of these malware families):

1. **Phishing email or malicious advertisement** carries a payload (e.g., Bumblebee, Warmcookie, Hijackloader) that establishes a beachhead on the victim machine.
2. **Loader/dropper stage** (Bumblebee, Hijackloader, Lactrodectus) pulls down additional modules — credential stealers, lateral-movement tooling, post-exploitation frameworks.
3. **Information-stealer / banking trojan stage** (DanaBot, Qakbot, Trickbot) harvests credentials, banking sessions, and corporate single-sign-on tokens; DanaBot specifically provides both criminal credential theft and on-demand espionage capability against government and military targets.
4. **Affiliate hand-off**: stolen access — RDP credentials, VPN tokens, Active Directory footholds — is sold to or used by ransomware affiliates (Conti, BlackBasta, REvil, LockBit) to deploy the encrypting payload.

DanaBot is singled out in the Phase 2 release: the US DOJ DanaBot indictment alleges DanaBot served **dual purposes** — commodity cybercrime (credential theft, banking fraud) plus state-aligned espionage (intrusions against government and military networks for handler-directed targeting).

### Victim profile and impact

The cited tier-1 sources (Europol, FBI, BMI Germany, plus The Hacker News for the DanaBot-specific arc) enumerate the following victim-side figures:

- **DanaBot alone**: 300,000+ computers infected worldwide; USD 50 million+ estimated cumulative financial damages.
- **Combined Phase 2 malware families**: Bumblebee, Trickbot, and Qakbot are documented in tier-1 reporting as the principal initial-access tools for the **Conti, BlackBasta, and REvil** ransomware ecosystems, which collectively victimised hospitals, schools, manufacturing companies, critical-infrastructure operators, and multinational corporations across at least 15 countries (figure from the umbrella [[operation-endgame|Operation Endgame]] reporting; per-family Phase 2 attribution is partly inferred from the Phase 1 + DanaBot disclosures).
- **No per-country victim breakdown** is provided in the cited Phase 2 sources; the figure of "9 servers seized in 10 countries" (Phase 1) versus "300 servers in Phase 2" indicates a substantially larger but uncharacterised victim footprint.

> [!note] Gap on victim profile
> The cited tier-1 Phase 2 sources enumerate infrastructure-seizure counts but do **not** publish per-malware-family victim counts, victim-country breakdowns, or per-family financial damage figures (except for the DanaBot-specific 300,000 / USD 50M arc). See the Contradictions section.

### Financial flow

- **DanaBot**: USD 50 million+ cumulative damages attributed by US DOJ. The 16-count DanaBot indictment alleges that operators received cryptocurrency payments through wallets linked to the alleged operators Aleksandr Stepanov and Artem Kalinkin (Novosibirsk, Russia); precise per-defendant proceeds breakdown not disclosed in the cited sources.
- **Phase 2 cryptocurrency seizures**: EUR 3.5 million from operator-controlled wallets identified during the investigation.
- **Cumulative across all Operation Endgame phases**: EUR 21.2 million+ in seized cryptocurrency. (A Phase 1 suspect-asset figure of EUR 69 million is also reported — see Contradictions for the relationship between asset-freeze and seizure totals.)

> [!note] Gap on financial flow
> Per-family ransom-revenue figures (for Bumblebee, Lactrodectus, Qakbot, Hijackloader, Trickbot, Warmcookie) are not disclosed in the cited Phase 2 tier-1 sources. The aggregate EUR 21.2M+ figure does not break down by malware family or by Phase. See Contradictions.

### Criminal organisation structure

The cited tier-1 sources describe the Phase 2 target ecosystem as a **services market** rather than a single criminal organisation:

- **Operator cells per malware family**: each of the seven malware families is run by a distinct operator team that maintains the codebase, the control-panel infrastructure, and the affiliate-recruitment channel. DanaBot's operator team is the only one publicly named in the Phase 2 release — **16 Russian nationals** indicted by US DOJ, including Aleksandr Stepanov (39) and Artem Kalinkin (34), both of Novosibirsk, Russia.
- **Affiliate model**: each operator team rents or licenses access to ransomware affiliates and other criminal customers. Affiliates pay either flat fees, per-install fees, or revenue-share splits; the Phase 1 Smokeloader customer database (seized May 2024) provided the template for the subsequent April 2025 demand-side follow-up.
- **Geographic distribution**: operator infrastructure spans cloud, bullet-proof-hosting, and compromised legitimate hosting across the 7+ Phase 2 jurisdictions plus additional non-cooperating locations (notably Russia, where many operators reside).
- **Russian-nexus concentration**: the named DanaBot operators are all Russian nationals; the broader Phase 2 indictment / EU Most Wanted list adds 18 suspects whose national affiliations are partially disclosed and weighted toward Russia and the former Soviet space.

> [!note] Gap on OCG structure
> The cited tier-1 Phase 2 sources name only the 16 DanaBot indicted operators. For the other six malware families (Bumblebee, Lactrodectus, Qakbot, Hijackloader, Trickbot, Warmcookie), operator identities are not enumerated in the cited Phase 2 sources, and only the EU Most Wanted listing (18 suspects total) hints at the broader operator pool. See Contradictions.

### Cumulative Operation Endgame Results (Phase 1 + Phase 2)

| Metric | Phase 1 (May 2024) | Phase 2 (May 2025) | Total |
|--------|-------------------|-------------------|-------|
| Arrests | 4 | 0 | 4 |
| Servers seized | 100+ | 300 | 400+ |
| Domains seized | 2,000+ | 650 | 2,650+ |
| Cryptocurrency seized | — | EUR 3.5M | EUR 21.2M+ (cumulative) |
| Arrest warrants | — | 20 | 20+ |
| EU Most Wanted | — | 18 | 18 |

## Participating Parties

### Coordinating Bodies
- [[europol-ec3|Europol]]
- [[eurojust|Eurojust]]

### Participating Countries (7)
Canada, Denmark, France, Germany, Netherlands, United Kingdom, United States

### Participating Agencies (15)
[[europol-ec3]], [[eurojust]], [[canada-rcmp|RCMP]], [[denmark-police|Danish Police]], [[france-national-police|French National Police]], [[france-gendarmerie|French Gendarmerie]], [[france-junalco|JUNALCO]], [[germany-bka|German BKA]], [[germany-frankfurt-prosecutor|Frankfurt Prosecutor]], [[netherlands-politie|Dutch National Police]], [[uk-nca|UK NCA]], [[fbi-cyber-division|FBI]], [[us-secret-service|US Secret Service]], [[us-dcis|DCIS]], [[us-doj|US DOJ]]

## Legal Framework

- **20 international arrest warrants** issued through coordinated judicial action
- **18 suspects** added to EU Most Wanted list
- **EUR 3.5 million** in cryptocurrency seized through court-authorized seizure orders

> [!info] Legal-basis note
> Specific legal bases for the international arrest warrants and cryptocurrency seizures need to be identified from additional sources.

## Operational Timeline

| Date | Event |
|------|-------|
| 2024-05-27 to 2024-05-29 | Phase 1 conducted |
| 2025-05-19 | Phase 2 action days begin |
| 2025-05-19 to 2025-05-22 | 300 servers taken down, 650 domains neutralized |
| 2025-05-23 | Public announcement by Europol |

## Results and Impact

| Metric | Count |
|--------|-------|
| Servers taken down | 300 |
| Domains neutralized | 650 |
| Cryptocurrency seized (this phase) | EUR 3.5 million |
| Cryptocurrency seized (total Endgame) | EUR 21.2 million+ |
| International arrest warrants | 20 |
| EU Most Wanted additions | 18 |
| Physical arrests | 0 (this phase) |
| Malware families targeted | 7 |

## Cooperation Mechanisms Used

- **Europol coordination:** Operational coordination across 7 countries
- **Eurojust:** Judicial coordination for arrest warrants and seizure orders
- **Multi-country simultaneous action:** Synchronized takedown of 300 servers across multiple jurisdictions
- **EU Most Wanted mechanism:** 18 additions to create public pressure and enable identification

## Lessons Learned

1. **Infrastructure over individuals:** Even without immediate arrests, taking down 300 servers and 650 domains caused significant operational disruption to the ransomware ecosystem.
2. **Cumulative financial impact:** The EUR 21.2M+ cumulative cryptocurrency seizures demonstrate that sustained campaigns compound financial disruption over time.
3. **Warrant-first approach:** Issuing 20 international arrest warrants and EU Most Wanted listings creates a legal framework for future arrests when suspects travel to cooperative jurisdictions.
4. **Sustained campaigns:** The 12-month gap between Phase 1 and Phase 2 demonstrates an ongoing operational model rather than one-off actions.

## Follow-Up Actions

The issuance of 20 international arrest warrants and 18 EU Most Wanted listings indicates sustained follow-on pressure, targeting the identified individuals when opportunities for arrest arise.

## Korean Involvement (한국의 참여)

No direct Korean involvement in Operation Endgame Phase 2 was identified.

## DanaBot Malware Takedown (Excel Data Supplement)

> [!note] Data from Excel batch import (2026-04-08)
> The following DanaBot-specific details were identified from The Hacker News reporting (row 11 of Excel data) and supplement the main Europol source.

As part of Operation Endgame, the US Department of Justice led the dismantlement of the **DanaBot** malware network specifically:
- **16 individuals** indicted by US DOJ for operating DanaBot
- **300,000+ computers** infected worldwide by DanaBot
- **USD 50 million+** in estimated financial damages from DanaBot alone
- DanaBot served dual purposes: cybercrime (credential theft, fraud) and espionage (government/military targeting)

### Follow-Up Phase: 5 Additional Detentions

A follow-up enforcement action (row 21, Europol URL) resulted in:
- **5 additional detentions** and interrogations
- Additional server takedowns
- This represents a continuation of the arrest-warrant execution phase following the main infrastructure takedown

## Contradictions & Open Questions

- What specific impact did Phase 2 have on ransomware deployment rates?
- How many of the 20 arrest warrant subjects have been subsequently apprehended? (At least 5 per follow-up reporting)
- How quickly did the targeted malware families reconstitute operations after the takedown?
- What is the relationship between the EUR 21.2M+ total and the Phase 1 EUR 69M suspect holdings figure?
- The 16 DanaBot indictments and 300K infection figure come from The Hacker News (non-official source) — official DOJ source needed for confirmation.
- **L26 gap — victim profile per malware family**: cited tier-1 Phase 2 sources publish only DanaBot-specific victim counts (300,000 infections, USD 50M damages). Per-family victim counts and per-country victim breakdowns for Bumblebee, Lactrodectus, Qakbot, Hijackloader, Trickbot, and Warmcookie are not disclosed.
- **L26 gap — financial flow per malware family**: only the EUR 3.5M Phase 2 cryptocurrency seizure and EUR 21.2M+ Operation-Endgame-cumulative figure are disclosed. Per-family ransom-revenue or operator-revenue figures (other than DanaBot's USD 50M+ damages attribution) are not enumerated.
- **L26 gap — OCG structure for six of seven malware families**: only the 16 DanaBot operators are publicly named. Operator identities, recruitment patterns, and revenue-share splits for Bumblebee, Lactrodectus, Qakbot, Hijackloader, Trickbot, and Warmcookie operator cells are not enumerated in the cited Phase 2 sources beyond the aggregate "18 EU Most Wanted listings" figure.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2025-05-23: Operation Endgame strikes again: the ransomware kill chain broken at its source.
- The Hacker News, 2025-05-28: DanaBot malware reporting.
- Europol, 2025-05-22: Operation Endgame Follow-up.
- FBI, 2024-05-29: Operation Endgame: Coordinated Worldwide Law Enforcement Action Against Network of Cybercriminals.
- Europol, 2024-05-30: Largest ever operation against botnets — Operation Endgame.
- KrebsOnSecurity, 2024-05-30: 'Operation Endgame' Hits Malware Delivery Platforms.
- Europol, 2025-05-22: Operation Endgame: Follow-up leads to detentions and server takedowns.

## Evidence and Attribution Notes

- Operation Endgame Phase 2 took down 300 servers, neutralized 650 domains, and seized EUR 3.5M in cryptocurrency (19-22 May 2025)
- 20 international arrest warrants issued; 18 suspects added to EU Most Wanted list
- Total Operation Endgame cryptocurrency seizures: EUR 21.2 million+
- Targeted initial-access malware: Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, Warmcookie
- 7 countries participated with 15 agencies; struck at the start of the ransomware attack chain
- During 19-22 May 2025, the second major phase of **Operation Endgame** disrupted ransomware-enabling infrastructure at an unprecedented scale: 300 servers taken down globally, 650 domains neutralized, and EUR 3.5 million in cryptocurrency seized (bringing the total Operation Endgame seizures to over EUR 21.2 million).
- International arrest warrants were issued for 20 key actors, with 18 suspects added to the EU Most Wanted list.
- The operation targeted initial-access malware families including Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, and Warmcookie.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- FBI, 2024-05-29: Law enforcement in Ukraine, Portugal, Romania, Lithuania, Bulgaria, and Switzerland supported police actions to arrest or interview suspects, conduct searches, and seize or take down servers.
- FBI, 2024-05-29: Beginning on May 28, 2024, the first coordinated international operation of its kind involved a dozen countries that conducted searches, questioned or arrested subjects, and took down or disrupted more than 100 servers to defeat multiple malware variants.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a infrastructure-seizure against Initial-access malware infrastructure (Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, Warmcookie), rather than a defendant-specific follow-on action. The record attributes lead responsibility to Europol Ec3 and coordination to Europol Ec3, with participating or affected jurisdictions recorded as Canada, Denmark, France, Germany, Netherlands, United Kingdom, United States.

The cooperation model is documented through named agencies and partners: Europol Ec3, Eurojust, Canada Rcmp, Denmark Police, France National Police, France Gendarmerie, France Junalco, Germany Bka, Germany Frankfurt Prosecutor, Netherlands Politie; enforcement posture: Seizure, Takedown, Asset Freeze.

Operational results captured for the canonical record: 300 servers seized; 650 domains seized; cryptocurrency/asset result recorded as EUR 3.5 million (this phase); EUR 21.2 million+ (total Operation Endgame); 20 international arrest warrants issued; 18 suspects added to EU Most Wanted list.

The canonical source set contains 7 reference(s): 2025 05 23 Europol Operation Endgame Phase2, 2025 05 28 Thehackernews Danabot Malware, 2025 05 22 Europol Endgame Follow Up, 2024 05 29 Fbi Gov Operation Endgame Coordinated Worldwide Law Enforcement Action Against Network O, 2024 05 30 Europol Europa Eu Largest Ever Operation Against Botnets Operation Endgame, 2024 05 30 Krebsonsecurity Com Operation Endgame Hits Malware Delivery Platforms, plus 1 more.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis and Mechanisms Used.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Operation Endgame strikes again: the ransomware kill chain broken at its source | Europol | 2025-05-23 | https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-strikes-again-ransomware-kill-chain-broken-its-source |
| [2] | DanaBot malware reporting | The Hacker News | 2025-05-28 | https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html |
| [3] | Operation Endgame: Follow-up leads to detentions and server takedowns | Europol | 2025-05-22 | https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-follow-leads-to-five-detentions-and-interrogations-well-server-takedowns |
| [4] | Operation Endgame: Coordinated Worldwide Law Enforcement Action Against Network of Cybercriminals | FBI | 2024-05-29 | https://www.fbi.gov/news/press-releases/operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-of-cybercriminals |
| [5] | Largest ever operation against botnets — Operation Endgame | Europol | 2024-05-30 | https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem |
| [6] | 'Operation Endgame' Hits Malware Delivery Platforms | KrebsOnSecurity | 2024-05-30 | https://krebsonsecurity.com/2024/05/operation-endgame-hits-malware-delivery-platforms/ |
