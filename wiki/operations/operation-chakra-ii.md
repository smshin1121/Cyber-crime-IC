---
type: operation
title: "Operation Chakra-II"
aliases:
  - "Operation Chakra-2"
  - "Chakra-II"
  - "Chakra 2"
case_id: CYB-2023-019
period: 3
operation_type: search-sweep
status: completed
enforcement_type:
  - search
  - seizure
outcome: success
timeframe:
  announced: 2023-10-19
  start: 2023-10-19
  end: 2023-10-19
  ongoing: false
crime_type: "[[online-fraud-ic]]"
target_entity: "Cyber-enabled financial-fraud and tech-support scam call-center infrastructure in India"
lead_agency: "[[cbi-india]]"
coordinating_body: "[[cbi-india]]"
participating_countries:
  - "[[india]]"
  - "[[united-states]]"
participating_agencies:
  - "[[cbi-india]]"
  - "[[fbi-cyber-division]]"
  - "[[interpol]]"
  - "[[microsoft]]"
legal_basis:
  - "Indian domestic cybercrime and fraud authorities"
  - "[[informal-cooperation]]"
mechanisms_used:
  - "[[informal-cooperation]]"
  - "[[public-private-cooperation]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "CBI searched 76 locations across India."
    - "Nine call centers were searched."
    - "Two cases involved complaints by Amazon and Microsoft about call centers posing as technical support for foreign nationals."
edges:
  - source_actor: "CBI India"
    target_actor: "FBI"
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: "CBI India"
    target_actor: "INTERPOL"
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: "CBI India"
    target_actor: "Microsoft"
    cooperation_type: public_private_cooperation
    legal_basis: informal
    direction: undirected
credibility_index: 2.2
source_tier: 3
missing_fields:
  - arrest_count
  - full_foreign_partner_list
related_cases: []
related_operations:
  - "[[operation-chakra-iii]]"
  - "[[operation-chakra-iv]]"
  - "[[operation-chakra-v]]"
challenges_encountered: []
lessons_learned:
  - "Private-sector complaints and foreign law-enforcement intelligence can trigger domestic search action against call-center fraud infrastructure."
source_count: 1
sources:
  - "[[2023-10-19_ndtv_operation-chakra-ii-cbi-raids-76-locations]]"
created: 2026-05-05
updated: 2026-05-05
operation_role: umbrella
parent_operation: ""
summary: "Operation Chakra-II was a CBI-led search sweep against cyber-enabled financial-fraud infrastructure in India. Public reporting described 76 searches, nine call centers searched, and foreign-law-enforcement and private-sector inputs including FBI, INTERPOL, Microsoft, and Amazon-related complaint material."
jurisdictions:
  - "[[india]]"
  - "[[united-states]]"
organizations:
  - "[[cbi-india]]"
  - "[[fbi-cyber-division]]"
  - "[[interpol]]"
  - "[[microsoft]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[voice-phishing-ic]]"
---
## Summary

Operation Chakra-II was a CBI-led search sweep against cyber-enabled financial-fraud infrastructure in India. Public reporting described **76 searches** after five cyber-enabled financial-fraud cases were registered. Two cases involved call centers allegedly posing as Amazon and Microsoft technical support for foreign nationals, and CBI searched **nine call centers**.

## International Cooperation Details

The available public source says CBI acted on inputs from FIU, FBI, INTERPOL, and other international agencies. The current structured country list is conservative: it records India as the enforcement jurisdiction and the United States because FBI and Microsoft-related inputs are explicitly named. The workbook sample lists a broader partner set, but those additional countries should be treated as review candidates until stronger source support is collected.

## Results

| Metric | Result |
|---|---:|
| Locations searched | 76 |
| Call centers searched | 9 |
| Publicly confirmed arrests | Not disclosed in current source |

## Scope Note

This page is included under [[voice-phishing-ic]] because the source describes technical-support call-center impersonation targeting foreign nationals. It should not be read as proof that every Operation Chakra-II case involved a voice call; it records the call-center subset relevant to VOIP/phone-enabled fraud analysis.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | CBI Launches Operation Chakra-2 Against Cyber Crime, Raids 76 Locations | NDTV / Press Trust of India | 2023-10-19 | https://www.ndtv.com/india-news/cbi-launches-operation-chankra-2-against-cyber-crime-raids-76-locations-4496354 |
