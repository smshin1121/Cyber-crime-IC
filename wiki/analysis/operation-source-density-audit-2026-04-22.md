---
title: Operation Source Density Audit (2026-04-22)
type: analysis
created: 2026-04-22
updated: 2026-04-22
summary: "Repository-wide audit of source density across operation pages, highlighting the scale of pages that remain below the 5-source minimum and the concentration of one-source follow-on operations."
source_count: 0
---
## Summary

This audit scanned all `wiki/operations/*.md` pages except `_index.md` and compared each page's `source_count` frontmatter value with the visible `## References` table density.

## Key Results

- Total operation pages audited: **1085**
- Pages with `source_count == 1`: **1021**
- Pages with `source_count < 5`: **1042**
- Pages with missing `source_count`: **7**
- Pages with `source_count >= 5`: **43**

## Concentration of One-Source Pages

The one-source pages are not evenly distributed.

- `operation-us-v-*`: **506**
- other `operation-*`: **490**
- non-`operation-*` slugs: **25**

This strongly suggests that most low-density pages are auto-generated or follow-on procedural pages rather than independently curated umbrella operations.

## Representative One-Source Pages

- [[marketplace-a-dekhtyarchuk-indictment]]
- [[operation-bakovia]]
- [[operation-cronos-phase1]]
- [[operation-checkmate-blacksuit]]
- [[operation-de-fr-online-fraud-group-2026]]
- [[operation-eur-600m-crypto-scam-network-2025]]
- [[operation-first-light-2024]]
- [[operation-jackal]]

## Pages Below Minimum but Above One Source

These still fail the 5-source standard and need review rather than automatic approval.

- [[carding-action-2020]] (`source_count: 3`)
- [[operation-endgame-phase2]] (`source_count: 3`)
- [[operation-rewired]] (`source_count: 4`)
- [[emotet-takedown]] (`source_count: 4`)
- [[goznym-takedown]] (`source_count: 3`)
- [[operation-chakra-iii]] (`source_count: 3`)
- [[qakbot-gallyamov-indictment]] (`source_count: 2`)

## Missing or Inconsistent Metadata

- Missing `source_count`: [[ddos-for-hire-sweep-2016]], [[hive-ransomware-takedown]], [[operation-delilah]], [[operation-lyrebird]], [[operation-nightfury]], [[operation-nova]], [[operation-shrouded-horizon]]
- `source_count` present but visible `## References` table missing or empty: [[bidencash-takedown]], [[carding-action-2020]], [[de-ch-crypto-mixer-takedown-2025]], [[operation-rewired]]

## Interpretation

The repository is still structurally dominated by low-density operation pages. In practice, this means `source_count: 1` should be treated as a presumptive review flag rather than as a satisfactory baseline. Many of these pages are likely valid as case follow-ons, but they do not currently meet the evidentiary standard expected of high-confidence operation pages.

## Recommended Triage Order

1. Reclassify or merge one-source `operation-us-v-*` follow-on pages into case records or umbrella operations where appropriate.
2. Repair metadata mismatches where `source_count` and visible references disagree.
3. Upgrade genuinely important umbrella operations from 1-4 sources to 5+ sources.
4. Only retain one-source operation pages as standalone records when they document a uniquely material enforcement event that cannot yet be merged or substantiated further.
