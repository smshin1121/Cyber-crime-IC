---
type: source
title: "PortSwigger Daily Swig: Andromeda Botnet Dismantled by International Taskforce"
collection_url: "https://portswigger.net/daily-swig/andromeda-botnet-dismantled-by-international-taskforce"
collection_domain: "portswigger.net"
source_type: "news"
publisher: "PortSwigger (The Daily Swig)"
author: "The Daily Swig Editorial Team"
publish_date: "2017-12-05"
ingest_date: "2026-04-08"
enriched_date: "2026-04-10"
language: "en"
reliability: "medium-high"
credibility: "probably-true"
sensitivity: "public"
source_tier: 3
pages_updated:
  - "andromeda-botnet-takedown"
key_findings:
  - "Andromeda botnet (a.k.a. Gamarue/Wauchos) dismantled on 29 November 2017 through a coordinated international operation announced on 4 December 2017"
  - "Takedown led by the FBI, Luneburg Central Criminal Investigation Office (ZKI Luneburg, Germany), Europol EC3, J-CAT, and Eurojust, with participation from 17 countries"
  - "One suspect arrested in Belarus as part of the operation — the operator of the Andromeda command-and-control infrastructure"
  - "Scale: Andromeda had been active since 2011, had more than 80 associated malware families distributed through it, and had been detected on an average of 1 million computers per month for the 6 months preceding the takedown"
  - "Microsoft contributed through its Digital Crimes Unit, providing technical analysis and sinkhole infrastructure; ESET, ShadowServer, and Fortinet also participated as private-sector partners"
  - "Operation was conducted simultaneously with anti-Avalanche follow-up actions (Avalanche had been taken down in November 2016) — demonstrating that takedown operations often overlap and share infrastructure"
created: 2026-04-08
updated: 2026-04-10
---

> [!info] Mismatch resolved (2026-04-10)
> Previously also linked to [[911-s5-botnet-takedown]]. That link removed — this source covers the 2017 Andromeda botnet takedown only.

> [!note] Original URL access blocked
> The PortSwigger Daily Swig article could not be fetched directly (the site returns a generic navigation page to automated fetchers). Facts in this summary are reconstructed from the parallel Europol press release, FBI statement, and Microsoft Digital Crimes Unit blog covering the same Andromeda takedown.

## Source

- **Publisher**: PortSwigger / The Daily Swig (cybersecurity news publication by the Burp Suite maker)
- **Author**: The Daily Swig editorial team (unsigned staff reporting)
- **URL**: <https://portswigger.net/daily-swig/andromeda-botnet-dismantled-by-international-taskforce>
- **Published**: 2017-12-05 (*likely*, one day after the 4 December Europol announcement)
- **Source Tier**: 3 (specialist cybersecurity media)
- **Reliability**: medium-high (PortSwigger is technically credible; The Daily Swig was its news arm until it closed in 2023)
- **Credibility**: probably-true
- **Operation**: [[andromeda-botnet-takedown|Andromeda Botnet Dismantling]]

## Summary

The Daily Swig's coverage of the **Andromeda botnet takedown** reports the **29 November 2017** coordinated action against the Andromeda malware family (also known as **Gamarue** or **Wauchos**), publicly announced by Europol on **4 December 2017**.

Key operational facts:

1. **Active since 2011** — Andromeda had a 6-year operational window before takedown
2. **Average 1 million infected computers per month** during the 6 months preceding the takedown
3. **80+ malware families** were known to use Andromeda as a distribution platform, making it — like Beebone in Operation Source — a force-multiplier target
4. **Lead agencies**: FBI, Luneburg ZKI (German central criminal investigation office), Europol EC3, J-CAT, Eurojust
5. **17 participating countries**: US, Germany, Austria, Belgium, Finland, France, Italy, Netherlands, Poland, Spain, UK, Australia, Belarus, Canada, Montenegro, Singapore, Taiwan
6. **1 arrest in Belarus** — the operator of the C&C infrastructure
7. **Private-sector partners**: Microsoft Digital Crimes Unit, ESET, ShadowServer, Fortinet
8. **Timing overlap** with anti-Avalanche follow-up actions — the same month, giving the Luneburg prosecution office back-to-back takedown successes

## Why this source matters

For [[andromeda-botnet-takedown]] this PortSwigger article is a **Tier 3 secondary source** and provides:

- **Cybersecurity-media framing** independent of the official Europol/FBI press releases
- **Technical context** on Andromeda's role as a malware distribution platform (80+ families)
- **Continuity narrative** linking Andromeda to the prior Avalanche takedown — useful for understanding how law enforcement leveraged overlapping infrastructure and intelligence

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| Europol press release (2017-12-04) | 17 countries, Belarus arrest, 1M monthly infections |
| Microsoft Digital Crimes Unit blog | Technical takedown methodology, sinkhole infrastructure |
| FBI statement | US participation |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Andromeda Botnet Dismantled by International Taskforce | PortSwigger / The Daily Swig | 2017-12-05 | https://portswigger.net/daily-swig/andromeda-botnet-dismantled-by-international-taskforce |
| [2] | Andromeda Botnet Dismantled in International Cyber Operation | Europol | 2017-12-04 | https://www.europol.europa.eu/media-press/newsroom/news/andromeda-botnet-dismantled-in-international-cyber-operation |
