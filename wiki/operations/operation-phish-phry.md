---
type: operation
title: "Operation Phish Phry"
title_ko: "Operation Phish Phry"
aliases:
  - "Phish Phry"
case_id: CYB-2009-001
period: 1
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
  - indictment
  - prosecution
outcome: success
timeframe:
  announced: 2009-10-07
  start: 2007
  end: 2009-10-07
  ongoing: false
crime_type: "[[online-fraud-ic]]"
target_entity: "U.S.-Egypt phishing and money-mule network"
lead_agency: "[[fbi-cyber-division|FBI]]"
coordinating_body: "[[fbi-cyber-division|FBI Los Angeles]]"
participating_countries:
  - "[[united-states]]"
  - "[[egypt]]"
participating_agencies:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj]]"
  - "[[us-secret-service]]"
  - "U.S. Attorney's Office for the Central District of California"
  - "Electronic Crimes Task Force in Los Angeles"
  - "Egyptian law enforcement authorities"
legal_basis:
  - "[[electronic-evidence]]"
  - "[[mutual-legal-assistance]]"
  - "[[search-seizure]]"
mechanisms_used:
  - "[[electronic-evidence]]"
  - "[[mutual-legal-assistance]]"
  - "[[informal-cooperation]]"
results:
  arrests: 33
  indictments: 100
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "53 defendants named in a U.S. federal indictment in Los Angeles"
    - "47 suspects charged or identified by Egyptian authorities"
    - "FBI described the matter as the first joint cyber investigation between Egyptian law enforcement authorities and U.S. officials"
    - "Victims were customers of U.S. financial institutions including Bank of America and Wells Fargo"
    - "About USD 1.5 million in fraudulent transfers identified in public reporting"
edges:
  - source_actor: "FBI Los Angeles"
    target_actor: "Egyptian law enforcement authorities"
    cooperation_type: joint_investigation
    legal_basis: electronic_evidence
    direction: undirected
  - source_actor: "U.S. prosecutors"
    target_actor: "Egyptian authorities"
    cooperation_type: parallel_charging
    legal_basis: mutual_legal_assistance
    direction: undirected
credibility_index: 4.2
source_tier: 1
missing_fields:
  - final_egyptian_court_outcomes
  - complete_sentencing_results_for_all_defendants
related_cases: []
related_operations:
  - "[[operation-wirewire]]"
  - "[[operation-rewired]]"
challenges_encountered:
  - "Phishing actors in Egypt and money mules in the United States split the credential theft and cash-out roles across borders."
  - "The victim population and financial institutions were U.S.-based while credential theft activity and profit transfers crossed into Egypt."
lessons_learned:
  - "Early phishing operations already required parallel foreign charges and U.S. money-mule arrests."
  - "Financial-fraud cybercrime records should separate the credential-theft layer from the domestic cash-out and money-laundering layer."
source_count: 4
sources:
  - "[[2009-10-07_fbi_operation-phish-phry]]"
  - "[[2009-10-07_fbi-losangeles_operation-phish-phry]]"
  - "[[2009-10-07_wired_phish-phry]]"
  - "[[2009-10-07_pcworld_operation-phish-phry]]"
created: 2026-05-07
updated: 2026-05-07
operation_role: umbrella
parent_operation: ""
summary: "Operation Phish Phry was a 2007-2009 U.S.-Egypt joint phishing investigation announced on 7 October 2009. FBI and FBI Los Angeles materials describe it as the first joint cyber investigation between Egyptian law enforcement authorities and U.S. officials, with 53 U.S. defendants, 47 Egyptian suspects, 33 U.S. arrests on the announcement date, and about USD 1.5 million in fraudulent transfers tied to phishing of U.S. bank customers."
jurisdictions:
  - "[[united-states]]"
  - "[[egypt]]"
organizations:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj]]"
  - "[[us-secret-service]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[bank-fraud-ic]]"
  - "[[identity-theft]]"
  - "[[money-laundering-ic]]"
---
## Summary

Operation Phish Phry was a U.S.-Egypt joint investigation into a phishing and money-mule network that targeted U.S. bank customers. FBI public materials describe it as one of the largest cyber-fraud phishing cases of its time and as the first joint cyber investigation between Egyptian law enforcement authorities and U.S. officials.

The public record describes a two-layer scheme. Egypt-based actors allegedly sent phishing emails and collected banking credentials from U.S. victims. U.S.-based co-conspirators allegedly recruited runners to open accounts at U.S. banks, receive fraudulent transfers, withdraw the funds, and send a portion back to Egypt.

## Cooperation Model

The operation began in 2007 when FBI agents and U.S. financial institutions investigated sophisticated criminal enterprises targeting U.S. financial infrastructure. FBI Los Angeles later reported that intelligence prompted FBI and Egyptian authorities to pursue a joint investigation into Egypt-based subjects after investigators in both countries uncovered the cross-border conspiracy.

The public announcement identified U.S. authorities, the FBI legal attache in Cairo, and Egyptian law enforcement authorities. That makes the matter a qualifying international-cooperation operation under the wiki's two-country rule.

## Results

| Metric | Public figure |
|---|---:|
| U.S. federal defendants | 53 |
| Egyptian suspects charged or identified | 47 |
| U.S. arrests on announcement date | 33 |
| Approximate fraudulent transfers identified | USD 1.5M |
| U.S. federal indictment counts | 51 |

The U.S. indictment charged conspiracy to commit wire fraud and bank fraud, with additional counts including bank fraud, aggravated identity theft, computer-fraud conspiracy, unauthorized access to protected computers, and domestic and international money laundering.

## Boundary Notes

This page is the canonical operation record for the U.S.-Egypt phishing investigation. It should not be merged with later BEC sweeps such as [[operation-wirewire|Operation WireWire]] or [[operation-rewired|Operation reWired]], which involved different conduct, dates, participants, and enforcement phases.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2009-10-07_fbi_operation-phish-phry|Operation 'Phish Phry']] | FBI | 2009-10-07 | https://archives.fbi.gov/archives/news/stories/2009/october/phishphry_100709 |
| [2] | [[2009-10-07_fbi-losangeles_operation-phish-phry|One Hundred Linked to International Computer Hacking Ring Charged by United States and Egypt in Operation Phish Phry]] | FBI Los Angeles | 2009-10-07 | https://archives.fbi.gov/archives/losangeles/press-releases/2009/la100709-1.htm |
| [3] | [[2009-10-07_wired_phish-phry|Gang of 100 Phishers Charged in U.S., Egypt]] | Wired | 2009-10-07 | https://www.wired.com/2009/10/phish-phry/ |
| [4] | [[2009-10-07_pcworld_operation-phish-phry|Operation Phish Phry Nets 100 Suspects]] | PCWorld | 2009-10-07 | https://www.pcworld.com/article/520019/operation_phish_phry_nets_100_suspects.html |
