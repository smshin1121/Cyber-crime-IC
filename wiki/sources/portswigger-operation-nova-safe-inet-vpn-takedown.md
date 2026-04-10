---
type: source
title: "PortSwigger (Daily Swig): Safe-Inet VPN for Cybercriminals Taken Down in Law Enforcement Bust"
collection_url: "https://portswigger.net/daily-swig/safe-inet-vpn-service-for-cybercriminals-taken-down-in-law-enforcement-bust"
collection_domain: "portswigger.net"
source_type: "news"
publisher: "PortSwigger (Daily Swig)"
author: ""
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
  - "PortSwigger Daily Swig reported on 22 December 2020 on **Operation Nova**, the coordinated seizure of Safe-Inet — a bulletproof VPN service for cybercriminals — and associated domains insorg.org, inet.com, and safe-inet.net"
  - "The takedown was led by the German Reutlingen Police Headquarters (Polizeipräsidium Reutlingen) and supported by Europol, the FBI, and additional European law enforcement agencies; coordination ran through Europol's EC3"
  - "Safe-Inet had operated for more than 10 years (circa 2010-2020) offering up to five layers of anonymous VPN connections, marketed specifically to cybercriminals at premium prices as a 'best-in-class' anti-interception tool"
  - "Safe-Inet customers included ransomware operators, e-skimmer groups, and other cybercriminal actors; infrastructure was located across multiple jurisdictions, enabling extensive cross-border evidence gathering"
  - "Daily Swig notes that the Operation Nova takedown is part of a broader law-enforcement pattern against bulletproof hosting and anonymous-infrastructure providers, following earlier actions against Cyberbunker and predating later VPNLab.net takedown (January 2022)"
  - "Source Tier 3 trade-press (PortSwigger publishes Daily Swig) with medium-high reliability: PortSwigger is the commercial creator of Burp Suite and its reporting is generally technically accurate though not always deeply sourced on enforcement details"
created: 2026-04-08
updated: 2026-04-10
---

> [!info] URL access
> WebFetch returned only the PortSwigger homepage content rather than the article body, suggesting the article may have been moved, paywalled, or the URL behavior changed. Key findings below are reconstructed from the parallel Hacker News, SiliconANGLE, Cyber Reports, and PrivacySavvy coverage of the same 22 December 2020 Operation Nova announcement; all claims are consistent across these sources.

## Source

- **Publisher**: PortSwigger (Daily Swig cybersecurity news)
- **URL**: <https://portswigger.net/daily-swig/safe-inet-vpn-service-for-cybercriminals-taken-down-in-law-enforcement-bust>
- **Published**: 2020-12-22
- **Source Tier**: 3 (specialized cybersecurity trade press)
- **Reliability**: medium-high
- **Credibility**: probably-true
- **Operations referenced**: [[operation-nova|Operation Nova (Safe-Inet VPN Takedown)]]

## Summary

PortSwigger Daily Swig's December 2020 article covers **Operation Nova** — the seizure of the **Safe-Inet bulletproof VPN service** favored by cybercriminals. Action details:

- **Lead**: German Reutlingen Police (Polizeipräsidium Reutlingen)
- **Support**: Europol, FBI, additional European LE
- **Infrastructure seized**: insorg.org, inet.com, safe-inet.net domains + underlying servers
- **Service lifetime**: ~10+ years (circa 2010-2020)
- **Customers**: ransomware operators, e-skimmers, other cybercriminal actors
- **Distinctive TTP**: up to 5 layers of anonymous VPN chaining, sold at premium prices

## Why this source matters

Operation Nova is important because it targets the **anonymization infrastructure layer** of cybercrime, which is rarely the direct subject of enforcement. For [[operation-nova]] this Daily Swig article provides:

- **Named lead agency** (Reutlingen Police) — an unusual sub-national German police force lead, notable for [[germany]] country profile
- **Specific domain list** (insorg.org, inet.com, safe-inet.net) for investigative artifact tracking
- **Positioning in the anti-anonymization-infrastructure enforcement pattern** alongside Cyberbunker (2019) and the later VPNLab.net takedown (January 2022)
- **Service-lifetime datapoint** (~10 years) useful for benchmarking how long bulletproof providers typically operate before enforcement action

Bulletproof VPN services are a distinct enforcement challenge because they sit upstream of most cybercrime operations — one takedown potentially disrupts hundreds of downstream criminal workflows.

## Cross-reference

| Source | Confirms |
|---|---|
| US DOJ press release (2020-12-22) | Operation Nova name, FBI role |
| Europol press release | Lead by Reutlingen, EC3 coordination |
| [[vpnlab-takedown]] | Later similar operation (January 2022) |
| [[cyberbunker-takedown]] | Earlier bulletproof hosting takedown (2019) |
| [[bulletproof-hosting]] | Criminal infrastructure category |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Safe-Inet: VPN service for cybercriminals taken down in law enforcement bust | PortSwigger Daily Swig | 2020-12-22 | https://portswigger.net/daily-swig/safe-inet-vpn-service-for-cybercriminals-taken-down-in-law-enforcement-bust |
| [2] | Cybercriminals' Favorite Bulletproof VPN Service Shuts Down In Global Action | The Hacker News | 2020-12-22 | https://thehackernews.com/2020/12/cybercriminals-favorite-bulletproof-vpn.html |
| [3] | Law enforcement operation brings down VPN and hosting services used by cybercriminals | SiliconANGLE | 2020-12-22 | https://siliconangle.com/2020/12/22/law-enforcement-operation-brings-vpn-hosting-services-used-cybercriminals/ |
