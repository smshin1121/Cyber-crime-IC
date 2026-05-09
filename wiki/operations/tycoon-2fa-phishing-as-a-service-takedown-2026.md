---
type: operation
title: "Tycoon 2FA Phishing-as-a-Service Platform Takedown (Europol EC3 + Microsoft + 6-country LE coalition, 2026-03-04)"
title_ko: "Tycoon 2FA 피싱-서비스(PhaaS) 플랫폼 단속 (Europol EC3 + Microsoft + 6개국 법집행 연합, 2026-03-04)"
aliases:
  - "Tycoon 2FA takedown 2026"
  - "Tycoon 2FA PhaaS disruption"
  - "Global phishing-as-a-service platform taken down 2026"
  - "Europol CIEP Tycoon 2FA operation"
case_id: CYB-2026-118
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - domain-seizure
  - search-seizure
outcome: success
timeframe:
  announced: 2026-03-04
  start: 2023-08
  end: 2026-03-04
  ongoing: false
crime_type: "[[cybercrime-infrastructure-ic]]"
crime_types:
  - "[[cybercrime-infrastructure-ic]]"
  - "[[online-fraud-ic]]"
  - "[[hacking-ic]]"
target_entity: "Tycoon 2FA — phishing-as-a-service (PhaaS) platform active since at least August 2023; among the largest phishing operations worldwide. At peak generated tens of millions of phishing emails per month and facilitated unauthorised access to nearly 100 000 organisations globally including schools, hospitals, and public institutions. By mid-2025 accounted for roughly 62% of all phishing attempts blocked by Microsoft."
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[latvia]]"
  - "[[lithuania]]"
  - "[[portugal]]"
  - "[[poland]]"
  - "[[spain]]"
  - "[[united-kingdom]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[latvia-state-police]]"
  - "[[lithuania-police]]"
  - "[[portugal-policia-judiciaria]]"
  - "[[poland-police]]"
  - "[[spain-national-police]]"
  - "[[spain-guardia-civil]]"
  - "[[uk-nca]]"
  - "[[microsoft]]"
  - "[[trend-micro]]"
  - "[[shadowserver]]"
organizations:
  - "[[europol-ec3]]"
  - "[[latvia-state-police]]"
  - "[[lithuania-police]]"
  - "[[portugal-policia-judiciaria]]"
  - "[[poland-police]]"
  - "[[spain-national-police]]"
  - "[[spain-guardia-civil]]"
  - "[[uk-nca]]"
  - "[[microsoft]]"
  - "[[trend-micro]]"
  - "[[shadowserver]]"
mechanisms_used:
  - "[[domain-seizure]]"
  - "[[search-seizure]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Europol European Cybercrime Centre (EC3) coordination role under Regulation (EU) 2016/794 (Europol Regulation)"
  - "Europol Cyber Intelligence Extension Programme (CIEP) — first-of-its-kind public-private operational framework hosting private-sector experts at The Hague alongside EC3 analysts"
  - "EC3 Advisory Groups — steady-state public-private intelligence-sharing forums that disseminated the initial Trend Micro intelligence"
  - "Microsoft-led technical disruption (domain takedowns + control-panel disablement) in parallel with national LE seizure operations"
  - "National investigative authority of each participating country: Latvia State Police; Lithuania Criminal Police Bureau; Portugal Judicial Police; Poland Central Cybercrime Bureau (Centralne Biuro Zwalczania Cyberprzestępczości / CBZC); Spain National Police and Guardia Civil; UK National Crime Agency"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 330
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "330 domains forming the core infrastructure of the Tycoon 2FA service (phishing pages + control panels) taken down"
    - "Technical disruption led by Microsoft with a coalition of private partners (Cloudflare, Coinbase, Intel471, Proofpoint, Shadowserver Foundation, SpyCloud, Trend Micro)"
    - "Seizure of infrastructure and other operational measures carried out by law enforcement in 6 countries — Latvia, Lithuania, Portugal, Poland, Spain, and the United Kingdom — coordinated by Europol"
    - "Underlying disrupted ecosystem: PhaaS platform active since August 2023; tens of millions of phishing emails per month at peak; nearly 100 000 organisations globally with credentials harvested or accessed"
    - "Pre-disruption Microsoft-blocked share: ~62% of all phishing attempts blocked by Microsoft (mid-2025)"
    - "Arrests / suspect identification not enumerated in the cited primary release"
