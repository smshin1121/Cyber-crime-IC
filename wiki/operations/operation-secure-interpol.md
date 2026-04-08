---
type: operation
title: "Operation Secure (INTERPOL Infostealer Crackdown)"
aliases: ["Operation Secure", "INTERPOL Infostealer Operation"]
case_id: "CYB-2025-012"
period: 3
operation_type: "infrastructure-seizure"
status: "completed"
enforcement_type:
  - "arrest"
  - "takedown"
  - "seizure"
outcome: "success"
credibility_index: 1.85
source_tier: 2
edges:
  - source_actor: "INTERPOL"
    target_actor: "Asia-Pacific LEAs"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
  - source_actor: "Group-IB"
    target_actor: "INTERPOL"
    cooperation_type: "info_sharing"
    legal_basis: "informal"
    direction: "directed"
  - source_actor: "Kaspersky"
    target_actor: "INTERPOL"
    cooperation_type: "info_sharing"
    legal_basis: "informal"
    direction: "directed"
  - source_actor: "Trend Micro"
    target_actor: "INTERPOL"
    cooperation_type: "info_sharing"
    legal_basis: "informal"
    direction: "directed"
missing_fields:
  - "legal_basis"
  - "mechanisms_used"
  - "individual_country_results"
  - "cryptocurrency_seized"
timeframe:
  announced: "2025-04-01"
  start: "2025-01-01"
  end: "2025-04-30"
  ongoing: false
crime_type: "[[hacking-ic]]"
target_entity: "Infostealer malware infrastructure and operators across Asia-Pacific"
lead_agency: "[[interpol-igci]]"
coordinating_body: "[[interpol-igci]]"
participating_countries:
  - "[[brunei]]"
  - "[[cambodia]]"
  - "[[fiji]]"
  - "[[hong-kong]]"
  - "[[india]]"
  - "[[indonesia]]"
  - "[[japan]]"
  - "[[kazakhstan]]"
  - "[[south-korea]]"
  - "[[laos]]"
  - "[[malaysia]]"
  - "[[maldives]]"
  - "[[nepal]]"
  - "[[papua-new-guinea]]"
  - "[[philippines]]"
  - "[[samoa]]"
  - "[[singapore]]"
  - "[[solomon-islands]]"
  - "[[sri-lanka]]"
  - "[[thailand]]"
  - "[[timor-leste]]"
  - "[[tonga]]"
  - "[[vanuatu]]"
  - "[[vietnam]]"
participating_agencies:
  - "[[interpol-igci]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 32
  indictments: 0
  servers_seized: 41
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 216000
  other:
    - "20,000+ malicious IPs and domains taken down"
    - "100GB+ of data seized"
    - "26 countries participated"
related_cases: []
related_operations:
  - "[[operation-synergia-ii]]"
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "[[2025-04-01-interpol-operation-secure-infostealer]]"
created: 2026-04-08
updated: 2026-04-08
---

# Operation Secure (INTERPOL Infostealer Crackdown)

## Summary

Operation Secure was an INTERPOL-led operation conducted from January to April 2025 across 26 Asia-Pacific countries, targeting infostealer malware infrastructure. The operation resulted in 32 arrests, the takedown of over 20,000 malicious IPs and domains, the seizure of 41 servers and 100GB+ of data, and notifications to more than 216,000 victims.

This operation focused specifically on information-stealing malware (infostealers) which harvest credentials, financial data, and personal information from infected systems. Private sector intelligence from Group-IB, Kaspersky, and Trend Micro supported the operation.

> [!note] Naming disambiguation
> This operation should not be confused with the Council of Europe's "Operation SECURE" capacity-building exercise (row 6 of Excel data), which was a training programme, not an enforcement operation.

## Background

Infostealers represent a growing cybercrime threat, serving as the initial access vector for ransomware, fraud, and identity theft operations. INTERPOL's Asia-Pacific cyber operations desk coordinated this region-wide crackdown as a successor to the [[operation-synergia-ii|Operation Synergia II]] model of large-scale infrastructure takedowns.

## Participating Parties

### Law Enforcement
- **Lead**: [[interpol-igci|INTERPOL]] (Asia-South Pacific Cybercrime Operations Desk)
- **26 countries**: Brunei, Cambodia, Fiji, Hong Kong (China), India, Indonesia, Japan, Kazakhstan, [[south-korea|South Korea]], Laos, Macau (China), Malaysia, Maldives, Nauru, Nepal, Papua New Guinea, Philippines, Samoa, Singapore, Solomon Islands, Sri Lanka, Thailand, Timor-Leste, Tonga, Vanuatu, Vietnam

### Private Sector Partners
- Group-IB
- Kaspersky
- Trend Micro

## Results and Impact

| Metric | Value |
|--------|-------|
| Arrests | 32 |
| Servers seized | 41 |
| Malicious IPs/domains taken down | 20,000+ |
| Data seized | 100GB+ |
| Victims notified | 216,000+ |
| Countries | 26 |

## Cooperation Mechanisms Used

> [!warning] Missing data
> Specific legal frameworks and cooperation mechanisms not detailed in available source. Likely INTERPOL I-24/7 network and bilateral cooperation agreements.

## Korean Involvement (한국의 참여)

South Korea (대한민국) was among the 26 participating countries. Specific Korean contributions (arrests, infrastructure actions) are not detailed in the available source.

## Contradictions & Open Questions

- Per-country breakdown of arrests and infrastructure actions not disclosed.
- Macau (China) and Kiribati mentioned in some source data but not confirmed in primary source.
- Legal basis for cross-border data sharing across 26 jurisdictions not specified.

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Source 1 | straitstimes.com | - | [원본](https://www.straitstimes.com/singapore/more-than-9000-malware-infected-servers-found-by-singapore-based-interpol-operation) |
| [2] | Source 2 | freemalaysiatoday.com | - | [원본](https://www.freemalaysiatoday.com/category/nation/2017/04/24/interpol-finds-9000-compromised-websites) |
