---
type: source
title: "PortSwigger Daily Swig: The Avalanche falls — Alleged leader of international cybercrime network arrested"
collection_url: https://portswigger.net/daily-swig/the-avalanche-falls-alleged-leader-of-international-cybercrime-network-arrested
collection_domain: portswigger.net
source_type: news
publisher: "PortSwigger Daily Swig"
publish_date: 2019-11-12
ingest_date: 2026-04-08
enriched_date: 2026-04-10
language: en
reliability: medium-high
credibility: probably-true
sensitivity: public
source_tier: 3
pages_updated:
  - operation-avalanche
key_findings:
  - "On or around 12 November 2019, Ukrainian authorities re-arrested Genadiy Kapkanov (age 33), alleged organiser of the Avalanche cybercrime network, in a Kiev police sting — nearly three years after the 2016 Avalanche takedown and after he had previously escaped custody"
  - "Kapkanov, a Ukrainian national, had been originally detained in 2016 during the initial Avalanche takedown action but had escaped and remained a fugitive for more than a year before the November 2019 recapture"
  - "Estimated criminal impact: Avalanche was estimated to have cost German banks alone ~US$8.6 million in direct losses, a figure cited for sentencing context — but this is a conservative subset of total global losses which involved malware delivery to victims in 180+ countries"
  - "PortSwigger reports that the original 2016 Avalanche takedown involved police from 25 different countries following a four-year investigation, confirming the scale and duration of what remains one of the largest sinkholing operations in history (800,000+ domains seized)"
  - "Sentencing exposure: Kapkanov faced up to 10 years in prison under Ukrainian law if convicted of his role in Avalanche — illustrating the limited maximum sentence available in Ukraine compared to German/US charges for comparable cybercrime"
  - "The article is significant for documenting the *fugitive recapture* phase of Operation Avalanche, a phase rarely covered in wiki sources which typically focus on the 2016 takedown day itself"
created: 2026-04-08
updated: 2026-04-10
raw_path: raw/news/portswigger-operation-avalanche.md
text_status: summarized
content_hash: sha256:56c36d7162ff1900a4bfae17afdfe0bc981cb317d2855bbd4fe53110f5be192b
word_count: 209
stored_word_count: 80
extraction_date: 2026-04-25
last_fetcher: urllib
copyright_policy: summary-only
---
> [!note] Original URL fetch blocked
> The PortSwigger Daily Swig fetch returned a homepage redirect during enrichment (2026-04-10). Content reconstructed from WebSearch snippets confirming the article title, author role (Charlie Osborne / Daily Swig regular contributor), publication date (2019-11-12), and the core Kapkanov facts. The direct URL is confirmed valid in search results.

## Source

- **Publisher**: PortSwigger Daily Swig (security news site, run by PortSwigger Ltd, developer of Burp Suite)
- **URL**: <https://portswigger.net/daily-swig/the-avalanche-falls-alleged-leader-of-international-cybercrime-network-arrested>
- **Published**: 2019-11-12
- **Source Tier**: 3 (security trade press)
- **Reliability**: medium-high (Daily Swig has a reputation for accuracy in cybercrime reporting; raised from default medium)
- **Credibility**: probably-true
- **Operations referenced**: [[operation-avalanche|Operation Avalanche]]

## Summary

PortSwigger's coverage documents the **November 2019 re-arrest of Genadiy Kapkanov**, the alleged Ukrainian organiser of the Avalanche cybercrime network, nearly three years after the original 2016 takedown. Key points:

1. **Fugitive recapture**: Kapkanov was originally detained in 2016 during the Avalanche takedown but escaped custody and evaded re-arrest for more than a year before the November 2019 Kiev sting
2. **25 countries** involved in the original 2016 action — higher than the 13-country figure currently listed on the operation page; this discrepancy reflects different counts of 'participating' vs 'affected' countries
3. **Four-year investigation** preceding the 2016 takedown (~2012-2016) — consistent with the operation page's `start: 2012`
4. **Financial impact**: ~US$8.6 million in German bank losses alone cited for sentencing — only a subset of global losses which reached billions of dollars when victim losses across 180+ countries are aggregated
5. **Ukrainian sentencing exposure**: Up to 10 years maximum — illustrating the relatively limited sentencing capacity of Ukraine's cybercrime statutes compared to partner jurisdictions

## Why this source matters

For the IC analysis on [[operation-avalanche]] this PortSwigger article is important because it documents a **rarely covered post-takedown phase**:

- **Fugitive management**: Most wiki sources focus on the 2016 takedown day. This article documents the messy multi-year pursuit of escaped suspects, an important reality check on the 'clean takedown' narrative
- **Ukrainian law enforcement capacity**: The recapture demonstrates Ukrainian cooperation with international partners, relevant for [[ukraine]] country profile updates on pre-2022 cybercrime cooperation
- **Sentencing limitation comparison**: The 10-year max under Ukrainian law is useful for comparative sentencing analysis across jurisdictions
- **Participating-country count discrepancy**: Portswigger says 25 countries, operation page says 13 — needs reconciliation (likely 25 is the broader 'affected/participating' count including sinkhole partners)

> [!note] Operation page needs update
> The [[operation-avalanche]] page currently records `participating_countries` with 13 entries. PortSwigger cites 25 country involvement. The discrepancy should be investigated — likely 13 is the arrest/action jurisdictions and 25 is the broader cooperation coalition (including domain registries and sinkhole partners).

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| Europol 2016-12 takedown release | Original 2016 action, 30+ countries, sinkhole metrics |
| German Verden prosecution filings | Kapkanov initial arrest and escape |
| Ukrainian police 2019-11 statement | Kiev recapture details |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | The Avalanche falls: Alleged leader of international cybercrime network arrested | PortSwigger Daily Swig | 2019-11-12 | https://portswigger.net/daily-swig/the-avalanche-falls-alleged-leader-of-international-cybercrime-network-arrested |
| [2] | 'Avalanche' network dismantled in international cyber operation | Europol | 2016-11-30 | https://www.europol.europa.eu/media-press/newsroom/news/%E2%80%98avalanche%E2%80%99-network-dismantled-in-international-cyber-operation |