edges:
  - source_actor: europol-ec3
    target_actor: microsoft
    cooperation_type: technical_assistance
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: europol-ec3
    target_actor: trend-micro
    cooperation_type: info_sharing
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: europol-ec3
    target_actor: latvia-state-police
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: lithuania-police
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: portugal-policia-judiciaria
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: poland-police
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: spain-national-police
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: spain-guardia-civil
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: uk-nca
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "specific action day(s) on which infrastructure seizures were executed (the cited release announces the disruption on 2026-03-04 but does not enumerate a discrete action-day date for the LE seizures)"
  - "arrests and / or named suspects (the cited release does not enumerate arrests; it focuses on infrastructure disruption)"
  - "specific judicial authority orchestrating each national seizure"
  - "specific Europol command-post / coordination-centre arrangement (e.g., on-site coordination centre vs. virtual command post) is not enumerated in the cited release"
related_cases: []
related_operations:
  - "[[labhost-phishing-as-a-service-takedown-2024]]"
  - "[[lumma-stealer-takedown]]"
  - "[[w3ll-phishing-kit-takedown-2026]]"
  - "[[leakbase-takedown-2026]]"
  - "[[xss-is-cybercrime-forum-takedown-2025]]"
challenges_encountered: []
lessons_learned:
  - "First wiki record of the Europol Cyber Intelligence Extension Programme (CIEP) as a discrete IC mechanism class — a first-of-its-kind Europol programme that physically embeds private-sector experts at The Hague alongside EC3 analysts and investigators on specific operational projects. Distinct from the EC3 Advisory Groups (steady-state info-sharing) and from one-off Europol mobile-office deployments to national LE."
  - "Two-tier public-private cooperation pattern: EC3 Advisory Groups (steady-state info-sharing) → CIEP (operational embedding). The Tycoon 2FA case is described as the first publicised CIEP-driven operational outcome."
  - "Microsoft-led technical takedown + LE-led seizure split is reaffirmed as a recurring pattern in PhaaS / cybercrime-infrastructure disruption (compare with [[labhost-phishing-as-a-service-takedown-2024|LabHost]] and [[lumma-stealer-takedown|Lumma Stealer]])."
  - "Six-country EU + UK LE coalition (Latvia, Lithuania, Portugal, Poland, Spain, UK) reflects a slim-but-targeted PhaaS-takedown footprint — significantly smaller than LabHost (19 countries) but with deeper private-sector integration through CIEP."
  - "Eight-private-partner roster (Cloudflare, Coinbase, Intel471, Microsoft, Proofpoint, Shadowserver Foundation, SpyCloud, Trend Micro) is one of the broadest publicly-named private-sector coalitions in a Europol-coordinated cybercrime-infrastructure takedown to date."
source_count: 1
sources:
  - "[[2026-03-04_europol_global-phishing-service-platform-tycoon-2fa-taken-down]]"
summary: "On 2026-03-04 Europol announced the coordinated public-private disruption of Tycoon 2FA — one of the largest phishing-as-a-service (PhaaS) platforms worldwide, active since at least August 2023. 330 domains forming the platform's core infrastructure (phishing pages + control panels) were taken down. Technical disruption led by Microsoft with a coalition of private partners (Cloudflare, Coinbase, Intel471, Proofpoint, Shadowserver Foundation, SpyCloud, Trend Micro). Seizures and other operational measures carried out by law enforcement in 6 countries — Latvia, Lithuania, Portugal, Poland, Spain, and the United Kingdom — coordinated by Europol's European Cybercrime Centre (EC3). The investigation began after intelligence-sharing by Trend Micro through Europol's EC3 Advisory Groups, escalating into operational embedding via the Cyber Intelligence Extension Programme (CIEP), a first-of-its-kind Europol public-private framework. At peak Tycoon 2FA generated tens of millions of phishing emails per month and facilitated unauthorised access to nearly 100 000 organisations globally including schools, hospitals, and public institutions; by mid-2025 it accounted for ~62 % of all phishing attempts blocked by Microsoft."
created: 2026-05-09
updated: 2026-05-09
---
## Summary

