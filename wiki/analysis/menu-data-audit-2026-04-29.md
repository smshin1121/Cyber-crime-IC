---
title: Menu Data Audit (2026-04-29)
type: analysis
created: 2026-04-29
updated: 2026-04-29
summary: "Repository-wide audit of data quality for top navigation and supporting wiki menu categories."
source_count: 0
---
## Summary

This audit checks each menu category for structural stubs, placeholder prose, thin records, source/reference count mismatches, and missing core metadata. It complements the operation/case depth audit, organization audit, source corpus audit, link checker, and integrity audit.

- Pages audited: **7416**
- High priority (`score >= 50`): **0**
- Medium priority (`25-49`): **0**

## Menu Summary

| Menu | Pages | High | Medium | Top issue count |
|---|---:|---:|---:|---:|
| operations | 1085 | 0 | 0 | 3 |
| organizations | 143 | 0 | 0 | 166 |
| countries | 110 | 0 | 0 | 70 |
| cases | 1202 | 0 | 0 | 905 |
| legal-frameworks | 22 | 0 | 0 | 4 |
| mechanisms | 27 | 0 | 0 | 14 |
| crime-types | 24 | 0 | 0 | 13 |
| concepts | 15 | 0 | 0 | 18 |
| procedures | 2 | 0 | 0 | 2 |
| challenges | 2 | 0 | 0 | 2 |
| sources | 4784 | 0 | 0 | 18 |

## Issue Counts

| Issue | Count |
|---|---:|
| thin_body | 904 |
| missing_metadata | 154 |
| no_sources | 51 |
| very_thin_body | 41 |
| menu_core_page_underbuilt | 36 |
| source_count_missing_refs | 19 |
| placeholder_language | 7 |
| source_count_mismatch | 3 |

## Top 120 Queue

