---
title: Source URL/Content Alignment Audit (2026-05-03)
type: analysis
created: 2026-05-03
updated: 2026-05-03
summary: "Corpus-wide audit comparing source-page metadata against linked raw URL metadata and fetched titles."
source_count: 0
---
## Summary

This audit compares every `wiki/sources` page with its linked `raw_path`. It is designed to catch cases where a source page or downstream operation cites one URL while its title/summary describes a different article.

- Source pages audited: **4784**
- Confirmed/high-confidence mismatches: **0**
- Review candidates: **40**
- CSV detail: `_workspace/source_url_content_alignment_2026-05-03.csv`

## Severity Counts

| Severity | Count |
|---|---:|
| ok | 4744 |
| review | 40 |

## Issue Counts

| Issue | Count |
|---|---:|
| ok | 4744 |
| source_raw_title_mismatch | 13 |
| generic_raw_title | 11 |
| source_raw_url_mismatch_raw_generic | 8 |
| source_raw_title_low_overlap | 4 |
| source_raw_url_drift | 3 |
| url_slug_title_low_overlap | 1 |

## Confirmed And High-Confidence Mismatches

| # | Source | Issue | Source title | Raw title | Evidence |
|---:|---|---|---|---|---|

## Review Candidates

| # | Source | Issue | Score | Source title | Raw title | URL |
|---:|---|---|---:|---|---|---|
| 1 | [[2016-11-28_pgdlisboa-pt_decree-law-no-81-2016]] | url_slug_title_low_overlap | 1.00 | Decree-Law No. 81/2016 | Decree-Law No. 81/2016 | https://pgdlisboa.pt/leis/lei_print_articulado.php?nid=2608&tabela=leis |
| 2 | [[2018-12-03_justia_united-states-v-allen-lint-case-docket-reference]] | source_raw_title_mismatch | 0.00 | United States v. Allen Lint case docket reference | ‘Darknet’ Drug Dealer Sentenced to Five Years in Prison | https://www.justice.gov/usao-wdwa/pr/darknet-drug-dealer-sentenced-five-years-prison |
| 3 | [[2021-07-06_darkreading-com_operation-lyrebird-morocco-arrest]] | source_raw_title_mismatch | 0.00 | INTERPOL operation leads to Morocco arrest in phishing and carding case | URL Source: https://www.darkreading.com/cyberattacks-data-breaches/interpol-operation-lyrebird-morocco-arrest | https://www.darkreading.com/cyberattacks-data-breaches/interpol-operation-lyrebird-morocco-arrest |
| 4 | [[2021-07_portswigger-net_operation-lyrebird-cybercops-nab-moroccan-phish-and-carding-kingpin]] | generic_raw_title | 0.00 | Operation Lyrebird: Cybercops nab Moroccan phish-and-carding kingpin | Web Application Security, Testing, & Scanning - PortSwigger | https://portswigger.net/daily-swig/operation-lyrebird-cybercops-nab-moroccan-phish-and-carding-kingpin |
| 5 | [[2022-05-26_washingtonpost_com_fentanyl-dealer-pleads-guilty-in-virginia-after-online-drug-bust]] | source_raw_title_low_overlap | 0.25 | Fentanyl dealer pleads guilty in Virginia after online drug bust | Akshay Ram Kancharla, 26, of Tampa, pleaded guilty Thursday to one count of distributing fentanyl | https://www.washingtonpost.com/dc-md-va/2022/05/26/virginia-fentanyl-plea/ |
| 6 | [[2024-05-22_justice-gov_page-not-found]] | generic_raw_title | 0.00 | 911 S5 Botnet Dismantled and Its Administrator Arrested in Coordinated International Operation | Page not found | https://www.justice.gov/archives/opa/pr/justice-department-leads-effort-among-multinational-partners-dismantle-worlds-largest-botnet |
| 7 | [[2024-05-22_justice-gov_united-states-v-yunhe-wang-911-s5-botnet]] | generic_raw_title | 0.00 | 911 S5 Botnet Dismantled and Its Administrator Arrested in Coordinated International Operation | Page not found | https://www.justice.gov/archives/opa/pr/justice-department-leads-effort-among-multinational-partners-dismantle-worlds-largest-botnet |
| 8 | [[2024-05-29_opa_yunhe-wang-911-s5-indictment]] | generic_raw_title | 0.00 | 911 S5 Botnet Dismantled and Its Administrator Arrested in Coordinated International Operation | Page not found | https://www.justice.gov/archives/opa/pr/justice-department-leads-effort-among-multinational-partners-dismantle-worlds-largest-botnet |
| 9 | [[2024-06-20_fincen_gov_supplemental-advisory-on-fentanyl-related-financial-activity]] | generic_raw_title | 0.00 | Supplemental Advisory on Fentanyl-Related Financial Activity | Page Not Found | https://www.fincen.gov/system/files/advisory/2024-06-20/FinCEN-Supplemental-Advisory-on-Fentanyl-Related-Financial-Activity-508C.pdf |
| 10 | [[2024-11-27_interpol-int-es_operation-haechi-v-5500-arrests]] | source_raw_title_mismatch | 0.09 | Una operación de INTERPOL contra la delincuencia financiera obtiene unos resultados récord: 5 500 detenciones | INTERPOL financial crime operation makes record 5,500 arrests, seizures worth over USD 400 million | https://www.interpol.int/es/Noticias-y-acontecimientos/Noticias/2024/Una-operacion-de-INTERPOL-contra-la-delincuencia-financiera-obtiene-unos-resultados-record-5-500-detenciones-e-incautaciones-por-valor-de-mas-de-4 |
| 11 | [[2024-11-27_interpol-int-fr_operation-haechi-v-5500-arrests]] | source_raw_title_mismatch | 0.18 | Une opération INTERPOL de lutte contre la criminalité financière aboutit à l'arrestation record de 5 500 personnes | INTERPOL financial crime operation makes record 5,500 arrests, seizures worth over USD 400 million | https://www.interpol.int/fr/Actualites-et-evenements/Actualites/2024/INTERPOL-financial-crime-operation-makes-record-5-500-arrests-seizures-worth-over-USD-400-million |
| 12 | [[2025-01-17_morelaw_re-united-states-of-america-v-anurag-pramod-murarka]] | source_raw_title_low_overlap | 0.40 | Re: United States of America v. Anurag Pramod Murarka | Re: United States of America v. Anu... \| MoreLaw Legal Cases | https://www.morelaw.com/verdicts/case.asp?d=189143&s=KY |
| 13 | [[2025-01-29_sdtx_heartsender-seizure]] | source_raw_url_mismatch_raw_generic | 0.00 | Cybercrime websites selling hacking tools to transnational organized crime groups seized | Page not found | https://www.justice.gov/usao-sdtx/pr/cybercrime-websites-selling-hacking-tools-transnational-organized-crime-groups-seized |
| 14 | [[2025-02-04-allahrakha-cross-border-e-crimes]] | source_raw_title_mismatch | 0.00 | Cross-Border E-Crimes: Jurisdiction and Due Process Challenges | ADLIYA: Jurnal Hukum dan Kemanusiaan | https://doi.org/10.15575/adliya.v18i2.38633 |
| 15 | [[2025-03-05_justice-gov_justice-department-charges-12-chinese-hackers-and-law-enforcement-officers-in-gl]] | source_raw_url_drift | 1.00 | Justice Department Charges 12 Chinese Contract Hackers and Law Enforcement Officers in Global Computer Intrusion Campaigns | Justice Department Charges 12 Chinese Hackers and Law Enforcement Officers in Global Computer Intrusion Campaigns | https://www.justice.gov/opa/pr/justice-department-charges-12-chinese-contract-hackers-and-law-enforcement-officers-global |
| 16 | [[2025-03-05_opa_wu-haibo-isoon-indictment]] | source_raw_url_mismatch_raw_generic | 0.00 | Justice Department Charges 12 Chinese Contract Hackers and Law Enforcement Officers in Global Computer Intrusion Campaigns | Page not found | https://www.justice.gov/opa/pr/justice-department-charges-12-chinese-contract-hackers-and-law-enforcement-officers-global |
| 17 | [[2025-04-01_helpnetsecurity-com_operation-secure-disrupts-global-infostealer-malware-operations]] | source_raw_title_mismatch | 0.00 | Operation Secure disrupts global infostealer malware operations | Page not found - Help Net Security | https://www.helpnetsecurity.com/2025/04/01/operation-secure-interpol-infostealer/ |
| 18 | [[2025-04-17_opa_parsarad-nemesis-indictment]] | source_raw_url_mismatch_raw_generic | 0.00 | Iranian National Indicted for Operating Online Marketplace Offering Fentanyl and Money Laundering Services | Page not found | https://www.justice.gov/opa/pr/iranian-national-indicted-operating-online-marketplace-offering-fentanyl-and-money |
| 19 | [[2025-05-09_morelaw_united-states-of-america-v-santana-sandoval-kevin-torres-velasquez]] | source_raw_title_low_overlap | 0.33 | United States of America v. Santana Sandoval, Kevin Torres Velasquez | Re: United States of America v. San... \| MoreLaw Legal Cases | https://www.morelaw.com/verdicts/case.asp?d=192858&n=25-MJ-59&s=WA |
| 20 | [[2025-05-22_justice-gov_qakbot-gallyamov-indictment]] | source_raw_url_mismatch_raw_generic | 0.00 | Leader of Qakbot Malware Conspiracy Indicted for Involvement in Global Ransomware Scheme | Page not found | https://www.justice.gov/opa/pr/leader-qakbot-malware-conspiracy-indicted-involvement-global-ransomware-scheme |
| 21 | [[2025-06-24_hoodline_sacramento-duo-confess-fentanyl-distribution-conspiracy-dark-web-drug-ring]] | source_raw_url_drift | 1.00 | Sacramento Duo Confess to Fentanyl Distribution Conspiracy, Await Sentencing After Dark Web Drug Ring Bust | Sacramento Duo Confess to Fentanyl Distribution Conspiracy, Await Sentencing After Dark Web Drug Ring Bust | https://hoodline.com/2025/06/sacramento-duo-confess-fentanyl-distribution-conspiracy-await-sentencing-after-dark-web-drug-ring-bust/ |
| 22 | [[2025-06-25_eurojust-europa-eu_trusted-seller-accounts-fraud-germany-romania]] | generic_raw_title | 0.00 | Eurojust helps uncover large-scale fraud based on trusted online seller accounts | Page not found | https://www.eurojust.europa.eu/news/eurojust-helps-uncover-large-scale-fraud-based-trusted-online-seller-accounts |
| 23 | [[2025-06-26_ieu-monitoring-com_eurojust-helps-uncover-large-scale-fraud-based-on-trusted-online-seller-accounts]] | source_raw_title_mismatch | 0.00 | Eurojust helps dismantle fraud scheme using hijacked trusted seller accounts | Insight EU Monitoring | https://ieu-monitoring.com/editorial/eurojust-helps-uncover-large-scale-fraud-based-on-trusted-online-seller-accounts/834094/ |
| 24 | [[2025-06-27_immuniweb-com_cybercrime-investigations-weekly-trusted-seller-fraud]] | source_raw_title_mismatch | 0.00 | Cybercrime Investigations Weekly - trusted seller account fraud | Four BreachForums Operators Arrested in France | https://www.immuniweb.com/blog/four-breachforums-operators-arrested-in-france.html |
| 25 | [[2025-09-23_decripto-org_eurojust-dismantles-eur-100-million-crypto-scam-five-arrests-and-seizures]] | source_raw_title_mismatch | 0.00 | Eurojust dismantles EUR 100 million crypto scam: five arrests and seizures | Pagina non trovata - Decripto.org | https://decripto.org/en/eurojust-dismantles-eur-100-million-crypto-scam-five-arrests-and-seizures/ |
| 26 | [[2026-02-12_fbi-gov_member-of-lummi-nation-indicted-for-distributing-fentanyl]] | source_raw_title_mismatch | 0.00 | Member of Lummi Nation Indicted for Distributing Fentanyl | Indian Country News | https://www.fbi.gov/investigate/violent-crime/indian-country-crime/indian-country-news |
| 27 | [[2026-03-13_cybernews-com_major-residential-proxy-service-socksescort-down]] | source_raw_title_low_overlap | 0.27 | Authorities shut down cybercrime service that sold access to 369,000 home internet connections | Authorities disrupt major cybercrime proxy service: malware infected thousands of America’s WiFi routers | https://cybernews.com/security/major-residential-proxy-service-socksescort-down/ |
| 28 | [[2026-03-18_wsfa_maryland-alabama-men-sentenced-federal-csam-charges]] | source_raw_url_drift | 1.00 | Maryland, Alabama men sentenced on federal child sexual abuse material charges | Maryland, Alabama men sentenced on federal child sexual abuse material charges | https://www.wsfa.com/2026/03/18/maryland-alabama-men-sentenced-federal-csam-charges/ |
| 29 | [[2026-04-17_justice-gov_administrator-of-nemesis-market-charged-for-role-operating-darknet-marketplace]] | source_raw_url_mismatch_raw_generic | 0.00 | Iranian National Indicted for Operating Online Marketplace Offering Fentanyl and Money Laundering Services | Page not found | https://www.justice.gov/opa/pr/iranian-national-indicted-operating-online-marketplace-offering-fentanyl-and-money |
| 30 | [[2026-04-17_justice-gov_documents-and-resources-related-disruption-emotet-malware-and-botnet]] | generic_raw_title | 0.00 | Emotet Botnet Disrupted in International Cyber Operation | Page not found | https://www.justice.gov/opa/documents-and-resources-related-disruption-emotet-malware-and-botnet |
| 31 | [[2026-04-17_justice-gov_international-operation-takes-down-cybercrime-ring-selling-hacking-tools]] | source_raw_url_mismatch_raw_generic | 0.00 | Cybercrime websites selling hacking tools to transnational organized crime groups seized | Page not found | https://www.justice.gov/usao-sdtx/pr/cybercrime-websites-selling-hacking-tools-transnational-organized-crime-groups-seized |
| 32 | [[2026-04-17_justice-gov_justice-department-charges-12-chinese-hackers-and-law-enforcement-officers-in-gl]] | source_raw_url_mismatch_raw_generic | 0.00 | Justice Department Charges 12 Chinese Contract Hackers and Law Enforcement Officers in Global Computer Intrusion Campaigns | Page not found | https://www.justice.gov/opa/pr/justice-department-charges-12-chinese-contract-hackers-and-law-enforcement-officers-global |
| 33 | [[2026-04-17_justice-gov_page-not-found]] | source_raw_url_mismatch_raw_generic | 0.00 | Cybercrime websites selling hacking tools to transnational organized crime groups seized | Page not found | https://www.justice.gov/usao-sdtx/pr/cybercrime-websites-selling-hacking-tools-transnational-organized-crime-groups-seized |
| 34 | [[2026-04-17_justice-gov_ukrainian-national-sentenced-to-10-years-in-prison-for-role-in-fin7-malware-sche]] | generic_raw_title | 0.00 | High-level organizer of notorious hacking group FIN7 sentenced to ten years in prison | Page not found | https://www.justice.gov/usao-wdwa/pr/ukrainian-national-sentenced-10-years-prison-role-fin7-malware-scheme |
| 35 | [[bbc-911-s5-botnet-dismantling-1]] | generic_raw_title | 0.00 | 911 S5 Botnet Dismantled and Its Administrator Arrested in Coordinated International Operation | Page not found | https://www.justice.gov/archives/opa/pr/justice-department-leads-effort-among-multinational-partners-dismantle-worlds-largest-botnet |
| 36 | [[bbc-911-s5-botnet-dismantling]] | source_raw_title_mismatch | 0.00 | BBC: 911 S5 Botnet Dismantling | Europol kills off shape-shifting 'Mystique' malware | https://www.bbc.com/news/technology-32218381 |
| 37 | [[bbc-operation-avalanche]] | source_raw_title_mismatch | 0.00 | BBC: Operation Avalanche | UK man arrested in connection with Sony and Xbox hack | https://www.bbc.com/news/technology-30849172 |
| 38 | [[polish-radio-911-s5-botnet-dismantling]] | source_raw_title_mismatch | 0.00 | Polish Radio: 911 S5 Botnet Dismantling | Poland plays key role in European operation against child exploitation network | https://www.polskieradio.pl/395/7789/artykul/3508265,poland-plays-key-role-in-european-operation-against-child-exploitation-network |
| 39 | [[portswigger-911-s5-botnet-dismantling]] | generic_raw_title | 0.00 | PortSwigger Daily Swig: Andromeda Botnet Dismantled by International Taskforce | Web Application Security, Testing, & Scanning - PortSwigger | https://portswigger.net/daily-swig/andromeda-botnet-dismantled-by-international-taskforce |
| 40 | [[portswigger-operation-avalanche]] | generic_raw_title | 0.00 | PortSwigger Daily Swig: The Avalanche falls — Alleged leader of international cybercrime network arrested | Web Application Security, Testing, & Scanning - PortSwigger | https://portswigger.net/daily-swig/the-avalanche-falls-alleged-leader-of-international-cybercrime-network-arrested |
