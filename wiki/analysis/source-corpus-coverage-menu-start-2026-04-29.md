---
type: analysis
title: "Source Corpus Coverage Audit (2026-04-29)"
created: 2026-04-29
updated: 2026-04-29
summary: "Repository-wide audit of wiki source pages, raw source records, fulltext coverage, summary-only coverage, and remaining fetch/materialization gaps."
---

# Source Corpus Coverage Audit

This audit checks whether every `wiki/sources` page has a separate raw/source-content record and whether that record is full text, summary-only, source-digest, or still missing.

## Coverage Summary

| Item | Count |
|---|---:|
| source_pages | 4767 |
| with_raw_path | 4765 |
| raw_exists | 4765 |
| with_url | 4747 |
| official_url | 2514 |
| nonofficial_or_no_url | 2253 |
| without_url | 20 |
| without_raw_path | 2 |
| raw_missing_or_unlinked | 2 |

## Raw Status

| Item | Count |
|---|---:|
| summary_only | 2222 |
| fulltext | 1574 |
| source_digest | 945 |
| raw_body_present | 24 |
| missing_raw_path | 2 |

## Fetch Queue

| Item | Count |
|---|---:|
| nonofficial_or_unknown | 528 |
| official | 2 |

## Source Types

| Item | Count |
|---|---:|
| press-release | 2692 |
| news | 1808 |
| court-document | 104 |
| case-document | 23 |
| government-report | 20 |
| report | 20 |
| official-guidance | 20 |
| government | 18 |
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

### missing_raw_path

| Source | Raw Path | Publisher | URL |
|---|---|---|---|
| `2026-04-29_asd-gov-au_about-australian-signals-directorate` | `` | Australian Signals Directorate | https://www.asd.gov.au/about |
| `2026-04-29_asd-gov-au_cyber-security` | `` | Australian Signals Directorate | https://www.asd.gov.au/about/what-we-do/cyber-security |

### needs_fetch

