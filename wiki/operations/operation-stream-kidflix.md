---
type: operation
title: "Operation Stream — Kidflix CSAM Platform Takedown"
aliases:
  - "Operation Stream"
  - "Kidflix takedown"
case_id: "CYB-2025-001"
period: 3
operation_type: "takedown"
status: "completed"
enforcement_type:
  - "arrest"
  - "seizure"
  - "takedown"
outcome: "success"
timeframe:
  announced: "2025-04-04"
  start: "2022-01-01"
  end: "2025-03-11"
  ongoing: false
crime_type: "[[csam-ic]]"
target_entity: "Kidflix (CSAM streaming platform)"
lead_agency: "[[germany-bka|Bavarian State Criminal Police (BKA Bavaria)]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[germany]]"
  - "[[netherlands]]"
  - "(35+ countries, full list not disclosed)"
participating_agencies:
  - "[[germany-bka|Bavarian State Criminal Police]]"
  - "[[europol-ec3]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 79
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "undisclosed (crypto payments traced via DeFi and exchanges)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1,393 suspects identified worldwide"
    - "3,000+ electronic devices seized"
    - "39 children identified and protected"
    - "91,000 unique CSAM videos (6,288 hours) on platform"
    - "1.8 million registered users"
edges:
  - source_actor: "ORG-NLEA-BKA-BAVARIA"
    target_actor: "ORG-ILEA-EUROPOL"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
  - source_actor: "ORG-ILEA-EUROPOL"
    target_actor: "(35+ country LEAs)"
    cooperation_type: "info_sharing"
    legal_basis: "unknown"
    direction: "directed"
  - source_actor: "ORG-NLEA-BKA-BAVARIA"
    target_actor: "ORG-NLEA-NETHERLANDS-POLITIE"
    cooperation_type: "evidence_transfer"
    legal_basis: "unknown"
    direction: "undirected"
credibility_index: 2.55
source_tier: 3
missing_fields:
  - "participating_countries_full_list"
  - "participating_agencies_count"
  - "servers_seized"
  - "cryptocurrency_seized_amount"
  - "legal_basis"
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "Cryptocurrency tracing (DeFi, Bitcoin ATMs, P2P) was essential for following the money"
  - "Long-term infiltration (2022-2025) required sustained international coordination"
source_count: 1
sources:
  - "[[2025-04-04-europol-operation-stream-kidflix]]"
created: 2026-04-08
updated: 2026-04-08
---

# Operation Stream — Kidflix CSAM Platform Takedown

## Summary

Operation Stream was a multi-year international law enforcement operation that dismantled Kidflix, one of the largest known child sexual abuse material (CSAM) streaming platforms on the dark web. Led by the Bavarian State Criminal Police and the Bavarian Central Office for the Prosecution of Cybercrime (ZCB), with coordination by [[europol-ec3|Europol]], the operation involved 35+ countries and is *highly likely* the largest CSAM platform takedown by user count (1.8 million registered users) as of 2025.

## Background

Kidflix launched in 2021 as a CSAM streaming platform on the dark web. Unlike traditional CSAM distribution sites, Kidflix enabled real-time streaming and used a cryptocurrency-based token system where uploaders earned tokens for categorizing content. The platform hosted over 91,000 unique videos totaling 6,288 hours, with approximately 3.5 new videos uploaded per hour.

## Participating Parties

- **Lead agency:** Bavarian State Criminal Police (Bayerisches Landeskriminalamt) and ZCB
- **Coordinating body:** [[europol-ec3|Europol]]
- **Participating countries:** 35+ (Germany and Netherlands explicitly named for server seizure)
- **Supporting role:** [[germany-bka|German Federal Criminal Police (BKA)]]

## Operational Timeline

| Date | Event |
|------|-------|
| 2021 | Kidflix platform launched |
| 2022 | Investigation initiated by Bavarian authorities |
| 2022-2025 | Multi-year investigation with Europol coordination |
| 2025-03-11 | Servers seized in Germany and Netherlands; platform taken offline |
| 2025-04-04 | Operation publicly announced |

## Results and Impact

- **Suspects identified:** 1,393 worldwide
- **Arrests:** 79 (some confirmed as both distributors and direct abusers)
- **Devices seized:** 3,000+
- **Children protected:** 39
- **Platform scale:** 1.8M users, 91K videos, 72K videos on server at seizure

## Cooperation Mechanisms Used

Europol provided coordination across 35+ countries. The investigation relied on cryptocurrency tracing through international exchanges, DeFi platforms, Bitcoin ATMs, and peer-to-peer exchanges.

## Challenges and Friction Points

- Cryptocurrency payment obfuscation through DeFi and multiple exchange types
- Scale of platform (1.8M users) created identification challenges
- Dark web hosting required specialized technical capabilities

## Korean Involvement (한국의 참여)

No direct Korean involvement reported in this operation.

## Contradictions & Open Questions

- Full list of 35+ participating countries not publicly disclosed
- Server seizure count not specified (only that servers in Germany and Netherlands were seized)
- Total cryptocurrency seized not disclosed despite tracing efforts
