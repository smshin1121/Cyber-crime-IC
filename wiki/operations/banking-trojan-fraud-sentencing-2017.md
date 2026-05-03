---
aliases:

case_id: CYB-2016-051
challenges_encountered:
  - "Only Tier 3 media coverage is currently linked; official court filings are still needed for charge and court details."
coordinating_body: ""
created: 2026-04-08
credibility_index: 2.55
crime_type: "[[banking-trojan-ic]]"
edges:

enforcement_type:
  - sentencing
  - prosecution
lead_agency: "[[uk-metropolitan-police|Metropolitan Police Service]]"
legal_basis:

lessons_learned:
  - "Operational-security failures can make banking-trojan cash-out actors traceable even when the upstream malware operation remains broader and less visible."
mechanisms_used:
  - "[[public-private-cooperation|Public-Private Cooperation]]"
missing_fields:
  - "official court filing"
  - "complete charge sheet"
  - "named upstream banking-trojan operators"

operation_type: sentencing
outcome: success
participating_agencies:
  - "[[uk-metropolitan-police|Metropolitan Police Service]]"

participating_countries:
  - "[[united-kingdom]]"

period: 1
related_cases:

related_operations:

results:
  arrests: 2
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 0
  other:
    - "Tomasz Skowron sentenced to 5 years in prison"
    - "Piotr Ptach sentenced to 3 years in prison"
    - "Approximately GBP 840,000 stolen from victims worldwide"
    - "Two UK construction firms lost approximately GBP 500,000"

  servers_seized: 0
  victims_notified: 0
source_count: 1
source_tier: 3
sources:
  - "[[2017-01-01_bleepingcomputer-com_crook-who-used-his-home-ip-address-for-banking-fraud-gets-5-years-in-prison]]"
status: absorbed
target_entity: "Tomasz Skowron banking-trojan cash-out activity"
timeframe:
  announced: 2016-12-21
  end: 2016-12-21
  ongoing: false
  start: 2014-12
title: "Banking Trojan Fraud Sentencing"
title_ko: "뱅킹 트로이목마 사기 판결"
type: operation
updated: "2026-05-03"
operation_role: follow-on
parent_operation: ""
summary: "Tomasz Skowron, a 29-year-old Polish national, was sentenced in the United Kingdom to 5 years in prison after Metropolitan Police investigators linked him to banking-trojan cash-out activity. The BleepingComputer report, citing London Metropolitan Police, says Skowron used his home IP address to move funds from compromised accounts; Piotr Ptach was also arrested and sentenced to 3 years for recruiting money mules."
crime_types:
  - "[[banking-trojan-ic]]"
  - "[[malware-ic]]"
---
> [!note] This record is documented from a Tier 3 cybersecurity-media source. Additional verification from official UK court or Metropolitan Police materials would strengthen reliability.

## Scope Note

This is not a standalone international-cooperation operation. It is a follow-on sentencing/prosecution record retained for traceability because it illustrates banking-trojan cash-out, cross-border victim/fund-flow facts, and private-sector reporting.

## Summary

Tomasz Skowron, a 29-year-old Polish national, was sentenced in the United Kingdom to **5 years in prison** for his role in a banking-trojan fraud and money-laundering scheme. BleepingComputer reported, citing London Metropolitan Police, that Skowron was identified because he used his **home IP address** while moving funds from compromised bank accounts.

The same report says Piotr Ptach, who helped recruit money mules, pleaded guilty and received a **3-year prison sentence**. The public source supports this page as a sentencing/prosecution record, not as a distinct multinational takedown operation.

## Background

The underlying criminal group used banking trojans to harvest online-banking credentials. Skowron was described as a cash-out actor granted access to stolen banking data: he moved money from compromised accounts into accounts he controlled or into mule accounts for withdrawal and laundering.

The source ties the case to victims in multiple jurisdictions. Police linked Skowron to fraudulent payments from the Commonwealth Bank of Australia into UK bank accounts, and to two man-in-the-middle attacks against UK construction firms that caused about **GBP 500,000** in losses.

## Participating Parties

| Role | Entity |
|---|---|
| Police source / investigator | [[uk-metropolitan-police|Metropolitan Police Service]] |
| Sentenced defendant | Tomasz Skowron |
| Co-defendant / mule recruiter | Piotr Ptach |
| Affected banking channel | Commonwealth Bank of Australia to UK bank accounts |

## Legal Framework

Specific UK charge and court-document details are not available from the current Tier 3 source. The public record used here supports the sentencing outcome and investigation narrative, but not a full legal-procedure reconstruction.

## Operational Timeline

| Date | Event |
|------|-------|
| 2014-12 | Police arrested Skowron after banking-industry reports flagged fraudulent transfers. |
| 2016-12-21 | BleepingComputer reported the 5-year sentence for Skowron and the 3-year sentence for Ptach. |

## Results and Impact

| Metric | Detail |
|--------|--------|
| Arrests | 2 reported: Skowron and Ptach |
| Sentence | Skowron: 5 years; Ptach: 3 years |
| Losses | About GBP 840,000 from victims worldwide; about GBP 500,000 tied to two UK construction firms |
| Attribution hook | Home IP address used to access compromised bank accounts |

## Cooperation Mechanisms Used

No formal MLAT, extradition, joint investigation team, or Europol/INTERPOL role is identified in the available source. The cooperation signal is narrower: banking-industry reporting to UK police, plus cross-border victim and fund-flow facts involving Australian and UK accounts.

## Lessons Learned

1. **OpSec failures enable prosecution:** The use of a home IP address for criminal activity provided investigators with a direct link to the perpetrator's identity.
2. **Cash-out layers are prosecutable even when upstream actors remain diffuse:** The source frames Skowron as one actor with access to data gathered by a broader banking-trojan operation.
3. **Private-sector reporting matters:** The arrest followed reports from the banking industry rather than a publicly described multinational takedown.

## Korean Involvement (한국 참여)

No Korean involvement identified.

## Contradictions & Open Questions

- Which UK court issued the sentence?
- What exact charges were used against Skowron and Ptach?
- Which banking trojan family was used by the upstream group?
- Did Australian law enforcement participate, or was Australia only represented through victim-bank fund flows?

## Follow-Up Actions

Official-source gap: Locate a Metropolitan Police release or UK court record for the sentencing, charges, court, and case number before treating this as a high-confidence legal-procedure record.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- BleepingComputer, 2016-12-21: Crook Who Used His Home IP Address for Banking Fraud Gets 5 Years in Prison.

## Evidence and Attribution Notes

- Tomasz Skowron, a 29-year-old Polish national, was sentenced to 5 years in a UK court for his role in a banking-trojan money-laundering and fraud scheme that stole approximately GBP 840,000 from victims worldwide.
- Skowron's accomplice Piotr Ptach received a 3-year sentence for recruiting money mules.
- Skowron was identified because he used his home IP address to access compromised victim bank accounts and transfer funds.
- UK police arrested Skowron in December 2014 after banking-industry reports.
- The article links Skowron to fraudulent payments from Commonwealth Bank of Australia into UK accounts and to man-in-the-middle attacks against two UK construction firms.
- Source-integrity audit on 2026-05-03 found that BBC article ID `uk-43893420` is a Webstresser/DDoS takedown story, not this banking-trojan sentencing. The mismatched BBC reference was removed from this operation.

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Crook Who Used His Home IP Address for Banking Fraud Gets 5 Years in Prison | BleepingComputer | 2016-12-21 | https://www.bleepingcomputer.com/news/security/crook-who-used-his-home-ip-address-for-banking-fraud-gets-5-years-in-prison/ |
