---
type: analysis
title: "VOIP Workbook and SNA Count Reconciliation (2026-05-06)"
title_ko: "VOIP xlsx 원천 건수와 SNA 반영 건수 정합성 검토"
analysis_type: count-reconciliation
scope: "Reconcile workbook source rows, source-backed operation expansion, and current SNA inclusion for voice-phishing-ic."
confidence: medium
created: 2026-05-06
updated: 2026-05-06
---

## Summary

This note reconciles the three counts used for [[voice-phishing-ic]]:

| Counting layer | Count | Meaning |
|---|---:|---|
| xlsx narrow source rows | 6 | Unique workbook serial numbers whose crime-type field directly names voice phishing, vishing, or illegal phone/call-center activity. |
| xlsx broader phone-enabled rows | 7 | The narrow set plus technical-support or remote-support fraud where the phone/call-center channel is central. |
| Source-backed SNA operations | 12 | Current operation slugs connected to `voice-phishing-ic` in `_workspace/sna/current/edges_op_crimetype.csv`. |

The difference is intentional. The workbook is a starting source list, while the wiki/SNA layer is operation-name based and accepts additional official or source-backed operation records when the phone-enabled fraud mechanism is clear.

## Workbook Counting Rule

The workbook count is deduplicated by `연번`, because the same source can appear in both the URL collection sheet and the extracted country-agency-crime sheet. `연번 359` appears twice for Belgium Phish and is counted once.

The narrow count uses the `죄명(한글)` field and matches:

- 보이스피싱
- 보이스 피싱
- 비싱
- 불법 전화센터 / 불법전화센터
- 불법 콜센터 / 불법콜센터

The broader count adds technical-support or remote-support scam rows when the record describes a phone or call-center operating model.

## Workbook Rows

| Serial | Year | Workbook operation name | SNA operation mapping | Count basis |
|---:|---:|---|---|---|
| 212 | 2023 | Operation HAECHI III | [[operation-haechi-iii]] | Narrow: 보이스 피싱. |
| 243 | 2023 | HAECHI IV | [[operation-haechi-iv]] | Narrow: 보이스피싱. |
| 253 | 2023 | Operation Chakra-II | [[operation-chakra-ii]] | Narrow: 불법 콜센터 and tech-support fraud. |
| 342 | 2024 | Operation HAECHI V | [[operation-haechi-v]] | Narrow: 보이스피싱. |
| 359 | 2024 | (가칭)Operation Belgium Phish | [[belgium-netherlands-phishing-gang]] | Narrow: 비싱; duplicate workbook-sheet appearance counted once. |
| 420 | 2025 | Operation Chakra-V | [[operation-chakra-v]] | Narrow: 불법 전화센터 and tech-support fraud. |
| 540 | 2025 | Operation Chakra-IV | [[operation-chakra-iv]] | Broader only: technical-support impersonation and remote access; treated as phone-enabled fraud after source review. |

## Current SNA Operation Set

The current SNA set contains 12 operation slugs for [[voice-phishing-ic]]:

| Operation | Inclusion rationale |
|---|---|
| [[belgium-netherlands-phishing-gang]] | Phone-phishing group targeting victims through bank/police impersonation. |
| [[korea-cambodia-scam-repatriation]] | Scam-center repatriation and investigation with Korean victim relevance. |
| [[korea-china-voice-phishing-qingdao]] | Korea-China bilateral voice-phishing call-center enforcement. |
| [[operation-chakra-ii]] | CBI call-center and tech-support scam enforcement. |
| [[operation-chakra-iii]] | Transnational cyber financial-crime network using call-center/remote-support methods. |
| [[operation-chakra-iv]] | German-victim tech-support and remote-access fraud. |
| [[operation-chakra-v]] | Japanese-victim tech-support and illegal call-center fraud. |
| [[operation-first-light-2024]] | INTERPOL First Light phone and online-scam operation. |
| [[operation-haechi-iii]] | INTERPOL HAECHI III, including voice phishing and related online fraud. |
| [[operation-haechi-iv]] | INTERPOL HAECHI IV, including voice phishing and wider financial fraud. |
| [[operation-haechi-v]] | INTERPOL HAECHI V, including the Korea-China voice-phishing syndicate disruption. |
| [[operation-haechi-vi]] | INTERPOL HAECHI VI, including voice phishing / phone-enabled financial-crime recovery. |

## Interpretation

For reporting, use the three-layer formula rather than a single number:

- xlsx 원천 협의 기준: 6 unique serials.
- xlsx 광의 phone-enabled 기준: 7 unique serials.
- 보강 후 작전명/SNA 기준: 12 operations.

This makes the data lineage defensible: the xlsx number remains an input count, while the SNA number reflects the curated operation corpus after source-backed enrichment.

## Residual Review Queue

- Keep [[operation-chakra-iv]] explicitly marked as broader phone-enabled fraud, not narrow Korean 보이스피싱.
- Prefer CBI, Japanese NPA, German police/prosecutor, INTERPOL, Europol, or Eurojust sources when additional Chakra-series official records become available.
- Retain [[voice-phishing-ic]] as an independent SNA target because the current centrality snapshot places it above [[csam-ic]] and [[illegal-iptv-ic]] among the six target crime categories.
