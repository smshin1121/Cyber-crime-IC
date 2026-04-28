---
type: analysis
title: "Source Content Record Materialization (2026-04-28)"
created: 2026-04-28
updated: 2026-04-28
summary: "Materialization report for creating separate raw/source-content records from wiki source metadata and source-page factual digests."
---

# Source Content Record Materialization

Dry run: `false`

## Status Counts

| Status | Count |
|---|---:|
| skipped_status_summary_only | 2222 |
| skipped_status_fulltext | 1471 |
| materialized | 1037 |
| skipped_status_raw_body_present | 35 |

## Source Class Counts

| Class | Count |
|---|---:|
| official | 2512 |
| nonofficial_or_unknown | 2253 |

## Sample Materialized Records

| Source | Raw Path | Official |
|---|---|---:|
| `2014-07-09_district-court-sd-new-york_united-states-v-ulbricht-2.md` | `raw/case-documents/2014-07-09_district-court-sd-new-york_united-states-v-ulbricht-2.md` | true |
| `2014-07-09_district-court-sd-new-york_united-states-v-ulbricht.md` | `raw/case-documents/2014-07-09_district-court-sd-new-york_united-states-v-ulbricht.md` | true |
| `2014-11-06_justice-gov_united-states-v-blake-benthall.md` | `raw/press-releases/2014-11-06_justice-gov_united-states-v-blake-benthall.md` | true |
| `2014-12-18_justice-gov_united-states-v-matthew-jones.md` | `raw/press-releases/2014-12-18_justice-gov_united-states-v-matthew-jones.md` | true |
| `2014-12-18_mdfl_matthew-jones-silk-road-sentencing.md` | `raw/case-documents/2014-12-18_mdfl_matthew-jones-silk-road-sentencing.md` | true |
| `2015-01-07_district-court-sd-new-york_united-states-v-ulbricht-2.md` | `raw/case-documents/2015-01-07_district-court-sd-new-york_united-states-v-ulbricht-2.md` | true |
| `2015-01-07_district-court-sd-new-york_united-states-v-ulbricht.md` | `raw/case-documents/2015-01-07_district-court-sd-new-york_united-states-v-ulbricht.md` | true |
| `2015-02-24_europol-europa-eu_botnet-taken-down-through-international-law-enforcement-cooperation.md` | `raw/press-releases/2015-02-24_europol-europa-eu_botnet-taken-down-through-international-law-enforcement-cooperation.md` | true |
| `2015-03-25_justice-gov_us-20v-20ross-20ulbricht-20indictment-pdf.md` | `raw/press-releases/2015-03-25_justice-gov_us-20v-20ross-20ulbricht-20indictment-pdf.md` | true |
| `2015-04-01_europol-europa-eu_international-police-operation-targets-polymorphic-beebone-botnet.md` | `raw/press-releases/2015-04-01_europol-europa-eu_international-police-operation-targets-polymorphic-beebone-botnet.md` | true |
| `2015-04-27_justice-gov_united-states-v-olivia-bolles.md` | `raw/press-releases/2015-04-27_justice-gov_united-states-v-olivia-bolles.md` | true |
| `2015-04-27_mdfl_olivia-bolles-silk-road-sentencing.md` | `raw/case-documents/2015-04-27_mdfl_olivia-bolles-silk-road-sentencing.md` | true |
| `2015-05-29_justice-gov_united-states-v-ulbricht-sentencing.md` | `raw/press-releases/2015-05-29_justice-gov_united-states-v-ulbricht-sentencing.md` | true |
| `2015-06-01_europol-europa-eu_international-operation-dismantles-criminal-group-of-cyber-fraudsters.md` | `raw/press-releases/2015-06-01_europol-europa-eu_international-operation-dismantles-criminal-group-of-cyber-fraudsters.md` | true |
| `2015-06-01_europol-europa-eu_major-cybercrime-ring-dismantled-by-joint-investigation-team.md` | `raw/press-releases/2015-06-01_europol-europa-eu_major-cybercrime-ring-dismantled-by-joint-investigation-team.md` | true |
| `2015-07-15_justice-gov_major-computer-hacking-forum-dismantled.md` | `raw/press-releases/2015-07-15_justice-gov_major-computer-hacking-forum-dismantled.md` | true |
| `2015-07-15_justice-gov_united-states-v-gudmunds-et-al-darkode-forum.md` | `raw/press-releases/2015-07-15_justice-gov_united-states-v-gudmunds-et-al-darkode-forum.md` | true |
| `2015-10-13_fbi-pittsburgh_bugat-botnet-administrator-arrested-and-malware-disabled.md` | `raw/press-releases/2015-10-13_fbi-pittsburgh_bugat-botnet-administrator-arrested-and-malware-disabled.md` | true |
| `2015-10-13_fbi_bugat-botnet-administrator-arrested-malware-disabled.md` | `raw/press-releases/2015-10-13_fbi_bugat-botnet-administrator-arrested-malware-disabled.md` | true |
| `2015-10-13_justice-gov_major-computer-hacking-forum-dismantled.md` | `raw/press-releases/2015-10-13_justice-gov_major-computer-hacking-forum-dismantled.md` | true |
| `2015-10-13_justice-gov_united-states-v-ghinkul-bugat-dridex-botnet.md` | `raw/press-releases/2015-10-13_justice-gov_united-states-v-ghinkul-bugat-dridex-botnet.md` | true |
| `2015-11-03_justice-gov_united-states-v-sheldon-kennedy.md` | `raw/press-releases/2015-11-03_justice-gov_united-states-v-sheldon-kennedy.md` | true |
| `2015-11-03_md_sheldon-kennedy-silk-road-sentencing.md` | `raw/case-documents/2015-11-03_md_sheldon-kennedy-silk-road-sentencing.md` | true |
| `2015-12-01_europol-europa-eu_international-action-against-dd4bc-cybercriminal-group.md` | `raw/press-releases/2015-12-01_europol-europa-eu_international-action-against-dd4bc-cybercriminal-group.md` | true |
| `2016-06-03_fbi-seattle_key-player-silk-road-20-sentenced-eight-years-prison.md` | `raw/press-releases/2016-06-03_fbi-seattle_key-player-silk-road-20-sentenced-eight-years-prison.md` | true |
| `2016-06-03_justice-gov_united-states-v-brian-richard-farrell.md` | `raw/press-releases/2016-06-03_justice-gov_united-states-v-brian-richard-farrell.md` | true |
| `2016-06-03_wdwa_farrell-silk-road-2-sentencing.md` | `raw/case-documents/2016-06-03_wdwa_farrell-silk-road-2-sentencing.md` | true |
| `2016-11-30_europol-europa-eu_avalanche-network-dismantled-in-international-cyber-operation.md` | `raw/press-releases/2016-11-30_europol-europa-eu_avalanche-network-dismantled-in-international-cyber-operation.md` | true |
| `2016-12-20_justice-gov_nigerian-nationals-charged-with-operating-business-compromise-scheme.md` | `raw/press-releases/2016-12-20_justice-gov_nigerian-nationals-charged-with-operating-business-compromise-scheme.md` | true |
| `2016-12-20_justice-gov_united-states-v-odufuye-and-nwoke.md` | `raw/press-releases/2016-12-20_justice-gov_united-states-v-odufuye-and-nwoke.md` | true |
| `2016-12-22_justice-gov_nigerian-nationals-charged-with-operating-business-compromise-scheme.md` | `raw/press-releases/2016-12-22_justice-gov_nigerian-nationals-charged-with-operating-business-compromise-scheme.md` | true |
| `2017-03-09_justice-gov_united-states-v-michael-carlton-paiva.md` | `raw/press-releases/2017-03-09_justice-gov_united-states-v-michael-carlton-paiva.md` | true |
| `2017-03-09_wdmi_paiva-silk-road-2-sentencing.md` | `raw/case-documents/2017-03-09_wdmi_paiva-silk-road-2-sentencing.md` | true |
| `2017-04-01_eurojust-europa-eu_operation-avalanche-a-closer-look.md` | `raw/press-releases/2017-04-01_eurojust-europa-eu_operation-avalanche-a-closer-look.md` | true |
| `2017-04-01_eurojust-europa-eu_operation-avalanche-closer-look.md` | `raw/government-reports/2017-04-01_eurojust-europa-eu_operation-avalanche-closer-look.md` | true |
| `2017-05-31_court-of-appeals-for-the-second-circuit_united-states-v-ulbricht-2.md` | `raw/case-documents/2017-05-31_court-of-appeals-for-the-second-circuit_united-states-v-ulbricht-2.md` | true |
| `2017-05-31_court-of-appeals-for-the-second-circuit_united-states-v-ulbricht.md` | `raw/case-documents/2017-05-31_court-of-appeals-for-the-second-circuit_united-states-v-ulbricht.md` | true |
| `2017-05-31_courtlistener-com_united-states-v-ulbricht.md` | `raw/press-releases/2017-05-31_courtlistener-com_united-states-v-ulbricht.md` | true |
| `2017-06-01_justice-gov_united-states-v-alexandre-cazes.md` | `raw/press-releases/2017-06-01_justice-gov_united-states-v-alexandre-cazes.md` | true |
| `2017-07-20-europol-alphabay-hansa-takedown.md` | `raw/press-releases/2017-07-20-europol-alphabay-hansa-takedown.md` | true |
