---
type: operation
title: "Operation Chakra-IV"
aliases:
  - "Operation Chakra 4"
  - "Chakra-IV"
  - "Chakra 4"
case_id: CYB-2025-021
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search
  - seizure
outcome: success
timeframe:
  announced: 2025-02-18
  start: 2025-02-12
  end: 2025-02-18
  ongoing: false
crime_type: "[[online-fraud-ic]]"
target_entity: "India-based remote-support and virtual-asset fraud network targeting German nationals"
lead_agency: "[[cbi-india]]"
coordinating_body: "[[cbi-india]]"
participating_countries:
  - "[[india]]"
  - "[[germany]]"
participating_agencies:
  - "[[cbi-india]]"
  - "[[interpol]]"
legal_basis:
  - "Indian Penal Code fraud and forgery provisions"
  - "Information Technology Act 2000 section 66D"
  - "[[informal-cooperation]]"
mechanisms_used:
  - "[[informal-cooperation]]"
  - "INTERPOL channels"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Six locations searched across Delhi, Kolkata, and Siliguri."
    - "Illegal call center at Webel IT Park, Matigara, Darjeeling dismantled."
    - "24 hard disks, seven mobile phones, one laptop, and documents recovered."
    - "Public reporting attributes EUR 646,032 in alleged German-victim transfers to cryptocurrency wallets controlled by the accused."
edges:
  - source_actor: "CBI India"
    target_actor: "German authorities"
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: "CBI India"
    target_actor: "INTERPOL"
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 3.0
source_tier: 3
missing_fields:
  - complete_german_partner_agency
related_cases: []
related_operations:
  - "[[operation-chakra-ii]]"
  - "[[operation-chakra-iii]]"
  - "[[operation-chakra-v]]"
challenges_encountered: []
lessons_learned:
  - "Remote-support fraud and virtual-asset laundering can require coordinated evidence development across victim and enforcement jurisdictions."
source_count: 3
sources:
  - "[[2025-02-18_freepressjournal_operation-chakra-iv-german-tech-support-scam]]"
  - "[[2025-02-18_newindianexpress-com_operation-chakra-iv-cbi-dismantles-virtual-asset-supported-network-targeting-german-nationals]]"
  - "[[2025-02-18_fintechbiznews-com_cbi-dismantles-virtual-asset-supported-transnational-cyber-crime-network]]"
created: 2026-05-05
updated: 2026-05-08
operation_role: umbrella
parent_operation: ""
summary: "Operation Chakra-IV was a CBI-led action, coordinated with German authorities and using INTERPOL channels, against a virtual-asset-supported cybercrime network targeting German nationals through remote-support and call-center fraud."
jurisdictions:
  - "[[india]]"
  - "[[germany]]"
organizations:
  - "[[cbi-india]]"
  - "[[interpol]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[voice-phishing-ic]]"
---
## Summary

Operation Chakra-IV was a CBI-led action against a virtual-asset-supported cybercrime network targeting German nationals. Public reporting says CBI coordinated closely with German authorities, registered the case on **12 February 2025**, searched six locations from **14 to 17 February 2025**, arrested one key accused, and dismantled an illegal call center in West Bengal.

## International Cooperation Details

The source identifies German authorities as cooperation partners and says the operation leveraged INTERPOL channels. The exact German agency is not named in the current source, so the structured agency list records CBI and INTERPOL while leaving the German agency as a metadata gap.

## Results

| Metric | Result |
|---|---:|
| Arrests | 1 |
| Locations searched | 6 |
| Illegal call centers dismantled | 1 |
| Hard disks recovered | 24 |
| Mobile phones recovered | 7 |
| Alleged German-victim transfers | EUR 646,032 |

## Scope Note

This page is included under [[voice-phishing-ic]] because the public source describes an illegal call center and remote-support impersonation pattern. It also remains within [[online-fraud-ic]] because the conduct is broader cyber-enabled financial fraud.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | CBI Dismantles Global Cybercrime Network Targeting Germans Since 2021 In Operation Chakra-IV | Free Press Journal | 2025-02-18 | https://www.freepressjournal.in/india/cbi-dismantles-global-cybercrime-network-targeting-germans-since-2021-in-operation-chakra-iv |
| [2] | Operation Chakra IV: CBI dismantles virtual asset-supported cybercrime network targeting German nationals | The New Indian Express | 2025-02-18 | https://www.newindianexpress.com/nation/2025/Feb/18/operation-chakra-iv-cbi-dismantles-virtual-asset-supported-cybercrime-network-targeting-german-nationals |
| [3] | CBI Dismantles Virtual Asset Supported Transnational Cyber Crime Network | FinTech BizNews | 2025-02-18 | https://fintechbiznews.com/govtregulators-authorities/cbi-dismantles-virtual-asset-supported-transnational-cyber-crime-network- |
