---
type: source
title: "BBC: 911 S5 Botnet Dismantling"
collection_url: https://www.bbc.com/news/technology-32218381
collection_domain: bbc.com
source_type: news
publisher: BBC
author: ""
publish_date: 2024-05-29
ingest_date: 2026-04-08
enriched_date: 2026-04-10
language: en
reliability: medium
credibility: possibly-true
sensitivity: public
source_tier: 4
pages_updated:
  - 911-s5-botnet-takedown
key_findings:
  - "The US Department of Justice on 29 May 2024 announced the dismantling of the 911 S5 residential-proxy botnet, described by officials as 'likely the world's largest botnet ever', comprising approximately 19 million compromised IP addresses across more than 190 countries (per DOJ press materials)"
  - "YunHe Wang, a 35-year-old Chinese national, was arrested in Singapore on 24 May 2024 as the alleged administrator who ran 911 S5 from 2014 until July 2022; Wang was charged in the Eastern District of Texas with conspiracy to commit computer fraud, wire fraud, and money laundering — facing a maximum 65-year sentence if convicted on all counts"
  - "DOJ alleges 911 S5 enabled billions of dollars of financial fraud including at least US$5.9 billion in fraudulent US pandemic-relief (EIDL/PPP) claims routed through proxies sold on 911 S5, plus bomb threats, child-exploitation material, and harassment"
  - "Coordinated law-enforcement action seized 23 domains and more than 70 servers across the US, Singapore, Thailand and Germany; cooperation involved the FBI, DOJ, DoD Criminal Investigative Service, and the Singapore Police Force, Thai and German authorities"
  - "The takedown illustrated the operational value of Singapore as an arrest venue for Chinese nationals suspected of cybercrime against US victims, given the absence of a US-China extradition treaty"
created: 2026-04-08
updated: 2026-04-10
raw_path: raw/news/bbc-911-s5-botnet-dismantling.md
text_status: summarized
content_hash: sha256:426d65151ecd5840fa4981c990b8768b122c9a75d2ae5a3366e247c85cf8613f
word_count: 1383
stored_word_count: 80
extraction_date: 2026-04-25
last_fetcher: urllib
copyright_policy: summary-only
---
> [!warning] URL verification
> The `collection_url` (`bbc.com/news/technology-32218381`) could not be verified via WebFetch or WebSearch (BBC blocks fetch; search returned no article match). The numeric ID format suggests a 2015-era BBC article, which would predate the 2024 911 S5 takedown. The original file may have mis-linked the URL during ingest. Key findings below are sourced from corroborating reporting on the same operation (Bleeping Computer, CBS News, The Hacker News, DOJ press release) and should be treated as *highly likely* accurate descriptions of the event itself, not necessarily of the BBC article behind this URL.

## Source

- **Publisher**: BBC
- **URL**: <https://www.bbc.com/news/technology-32218381>
- **Published**: 2024-05-29 (assumed — date of DOJ announcement; BBC article itself not retrievable)
- **Source Tier**: 4 (mainstream generalist news, unverified URL)
- **Reliability**: medium
- **Credibility**: possibly-true (URL unverifiable; content inferred from parallel reporting)
- **Operations referenced**: [[911-s5-botnet-takedown|911 S5 Botnet Takedown]]

## Summary

This source was originally filed as BBC coverage of the **911 S5 residential-proxy botnet takedown**. The DOJ announcement on 29 May 2024 described 911 S5 as *almost certainly* the largest botnet ever dismantled by number of infected IPs — ~19 million compromised devices across 190+ countries, operated from 2014 to mid-2022 by a Chinese national, YunHe Wang, who was arrested in Singapore on 24 May 2024.

The botnet enabled fraudulent access to US pandemic-relief programs (with estimated US$5.9 billion in EIDL/PPP claims attributable to 911 S5 proxies), as well as bomb threats, CSAM distribution, and targeted harassment campaigns. Coordinated seizures took down 23 domains and 70+ servers.

## Why this source matters

For the IC analysis on [[911-s5-botnet-takedown]], a BBC article would provide mainstream-media corroboration of the DOJ indictment and would be relevant for European audience reach. However, because the URL cannot be verified, this entry currently serves as a placeholder — the parallel coverage from BleepingComputer, CBS News, and The Hacker News carries the weight of evidence.

## Cross-reference

| Source | Confirms |
|---|---|
| US DOJ press release (2024-05-29) | Indictment, arrest, charges, scale |
| BleepingComputer | 19M IPs, 23 domains, 70+ servers |
| CBS News | YunHe Wang, Singapore arrest |
| [[the-hacker-news-911-s5-botnet-dismantling]] (if exists) | Technical details |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | (Unverified) 911 S5 Botnet Dismantling | BBC | 2024-05-29 | https://www.bbc.com/news/technology-32218381 |
| [2] | US Dismantles World's Largest 911 S5 Botnet with 19 Million Infected Devices | The Hacker News | 2024-05-30 | https://thehackernews.com/2024/05/us-dismantles-worlds-largest-911-s5.html |
| [3] | Feds take down one of world's largest malicious botnets and arrest its administrator | CBS News | 2024-05-29 | https://www.cbsnews.com/news/feds-largest-malicious-botnets-arrest-administrator/ |
| [4] | US dismantles 911 S5 residential proxy botnet used for cyberattacks, arrests admin | BleepingComputer | 2024-05-29 | https://www.bleepingcomputer.com/news/security/us-dismantles-911-s5-residential-proxy-botnet-used-for-cyberattacks-arrests-admin/ |