On **2026-03-04**, Europol announced the coordinated public-private disruption of **Tycoon 2FA** — one of the **largest phishing-as-a-service (PhaaS) platforms worldwide**, active since at least **August 2023**. **330 domains** forming the platform's core infrastructure (phishing pages + control panels) were taken down. The technical disruption was led by **Microsoft** with a coalition of private partners; seizure of infrastructure and other operational measures were carried out by law enforcement in **six countries** — **Latvia, Lithuania, Portugal, Poland, Spain, and the United Kingdom** — coordinated by [[europol-ec3|Europol's European Cybercrime Centre (EC3)]].

## Background

Tycoon 2FA was a phishing-as-a-service (PhaaS) platform active since at least August 2023 that enabled thousands of cybercriminals to covertly access email and cloud-based service accounts. At scale, the platform generated **tens of millions of phishing emails each month** and facilitated unauthorised access to **nearly 100 000 organisations globally**, including schools, hospitals, and public institutions. By **mid-2025** Tycoon 2FA accounted for roughly **62 %** of all phishing attempts blocked by Microsoft.

The investigation was triggered by intelligence shared by **Trend Micro**. Europol disseminated this information through its **EC3 Advisory Groups** and operational networks, enabling a coordinated operational strategy to be developed. A number of Advisory Group members were subsequently brought into the investigation to support the disruption effort, and through Europol's **Cyber Intelligence Extension Programme (CIEP)**, Microsoft and Trend Micro worked alongside law enforcement authorities providing technical expertise and infrastructure analysis.

## Participating Parties

| Country / Sector | Authority / Partner |
|---|---|
| Coordinating | [[europol-ec3\|Europol European Cybercrime Centre (EC3)]] (central hub between private partners and investigators; CIEP framework operator) |
| Latvia | [[latvia-state-police\|Latvia State Police]] |
| Lithuania | [[lithuania-police\|Lithuania Criminal Police Bureau]] |
| Portugal | [[portugal-policia-judiciaria\|Portugal Judicial Police]] |
| Poland | [[poland-police\|Poland Central Cybercrime Bureau (CBZC)]] |
| Spain | [[spain-national-police\|Spanish National Police]]; [[spain-guardia-civil\|Guardia Civil]] |
| United Kingdom | [[uk-nca\|UK National Crime Agency]] |
| Private — technical lead | [[microsoft\|Microsoft]] |
| Private — initial intelligence | [[trend-micro\|Trend Micro]] |
| Private — coalition (named) | Cloudflare; Coinbase; Intel471; Proofpoint; [[shadowserver\|Shadowserver Foundation]]; SpyCloud |

## Legal Framework

- **Europol European Cybercrime Centre (EC3) coordination role** under Regulation (EU) 2016/794 (Europol Regulation).
- **Europol Cyber Intelligence Extension Programme (CIEP)** — described in the cited release as a first-of-its-kind Europol programme that brings private-sector experts to The Hague to work temporarily side-by-side with EC3 analysts and investigators on specific operational projects.
- **EC3 Advisory Groups** — Europol's steady-state public-private intelligence-sharing forums that disseminated the initial Trend Micro intelligence.
- **Microsoft-led technical disruption** (domain takedowns and control-panel disablement) executed in parallel with national LE seizure operations.
- **National investigative authority** of each participating country (Latvia State Police; Lithuania Criminal Police Bureau; Portugal Judicial Police; Poland CBZC; Spain National Police + Guardia Civil; UK NCA).

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2023-08 (at least) | Tycoon 2FA platform begins operation | Europol 2026-03-04 |
| (undated) | Trend Micro shares intelligence; Europol disseminates through EC3 Advisory Groups | Europol 2026-03-04 |
| (undated) | Coordinated operational strategy developed; Advisory Group members brought into the investigation | Europol 2026-03-04 |
| (undated) | CIEP-framework collaboration: Microsoft + Trend Micro work alongside LE in The Hague | Europol 2026-03-04 |
| Mid-2025 | Tycoon 2FA at peak ~62 % of all phishing attempts blocked by Microsoft | Europol 2026-03-04 |
| (undated, pre-2026-03-04) | Action / disruption phase: 330 domains taken down by Microsoft + private coalition; LE seizures in 6 countries | Europol 2026-03-04 |
| 2026-03-04 | Europol announces the disruption | Europol 2026-03-04 |

## Results and Impact

