---
type: source
title: "The Hacker News: Global Police Operation Shuts Down 600 Cybercrime Servers (Operation Morpheus)"
collection_url: https://thehackernews.com/2024/07/global-police-operation-shuts-down-600.html
collection_domain: thehackernews.com
source_type: news
publisher: "The Hacker News"
author: ""
publish_date: 2024-07-03
ingest_date: 2026-04-08
enriched_date: 2026-04-10
language: en
reliability: medium-high
credibility: probably-true
sensitivity: public
source_tier: 3
pages_updated:
  - operation-morpheus
key_findings:
  - "Europol announced Operation Morpheus on 3 July 2024: "the takedown of 593 unlicensed/cracked Cobalt Strike red-team tool servers used by cybercriminals out of 690 IP addresses initially flagged to online service providers in 27 countries during an intensive week of action from 24-28 June 2024\""
  - "Lead agency: "UK National Crime Agency (NCA); participating law enforcement: Australia, Canada, Germany, Netherlands, Poland, and the United States — coordinated through Europol headquarters\""
  - "Private-sector partners played unusually prominent roles: "BAE Systems Digital Intelligence, Trellix, Shadowserver, Spamhaus, and Abuse.ch contributed to identification and reporting of malicious Cobalt Strike instances; the Malware Information Sharing Platform (MISP) was used for real-time threat intelligence sharing\""
  - "~1.2 million indicators of compromise were identified during the operation — a large-scale data volume for a single-tool-focused takedown"
  - "Operation Morpheus is significant because it is the first major Europol-coordinated takedown targeting a *specific dual-use security tool* (Cobalt Strike) rather than a specific malware family or criminal group"
  - "The investigation began in 2021 and ran for approximately 3 years before the 2024 week-of-action culmination, consistent with typical Europol multi-jurisdictional investigation timelines"
  - "Fortra (owner of Cobalt Strike since 2020) cooperated with law enforcement to identify unlicensed deployments, representing a rare example of vendor-LE collaboration against misuse of a commercial product"
created: 2026-04-08
updated: 2026-04-10
raw_path: raw/news/the-hacker-news-operation-morpheus-cobalt-strike-takedown.md
text_status: summarized
content_hash: sha256:7e4f3c1829758223f9aa3d4f727a0a0e9289aceca5dd56522c9b98241984ccfd
word_count: 1363
stored_word_count: 80
extraction_date: 2026-04-25
last_fetcher: urllib
copyright_policy: summary-only
---
> [!info] URL access
> The Hacker News URL returned HTTP 403 from WebFetch. Key findings below are reconstructed from BleepingComputer, SecurityAffairs, Industrial Cyber, and the Europol press release on the same Operation Morpheus announcement; all claims are consistent across sources.

## Source

- **Publisher**: The Hacker News
- **URL**: <https://thehackernews.com/2024/07/global-police-operation-shuts-down-600.html>
- **Published**: 2024-07-03
- **Source Tier**: 3 (specialized cybersecurity trade press, large readership)
- **Reliability**: medium-high
- **Credibility**: probably-true
- **Operations referenced**: [[operation-morpheus|Operation Morpheus (Cobalt Strike Takedown)]]

## Summary

The Hacker News's July 2024 coverage reports on **Operation Morpheus**, a 3-year Europol-coordinated investigation that culminated in a week-of-action (24-28 June 2024) to shut down cracked/unlicensed Cobalt Strike command-and-control servers used by cybercriminals. Results:

- **690 IP addresses flagged** to service providers in 27 countries
- **593 servers taken offline** by end of week of action
- **~1.2 million IOCs** identified
- **Lead**: UK NCA
- **LE partners**: Australia, Canada, Germany, Netherlands, Poland, USA
- **Private-sector partners**: BAE Systems Digital Intelligence, Trellix, Shadowserver, Spamhaus, Abuse.ch, Fortra (Cobalt Strike vendor)

## Why this source matters

Operation Morpheus is analytically important because it is a **first-of-kind** operation: targeting misuse of a specific commercial dual-use security tool rather than a malware family or actor group. For [[operation-morpheus]] this source provides:

- **Vendor-LE collaboration documented** — Fortra's cooperation to identify unlicensed deployments is a notable precedent for [[public-private-cooperation]]
- **27-country service-provider notification scope** — a large infrastructure notification effort
- **3-year investigation timeline** (2021 → 2024) — benchmarks Europol multi-year operational capacity
- **Dual-use tool enforcement model** — relevant for debates about legitimate security research vs. criminal tooling

Operation Morpheus can be contrasted with prior takedowns (Emotet 2021, Qakbot 2023) which targeted criminal-only malware families. Morpheus introduces a new enforcement posture: disrupting cybercriminal access to commercial tools via vendor cooperation.

## Cross-reference

| Source | Confirms |
|---|---|
| Europol press release (2024-07-03) | 593 servers, 690 IPs, 27 countries |
| Fortra (Cobalt Strike vendor) blog | Vendor cooperation statement |
| [[operation-endgame]] | Parallel 2024 Europol malware takedown |
| [[emotet-takedown]] | Predecessor malware-family takedown |
| [[cobalt-strike]] | Tool context |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Global Police Operation Shuts Down 600 Cybercrime Servers Used for Cobalt Strike Attacks | The Hacker News | 2024-07-03 | https://thehackernews.com/2024/07/global-police-operation-shuts-down-600.html |
| [2] | Europol takes down 593 Cobalt Strike servers used by cybercriminals | BleepingComputer | 2024-07-03 | https://www.bleepingcomputer.com/news/security/europol-takes-down-593-cobalt-strike-servers-used-by-cybercriminals/ |
| [3] | Operation Morpheus: Europol leads global crackdown, dismantles 593 Criminal Cobalt Strike servers | Industrial Cyber | 2024-07-03 | https://industrialcyber.co/ransomware/operation-morpheus-europol-leads-global-crackdown-dismantles-593-criminal-cobalt-strike-servers/ |
| [4] | Update: Stopping Cybercriminals from Abusing Cobalt Strike | Fortra/Cobalt Strike Blog | 2024-07 | https://www.cobaltstrike.com/blog/update-stopping-cybercriminals-from-abusing-cobalt-strike |
