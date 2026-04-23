---
title: "Multi-Country Low-Source Operation Survey (2026-04-22)"
type: analysis
created: 2026-04-22
updated: 2026-04-22
summary: "Survey queue for operation pages below the 5-source floor, prioritised for non-DOJ enrichment across 10 target countries plus backbone regional sources."
source_count: 0
---
## Summary

This survey isolates operation pages that still sit below the `5`-source floor and should be enriched rather than passed.
Pages already at `5+` sources are excluded from the search queue.
The search strategy is intentionally non-US-first to reduce current DOJ concentration.

## Survey Rules

- Scope: `wiki/operations/*.md` only.
- Pass condition: `source_count >= 5`.
- Search buckets: `retain_and_enrich`, `high_risk_review`.
- Country frame: Germany, France, United Kingdom, Netherlands, Belgium, Spain, Italy, Japan, South Korea, Canada.
- Backbone supplementation: Europol, Eurojust, INTERPOL, Council of Europe, and open research (papers).
- `insane-search` usage: query templates are written for blocked-site retrieval via Jina, TLS impersonation, or browser fallback when ordinary fetches fail.

## Queue Snapshot

- Target operations below threshold: **0**
- `retain_and_enrich`: **0**
- `high_risk_review`: **0**
- Operations already carrying at least one DOJ source: **0**
- Operations directly matching one or more target countries: **0**

## Target Country Coverage

| Country | Assigned operations |
|---|---:|

## Priority Queue

| Operation | Sources | Bucket | Priority countries | Current source domains | Notes |
|---|---:|---|---|---|---|

## Search Playbook

Use the queries below with normal web search first. If the source is blocked, run the same URL through `insane-search` fallbacks in this order: Jina Reader -> curl_cffi TLS impersonation -> Playwright/browser fallback.