| Rank | Page | Menu | Score | Sources | Refs | Body words | Issues |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | [[dual-criminality]] | concepts | 22 | 2 | 2 | 115 | thin_body:115, menu_core_page_underbuilt:115 |
| 2 | [[nationality-principle]] | concepts | 22 | 2 | 2 | 108 | thin_body:108, menu_core_page_underbuilt:108 |
| 3 | [[ne-bis-in-idem]] | concepts | 22 | 2 | 2 | 108 | thin_body:108, menu_core_page_underbuilt:108 |
| 4 | [[specialty-principle]] | concepts | 22 | 2 | 2 | 114 | thin_body:114, menu_core_page_underbuilt:114 |
| 5 | [[territoriality-principle]] | concepts | 22 | 2 | 2 | 116 | thin_body:116, menu_core_page_underbuilt:116 |
| 6 | [[csam-ic]] | crime-types | 22 | 3 | 3 | 117 | thin_body:117, menu_core_page_underbuilt:117 |
| 7 | [[cloud-act]] | legal-frameworks | 22 | 2 | 2 | 123 | thin_body:123, menu_core_page_underbuilt:123 |
| 8 | [[second-additional-protocol]] | legal-frameworks | 22 | 2 | 2 | 112 | thin_body:112, menu_core_page_underbuilt:112 |
| 9 | [[24-7-network]] | mechanisms | 22 | 2 | 2 | 138 | thin_body:138, menu_core_page_underbuilt:138 |
| 10 | [[europol-jit]] | mechanisms | 22 | 2 | 2 | 122 | thin_body:122, menu_core_page_underbuilt:122 |
| 11 | [[interpol-i-grip]] | mechanisms | 22 | 2 | 2 | 132 | thin_body:132, menu_core_page_underbuilt:132 |
| 12 | [[mlat-process]] | mechanisms | 22 | 2 | 2 | 133 | thin_body:133, menu_core_page_underbuilt:133 |
| 13 | [[ross-ulbricht-found-guilty-on-all-counts]] | cases | 20 | 1 | 1 | 530 | placeholder_language:1 |
| 14 | [[ross-ulbricht-sentenced-to-life-in-federal-prison]] | cases | 20 | 1 | 1 | 480 | placeholder_language:1 |
| 15 | [[ross-ulbricht-sentenced-to-life-in-prison]] | cases | 20 | 1 | 1 | 466 | placeholder_language:1 |
| 16 | [[us-v-adafin-xdedic]] | cases | 20 | 1 | 1 | 49 | very_thin_body:49 |
| 17 | [[us-v-adejumo-jinadu-xdedic]] | cases | 20 | 1 | 1 | 423 | placeholder_language:1 |
| 18 | [[us-v-almashwali-alphabay]] | cases | 20 | 1 | 1 | 21 | very_thin_body:21 |
| 19 | [[us-v-aragon-dark-web]] | cases | 20 | 1 | 1 | 17 | very_thin_body:17 |
| 20 | [[us-v-barraza-flores-dark-web]] | cases | 20 | 1 | 1 | 30 | very_thin_body:30 |
| 21 | [[us-v-bookman-dark-web]] | cases | 20 | 1 | 1 | 25 | very_thin_body:25 |
| 22 | [[us-v-brewer-dark-web]] | cases | 20 | 1 | 1 | 30 | very_thin_body:30 |
| 23 | [[us-v-brian-mcdonald-dark-web]] | cases | 20 | 1 | 1 | 24 | very_thin_body:24 |
| 24 | [[us-v-castro-dark-web]] | cases | 20 | 1 | 1 | 29 | very_thin_body:29 |
| 25 | [[us-v-curry-brooke-dark-web]] | cases | 20 | 1 | 1 | 24 | very_thin_body:24 |
| 26 | [[us-v-dittman-schiffner-langer-dark-web]] | cases | 20 | 1 | 1 | 26 | very_thin_body:26 |
| 27 | [[us-v-evan-hernandez-dark-web]] | cases | 20 | 1 | 1 | 21 | very_thin_body:21 |
| 28 | [[us-v-fatukala-cocaine-dark-web]] | cases | 20 | 1 | 1 | 22 | very_thin_body:22 |
| 29 | [[us-v-gary-davis-silk-road]] | cases | 20 | 1 | 1 | 35 | very_thin_body:35 |
| 30 | [[us-v-gutierrez-villasenor-dark-web]] | cases | 20 | 1 | 1 | 16 | very_thin_body:16 |
| 31 | [[us-v-haney-silk-road]] | cases | 20 | 1 | 1 | 22 | very_thin_body:22 |
| 32 | [[us-v-hernandez-dark-web]] | cases | 20 | 1 | 1 | 20 | very_thin_body:20 |
| 33 | [[us-v-herrell-alphabay]] | cases | 20 | 1 | 1 | 19 | very_thin_body:19 |
| 34 | [[us-v-holly-adams-dark-web]] | cases | 20 | 1 | 1 | 36 | very_thin_body:36 |
| 35 | [[us-v-john-cruz-dark-web]] | cases | 20 | 1 | 1 | 19 | very_thin_body:19 |
| 36 | [[us-v-john-mckernan-dark-web]] | cases | 20 | 1 | 1 | 24 | very_thin_body:24 |
| 37 | [[us-v-kancharla-dark-web]] | cases | 20 | 1 | 1 | 20 | very_thin_body:20 |
| 38 | [[us-v-lint-dream-market]] | cases | 20 | 1 | 1 | 23 | very_thin_body:23 |
| 39 | [[us-v-madding-dark-web]] | cases | 20 | 1 | 1 | 24 | very_thin_body:24 |
| 40 | [[us-v-nicholas-partlow-dark-web]] | cases | 20 | 1 | 1 | 16 | very_thin_body:16 |
| 41 | [[us-v-ogando-dawodu-spencer-dark-web]] | cases | 20 | 1 | 1 | 29 | very_thin_body:29 |
| 42 | [[us-v-ogunlana-xdedic]] | cases | 20 | 1 | 1 | 44 | very_thin_body:44 |
| 43 | [[us-v-okparaeke-dark-web]] | cases | 20 | 1 | 1 | 24 | very_thin_body:24 |
| 44 | [[us-v-orgil-dark-web]] | cases | 20 | 1 | 1 | 23 | very_thin_body:23 |
| 45 | [[us-v-oyebanjo-xdedic]] | cases | 20 | 1 | 1 | 40 | very_thin_body:40 |
| 46 | [[us-v-peck-dark-web]] | cases | 20 | 1 | 1 | 31 | very_thin_body:31 |
| 47 | [[us-v-roberts-dark-web]] | cases | 20 | 1 | 1 | 20 | very_thin_body:20 |
| 48 | [[us-v-sabbagh-dark-web]] | cases | 20 | 1 | 1 | 16 | very_thin_body:16 |
| 49 | [[us-v-scanlan-dark-web]] | cases | 20 | 1 | 1 | 31 | very_thin_body:31 |
| 50 | [[us-v-shaughnessy-dark-web]] | cases | 20 | 1 | 1 | 19 | very_thin_body:19 |
| 51 | [[us-v-sirotkin-deaver-dark-web]] | cases | 20 | 1 | 1 | 22 | very_thin_body:22 |
| 52 | [[us-v-tan-dark-web]] | cases | 20 | 1 | 1 | 22 | very_thin_body:22 |
| 53 | [[us-v-taylor-fischer-dark-web]] | cases | 20 | 1 | 1 | 23 | very_thin_body:23 |
| 54 | [[us-v-taylor-xdedic]] | cases | 20 | 1 | 1 | 40 | very_thin_body:40 |
| 55 | [[us-v-udvardi-dark-web]] | cases | 20 | 1 | 1 | 21 | very_thin_body:21 |
| 56 | [[us-v-vlastos-dark-web]] | cases | 20 | 1 | 1 | 25 | very_thin_body:25 |
| 57 | [[us-v-witters-dark-web]] | cases | 20 | 1 | 1 | 26 | very_thin_body:26 |
| 58 | [[bulletproof-hosting]] | concepts | 20 | 4 | 4 | 243 | placeholder_language:1 |
| 59 | [[algeria]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 60 | [[angola]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 61 | [[argentina]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 62 | [[australia]] | countries | 20 | 0 | 0 | 770 | no_sources |
| 63 | [[azerbaijan]] | countries | 20 | 0 | 0 | 173 | no_sources |
| 64 | [[belarus]] | countries | 20 | 0 | 0 | 173 | no_sources |
| 65 | [[belize]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 66 | [[bolivia]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 67 | [[bosnia-and-herzegovina]] | countries | 20 | 0 | 0 | 173 | no_sources |
| 68 | [[brunei]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 69 | [[cambodia]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 70 | [[chile]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 71 | [[china]] | countries | 20 | 0 | 0 | 1009 | no_sources |
| 72 | [[costa-rica]] | countries | 20 | 0 | 0 | 174 | no_sources |
| 73 | [[croatia]] | countries | 20 | 0 | 0 | 173 | no_sources |
| 74 | [[czechia]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 75 | [[democratic-republic-of-the-congo]] | countries | 20 | 0 | 0 | 175 | no_sources |
| 76 | [[ecuador]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 77 | [[gabon]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 78 | [[ghana]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 79 | [[guyana]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 80 | [[iceland]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 81 | [[ireland]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 82 | [[japan]] | countries | 20 | 0 | 0 | 900 | no_sources |
| 83 | [[kazakhstan]] | countries | 20 | 0 | 0 | 173 | no_sources |
| 84 | [[laos]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 85 | [[lithuania]] | countries | 20 | 0 | 0 | 173 | no_sources |
| 86 | [[luxembourg]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 87 | [[macau]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 88 | [[macedonia]] | countries | 20 | 0 | 0 | 172 | no_sources |
| 89 | [[madagascar]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 90 | [[mexico]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 91 | [[mongolia]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 92 | [[montenegro]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 93 | [[mozambique]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 94 | [[namibia]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 95 | [[new-zealand]] | countries | 20 | 0 | 0 | 172 | no_sources |
| 96 | [[nigeria]] | countries | 20 | 0 | 0 | 855 | no_sources |
| 97 | [[pakistan]] | countries | 20 | 0 | 0 | 174 | no_sources |
| 98 | [[paraguay]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 99 | [[peru]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 100 | [[philippines]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 101 | [[senegal]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 102 | [[slovenia]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 103 | [[suriname]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 104 | [[tunisia]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 105 | [[turkey]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 106 | [[united-arab-emirates]] | countries | 20 | 0 | 0 | 173 | no_sources |
| 107 | [[uruguay]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 108 | [[venezuela]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 109 | [[zimbabwe]] | countries | 20 | 0 | 0 | 171 | no_sources |
| 110 | [[operation-us-v-adejumo-jinadu-xdedic]] | operations | 20 | 1 | 1 | 117 | placeholder_language:1 |
| 111 | [[operation-us-v-kevin-james-strutz]] | operations | 20 | 1 | 1 | 113 | placeholder_language:1 |
| 112 | [[portugal-police]] | organizations | 18 | 0 | 3 | 294 | source_count_missing_refs:3, missing_metadata:jurisdiction |
| 113 | [[romania-diicot]] | organizations | 18 | 0 | 4 | 320 | source_count_missing_refs:4, missing_metadata:jurisdiction |
| 114 | [[romania-police]] | organizations | 18 | 0 | 4 | 274 | source_count_missing_refs:4, missing_metadata:jurisdiction |
| 115 | [[apcert]] | organizations | 16 | 2 | 2 | 136 | thin_body:136, missing_metadata:jurisdiction |
| 116 | [[bulgaria-ministry-of-interior]] | organizations | 16 | 2 | 2 | 126 | thin_body:126, missing_metadata:jurisdiction |
| 117 | [[denmark-national-police]] | organizations | 16 | 2 | 2 | 122 | thin_body:122, missing_metadata:jurisdiction |
| 118 | [[dod-inspector-general]] | organizations | 16 | 2 | 2 | 109 | thin_body:109, missing_metadata:jurisdiction |
| 119 | [[dutch-nhtcu]] | organizations | 16 | 3 | 3 | 96 | thin_body:96, missing_metadata:jurisdiction |
| 120 | [[first-forum-incident-response]] | organizations | 16 | 2 | 2 | 132 | thin_body:132, missing_metadata:jurisdiction |

## Remediation Rules

1. Treat top-navigation categories before supporting-only categories when scores tie.
2. Replace structural stubs with source-backed summaries before adding new pages.
3. Do not infer legal status, treaty participation, or agency authority without a cited source.
4. Keep absorbed operation wrappers lightweight unless they need to carry unique evidence or procedural context.
