---
title: Content Enrichment Queue (2026-04-26)
type: analysis
created: 2026-04-26
updated: 2026-04-26
summary: "Prioritized queue for enriching source-rich, thin, placeholder, or duplicate-reference operation and case pages."
source_count: 0
---
## Summary

This queue converts the content-depth audit into an execution list. It is ordered to fix pages where existing sources already contain enough material before searching for new sources.

- Audited operation/case pages: **2287**
- Queue size: **99**

## Top Queue

| Rank | Page | Type | Score | Sources | Body words | Source words | Recommendation | Issues |
|---:|---|---|---:|---:|---:|---:|---|---|
| 1 | [[us-v-of-silk-road]] | case | 101 | 5 | 123 | 7160 | enrich_from_existing_raw_sources | source_rich_thin_body:123w, missing_quality_sections:2/6, raw_available_underused:7160w_sources, high_source_to_body_gap, possible_crime_type_mismatch:dark-web-ic |
| 2 | [[operation-killer-bee]] | operation | 101 | 5 | 165 | 6852 | enrich_from_existing_raw_sources | source_rich_thin_body:165w, missing_quality_sections:2/6, raw_available_underused:6852w_sources, high_source_to_body_gap, possible_crime_type_mismatch:malware-ic |
| 3 | [[operation-sentinel-africa]] | operation | 101 | 5 | 340 | 4239 | enrich_from_existing_raw_sources | source_rich_thin_body:340w, missing_quality_sections:2/6, raw_available_underused:4239w_sources, high_source_to_body_gap, possible_crime_type_mismatch:ransomware-ic |
| 4 | [[lumma-stealer-takedown]] | operation | 101 | 5 | 333 | 3284 | enrich_from_existing_raw_sources | source_rich_thin_body:333w, missing_quality_sections:2/6, raw_available_underused:3284w_sources, high_source_to_body_gap, possible_crime_type_mismatch:malware-ic |
| 5 | [[operation-source]] | operation | 101 | 5 | 153 | 3084 | enrich_from_existing_raw_sources | source_rich_thin_body:153w, missing_quality_sections:2/6, raw_available_underused:3084w_sources, high_source_to_body_gap, possible_crime_type_mismatch:ransomware-ic |
| 6 | [[operation-pleiades]] | operation | 101 | 5 | 265 | 2893 | enrich_from_existing_raw_sources | source_rich_thin_body:265w, missing_quality_sections:3/6, raw_available_underused:2893w_sources, high_source_to_body_gap, possible_crime_type_mismatch:ransomware-ic |
| 7 | [[operation-australian-man-arrested-in-germany-accused-of-running-world-s-largest-darknet-marketplace]] | operation | 97 | 5 | 113 | 8894 | enrich_from_existing_raw_sources | source_rich_thin_body:113w, missing_quality_sections:1/6, raw_available_underused:8894w_sources, high_source_to_body_gap, generated_enforcement_title |
| 8 | [[operation-operation-orion-international-144-arrested-in-major-child-abuse-operation-across-south-america]] | operation | 97 | 5 | 124 | 5977 | enrich_from_existing_raw_sources | source_rich_thin_body:124w, missing_quality_sections:2/6, raw_available_underused:5977w_sources, high_source_to_body_gap, generated_enforcement_title |
| 9 | [[operation-12-members-of-an-irish-high-risk-criminal-network-arrested]] | operation | 97 | 6 | 116 | 4839 | enrich_from_existing_raw_sources | source_rich_thin_body:116w, missing_quality_sections:2/6, raw_available_underused:4839w_sources, high_source_to_body_gap, generated_enforcement_title |
| 10 | [[operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown]] | operation | 97 | 5 | 122 | 3378 | enrich_from_existing_raw_sources | source_rich_thin_body:122w, missing_quality_sections:2/6, raw_available_underused:3378w_sources, high_source_to_body_gap, generated_enforcement_title |
| 11 | [[operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown-3]] | operation | 97 | 5 | 122 | 3378 | enrich_from_existing_raw_sources | source_rich_thin_body:122w, missing_quality_sections:2/6, raw_available_underused:3378w_sources, high_source_to_body_gap, generated_enforcement_title |
| 12 | [[operation-europol-french-coder-who-helped-extort-british-company-arrested-in-thailand]] | operation | 97 | 5 | 120 | 2924 | enrich_from_existing_raw_sources | source_rich_thin_body:120w, missing_quality_sections:2/6, raw_available_underused:2924w_sources, high_source_to_body_gap, generated_enforcement_title |
| 13 | [[operation-french-coder-who-helped-extort-british-company-arrested-in-thailand]] | operation | 97 | 5 | 118 | 2598 | enrich_from_existing_raw_sources | source_rich_thin_body:118w, missing_quality_sections:2/6, raw_available_underused:2598w_sources, high_source_to_body_gap, generated_enforcement_title |
| 14 | [[911-s5-botnet-takedown]] | operation | 97 | 5 | 116 | 1954 | enrich_from_existing_raw_sources | source_rich_thin_body:116w, missing_quality_sections:2/6, raw_available_underused:1954w_sources, unresolved_operation_name, possible_crime_type_mismatch:csam-ic |
| 15 | [[fin7-takedown]] | operation | 97 | 5 | 137 | 1543 | enrich_from_existing_raw_sources | source_rich_thin_body:137w, missing_quality_sections:2/6, raw_available_underused:1543w_sources, unresolved_operation_name, possible_crime_type_mismatch:malware-ic |
| 16 | [[zeus-spyeye-jit-takedown]] | operation | 95 | 6 | 145 | 5796 | enrich_from_existing_raw_sources | source_rich_thin_body:145w, missing_quality_sections:2/6, raw_available_underused:5796w_sources, high_source_to_body_gap, unresolved_operation_name |
| 17 | [[cyber-fraud-international-2015]] | operation | 95 | 5 | 155 | 5663 | enrich_from_existing_raw_sources | source_rich_thin_body:155w, missing_quality_sections:2/6, raw_available_underused:5663w_sources, high_source_to_body_gap, unresolved_operation_name |
| 18 | [[ddos-for-hire-sweep-2016]] | operation | 95 | 6 | 164 | 5484 | enrich_from_existing_raw_sources | source_rich_thin_body:164w, missing_quality_sections:2/6, raw_available_underused:5484w_sources, high_source_to_body_gap, unresolved_operation_name |
| 19 | [[romania-phishing-takedown-2024]] | operation | 95 | 5 | 140 | 4242 | enrich_from_existing_raw_sources | source_rich_thin_body:140w, missing_quality_sections:2/6, raw_available_underused:4242w_sources, high_source_to_body_gap, unresolved_operation_name |
| 20 | [[rex-mundi-takedown]] | operation | 95 | 5 | 150 | 2924 | enrich_from_existing_raw_sources | source_rich_thin_body:150w, missing_quality_sections:2/6, raw_available_underused:2924w_sources, high_source_to_body_gap, unresolved_operation_name |
| 21 | [[operation-goldfish-alpha-night-fury]] | operation | 89 | 5 | 156 | 1486 | enrich_from_existing_raw_sources | source_rich_thin_body:156w, missing_quality_sections:2/6, raw_available_underused:1486w_sources, possible_crime_type_mismatch:bec-ic |
| 22 | [[operation-cyber-guardian]] | operation | 87 | 5 | 348 | 9162 | enrich_from_existing_raw_sources | source_rich_thin_body:348w, missing_quality_sections:2/6, raw_available_underused:9162w_sources, high_source_to_body_gap |
| 23 | [[global-airport-action-day]] | operation | 87 | 6 | 187 | 9151 | enrich_from_existing_raw_sources | source_rich_thin_body:187w, missing_quality_sections:2/6, raw_available_underused:9151w_sources, high_source_to_body_gap |
| 24 | [[150-arrested-in-dark-web-drug-bust-as-police-seize-eur-26-million]] | case | 87 | 5 | 209 | 8025 | enrich_from_existing_raw_sources | source_rich_thin_body:209w, missing_quality_sections:2/6, raw_available_underused:8025w_sources, high_source_to_body_gap |
| 25 | [[isoon-apt27-indictment]] | operation | 87 | 6 | 341 | 8012 | enrich_from_existing_raw_sources | source_rich_thin_body:341w, missing_quality_sections:2/6, raw_available_underused:8012w_sources, high_source_to_body_gap |
| 26 | [[operation-orion-international]] | operation | 87 | 5 | 321 | 5782 | enrich_from_existing_raw_sources | source_rich_thin_body:321w, missing_quality_sections:2/6, raw_available_underused:5782w_sources, high_source_to_body_gap |
| 27 | [[lakeland-man-pleads-guilty-to-receiving-child-sex-abuse-videos-from-the-largest-darknet-child-pornography-webs]] | case | 87 | 5 | 330 | 5593 | enrich_from_existing_raw_sources | source_rich_thin_body:330w, missing_quality_sections:3/6, raw_available_underused:5593w_sources, high_source_to_body_gap |
| 28 | [[operation-germany-romania-trusted-seller-fraud-2025]] | operation | 87 | 5 | 115 | 5255 | enrich_from_existing_raw_sources | source_rich_thin_body:115w, missing_quality_sections:1/6, raw_available_underused:5255w_sources, high_source_to_body_gap |
| 29 | [[operation-checkmate-blacksuit]] | operation | 87 | 5 | 295 | 4934 | enrich_from_existing_raw_sources | source_rich_thin_body:295w, missing_quality_sections:2/6, raw_available_underused:4934w_sources, high_source_to_body_gap |
| 30 | [[operation-red-card]] | operation | 87 | 6 | 313 | 4332 | enrich_from_existing_raw_sources | source_rich_thin_body:313w, missing_quality_sections:2/6, raw_available_underused:4332w_sources, high_source_to_body_gap |
| 31 | [[fake-shopping-sites-takedown-2024]] | operation | 87 | 6 | 162 | 4265 | enrich_from_existing_raw_sources | source_rich_thin_body:162w, missing_quality_sections:2/6, raw_available_underused:4265w_sources, high_source_to_body_gap |
| 32 | [[operation-wirewire]] | operation | 87 | 5 | 162 | 4173 | enrich_from_existing_raw_sources | source_rich_thin_body:162w, missing_quality_sections:2/6, raw_available_underused:4173w_sources, high_source_to_body_gap |
| 33 | [[operation-eur-100m-illegal-financial-service-laundering-2025]] | operation | 87 | 5 | 165 | 3881 | enrich_from_existing_raw_sources | source_rich_thin_body:165w, missing_quality_sections:2/6, raw_available_underused:3881w_sources, high_source_to_body_gap |
| 34 | [[operation-stream-kidflix]] | operation | 87 | 6 | 316 | 3822 | enrich_from_existing_raw_sources | source_rich_thin_body:316w, missing_quality_sections:2/6, raw_available_underused:3822w_sources, high_source_to_body_gap |
| 35 | [[operation-haechi-ii]] | operation | 87 | 5 | 198 | 3733 | enrich_from_existing_raw_sources | source_rich_thin_body:198w, missing_quality_sections:2/6, raw_available_underused:3733w_sources, high_source_to_body_gap |
| 36 | [[2bagoldmule-qqaazz]] | operation | 87 | 5 | 169 | 3651 | enrich_from_existing_raw_sources | source_rich_thin_body:169w, missing_quality_sections:2/6, raw_available_underused:3651w_sources, high_source_to_body_gap |
| 37 | [[operation-eur-600m-crypto-scam-network-2025]] | operation | 87 | 5 | 85 | 3242 | enrich_from_existing_raw_sources | source_rich_thin_body:85w, missing_quality_sections:2/6, raw_available_underused:3242w_sources, high_source_to_body_gap |
| 38 | [[hive-ransomware-takedown]] | operation | 87 | 5 | 181 | 2915 | enrich_from_existing_raw_sources | source_rich_thin_body:181w, missing_quality_sections:2/6, raw_available_underused:2915w_sources, high_source_to_body_gap |
| 39 | [[banking-trojan-fraud-sentencing-2017]] | operation | 83 | 5 | 317 | 4006 | enrich_from_existing_raw_sources | source_rich_thin_body:317w, raw_available_underused:4006w_sources, high_source_to_body_gap, possible_crime_type_mismatch:malware-ic |
| 40 | [[operation-delilah]] | operation | 83 | 5 | 312 | 3708 | enrich_from_existing_raw_sources | source_rich_thin_body:312w, raw_available_underused:3708w_sources, high_source_to_body_gap, possible_crime_type_mismatch:malware-ic |
| 41 | [[simda-botnet-takedown]] | operation | 83 | 5 | 183 | 1733 | enrich_from_existing_raw_sources | source_rich_thin_body:183w, missing_quality_sections:2/6, raw_available_underused:1733w_sources, unresolved_operation_name |
| 42 | [[bremerton-washington-man-sentenced-to-3-years-in-prison-for-extensive-swatting-campaign-targeting-victims-in-u]] | case | 75 | 5 | 152 | 1620 | enrich_from_existing_raw_sources | source_rich_thin_body:152w, missing_quality_sections:2/6, raw_available_underused:1620w_sources |
| 43 | [[operation-bremerton-washington-man-sentenced-to-3-years-in-prison-for-extensive-swatting-campaign-targeting-victims-in-u]] | operation | 75 | 5 | 309 | 1620 | enrich_from_existing_raw_sources | source_rich_thin_body:309w, missing_quality_sections:3/6, raw_available_underused:1620w_sources |
| 44 | [[operation-eur-3m-online-investment-fraud-2025]] | operation | 75 | 5 | 101 | 1619 | enrich_from_existing_raw_sources | source_rich_thin_body:101w, missing_quality_sections:1/6, raw_available_underused:1619w_sources |
| 45 | [[dark-web-narcotics-trafficker-sentenced-to-96-months-in-prison-for-distributing-fentanyl-heroin-methamphetamin]] | case | 75 | 6 | 195 | 1308 | enrich_from_existing_raw_sources | source_rich_thin_body:195w, missing_quality_sections:2/6, raw_available_underused:1308w_sources |
| 46 | [[operation-dark-web-narcotics-trafficker-sentenced-to-96-months-in-prison-for-distributing-fentanyl-heroin-methamphetamin]] | operation | 75 | 6 | 340 | 1308 | enrich_from_existing_raw_sources | source_rich_thin_body:340w, missing_quality_sections:3/6, raw_available_underused:1308w_sources |
| 47 | [[operation-eur-100m-crypto-investment-fraud-2025]] | operation | 75 | 5 | 171 | 1247 | enrich_from_existing_raw_sources | source_rich_thin_body:171w, missing_quality_sections:2/6, raw_available_underused:1247w_sources |
| 48 | [[operation-lyrebird]] | operation | 69 | 5 | 264 | 9605 | enrich_from_existing_raw_sources | source_rich_thin_body:264w, raw_available_underused:9605w_sources, high_source_to_body_gap |
| 49 | [[operation-hyperion]] | operation | 69 | 6 | 267 | 5214 | enrich_from_existing_raw_sources | source_rich_thin_body:267w, raw_available_underused:5214w_sources, high_source_to_body_gap |
| 50 | [[operation-nightfury]] | operation | 69 | 6 | 312 | 4936 | enrich_from_existing_raw_sources | source_rich_thin_body:312w, raw_available_underused:4936w_sources, high_source_to_body_gap |
| 51 | [[operation-falcon]] | operation | 67 | 5 | 162 | 417 | manual_crime_type_review | source_rich_thin_body:162w, missing_quality_sections:2/6, possible_crime_type_mismatch:malware-ic |
| 52 | [[nemesis-market-takedown]] | operation | 67 | 5 | 190 | 281 | manual_crime_type_review | source_rich_thin_body:190w, missing_quality_sections:3/6, possible_crime_type_mismatch:dark-web-ic |
| 53 | [[us-v-parsarad-nemesis]] | case | 67 | 5 | 223 | 279 | manual_crime_type_review | source_rich_thin_body:223w, missing_quality_sections:3/6, possible_crime_type_mismatch:dark-web-ic |
| 54 | [[operation-talent]] | operation | 67 | 5 | 342 | 139 | manual_crime_type_review | source_rich_thin_body:342w, missing_quality_sections:2/6, possible_crime_type_mismatch:malware-ic |
| 55 | [[operation-shrouded-horizon]] | operation | 67 | 5 | 260 | 0 | manual_crime_type_review | source_rich_thin_body:260w, missing_quality_sections:2/6, possible_crime_type_mismatch:malware-ic |
| 56 | [[operation-bakovia]] | operation | 66 | 5 | 360 | 8335 | manual_crime_type_review | missing_quality_sections:3/6, raw_available_underused:8335w_sources, high_source_to_body_gap, possible_crime_type_mismatch:malware-ic |
| 57 | [[operation-haechi-iv]] | operation | 66 | 5 | 442 | 5457 | manual_crime_type_review | missing_quality_sections:2/6, raw_available_underused:5457w_sources, high_source_to_body_gap, possible_crime_type_mismatch:bec-ic |
| 58 | [[two-southern-california-men-who-supplied-fentanyl-sold-to-darknet-customers-in-all-50-states-sentenced-to-fede]] | case | 64 | 1 | 92 | 1225 | replace_placeholder_or_absorb_wrapper | placeholder_language:6, raw_available_underused:1225w_sources, possible_crime_type_mismatch:dark-web-ic |
| 59 | [[operation-europol-105-arrested-for-stealing-over-12-million-from-us-based-banks-operation-secreto]] | operation | 63 | 5 | 124 | 437 | manual_review | source_rich_thin_body:124w, missing_quality_sections:2/6, generated_enforcement_title |
| 60 | [[operation-us-v-parsarad-nemesis]] | operation | 63 | 5 | 75 | 279 | manual_review | source_rich_thin_body:75w, missing_quality_sections:1/6, generated_enforcement_title |
| 61 | [[black-axe-bec-2021]] | operation | 57 | 5 | 280 | 2259 | enrich_from_existing_raw_sources | source_rich_thin_body:280w, raw_available_underused:2259w_sources |
| 62 | [[marketplace-a-dekhtyarchuk-indictment]] | operation | 57 | 5 | 288 | 1620 | enrich_from_existing_raw_sources | source_rich_thin_body:288w, raw_available_underused:1620w_sources |
| 63 | [[operation-secure-interpol]] | operation | 54 | 5 | 375 | 1826 | manual_crime_type_review | missing_quality_sections:2/6, raw_available_underused:1826w_sources, possible_crime_type_mismatch:ransomware-ic |
| 64 | [[qakbot-gallyamov-indictment]] | operation | 54 | 5 | 364 | 1787 | manual_crime_type_review | missing_quality_sections:2/6, raw_available_underused:1787w_sources, possible_crime_type_mismatch:malware-ic |
| 65 | [[operation-eur-300m-global-credit-card-fraud-2025]] | operation | 53 | 5 | 113 | 799 | manual_review | source_rich_thin_body:113w, missing_quality_sections:2/6 |
| 66 | [[operation-secreto]] | operation | 53 | 5 | 162 | 437 | manual_review | source_rich_thin_body:162w, missing_quality_sections:2/6 |
| 67 | [[105-arrested-for-stealing-over-eur-12-million-from-us-based-banks]] | case | 53 | 5 | 202 | 213 | manual_review | source_rich_thin_body:202w, missing_quality_sections:2/6 |
| 68 | [[operation-de-fr-online-fraud-group-2026]] | operation | 53 | 5 | 144 | 170 | manual_review | source_rich_thin_body:144w, missing_quality_sections:2/6 |
| 69 | [[operation-serengeti]] | operation | 52 | 5 | 360 | 17967 | manual_review | missing_quality_sections:3/6, raw_available_underused:17967w_sources, high_source_to_body_gap |
| 70 | [[franco-israeli-ceo-fraud]] | operation | 52 | 5 | 413 | 4169 | manual_review | missing_quality_sections:3/6, raw_available_underused:4169w_sources, high_source_to_body_gap |
| 71 | [[operation-contender-2]] | operation | 52 | 6 | 353 | 3147 | manual_review | missing_quality_sections:2/6, raw_available_underused:3147w_sources, high_source_to_body_gap |
| 72 | [[operation-jackal-iii]] | operation | 52 | 5 | 364 | 2651 | manual_review | missing_quality_sections:2/6, raw_available_underused:2651w_sources, high_source_to_body_gap |
| 73 | [[operation-jackal]] | operation | 52 | 5 | 358 | 2591 | manual_review | missing_quality_sections:2/6, raw_available_underused:2591w_sources, high_source_to_body_gap |
| 74 | [[ross-ulbricht-sentenced-to-life-in-federal-prison]] | case | 50 | 1 | 81 | 2007 | replace_placeholder_or_absorb_wrapper | placeholder_language:6, raw_available_underused:2007w_sources |
| 75 | [[senior-advisor-arrested-in-thailand]] | case | 50 | 1 | 78 | 1937 | replace_placeholder_or_absorb_wrapper | placeholder_language:6, raw_available_underused:1937w_sources |
| 76 | [[ross-ulbricht-sentenced-to-life-in-prison]] | case | 50 | 1 | 80 | 1532 | replace_placeholder_or_absorb_wrapper | placeholder_language:6, raw_available_underused:1532w_sources |
| 77 | [[ross-ulbricht-found-guilty-on-all-counts]] | case | 50 | 1 | 80 | 1447 | replace_placeholder_or_absorb_wrapper | placeholder_language:6, raw_available_underused:1447w_sources |
| 78 | [[5-charged-in-2-8-million-dark-web-drug-trafficking-money-laundering-conspiracy]] | case | 50 | 1 | 85 | 1386 | replace_placeholder_or_absorb_wrapper | placeholder_language:6, raw_available_underused:1386w_sources |
| 79 | [[us-v-in-manhattan-federal-court]] | case | 50 | 1 | 84 | 1330 | replace_placeholder_or_absorb_wrapper | placeholder_language:6, raw_available_underused:1330w_sources |
| 80 | [[us-v-bugat-botnet-administrator]] | case | 50 | 1 | 83 | 1270 | replace_placeholder_or_absorb_wrapper | placeholder_language:6, raw_available_underused:1270w_sources |
| 81 | [[bugat-botnet-administrator-arrested-and-malware-disabled]] | case | 50 | 1 | 83 | 1264 | replace_placeholder_or_absorb_wrapper | placeholder_language:6, raw_available_underused:1264w_sources |
| 82 | [[operation-nervone]] | operation | 49 | 5 | 302 | 172 | manual_crime_type_review | source_rich_thin_body:302w, possible_crime_type_mismatch:bec-ic |
| 83 | [[darkode-takedown]] | operation | 48 | 5 | 407 | 10629 | manual_crime_type_review | raw_available_underused:10629w_sources, high_source_to_body_gap, possible_crime_type_mismatch:malware-ic |
| 84 | [[operation-destabilise]] | operation | 48 | 5 | 377 | 7642 | manual_crime_type_review | raw_available_underused:7642w_sources, high_source_to_body_gap, possible_crime_type_mismatch:ransomware-ic |
| 85 | [[zeus-spyeye-takedown]] | operation | 48 | 6 | 398 | 5796 | manual_crime_type_review | raw_available_underused:5796w_sources, high_source_to_body_gap, possible_crime_type_mismatch:malware-ic |
| 86 | [[operation-nova]] | operation | 48 | 5 | 369 | 5789 | manual_crime_type_review | raw_available_underused:5789w_sources, high_source_to_body_gap, possible_crime_type_mismatch:ransomware-ic |
| 87 | [[qqaazz-money-laundering-takedown]] | operation | 48 | 5 | 359 | 3943 | manual_crime_type_review | raw_available_underused:3943w_sources, high_source_to_body_gap, possible_crime_type_mismatch:bec-ic |
| 88 | [[imminent-monitor-rat-takedown]] | operation | 48 | 5 | 412 | 3780 | manual_crime_type_review | raw_available_underused:3780w_sources, high_source_to_body_gap, possible_crime_type_mismatch:malware-ic |
| 89 | [[operation-morpheus]] | operation | 48 | 5 | 426 | 2595 | manual_crime_type_review | raw_available_underused:2595w_sources, high_source_to_body_gap, possible_crime_type_mismatch:ransomware-ic |
| 90 | [[3-north-korean-military-hackers-indicted-in-wide-ranging-scheme-to-commit-cyber-attacks-and-financial-crimes-a]] | case | 47 | 1 | 69 | 2501 | replace_placeholder_or_absorb_wrapper | placeholder_language:5, raw_available_underused:2501w_sources |
| 91 | [[founder-and-majority-owner-of-bitzlato-a-cryptocurrency-exchange-charged-with-unlicensed-money-transmitting]] | case | 47 | 1 | 65 | 1889 | replace_placeholder_or_absorb_wrapper | placeholder_language:5, raw_available_underused:1889w_sources |
| 92 | [[2-defendants-charged-in-u-s-courts-as-part-of-global-crackdown-on-booter-services-offering-distributed-denial-]] | case | 47 | 1 | 69 | 1688 | replace_placeholder_or_absorb_wrapper | placeholder_language:5, raw_available_underused:1688w_sources |
| 93 | [[canadian-hacker-who-conspired-with-and-aided-russian-fsb-officers-pleads-guilty]] | case | 47 | 1 | 63 | 1652 | replace_placeholder_or_absorb_wrapper | placeholder_language:5, raw_available_underused:1652w_sources |
| 94 | [[dark-web-vendor-of-illegal-narcotics-indicted-for-distributing-heroin-and-cocaine-in-exchange-for-bitcoin]] | case | 47 | 1 | 67 | 1525 | replace_placeholder_or_absorb_wrapper | placeholder_language:5, raw_available_underused:1525w_sources |
| 95 | [[former-hedge-fund-manager-convicted-of-wire-fraud-money-laundering-and-contempt-of-court]] | case | 47 | 1 | 65 | 1276 | replace_placeholder_or_absorb_wrapper | placeholder_language:5, raw_available_underused:1276w_sources |
| 96 | [[four-members-of-notorious-cybercrime-group-fin9-charged-for-roles-in-attacking-u-s-companies]] | case | 47 | 1 | 65 | 1258 | replace_placeholder_or_absorb_wrapper | placeholder_language:5, raw_available_underused:1258w_sources |
| 97 | [[citizen-of-croatia-and-serbia-charged-with-running-monopoly-drug-market-on-the-darknet]] | case | 47 | 1 | 65 | 1253 | replace_placeholder_or_absorb_wrapper | placeholder_language:5, raw_available_underused:1253w_sources |
| 98 | [[4-arrested-in-latest-l-a-county-based-jcode-operation-for-allegedly-operating-a-drug-distribution-network-on-t]] | case | 47 | 1 | 69 | 1248 | replace_placeholder_or_absorb_wrapper | placeholder_language:5, raw_available_underused:1248w_sources |
| 99 | [[nigerian-bec-convictions-2023]] | operation | 35 | 5 | 267 | 298 | manual_review | source_rich_thin_body:267w |

## Execution Rules

1. Fix `duplicate_source_url_refs` before counting a page as source-rich.
2. For `enrich_from_existing_raw_sources`, use already collected raw/source text first.
3. For `replace_placeholder_or_absorb_wrapper`, decide whether the page is a real case/operation or a wrapper that should point to a canonical record.
4. For `manual_crime_type_review`, do not change taxonomy without source-backed review.
