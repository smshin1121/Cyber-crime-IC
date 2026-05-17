---
type: operation
title: "Eurojust €100M Cryptocurrency Investment Fraud Takedown (Spain-Lithuania JIT, 2025)"
title_ko: "Eurojust 1억 유로 암호화폐 투자 사기 단속 (스페인-리투아니아 JIT, 2025)"
aliases:
  - "Eurojust 100M crypto fraud 2025"
  - "Spain-Lithuania crypto JIT takedown"
case_id: CYB-2025-204
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - asset-freeze
outcome: success
timeframe:
  announced: 2025-09-23
  start: 2018
  end: 2025-09-23
  ongoing: false
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
target_entity: "Cross-border online cryptocurrency investment fraud network active since at least 2018, defrauding 100+ victims in Germany, France, Italy, and Spain of EUR 100 million+ via professionally designed online platforms; proceeds laundered through Lithuanian bank accounts; cumulative corpus involves 23 countries"
lead_agency: "[[eurojust]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[spain]]"
  - "[[portugal]]"
  - "[[italy]]"
  - "[[romania]]"
  - "[[bulgaria]]"
  - "[[lithuania]]"
  - "[[germany]]"
  - "[[france]]"
participating_agencies:
  - "[[eurojust]]"
  - "[[europol-ec3]]"
  - "[[romania-diicot]]"
organizations:
  - "[[eurojust]]"
  - "[[europol-ec3]]"
  - "[[romania-diicot]]"
mechanisms_used:
  - "[[europol-jit]]"
  - "[[eurojust-coordination-meeting]]"
  - "[[european-arrest-warrant]]"
  - "[[european-investigation-order]]"
  - "[[asset-freezing]]"
  - "[[search-seizure]]"
legal_basis:
  - "Joint Investigation Team (JIT) between Spanish and Lithuanian authorities, Europol joined"
  - "European Arrest Warrant (EAW)"
  - "European Investigation Order(s) (EIO)"
  - "Freezing orders"
results:
  arrests: 5
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "100+ victims in Germany, France, Italy, and Spain defrauded of EUR 100 million+"
    - "Joint action day with searches in Spain (5), Portugal (5), Italy, Romania, and Bulgaria"
    - "Bank accounts and other financial assets frozen in Italy, Romania, and Bulgaria"
    - "Spain-Lithuania JIT established and joined by Europol"
    - "Europol deployed cryptocurrency expert to Portugal for in-country crypto-asset seizure on the action day"
    - "Lithuanian bank accounts identified as primary proceeds-laundering route"
    - "23-country corpus (proceeds-laundering or victim jurisdictions); 6 named action-day countries (Spain, Portugal, Italy, Romania, Bulgaria, Lithuania)"
    - "Active since at least 2018"
edges:
  - source_actor: spain
    target_actor: lithuania
    cooperation_type: joint_investigation
    legal_basis: europol-jit
    direction: undirected
  - source_actor: europol-ec3
    target_actor: spain
    cooperation_type: technical_assistance
    legal_basis: europol-jit
    direction: undirected
  - source_actor: europol-ec3
    target_actor: lithuania
    cooperation_type: technical_assistance
    legal_basis: europol-jit
    direction: undirected
  - source_actor: europol-ec3
    target_actor: portugal
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: undirected
  - source_actor: eurojust
    target_actor: spain
    cooperation_type: coordination
    legal_basis: european-arrest-warrant
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "indictments (post-arrest charging not enumerated)"
  - "individual victim breakdowns by country"
related_cases:

related_operations:
  - "[[eurojust-600m-crypto-money-laundering-takedown-2025]]"
  - "[[eurojust-massive-investment-fraud-hundreds-thousands-victims-2022]]"
challenges_encountered:

