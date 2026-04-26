---
type: case
title: "Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain"
case_number: "Source-derived from Europol Carbanak/Cobalt arrest reporting"
jurisdiction: "International law enforcement action (multi-jurisdictional)"
jurisdiction_country: "[[international]]"
case_type: prosecution
status: prosecuted
crime_charged:
  - "[[malware-ic]]"
  - "[[bank-fraud-ic]]"
  - "[[online-fraud-ic]]"
defendants:
  - name: "Unidentified alleged Carbanak/Cobalt mastermind"
    nationality: Unknown
    status: prosecuted
    sentence: ""
    location_at_arrest: Spain
related_operation: "[[operation-mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain]]"
ic_elements:
  mlat_requests:
    []
  extradition: ""
  evidence_from_abroad:
    []
  foreign_arrests:
    []
  asset_freezing:
    []
cooperating_agencies:
  - "[[europol-ec3]]"
  - "[[fbi]]"
legal_frameworks_invoked:
  - "[[informal-cooperation]]"
mechanisms_used:
  - "[[informal-cooperation]]"
key_legal_issues:
  - "[[malware-ic]]"
  - "[[bank-fraud-ic]]"
precedent_value: "Strong for cross-border operational context, weak for defendant identity and downstream docket detail."
source_count: 4
sources:
  - "[[2018-03-01_europol-europa-eu_mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain]]"
  - "[[2015-02-16_securelist_the-great-bank-robbery-the-carbanak-apt]]"
  - "[[2026-04-18_europol-europa-eu_carbanak-cobalt-infographic]]"
  - "[[2018-08-01_fbi-gov_how-cyber-crime-group-fin7-attacked-and-stole-data-from-hundreds-of-us-companies]]"
created: 2026-04-18
updated: 2026-04-26
summary: "Spanish authorities, supported by Europol and other international partners, arrested the alleged mastermind behind the Carbanak/Cobalt campaigns in Spain. Public sources firmly support the arrest event and campaign scale but do not cleanly identify the suspect by name within the source set used here."
---
## Summary

Spanish authorities, supported by Europol and other international partners, arrested the alleged mastermind behind the Carbanak/Cobalt campaigns in Spain. Public sources firmly support the arrest event and campaign scale but do not cleanly identify the suspect by name within the source set used here.

## Facts

The source set links the arrest to a campaign that targeted more than 100 financial institutions across more than 40 countries and was publicly associated with losses of more than EUR 1 billion. The technical tradecraft described in Kaspersky's reporting includes spear-phishing, lateral movement inside bank networks, and ATM or account-manipulation cash-out patterns.

## International Cooperation Elements

This page remains valuable because the operational footprint is clear even when the defendant identity is not:

- Spain conducted the arrest
- [[europol-ec3|Europol EC3]] coordinated internationally
- Kaspersky contributed technical intelligence that informed public understanding of the campaign

## Legal Analysis

The main integrity issue is identity. The source set used in this repo does not currently include a clean public charging document or court filing that settles the defendant's name and procedural status. To avoid dataset contamination, this page keeps the suspect unidentified. It records only what the current public-source record clearly supports: the arrest event, the campaign scale and the international cooperation pattern.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2018-03-01: Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain.
- Kaspersky Securelist, 2015-02-16: The Great Bank Robbery: the Carbanak APT.
- Europol, 2026-04-18: Carbanak / Cobalt infographic.
- FBI, 2018-08-01: How Cyber Crime Group FIN7 Attacked and Stole Data from Hundreds of U.S. Companies.

## Operational Timeline

- 2015-02-16: public source coverage from Kaspersky Securelist.
- 2018-03-01: public source coverage from Europol.
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

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain | Europol | 2018-03-01 | https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain |
| [2] | The Great Bank Robbery: the Carbanak APT | Kaspersky Securelist | 2015-02-16 | https://securelist.com/the-great-bank-robbery-the-carbanak-apt/68732/ |
| [3] | Carbanak / Cobalt infographic | Europol | 2026-04-18 | https://www.europol.europa.eu/cms/sites/default/files/documents/carbanakcobalt.pdf |
| [4] | How Cyber Crime Group FIN7 Attacked and Stole Data from Hundreds of U.S. Companies | FBI | 2018-08-01 | https://www.fbi.gov/contact-us/field-offices/seattle/news/stories/how-cyber-crime-group-fin7-attacked-and-stole-data-from-hundreds-of-us-companies |
