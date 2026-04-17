---
operation_role: umbrella
parent_operation: ""
summary: "**Operation Nova** was an international law enforcement action that took down **Safe-Inet**, a bulletproof VPN service that had operated for over a decade. The operation was led by [[germany-bka|German BKA]] and coordinated by [[europol-ec3|Europol]], with participation from the FBI and law enforcement agencies in the Netherlands, Switzerland, and France. The service had been used by ransomware operators, Magecart web skimmers, and other cybercriminals to conceal their identities and locations."
---
﻿---
aliases:
- Operation Nova
- Safe-Inet takedown
case_id: CYB-2020-050
challenges_encountered: []
coordinating_body: '[[europol-ec3]]'
created: 2026-04-08
credibility_index: 2.55
crime_type: '[[cybercrime-infrastructure-ic]]'
edges:
- cooperation_type: joint_investigation
  direction: undirected
  legal_basis: unknown
  source_actor: Germany BKA
  target_actor: Europol
- cooperation_type: joint_investigation
  direction: undirected
  legal_basis: unknown
  source_actor: FBI
  target_actor: Europol
enforcement_type:
- seizure
- takedown
lead_agency: '[[germany-bka]]'
legal_basis: []
lessons_learned:
- Targeting cybercrime infrastructure (bulletproof hosting/VPN) can disrupt multiple
  criminal groups simultaneously
mechanisms_used: []
missing_fields:
- legal_basis
- mechanisms_used
operation_type: infrastructure-seizure
outcome: success
participating_agencies:
- '[[germany-bka]]'
- '[[fbi-cyber-division]]'
- '[[europol-ec3]]'
participating_countries:
- '[[germany]]'
- '[[united-states]]'
- '[[netherlands]]'
- '[[switzerland]]'
- '[[france]]'
period: 2
related_cases: []
related_operations: []
results:
  arrests: 0
  cryptocurrency_seized: ''
  decryption_keys_recovered: 0
  domains_seized: 3
  indictments: 0
  other:
  - Safe-Inet VPN service shut down
  - Service had been active for over a decade
  - Used by ransomware operators, Magecart skimmers, and other cybercriminals
  servers_seized: 3
  victims_notified: 0
source_count: 3
source_tier: 3
sources:
- tier3-cyberscoop-safe-inet-2020
- tier3-portswigger-safe-inet-2020
- tier3-cybersecuritynews-safe-inet-2020
status: completed
target_entity: Safe-Inet bulletproof VPN service
timeframe:
  announced: '2020-12-22'
  end: '2020-12-22'
  ongoing: false
  start: '2020-12-22'
title: Operation Nova (Safe-Inet VPN Takedown)
title_ko: 노바 작전 (Safe-Inet VPN 소탕)
type: operation
updated: '2026-04-09'
---

> [!note] This operation is documented from a Tier 3 (cybersecurity media) source. Additional verification from official sources (Tier 1-2) would strengthen data reliability.

## Summary

**Operation Nova** was an international law enforcement action that took down **Safe-Inet**, a bulletproof VPN service that had operated for over a decade. The operation was led by [[germany-bka|German BKA]] and coordinated by [[europol-ec3|Europol]], with participation from the FBI and law enforcement agencies in the Netherlands, Switzerland, and France. The service had been used by ransomware operators, Magecart web skimmers, and other cybercriminals to conceal their identities and locations.

The takedown of Safe-Inet represented an infrastructure-focused approach to cybercrime disruption, targeting the enabling services rather than individual criminal groups.

## Background

Safe-Inet was a VPN service that catered specifically to cybercriminals, providing anonymity and protection from law enforcement investigation. Unlike legitimate VPN services, Safe-Inet functioned as "bulletproof" infrastructure, deliberately ignoring abuse complaints and law enforcement requests. The service supported multiple layers of VPN connections and was marketed in underground forums as a tool for concealing criminal activity.

## Participating Parties

### Lead Agency
- [[germany-bka|German Federal Criminal Police Office (BKA)]]

### Coordinating Body
- [[europol-ec3|Europol EC3]]

### Participating Countries (5)
- [[germany|Germany]]
- [[united-states|United States]]
- [[netherlands|Netherlands]]
- [[switzerland|Switzerland]]
- [[france|France]]

## Legal Framework

Specific legal instruments have not been detailed in available Tier 3 sources.

## Operational Timeline

| Date | Event |
|------|-------|
| ~2010+ | Safe-Inet VPN service operating |
| Pre-2020 | Investigation into Safe-Inet |
| 2020-12-22 | Coordinated seizure of Safe-Inet infrastructure and domains |

## Results and Impact

| Metric | Count |
|--------|-------|
| Servers seized | 3 |
| Domains seized | 3 |
| Countries involved | 5 |
| Service operational years | 10+ |

## Cooperation Mechanisms Used

Not detailed in Tier 3 sources. The German-led, Europol-coordinated pattern with FBI involvement is consistent with established EU-US cooperation frameworks.

## Korean Involvement (한국의 참여)

No Korean involvement identified.

## Contradictions & Open Questions

- Were any operators of Safe-Inet identified or arrested?
- How many criminal groups were using the service?
- What was the technical method for identifying and seizing the infrastructure?
- Did the takedown lead to any follow-up investigations against the service's users?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Safe Inet Takedown Fbi Interpol | CyberScoop | 2020-12-22 | [원본](https://cyberscoop.com/safe-inet-takedown-fbi-interpol/) |
| [2] | Bulletproof Vpn Seized | cybersecuritynews.com | 2020-12-22 | [원본](http://web.archive.org/web/20240714062723/https://cybersecuritynews.com/bulletproof-vpn-seized/) |
| [3] | Safe Inet Vpn Service For Cybercriminals Taken Down In Law Enforcement Bust | portswigger.net | 2020-12-22 | [원본](https://portswigger.net/daily-swig/safe-inet-vpn-service-for-cybercriminals-taken-down-in-law-enforcement-bust) |