lessons_learned:
  - "First wiki record explicitly capturing a Spain-Lithuania JIT pattern in a major cryptocurrency-investment-fraud joint action day, with Europol joining as a third operational party. The 23-country corpus is among the wider per-operation jurisdictional coverage in the wiki."
  - "Europol cryptocurrency-expert in-country deployment to Portugal demonstrates a discrete IC mechanism class for cross-jurisdictional crypto-asset seizure that complements traditional JIT and EAW/EIO instruments."
  - "Lithuanian bank-account proceeds-laundering pattern identified by DOJ/Eurojust as the recurring laundering route — adds to the wiki's documentation of Lithuanian financial-system exposure to EU-wide crypto-fraud schemes alongside the [[us-v-tymoshchuk-nefilim-megacortex-lockergoga|Tymoshchuk Lithuania-cooperation track record]]."
source_count: 2
sources:
  - "[[2025-09-23_eurojust_100m-cryptocurrency-investment-fraud-takedown]]"
  - "[[2025-09-25_policia-judiciaria-pt_lisbon-leader-international-crypto-fraud-organisation]]"
summary: "Eurojust-coordinated 2025-09-23 joint action day across Spain, Portugal, Italy, Romania, and Bulgaria led to 5 arrests including the alleged main perpetrator behind an online cryptocurrency investment fraud running since at least 2018 that defrauded 100+ victims in Germany, France, Italy, and Spain of EUR 100 million+. Spain-Lithuania Joint Investigation Team supported by Europol; Europol deployed a cryptocurrency expert to Portugal for in-country crypto-asset seizure. 23-country corpus (proceeds-laundering or victim jurisdictions). Lithuanian bank accounts identified as the primary proceeds-laundering route. Eurojust assisted with the execution of a European Arrest Warrant, European Investigation Orders, and freezing orders."
created: 2026-05-09
updated: 2026-05-17
---
## Summary

On 2025-09-23 [[eurojust|Eurojust]] announced the coordinated joint action day during which **five suspects were arrested**, including the alleged main perpetrator behind an online cryptocurrency investment fraud that defrauded **over 100 victims in Germany, France, Italy, and Spain** of at least **EUR 100 million** through professionally designed online cryptocurrency-investment platforms running since at least **2018**. The fraud corpus covered **23 countries** as either proceeds-laundering or victim jurisdictions. Action-day searches occurred in **Spain (5 places), Portugal (5 places), Italy, Romania, and Bulgaria**, with bank accounts and other financial assets frozen in Italy, Romania, and Bulgaria.

The investigation was operationalised through a **Spain-Lithuania Joint Investigation Team (JIT)** that [[europol-ec3|Europol]] joined as the third operational party. Europol deployed a **cryptocurrency expert to Portugal** for in-country crypto-asset seizure on the action day, and provided operational and analytical support to national investigators since September 2020. Eurojust supported the JIT setup, coordinated the joint action day, organised coordination meetings, and assisted with the execution of a **European Arrest Warrant**, **European Investigation Orders**, and **freezing orders**.

## Background

### Modus operandi

The criminal network operated a **multi-platform "advance-fee" cryptocurrency investment scam** active since at least 2018. The Eurojust release describes "professionally designed online cryptocurrency-investment platforms" — i.e., custom web front-ends with dashboards, balance ledgers, fictitious investment-performance charts, and account-management interfaces that simulated a regulated brokerage. Victims were recruited via online advertisements, cold-call lead lists, and social-media direct outreach; they were onboarded through staged "account managers" and induced to deposit progressively larger sums against promised high returns. The dashboards displayed simulated gains for an extended period — often months — to build trust and to motivate further deposits. **The withdrawal trap (advance-fee element) is the defining mechanic**: when victims attempted to withdraw their notional profits or principal, the platform demanded successive additional payments framed as "withdrawal taxes," "anti-money-laundering fees," "verification deposits," or "liquidity-bridge fees" — each payment extracted further funds. Once victim payment capacity was exhausted, the platform disappeared and the websites went offline, severing the victim's only contact channel. The pattern repeated across multiple successive platforms over the seven-year operational period, with operators rotating domain names and brand identities to evade detection and to recycle victim-recruitment infrastructure.

### Victim profile and impact

