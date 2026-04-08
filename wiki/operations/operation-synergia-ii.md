---
type: operation
title: "Operation Synergia II"
aliases: ["Synergia II", "Synergia 2"]
operation_type: "infrastructure-seizure"
status: "completed"
case_id: "CYB-2024-007"
period: 3
enforcement_type:
  - "arrest"
  - "seizure"
  - "takedown"
outcome: "success"
credibility_index: 3.25
source_tier: 2
edges:
  - source_actor: "INTERPOL"
    target_actor: "Group-IB"
    cooperation_type: "info_sharing"
    legal_basis: "unknown"
    direction: "directed"
  - source_actor: "INTERPOL"
    target_actor: "Trend Micro"
    cooperation_type: "info_sharing"
    legal_basis: "unknown"
    direction: "directed"
  - source_actor: "INTERPOL"
    target_actor: "Hong Kong Police"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
missing_fields:
  - "legal_basis"
  - "mechanisms_used"
  - "full_participating_countries_list"
timeframe:
  announced: "2024-11-06"
  start: "2024-04-01"
  end: "2024-08-31"
  ongoing: false
crime_type: "[[ransomware-ic]]"
target_entity: "Phishing, ransomware, and information stealer infrastructure"
lead_agency: "[[interpol-igci]]"
coordinating_body: "[[interpol-igci]]"
participating_countries: []
participating_agencies:
  - "[[interpol-igci]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 41
  indictments: 0
  servers_seized: 59
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "22,800 malicious IP addresses taken down (76% of ~30,000 identified)"
    - "43 electronic devices seized (laptops, mobile phones, hard disks)"
    - "65 additional individuals under investigation"
related_cases: []
related_operations:
  - "[[operation-haechi-v]]"
  - "[[operation-serengeti]]"
challenges_encountered: []
lessons_learned:
  - "Public-private partnership model (Group-IB, Trend Micro, Kaspersky, Team Cymru) enables comprehensive threat intelligence for infrastructure-focused operations"
  - "Broad participation (95 countries) demonstrates INTERPOL's unique convening power for global cyber operations"
source_count: 1
sources:
  - "[[2024-11-06-interpol-operation-synergia-ii]]"
created: 2026-04-08
updated: 2026-04-08
---

## Summary

Operation Synergia II was a massive INTERPOL-coordinated operation targeting malicious cyber infrastructure across **95 INTERPOL member countries** from April to August 2024. The operation focused on phishing, ransomware, and information stealer infrastructure. It identified approximately 30,000 suspicious IP addresses, took down 76% of them (~22,800), seized 59 servers and 43 electronic devices, and resulted in 41 arrests with 65 others still under investigation.

The operation demonstrated INTERPOL's unique capacity to coordinate global-scale infrastructure-focused cyber operations with extensive private sector partnership.

## Background

Operation Synergia II was the second iteration of INTERPOL's Synergia operation series. The first Operation Synergia (September-November 2023) coordinated across 60+ countries and took down 1,300+ suspicious servers. [^synergia1]

[^synergia1]: > [!warning] Source needed — Operation Synergia (2023) statistics are not from a collected source. Only Synergia II (2024) has a collected source. Synergia II significantly expanded the scope to 95 countries and shifted focus to IP-level infrastructure disruption.

## Participating Parties

- **Lead:** [[interpol-igci|INTERPOL IGCI]]
- **Participating countries:** 95 INTERPOL member countries
- **Private sector partners:** Group-IB, Trend Micro, Kaspersky, Team Cymru

### Notable Country Actions

| Country | Action |
|---------|--------|
| Hong Kong | Took down 1,037 malicious servers |
| Macau (China) | Took down 291 servers |
| Mongolia | Searched 21 houses, seized server, identified 93 linked individuals |
| Madagascar | Identified 11 people, seized 11 devices |
| Estonia | Seized 80GB+ of server data |

## Results and Impact

| Metric | Value |
|--------|-------|
| Countries participating | 95 |
| Suspicious IPs identified | ~30,000 |
| IPs taken down | ~22,800 (76%) |
| Servers seized | 59 |
| Electronic devices seized | 43 |
| Arrests | 41 |
| Under investigation | 65 |

## Cooperation Mechanisms Used

- INTERPOL's I-24/7 secure communications network
- Public-private intelligence sharing with cybersecurity companies
- INTERPOL Cyber Fusion Centre threat intelligence aggregation
- National Central Bureaus (NCBs) in 95 countries

## Korean Involvement (한국의 참여)

No specific Korean involvement was noted in the published results of Operation Synergia II.

## Contradictions & Open Questions

- What is the breakdown of the 41 arrests by country?
- What follow-up actions were taken against the 65 individuals under investigation?
- How was the threat intelligence from private sector partners integrated into operational planning?
- What was the long-term impact on the phishing/ransomware infrastructure that was taken down?

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | INTERPOL cyber operation takes down 22,000 malicious IP addresses — Operation Synergia II | INTERPOL | 2024-11-06 | [원본](https://www.interpol.int/News-and-Events/News/2024/INTERPOL-cyber-operation-takes-down-22-000-malicious-IP-addresses) |
| [2] | Supplementary source | kaspersky.com | - | [원본](https://www.kaspersky.com/about/press-releases/kaspersky-shares-cyberthreat-data-with-interpol-in-operation-to-disrupt-transnational-cybercrime) |
