---
type: operation
title: "Operation NightFury (Magecart/GetBilling)"
title_ko: "나이트퓨리 작전 (Magecart/GetBilling)"
aliases: ["Operation Night Fury", "Magecart Indonesia arrest", "GetBilling operation"]
case_id: "CYB-2020-051"
period: 2
operation_type: "arrest-sweep"
status: "completed"
enforcement_type:
  - "arrest"
outcome: "success"
timeframe:
  announced: "2020-01-24"
  start: "2020-01-24"
  end: "2020-01-24"
  ongoing: false
crime_type: "[[online-fraud-ic]]"
target_entity: "Magecart/GetBilling web skimming group"
lead_agency: "[[interpol]]"
coordinating_body: "[[interpol]]"
participating_countries:
  - "[[indonesia]]"
  - "[[singapore]]"
participating_agencies:
  - "[[interpol]]"
  - "[[indonesia-police]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 3
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "3 Indonesian nationals arrested for Magecart web skimming"
    - "GetBilling JavaScript skimmer infrastructure disrupted"
    - "Group-IB provided private sector intelligence"
edges:
  - source_actor: "INTERPOL"
    target_actor: "Indonesia Police"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
  - source_actor: "Group-IB"
    target_actor: "INTERPOL"
    cooperation_type: "technical_assistance"
    legal_basis: "unknown"
    direction: "directed"
credibility_index: 2.55
source_tier: 3
missing_fields:
  - "legal_basis"
  - "mechanisms_used"
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "INTERPOL-coordinated operations can successfully target cybercriminals in Southeast Asia"
  - "Private sector threat intelligence (Group-IB) can directly support law enforcement operations"
source_count: 2
sources:
  - "tier3-cyberscoop-magecart-nightfury-2020"
  - "tier3-groupib-nightfury-2020"
created: 2026-04-08
updated: 2026-04-08
---

> [!note] This operation is documented from a Tier 3 (cybersecurity media) source. Additional verification from official sources (Tier 1-2) would strengthen data reliability.

## Summary

**Operation NightFury** was an INTERPOL-coordinated operation that resulted in the arrest of **3 Indonesian nationals** involved in **Magecart**-style web skimming attacks using the **GetBilling** JavaScript skimmer. The operation involved cooperation between INTERPOL, Indonesian law enforcement, and private sector cybersecurity firm **Group-IB**, which provided critical intelligence.

The arrests represented a significant action against Magecart-type web skimming groups operating in Southeast Asia.

## Background

Magecart is an umbrella term for cybercriminal groups and techniques that involve injecting malicious JavaScript code into e-commerce websites to steal payment card data during checkout. The GetBilling variant was a specific skimmer tool used by the arrested suspects. The suspects compromised hundreds of e-commerce websites to steal credit card details from unsuspecting shoppers.

## Participating Parties

### Coordinating Body
- [[interpol|INTERPOL]]

### Participating Countries
- [[indonesia|Indonesia]]
- [[singapore|Singapore]]

### Private Sector Support
- Group-IB (threat intelligence and technical analysis)

## Legal Framework

Specific legal instruments not detailed in Tier 3 sources.

## Operational Timeline

| Date | Event |
|------|-------|
| Pre-2020 | Investigation with Group-IB intelligence support |
| 2020-01-24 | 3 arrests in Indonesia announced |

## Results and Impact

| Metric | Count |
|--------|-------|
| Arrests | 3 |
| Countries involved | 2 (+ INTERPOL coordination) |

## Cooperation Mechanisms Used

INTERPOL coordination with local law enforcement, supported by private sector threat intelligence from Group-IB.

## Korean Involvement (한국의 참여)

No Korean involvement identified. South Korean e-commerce sites could potentially be targets of Magecart-style attacks.

## Contradictions & Open Questions

- How many websites were compromised by the GetBilling group?
- How much financial loss was attributed to the group?
- Were the suspects convicted and sentenced?
- What was Singapore's specific role in the operation?

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Source 1 | group-ib.com | - | [원본](https://www.group-ib.com/media-center/press-releases/night-fury/) |
| [2] | Source 2 | cyberscoop.com | - | [원본](https://cyberscoop.com/magecart-arrest-indonesia-interpol-getbilling/) |