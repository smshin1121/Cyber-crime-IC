---
type: source
title: "BBC: Unverified Botnet Article (URL mismatch — cannot confirm 911 S5 coverage)"
collection_url: "https://www.bbc.com/news/technology-35028690"
collection_domain: "bbc.com"
source_type: "news"
publisher: "BBC News"
publish_date: "2009-03-13"
ingest_date: "2026-04-08"
enriched_date: "2026-04-10"
language: "en"
reliability: "low"
credibility: "possibly-true"
sensitivity: "public"
source_tier: 4
pages_updated: []
key_findings:
  - "URL-TOPIC MISMATCH: The stored URL (bbc.com/news/technology-35028690) does NOT cover the 2024 911 S5 botnet takedown. Reverse lookup and BBC URL conventions place article 35028690 in the late-2015 timeframe and unrelated to 911 S5"
  - "The BBC botnet article most commonly associated with the slug has historically been the 2009 BBC Click ethics story in which BBC journalists purchased a ~22,000-machine botnet for investigative purposes, later disabled and with affected users notified — per Threatpost, Silicon UK, The Register and ITPro coverage"
  - "The actual 911 S5 botnet dismantling was announced on 29 May 2024 by the US DOJ, FBI, DHS and Treasury, with participation from Germany, Singapore and Thailand; YunHe Wang was arrested in Singapore on 24 May 2024 (per DOJ press release and multiple secondary sources)"
  - "911 S5 had ensnared ~19 million Windows devices across 190+ countries between 2014 and 2022 through deceptive free VPN distributions (per FBI director and DOJ statements)"
  - "This source record is retained for traceability but should be treated as LOW confidence until a correct BBC article on 911 S5 is identified"
created: 2026-04-08
updated: 2026-04-10
---

> [!warning] URL-topic mismatch
> The stored URL (`bbc.com/news/technology-35028690`) could not be retrieved during enrichment (WebFetch blocked by BBC, WebSearch returned only unrelated 2009 BBC Click botnet stories). Based on BBC URL conventions (the `technology-35xxxxxx` range corresponds to late-2015 / early-2016 BBC Technology articles), this URL cannot cover the 2024 911 S5 takedown. The most likely historical BBC piece at this URL is an unrelated botnet story.

## Source

- **Publisher**: BBC News
- **URL**: <https://www.bbc.com/news/technology-35028690>
- **Published**: Unverified; URL format suggests 2015-12 or early 2016, but content could not be retrieved during enrichment
- **Source Tier**: 4 (mainstream general-interest press, unverified target article)
- **Reliability**: medium (BBC News baseline)
- **Credibility**: possibly-true (cannot assess without article content)
- **Operations referenced**: [[911-s5-botnet-takedown|911 S5 Botnet Dismantling]]

## Summary

This source record was created as part of a batch ingest linking BBC coverage to the [[911-s5-botnet-takedown]] operation page. During enrichment (2026-04-10) the URL returned blocked content, and the URL slug (`technology-35028690`) is inconsistent with a 2024 article on the 911 S5 takedown — BBC's numeric ID range 35xxxxxx corresponds to late 2015.

The 911 S5 operation itself was announced on 29 May 2024 and involved:

- **Lead**: US DOJ, FBI, DHS, Treasury (OFAC sanctions under the same action)
- **International partners**: Germany, Singapore, Thailand
- **Scale**: ~19 million infected Windows IP addresses across 190+ countries
- **Arrest**: YunHe Wang (35, Chinese national) arrested in Singapore on 2024-05-24
- **Vector**: Free-VPN deception (MaskVPN, DewVPN, PaladinVPN and others) hiding proxy backdoors

None of this is *directly* supported by the BBC URL currently on file.

## Why this source matters

- Documents a provenance gap that should be corrected when possible
- Highlights the need to replace this entry with a legitimate BBC 2024 article on 911 S5 (e.g., a `bbc.com/news/articles/...` 2024 slug) or downgrade the `source_count` on the operation page

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| US DOJ 2024-05-29 press release | Operation timeline, YunHe Wang arrest, country list |
| The Hacker News 2024-05 | 19M infected devices, FBI director quote |
| SecurityWeek 2024-05 | Chinese mastermind arrested in Singapore |
| US Treasury OFAC action 2024-05 | Sanctions on associated network |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | (Unverified original BBC article at stored slug) | BBC News | unverified | https://www.bbc.com/news/technology-35028690 |
| [2] | Justice Department Leads Effort to Dismantle 911 S5 Botnet | US DOJ | 2024-05-29 | https://www.justice.gov/opa/pr/justice-department-leads-effort-among-multinational-partners-dismantle-worlds-largest-botnet |
| [3] | Treasury Sanctions a Cybercrime Network Associated with the 911 S5 Botnet | US Treasury | 2024-05-28 | https://home.treasury.gov/news/press-releases/jy2375 |
| [4] | US Dismantles World's Largest 911 S5 Botnet with 19 Million Infected Devices | The Hacker News | 2024-05-30 | https://thehackernews.com/2024/05/us-dismantles-worlds-largest-911-s5.html |
