---
type: analysis
title: "Source Corpus Coverage Audit (2026-04-28)"
created: 2026-04-28
updated: 2026-04-28
summary: "Repository-wide audit of wiki source pages, raw source records, fulltext coverage, summary-only coverage, and remaining fetch/materialization gaps."
---

# Source Corpus Coverage Audit

This audit checks whether every `wiki/sources` page has a separate raw/source-content record and whether that record is full text, summary-only, source-digest, or still missing.

## Coverage Summary

| Item | Count |
|---|---:|
| source_pages | 4765 |
| with_raw_path | 4765 |
| raw_exists | 4765 |
| with_url | 4745 |
| official_url | 2512 |
| nonofficial_or_no_url | 2253 |
| without_url | 20 |

## Raw Status

| Item | Count |
|---|---:|
| summary_only | 2222 |
| fulltext | 1471 |
| source_digest | 1037 |
| raw_body_present | 35 |

## Fetch Queue

| Item | Count |
|---|---:|
| official | 1072 |
| nonofficial_or_unknown | 619 |

## Source Types

| Item | Count |
|---|---:|
| press-release | 2692 |
| news | 1808 |
| court-document | 104 |
| case-document | 23 |
| government-report | 20 |
| report | 20 |
| government | 18 |
| official-guidance | 18 |
| official-article | 7 |
| official-press-release | 5 |
| news-article | 5 |
| court-press-release | 3 |
| court-record | 3 |
| advisory | 3 |
| blog | 2 |
| government-index | 2 |
| bulletin | 2 |
| advocacy-news-roundup | 2 |
| government-summary | 2 |
| technical-report | 1 |
| official-statement | 1 |
| corporate-blog | 1 |
| district-press-release | 1 |
| legal-summary | 1 |
| investigative-news-release | 1 |
| wanted-poster | 1 |
| research | 1 |
| speech | 1 |
| court-update | 1 |
| policy-document | 1 |
| guidance | 1 |
| podcast | 1 |
| analysis | 1 |
| legal-notice | 1 |
| legal-case-summary | 1 |
| academic-paper | 1 |
| research-blog | 1 |
| agency-story | 1 |
| annual-report | 1 |
| agency-news | 1 |
| threat-advisory | 1 |
| institutional-page | 1 |
| country-profile | 1 |
| infographic | 1 |
| corporate-reference | 1 |

## Interpretation

- `fulltext` records can be used directly for source-grounded enrichment.
- `summary_only` and `source_digest` records should drive factual wiki enrichment through paraphrased fact bullets, not article reproduction.
- `missing_raw_path` and `missing_raw_file` records need materialization before the corpus can be treated as complete.
- Official/public records should be prioritized for full-text fetching; nonofficial media should remain rights-sensitive unless a permissive basis is documented.

## Example Gaps

### needs_fetch

