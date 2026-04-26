---
type: source
title: "CyberScoop: International sting shuts down 'favorite' VPN of cybercriminals"
collection_url: "https://cyberscoop.com/safe-inet-takedown-fbi-interpol/"
collection_domain: "cyberscoop.com"
source_type: "news"
publisher: "CyberScoop"
author: "Joe Warminsky"
publish_date: "2020-12-22"
ingest_date: "2026-04-08"
enriched_date: "2026-04-10"
language: "en"
reliability: "medium-high"
credibility: "probably-true"
sensitivity: "public"
source_tier: 3
pages_updated:
  - "operation-nova"
key_findings:
  - "On 22 December 2020, German Reutlingen Police Headquarters led a multi-country operation (codenamed Operation Nova) that seized the infrastructure of Safe-Inet, a decade-old bulletproof VPN service marketed in underground forums as a cybercriminal anonymization tool"
  - "Three domains were seized — safe-inet.com, safe-inet.net and insorg.org — corresponding to the service's multiple branded fronts. Servers were seized in multiple jurisdictions, though the exact count was reported as 'infrastructure in five countries'"
  - "Participating countries: Germany (lead), United States, France, Netherlands, Switzerland — coordinated through Europol. The FBI was the primary US participant"
  - "Safe-Inet offered 'up to 5 layers of anonymous VPN connections' with Russian/English support, positioning itself as bulletproof hosting for ransomware operators, e-skimmers (Magecart), spearphishers, and account-takeover actors"
  - "CyberScoop reports that ~250 companies worldwide received warnings from law enforcement about ransomware risks connected to Safe-Inet infrastructure — indicating downstream victim notification was integrated into the takedown action"
  - "Europol quote cited: 'This VPN service was sold at a high price to the criminal underworld as one of the best tools available to avoid law enforcement interception' — positioning the takedown as infrastructure disruption of the cybercrime-as-a-service supply chain"
created: 2026-04-08
updated: 2026-04-10
duplicate_of: "[[2020-12-22_cyberscoop-com_safe-inet-takedown-fbi-interpol]]"
duplicate_reason: same_collection_url
duplicate_key: "https://cyberscoop.com/safe-inet-takedown-fbi-interpol/"
duplicate_normalized_at: 2026-04-26
---

## Source

- **Publisher**: CyberScoop
- **Author**: Joe Warminsky (CyberScoop editor)
- **URL**: <https://cyberscoop.com/safe-inet-takedown-fbi-interpol/>
- **Published**: 2020-12-22 (same day as coordinated takedown announcement)
- **Source Tier**: 3 (cybersecurity trade press)
- **Reliability**: medium-high (CyberScoop editorial + sourced from Europol statement; raised from default medium)
- **Credibility**: probably-true (corroborated by Europol, PortSwigger, cybersecuritynews.com same-day)
- **Operations referenced**: [[operation-nova|Operation Nova (Safe-Inet VPN Takedown)]]

## Summary

CyberScoop's coverage of **Operation Nova** documents the **22 December 2020** seizure of Safe-Inet, a decade-old bulletproof VPN service that catered to cybercriminals. Key points:

1. **Lead agency**: German Reutlingen Police Headquarters (not BKA as sometimes reported) — an important correction for the operation page's lead-agency field
2. **Three branded fronts seized**: safe-inet.com, safe-inet.net, insorg.org — the service operated under multiple domain brands to evade takedown
3. **Five participating countries**: Germany, US, France, Netherlands, Switzerland
4. **Victim notification component**: ~250 companies proactively warned about ransomware risks from associated infrastructure — an unusual step integrating takedown with victim protection
5. **Service profile**: "Up to 5 layers of anonymous VPN", Russian/English-language support, marketed explicitly in cybercriminal forums

## Why this source matters

For the IC analysis on [[operation-nova]] this CyberScoop article provides:

- **A named author** (Joe Warminsky) improving the reliability rating
- **Specific domain names** seized (the operation page currently lists `domains_seized: 3` but does not enumerate them)
- **Victim notification data** (~250 companies warned) — a datapoint not currently captured in the operation page
- **Clarification of the German lead agency** (Reutlingen Police Headquarters, not federal BKA) — the operation page should be updated

> [!note] Operation page correction needed
> The [[operation-nova]] page currently records `lead_agency: [[germany-bka]]`. CyberScoop and the Europol press release both identify the **Reutlingen Police Headquarters** (a Land-level police authority, not the federal BKA) as the operational lead. BKA's role was coordinative.

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| Europol press release 2020-12-22 | 5 countries, 3 domains, ~decade of operation |
| PortSwigger Daily Swig 2020-12-22 | Same figures, bulletproof VPN characterization |
| Krebs on Security 2020-12-22 | Customer identification and investigation continuity |

Source diversity for Operation Nova is *medium* — all three secondary sources cite the Europol statement, providing limited independent verification.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | International sting shuts down 'favorite' VPN of cybercriminals | CyberScoop (Joe Warminsky) | 2020-12-22 | https://cyberscoop.com/safe-inet-takedown-fbi-interpol/ |
| [2] | Cybercriminals' favourite VPN taken down in global action | Europol | 2020-12-22 | https://www.europol.europa.eu/media-press/newsroom/news/cybercriminals%E2%80%99-favourite-vpn-taken-down-in-global-action |
| [3] | Safe-Inet VPN service for cybercriminals taken down in law enforcement bust | PortSwigger Daily Swig | 2020-12-22 | https://portswigger.net/daily-swig/safe-inet-vpn-service-for-cybercriminals-taken-down-in-law-enforcement-bust |