- **330 domains** forming the core infrastructure (phishing pages + control panels) **taken down**.
- **6-country LE coalition** executes seizures and operational measures: Latvia, Lithuania, Portugal, Poland, Spain, UK.
- **8 named private partners** in the disruption coalition: Cloudflare, Coinbase, Intel471, Microsoft, Proofpoint, Shadowserver Foundation, SpyCloud, Trend Micro.
- **Underlying disrupted ecosystem**: ~30 months of operation (Aug 2023 to early 2026); tens of millions of phishing emails per month at peak; nearly 100 000 organisations globally accessed; ~62 % share of Microsoft-blocked phishing attempts at mid-2025.
- **Arrests / named suspects**: not enumerated in the cited primary release. The release focuses on infrastructure disruption, not on prosecutions.

## Cooperation Mechanisms Used

The cited release describes three discrete IC mechanism classes for this operation:

1. **Europol Cyber Intelligence Extension Programme (CIEP)** — first-of-its-kind Europol public-private operational framework that hosts private-sector experts at The Hague to work side-by-side with EC3 analysts and investigators on specific operational projects. The Tycoon 2FA case is described as the first publicised CIEP-driven operational outcome.
2. **EC3 Advisory Groups** — Europol's steady-state public-private intelligence-sharing forums; the entry-point for Trend Micro's initial intelligence and the recruitment pool for the eventual CIEP-embedded private partners.
3. **Microsoft-led technical disruption + national LE seizure split** — the platform-level disruption (domain takedowns + control-panel disablement) is led by Microsoft with a coalition of private partners, while infrastructure seizures and other operational measures are carried out by national LE in 6 countries, all coordinated by Europol. Compare with [[labhost-phishing-as-a-service-takedown-2024|LabHost (April 2024)]] and [[lumma-stealer-takedown|Lumma Stealer (May 2025)]].

## Challenges and Friction Points

The cited release does not enumerate specific challenges. *Likely* (analyst inference): a 6-country + 8-private-partner coalition coordinated through a brand-new CIEP framework would face the usual public-private friction (NDAs, evidentiary chain-of-custody for industry-derived telemetry, varying national admissibility standards for private-sector intrusion data). None of these is documented in the source.

## Lessons Learned

- First wiki record of the **Europol Cyber Intelligence Extension Programme (CIEP)** as a discrete IC mechanism class.
- Two-tier public-private cooperation pattern: **EC3 Advisory Groups** (steady-state info-sharing) → **CIEP** (operational embedding).
- Microsoft-led technical takedown + LE-led seizure split is reaffirmed as a recurring pattern in PhaaS / cybercrime-infrastructure disruption.
- A six-country EU + UK LE coalition with eight named private-sector partners is one of the broadest publicly-named private-sector coalitions in a Europol-coordinated cybercrime-infrastructure takedown to date.

## Follow-Up Actions

The cited release does not enumerate downstream prosecutions or sanctions. *Likely* (analyst inference): operator-identification and / or money-laundering follow-on prosecutions in one or more of the 6 LE-coalition jurisdictions, but none is documented in the source.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited Europol release among the participating jurisdictions or private partners. The case is recorded in the wiki for the new CIEP IC mechanism class and the Microsoft-led + 6-country-LE PhaaS-takedown pattern. Korean exposure to Tycoon 2FA as a phishing platform — given the global ~100 000 organisations affected and the platform's worldwide scale — is *likely* present but is not enumerated in this source.

## Contradictions & Open Questions

- The cited release does not enumerate a discrete action-day date for the LE seizures, only the announcement date of 2026-03-04.
- Arrests / named suspects are not enumerated; the release focuses entirely on infrastructure disruption.
- Specific judicial authorities orchestrating each national seizure are not enumerated.
- Specific Europol command-post / coordination-centre arrangement (on-site vs. virtual) is not enumerated, in contrast with the more detailed [[xss-is-cybercrime-forum-takedown-2025|xss.is takedown]] release.
- The release frames Tycoon 2FA as having ~62 % of mid-2025 Microsoft-blocked phishing share but does not provide an aggregate post-disruption phishing-blocked share to quantify residual / displacement effects.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2026-03-04_europol_global-phishing-service-platform-tycoon-2fa-taken-down\|Global phishing-as-a-service platform taken down in coordinated public-private action]] | Europol | 2026-03-04 | https://www.europol.europa.eu/media-press/newsroom/news/global-phishing-service-platform-taken-down-in-coordinated-public-private-action |