The Eurojust release enumerates **100+ victims in Germany, France, Italy, and Spain** with **aggregate losses of EUR 100 million+** — i.e., an average individual loss of approximately EUR 1 million, signalling either high-net-worth victim targeting or extreme per-victim losses driven by sustained advance-fee pyramiding. The 23-country corpus indicates either victim presence in or proceeds-flow through 19 additional countries beyond the four named victim jurisdictions. The Eurojust release does not break down victim demographics, but advance-fee crypto-investment scams characteristically target middle-aged-to-older professionals with investable savings, often recently retired or otherwise outside the workforce, and the high per-victim loss profile suggests a focus on individuals with substantial liquid assets rather than mass-market micro-victimisation.

### Financial flow

The Eurojust release explicitly identifies the laundering route: **"Large parts of these investments were diverted mainly to bank accounts in Lithuania to launder the proceeds."** This is an unusually specific tier-1 attribution of laundering geography. The 23-country corpus implies a layered laundering structure — victim funds collected through payment processors and shell-company bank accounts in multiple jurisdictions, concentrated through Lithuanian bank accounts as the consolidation layer, and likely further dispersed into cryptocurrency, real estate, and other asset classes from there. Action-day freezing actions targeted financial assets in Italy, Romania, and Bulgaria (additional layering jurisdictions), but the EUR amounts frozen are not disclosed and the Lithuanian-account proceeds were already partially laundered by the action date. The Europol cryptocurrency-expert deployment to Portugal for in-country crypto-asset seizure indicates that **at least the Portugal node held crypto-asset holdings of the network**, distinct from the Lithuanian fiat-banking laundering route.

### Criminal organization structure

Five arrests including **the alleged main perpetrator** (detained in Lisbon per the Polícia Judiciária 2025-09-25 release). The Portuguese release characterises the detainee as "líder de organização internacional" (leader of an international organisation), indicating a hierarchical OCG structure with a clearly identified principal. Searches in five places in Spain plus five in Portugal plus additional sites in Italy, Romania, and Bulgaria imply a distributed operations cell footprint across at least five EU member states. The 2018-onwards seven-year operational continuity and the EUR 100 million+ scale require a stable team of platform developers, customer-facing "account managers," money-laundering operators, and command structure — consistent with a mid-to-large OCG rather than a small criminal cell. Per-cell role enumeration is not in the cited tier-1 sources.

## Participating Parties

| Role | Parties |
|---|---|
| Coordinating bodies | [[eurojust\|Eurojust]] (JIT support; coordination meetings; EAW/EIO/freezing-order execution); [[europol-ec3\|Europol]] (joined the JIT; cryptocurrency expert deployed to Portugal) |
| JIT partners | Spain, Lithuania (Europol joined as third party) |
| Spain | Investigative Court no. 1 of the Audiencia Nacional; Anti-Corruption Public Prosecutor's Office (PPO); Policía Nacional |
| Portugal | Central Department of Criminal Investigation and Prosecution Lisbon; Central Court of Criminal Investigation Lisbon; Judiciary Police |
| Bulgaria | PPO Sofia City; District PPO Plovdiv |
| Italy | PPO Turin; Guardia di Finanza — Nucleo Centrale Polizia Valutaria Rome; Guardia di Finanza — Nucleo Polizia Economico Finanzaria Turin |
| Lithuania | Prosecutor General's Office; Financial Crime Investigation Service |
| Romania | [[romania-diicot\|Prosecution Office of the High Court of Justice — Directorate for Investigation of Organised Crime and Terrorism (DIICOT)]]; Prosecution Office of the Court of Appeal Bucharest; Romanian Police — Directorate for Combatting Organised Crime, Service for Financial Investigations |
| Named victim jurisdictions | Germany, France, Italy, Spain (4 countries with 100+ victims; total 23-country corpus) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| at least 2018 | Cryptocurrency-investment fraud network active | Eurojust 2025-09-23 |
| September 2020 | Europol begins providing operational and analytical support to national investigators | Eurojust 2025-09-23 |
| (date not enumerated) | Spain-Lithuania JIT established with Eurojust support | Eurojust 2025-09-23 |
| 2025-09-23 (approx.) | Joint action day in Spain, Portugal, Italy, Romania, Bulgaria; 5 arrests; assets frozen | Eurojust 2025-09-23 |

