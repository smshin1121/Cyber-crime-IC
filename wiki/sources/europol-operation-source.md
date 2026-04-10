---
type: source
title: "Europol: International Police Operation Targets Polymorphic Beebone Botnet (Operation Source)"
collection_url: "https://www.europol.europa.eu/media-press/newsroom/news/international-police-operation-targets-polymorphic-beebone-botnet"
collection_domain: "europol.europa.eu"
source_type: "press-release"
publisher: "Europol"
author: "Europol Press Office"
publish_date: "2015-04-09"
ingest_date: "2026-04-08"
enriched_date: "2026-04-10"
language: "en"
reliability: "high"
credibility: "confirmed"
sensitivity: "public"
source_tier: 2
pages_updated:
  - "operation-source"
  - "europol-ec3"
  - "j-cat"
  - "dutch-nhtcu"
  - "fbi"
  - "netherlands"
key_findings:
  - "Europol EC3, the Joint Cybercrime Action Taskforce (J-CAT), and the Dutch National High Tech Crime Unit (NHTCU) sinkholed the Beebone (W32/Worm-AAEH) polymorphic botnet on 8 April 2015 in a coordinated international action"
  - "The botnet was neutralized by registering, suspending, or seizing command-and-control (C&C) domains used for malware communication — sinkhole methodology rather than server seizure"
  - "5 million unique polymorphic samples of the W32/Worm-AAEH family identified; 205,000+ samples collected from 23,000 systems across 195 countries during 2013-2014"
  - "~12,000 computers actively infected at time of takedown, though Europol noted many additional infections likely existed; United States had the most infections, followed by Japan, India, and Taiwan"
  - "The operation used Beebone as a distribution vector for other malware: financial credential stealers, ransomware, rootkits, and fake antivirus software — making the takedown a force multiplier against multiple malware families"
  - "Participating organizations: Europol EC3 (coordination), J-CAT, Dutch NHTCU, FBI, US National Cyber Investigative Joint Task Force, Eurojust (judicial coordination), plus private-sector partners Intel Security, Kaspersky Lab, Shadowserver, F-Secure, Symantec, and TrendMicro"
  - "Operation Source is an early example of the public-private-partnership (PPP) model for botnet takedowns that would later be refined in Operations Avalanche (2016), Andromeda (2017), and Endgame (2024-2025)"
created: 2026-04-08
updated: 2026-04-10
---

## Source

- **Publisher**: Europol
- **Author**: Europol Press Office (institutional)
- **URL**: <https://www.europol.europa.eu/media-press/newsroom/news/international-police-operation-targets-polymorphic-beebone-botnet>
- **Published**: 2015-04-09
- **Source Tier**: 2 (Tier A — official international agency)
- **Reliability**: high (primary official source from the coordinating body)
- **Credibility**: confirmed
- **Operations referenced**: [[operation-source|Operation Source (Beebone Botnet Takedown)]]

## Summary

The Europol press release announces **Operation Source**, the coordinated takedown of the **polymorphic Beebone botnet** (also known as **W32/Worm-AAEH**) on **8 April 2015**. The operation was led by **Europol's European Cybercrime Centre (EC3)** with the **Joint Cybercrime Action Taskforce (J-CAT)** and the **Dutch National High Tech Crime Unit (NHTCU)** as principal operational partners, and supported by the **FBI**, the **US National Cyber Investigative Joint Task Force**, **Eurojust**, and a consortium of private cybersecurity firms.

The takedown methodology was **domain sinkholing** — registering, suspending, or seizing domains used by the botnet for command-and-control communication — rather than physical server seizure. This reflected the polymorphic nature of the malware, which rotated its infrastructure rapidly.

Key technical metrics:
- **5 million unique polymorphic samples** of the W32/Worm-AAEH family
- **205,000+ samples** collected from **23,000 systems** across **195 countries** during 2013-2014 analysis period
- **~12,000 computers** actively infected at the time of takedown
- Top affected countries: **United States, Japan, India, Taiwan**

Beebone was significant because it served as a **distribution vector** for other malware — financial credential stealers, ransomware, rootkits, and fake antivirus — making its disruption a force multiplier against multiple criminal ecosystems simultaneously.

## Why this source matters

For [[operation-source]] this Europol press release is the **only Tier-2 primary source** currently in the wiki and provides:

- **Authoritative confirmation** of the participating agencies and private-sector partners
- **Sinkhole methodology detail** — important for understanding the technical approach
- **Force-multiplier framing** — Beebone's role as a distributor for other malware is the *strategic* justification for the takedown
- **Historical reference point** — Operation Source is one of the earliest large-scale EU-led botnet takedowns and established the public-private-partnership model refined in later operations
- **7 private-sector partners** — an unusually broad industry coalition for a 2015-era takedown

## Operational significance for cybercrime IC

Operation Source is a reference case for:

1. **Public-private partnership (PPP) model** — 7 private security vendors participated, well beyond the typical 1-2 vendor partnerships of earlier takedowns
2. **Sinkhole-over-seize methodology** for polymorphic botnets where physical server seizure is infeasible due to rapid infrastructure rotation
3. **Force-multiplier justification** — the value proposition is not just shutting down one botnet but disrupting the distribution path for many malware families
4. **J-CAT operational debut** — one of the earliest major operations by the Joint Cybercrime Action Taskforce established in 2014

## Cross-reference with other sources

No additional sources for Operation Source are currently in the wiki. This is a **single-source operation** in the current dataset and should be flagged for lower source diversity.

| Source | Confirms |
|---|---|
| Europol press release (this source) | All operation facts |
| Intel Security / McAfee Labs reporting (external) | Technical W32/Worm-AAEH analysis |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | International Police Operation Targets Polymorphic Beebone Botnet | Europol | 2015-04-09 | https://www.europol.europa.eu/media-press/newsroom/news/international-police-operation-targets-polymorphic-beebone-botnet |
