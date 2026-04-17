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
missing_fields:
  - legal_basis
  - mechanisms_used
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

mechanisms_used:

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
challenges_encountered:

lessons_learned:
  - "Infrastructure-focused operations can achieve massive scale (300 servers, 650 domains) even without immediate arrests"
  - "International arrest warrants and EU Most Wanted listings create sustained pressure on fugitives"
  - "Cumulative cryptocurrency seizures (EUR 21.2M+) demonstrate the financial disruption potential of sustained campaigns"
source_count: 3
sources:
  - "[[2025-05-23-europol-operation-endgame-phase2]]"
  - "[[2025-05-28-thehackernews-danabot-malware]]"
  - "[[2025-05-22-europol-endgame-follow-up]]"
created: 2026-04-08
updated: 2026-04-12
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
---
## Summary

**Operation Endgame Phase 2** was the second major phase of the international campaign against ransomware-enabling infrastructure, conducted between 19 and 22 May 2025. The operation achieved an unprecedented scale of infrastructure disruption: **300 servers taken down**, **650 domains neutralized**, and **EUR 3.5 million in cryptocurrency seized** (bringing total Operation Endgame seizures to over EUR 21.2 million).

While no physical arrests were made during this phase, **20 international arrest warrants** were issued and **18 suspects** were added to the **EU Most Wanted list**, creating sustained pressure on identified actors. The operation targeted initial-access malware families — Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, and Warmcookie — that form the beginning of the ransomware attack chain.

## Background

Building on [[operation-endgame-phase1|Phase 1]] (May 2024), which targeted 6 dropper malware families and resulted in 4 arrests and 100+ servers taken down, Phase 2 expanded the scope to 7 malware families and achieved significantly larger infrastructure takedowns.

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

> [!warning] Legal status check needed
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

1. **Infrastructure over individuals:** Even without immediate arrests, taking down 300 servers and 650 domains *almost certainly* caused significant operational disruption to the ransomware ecosystem.
2. **Cumulative financial impact:** The EUR 21.2M+ cumulative cryptocurrency seizures demonstrate that sustained campaigns compound financial disruption over time.
3. **Warrant-first approach:** Issuing 20 international arrest warrants and EU Most Wanted listings creates a legal framework for future arrests when suspects travel to cooperative jurisdictions.
4. **Sustained campaigns:** The 12-month gap between Phase 1 and Phase 2 suggests an ongoing operational model rather than one-off actions.

## Follow-Up Actions

The issuance of 20 international arrest warrants and 18 EU Most Wanted listings *almost certainly* indicates that further phases are planned, likely targeting the identified individuals when opportunities for arrest arise.

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
- The 16 DanaBot indictments and 300K infection figure come from The Hacker News (Tier 3) — official DOJ source needed for confirmation.

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Operation Endgame strikes again: the ransomware kill chain broken at its source | Europol | 2025-05-23 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-strikes-again-ransomware-kill-chain-broken-its-source) |
| [2] | US Dismantles DanaBot Malware Network | The Hacker News | 2025-05-28 | [원본](https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html) |
| [3] | Operation Endgame: Follow-up leads to detentions and server takedowns | Europol | 2025-05-22 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-follow-leads-to-five-detentions-and-interrogations-well-server-takedowns) |
