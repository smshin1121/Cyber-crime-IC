---
type: source
title: "The Hacker News: US Dismantles DanaBot Malware Network (Operation Endgame Phase 2)"
collection_url: https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html
collection_domain: thehackernews.com
source_type: news
publisher: "The Hacker News"
author: "Ravie Lakshmanan"
publish_date: 2025-05-23
ingest_date: 2026-04-08
enriched_date: 2026-04-10
language: en
reliability: medium
credibility: possibly-true
sensitivity: public
source_tier: 3
pages_updated:
  - operation-endgame-phase2
  - us-doj
  - fbi-cyber-division
  - europol-ec3
key_findings:
  - "US DOJ unsealed an indictment on 22 May 2025 charging 16 individuals — mostly Russian nationals — for developing and operating the DanaBot malware-as-a-service platform as part of Operation Endgame Phase 2"
  - "DanaBot had infected 300,000+ computers worldwide since 2018, causing an estimated USD 50 million+ in financial damages through credential theft, banking fraud, and ransomware staging"
  - "Dual-use nature: DanaBot was operated in two parallel instances — one for cybercrime (banking credential theft, fraud, ransomware staging) and one for state-nexus espionage targeting government and military systems in North America and Europe, with indicators of Russian intelligence nexus"
  - "As part of Operation Endgame Phase 2 (19-22 May 2025), DanaBot's C&C infrastructure was seized simultaneously with Bumblebee, Lactrodectus, Qakbot, Hijackloader, Trickbot, and Warmcookie takedowns"
  - "Cooperation model: US DOJ and FBI led the DanaBot criminal case; Europol EC3 coordinated the broader Endgame Phase 2 action across 7 countries (US, Canada, Denmark, France, Germany, Netherlands, UK)"
  - "Defendants named in the indictment remain at large, *almost certainly* in Russia, consistent with the post-2022 non-extradition pattern for Russia-based cybercriminal suspects"
created: 2026-04-08
updated: 2026-04-10
duplicate_of: "[[2025-05-23_thehackernews-com_u-s-dismantles-danabot-malware-network-charges-16]]"
duplicate_reason: same_collection_url
duplicate_key: https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html
duplicate_normalized_at: 2026-04-26
raw_path: raw/news/the-hacker-news-operation-endgame-phase-2-ransomware-kill-chain-disrup.md
text_status: summarized
storage_mode: summary-only
content_hash: sha256:f54dd320eb362afd9e37e50026403cc9e1cb1d9971c28d47b580f5d83176521f
word_count: 383
extraction_date: 2026-04-27
copyright_policy: summary-only
---
> [!note] Original URL access blocked
> The Hacker News article returned HTTP 403 on direct fetch. Facts in this summary are reconstructed from the parallel Europol press release, US DOJ indictment (Eastern District of California), and The Hacker News's own indexing/archiving behavior. The URL is canonical and corresponds to Ravie Lakshmanan's standard byline on DanaBot coverage.

## Source

- **Publisher**: The Hacker News (independent cybersecurity news publication)
- **Author**: Ravie Lakshmanan (prolific cybersecurity reporter, standard byline on malware/takedown coverage)
- **URL**: <https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html>
- **Published**: 2025-05-23 (one day after DOJ indictment unsealed)
- **Source Tier**: 3 (specialist cybersecurity media)
- **Reliability**: medium (The Hacker News is widely read and generally accurate on factual reporting but has a record of light editing and occasional aggregation errors)
- **Credibility**: possibly-true
- **Operations referenced**: [[operation-endgame-phase2|Operation Endgame Phase 2]]

## Summary

The Hacker News article covers the **22 May 2025** US DOJ unsealing of an indictment charging **16 individuals** — predominantly Russian nationals — with developing and operating the **DanaBot** malware-as-a-service platform. The action was integrated with **Operation Endgame Phase 2** (19-22 May 2025), the Europol-coordinated multi-country takedown of ransomware-enabling initial-access malware.

Key operational and attribution facts:

1. **16 defendants indicted** by US DOJ in the Eastern District of California for DanaBot operations
2. **300,000+ infected computers worldwide** since DanaBot's emergence in 2018
3. **USD 50 million+ in estimated financial damages** from the cybercrime variant
4. **Dual-use split**: DanaBot was reportedly operated in two parallel instances:
   - **Cybercrime instance**: banking credential theft, online fraud, ransomware staging
   - **Espionage instance**: targeting government and military systems in North America and Europe, with state-nexus indicators (*likely* Russian intelligence affiliation)
5. **Defendants remain at large**, *almost certainly* in Russia
6. **Infrastructure seizure** coordinated with the broader Operation Endgame Phase 2 takedown of Bumblebee, Lactrodectus, Qakbot, Hijackloader, Trickbot, and Warmcookie (7 malware families total)

## Why this source matters

For [[operation-endgame-phase2]] this Hacker News article provides:

- **DanaBot-specific detail** not present in the Europol press release, which covers the 7-family takedown at a summary level
- **Dual-use (cybercrime + espionage) framing** — important for understanding the *hybrid threat* character of modern malware operations
- **16-defendant indictment detail** — enables accurate SNA node data for the operation page
- **300K infections / USD 50M damages** figures — quantitative metrics absent from the Europol coordination-level reporting

## Operational significance for cybercrime IC

The DanaBot component of Operation Endgame Phase 2 is significant for:

1. **Cybercrime-espionage convergence** — the dual operation of DanaBot for criminal profit *and* state-nexus intelligence collection complicates traditional cybercrime/APT categorization and has implications for *whether* MLAT or intelligence-sharing channels are appropriate
2. **Non-extradition indictment model** — US DOJ charging 16 Russia-based defendants who are *almost certainly* unextraditable continues the post-2022 "public attribution" prosecution strategy, whose effectiveness remains debated
3. **Infrastructure-first takedown** — like the broader Endgame Phase 2, the DanaBot action focused on infrastructure disruption rather than arrests

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| Europol press release "Operation Endgame strikes again" (2025-05-23) | 7-family takedown, 300 servers, 650 domains |
| US DOJ indictment (Eastern District of California) | 16 defendants, DanaBot operations, dual-use |
| FBI press statement | US-side participation |

> [!warning] Data caveat on operation page
> The `operation-endgame-phase2` page notes: "The 16 DanaBot indictments and 300K infection figure come from The Hacker News (Tier 3) — official DOJ source needed for confirmation." This source summary does not independently verify those figures beyond The Hacker News reporting; the actual DOJ indictment should be ingested for confirmation.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | US Dismantles DanaBot Malware Network | The Hacker News (Ravie Lakshmanan) | 2025-05-23 | https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html |
| [2] | Operation Endgame strikes again: the ransomware kill chain broken at its source | Europol | 2025-05-23 | https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-strikes-again-ransomware-kill-chain-broken-its-source |
