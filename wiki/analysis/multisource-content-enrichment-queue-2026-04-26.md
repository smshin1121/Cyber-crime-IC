---
title: Multi-Source Content Enrichment Queue (2026-04-26)
type: analysis
created: 2026-04-26
updated: 2026-04-26
summary: "Queue for enriching operation and case pages from existing source records."
source_count: 0
---
## Summary

This queue converts the content-depth audit into an execution list. It is ordered to fix pages where existing sources already contain enough material before searching for new sources.

- Selection mode: **all operation/case pages with at least 2 sources**
- Audited operation/case pages: **2287**
- Queue size: **145**

## Top Queue

| Rank | Page | Type | Score | Sources | Body words | Source words | Recommendation | Issues |
|---:|---|---|---:|---:|---:|---:|---|---|
| 1 | [[australian-man-arrested-in-germany-accused-of-running-world-s-largest-darknet-marketplace]] | case | 34 | 5 | 447 | 8894 | enrich_all_multisource_from_existing_sources | raw_available_underused:8894w_sources, high_source_to_body_gap |
| 2 | [[operation-germany-romania-trusted-seller-fraud-2025]] | operation | 34 | 5 | 368 | 5255 | enrich_all_multisource_from_existing_sources | raw_available_underused:5255w_sources, high_source_to_body_gap |
| 3 | [[romania-phishing-takedown-2024]] | operation | 34 | 5 | 375 | 4242 | enrich_all_multisource_from_existing_sources | raw_available_underused:4242w_sources, high_source_to_body_gap |
| 4 | [[operation-eur-100m-illegal-financial-service-laundering-2025]] | operation | 34 | 5 | 426 | 3881 | enrich_all_multisource_from_existing_sources | raw_available_underused:3881w_sources, high_source_to_body_gap |
| 5 | [[operation-french-coder-who-helped-extort-british-company-arrested-in-thailand]] | operation | 34 | 5 | 391 | 2598 | enrich_all_multisource_from_existing_sources | raw_available_underused:2598w_sources, high_source_to_body_gap |
| 6 | [[bremerton-washington-man-sentenced-to-3-years-in-prison-for-extensive-swatting-campaign-targeting-victims-in-u]] | case | 22 | 5 | 427 | 1620 | enrich_all_multisource_from_existing_sources | raw_available_underused:1620w_sources |
| 7 | [[operation-eur-3m-online-investment-fraud-2025]] | operation | 22 | 5 | 408 | 1619 | enrich_all_multisource_from_existing_sources | raw_available_underused:1619w_sources |
| 8 | [[operation-eur-100m-crypto-investment-fraud-2025]] | operation | 22 | 5 | 448 | 1247 | enrich_all_multisource_from_existing_sources | raw_available_underused:1247w_sources |
| 9 | [[proxy-service-takedown-2026-03]] | operation | 14 | 5 | 1126 | 3540 | enrich_all_multisource_from_existing_sources | possible_crime_type_mismatch:ransomware-ic |
| 10 | [[operation-avalanche]] | operation | 14 | 7 | 795 | 2942 | enrich_all_multisource_from_existing_sources | possible_crime_type_mismatch:dark-web-ic |
| 11 | [[xdedic-marketplace-takedown]] | operation | 14 | 9 | 1128 | 2481 | enrich_all_multisource_from_existing_sources | possible_crime_type_mismatch:malware-ic |
| 12 | [[us-v-galochkin-trickbot-conti]] | case | 14 | 3 | 806 | 502 | enrich_all_multisource_from_existing_sources | possible_crime_type_mismatch:dark-web-ic |
| 13 | [[infraud-organization-takedown]] | operation | 14 | 7 | 555 | 0 | enrich_all_multisource_from_existing_sources | possible_crime_type_mismatch:dark-web-ic |
| 14 | [[operation-heart-blocker]] | operation | 14 | 5 | 1538 | 0 | enrich_all_multisource_from_existing_sources | possible_crime_type_mismatch:malware-ic |
| 15 | [[operation-serengeti]] | operation | 12 | 5 | 596 | 17967 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 16 | [[darkode-takedown]] | operation | 12 | 5 | 671 | 10629 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 17 | [[operation-lyrebird]] | operation | 12 | 5 | 509 | 9605 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 18 | [[operation-cyber-guardian]] | operation | 12 | 5 | 627 | 9162 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 19 | [[global-airport-action-day]] | operation | 12 | 6 | 520 | 9151 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 20 | [[darkmarket-takedown]] | operation | 12 | 5 | 491 | 8894 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 21 | [[operation-australian-man-arrested-in-germany-accused-of-running-world-s-largest-darknet-marketplace]] | operation | 12 | 5 | 515 | 8894 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 22 | [[operation-bakovia]] | operation | 12 | 5 | 631 | 8335 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 23 | [[150-arrested-in-dark-web-drug-bust-as-police-seize-eur-26-million]] | case | 12 | 5 | 505 | 8025 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 24 | [[operation-destabilise]] | operation | 12 | 5 | 628 | 7642 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 25 | [[us-v-of-silk-road]] | case | 12 | 5 | 556 | 7160 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 26 | [[operation-killer-bee]] | operation | 12 | 5 | 544 | 6852 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 27 | [[operation-operation-orion-international-144-arrested-in-major-child-abuse-operation-across-south-america]] | operation | 12 | 5 | 527 | 5977 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 28 | [[zeus-spyeye-jit-takedown]] | operation | 12 | 6 | 510 | 5796 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 29 | [[zeus-spyeye-takedown]] | operation | 12 | 6 | 694 | 5796 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 30 | [[operation-nova]] | operation | 12 | 5 | 575 | 5789 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 31 | [[operation-orion-international]] | operation | 12 | 5 | 585 | 5782 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 32 | [[cyber-fraud-international-2015]] | operation | 12 | 5 | 508 | 5663 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 33 | [[lakeland-man-pleads-guilty-to-receiving-child-sex-abuse-videos-from-the-largest-darknet-child-pornography-webs]] | case | 12 | 5 | 567 | 5593 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 34 | [[ddos-for-hire-sweep-2016]] | operation | 12 | 6 | 501 | 5484 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 35 | [[operation-hyperion]] | operation | 12 | 6 | 491 | 5214 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 36 | [[operation-nightfury]] | operation | 12 | 6 | 644 | 4936 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 37 | [[operation-checkmate-blacksuit]] | operation | 12 | 5 | 578 | 4934 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 38 | [[operation-12-members-of-an-irish-high-risk-criminal-network-arrested]] | operation | 12 | 6 | 469 | 4839 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 39 | [[operation-red-card]] | operation | 12 | 6 | 555 | 4332 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 40 | [[fake-shopping-sites-takedown-2024]] | operation | 12 | 6 | 505 | 4265 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 41 | [[operation-sentinel-africa]] | operation | 12 | 5 | 608 | 4239 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 42 | [[operation-wirewire]] | operation | 12 | 5 | 517 | 4173 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 43 | [[franco-israeli-ceo-fraud]] | operation | 12 | 5 | 663 | 4169 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 44 | [[banking-trojan-fraud-sentencing-2017]] | operation | 12 | 5 | 593 | 4006 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 45 | [[qqaazz-money-laundering-takedown]] | operation | 12 | 5 | 674 | 3943 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 46 | [[operation-stream-kidflix]] | operation | 12 | 6 | 612 | 3822 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 47 | [[imminent-monitor-rat-takedown]] | operation | 12 | 5 | 525 | 3780 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 48 | [[rydox-marketplace-takedown]] | operation | 12 | 5 | 663 | 3759 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 49 | [[operation-haechi-ii]] | operation | 12 | 5 | 567 | 3733 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 50 | [[operation-delilah]] | operation | 12 | 5 | 642 | 3708 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 51 | [[2bagoldmule-qqaazz]] | operation | 12 | 5 | 513 | 3651 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 52 | [[operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown-3]] | operation | 12 | 5 | 468 | 3378 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 53 | [[lumma-stealer-takedown]] | operation | 12 | 5 | 576 | 3284 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 54 | [[operation-eur-600m-crypto-scam-network-2025]] | operation | 12 | 5 | 457 | 3242 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 55 | [[operation-contender-2]] | operation | 12 | 6 | 651 | 3147 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 56 | [[operation-source]] | operation | 12 | 5 | 482 | 3084 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 57 | [[operation-europol-french-coder-who-helped-extort-british-company-arrested-in-thailand]] | operation | 12 | 5 | 474 | 2924 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 58 | [[rex-mundi-takedown]] | operation | 12 | 5 | 491 | 2924 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 59 | [[hive-ransomware-takedown]] | operation | 12 | 5 | 501 | 2915 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 60 | [[operation-pleiades]] | operation | 12 | 5 | 562 | 2893 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 61 | [[operation-jackal-iii]] | operation | 12 | 5 | 676 | 2651 | enrich_all_multisource_from_existing_sources | high_source_to_body_gap |
| 62 | [[operation-first-light-2024]] | operation | 0 | 5 | 818 | 44742 | enrich_all_multisource_from_existing_sources |  |
| 63 | [[silk-road-takedown]] | operation | 0 | 7 | 2373 | 11006 | enrich_all_multisource_from_existing_sources |  |
| 64 | [[alphabay-takedown]] | operation | 0 | 5 | 2232 | 9599 | enrich_all_multisource_from_existing_sources |  |
| 65 | [[operation-dark-huntor]] | operation | 0 | 5 | 1781 | 8025 | enrich_all_multisource_from_existing_sources |  |
| 66 | [[isoon-apt27-indictment]] | operation | 0 | 6 | 704 | 8012 | enrich_all_multisource_from_existing_sources |  |
| 67 | [[operation-power-off]] | operation | 0 | 7 | 1552 | 7211 | enrich_all_multisource_from_existing_sources |  |
| 68 | [[operation-rewired]] | operation | 0 | 5 | 1461 | 6829 | enrich_all_multisource_from_existing_sources |  |
| 69 | [[operation-endgame]] | operation | 0 | 9 | 2786 | 6174 | enrich_all_multisource_from_existing_sources |  |
| 70 | [[operation-cronos-phase1]] | operation | 0 | 7 | 1005 | 6027 | enrich_all_multisource_from_existing_sources |  |
| 71 | [[emotet-takedown]] | operation | 0 | 6 | 1904 | 5776 | enrich_all_multisource_from_existing_sources |  |
| 72 | [[carding-action-2020]] | operation | 0 | 6 | 1170 | 5589 | enrich_all_multisource_from_existing_sources |  |
| 73 | [[operation-haechi-iv]] | operation | 0 | 5 | 770 | 5457 | enrich_all_multisource_from_existing_sources |  |
| 74 | [[operation-endgame-phase1]] | operation | 0 | 5 | 833 | 5290 | enrich_all_multisource_from_existing_sources |  |
| 75 | [[operation-cronos-phase3]] | operation | 0 | 5 | 910 | 5154 | enrich_all_multisource_from_existing_sources |  |
| 76 | [[goznym-takedown]] | operation | 0 | 5 | 941 | 4981 | enrich_all_multisource_from_existing_sources |  |
| 77 | [[operation-haechi-v]] | operation | 0 | 5 | 804 | 4635 | enrich_all_multisource_from_existing_sources |  |
| 78 | [[zambia-golden-top-call-center]] | operation | 0 | 8 | 778 | 3754 | enrich_all_multisource_from_existing_sources |  |
| 79 | [[operation-haechi-iii]] | operation | 0 | 5 | 1675 | 3690 | enrich_all_multisource_from_existing_sources |  |
| 80 | [[operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown]] | operation | 0 | 5 | 756 | 3378 | enrich_all_multisource_from_existing_sources |  |
| 81 | [[operation-trojan-shield]] | operation | 0 | 6 | 734 | 3019 | enrich_all_multisource_from_existing_sources |  |
| 82 | [[vpnlab-takedown]] | operation | 0 | 5 | 1490 | 2932 | enrich_all_multisource_from_existing_sources |  |
| 83 | [[korea-cambodia-scam-repatriation]] | operation | 0 | 5 | 725 | 2874 | enrich_all_multisource_from_existing_sources |  |
| 84 | [[ramnit-botnet-takedown]] | operation | 0 | 5 | 793 | 2849 | enrich_all_multisource_from_existing_sources |  |
| 85 | [[operation-haechi-vi]] | operation | 0 | 5 | 921 | 2733 | enrich_all_multisource_from_existing_sources |  |
| 86 | [[operation-morpheus]] | operation | 0 | 5 | 701 | 2595 | enrich_all_multisource_from_existing_sources |  |
| 87 | [[operation-jackal]] | operation | 0 | 5 | 705 | 2591 | enrich_all_multisource_from_existing_sources |  |
| 88 | [[de-ch-crypto-mixer-takedown-2025]] | operation | 0 | 5 | 978 | 2589 | enrich_all_multisource_from_existing_sources |  |
| 89 | [[operation-endgame-phase2]] | operation | 0 | 7 | 1008 | 2559 | enrich_all_multisource_from_existing_sources |  |
| 90 | [[korea-china-voice-phishing-qingdao]] | operation | 0 | 5 | 726 | 2430 | enrich_all_multisource_from_existing_sources |  |
| 91 | [[black-axe-bec-2021]] | operation | 0 | 5 | 555 | 2259 | enrich_all_multisource_from_existing_sources |  |
| 92 | [[operation-chakra-iii]] | operation | 0 | 5 | 1486 | 2178 | enrich_all_multisource_from_existing_sources |  |
| 93 | [[bec-nigeria-2016]] | operation | 0 | 5 | 980 | 2041 | enrich_all_multisource_from_existing_sources |  |
| 94 | [[emotet-disruption-ladybird]] | case | 0 | 3 | 665 | 2019 | enrich_all_multisource_from_existing_sources |  |
| 95 | [[911-s5-botnet-takedown]] | operation | 0 | 5 | 469 | 1954 | enrich_all_multisource_from_existing_sources |  |
| 96 | [[cyberbunker-takedown]] | operation | 0 | 5 | 1724 | 1845 | enrich_all_multisource_from_existing_sources |  |
| 97 | [[operation-secure-interpol]] | operation | 0 | 5 | 616 | 1826 | enrich_all_multisource_from_existing_sources |  |
| 98 | [[qakbot-gallyamov-indictment]] | operation | 0 | 5 | 618 | 1787 | enrich_all_multisource_from_existing_sources |  |
| 99 | [[simda-botnet-takedown]] | operation | 0 | 5 | 482 | 1733 | enrich_all_multisource_from_existing_sources |  |
| 100 | [[marketplace-a-dekhtyarchuk-indictment]] | operation | 0 | 5 | 664 | 1620 | enrich_all_multisource_from_existing_sources |  |
| 101 | [[operation-bremerton-washington-man-sentenced-to-3-years-in-prison-for-extensive-swatting-campaign-targeting-victims-in-u]] | operation | 0 | 5 | 626 | 1620 | enrich_all_multisource_from_existing_sources |  |
| 102 | [[belgium-netherlands-phishing-gang]] | operation | 0 | 5 | 589 | 1598 | enrich_all_multisource_from_existing_sources |  |
| 103 | [[fin7-takedown]] | operation | 0 | 5 | 575 | 1543 | enrich_all_multisource_from_existing_sources |  |
| 104 | [[operation-goldfish-alpha-night-fury]] | operation | 0 | 5 | 538 | 1486 | enrich_all_multisource_from_existing_sources |  |
| 105 | [[dark-web-narcotics-trafficker-sentenced-to-96-months-in-prison-for-distributing-fentanyl-heroin-methamphetamin]] | case | 0 | 6 | 510 | 1308 | enrich_all_multisource_from_existing_sources |  |
| 106 | [[operation-dark-web-narcotics-trafficker-sentenced-to-96-months-in-prison-for-distributing-fentanyl-heroin-methamphetamin]] | operation | 0 | 6 | 666 | 1308 | enrich_all_multisource_from_existing_sources |  |
| 107 | [[andromeda-botnet-takedown]] | operation | 0 | 4 | 496 | 1185 | enrich_all_multisource_from_existing_sources |  |
| 108 | [[us-v-okpe-obogo-bec]] | case | 0 | 5 | 848 | 1106 | enrich_all_multisource_from_existing_sources |  |
| 109 | [[us-v-miller-poweroff]] | case | 0 | 2 | 712 | 1075 | enrich_all_multisource_from_existing_sources |  |
| 110 | [[phobos-8base-crackdown]] | operation | 0 | 5 | 711 | 1019 | enrich_all_multisource_from_existing_sources |  |
| 111 | [[doublevpn-takedown]] | operation | 0 | 5 | 1260 | 937 | enrich_all_multisource_from_existing_sources |  |
| 112 | [[operation-eur-300m-global-credit-card-fraud-2025]] | operation | 0 | 5 | 354 | 799 | enrich_all_multisource_from_existing_sources |  |
| 113 | [[africa-cyber-surge-ii]] | operation | 0 | 5 | 624 | 748 | enrich_all_multisource_from_existing_sources |  |
| 114 | [[operation-synergia-ii]] | operation | 0 | 5 | 638 | 742 | enrich_all_multisource_from_existing_sources |  |
| 115 | [[us-v-ulbricht-silk-road]] | case | 0 | 2 | 938 | 689 | enrich_all_multisource_from_existing_sources |  |
| 116 | [[us-v-yakubets-dridex]] | case | 0 | 3 | 691 | 463 | enrich_all_multisource_from_existing_sources |  |
| 117 | [[operation-europol-105-arrested-for-stealing-over-12-million-from-us-based-banks-operation-secreto]] | operation | 0 | 5 | 519 | 437 | enrich_all_multisource_from_existing_sources |  |
| 118 | [[operation-secreto]] | operation | 0 | 5 | 543 | 437 | enrich_all_multisource_from_existing_sources |  |
| 119 | [[operation-falcon]] | operation | 0 | 5 | 474 | 417 | enrich_all_multisource_from_existing_sources |  |
| 120 | [[blackcat-lockeroga-kelvin-security-2023]] | operation | 0 | 5 | 793 | 338 | enrich_all_multisource_from_existing_sources |  |
| 121 | [[cryptex-pm2btc-sanctions]] | operation | 0 | 6 | 651 | 338 | enrich_all_multisource_from_existing_sources |  |
| 122 | [[nigerian-bec-convictions-2023]] | operation | 0 | 5 | 564 | 298 | enrich_all_multisource_from_existing_sources |  |
| 123 | [[nemesis-market-takedown]] | operation | 0 | 5 | 443 | 281 | enrich_all_multisource_from_existing_sources |  |
| 124 | [[operation-us-v-parsarad-nemesis]] | operation | 0 | 5 | 450 | 279 | enrich_all_multisource_from_existing_sources |  |
| 125 | [[us-v-parsarad-nemesis]] | case | 0 | 5 | 484 | 279 | enrich_all_multisource_from_existing_sources |  |
| 126 | [[us-v-gudmunds-darkode]] | case | 0 | 2 | 516 | 262 | enrich_all_multisource_from_existing_sources |  |
| 127 | [[carbanak-cobalt-takedown]] | operation | 0 | 4 | 588 | 260 | enrich_all_multisource_from_existing_sources |  |
| 128 | [[mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain]] | case | 0 | 4 | 463 | 260 | enrich_all_multisource_from_existing_sources |  |
| 129 | [[us-v-bondarenko-infraud]] | case | 0 | 2 | 626 | 220 | enrich_all_multisource_from_existing_sources |  |
| 130 | [[us-v-astamirov-vasiliev-lockbit]] | case | 0 | 2 | 766 | 217 | enrich_all_multisource_from_existing_sources |  |
| 131 | [[105-arrested-for-stealing-over-eur-12-million-from-us-based-banks]] | case | 0 | 5 | 501 | 213 | enrich_all_multisource_from_existing_sources |  |
| 132 | [[operation-105-arrested-for-stealing-over-eur-12-million-from-us-based-banks]] | operation | 0 | 5 | 671 | 213 | enrich_all_multisource_from_existing_sources |  |
| 133 | [[us-v-stepanov-danabot]] | case | 0 | 2 | 518 | 212 | enrich_all_multisource_from_existing_sources |  |
| 134 | [[us-v-anom-distributors]] | case | 0 | 2 | 750 | 188 | enrich_all_multisource_from_existing_sources |  |
| 135 | [[operation-nervone]] | operation | 0 | 5 | 474 | 172 | enrich_all_multisource_from_existing_sources |  |
| 136 | [[operation-de-fr-online-fraud-group-2026]] | operation | 0 | 5 | 372 | 170 | enrich_all_multisource_from_existing_sources |  |
| 137 | [[operation-talent]] | operation | 0 | 5 | 581 | 139 | enrich_all_multisource_from_existing_sources |  |
| 138 | [[bali-villa-cybercrime-raid-2024]] | operation | 0 | 5 | 1449 | 0 | enrich_all_multisource_from_existing_sources |  |
| 139 | [[bidencash-takedown]] | operation | 0 | 5 | 1566 | 0 | enrich_all_multisource_from_existing_sources |  |
| 140 | [[dridex-operations]] | operation | 0 | 8 | 2181 | 0 | enrich_all_multisource_from_existing_sources |  |
| 141 | [[myanmar-kokang-scam-compound-crackdown]] | operation | 0 | 5 | 2115 | 0 | enrich_all_multisource_from_existing_sources |  |
| 142 | [[operation-kraken-ghost-platform]] | operation | 0 | 6 | 1898 | 0 | enrich_all_multisource_from_existing_sources |  |
| 143 | [[operation-onymous]] | operation | 0 | 5 | 1905 | 0 | enrich_all_multisource_from_existing_sources |  |
| 144 | [[operation-shrouded-horizon]] | operation | 0 | 5 | 415 | 0 | enrich_all_multisource_from_existing_sources |  |
| 145 | [[trickbot-operations]] | operation | 0 | 5 | 1907 | 0 | enrich_all_multisource_from_existing_sources |  |

## Execution Rules

1. Fix `duplicate_source_url_refs` before counting a page as source-rich.
2. For `enrich_from_existing_raw_sources`, use already collected raw/source text first.
3. For `replace_placeholder_or_absorb_wrapper`, decide whether the page is a real case/operation or a wrapper that should point to a canonical record.
4. For `manual_crime_type_review`, do not change taxonomy without source-backed review.
