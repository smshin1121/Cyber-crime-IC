---
type: source
title: "Europol: Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain (Carbanak/Cobalt)"
collection_url: https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain
collection_domain: europol.europa.eu
source_type: press-release
publisher: Europol
author: "Europol Press Office"
publish_date: 2018-03-26
ingest_date: 2026-04-08
enriched_date: 2026-04-10
language: en
reliability: high
credibility: confirmed
sensitivity: public
source_tier: 2
pages_updated:
  - carbanak-cobalt-takedown
  - europol-ec3
  - spanish-national-police
  - fbi
  - romania
  - belarus
  - taiwan
key_findings:
  - "Alleged mastermind of the Carbanak/Cobalt cybercrime group arrested in Alicante, Spain on 26 March 2018 by the Spanish National Police (Policía Nacional) following a multi-year joint investigation"
  - "Group caused cumulative losses of over EUR 1 billion to the financial industry since 2013; Cobalt malware alone enabled thefts of up to EUR 10 million per heist"
  - "Over 100 financial institutions targeted across more than 40 countries — a significant scale for a single cybercriminal enterprise"
  - "International cooperation partners: Spanish National Police (lead), Europol EC3 (coordination), US FBI, Romanian authorities, Moldovan authorities, Belarusian authorities, Taiwanese authorities, and private-sector cybersecurity firms"
  - "Malware evolution timeline: Anunak (late 2013) ??Carbanak (2014-2016) ??Cobalt Strike-based custom tooling (post-2016) ??illustrating the group''s continuous tool development"
  - "Modus operandi: spear-phishing emails with malicious attachments sent to bank employees, followed by lateral movement to internal banking networks and ATM-controlling servers to execute ''jackpotting'' cash withdrawals and SWIFT-style account manipulations"
created: 2026-04-08
updated: 2026-04-18
defendant_names:
  - "Billion Cyber Bank Robbery"
duplicate_of: "[[2018-03-01_europol-europa-eu_mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain]]"
duplicate_reason: same_collection_url
duplicate_key: https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain
duplicate_normalized_at: 2026-04-26
raw_path: raw/press-releases/europol-carbanakcobalt-mastermind-arrest.md
text_status: source-digest
storage_mode: source-digest
content_hash: sha256:de86fb9530e7f16422e1d99b4602f39fa567159daa3d099eb3cef5167f1f146b
word_count: 347
extraction_date: 2026-04-28
---
## Source

- **Publisher**: Europol (European Union Agency for Law Enforcement Cooperation)
- **Author**: Europol Press Office (institutional, unsigned)
- **URL**: <https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain>
- **Published**: 2018-03-26
- **Source Tier**: 2 (Tier A — official international agency)
- **Reliability**: high (primary official source from the coordinating body)
- **Credibility**: confirmed
- **Operations referenced**: [[carbanak-cobalt-takedown|Carbanak/Cobalt Mastermind Arrest]]

## Summary

The Europol press release announces the **arrest of the alleged mastermind** behind the **Carbanak** and **Cobalt** malware campaigns in **Alicante, Spain** on **26 March 2018**. The arrest was executed by the Spanish National Police with coordination from Europol's European Cybercrime Centre (EC3) and joint investigative support from the US FBI and law enforcement in Romania, Moldova, Belarus, and Taiwan.

Key operational facts:

1. **EUR 1 billion+ in cumulative losses** across 100+ financial institutions in 40+ countries since 2013
2. **Malware evolution**: Anunak (2013) → Carbanak (2014-2016) → Cobalt Strike customization (post-2016) — the group continuously updated its tooling
3. **Modus operandi**: targeted spear-phishing against bank employees, followed by deep lateral movement inside bank networks to access ATM management systems (enabling "jackpotting" — commanding ATMs to dispense cash on demand) and payment-transfer systems
4. **Multi-year joint investigation** — the arrest was the culmination of a sustained multi-country effort rather than a single-event operation
5. **Private-sector contribution** — cybersecurity companies (notably Kaspersky Lab, which originally named the Carbanak group in 2015) provided technical intelligence throughout

## Why this source matters

For [[carbanak-cobalt-takedown]] this Europol press release is the **primary Tier-2 source** and provides:

- **Authoritative confirmation** of the 100+ institutions / 40+ countries / EUR 1B loss figures (previously reported by Kaspersky)
- **Named cooperating countries** — Spain (lead arrest), US, Romania, Moldova, Belarus, Taiwan — enabling accurate SNA edge-data population on the operation page
- **Europol EC3 coordination role** — confirmed, not merely inferred
- **Malware-lineage narrative** (Anunak → Carbanak → Cobalt) — important for understanding the group's *persistence* across multiple takedown attempts
- **Non-arrest of other group members** — the single mastermind arrest did not dismantle the group, which the press release implicitly acknowledges

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| Kaspersky Lab "Carbanak APT" report (2015) | Original malware attribution, initial $1B estimate |
| US DOJ / FBI statements | US participation in the investigation |
| Spanish Policía Nacional press conference | Arrest location, Alicante |

The Europol press release is the *most authoritative* source for the 2018 arrest itself. The Kaspersky 2015 report should be consulted for the technical malware details.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain | Europol | 2018-03-26 | https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain |
| [2] | Carbanak APT: The Great Bank Robbery | Kaspersky Lab (technical report) | 2015-02 | https://securelist.com/the-great-bank-robbery-the-carbanak-apt/68732/ |
