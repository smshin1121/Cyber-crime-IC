---
type: operation
title: "Operation Trident Breach"
aliases:
  - "FBI Operation Trident Breach"
  - "Trident Breach"
  - "Jabber Zeus Trident Breach"
case_id: CYB-2010-001
period: 1
operation_role: umbrella
parent_operation: ""
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
  - search-and-seizure
  - indictment
  - intelligence-sharing
outcome: success
timeframe:
  announced: 2010-10-01
  start: 2009-05
  end: 2010-10-01
  ongoing: false
crime_type: "[[banking-trojan-ic]]"
crime_types:
  - "[[banking-trojan-ic]]"
  - "[[malware-ic]]"
  - "[[bank-fraud-ic]]"
  - "[[money-laundering-ic]]"
target_entity: "Zeus/Jabber Zeus online-banking theft crew and associated money-mule network"
lead_agency: "[[fbi-cyber-division]]"
coordinating_body: "[[fbi-cyber-division]]"
participating_countries:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[netherlands]]"
  - "[[ukraine]]"
jurisdictions:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[netherlands]]"
  - "[[ukraine]]"
participating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[netherlands-politie]]"
  - "[[uk-metropolitan-police]]"
  - "[[ukraine-sbu]]"
  - "[[us-doj]]"
  - "[[us-secret-service]]"
  - "[[us-dhs]]"
  - "[[us-postal-inspection]]"
organizations:
  - "[[fbi-cyber-division]]"
  - "[[netherlands-politie]]"
  - "[[uk-metropolitan-police]]"
  - "[[ukraine-sbu]]"
  - "[[us-doj]]"
  - "[[us-secret-service]]"
  - "[[us-dhs]]"
  - "[[us-postal-inspection]]"
mechanisms_used:
  - "[[informal-cooperation]]"
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[public-private-cooperation]]"
legal_basis:
  - "Domestic bank-fraud, money-laundering, computer-crime, and search-warrant authorities in participating jurisdictions"
results:
  arrests: 64
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "FBI reported attempted theft of USD 220 million and actual losses of USD 70 million."
    - "Ukrainian SBU detained five key subjects and executed eight search warrants with about 50 officers."
    - "Public reporting attributed 39 U.S. arrests and 20 U.K. arrests to the same enforcement week, in addition to the five Ukraine detentions."
    - "U.S. reporting linked the investigation to 390 ACH-fraud cases, 92 suspects charged in the United States, and more than 3,500 money mules."
    - "The FBI named partners in the Netherlands, Ukraine, and the United Kingdom, plus U.S. cybercrime task forces and financial-sector working groups."
credibility_index: 4.25
source_tier: 1
missing_fields:
related_cases:
related_operations:
  - "[[zeus-spyeye-jit-takedown]]"
  - "[[dridex-operations]]"
challenges_encountered:
  - "The operation combines a malware crew, money-mule enforcement, and multiple national charging tracks. This page records the operation-level international cooperation and does not merge later Zeus-derived botnet operations into this 2010 action."
lessons_learned:
  - "Banking-trojan enforcement requires coupling malware attribution with money-mule, bank-record, and cross-border infrastructure evidence."
  - "Early FBI cybercrime legal-attache relationships and embedded cyber investigators were operationally important for obtaining action in foreign jurisdictions."
source_count: 5
sources:
  - "[[2010-10-01_fbi_operation-trident-breach]]"
  - "[[2010-09-30_fbi-newyork_zeus-trojan-bank-fraud]]"
  - "[[2010-10-01_fbi_cyber-bust-zeus]]"
  - "[[2010-10-02_krebsonsecurity_operation-trident-breach-zeus]]"
  - "[[2010-10-01_wired_zeus-ukraine-arrests-trident-breach]]"
summary: "Operation Trident Breach was an FBI-led 2009-2010 multinational operation against a Zeus/Jabber Zeus online-banking theft network and its money-mule layer. Public sources identify cooperation among the United States, United Kingdom, Netherlands, and Ukraine, with attempted theft of USD 220 million, actual losses of USD 70 million, five Ukrainian SBU detentions, 39 U.S. arrests, and 20 U.K. arrests reported during the enforcement week."
created: 2026-05-07
updated: 2026-05-07
---
# Operation Trident Breach

## Summary

Operation Trident Breach was an FBI-led multinational action against a Zeus/Jabber Zeus online-banking theft network and the money-mule layer used to move stolen funds. The investigation began in May 2009 after FBI agents in Omaha, Nebraska identified suspicious ACH batch payments to 46 U.S. bank accounts. The FBI later described the operation as a large-scale international organized cybercrime investigation involving the United States, United Kingdom, Netherlands, and Ukraine.

