---
type: operation
title: "Operation Bakovia (CTB-Locker/Cerber Ransomware)"
title_ko: "바코비아 작전 (CTB-Locker/Cerber 랜섬웨어)"
aliases: ["Operation Bakovia", "CTB-Locker Cerber arrests"]
case_id: "CYB-2018-050"
period: 1
operation_type: "arrest-sweep"
status: "completed"
enforcement_type:
  - "arrest"
  - "seizure"
outcome: "success"
timeframe:
  announced: "2017-12-20"
  start: "2017-12-20"
  end: "2017-12-20"
  ongoing: false
crime_type: "[[ransomware-ic]]"
target_entity: "CTB-Locker and Cerber ransomware distributors"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[romania]]"
  - "[[netherlands]]"
  - "[[united-states]]"
  - "[[united-kingdom]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[romania-diicot]]"
  - "[[fbi-cyber-division]]"
  - "[[uk-nca]]"
  - "[[netherlands-politie]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 5
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Romanian suspects arrested for CTB-Locker and Cerber ransomware distribution"
    - "McAfee provided private-sector intelligence support"
edges:
  - source_actor: "Europol"
    target_actor: "Romania DIICOT"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
  - source_actor: "Europol"
    target_actor: "FBI"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
credibility_index: 1.88
source_tier: 3
missing_fields:
  - "legal_basis"
  - "mechanisms_used"
  - "exact_arrest_details"
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "Private-sector partnership (McAfee) enhanced law enforcement intelligence gathering"
source_count: 1
sources:
  - "tier3-cyberscoop-bakovia-2017"
created: 2026-04-08
updated: 2026-04-08
---

> [!note] This operation is documented from a Tier 3 (cybersecurity media) source. Additional verification from official sources (Tier 1-2) would strengthen data reliability.

## Summary

**Operation Bakovia** was a joint international law enforcement action targeting the distributors of **CTB-Locker** and **Cerber** ransomware, two of the most widespread ransomware families in 2016-2017. Coordinated by [[europol-ec3|Europol]], the operation resulted in arrests in Romania, with support from the FBI, UK NCA, and Dutch National Police. McAfee provided key private-sector intelligence support.

## Background

CTB-Locker (Curve-Tor-Bitcoin Locker) was a ransomware family that encrypted victims' files and demanded Bitcoin payment for decryption. Cerber operated as a Ransomware-as-a-Service (RaaS) platform, allowing affiliates to distribute the malware in exchange for a share of ransom payments. Both families were responsible for significant financial losses worldwide.

## Participating Parties

### Coordinating Body
- [[europol-ec3|Europol EC3]]
- [[eurojust|Eurojust]]

### Participating Countries
- [[romania|Romania]] (lead arrests)
- [[netherlands|Netherlands]]
- [[united-states|United States]]
- [[united-kingdom|United Kingdom]]

### Participating Agencies
- [[romania-diicot|Romania DIICOT]]
- [[europol-ec3|Europol EC3]]
- [[fbi-cyber-division|FBI Cyber Division]]
- [[uk-nca|UK National Crime Agency]]
- [[netherlands-politie|Dutch National Police]]

### Private Sector Support
- McAfee (intelligence and technical support)

## Legal Framework

Specific legal instruments enabling the cooperation have not been detailed in the Tier 3 source. The involvement of [[eurojust|Eurojust]] suggests formal judicial cooperation channels were used.

## Operational Timeline

| Date | Event |
|------|-------|
| Pre-2017 | Multi-country investigation into CTB-Locker and Cerber ransomware |
| 2017-12-20 | Arrests in Romania; operation announced |

## Results and Impact

| Metric | Count |
|--------|-------|
| Arrests | 5 (Romania) |
| Countries involved | 4 |

## Cooperation Mechanisms Used

The involvement of Europol and Eurojust suggests use of Joint Investigation Team (JIT) procedures and SIENA messaging, though specific details are not confirmed from the Tier 3 source.

## Korean Involvement (한국의 참여)

No Korean involvement identified in Operation Bakovia.

## Contradictions & Open Questions

- What specific legal framework (JIT, MLAT) was used for the cooperation?
- Were the arrested individuals ultimately convicted?
- What was the estimated total damage caused by the CTB-Locker/Cerber operations?
- What role did McAfee's intelligence play in identifying the suspects?

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | CTB-Locker Cerber ransomware arrests — Europol, McAfee | CyberScoop | ~2017-12 | [link](https://cyberscoop.com/ctb-locker-cerber-ransomware-arrests-europol-mcafee/) |
