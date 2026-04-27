---
type: operation
title: "Carbanak/Cobalt Mastermind Arrest"
title_ko: "Carbanak/Cobalt 조직 핵심 인물 체포"
aliases:
  - "Carbanak Cobalt Takedown"
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
target_entity: "Carbanak/Cobalt cybercrime group"
lead_agency: "[[spanish-national-police]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[spain]]"
  - "[[united-states]]"
  - "[[romania]]"
participating_agencies:
  - "[[spanish-national-police]]"
  - "[[europol-ec3]]"
  - "[[fbi]]"
  - "[[romanian-police]]"
  - "[[kaspersky-lab]]"
legal_basis:
  []
mechanisms_used:
  - "[[informal-cooperation]]"
related_cases:
  []
related_operations:
  []
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
  - source_actor: "Spanish National Police"
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
  - "[[2015-02-16_securelist_the-great-bank-robbery-the-carbanak-apt]]"
  - "[[2026-04-18_europol-europa-eu_carbanak-cobalt-infographic]]"
  - "[[2018-08-01_fbi-gov_how-cyber-crime-group-fin7-attacked-and-stole-data-from-hundreds-of-us-companies]]"
  - "[[2018-03-26_securityweek_ukrainian-suspected-leading-carbanak-gang-arrested-spain]]"
summary: "Spanish authorities, supported by Europol and other international partners, arrested the alleged mastermind behind the Carbanak/Cobalt bank-fraud campaigns in Spain. The arrest narrative is official; the technical understanding of the campaign still depends heavily on Kaspersky's earlier reporting."
created: 2026-04-08
updated: 2026-04-27
---
## Summary

Spanish authorities, supported by Europol and other international partners, arrested the alleged mastermind behind the Carbanak/Cobalt bank-fraud campaigns in Spain. The arrest narrative is official; the technical understanding of the campaign still depends heavily on Kaspersky's earlier reporting.

> [!note] Audit Note — Participating Countries (2026-04-21)
> Belarus, Moldova, and Taiwan were removed from `participating_countries` after a tier-1 source cross-check: the Europol Carbanak/Cobalt PDF (1.1 MB), BBC, Reuters, and Kaspersky's Securelist writeup all fail to name any of the three as operational participants (targeting / victim geography was discussed, not LE contribution). Retained countries — Spain (lead), United States (FBI), Romania — are each explicitly named in multiple primary sources.

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

## Cooperation And Legal Analysis

This page deliberately separates two evidence layers. Europol and the Spanish-police reporting establish the arrest and partner set. Kaspersky's report explains the attack chain, including spear-phishing, lateral movement, internal-bank compromise and ATM cash-out behavior. Mixing those layers without distinction would make the page less transparent.

Another integrity issue is identity. The current source set used by this repo does not cleanly establish a defendant name from an official charging document. To avoid contaminating the dataset, the page keeps the suspect unidentified rather than lifting a disputed or weakly sourced identity from secondary reporting.

## Follow-Up Actions

> [!warning] No public court documents found
> The repo currently has strong public reporting for the arrest event and campaign mechanics, but not a robust public docket set for the post-arrest prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2018-03-01: Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain.
- Kaspersky Securelist, 2015-02-16: The Great Bank Robbery: the Carbanak APT.
- Europol, 2026-04-18: Carbanak / Cobalt infographic.
- FBI, 2018-08-01: How Cyber Crime Group FIN7 Attacked and Stole Data from Hundreds of U.S. Companies.
- SecurityWeek, 2018-03-26: Ukrainian Suspected of Leading Carbanak Gang Arrested in Spain.

## Operational Timeline

- 2013: activity or investigation start.
- 2018-03: public announcement.
- 2018-03: reported enforcement endpoint.
- 2015-02-16: public source coverage from Kaspersky Securelist.
- 2018-03-01: public source coverage from Europol.
- 2018-03-26: public source coverage from SecurityWeek.
- 2018-08-01: public source coverage from FBI.
- 2026-04-18: public source coverage from Europol.

## Evidence and Attribution Notes

- The Spanish National Police, in cooperation with Europol, the FBI, Romanian police, Belarusian police, and Taiwanese authorities, arrested the mastermind behind the Carbanak and Cobalt malware campaigns in Spain.
- The suspect led a cybercrime group that had used Carbanak, Cobalt, and Anunak malware to steal over EUR 1 billion from more than 100 financial institutions across 40+ countries since 2013.
- Private cybersecurity firms including Kaspersky contributed to the investigation.
- Kaspersky documented the Carbanak campaign as a financially motivated intrusion set targeting banks directly rather than retail banking customers.
- The report estimated losses up to USD 1 billion across roughly 100 financial institutions and described the group's spear-phishing, lateral movement and ATM cash-out methods.
- The report is the key technical source for the malware and intrusion tradecraft later cited by Europol and other official bodies.
- This Kaspersky technical report is the foundational public description of the Carbanak campaign.
- It lays out the intrusion chain, identifies the direct-bank-targeting model, and explains why law-enforcement claims about scale and modus operandi in 2018 were credible.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- FBI, 2018-01-01: Since at least 2015, FIN7 members engaged in a highly sophisticated malware campaign targeting more than 100 U.S.
- FBI, 2018-01-01: View larger and download Network Intrusion: Control and Data Exfiltration Once infected, the compromised victim computer connected to one of FIN7’s command and control servers located throughout the world.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a joint-investigation against Carbanak/Cobalt cybercrime group, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Spanish National Police and coordination to Europol Ec3, with participating or affected jurisdictions recorded as Spain, United States, Romania.

The cooperation model is documented through named agencies and partners: Spanish National Police, Europol Ec3, Fbi, Romanian Police, Kaspersky Lab; mechanisms: informal cooperation; enforcement posture: Arrest.

Operational results captured for the canonical record: 1 arrests; 100+ financial institutions in 40+ countries targeted; EUR 1 billion+ in losses publicly attributed to the campaign.

The canonical source set contains 5 reference(s): 2018 03 01 Europol Europa Eu Mastermind Behind Eur 1 Billion Cyber Bank Robbery Arrested In Spain, 2015 02 16 Securelist The Great Bank Robbery The Carbanak Apt, 2026 04 18 Europol Europa Eu Carbanak Cobalt Infographic, 2018 08 01 Fbi Gov How Cyber Crime Group Fin7 Attacked And Stole Data From Hundreds Of Us Companies, 2018 03 26 Securityweek Ukrainian Suspected Leading Carbanak Gang Arrested Spain.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain | Europol | 2018-03-01 | https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain |
| [2] | The Great Bank Robbery: the Carbanak APT | Kaspersky Securelist | 2015-02-16 | https://securelist.com/the-great-bank-robbery-the-carbanak-apt/68732/ |
| [3] | Carbanak / Cobalt infographic | Europol | 2026-04-18 | https://www.europol.europa.eu/cms/sites/default/files/documents/carbanakcobalt.pdf |
| [4] | How Cyber Crime Group FIN7 Attacked and Stole Data from Hundreds of U.S. Companies | FBI | 2018-08-01 | https://www.fbi.gov/contact-us/field-offices/seattle/news/stories/how-cyber-crime-group-fin7-attacked-and-stole-data-from-hundreds-of-us-companies |
| [5] | Ukrainian Suspected of Leading Carbanak Gang Arrested in Spain | SecurityWeek | 2018-03-26 | https://www.securityweek.com/ukrainian-suspected-leading-carbanak-gang-arrested-spain/ |