The operation is included in this corpus because the official FBI release names foreign police partners in the Netherlands, Ukraine, and the United Kingdom; identifies the Zeus botnet as the malware tool; and records arrests, search warrants, digital evidence, public-private support, and financial-sector coordination.

## Cooperation Model

- **FBI coordination:** The FBI Cyber Division and field-office cybercrime task forces coordinated the U.S. investigation and worked with foreign counterparts.
- **Ukraine operational action:** The Security Service of Ukraine detained five key subjects on 30 September 2010 and executed eight search warrants with approximately 50 officers.
- **Netherlands investigative support:** The Netherlands Police Agency's high-tech crime unit helped identify the hackers by monitoring Dutch infrastructure used by the group.
- **United Kingdom enforcement:** The Metropolitan Police Service carried out arrests and charges linked to the money-mule layer and Zeus-related thefts.
- **Public-private support:** The FBI release identifies financial-industry working groups, public-private partnerships, and Internet security researchers as part of the intelligence and disruption model.

## Participating Countries

The source-backed country set is [[united-states|United States]], [[united-kingdom|United Kingdom]], [[netherlands|Netherlands]], and [[ukraine|Ukraine]]. Additional legal-attache activity is described in broader terms, but this page records only the countries explicitly tied to the operation by the primary FBI source set.

## Results and Impact

| Metric | Value |
|---|---:|
| Attempted theft | USD 220 million |
| Actual theft/losses | USD 70 million |
| U.S. suspects charged | 92 |
| U.S. arrests reported | 39 |
| U.K. arrests reported | 20 |
| Ukraine detentions | 5 |
| Ukraine search warrants | 8 |
| Money mules referenced in public reporting | 3,500+ |
| ACH-fraud cases tracked by FBI reporting | 390 |

The numeric arrest field uses the public 39 U.S. arrests plus 20 U.K. arrests plus five Ukraine detentions reported across the FBI/Krebs/Wired/PCWorld source set. The official FBI press release is more conservative and describes "numerous" arrests and search warrants without a single global total, so the structured result should be read as a sourced public-reporting aggregate rather than a single indictment count.

## Boundary and Non-Duplication Notes

This page is distinct from [[zeus-spyeye-jit-takedown]], which covers the 2015 Europol-Eurojust Joint Investigation Team action against a Zeus/SpyEye banking-trojan ring in Ukraine. It is also distinct from [[dridex-operations]], which records the later Bugat/Dridex/Evil Corp disruption and prosecution sequence.

Operation Trident Breach should remain bounded to the 2009-2010 Zeus/Jabber Zeus banking-theft and money-mule enforcement action. Later GameOver Zeus, Dridex/Bugat, GozNym, and Zeus/SpyEye actions should be treated as related but separate operation records unless a source explicitly merges them.

## Evidence Notes

The FBI national press release is the anchor source for the operation name, the May 2009 start, the U.S.-U.K.-Netherlands-Ukraine cooperation frame, the Zeus malware mechanism, the USD 220 million attempted theft and USD 70 million actual losses, and the Ukrainian SBU searches and detentions. The FBI New York and FBI story pages provide parallel official coverage of the U.S. charging and arrest layer. Krebs, Wired, and PCWorld independently corroborate the operation name, country set, 39 U.S. arrests, 20 U.K. arrests, five Ukraine detentions, and the 3,500+ money-mule scale.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | International Cooperation Disrupts Multi-Country Cyber Theft Ring | FBI | 2010-10-01 | https://archives.fbi.gov/archives/news/pressrel/press-releases/international-cooperation-disrupts-multi-country-cyber-theft-ring |
| [2] | Manhattan U.S. Attorney Charges 37 Defendants Involved in Global Bank Fraud Schemes that Used "Zeus Trojan" and Other Malware to Steal Millions of Dollars from U.S. Bank Accounts | FBI New York | 2010-09-30 | https://archives.fbi.gov/archives/newyork/press-releases/2010/nyfo093010.htm |
| [3] | Cyber Bust: Global Partnerships Lead to Major Arrests | FBI | 2010-10-01 | https://archives.fbi.gov/archives/news/stories/2010/october/cyber-banking-fraud |
| [4] | Ukraine Detains 5 Individuals Tied to USD 70 Million in U.S. eBanking Heists | Krebs on Security | 2010-10-02 | https://krebsonsecurity.com/2010/10/ukraine-detains-5-individuals-tied-to-70-million-in-ebanking-heists/ |
| [5] | 5 Key Players Nabbed in Ukraine in USD 70-Million Bank Fraud Ring | Wired | 2010-10-01 | https://www.wired.com/2010/10/zeus-ukraine-arrests/ |
