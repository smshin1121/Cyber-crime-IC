---
type: source
title: "Europol: Andromeda Botnet Dismantled in International Cyber Operation"
collection_url: https://www.europol.europa.eu/media-press/newsroom/news/andromeda-botnet-dismantled-in-international-cyber-operation
collection_domain: europol.europa.eu
source_type: press-release
publisher: Europol
publish_date: 2017-12-04
ingest_date: 2026-04-08
enriched_date: 2026-04-10
language: en
reliability: high
credibility: probably-true
sensitivity: public
source_tier: 2
pages_updated:
  - andromeda-botnet-takedown
key_findings:
  - "Europol announced on 2017-12-04 the dismantling of the Andromeda (a.k.a. Gamarue) botnet, characterised as one of the longest-running malware families in existence; coordinated law-enforcement action occurred on 2017-11-29"
  - "During a 48-hour sinkhole window, authorities captured ~2 million unique victim IP addresses from 223 countries; in the 6 months preceding the takedown Andromeda was detected or blocked on an average of over 1 million machines per month"
  - "Operational results: 1,500 malicious domains sinkholed; 1 suspect arrested in Belarus"
  - "Lead agencies: FBI, Europol EC3, Luneburg Central Criminal Investigation Inspectorate (Germany), Eurojust, and J-CAT (Joint Cybercrime Action Task Force)"
  - "EU member states participating: Austria, Belgium, Finland, France, Italy, Netherlands, Poland, Spain, UK; non-EU partners: Australia, Belarus, Canada, Montenegro, Singapore, Taiwan"
  - "Notable IC feature: Belarus played both as arrest location and participating state — a rare example of Belarusian cybercrime cooperation with Western agencies; Taiwan's inclusion (alongside Singapore) signals East Asian partner involvement"
created: 2026-04-08
updated: 2026-04-10
duplicate_of: "[[2017-12-04_europol-europa-eu_andromeda-botnet-dismantled-in-international-cyber-operation]]"
duplicate_reason: same_collection_url
duplicate_key: https://www.europol.europa.eu/media-press/newsroom/news/andromeda-botnet-dismantled-in-international-cyber-operation
duplicate_normalized_at: 2026-04-26
raw_path: raw/press-releases/europol-andromeda-botnet-dismantling.md
text_status: source-digest
storage_mode: source-digest
content_hash: sha256:bd9ac4086158dc6f5419016a5e6459c6ff34c0c4cdb41ea78bc268dff9241a7f
word_count: 336
extraction_date: 2026-04-28
---
## Source

- **Publisher**: Europol (European Union Agency for Law Enforcement Cooperation)
- **URL**: <https://www.europol.europa.eu/media-press/newsroom/news/andromeda-botnet-dismantled-in-international-cyber-operation>
- **Published**: 2017-12-04
- **Source Tier**: 2 (official supranational agency press release)
- **Reliability**: high (Europol is the coordinating body and primary source for operational facts)
- **Credibility**: probably-true (Europol press releases are authoritative for operational numbers they coordinate)
- **Operations referenced**: [[andromeda-botnet-takedown|Andromeda / Gamarue Botnet Takedown]]

## Summary

Europol's press release documents the **Andromeda (Gamarue) botnet dismantling**, executed on **2017-11-29** and announced on **2017-12-04**. Headline facts:

1. **Scale**: ~2 million unique victim IPs from 223 countries observed during a 48-hour sinkhole; >1 million machines/month detected in the 6 months before takedown
2. **Longevity**: Andromeda characterized as *"one of the longest-running malware families in existence"* — active since at least 2011
3. **Operational results**: 1,500 malicious domains sinkholed; 1 arrest in Belarus
4. **Lead agencies**: FBI, Europol EC3, German Luneburg Criminal Investigation Inspectorate, Eurojust, J-CAT
5. **Participating countries** — EU: Austria, Belgium, Finland, France, Italy, Netherlands, Poland, Spain, UK; non-EU: Australia, Belarus, Canada, Montenegro, Singapore, Taiwan
6. **Mechanism**: Sinkholing combined with coordinated arrest; follow-up victim remediation via national CERTs

## Why this source matters

For [[andromeda-botnet-takedown]] this Europol press release is the **primary official source**:

- Authoritative operational numbers (domains, IPs, countries) that later news coverage cites
- Definitive list of participating agencies and countries (critical for SNA edge construction in the operation page's `edges` block)
- Confirmation of **Belarusian participation** — significant because Belarus is rarely reported as cooperating in cybercrime takedowns with Western agencies
- Confirmation of **Taiwan participation** — significant because Taiwan is often excluded from multilateral cooperation due to diplomatic recognition issues

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| FBI press release (2017-12-04) | US perspective, sinkhole mechanics |
| Microsoft Digital Crimes Unit blog | Private-sector technical role (sinkhole infrastructure) |
| German BKA press release | National-level arrest coordination |
| [[bleeping-computer-andromeda-botnet-takedown]] (if present) | Independent news coverage |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Andromeda botnet dismantled in international cyber operation | Europol | 2017-12-04 | https://www.europol.europa.eu/media-press/newsroom/news/andromeda-botnet-dismantled-in-international-cyber-operation |
| [2] | Microsoft and Law Enforcement Disrupt Andromeda Botnet | Microsoft DCU | 2017-12-04 | https://blogs.microsoft.com/on-the-issues/2017/12/04/microsoft-assists-law-enforcement-help-disrupt-andromeda-botnet/ |
| [3] | Andromeda Botnet Gets Crushed | BleepingComputer | 2017-12-04 | https://www.bleepingcomputer.com/news/security/andromeda-botnet-gets-crushed-in-eu-us-law-enforcement-operation/ |