| Source | Raw Path | Publisher | URL |
|---|---|---|---|
| `2003-04-19_legislatie-just-ro_law-no-161-2003-title-iii` | `raw/press-releases/2003-04-19_legislatie-just-ro_law-no-161-2003-title-iii.md` | Romanian Government | https://legislatie.just.ro/Public/DetaliiDocument/43323 |
| `2010-12-21_antic-cm_law-no-2010-012-of-21-december-2010-relating-to-cybersecurity-and-cybercriminali` | `raw/press-releases/2010-12-21_antic-cm_law-no-2010-012-of-21-december-2010-relating-to-cybersecurity-and-cybercriminali.md` | Republic of Cameroon / ANTIC | https://www.antic.cm/images/stories/laws/Law%20relating%20to%20cybersecurity%20and%20cybercriminality%20in%20Cameroon.pdf |
| `2012-01-01_143bis-ch_swiss-coordination-unit-for-cybercrime-control-cyco-annual-report` | `raw/press-releases/2012-01-01_143bis-ch_swiss-coordination-unit-for-cybercrime-control-cyco-annual-report.md` | Fedpol | https://143bis.ch/blog/wp-content/uploads/2018/10/rechenschaftsbericht-2011-e.pdf |
| `2013-08-12_artci-ci_loi-n-2013-451-relative-la-lutte-contre-la-cybercriminalit-journal-officiel` | `raw/press-releases/2013-08-12_artci-ci_loi-n-2013-451-relative-la-lutte-contre-la-cybercriminalit-journal-officiel.md` | Republic of Côte d'Ivoire | https://www.artci.ci/images/stories/pdf/lois/loi_2013_451.pdf |
| `2014-02-20_cbsnews-baltimore_neb-man-charged-in-silk-road-case` | `raw/news/2014-02-20_cbsnews-baltimore_neb-man-charged-in-silk-road-case.md` | CBS News Baltimore | https://www.cbsnews.com/baltimore/news/neb-man-charged-in-silk-road-case/ |
| `2014-12-05_haitianbusiness_haitian-man-maxito-pean-indicted-saratoga-233000-email-scam` | `raw/news/2014-12-05_haitianbusiness_haitian-man-maxito-pean-indicted-saratoga-233000-email-scam.md` | Haitian Business | http://haitianbusiness.com/haitian-man-maxito-pean-indicted-in-saratoga-over-233000-via-an-email-scam |
| `2015-02-25_anubisnetworks_aids-europols-european-cybercrime-centre-in-takedown-of-malicious-botnet` | `raw/press-releases/2015-02-25_anubisnetworks_aids-europols-european-cybercrime-centre-in-takedown-of-malicious-botnet.md` | AnubisNetworks | https://www.anubisnetworks.com/news/community/news/anubisnetworks-aids-europols-european-cybercrime-centre-in-takedown-of-malicious-botnet |
| `2015-05-29_cnn-money_silk-road-ross-ulbricht-prison-sentence` | `raw/news/2015-05-29_cnn-money_silk-road-ross-ulbricht-prison-sentence.md` | CNN Money | https://money.cnn.com/2015/05/29/technology/silk-road-ross-ulbricht-prison-sentence/index.html |
| `2015-06-11_europeanaffairs_europol-operation-triangle-cybercrime-net-dismantled` | `raw/press-releases/2015-06-11_europeanaffairs_europol-operation-triangle-cybercrime-net-dismantled.md` | European Affairs Magazine | https://www.europeanaffairs.it/blog/2015/06/11/europol-operation-triangle-cybercrime-net-dismantled/ |
| `2015-10-13_networkworld_fbi-doj-take-out-10-million-bugat-banking-botnet` | `raw/news/2015-10-13_networkworld_fbi-doj-take-out-10-million-bugat-banking-botnet.md` | Network World | https://www.networkworld.com/article/944308/fbi-doj-take-out-10-million-bugat-banking-botnet-zeus.html/amp |
| `2016-01-01_ilo-org_natlex-law-n-4411-of-2016-ratifying-the-convention-of-the-council-of-europe-on-c` | `raw/press-releases/2016-01-01_ilo-org_natlex-law-n-4411-of-2016-ratifying-the-convention-of-the-council-of-europe-on-c.md` | International Labour Organization (NATLEX) | https://ilo.org/dyn/natlex/natlex4.detail?p_classification=15.05&p_count=2&p_isn=104604&p_lang=en |
| `2016-06-06_securityweek_silk-road-20-admin-sentenced-8-years-prison` | `raw/news/2016-06-06_securityweek_silk-road-20-admin-sentenced-8-years-prison.md` | SecurityWeek | https://www.securityweek.com/silk-road-20-admin-sentenced-8-years-prison/ |
| `2016-06-08_databreachesnet_former-agilent-technologies-employee-pleads-guilty-to-damaging-ex-employers-computers` | `raw/news/2016-06-08_databreachesnet_former-agilent-technologies-employee-pleads-guilty-to-damaging-ex-employers-computers.md` | DataBreaches.net | https://databreaches.net/2016/06/08/former-agilent-technologies-employee-pleads-guilty-to-damaging-ex-employers-computers/ |
| `2016-06-11_kron4_former-silicon-valley-employee-pleads-guilty-damaging-computers` | `raw/news/2016-06-11_kron4_former-silicon-valley-employee-pleads-guilty-damaging-computers.md` | KRON4 | https://www.kron4.com/news/former-silicon-valley-employee-pleads-guilty-to-damaging-computers/ |
| `2016-08-01_cnn_nigerian-man-arrested-in-global-60-million-scam` | `raw/press-releases/2016-08-01_cnn_nigerian-man-arrested-in-global-60-million-scam.md` | CNN | https://money.cnn.com/2016/08/01/news/companies/nigeria-scam-arrest/index.html |

## Artifacts

- CSV: `_workspace/source_corpus_coverage_2026-04-29.csv`