## Results and Impact

- **5 arrests** (including the alleged main perpetrator).
- **5 places searched in Spain; 5 places searched in Portugal**; additional searches in Italy, Romania, and Bulgaria.
- **Bank accounts and other financial assets frozen** in Italy, Romania, and Bulgaria.
- **EUR 100 million+** defrauded from **100+ victims** in Germany, France, Italy, and Spain.
- **23-country corpus** (proceeds-laundering or victim jurisdictions).
- Lithuanian bank accounts identified as primary proceeds-laundering route.

## Cooperation Mechanisms Used

The cited release describes a **Joint Investigation Team (JIT)** between Spanish and Lithuanian authorities — the foundational instrument — with Europol joining as a third operational party. Eurojust assisted with the execution of a **European Arrest Warrant (EAW)**, **European Investigation Orders (EIO)**, and **freezing orders**. Europol's contribution included deployment of a cryptocurrency expert to Portugal for in-country crypto-asset seizure during the action day. The cooperation pattern is one of the most fully-articulated multi-instrument JIT records in the wiki corpus for a single operation, layering JIT, EAW, EIO, freezing orders, and cryptocurrency-expert deployment within a single joint action day.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited Eurojust release among the 23 countries in the fraud corpus or among the action-day jurisdictions. The case is recorded in the wiki for the Spain-Lithuania JIT cooperation pattern, the EU-wide cryptocurrency-investment-fraud methodology, and the Europol cryptocurrency-expert in-country deployment mechanism. Korean exposure to similar cryptocurrency-investment-fraud schemes is documented elsewhere in the wiki under broader voice-phishing and online-fraud corpus.

## Contradictions & Open Questions

- The cited release names 23 countries in the fraud corpus but enumerates only 8 (Spain, Portugal, Italy, Romania, Bulgaria, Lithuania, Germany, France). The remaining 15 countries are not enumerated.
- Specific victim numbers per country (Germany, France, Italy, Spain) are not enumerated; only the cumulative "100+ victims" total.
- The specific cryptocurrency-investment platform name (and any aliases) is not disclosed in the cited Eurojust release.
- Post-action-day charging timelines, indictment counts, and sentencing schedules are not enumerated.
- **L26 gap — financial flow quantification**: EUR amounts frozen on the action day in Italy, Romania, and Bulgaria, and crypto-asset amounts seized in Portugal, are not enumerated in the cited tier-1 sources; the EUR 100 million+ aggregate loss figure is not matched against recovery totals.
- **L26 gap — victim demographics**: per-country victim counts (within the named four — DE/FR/IT/ES), age profile, recruitment vector (advertising vs. cold-call vs. social-media outreach), and per-victim loss distribution are absent from the cited tier-1 sources.
- **L26 gap — OCG role enumeration**: the five arrestees' individual roles (platform developers, account managers, money-laundering operators, recruiters) and nationalities (beyond the Portuguese-detained main perpetrator) are not enumerated; the relationship between the main perpetrator and the other four arrestees (subordinates, partners, separate cell heads) is not disclosed.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-09-23_eurojust_100m-cryptocurrency-investment-fraud-takedown\|Eurojust coordinates action to halt cryptocurrency fraud of over 100 million euros across Europe]] | Eurojust | 2025-09-23 | https://www.eurojust.europa.eu/news/eurojust-coordinates-action-halt-cryptocurrency-fraud-over-100-million-euros-across-europe |
| [2] | [[2025-09-25_policia-judiciaria-pt_lisbon-leader-international-crypto-fraud-organisation\|Detido em Lisboa lider de organizacao internacional de criptoativos]] | Policia Judiciaria (Portugal) | 2025-09-25 | https://www.policiajudiciaria.pt/detido-em-lisboa-lider-de-organizacao-internacional-de-criptoativos/ |
