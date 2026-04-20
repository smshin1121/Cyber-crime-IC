---
type: operation
title: Carbanak/Cobalt Mastermind Arrest
title_ko: Carbanak/Cobalt 조직 핵심 인물 체포
aliases:
  - Carbanak Cobalt Takedown
case_id: CYB-2018-001
period: 1
operation_type: joint-investigation
operation_role: umbrella
parent_operation: ""
status: completed
enforcement_type:
  - arrest
outcome: success
timeframe:
  announced: 2018-03
  start: 2013
  end: 2018-03
  ongoing: false
crime_type: "[[malware-ic]]"
crime_types:
  - "[[malware-ic]]"
target_entity: Carbanak/Cobalt cybercrime group
lead_agency: "[[spanish-national-police]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[spain]]"
  - "[[united-states]]"
  - "[[romania]]"
  - "[[moldova]]"
  - "[[belarus]]"
  - "[[taiwan]]"
participating_agencies:
  - "[[spanish-national-police]]"
  - "[[europol-ec3]]"
  - "[[fbi]]"
  - "[[romanian-police]]"
  - "[[kaspersky-lab]]"
legal_basis: []
mechanisms_used:
  - "[[informal-cooperation]]"
related_cases: []
related_operations: []
results:
  arrests: 1
  servers_seized: 0
  domains_seized: 0
  indictments: 0
  decryption_keys_recovered: 0
  victims_notified: 0
  cryptocurrency_seized: ""
  other:
    - "100+ financial institutions in 40+ countries targeted"
    - "EUR 1 billion+ in losses publicly attributed to the campaign"
edges:
  - source_actor: Spanish National Police
    target_actor: Europol
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 3.5
source_tier: 2
source_count: 5
sources:
  - "[[2018-03-01_europol-europa-eu_mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain]]"
  - "[[europol-carbanakcobalt-mastermind-arrest]]"
  - "[[2015-02-16_securelist_the-great-bank-robbery-the-carbanak-apt]]"
  - "[[2026-04-18_europol-europa-eu_carbanak-cobalt-infographic]]"
  - "[[2018-08-01_fbi-gov_how-cyber-crime-group-fin7-attacked-and-stole-data-from-hundreds-of-us-companies]]"
summary: "Spanish authorities, supported by Europol and other international partners, arrested the alleged mastermind behind the Carbanak/Cobalt bank-fraud campaigns in Spain. The arrest narrative is official; the technical understanding of the campaign still depends heavily on Kaspersky's earlier reporting."
created: 2026-04-08
updated: 2026-04-18
---
## Summary

Spanish authorities, supported by Europol and other international partners, arrested the alleged mastermind behind the Carbanak/Cobalt bank-fraud campaigns in Spain. The arrest narrative is official; the technical understanding of the campaign still depends heavily on Kaspersky's earlier reporting.

## Why The Operation Matters

Carbanak/Cobalt matters because it sits at the intersection of financial intrusion, bank fraud and cross-border law enforcement. Public sources consistently describe the campaign as targeting financial institutions directly rather than merely stealing consumer credentials.

## Participating Parties

**Lead and coordination:**
- [[spanish-national-police|Spanish National Police]]
- [[europol-ec3|Europol EC3]]

**Named partners in public reporting:**
- [[fbi]]
- Romanian authorities
- Moldovan authorities
- Belarusian authorities
- Taiwanese authorities
- [[kaspersky-lab|Kaspersky Lab]] as a private-sector technical contributor

## Results

- 1 alleged mastermind arrested in Spain
- campaign publicly associated with EUR 1 billion+ in losses
- more than 100 financial institutions in 40+ countries affected according to the source set

## Cooperation And Legal Analysis

This page deliberately separates two evidence layers. Europol and the Spanish-police reporting establish the arrest and partner set. Kaspersky's report explains the attack chain, including spear-phishing, lateral movement, internal-bank compromise and ATM cash-out behavior. Mixing those layers without distinction would make the page less transparent.

Another integrity issue is identity. The current source set used by this repo does not cleanly establish a defendant name from an official charging document. To avoid contaminating the dataset, the page keeps the suspect unidentified rather than lifting a disputed or weakly sourced identity from secondary reporting.

## Follow-Up Actions

> [!warning] No public court documents found
> The repo currently has strong public reporting for the arrest event and campaign mechanics, but not a robust public docket set for the post-arrest prosecution.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| 1 | Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain | Europol | 2018-03-01 | https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain |
| 2 | Europol: Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain (Carbanak/Cobalt) | repo source page | 2026-04-10 | [[europol-carbanakcobalt-mastermind-arrest]] |
| 3 | The Great Bank Robbery: the Carbanak APT | Kaspersky Securelist | 2015-02-16 | https://securelist.com/the-great-bank-robbery-the-carbanak-apt/68732/ |
| 4 | Carbanak / Cobalt infographic | Europol | current | https://www.europol.europa.eu/cms/sites/default/files/documents/carbanakcobalt.pdf |
| 5 | How Cyber Crime Group FIN7 Attacked and Stole Data from Hundreds of U.S. Companies | FBI | 2018-08-01 | https://www.fbi.gov/contact-us/field-offices/seattle/news/stories/how-cyber-crime-group-fin7-attacked-and-stole-data-from-hundreds-of-us-companies |
