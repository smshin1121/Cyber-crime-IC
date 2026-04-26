---
type: operation
title: "Nigerian BEC Email Fraud Arrest ($60M)"
title_ko: "나이지리아 BEC 이메일 사기 체포 (6천만 달러)"
aliases:
  - "Nigerian email scammer arrest 2016"
  - "$60M BEC arrest"
case_id: CYB-2016-050
period: 1
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
outcome: success
timeframe:
  announced: 2016-08-01
  start: 2015
  end: 2016-08-01
  ongoing: false
crime_type: "[[bec-ic]]"
target_entity: "Nigerian BEC scammer ($60M fraud)"
lead_agency: "[[interpol]]"
coordinating_body: "[[interpol]]"
participating_countries:
  - "[[nigeria]]"
participating_agencies:
  - "[[interpol]]"
  - "[[nigeria-efcc]]"
  - "[[interpol-igci]]"
  - "[[trend-micro]]"
  - "Fortinet FortiGuard Labs"
legal_basis:
  - "[[informal-cooperation]]"
  - "[[public-private-cooperation]]"
mechanisms_used:
  - "[[informal-cooperation]]"
  - "[[public-private-cooperation]]"
  - "[[search-seizure]]"

results:
  arrests: 2
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "$60 million in BEC fraud attributed to arrested individual"
    - "INTERPOL and EFCC arrested a 40-year-old Nigerian national known as Mike"
    - "A second 38-year-old suspect was also arrested by Nigerian authorities"
    - "Device forensics linked the suspects to BEC, payment diversion, CEO fraud, and romance scams"
edges:
  - source_actor: INTERPOL
    target_actor: "Nigeria EFCC"
    cooperation_type: joint_investigation
    legal_basis: public_private_cooperation
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - suspect_legal_name
  - final_case_outcome
  - sentencing_or_conviction_record
related_cases:

related_operations:

challenges_encountered:

lessons_learned:

source_count: 5
sources:
  - "[[2016-08-01_interpol-es_ringleader-of-global-network-behind-thousands-of-online-scams-arrested-in-nigeria]]"
  - "[[2016-08-01_arstechnica_nigerian-authorities-arrest-alleged-mastermind-of-60m-worth-of-online-scams]]"
  - "[[2016-08-01_cnn_nigerian-man-arrested-in-global-60-million-scam]]"
  - "[[2016-08-01_dw_nigerian-arrested-for-international-60-million-dollar-online-fraud]]"
  - "[[2016-12-22_justice-gov_nigerian-nationals-charged-with-operating-business-compromise-scheme]]"
created: 2026-04-08
updated: 2026-04-26
operation_role: umbrella
parent_operation: ""
summary: "INTERPOL and Nigeria's EFCC arrested the alleged leader of a transnational online-fraud network in Port Harcourt, Nigeria. The official INTERPOL record attributes more than USD 60 million in BEC, payment-diversion, CEO-fraud, and romance-scam activity to the network, which used actors and laundering contacts across multiple countries."
jurisdictions:
  - "[[nigeria]]"
  - "[[united-states]]"
organizations:
  - "[[interpol]]"
  - "[[nigeria-efcc]]"
  - "[[interpol-igci]]"
  - "[[trend-micro]]"
crime_types:
  - "[[bec-ic]]"
---
## Summary

This operation was not just a generic Nigeria-based BEC arrest. The primary INTERPOL record identifies it as a joint INTERPOL-EFCC action against the alleged leader of a global online-fraud network. The suspect, a 40-year-old Nigerian national known publicly as "Mike," was arrested in Port Harcourt, Rivers State, Nigeria, after intelligence supplied through INTERPOL's public-private partnership pipeline helped locate him.

The source base attributes more than **USD 60 million** in fraud exposure to the network. One reported victim was allegedly induced to pay **USD 15.4 million**. The activity was not limited to one fraud pattern: seized-device forensics linked the suspect to business email compromise, payment-diversion fraud, CEO fraud, and romance scams.

## Background

The INTERPOL account describes a network of at least 40 people across Nigeria, Malaysia, and South Africa. Its operators compromised small and medium-sized business email accounts in Australia, Canada, India, Malaysia, Romania, South Africa, Thailand, and the United States. The compromised accounts were then used to misdirect payments from companies doing business with those account holders.

The network also relied on laundering infrastructure outside Nigeria. INTERPOL identified contacts in China, Europe, and the United States who supplied bank-account details for moving illicit proceeds. These countries should therefore be read as victim, infrastructure, or laundering geographies unless a source separately confirms law-enforcement participation.

## Participating Parties