| Source | Raw Path | Publisher | URL |
|---|---|---|---|
| `2003-04-19_legislatie-just-ro_law-no-161-2003-title-iii` | `raw/press-releases/2003-04-19_legislatie-just-ro_law-no-161-2003-title-iii.md` | Romanian Government | https://legislatie.just.ro/Public/DetaliiDocument/43323 |
| `2010-12-21_antic-cm_law-no-2010-012-of-21-december-2010-relating-to-cybersecurity-and-cybercriminali` | `raw/press-releases/2010-12-21_antic-cm_law-no-2010-012-of-21-december-2010-relating-to-cybersecurity-and-cybercriminali.md` | Republic of Cameroon / ANTIC | https://www.antic.cm/images/stories/laws/Law%20relating%20to%20cybersecurity%20and%20cybercriminality%20in%20Cameroon.pdf |
| `2012-01-01_143bis-ch_swiss-coordination-unit-for-cybercrime-control-cyco-annual-report` | `raw/press-releases/2012-01-01_143bis-ch_swiss-coordination-unit-for-cybercrime-control-cyco-annual-report.md` | Fedpol | https://143bis.ch/blog/wp-content/uploads/2018/10/rechenschaftsbericht-2011-e.pdf |
| `2013-08-12_artci-ci_loi-n-2013-451-relative-la-lutte-contre-la-cybercriminalit-journal-officiel` | `raw/press-releases/2013-08-12_artci-ci_loi-n-2013-451-relative-la-lutte-contre-la-cybercriminalit-journal-officiel.md` | Republic of Côte d'Ivoire | https://www.artci.ci/images/stories/pdf/lois/loi_2013_451.pdf |
| `2014-02-20_cbsnews-baltimore_neb-man-charged-in-silk-road-case` | `raw/news/2014-02-20_cbsnews-baltimore_neb-man-charged-in-silk-road-case.md` | CBS News Baltimore | https://www.cbsnews.com/baltimore/news/neb-man-charged-in-silk-road-case/ |
| `2014-07-09_district-court-sd-new-york_united-states-v-ulbricht-2` | `raw/case-documents/2014-07-09_district-court-sd-new-york_united-states-v-ulbricht-2.md` | District Court, S.D. New York | https://www.courtlistener.com/opinion/7307490/united-states-v-ulbricht/ |
| `2014-07-09_district-court-sd-new-york_united-states-v-ulbricht` | `raw/case-documents/2014-07-09_district-court-sd-new-york_united-states-v-ulbricht.md` | District Court, S.D. New York | https://www.courtlistener.com/opinion/7307490/united-states-v-ulbricht/ |
| `2014-11-06_justice-gov_united-states-v-blake-benthall` | `raw/press-releases/2014-11-06_justice-gov_united-states-v-blake-benthall.md` | US DOJ (Southern District of New York) | https://www.justice.gov/usao-sdny/pr/operator-silk-road-20-website-charged-manhattan-federal-court |
| `2014-11-06_sdny_benthall-silk-road-2-complaint` | `raw/case-documents/2014-11-06_sdny_benthall-silk-road-2-complaint.md` | US DOJ (Southern District of New York) | https://www.justice.gov/usao-sdny/pr/operator-silk-road-20-website-charged-manhattan-federal-court |
| `2014-12-05_haitianbusiness_haitian-man-maxito-pean-indicted-saratoga-233000-email-scam` | `raw/news/2014-12-05_haitianbusiness_haitian-man-maxito-pean-indicted-saratoga-233000-email-scam.md` | Haitian Business | http://haitianbusiness.com/haitian-man-maxito-pean-indicted-in-saratoga-over-233000-via-an-email-scam |
| `2014-12-18_justice-gov_united-states-v-matthew-jones` | `raw/press-releases/2014-12-18_justice-gov_united-states-v-matthew-jones.md` | US DOJ (Middle District of Florida) | https://www.justice.gov/usao-mdfl/pr/texas-business-executive-sentenced-prison-illegally-selling-oxycodone-silk-road |
| `2014-12-18_mdfl_matthew-jones-silk-road-sentencing` | `raw/case-documents/2014-12-18_mdfl_matthew-jones-silk-road-sentencing.md` | US DOJ (Middle District of Florida) | https://www.justice.gov/usao-mdfl/pr/texas-business-executive-sentenced-prison-illegally-selling-oxycodone-silk-road |
| `2015-01-07_district-court-sd-new-york_united-states-v-ulbricht-2` | `raw/case-documents/2015-01-07_district-court-sd-new-york_united-states-v-ulbricht-2.md` | District Court, S.D. New York | https://www.courtlistener.com/opinion/7311405/united-states-v-ulbricht/ |
| `2015-01-07_district-court-sd-new-york_united-states-v-ulbricht` | `raw/case-documents/2015-01-07_district-court-sd-new-york_united-states-v-ulbricht.md` | District Court, S.D. New York | https://www.courtlistener.com/opinion/7311405/united-states-v-ulbricht/ |
| `2015-02-24_europol-europa-eu_botnet-taken-down-through-international-law-enforcement-cooperation` | `raw/press-releases/2015-02-24_europol-europa-eu_botnet-taken-down-through-international-law-enforcement-cooperation.md` | Europol | https://www.europol.europa.eu/media-press/newsroom/news/botnet-taken-down-through-international-law-enforcement-cooperation |

## Artifacts

- CSV: `_workspace/source_corpus_coverage_after_materialize_2026-04-28.csv`
