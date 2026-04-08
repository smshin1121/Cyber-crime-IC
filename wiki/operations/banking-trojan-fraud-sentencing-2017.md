---
type: operation
title: "Banking Trojan Fraud Sentencing"
title_ko: "뱅킹 트로이목마 사기 판결"
aliases: ["Banking trojan home IP fraud case"]
case_id: "CYB-2017-051"
period: 1
operation_type: "joint-investigation"
status: "completed"
enforcement_type:
  - "arrest"
  - "indictment"
outcome: "success"
timeframe:
  announced: "2017-01-01"
  start: "2017-01-01"
  end: "2017-12-31"
  ongoing: false
crime_type: "[[banking-trojan-ic]]"
target_entity: "Banking fraud perpetrator (used home IP)"
lead_agency: ""
coordinating_body: ""
participating_countries:
  - "[[united-states]]"
participating_agencies: []
legal_basis: []
mechanisms_used: []
results:
  arrests: 1
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "5-year prison sentence for banking fraud using trojans"
edges:
  - source_actor: "US DOJ"
    target_actor: "unknown"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
credibility_index: 1.88
source_tier: 3
missing_fields:
  - "legal_basis"
  - "mechanisms_used"
  - "exact_timeframe"
  - "participating_agencies"
  - "international_cooperation_details"
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "Operational security failures (using home IP address) can lead to identification and prosecution"
source_count: 1
sources:
  - "tier3-bleepingcomputer-banking-trojan-2017"
created: 2026-04-08
updated: 2026-04-08
---

> [!note] This operation is documented from a Tier 3 (cybersecurity media) source. Additional verification from official sources (Tier 1-2) would strengthen data reliability.

## Summary

A cybercriminal who used banking trojans for financial fraud was sentenced to **5 years in prison** after being identified in part because he used his home IP address during the fraud. The case illustrates how basic operational security failures can enable law enforcement to identify and prosecute cybercriminals even in technically sophisticated fraud schemes.

## Background

Banking trojan fraud involves deploying malware that intercepts online banking sessions to steal credentials and redirect funds. While the technical aspects of such attacks can be sophisticated, the perpetrator in this case made a critical error by conducting fraudulent activities from his home IP address, making identification straightforward for investigators.

## Participating Parties

> [!warning] Legal status check needed
> The specific law enforcement agencies and any international cooperation elements need verification from official sources.

## Legal Framework

Specific legal details beyond the 5-year sentence are not available from the Tier 3 source.

## Operational Timeline

| Date | Event |
|------|-------|
| ~2017 | Sentencing: 5-year prison term for banking trojan fraud |

## Results and Impact

| Metric | Detail |
|--------|--------|
| Arrests | 1 |
| Sentence | 5 years in prison |

## Cooperation Mechanisms Used

Not detailed in available Tier 3 source.

## Lessons Learned

1. **OpSec failures enable prosecution:** The use of a home IP address for criminal activity provided investigators with a direct link to the perpetrator's identity.

## Korean Involvement (한국의 참여)

No Korean involvement identified.

## Contradictions & Open Questions

- What was the suspect's nationality and where was the prosecution?
- Were there international cooperation elements in the investigation?
- What was the total financial loss attributed to the scheme?
- What specific banking trojan was used?

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Crook Who Used His Home IP Address for Banking Fraud Gets 5 Years in Prison | BleepingComputer | ~2017 | [link](https://www.bleepingcomputer.com/news/security/crook-who-used-his-home-ip-address-for-banking-fraud-gets-5-years-in-prison/) |