### Lead and Coordinating Bodies
- [[interpol|INTERPOL]]
- [[nigeria-efcc|Nigerian Economic and Financial Crimes Commission]]
- [[interpol-igci|INTERPOL Global Complex for Innovation]]

### Private and Technical Partners
- [[trend-micro|Trend Micro]]
- Fortinet FortiGuard Labs
- INTERPOL Digital Crime Centre
- Cyber Defense Institute at IGCI

### Geography

The verified arrest jurisdiction is [[nigeria|Nigeria]]. The United States appears in the record as a victim and laundering-contact geography, and in a separate DOJ BEC source in this page's reference set. The page therefore treats U.S. involvement cautiously unless a source confirms direct operational participation in this specific Nigerian arrest.

## Cooperation Mechanics

The cooperation chain is unusually explicit for a BEC arrest. Trend Micro first provided a report to INTERPOL through its strategic-partner relationship at IGCI in Singapore. Fortinet FortiGuard Labs then supplied actionable intelligence in 2015. INTERPOL Digital Crime Centre specialists, including experts from the Cyber Defense Institute at IGCI, worked with EFCC to locate the suspect in Nigeria.

After the arrest, EFCC conducted forensic examination of seized devices. Those device reviews connected the suspect to multiple fraud types and helped distinguish the observed conduct from a simple single-victim wire-fraud case.

## Legal and Procedural Status

The two arrested suspects reportedly faced Nigerian charges including hacking, conspiracy, and obtaining money under false pretences. At the time of the INTERPOL release, both were on administrative bail while the investigation continued. No final conviction or sentencing record has been confirmed in the current corpus.

## Operational Timeline

| Date | Event |
|------|-------|
| 2015 | Fortinet FortiGuard Labs supplied actionable intelligence that supported the lead-development process |
| 2016-06 | INTERPOL and EFCC located and arrested the alleged ringleader in Port Harcourt |
| 2016-08-01 | INTERPOL publicly announced the joint action |
| 2016-12-22 | DOJ published a separate Connecticut BEC prosecution source included in this page's reference set |

## Results and Impact

| Metric | Detail |
|--------|--------|
| Arrests | 2 reported by Nigerian authorities |
| Primary suspect | 40-year-old Nigerian national publicly identified only as "Mike" |
| Network size | At least 40 individuals across Nigeria, Malaysia, and South Africa |
| Estimated fraud exposure | More than USD 60 million |
| Largest single known victim payment | USD 15.4 million |
| Fraud types | BEC, payment diversion, CEO fraud, romance scams |
| Confirmed procedural step | EFCC forensic examination of seized devices |

## Korean Involvement

No Korean law-enforcement participation or Korean victim link is identified in the current sources.

## Contradictions & Open Questions

- The public record identifies the lead suspect only as "Mike"; the legal name is not confirmed in the current corpus.
- The INTERPOL release confirms hundreds of victims and multiple affected countries, but it does not provide a complete victim list.
- The final Nigerian case outcome, if any, is not present in the collected sources.
- The DOJ Connecticut BEC source in this reference set is related by fraud pattern and nationality but should not be treated as proof of U.S. participation in the Port Harcourt arrest unless a direct link is separately established.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search and repository review have not produced a public Nigerian court docket or final judgment for this operation. The priority follow-up is therefore to locate EFCC court filings, Nigerian press releases, or later INTERPOL updates that identify the final procedural result.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Ringleader of global network behind thousands of online scams arrested in Nigeria | INTERPOL | 2016-08-01 | https://www.interpol.int/es/Noticias-y-acontecimientos/Noticias/2016/Ringleader-of-global-network-behind-thousands-of-online-scams-arrested-in-Nigeria |
| [2] | Nigerian authorities arrest alleged mastermind of $60M worth of online scams | Ars Technica | 2016-08-01 | https://arstechnica.com/tech-policy/2016/08/nigerian-authorities-arrest-alleged-mastermind-of-60m-worth-of-online-scams/ |
| [3] | Nigerian man arrested in global, $60 million scam | CNN | 2016-08-01 | https://money.cnn.com/2016/08/01/news/companies/nigeria-scam-arrest/index.html |
| [4] | Nigerian arrested for international 60 million dollar online fraud | Deutsche Welle | 2016-08-01 | https://www.dw.com/en/nigerian-arrested-for-international-60-million-dollar-online-fraud/a-19441117 |
| [5] | Nigerian Nationals Charged with Operating Business Compromise Scheme | DOJ D. Conn. | 2016-12-22 | https://www.justice.gov/usao-ct/pr/nigerian-nationals-charged-operating-business-compromise-scheme |
