---
type: operation
title: "Operation HAECHI IV"
aliases: ["HAECHI IV", "HAECHI 4"]
operation_type: "arrest-sweep"
status: "completed"
case_id: "CYB-2023-004"
period: 3
enforcement_type:
  - "arrest"
  - "asset_freeze"
outcome: "success"
credibility_index: 2.28
source_tier: 2
edges:
  - source_actor: "KNPA"
    target_actor: "INTERPOL"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
  - source_actor: "KNPA"
    target_actor: "Philippines Police"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
missing_fields:
  - "legal_basis"
  - "mechanisms_used"
  - "full_participating_countries_list"
timeframe:
  announced: "2023-12-19"
  start: "2023-07"
  end: "2023-12"
  ongoing: false
crime_type: "[[online-fraud-ic]]"
target_entity: "Cyber-enabled financial crime networks (voice phishing, romance scams, BEC, investment fraud, online sextortion, e-commerce fraud)"
lead_agency: "[[interpol-igci]]"
coordinating_body: "[[interpol-igci]]"
participating_countries:
  - "[[south-korea]]"
  - "United States"
  - "United Kingdom"
  - "Japan"
  - "India"
participating_agencies:
  - "[[interpol-igci]]"
  - "[[knpa-cyber-bureau]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 3500
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "USD 101 million (virtual assets)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "USD 300 million total seized (USD 199 million fiat + USD 101 million virtual assets)"
    - "82,112 suspicious bank accounts blocked"
    - "260% increase in arrests compared to HAECHI III"
    - "Filipino-Korean cooperation led to arrest of high-profile online gambling criminal in Manila"
related_cases: []
related_operations:
  - "[[operation-haechi-v]]"
  - "[[operation-haechi-vi]]"
challenges_encountered: []
lessons_learned:
  - "Series-based approach enables consistent escalation (975 → 3,500 arrests from HAECHI III to IV)"
  - "AI-generated voice cloning emerging as new threat for impersonation scams"
  - "Virtual assets now represent significant portion of seizures (USD 101M of USD 300M total)"
source_count: 1
sources:
  - "[[2023-12-19-interpol-operation-haechi-iv]]"
created: 2026-04-08
updated: 2026-04-08
---

## Summary

Operation HAECHI IV was the fourth iteration of the Korea-initiated HAECHI series, running from July to December 2023 across **34 countries**. The operation resulted in approximately **3,500 arrests** and seizure of **USD 300 million** (USD 199M fiat, USD 101M virtual assets). Authorities blocked **82,112 suspicious bank accounts**. HAECHI IV represented a **260% increase** in arrests compared to HAECHI III (2022).

## Background

The HAECHI series, led by [[south-korea|South Korea]], is INTERPOL's flagship financial cybercrime operation. HAECHI IV targeted seven types of cyber-enabled fraud simultaneously:
1. Voice phishing (보이스피싱)
2. Romance scams
3. Online sextortion
4. Investment fraud
5. Money laundering (illegal online gambling)
6. Business email compromise (BEC)
7. E-commerce fraud

Investment fraud, BEC, and e-commerce fraud accounted for **75%** of cases investigated.

## Participating Parties

- **Lead:** [[interpol-igci|INTERPOL IGCI]]
- **Key national agency:** [[knpa-cyber-bureau|Korean National Police Agency (경찰청)]]
- **34 participating countries** including United States, United Kingdom, Japan, Hong Kong (China), India

## HAECHI Series Progression

| Operation | Year | Countries | Arrests | Seized |
|-----------|------|-----------|---------|--------|
| HAECHI III | 2022 | 30 | 975 | ~$130M | [^haechi3]
| **HAECHI IV** | **2023** | **34** | **3,500** | **$300M** |

[^haechi3]: > [!warning] Source needed — HAECHI III statistics (975 arrests, ~$130M) are not from a collected source. The HAECHI IV press release references a "260% arrest increase over HAECHI III" but does not provide explicit HAECHI III totals.
| [[operation-haechi-v|HAECHI V]] | 2024 | 40 | 5,500+ | $400M+ |
| [[operation-haechi-vi|HAECHI VI]] | 2025 | 40 | - | $439M |

## Results and Impact

- **~3,500 arrests** — 260% increase from HAECHI III
- **USD 300 million** seized (USD 199M fiat + USD 101M virtual assets)
- **82,112 bank accounts** blocked
- **Filipino-Korean cooperation:** Arrest in Manila of high-profile online gambling criminal after two-year manhunt

### Emerging Threats Identified

- **2 INTERPOL Purple Notices** issued warning of:
  - Fraudulent NFT sales
  - Deepfake technology use in scams
- UK police reported **AI-generated voice cloning** in impersonation scams — a significant evolution of voice phishing methodology

## Korean Involvement (한국의 참여)

South Korea leads the HAECHI series through the [[knpa-cyber-bureau|KNPA]]. In HAECHI IV:
- Korea served as the initiating and lead country
- Filipino-Korean cooperation resulted in arrest of an online gambling criminal in Manila after a 2-year manhunt
- HAECHI IV continued to address voice phishing — Korea's top domestic cybercrime concern
- The 34-country participation and 260% arrest increase reflect Korea's growing influence in international financial cybercrime enforcement

## Contradictions & Open Questions

- What is the breakdown of arrests by country and crime type?
- How many of the 82,112 blocked bank accounts resulted in successful fund recovery?
- What specific AI voice cloning cases were identified?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

## References
| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | USD 300 million seized and 3,500 suspects arrested in international financial crime operation — Operation HAECHI IV | INTERPOL | 2023-12-19 | [원본](https://www.interpol.int/News-and-Events/News/2023/USD-300-million-seized-and-3-500-suspects-arrested-in-international-financial-crime-operation) |
