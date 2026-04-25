from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
SOURCES_DIR = ROOT / "wiki" / "sources"
TODAY = "2026-04-25"

CURATED: dict[str, dict[str, Any]] = {
    "operation-members-of-seattle-drug-trafficking-organization-indicted-for-distribution-of-heroin": {
        "sources": [
            "2016-08-11_justice-gov_members-of-seattle-drug-trafficking-organization-indicted-for-distribution-of-he",
            "2016-08-11_fox13seattle_feds-seattle-heroin-traffickers-indicted-one-arrested-near-tijuana",
            "2016-08-11_spokesman_authorities-seattle-heroin-traffickers-indicted",
            "2014-04-25_bellevuereporter_eastside-narcotics-task-force-investigating-drug-running-money-laundering-case",
            "2016-08-12_newstalkkit_authorities-say-leader-of-heroin-traffickers-is-in-custody-awaiting-charges",
        ],
    },
    "operation-resident-of-tacoma-hotel-indicted-for-drug-and-gun-crimes": {
        "sources": [
            "2023-08-02_justice-gov_resident-of-tacoma-hotel-indicted-for-drug-and-gun-crimes",
            "2023-08-03_foxnews_washington-state-man-found-in-hotel-room-with-95-pounds-of-drugs-firearms-police",
            "2023-02-03_fox13seattle_deputies-arrest-drug-dealer-seize-100-pounds-of-drugs-stored-in-tacoma-hotel-rooms",
            "2023-07-27_midpage_united-states-v-contreras-arias",
            "2023-08-02_justice-gov_contreras-arias-indictment-pdf",
        ],
    },
    "operation-renton-washington-man-who-worked-with-his-son-to-deal-drugs-and-launder-proceeds-sentenced-to-5-years-in-priso": {
        "sources": [
            "2025-01-16_justice-gov_renton-washington-man-who-worked-with-his-son-to-deal-drugs-and-launder-proceeds",
            "2025-01-16_ocdetf_renton-washington-man-who-worked-with-his-son-to-deal-drugs-and-launder-proceeds-sentenced-to-5-years-in-prison",
            "2025-01-17_fox13seattle_renton-man-sentenced-family-drug-ring",
            "2025-01-22_rentonreporter_renton-man-sentenced-to-five-years-for-drug-dealing",
            "2025-01-16_federalnewswire_renton-man-sentenced-for-drug-trafficking-forfeits-assets",
        ],
    },
    "operation-seven-indicted-in-seattle-in-connection-with-coast-to-coast-drug-trafficking-conspiracy": {
        "sources": [
            "2023-03-03_justice-gov_seven-indicted-in-seattle-in-connection-with-coast-to-coast-drug-trafficking-con",
            "2023-03-03_dea-gov_seven-indicted-seattle-connection-coast-coast-drug-trafficking-conspiracy",
            "2024-01-08_justice-gov_thirty-five-individuals-charged-second-superseding-indictment-participating-violent",
            "2025-09-24_justice-gov_three-convicted-roles-nationwide-drug-distribution-conspiracy",
            "2026-02-06_irs-gov_seattle-man-sentenced-to-35-years-in-prison-following-september-2025-conviction-by-jury-for-role-in-transnational-drug-trafficking-organization",
        ],
    },
    "operation-three-snohomish-county-men-indicted-for-drug-trafficking-conspiracy-involving-cocaine-fentanyl-and-firearms": {
        "sources": [
            "2025-04-08_justice-gov_three-snohomish-county-men-indicted-for-drug-trafficking-conspiracy-involving-co",
            "2025-03-14_lynnwoodtimes_percy-levy",
            "2025-03-17_fox13seattle_everett-man-granted-clemency-arrested",
            "2025-03-17_audacy_man-previously-granted-clemency-arrested-with-enough-fentanyl-to-kill-278000-people",
            "2025-03-17_kiro7_everett-community-activist-arrested-facing-11-felony-charges-following-undercover-investigation",
        ],
    },
    "operation-two-everett-residents-charged-federally-for-drug-distribution-activities-involving-multiple-kilos-of-fentanyl-": {
        "sources": [
            "2025-05-09_justice-gov_two-everett-residents-charged-federally-for-drug-distribution-activities-involvi",
            "2025-04-11_heraldnet_dea-agents-everett-man-had-enough-fentanyl-to-kill-millions",
            "2025-05-12_kiro7_honduran-nationals-arrested-everett-with-7-kilos-fentanyl-intending-distribute",
            "2025-05-13_lynnwoodtimes_two-everett-men-charged-with-distributing-enough-fentanyl-to-kill-half-of-all-wa-residents",
            "2025-05-09_morelaw_united-states-of-america-v-santana-sandoval-kevin-torres-velasquez",
        ],
    },
    "operation-online-scamming-fraud-three-nigerians-arrested-in-interpol-operation-killer-bee": {
        "sources": [
            "2022-05-30_cybersecurity-review_online-scamming-fraud-three-nigerians-arrested-in-interpol-operation-killer-bee",
            "2022-05-30_trendmicro_operation-killer-bee-agent-tesla-bec-actors",
            "2022-10-18_mha-gov-sg_interpol-global-cybercrime-conference-killer-bee",
            "2022-05-30_interpol-es_operation-killer-bee",
        ],
    },
    "operation-interpol-online-scamming-fraud-three-nigerians-arrested-in-operation-killer-bee": {
        "sources": [
            "2022-05-30_cybersecurity-review_online-scamming-fraud-three-nigerians-arrested-in-interpol-operation-killer-bee",
            "2022-05-30_trendmicro_operation-killer-bee-agent-tesla-bec-actors",
            "2022-10-18_mha-gov-sg_interpol-global-cybercrime-conference-killer-bee",
            "2022-05-30_interpol-es_operation-killer-bee",
        ],
        "title": 'INTERPOL: Online Scamming Fraud "Three Nigerians Arrested in Operation Killer Bee" Enforcement Action',
        "alias": 'INTERPOL: Online Scamming Fraud "Three Nigerians Arrested in Operation Killer Bee"',
    },
    "operation-interpol-seized-130-million-from-cybercriminals-in-global-haechi-iii-crackdown": {
        "sources": [
            "2022-11-24_interpol-int_cyber-enabled-financial-crime-usd-130-million-intercepted-in-global-interpol-pol",
            "2022-11-24_bleepingcomputer-com_interpol-seized-130-million-from-cybercriminals-worldwide",
            "2022-11-01_gbhackers-com_operation-haechi-iii-interpol-arrested-1000-cyber-criminals-seized-130-million",
            "2022-11-01_therecord-media_almost-1-000-suspects-arrested-in-interpol-operation-which-seized-over-129-milli",
        ],
    },
    "operation-interpol-seized-130-million-from-cybercriminals-worldwide": {
        "sources": [
            "2022-11-24_interpol-int_cyber-enabled-financial-crime-usd-130-million-intercepted-in-global-interpol-pol",
            "2022-11-01_gbhackers-com_operation-haechi-iii-interpol-arrested-1000-cyber-criminals-seized-130-million",
            "2022-11-24_thehackernews-com_interpol-seized-130-million-from-cybercriminals-in-global-haechi-iii-crackdown",
            "2022-11-01_therecord-media_almost-1-000-suspects-arrested-in-interpol-operation-which-seized-over-129-milli",
        ],
    },
    "operation-interpol-seized-130-million-from": {
        "sources": [
            "2022-11-24_interpol-int_cyber-enabled-financial-crime-usd-130-million-intercepted-in-global-interpol-pol",
            "2022-11-24_bleepingcomputer-com_interpol-seized-130-million-from-cybercriminals-worldwide",
            "2022-11-01_gbhackers-com_operation-haechi-iii-interpol-arrested-1000-cyber-criminals-seized-130-million",
            "2022-11-01_therecord-media_almost-1-000-suspects-arrested-in-interpol-operation-which-seized-over-129-milli",
        ],
        "title": "Interpol Seized $130 Million From Cybercriminals Enforcement Action",
        "alias": "Interpol Seized $130 Million From Cybercriminals",
    },
    "operation-operation-haechi-iii-interpol-arrested-1000-cyber-criminals-seized-130-million": {
        "sources": [
            "2022-11-24_interpol-int_cyber-enabled-financial-crime-usd-130-million-intercepted-in-global-interpol-pol",
            "2022-11-24_bleepingcomputer-com_interpol-seized-130-million-from-cybercriminals-worldwide",
            "2022-11-24_thehackernews-com_interpol-seized-130-million-from-cybercriminals-in-global-haechi-iii-crackdown",
            "2022-11-01_therecord-media_almost-1-000-suspects-arrested-in-interpol-operation-which-seized-over-129-milli",
        ],
    },
    "operation-almost-1-000-suspects-arrested-in-interpol-operation-which-seized-over-129-million": {
        "sources": [
            "2022-11-24_interpol-int_cyber-enabled-financial-crime-usd-130-million-intercepted-in-global-interpol-pol",
            "2022-11-24_bleepingcomputer-com_interpol-seized-130-million-from-cybercriminals-worldwide",
            "2022-11-01_gbhackers-com_operation-haechi-iii-interpol-arrested-1000-cyber-criminals-seized-130-million",
            "2022-11-24_thehackernews-com_interpol-seized-130-million-from-cybercriminals-in-global-haechi-iii-crackdown",
        ],
    },
    "operation-hook-line-and-sinker-cybercrime-network-phishing-bank-credentials-arrested-in-romania": {
        "sources": [
            "2020-09-29_ilmetropolitano-it_hook-line-and-sinker-cybercrime-network-phishing-bank-credentials-arrested-in-romania",
            "2020-09-29_eurojust-europa-eu_successful-takedown-in-romania-of-an-ocg-carrying-out-elaborated-cybercrime-and-bank-frauds",
            "2020-10-13_incibe-es_operacion-internacional-contra-un-grupo-de-ciberdelincuentes",
            "2020-10-13_incibe-es_en_international-operation-against-group-cybercriminals",
        ],
    },
    "operation-ghost-cybercrime-platform-dismantled-in-global-operation-51-arrested": {
        "sources": [
            "2024-09-18_theregister-com_51-arrests-made-in-global-takedown-of-ghost-crime-platform",
            "2024-10-03_ia-acs-org-au_9m-in-crypto-seized-from-accused-ghost-app-creator",
            "2024-09-18_eurojust-europa-eu_51-arrests-wide-scale-operation-take-down-encrypted-communication-platform-used-organised-crime-groups",
            "2024-09-19_euronews_europol-arrests-51-people-and-dismantles-encrypted-communication-platform",
        ],
    },
    "operation-operator-of-silk-road-2-0-website-charged-in-manhattan-federal-court": {
        "sources": [
            "2014-11-06_fbi-gov_operator-of-silk-road-2-0-website-charged-in-manhattan-federal-court",
            "2014-11-06_ice-gov_international-probe-leads-to-the-arrest-of-the-alleged-operator-of-silk-road-2-0",
            "2015-01-01_europol-europa-eu_iocta-2015-darknets",
            "2015-01-01_swansea-ac-uk_gdpo-situation-analysis-operation-onymous",
        ],
        "title": 'Operator Of "Silk Road 2.0" Website Charged In Manhattan Federal Court Enforcement Action',
        "alias": 'Operator Of "Silk Road 2.0" Website Charged In Manhattan Federal Court',
    },
    "operation-usd-300-million-seized-and-3-500-suspects-arrested-in-international-financial-crime-operation-operation-haechi": {
        "sources": [
            "2023-12-19_interpol-es_usd-300-million-seized-and-3-500-suspects-arrested-operation-haechi-iv",
            "2023-12-21_mynavi-techplus_interpol-operation-haechi-iv",
            "2023-12-20_pcgamer_interpol-seizes-usd300m-from-global-cybercriminals-and-says-ai-voice-cloning-is-creating-a-whole-new-class-of-victim",
            "2023-12-20_techradar_interpol-operation-results-in-arrest-of-3500-criminals-and-seizure-of-300-million",
        ],
    },
    "operation-usd-300-million-seized-and-3-500-suspects-arrested-in-international-financial-crime-operation-operation-haechi-2": {
        "sources": [
            "2023-12-19_interpol-es_usd-300-million-seized-and-3-500-suspects-arrested-operation-haechi-iv",
            "2023-12-21_mynavi-techplus_interpol-operation-haechi-iv",
            "2023-12-20_pcgamer_interpol-seizes-usd300m-from-global-cybercriminals-and-says-ai-voice-cloning-is-creating-a-whole-new-class-of-victim",
            "2023-12-20_techradar_interpol-operation-results-in-arrest-of-3500-criminals-and-seizure-of-300-million",
        ],
        "title": "USD 300 million seized and 3,500 suspects arrested in international financial crime operation - Operation HAECHI IV Enforcement Action",
        "alias": "USD 300 million seized and 3,500 suspects arrested in international financial crime operation - Operation HAECHI IV",
    },
    "operation-usd-300-million-seized-and-3-500-suspects-arrested-in-international-financial-crime-operation-operation-haechi-3": {
        "sources": [
            "2023-12-19_interpol-es_usd-300-million-seized-and-3-500-suspects-arrested-operation-haechi-iv",
            "2023-12-21_mynavi-techplus_interpol-operation-haechi-iv",
            "2023-12-20_pcgamer_interpol-seizes-usd300m-from-global-cybercriminals-and-says-ai-voice-cloning-is-creating-a-whole-new-class-of-victim",
            "2023-12-20_techradar_interpol-operation-results-in-arrest-of-3500-criminals-and-seizure-of-300-million",
        ],
    },
    "operation-usd-300-million-seized-and-3-500-suspects-arrested-operation-haechi-iv": {
        "sources": [
            "2023-12-19_interpol-es_usd-300-million-seized-and-3-500-suspects-arrested-operation-haechi-iv",
            "2023-12-21_mynavi-techplus_interpol-operation-haechi-iv",
            "2023-12-20_pcgamer_interpol-seizes-usd300m-from-global-cybercriminals-and-says-ai-voice-cloning-is-creating-a-whole-new-class-of-victim",
            "2023-12-20_techradar_interpol-operation-results-in-arrest-of-3500-criminals-and-seizure-of-300-million",
        ],
        "title": "USD 300 million seized and 3,500 suspects arrested - Operation HAECHI IV Enforcement Action",
        "alias": "USD 300 million seized and 3,500 suspects arrested - Operation HAECHI IV",
    },
    "operation-europol-mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain-carbanak-cobalt": {
        "sources": [
            "2018-03-01_europol-europa-eu_mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain",
            "2015-02-16_securelist_the-great-bank-robbery-the-carbanak-apt",
            "2018-08-01_fbi-gov_how-cyber-crime-group-fin7-attacked-and-stole-data-from-hundreds-of-us-companies",
            "2026-04-18_europol-europa-eu_carbanak-cobalt-infographic",
        ],
    },
    "operation-three-arrested-as-interpol-group-ib-and-the-nigeria-police-force-disrupt-prol": {
        "sources": [
            "2020-11-01_cyberscoop-com_nigeria-email-scam-arrests-bec-group-ib",
            "2020-11-25_group-ib_operation-falcon-group-ib-helps-interpol-identify-nigerian-bec-ring-members",
            "2020-11-27_guardian-ng_operation-falcon-nigerian-police-join-interpol-group-ib-to-arrest-three-suspected-tmt-fraudsters",
            "2020-11-27_pmnewsnigeria-com_interpol-3-nigerians-busted-for-cyber-crime-operate-in-150-countries",
        ],
        "title": "Three Arrested as INTERPOL, Group-IB and the Nigeria Police Force Disrupt Prolific Cybercrime Group Enforcement Action",
        "alias": "Three Arrested as INTERPOL, Group-IB and the Nigeria Police Force Disrupt Prolific Cybercrime Group",
    },
    "operation-key-player-in-silk-road-2-0-sentenced-to-eight-years-in-prison": {
        "sources": [
            "2014-11-06_fbi-gov_operator-of-silk-road-2-0-website-charged-in-manhattan-federal-court",
            "2014-11-06_ice-gov_international-probe-leads-to-the-arrest-of-the-alleged-operator-of-silk-road-2-0",
            "2015-01-01_europol-europa-eu_iocta-2015-darknets",
            "2015-01-01_swansea-ac-uk_gdpo-situation-analysis-operation-onymous",
        ],
        "title": 'Key Player in "Silk Road 2.0" Sentenced to Eight Years in Prison Enforcement Action',
        "alias": 'Key Player in "Silk Road 2.0" Sentenced to Eight Years in Prison',
    },
    "operation-texas-business-executive-sentenced-to-prison-for-illegally-selling-oxycodone-on-silk-road": {
        "sources": [
            "2014-02-04_justice-gov_manhattan-u-s-attorney-announces-the-indictment-of-ross-ulbricht",
            "2015-02-04_fbi-gov_ross-ulbricht-found-guilty-on-all-counts",
            "2015-05-29_fbi-gov_ross-ulbricht-sentenced-to-life-in-prison",
            "2015-05-29_ice-gov_ross-ulbricht-sentenced-to-life-in-federal-prison",
        ],
    },
    "operation-silk-road-vendor-sentenced-to-two-years-in-prison": {
        "sources": [
            "2014-02-04_justice-gov_manhattan-u-s-attorney-announces-the-indictment-of-ross-ulbricht",
            "2015-02-04_fbi-gov_ross-ulbricht-found-guilty-on-all-counts",
            "2015-05-29_fbi-gov_ross-ulbricht-sentenced-to-life-in-prison",
            "2015-05-29_ice-gov_ross-ulbricht-sentenced-to-life-in-federal-prison",
        ],
    },
    "operation-senior-adviser-to-the-operator-of-the-silk-road-online-black-market-sentenced-to-20-years-in-prison": {
        "sources": [
            "2015-12-03_ice-gov_senior-advisor-arrested-in-thailand",
            "2014-02-04_justice-gov_manhattan-u-s-attorney-announces-the-indictment-of-ross-ulbricht",
            "2015-02-04_fbi-gov_ross-ulbricht-found-guilty-on-all-counts",
            "2015-05-29_ice-gov_ross-ulbricht-sentenced-to-life-in-federal-prison",
        ],
    },
    "operation-irish-man-who-helped-operate-the-silk-road-website-sentenced-in-manhattan-federal-court-to-over-six-years-in-p": {
        "sources": [
            "2014-02-04_justice-gov_manhattan-u-s-attorney-announces-the-indictment-of-ross-ulbricht",
            "2015-02-04_fbi-gov_ross-ulbricht-found-guilty-on-all-counts",
            "2015-05-29_fbi-gov_ross-ulbricht-sentenced-to-life-in-prison",
            "2015-05-29_ice-gov_ross-ulbricht-sentenced-to-life-in-federal-prison",
        ],
        "title": 'Irish Man Who Helped Operate The "Silk Road" Website Sentenced In Manhattan Federal Court To Over Six Years In Prison Enforcement Action',
        "alias": 'Irish Man Who Helped Operate The "Silk Road" Website Sentenced In Manhattan Federal Court To Over Six Years In Prison',
    },
    "operation-silk-road-dark-web-fraud-defendant-sentenced-following-seizure-and-forfeiture-of-over-3-4-billion-in-cryptocur": {
        "sources": [
            "2014-02-04_justice-gov_manhattan-u-s-attorney-announces-the-indictment-of-ross-ulbricht",
            "2015-02-04_fbi-gov_ross-ulbricht-found-guilty-on-all-counts",
            "2015-05-29_fbi-gov_ross-ulbricht-sentenced-to-life-in-prison",
            "2015-05-29_ice-gov_ross-ulbricht-sentenced-to-life-in-federal-prison",
        ],
    },
    "operation-silk-road-drug-vendor-who-claimed-to-commit-murders-for-hire-for-silk-road-founder-ross-ulbricht-charged-with-": {
        "sources": [
            "2014-02-04_justice-gov_manhattan-u-s-attorney-announces-the-indictment-of-ross-ulbricht",
            "2015-02-04_fbi-gov_ross-ulbricht-found-guilty-on-all-counts",
            "2015-05-29_fbi-gov_ross-ulbricht-sentenced-to-life-in-prison",
            "2015-05-29_ice-gov_ross-ulbricht-sentenced-to-life-in-federal-prison",
        ],
    },
    "operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace": {
        "sources": [
            "2021-09-08_mdfl_ivanov-tolpintsev-xdedic-extradition",
            "2022-11-22_mdfl_habasescu-xdedic-extradition",
            "2023-02-22_mdfl_pankov-xdedic-extradition",
            "2024-08-07_justice-gov_xdedic-marketplace-victim-services-case-summary",
        ],
    },
    "operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-2": {
        "sources": [
            "2021-09-08_mdfl_ivanov-tolpintsev-xdedic-extradition",
            "2022-11-22_mdfl_habasescu-xdedic-extradition",
            "2023-02-22_mdfl_pankov-xdedic-extradition",
            "2024-08-07_justice-gov_xdedic-marketplace-victim-services-case-summary",
        ],
    },
    "operation-moldovan-national-and-technical-mastermind-of-xdedic-marketplace-extradited-from-spain": {
        "sources": [
            "2021-09-08_mdfl_ivanov-tolpintsev-xdedic-extradition",
            "2023-02-22_mdfl_pankov-xdedic-extradition",
            "2024-01-04_justice-gov_united-states-v-akinola-taylor",
            "2024-08-07_justice-gov_xdedic-marketplace-victim-services-case-summary",
        ],
    },
    "operation-16-defendants-federally-charged-in-connection-with-danabot-malware-scheme-that-infected-computers-worldwide": {
        "sources": [
            "2025-05-23_justice-gov_united-states-v-stepanov-et-al-danabot-operation-endgame-phase-2",
            "2025-05-23_helpnetsecurity-com_danabot-botnet-disrupted-qakbot-leader-indicted",
            "2025-05-23_doj_danabot-indictment",
            "2025-05-23_thehackernews-com_u-s-dismantles-danabot-malware-network-charges-16",
        ],
    },
    "operation-multiple-foreign-nationals-charged-in-connection-with-trickbot-malware-and-conti-ransomware-conspiracies": {
        "sources": [
            "2023-09-07_secretservice-gov_multiple-foreign-nationals-charged-in-connection-with-trickbot-and-conti",
            "2023-09-07_justice-gov_united-states-v-galochkin-et-al-trickbot-conti",
            "2026-04-17_justice-gov_trickbot-conti-sdca-indictment-pdf",
            "2024-01-01_bleepingcomputer-com_russian-trickbot-malware-dev-sentenced-to-64-months-in-prison",
        ],
    },
    "operation-multiple-foreign-nationals-charged-in-connection-with-trickbot-malware-and-conti-ransomware-conspiracies-2": {
        "sources": [
            "2023-09-07_secretservice-gov_multiple-foreign-nationals-charged-in-connection-with-trickbot-and-conti",
            "2023-09-07_justice-gov_united-states-v-galochkin-et-al-trickbot-conti",
            "2026-04-17_justice-gov_trickbot-conti-mdtn-indictment-pdf",
            "2024-01-01_bleepingcomputer-com_russian-trickbot-malware-dev-sentenced-to-64-months-in-prison",
        ],
    },
    "operation-phobos-ransomware-affiliates-arrested-in-coordinated-international-disruption": {
        "sources": [
            "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested",
            "2025-02-11_bleepingcomputer-com_us-charges-phobos-8base-ransomware-operators",
            "cbs-news-hive-ransomware-infrastructure-takedown",
            "2024-11-18_justice-gov_phobos-ransomware-administrator-extradited-from-south-korea-to-face-cybercrime-c",
        ],
    },
    "operation-phobos-ransomware-administrator-extradited-from-south-korea-to-face-cybercrime-charges": {
        "sources": [
            "2024-11-18_justice-gov_phobos-ransomware-administrator-extradited-from-south-korea-to-face-cybercrime-c",
            "2025-02-11_europol_phobos-8base-ransomware-arrests",
            "2025-02-11_bleepingcomputer-com_us-charges-phobos-8base-ransomware-operators",
            "cbs-news-hive-ransomware-infrastructure-takedown",
        ],
    },
    "operation-dual-russian-and-israeli-national-extradited-to-the-united-states-for-his-role-in-the-lockbit-ransomware-consp": {
        "sources": [
            "2026-04-18_justice-gov_us-charges-dual-russian-and-israeli-national-developer-lockbit-ransomware-group",
            "2024-02-20_europol_operation-cronos-lockbit",
            "2024-07-18_nj_lockbit-astamirov-vasiliev-pleas",
            "2024-10-01_europol_operation-cronos-lockbit-phase3",
        ],
    },
    "operation-usd-257-million-seized-in-global-police-crackdown-against-online-scams-operation-first-light-2024": {
        "sources": [
            "2024-06-18_interpol-int_operation-first-light-2024",
            "2024-07-01_police-gov-sg_mid-year-scams-and-cybercrime-brief-2024-operation-first-light",
            "2025-12-01_police-gov-sg_cad-report-2024-operation-first-light",
            "2026-02-01_interpol-int_annual-report-2024-operation-first-light",
        ],
    },
    "operation-usd-257-million-seized-in-global-police-crackdown-against-online-scams-operation-first-light-2024-2": {
        "sources": [
            "2024-06-18_interpol-int_operation-first-light-2024",
            "2024-07-01_police-gov-sg_mid-year-scams-and-cybercrime-brief-2024-operation-first-light",
            "2025-12-01_police-gov-sg_cad-report-2024-operation-first-light",
            "2026-02-01_interpol-int_annual-report-2024-operation-first-light",
        ],
    },
    "operation-usd-257-million-seized-in-global-police-crackdown-against-online-scams-operation-first-light-2024-3": {
        "sources": [
            "2024-06-18_interpol-int_operation-first-light-2024",
            "2024-07-01_police-gov-sg_mid-year-scams-and-cybercrime-brief-2024-operation-first-light",
            "2025-12-01_police-gov-sg_cad-report-2024-operation-first-light",
            "2026-02-01_interpol-int_annual-report-2024-operation-first-light",
        ],
    },
    "operation-nigerian-citizen-extradited-from-the-u-k-arraigned-on-indictment-for-wire-fraud-involving-stolen-tax-informati": {
        "sources": [
            "2016-12-22_justice-gov_nigerian-nationals-charged-with-operating-business-compromise-scheme",
            "2018-06-11_fbi-gov_international-bec-takedown",
            "2019-09-10_fbi-gov_operation-rewired-bec-takedown",
            "2020-11-25_group-ib_operation-falcon-group-ib-helps-interpol-identify-nigerian-bec-ring-members",
        ],
    },
    "operation-nigerian-national-pleads-guilty-to-1-25-million-business-email-compromise-scam-impacting-u-s-company": {
        "sources": [
            "2018-06-11_fbi-gov_international-bec-takedown",
            "2019-09-10_fbi-gov_operation-rewired-bec-takedown",
            "2020-11-25_group-ib_operation-falcon-group-ib-helps-interpol-identify-nigerian-bec-ring-members",
            "2023-06-06_interpol-int_operation-jackal-black-axe-bec",
        ],
    },
    "operation-nigerian-national-pleads-guilty-to-multi-million-dollar-cyber-fraud-scheme-targeting-tulsa-company-and-four-ot": {
        "sources": [
            "2018-06-11_fbi-gov_international-bec-takedown",
            "2019-09-10_fbi-gov_operation-rewired-bec-takedown",
            "2020-11-25_group-ib_operation-falcon-group-ib-helps-interpol-identify-nigerian-bec-ring-members",
            "2023-06-06_interpol-int_operation-jackal-black-axe-bec",
        ],
    },
    "operation-nigerian-national-sentenced-to-more-than-12-years-in-federal-prison-for-cyber-scams": {
        "sources": [
            "2016-08-01_interpol-es_ringleader-of-global-network-behind-thousands-of-online-scams-arrested-in-nigeria",
            "2016-08-01_arstechnica_nigerian-authorities-arrest-alleged-mastermind-of-60m-worth-of-online-scams",
            "2016-08-01_cnn_nigerian-man-arrested-in-global-60-million-scam",
            "2016-08-01_dw_nigerian-arrested-for-international-60-million-dollar-online-fraud",
        ],
    },
    "operation-nigerian-scammer-arrested-for-60-million-email-fraud": {
        "sources": [
            "2016-08-01_interpol-es_ringleader-of-global-network-behind-thousands-of-online-scams-arrested-in-nigeria",
            "2016-08-01_arstechnica_nigerian-authorities-arrest-alleged-mastermind-of-60m-worth-of-online-scams",
            "2016-08-01_cnn_nigerian-man-arrested-in-global-60-million-scam",
            "2016-08-01_dw_nigerian-arrested-for-international-60-million-dollar-online-fraud",
        ],
    },
    "operation-romanian-national-pleads-guilty-selling-access-networks-oregon-state-government-office": {
        "sources": [
            "2026-04-18_justice-gov_romanian-national-pleads-guilty-selling-access-networks-oregon-state-government-office-and",
            "2026-04-17_justice-gov_organized-romanian-criminal-groups-targeted-by-doj-and-romanian-law-enforcement",
            "2026-04-17_coe-int_romania-profile",
            "2026-04-17_en-wikipedia-org_romanian-police",
        ],
    },
    "operation-romanian-national-pleads-guilty-to-selling-access-to-networks-of-oregon-state-government-office-and-other-u-s-": {
        "sources": [
            "2026-04-18_justice-gov_romanian-national-pleads-guilty-selling-access-networks-oregon-state-government-office",
            "2026-04-17_justice-gov_organized-romanian-criminal-groups-targeted-by-doj-and-romanian-law-enforcement",
            "2026-04-17_coe-int_romania-profile",
            "2026-04-17_en-wikipedia-org_romanian-police",
        ],
    },
    "operation-romanian-national-pleads-guilty-to-selling-access-to-networks-of-oregon-state-government-office-and-other-u-s--2": {
        "sources": [
            "2026-04-18_justice-gov_romanian-national-pleads-guilty-selling-access-networks-oregon-state-government-office-and",
            "2026-04-17_justice-gov_organized-romanian-criminal-groups-targeted-by-doj-and-romanian-law-enforcement",
            "2026-04-17_coe-int_romania-profile",
            "2026-04-17_en-wikipedia-org_romanian-police",
        ],
    },
    "operation-romanian-woman-pleads-guilty-to-federal-charges-in-hacking-of-metropolitan-police-department-surveillance-came": {
        "sources": [
            "2017-12-28_justice-gov_two-romanian-suspects-charged-with-hacking-of-metropolitan-police-department-sur",
            "2018-09-20_justice-gov_romanian-woman-pleads-guilty-to-federal-charges-in-hacking-of-metropolitan-polic",
            "2026-04-17_justice-gov_organized-romanian-criminal-groups-targeted-by-doj-and-romanian-law-enforcement",
            "2026-04-17_en-wikipedia-org_romanian-police",
        ],
    },
    "operation-two-romanian-suspects-charged-with-hacking-of-metropolitan-police-department-surveillance-cameras-in-connectio": {
        "sources": [
            "2017-12-28_justice-gov_two-romanian-suspects-charged-with-hacking-of-metropolitan-police-department-sur",
            "2018-09-20_justice-gov_romanian-woman-pleads-guilty-to-federal-charges-in-hacking-of-metropolitan-polic",
            "2026-04-17_justice-gov_organized-romanian-criminal-groups-targeted-by-doj-and-romanian-law-enforcement",
            "2026-04-17_en-wikipedia-org_romanian-police",
        ],
    },
    "operation-two-texas-men-charged-in-stealing-over-a-million-dollars-in-a-romance-scam": {
        "sources": [
            "2021-09-08_justice-gov_two-texas-men-charged-in-stealing-over-a-million-dollars-in-a-romance-scam",
            "2025-09-02_justice-gov_justice-department-seeks-forfeiture-of-848-247-in-cryptocurrency-from-confidence",
            "2026-04-18_justice-gov_united-states-seizes-more-868247-alleged-proceeds-cryptocurrency-confidence-scheme",
            "2026-04-18_justice-gov_four-individuals-charged-laundering-millions-cryptocurrency-investment-scams-known-pig",
        ],
    },
    "operation-justice-department-seeks-forfeiture-of-848-247-in-cryptocurrency-from-confidence-scams": {
        "sources": [
            "2025-09-02_justice-gov_justice-department-seeks-forfeiture-of-848-247-in-cryptocurrency-from-confidence",
            "2026-04-18_justice-gov_united-states-seizes-more-868247-alleged-proceeds-cryptocurrency-confidence-scheme",
            "2026-04-18_justice-gov_four-individuals-charged-laundering-millions-cryptocurrency-investment-scams-known-pig",
            "2026-04-17_trmlabs-com_unmasking-a-crypto-scam-network-the-royal-thai-police-crack-down",
        ],
    },
    "operation-justice-department-seeks-forfeiture-of-over-5-million-in-bitcoin-stolen-in-sim-swapping-scams": {
        "sources": [
            "2019-02-05_justice-gov_two-men-indicted-in-sim-swapping-scheme-to-steal-cryptocurrency",
            "2022-11-08_justice-gov_michigan-man-sentenced-to-3-years-in-prison-for-role-in-sim-swapping-that-led-to",
            "2026-04-18_justice-gov_two-men-indicted-sim-swapping-scheme-steal-cryptocurrency",
            "2026-04-18_justice-gov_michigan-man-sentenced-3-years-prison-role-sim-swapping-led-account-takeovers-and",
        ],
    },
    "operation-two-men-indicted-in-sim-swapping-scheme-to-steal-cryptocurrency": {
        "sources": [
            "2019-02-05_justice-gov_two-men-indicted-in-sim-swapping-scheme-to-steal-cryptocurrency",
            "2022-11-08_justice-gov_michigan-man-sentenced-to-3-years-in-prison-for-role-in-sim-swapping-that-led-to",
            "2026-04-18_justice-gov_justice-department-seeks-forfeiture-over-5-million-bitcoin-stolen-sim-swapping-scams",
            "2026-04-18_justice-gov_michigan-man-sentenced-3-years-prison-role-sim-swapping-led-account-takeovers-and",
        ],
    },
    "operation-chinese-national-sentenced-prison-role-crypto-scam-targeting-americans": {
        "sources": [
            "2026-01-27_justice-gov_chinese-national-sentenced-to-prison-for-role-in-crypto-scam-targeting-americans",
            "2026-04-17_trmlabs-com_unmasking-a-crypto-scam-network-the-royal-thai-police-crack-down",
            "2025-11-06_thepaypers-com_crypto-scammers-steal-over-eur-600-million-now-arrested",
            "2026-04-18_justice-gov_four-individuals-charged-laundering-millions-cryptocurrency-investment-scams-known-pig",
        ],
    },
    "operation-rydox-cybercrime-marketplace-shut-down-and-three-administrators-arrested": {
        "sources": [
            "2024-12-12_justice-gov_rydox-cybercrime-marketplace-shut-down-and-three-administrators-arrested",
            "2024-12-12_cyberscoop-com_rydox-cybercriminal-marketplace-seized-doj-albania-kosovo",
            "2024-12-13_securityaffairs-com_us-authorities-seized-marketplace-rydox",
            "2024-12-16_bitdefender-com_rydox-cybercrime-marketplace-seized-by-law-enforcement-suspected-admins-arrested",
        ],
    },
    "operation-kosovo-national-pleads-guilty-to-operating-an-online-criminal-marketplace": {
        "sources": [
            "2025-05-13_justice-gov_administrator-of-online-criminal-marketplace-extradited-from-kosovo-to-the-unite",
            "2024-12-12_justice-gov_rydox-cybercrime-marketplace-shut-down-and-three-administrators-arrested",
            "2024-12-13_technadu_kosovo-police-shuts-down-rydox-cybercrime-marketplace",
            "2024-12-16_bitdefender-com_rydox-cybercrime-marketplace-seized-by-law-enforcement-suspected-admins-arrested",
        ],
    },
    "operation-administrator-of-online-criminal-marketplace-extradited-from-kosovo-to-the-united-states": {
        "sources": [
            "2025-05-13_justice-gov_administrator-of-online-criminal-marketplace-extradited-from-kosovo-to-the-unite",
            "2024-12-12_justice-gov_rydox-cybercrime-marketplace-shut-down-and-three-administrators-arrested",
            "2024-12-13_technadu_kosovo-police-shuts-down-rydox-cybercrime-marketplace",
            "2024-12-16_bitdefender-com_rydox-cybercrime-marketplace-seized-by-law-enforcement-suspected-admins-arrested",
        ],
    },
    "operation-servers-seized-in-ukraine-moldova-as-germany-takes-down-world-s-largest-illegal-darknet-marketplace": {
        "sources": [
            "2021-01-12_europol-europa-eu_darkmarket-world-s-largest-illegal-dark-web-marketplace-taken-down",
            "2021-01-12_thehackernews-com_authorities-take-down-world-s-largest-illegal-dark-web-marketplace",
            "2021-01-12_sbs-com-au_australian-man-arrested-in-germany-accused-of-running-world-s-largest-darknet-ma",
            "2026-04-18_justice-gov_justice-department-investigation-leads-shutdown-largest-online-darknet-marketplace",
        ],
    },
    "operation-owners-of-empire-market-charged-in-chicago-with-operating-430-million-dark-web-marketplace": {
        "sources": [
            "2026-01-27_justice-gov_co-creator-of-dark-web-marketplace-pleads-guilty-in-chicago-to-drug-conspiracy-c",
            "2026-04-18_justice-gov_co-creator-dark-web-marketplace-pleads-guilty-chicago-drug-conspiracy-charge",
            "2021-07-20_europol-europa-eu_massive-blow-to-criminal-dark-web-activities-after-globally-coordinated-operatio",
            "2015-01-01_europol-europa-eu_iocta-2015-darknets",
        ],
    },
    "operation-individual-arrested-and-charged-with-operating-notorious-darknet-cryptocurrency-mixer": {
        "sources": [
            "2021-08-18_justice-gov_ohio-resident-pleads-guilty-to-operating-darknet-based-bitcoin-mixer-that-launde",
            "2024-11-15_justice-gov_operator-of-helix-darknet-cryptocurrency-mixer-sentenced-in-money-laundering-con",
            "2026-04-18_justice-gov_operator-bitcoin-fog-sentenced-more-12-years-prison-running-notorious-darknet",
            "2026-04-18_justice-gov_justice-department-investigation-leads-takedown-darknet-cryptocurrency-mixer-processed",
        ],
    },
    "operation-ohio-resident-pleads-guilty-to-operating-darknet-based-bitcoin-mixer-that-laundered-over-300-million": {
        "sources": [
            "2021-08-18_justice-gov_ohio-resident-pleads-guilty-to-operating-darknet-based-bitcoin-mixer-that-launde",
            "2024-11-15_justice-gov_operator-of-helix-darknet-cryptocurrency-mixer-sentenced-in-money-laundering-con",
            "2026-04-18_justice-gov_government-forfeits-over-400m-assets-tied-helix-darknet-cryptocurrency-mixer",
            "2026-04-18_justice-gov_us-obtains-legal-title-400-million-assets-tied-helix-cryptocurrency-mixer",
        ],
    },
    "operation-operator-of-helix-darknet-cryptocurrency-mixer-sentenced-in-money-laundering-conspiracy-involving-hundreds-of-": {
        "sources": [
            "2021-08-18_justice-gov_ohio-resident-pleads-guilty-to-operating-darknet-based-bitcoin-mixer-that-launde",
            "2026-04-18_justice-gov_government-forfeits-over-400m-assets-tied-helix-darknet-cryptocurrency-mixer",
            "2026-04-18_justice-gov_us-obtains-legal-title-400-million-assets-tied-helix-cryptocurrency-mixer",
            "2026-04-18_justice-gov_justice-department-investigation-leads-takedown-darknet-cryptocurrency-mixer-processed",
        ],
    },
    "operation-new-york-man-admits-continuing-to-sell-counterfeit-xanax-on-dark-web": {
        "sources": [
            "2023-04-14_justice-gov_new-york-man-indicted-in-st-louis-accused-of-selling-counterfeit-xanax-on-dark-w",
            "2024-05-01_justice-gov_darknet-vendor-who-sold-millions-of-counterfeit-xanax-sentenced",
            "2025-11-18_justice-gov_new-york-man-sentenced-to-54-months-in-prison-for-selling-counterfeit-xanax-on-d",
            "2025-11-18_justice-gov_united-states-v-john-cruz",
        ],
    },
    "operation-new-york-man-indicted-in-st-louis-accused-of-selling-counterfeit-xanax-on-dark-web": {
        "sources": [
            "2025-07-01_justice-gov_new-york-man-admits-continuing-to-sell-counterfeit-xanax-on-dark-web",
            "2024-05-01_justice-gov_darknet-vendor-who-sold-millions-of-counterfeit-xanax-sentenced",
            "2025-11-18_justice-gov_new-york-man-sentenced-to-54-months-in-prison-for-selling-counterfeit-xanax-on-d",
            "2025-11-18_justice-gov_united-states-v-john-cruz",
        ],
    },
    "operation-new-york-man-sentenced-to-54-months-in-prison-for-selling-counterfeit-xanax-on-dark-web": {
        "sources": [
            "2023-04-14_justice-gov_new-york-man-indicted-in-st-louis-accused-of-selling-counterfeit-xanax-on-dark-w",
            "2025-07-01_justice-gov_new-york-man-admits-continuing-to-sell-counterfeit-xanax-on-dark-web",
            "2024-05-01_justice-gov_darknet-vendor-who-sold-millions-of-counterfeit-xanax-sentenced",
            "2025-11-18_justice-gov_new-york-man-sentenced-to-54-months-in-prison-for-selling-counterfeit-xanax-on-d",
        ],
    },
    "operation-culpeper-woman-arrested-in-dark-web-murder-for-hire-plot": {
        "sources": [
            "2024-06-02_justice-gov_woman-accused-of-murder-for-hire-admits-to-using-the-dark-web-to-carry-out-the-c",
            "2024-05-09_justice-gov_woman-sentenced-to-9-years-in-dark-web-murder-for-hire-plot",
            "2024-08-19_justice-gov_woman-who-used-the-dark-web-to-commit-a-murder-for-hire-to-kill-an-ex-boyfriend",
            "2023-07-21_justice-gov_nevada-woman-sentenced-to-5-years-prison-for-hiring-hitman-on-dark-web-to-kill-h",
        ],
    },
    "operation-nevada-woman-sentenced-to-5-years-prison-for-hiring-hitman-on-dark-web-to-kill-her-ex-husband": {
        "sources": [
            "2021-10-27_justice-gov_culpeper-woman-arrested-in-dark-web-murder-for-hire-plot",
            "2024-07-08_justice-gov_queens-woman-charged-with-using-a-hitman-for-hire-website-on-the-dark-web-to-ord",
            "2024-06-02_justice-gov_woman-accused-of-murder-for-hire-admits-to-using-the-dark-web-to-carry-out-the-c",
            "2024-05-09_justice-gov_woman-sentenced-to-9-years-in-dark-web-murder-for-hire-plot",
        ],
    },
    "operation-queens-woman-charged-with-using-a-hitman-for-hire-website-on-the-dark-web-to-order-murder-of-her-lovers-wife": {
        "sources": [
            "2021-10-27_justice-gov_culpeper-woman-arrested-in-dark-web-murder-for-hire-plot",
            "2023-07-21_justice-gov_nevada-woman-sentenced-to-5-years-prison-for-hiring-hitman-on-dark-web-to-kill-h",
            "2024-06-02_justice-gov_woman-accused-of-murder-for-hire-admits-to-using-the-dark-web-to-carry-out-the-c",
            "2024-05-09_justice-gov_woman-sentenced-to-9-years-in-dark-web-murder-for-hire-plot",
        ],
    },
    "operation-woman-accused-of-murder-for-hire-admits-to-using-the-dark-web-to-carry-out-the-crime": {
        "sources": [
            "2021-10-27_justice-gov_culpeper-woman-arrested-in-dark-web-murder-for-hire-plot",
            "2023-07-21_justice-gov_nevada-woman-sentenced-to-5-years-prison-for-hiring-hitman-on-dark-web-to-kill-h",
            "2024-05-09_justice-gov_woman-sentenced-to-9-years-in-dark-web-murder-for-hire-plot",
            "2024-08-19_justice-gov_woman-who-used-the-dark-web-to-commit-a-murder-for-hire-to-kill-an-ex-boyfriend",
        ],
    },
    "operation-woman-sentenced-to-9-years-in-dark-web-murder-for-hire-plot": {
        "sources": [
            "2021-10-27_justice-gov_culpeper-woman-arrested-in-dark-web-murder-for-hire-plot",
            "2023-07-21_justice-gov_nevada-woman-sentenced-to-5-years-prison-for-hiring-hitman-on-dark-web-to-kill-h",
            "2024-06-02_justice-gov_woman-accused-of-murder-for-hire-admits-to-using-the-dark-web-to-carry-out-the-c",
            "2024-08-19_justice-gov_woman-who-used-the-dark-web-to-commit-a-murder-for-hire-to-kill-an-ex-boyfriend",
        ],
    },
    "operation-woman-who-used-the-dark-web-to-commit-a-murder-for-hire-to-kill-an-ex-boyfriends-new-girlfriend-is-sentenced-t": {
        "sources": [
            "2021-10-27_justice-gov_culpeper-woman-arrested-in-dark-web-murder-for-hire-plot",
            "2023-07-21_justice-gov_nevada-woman-sentenced-to-5-years-prison-for-hiring-hitman-on-dark-web-to-kill-h",
            "2024-06-02_justice-gov_woman-accused-of-murder-for-hire-admits-to-using-the-dark-web-to-carry-out-the-c",
            "2024-05-09_justice-gov_woman-sentenced-to-9-years-in-dark-web-murder-for-hire-plot",
        ],
    },
    "operation-utah-man-charged-with-murder-for-hire-scheme": {
        "sources": [
            "2023-12-06_justice-gov_utah-man-pleads-guilty-to-murder-for-hire-scheme",
            "2024-04-05_justice-gov_utah-man-sentenced-to-seven-years-in-prison-for-murder-for-hire-scheme",
            "2021-10-27_justice-gov_culpeper-woman-arrested-in-dark-web-murder-for-hire-plot",
            "2024-06-02_justice-gov_woman-accused-of-murder-for-hire-admits-to-using-the-dark-web-to-carry-out-the-c",
        ],
    },
    "operation-utah-man-pleads-guilty-to-murder-for-hire-scheme": {
        "sources": [
            "2021-11-12_justice-gov_utah-man-charged-with-murder-for-hire-scheme",
            "2024-04-05_justice-gov_utah-man-sentenced-to-seven-years-in-prison-for-murder-for-hire-scheme",
            "2021-10-27_justice-gov_culpeper-woman-arrested-in-dark-web-murder-for-hire-plot",
            "2024-06-02_justice-gov_woman-accused-of-murder-for-hire-admits-to-using-the-dark-web-to-carry-out-the-c",
        ],
    },
    "operation-utah-man-sentenced-to-seven-years-in-prison-for-murder-for-hire-scheme": {
        "sources": [
            "2021-11-12_justice-gov_utah-man-charged-with-murder-for-hire-scheme",
            "2023-12-06_justice-gov_utah-man-pleads-guilty-to-murder-for-hire-scheme",
            "2021-10-27_justice-gov_culpeper-woman-arrested-in-dark-web-murder-for-hire-plot",
            "2024-06-02_justice-gov_woman-accused-of-murder-for-hire-admits-to-using-the-dark-web-to-carry-out-the-c",
        ],
    },
    "operation-darknet-drug-vendor-arrested-for-distributing-illicit-prescription-drugs": {
        "sources": [
            "2020-12-02_justice-gov_darknet-drug-vendor-arrested-for-distributing-illicit-prescription-drugs",
            "2021-08-04_justice-gov_darknet-drug-vendor-pleads-guilty-to-distributing-illicit-prescription-drugs",
            "2020-04-09_justice-gov_darknet-vendor-arrested-on-distribution-and-money-laundering-charges",
            "2016-10-31_ice-gov_international-darknet-marketplace-enforcement-operation",
        ],
    },
    "operation-darknet-vendor-arrested-on-distribution-and-money-laundering-charges": {
        "sources": [
            "2020-12-02_justice-gov_darknet-drug-vendor-arrested-for-distributing-illicit-prescription-drugs",
            "2021-08-04_justice-gov_darknet-drug-vendor-pleads-guilty-to-distributing-illicit-prescription-drugs",
            "2016-10-31_ice-gov_international-darknet-marketplace-enforcement-operation",
            "2016-11-01_fbi-gov_a-primer-on-darknet-marketplaces",
        ],
    },
    "operation-man-pleads-guilty-to-conspiracy-to-distribute-meth-on-the-darknet": {
        "sources": [
            "2022-07-12_justice-gov_man-sentenced-for-conspiracy-to-distribute-meth-on-the-darknet",
            "2023-06-06_justice-gov_dark-web-traffickers-of-heroin-methamphetamine-and-cocaine-prosecuted",
            "2016-10-31_ice-gov_international-darknet-marketplace-enforcement-operation",
            "2017-07-20_europol-europa-eu_massive-blow-to-criminal-dark-web-activities-after-globally-coordinated-operatio",
        ],
    },
    "operation-man-sentenced-for-conspiracy-to-distribute-meth-on-the-darknet": {
        "sources": [
            "2020-12-15_justice-gov_man-pleads-guilty-to-conspiracy-to-distribute-meth-on-the-darknet",
            "2023-06-06_justice-gov_dark-web-traffickers-of-heroin-methamphetamine-and-cocaine-prosecuted",
            "2016-10-31_ice-gov_international-darknet-marketplace-enforcement-operation",
            "2017-07-20_europol-europa-eu_massive-blow-to-criminal-dark-web-activities-after-globally-coordinated-operatio",
        ],
    },
    "operation-issaquah-washington-man-sentenced-to-7-years-in-prison-for-dealing-fentanyl-and-other-drugs-on-the-darknet": {
        "sources": [
            "2024-07-22_justice-gov_puyallup-man-caught-with-nearly-100-000-fentanyl-pills-and-five-firearms-sentenc",
            "2025-02-25_justice-gov_king-county-man-who-dealt-narcotics-on-the-dark-web-and-kept-a-cache-of-weapons",
            "2023-12-06_justice-gov_pierce-county-based-drug-trafficking-organization-indicted-for-distributing-coca",
            "2023-04-20_justice-gov_six-indicted-as-part-of-whatcom-county-fentanyl-trafficking-organization",
        ],
    },
    "operation-o-c-and-houston-men-sentenced-to-decades-in-prison-for-supplying-fentanyl-and-other-drugs-sold-on-darknet-and-": {
        "sources": [
            "2025-01-13_justice-gov_two-southern-california-men-who-supplied-fentanyl-sold-to-darknet-customers-in-a",
            "2023-11-07_justice-gov_federal-grand-jury-indicts-2-for-allegedly-supplying-fentanyl-and-other-narcotic",
            "2023-05-18_justice-gov_federal-grand-jury-indicts-san-fernando-valley-duo-who-allegedly-used-darknet-ma",
            "2026-04-18_justice-gov_los-angeles-case-part-largest-international-operation-against-darknet-trafficking",
        ],
    },
    "operation-puyallup-man-caught-with-nearly-100-000-fentanyl-pills-and-five-firearms-sentenced-to-six-and-a-half-years-in-": {
        "sources": [
            "2022-09-23_justice-gov_issaquah-washington-man-sentenced-to-7-years-in-prison-for-dealing-fentanyl-and",
            "2025-02-25_justice-gov_king-county-man-who-dealt-narcotics-on-the-dark-web-and-kept-a-cache-of-weapons",
            "2023-12-06_justice-gov_pierce-county-based-drug-trafficking-organization-indicted-for-distributing-coca",
            "2024-07-15_justice-gov_significant-member-of-a-whatcom-county-fentanyl-trafficking-ring-sentenced-to-4",
        ],
    },
    "operation-king-county-man-who-dealt-narcotics-on-the-dark-web-and-kept-a-cache-of-weapons-at-his-rv-sentenced-to-8-years": {
        "sources": [
            "2022-09-23_justice-gov_issaquah-washington-man-sentenced-to-7-years-in-prison-for-dealing-fentanyl-and",
            "2024-07-22_justice-gov_puyallup-man-caught-with-nearly-100-000-fentanyl-pills-and-five-firearms-sentenc",
            "2023-12-06_justice-gov_pierce-county-based-drug-trafficking-organization-indicted-for-distributing-coca",
            "2024-07-15_justice-gov_significant-member-of-a-whatcom-county-fentanyl-trafficking-ring-sentenced-to-4",
        ],
    },
    "operation-significant-member-of-a-whatcom-county-fentanyl-trafficking-ring-sentenced-to-4-years-in-prison": {
        "sources": [
            "2023-04-20_justice-gov_six-indicted-as-part-of-whatcom-county-fentanyl-trafficking-organization",
            "2021-02-23_justice-gov_three-allegedly-responsible-for-distributing-thousands-of-fentanyl-pills-in-what",
            "2023-12-06_justice-gov_pierce-county-based-drug-trafficking-organization-indicted-for-distributing-coca",
            "2024-07-22_justice-gov_puyallup-man-caught-with-nearly-100-000-fentanyl-pills-and-five-firearms-sentenc",
        ],
    },
    "operation-pierce-county-based-drug-trafficking-organization-indicted-for-distributing-cocaine-fentanyl-and-marijuana": {
        "sources": [
            "2023-04-20_justice-gov_six-indicted-as-part-of-whatcom-county-fentanyl-trafficking-organization",
            "2021-02-23_justice-gov_three-allegedly-responsible-for-distributing-thousands-of-fentanyl-pills-in-what",
            "2024-07-15_justice-gov_significant-member-of-a-whatcom-county-fentanyl-trafficking-ring-sentenced-to-4",
            "2024-07-22_justice-gov_puyallup-man-caught-with-nearly-100-000-fentanyl-pills-and-five-firearms-sentenc",
        ],
    },
    "operation-the-drug-llama-pleads-guilty-to-distributing-fentanyl-on-the-dark-web": {
        "sources": [
            "2020-02-12_justice-gov_dark-web-fentanyl-trafficker-known-as-the-drug-llama-sentenced-to-13-years-in-fe",
            "2020-10-08_justice-gov_prolific-dark-web-dealer-of-carfentanil-and-fentanyl-sentenced-to-17-years-in-pr",
            "2024-04-12_justice-gov_seattle-man-sentenced-for-buying-630-000-counterfeit-pills-on-the-dark-web",
            "2022-06-01_justice-gov_two-men-indicted-for-international-conspiracy-to-ship-fentanyl-other-drugs-into",
        ],
    },
    "operation-prolific-dark-web-dealer-of-carfentanil-and-fentanyl-sentenced-to-1712-years-in-prison": {
        "sources": [
            "2019-07-17_justice-gov_the-drug-llama-pleads-guilty-to-distributing-fentanyl-on-the-dark-web",
            "2024-04-12_justice-gov_seattle-man-sentenced-for-buying-630-000-counterfeit-pills-on-the-dark-web",
            "2022-06-01_justice-gov_two-men-indicted-for-international-conspiracy-to-ship-fentanyl-other-drugs-into",
            "2025-06-23_justice-gov_seven-georgians-indicted-for-operating-online-fentanyl-meth-marketplace",
        ],
    },
    "operation-two-men-indicted-for-international-conspiracy-to-ship-fentanyl-other-drugs-into-united-states-through-dark-web": {
        "sources": [
            "2025-06-23_justice-gov_seven-georgians-indicted-for-operating-online-fentanyl-meth-marketplace",
            "2024-04-12_justice-gov_seattle-man-sentenced-for-buying-630-000-counterfeit-pills-on-the-dark-web",
            "2019-07-17_justice-gov_the-drug-llama-pleads-guilty-to-distributing-fentanyl-on-the-dark-web",
            "2020-10-08_justice-gov_prolific-dark-web-dealer-of-carfentanil-and-fentanyl-sentenced-to-17-years-in-pr",
        ],
    },
    "operation-seven-georgians-indicted-for-operating-online-fentanyl-meth-marketplace": {
        "sources": [
            "2022-06-01_justice-gov_two-men-indicted-for-international-conspiracy-to-ship-fentanyl-other-drugs-into",
            "2024-04-12_justice-gov_seattle-man-sentenced-for-buying-630-000-counterfeit-pills-on-the-dark-web",
            "2023-11-08_justice-gov_serbian-citizen-pleads-guilty-to-running-monopoly-drug-market-on-the-darknet",
            "2026-01-27_justice-gov_slovakian-man-admits-aiding-darknet-market-that-sold-drugs-and-stolen-personal-i",
        ],
    },
    "operation-serbian-citizen-pleads-guilty-to-running-monopoly-drug-market-on-the-darknet": {
        "sources": [
            "2026-04-18_justice-gov_serbian-citizen-sentenced-14-years-prison-operating-monopoly-narcotics-marketplace-dark",
            "2026-01-27_justice-gov_slovakian-man-admits-aiding-darknet-market-that-sold-drugs-and-stolen-personal-i",
            "2023-12-21_justice-gov_slovakian-man-accused-of-running-darknet-market-selling-drugs-and-personal-infor",
            "2025-06-23_justice-gov_seven-georgians-indicted-for-operating-online-fentanyl-meth-marketplace",
        ],
    },
    "operation-slovakian-man-admits-aiding-darknet-market-that-sold-drugs-and-stolen-personal-information": {
        "sources": [
            "2023-12-21_justice-gov_slovakian-man-accused-of-running-darknet-market-selling-drugs-and-personal-infor",
            "2023-11-08_justice-gov_serbian-citizen-pleads-guilty-to-running-monopoly-drug-market-on-the-darknet",
            "2026-04-18_justice-gov_serbian-citizen-sentenced-14-years-prison-operating-monopoly-narcotics-marketplace-dark",
            "2025-06-23_justice-gov_seven-georgians-indicted-for-operating-online-fentanyl-meth-marketplace",
        ],
    },
    "operation-slovakian-man-admits-aiding-darknet-market-sold-drugs-and-stolen-personal-information": {
        "sources": [
            "2023-12-21_justice-gov_slovakian-man-accused-of-running-darknet-market-selling-drugs-and-personal-infor",
            "2023-11-08_justice-gov_serbian-citizen-pleads-guilty-to-running-monopoly-drug-market-on-the-darknet",
            "2026-04-18_justice-gov_serbian-citizen-sentenced-14-years-prison-operating-monopoly-narcotics-marketplace-dark",
            "2025-06-23_justice-gov_seven-georgians-indicted-for-operating-online-fentanyl-meth-marketplace",
        ],
    },
    "operation-sturgis-man-charged-with-selling-counterfeit-drugs-on-dark-web": {
        "sources": [
            "2025-01-08_justice-gov_sturgis-man-sentenced-to-70-months-for-selling-drugs-on-dark-web",
            "2024-04-12_justice-gov_seattle-man-sentenced-for-buying-630-000-counterfeit-pills-on-the-dark-web",
            "2025-11-18_justice-gov_new-york-man-sentenced-to-54-months-in-prison-for-selling-counterfeit-xanax-on-d",
            "2024-05-01_justice-gov_darknet-vendor-who-sold-millions-of-counterfeit-xanax-sentenced",
        ],
    },
    "operation-sturgis-man-sentenced-to-70-months-for-selling-drugs-on-dark-web": {
        "sources": [
            "2024-05-29_justice-gov_sturgis-man-charged-with-selling-counterfeit-drugs-on-dark-web",
            "2024-04-12_justice-gov_seattle-man-sentenced-for-buying-630-000-counterfeit-pills-on-the-dark-web",
            "2025-11-18_justice-gov_new-york-man-sentenced-to-54-months-in-prison-for-selling-counterfeit-xanax-on-d",
            "2024-05-01_justice-gov_darknet-vendor-who-sold-millions-of-counterfeit-xanax-sentenced",
        ],
    },
    "operation-seattle-man-sentenced-for-buying-630-000-counterfeit-pills-on-the-dark-web": {
        "sources": [
            "2024-05-29_justice-gov_sturgis-man-charged-with-selling-counterfeit-drugs-on-dark-web",
            "2025-01-08_justice-gov_sturgis-man-sentenced-to-70-months-for-selling-drugs-on-dark-web",
            "2025-11-18_justice-gov_new-york-man-sentenced-to-54-months-in-prison-for-selling-counterfeit-xanax-on-d",
            "2024-05-01_justice-gov_darknet-vendor-who-sold-millions-of-counterfeit-xanax-sentenced",
        ],
    },
    "operation-kc-man-sentenced-for-selling-meth-heroin-on-the-dark-web": {
        "sources": [
            "2024-02-29_justice-gov_kc-man-sentenced-for-selling-meth-heroin-on-the-dark-web",
            "2024-02-29_dea-gov_dark-web-dealer-meth-heroin-heads-prison",
            "2024-02-29_kctv5-com_kc-man-sentenced-decade-prison-selling-meth-heroin-dark-web",
            "2024-03-01_kttn-com_kc-man-sentenced-10-years-prison-selling-meth-heroin-dark-web",
            "2024-02-29_dea-gov_press-releases-dark-web-dealer-meth-heroin-heads-prison-index",
        ],
    },
    "operation-tattoo-shop-owner-sentenced-to-more-than-7-years-in-prison-for-distributing-heroin-and-methamphetamine-on-the-": {
        "sources": [
            "2022-11-15_justice-gov_tattoo-shop-owner-sentenced-to-more-than-7-years-in-prison-for-distributing-hero",
            "2022-11-15_oversight-gov_tattoo-shop-owner-sentenced-more-7-years-prison-distributing-heroin-and-methamphetamine-dark-web",
            "2021-10-07_justice-gov_arizona-man-pleads-guilty-dark-web-narcotics-conspiracy",
            "2022-02-17_justice-gov_arizona-man-sentenced-over-11-years-prison-conspiracy-sell-narcotics-dark-web",
            "2022-02-17_uspsoig-gov_arizona-man-sentenced-over-11-years-prison-conspiracy-sell-narcotics-dark-web",
        ],
    },
    "operation-iranian-national-indicted-for-operating-online-marketplace-offering-fentanyl-and-money-laundering-services": {
        "sources": [
            "2025-04-17_justice-gov_iranian-national-indicted-for-operating-online-marketplace-offering-fentanyl-and",
            "2025-04-17_justice-gov_iranian-national-indicted-for-operating-online-marketplace-offering-fentanyl-oth",
            "2025-03-05_securityweek_us-sanctions-iranian-administrator-nemesis-darknet-marketplace",
            "2024-03-21_apnews_german-authorities-shut-down-online-marketplace-for-drugs-data-and-cybercrime-services",
            "2024-03-25_cybernews_darknet-marketplace-nemesis-market-brought-down-by-authorities",
        ],
    },
    "operation-international-crypto-vendor-sentenced-for-money-laundering-conspiracy": {
        "sources": [
            "2025-01-17_justice-gov_international-crypto-vendor-sentenced-for-money-laundering-conspiracy",
            "2025-04-08_gizmodo_the-fbi-hijacked-and-ran-a-dark-web-money-laundering-operation-called-elonmuskwhm",
            "2025-01-24_cyberintel-media_fbi-takes-down-crypto-laundering-scam",
            "2025-01-21_cryptotimes-io_indian-crypto-vendor-sentenced-in-prison-for-money-laundering",
            "2025-01-17_morelaw_re-united-states-of-america-v-anurag-pramod-murarka",
        ],
    },
    "operation-iranian-national-indicted-for-operating-online-marketplace-offering-fentanyl-other-drugs-and-money-laundering-": {
        "sources": [
            "2025-04-17_justice-gov_iranian-national-indicted-for-operating-online-marketplace-offering-fentanyl-oth",
            "2025-04-17_opa_parsarad-nemesis-indictment",
            "2025-03-05_securityweek_us-sanctions-iranian-administrator-nemesis-darknet-marketplace",
            "2024-03-21_therecord-media_nemesis-darknet-marketplace-raided-in-germany-led-operation",
            "2024-03-21_bka-de_illegaler-darknet-marktplatz-nemesis-market-abgeschaltet",
        ],
    },
    "operation-law-enforcement-seize-record-amounts-of-illegal-drugs-firearms-and-drug-trafficking-proceeds-in-international-": {
        "sources": [
            "2026-04-18_justice-gov_law-enforcement-seize-record-amounts-illegal-drugs-firearms-and-drug-trafficking-proceeds",
            "2025-05-22_fbi-gov_global-operation-targets-darknet-drug-trafficking",
            "2025-05-22_ice-gov_ice-europol-law-enforcement-partners-dismantle-major-illicit-drug-networks-global-darknet-crackdown",
            "2025-05-22_occrp_org_massive-dark-web-sweep-leads-to-270-arrests-worldwide",
            "2025-05-22_hackread_com_operation-raptor-270-arrested-global-crackdown-on-dark-web-vendors",
        ],
    },
    "operation-three-darknet-fentanyl-vendors-sentenced-to-over-20-years-in-prison": {
        "sources": [
            "2023-07-14_edva_dittman-schiffner-langer-darknet-sentencing",
            "2023-07-14_justice-gov_three-darknet-fentanyl-vendors-sentenced-to-over-20-years-in-prison",
            "2023-07-14_fda-gov_three-darknet-fentanyl-vendors-sentenced-over-20-years-prison",
            "2023-07-18_ice-gov_hsi-arizona-investigation-sends-3-darknet-fentanyl-vendors-prison-more-20-years",
            "2023-07-19_hstoday_us_hsi-arizona-investigation-sends-3-darknet-fentanyl-vendors-to-prison-for-more-than-20-years",
            "2023-01-20_businessinsider_a-dark-web-drug-trafficker-gave-the-fbi-a-roadmap-to-his-clients",
        ],
    },
    "operation-us-v-kancharla-dark-web": {
        "sources": [
            "2022-05-26_edva_kancharla-darknet-vendor-plea",
            "2022-05-26_justice-gov_united-states-v-akshay-ram-kancharla",
            "2022-05-26_justice-gov_darknet-vendor-of-fentanyl-laced-pills-pleads-guilty",
            "2022-05-26_washingtonpost_com_fentanyl-dealer-pleads-guilty-in-virginia-after-online-drug-bust",
            "2022-05-30_media-uspa24-com_darknet-vendor-of-fentanyl-laced-pills-pleads-guilty",
            "2022-05-26_shorenewsnetwork_com_darknet-vendor-of-fentanyl-laced-pills-pleads-guilty",
            "2022-05-31_safemedicines_org_may-31-2022",
        ],
    },
    "operation-us-v-udvardi-dark-web": {
        "sources": [
            "2023-08-17_edva_justin-udvardi-darknet-sentencing",
            "2023-08-17_justice-gov_united-states-v-justin-udvardi",
            "2023-08-17_justice-gov_darknet-vendor-sentenced-for-distribution-of-fentanyl-laced-pills-and-crystal-me",
            "2023-08-17_azfamily_com_glendale-man-sentenced-35-years-selling-fentanyl-crystal-meth-dark-web",
            "2023-07-14_fda-gov_three-darknet-fentanyl-vendors-sentenced-over-20-years-prison",
            "2023-08-21_safemedicines_org_aug-21-2023",
            "2024-06-20_fincen_gov_supplemental-advisory-on-fentanyl-related-financial-activity",
        ],
    },
    "operation-us-v-taylor-fischer-dark-web": {
        "sources": [
            "2023-08-25_edva_taylor-fischer-darknet-vendors-plea",
            "2023-08-25_justice-gov_two-darknet-vendors-plead-guilty-to-trafficking-fentanyl-and-other-illegal-drugs",
            "2023-08-28_hstoday_us_two-darknet-vendors-plead-guilty-to-trafficking-fentanyl-and-other-illegal-drugs",
            "2023-08-25_crimewire_two-darknet-vendors-plead-guilty-to-trafficking-fentanyl-and-other-illegal-drugs",
            "2023-08-17_justice-gov_darknet-vendor-sentenced-for-distribution-of-fentanyl-laced-pills-and-crystal-me",
            "2023-08-31_protos_com_crypto-using-sky-high-fentanyl-dealers-plead-guilty",
        ],
    },
    "operation-us-v-brewer-dark-web": {
        "sources": [
            "2021-07-08_ndtx_brewer-operation-disruptor-sentencing",
            "2021-07-08_justice-gov_darkweb-drug-trafficker-arrested-in-operation-disruptor-sentenced-to-6-5-years-i",
            "2020-12-17_justice-gov_darkweb-drug-trafficker-arrested-in-operation-disruptor-pleads-guilty",
            "2021-01-06_cbsnews_com_darkweb-drug-trafficker-arrested-in-operation-disruptor-pleads-guilty",
            "2021-08-30_dallasobserver_com_operation-disruptor-plano-man-sentenced-as-feds-target-dark-web-drug-dealers",
            "2021-07-09_tarnkappe-info_operation-disruptor-darknet-drogenhaendler-zu-65-jahren-gefaengnis-verurteilt",
        ],
    },
    "operation-us-v-darkweb-drug-trafficker": {
        "sources": [
            "2026-04-18_justice-gov_darkweb-drug-trafficker-arrested-operation-disruptor-pleads-guilty",
            "2020-12-17_justice-gov_darkweb-drug-trafficker-arrested-in-operation-disruptor-pleads-guilty",
            "2026-04-18_justice-gov_ndtx-charges-alleged-darkweb-drug-trafficker-arrested-doj-operation-disruptor",
            "2021-01-06_cbsnews_com_darkweb-drug-trafficker-arrested-in-operation-disruptor-pleads-guilty",
            "2021-08-30_dallasobserver_com_operation-disruptor-plano-man-sentenced-as-feds-target-dark-web-drug-dealers",
            "2020-12-17_cbsnews_com_north-texas-man-pleads-guilty-to-drug-trafficking-crime-on-darkweb",
        ],
    },
    "operation-nicaraguan-national-pleads-guilty-to-conspiring-to-distribute-cocaine-and-marijuana-on-the-darknet": {
        "sources": [
            "2026-04-18_justice-gov_nicaraguan-national-pleads-guilty-conspiring-distribute-cocaine-and-marijuana-darknet",
            "2019-06-03_dea-gov_nicaraguan-national-pleads-guilty-conspiring-distribute-cocaine-and-marijuana-darknet",
            "2019-06-04_ice-gov_nicaraguan-national-pleads-guilty-conspiring-distribute-cocaine-marijuana-darknet",
            "2019-06-03_dea-gov_press-releases-index-nicaraguan-national-darknet",
            "2018-10-12_justice-gov_two-sacramento-men-indicted-for-distributing-cocaine-and-marijuana-on-dark-web-m",
        ],
    },
    "operation-parma-men-among-those-charged-as-part-of-crackdown-on-darknet-vendors": {
        "sources": [
            "2026-04-18_justice-gov_parma-men-among-those-charged-part-crackdown-darknet-vendors",
            "2018-06-26_secretservice-gov_parma-men-among-those-charged-part-crackdown-darknet-vendors",
            "2018-06-26_justice-gov_opa_first-nationwide-undercover-operation-targeting-darknet-vendors-results-arrests-more-35",
            "2018-06-26_justice-gov_vt_first-nationwide-undercover-operation-targeting-darknet-vendors-results-arrests-more-35",
            "2018-06-27_wired_a-top-dark-web-drug-ring-goes-down-thanks-to-atm-withdrawals",
        ],
    },
    "operation-two-sacramento-men-indicted-for-distributing-cocaine-and-marijuana-on-dark-web-marketplaces": {
        "sources": [
            "2026-04-18_justice-gov_two-sacramento-men-indicted-distributing-cocaine-and-marijuana-dark-web-marketplaces",
            "2018-06-26_secretservice-gov_parma-men-among-those-charged-part-crackdown-darknet-vendors",
            "2018-06-26_justice-gov_opa_first-nationwide-undercover-operation-targeting-darknet-vendors-results-arrests-more-35",
            "2018-06-26_justice-gov_vt_first-nationwide-undercover-operation-targeting-darknet-vendors-results-arrests-more-35",
            "2019-06-03_dea-gov_nicaraguan-national-pleads-guilty-conspiring-distribute-cocaine-and-marijuana-darknet",
        ],
    },
    "operation-sacramento-man-indicted-for-drug-distribution-via-the-darknet": {
        "sources": [
            "2026-04-18_justice-gov_sacramento-man-indicted-drug-distribution-darknet",
            "2021-10-26_justice-gov_opa_international-law-enforcement-operation-targeting-opioid-traffickers-darknet-results-150",
            "2021-10-26_dea-gov_department-of-justice-announces-results-of-operation-dark-huntor",
            "2021-10-26_justice-gov_deputy-ag-lisa-monaco-delivers-remarks-on-operation-dark-huntor",
            "2021-10-26_wired_dark-web-drug-busts-lead-to-150-arrests",
        ],
    },
    "operation-maryland-men-indicted-on-charges-relating-to-dark-web-drug-distribution-and-money-laudering-government-seized-": {
        "sources": [
            "2026-04-18_justice-gov_maryland-men-indicted-charges-relating-dark-web-drug-distribution-and-money-laudering",
            "2018-06-26_justice-gov_maryland-men-indicted-on-charges-relating-to-dark-web-drug-distribution-and-mone",
            "2018-06-26_justice-gov_opa_first-nationwide-undercover-operation-targeting-darknet-vendors-results-arrests-more-35",
            "2018-06-26_justice-gov_vt_first-nationwide-undercover-operation-targeting-darknet-vendors-results-arrests-more-35",
            "2018-06-26_bitcoininsider_org_17-million-bitcoin-seized-dark-web-undercover-sting-operation",
            "2018-06-26_secretservice-gov_parma-men-among-those-charged-part-crackdown-darknet-vendors",
        ],
    },
    "operation-leader-of-darknet-italianmafiabrussels-drug-trafficking-organization-sentenced-to-11-years-imprisonment": {
        "sources": [
            "2026-04-18_justice-gov_leader-darknet-italianmafiabrussels-drug-trafficking-organization-sentenced-11-years",
            "2018-10-01_justice-gov_leader-of-darknet-italianmafiabrussels-drug-trafficking-organization-sentenced-t",
            "2016-10-17_justice-gov_romania-extradites-alleged-leader-italianmafiabrussels-drug-trafficking-organization",
            "2016-10-17_ice-gov_alleged-leader-italianmafiabrussels-drug-trafficking-organization-extradited-romania",
            "2018-10-01_ice-gov_leader-darknets-italianmafiabrussels-drug-trafficking-organization-sentenced-denver",
            "2018-10-01_denver7_com_leader-of-italianmafiabrussels-drug-trafficking-organization-sentenced-to-prison-in-denver",
        ],
    },
    "operation-member-of-darknet-drug-trafficking-organization-italianmafiabrussels-sentenced-to-prison": {
        "sources": [
            "2026-04-18_justice-gov_member-darknet-drug-trafficking-organization-italianmafiabrussels-sentenced-prison",
            "2018-04-12_justice-gov_member-of-darknet-drug-trafficking-organization-italianmafiabrussels-sentenced-t",
            "2018-04-11_ice-gov_member-darknet-drug-trafficking-organization-italianmafiabrussels-sentenced-3-years",
            "2016-10-17_justice-gov_romania-extradites-alleged-leader-italianmafiabrussels-drug-trafficking-organization",
            "2016-10-17_ice-gov_alleged-leader-italianmafiabrussels-drug-trafficking-organization-extradited-romania",
            "2018-04-11_occrp_org_us-3-years-prison-for-international-darknet-drug-trafficker",
        ],
    },
    "operation-three-l-a-residents-charged-in-darknet-drug-ring-that-allegedly-shipped-methamphetamine-to-buyers-around-the-w": {
        "sources": [
            "2026-04-18_justice-gov_three-la-residents-charged-darknet-drug-ring-allegedly-shipped-methamphetamine-buyers",
            "2019-04-02_justice-gov_three-l-a-residents-charged-in-darknet-drug-ring-that-allegedly-shipped-methamph",
            "2020-07-15_justice-gov_los-angeles-county-woman-pleads-guilty-to-conspiring-to-distribute-heroin-metham",
            "2024-06-18_justice-gov_southern-california-woman-pleads-guilty-to-fentanyl-distribution-and-money-laund",
            "2025-12-09_justice-gov_southern-california-man-pleads-guilty-to-fentanyl-and-methamphetamine-distributi",
            "2024-11-21_justice-gov_santa-clarita-man-who-led-organization-that-trafficked-drugs-to-darknet-customer",
        ],
    },
    "operation-los-angeles-county-woman-pleads-guilty-to-conspiring-to-distribute-heroin-methamphetamine-and-cocaine-on-the-d": {
        "sources": [
            "2020-07-15_justice-gov_united-states-v-catherine-stuckey",
            "2019-04-02_justice-gov_three-l-a-residents-charged-in-darknet-drug-ring-that-allegedly-shipped-methamph",
            "2024-06-18_justice-gov_southern-california-woman-pleads-guilty-to-fentanyl-distribution-and-money-laund",
            "2025-12-09_justice-gov_southern-california-man-pleads-guilty-to-fentanyl-and-methamphetamine-distributi",
            "2024-11-21_justice-gov_santa-clarita-man-who-led-organization-that-trafficked-drugs-to-darknet-customer",
        ],
    },
    "operation-southern-california-woman-pleads-guilty-to-fentanyl-distribution-and-money-laundering-conspiracy": {
        "sources": [
            "2026-04-18_justice-gov_southern-california-woman-pleads-guilty-fentanyl-distribution-and-money-laundering",
            "2024-06-18_justice-gov_southern-california-woman-pleads-guilty-to-fentanyl-distribution-and-money-laund",
            "2025-12-09_justice-gov_southern-california-man-pleads-guilty-to-fentanyl-and-methamphetamine-distributi",
            "2024-11-21_justice-gov_santa-clarita-man-who-led-organization-that-trafficked-drugs-to-darknet-customer",
            "2019-04-02_justice-gov_three-l-a-residents-charged-in-darknet-drug-ring-that-allegedly-shipped-methamph",
            "2020-07-15_justice-gov_los-angeles-county-woman-pleads-guilty-to-conspiring-to-distribute-heroin-metham",
        ],
    },
    "operation-southern-california-man-pleads-guilty-to-fentanyl-and-methamphetamine-distribution-conspiracy": {
        "sources": [
            "2026-04-18_justice-gov_southern-california-man-pleads-guilty-fentanyl-and-methamphetamine-distribution",
            "2025-12-09_justice-gov_southern-california-man-pleads-guilty-to-fentanyl-and-methamphetamine-distributi",
            "2024-06-18_justice-gov_southern-california-woman-pleads-guilty-to-fentanyl-distribution-and-money-laund",
            "2024-11-21_justice-gov_santa-clarita-man-who-led-organization-that-trafficked-drugs-to-darknet-customer",
            "2019-04-02_justice-gov_three-l-a-residents-charged-in-darknet-drug-ring-that-allegedly-shipped-methamph",
            "2020-07-15_justice-gov_los-angeles-county-woman-pleads-guilty-to-conspiring-to-distribute-heroin-metham",
        ],
    },
    "operation-santa-clarita-man-who-led-organization-that-trafficked-drugs-to-darknet-customers-nationwide-sentenced-to-8-ye": {
        "sources": [
            "2026-04-18_justice-gov_santa-clarita-man-who-led-organization-trafficked-drugs-darknet-customers-nationwide",
            "2024-11-21_justice-gov_santa-clarita-man-who-led-organization-that-trafficked-drugs-to-darknet-customer",
            "2025-12-09_justice-gov_southern-california-man-pleads-guilty-to-fentanyl-and-methamphetamine-distributi",
            "2024-06-18_justice-gov_southern-california-woman-pleads-guilty-to-fentanyl-distribution-and-money-laund",
            "2019-04-02_justice-gov_three-l-a-residents-charged-in-darknet-drug-ring-that-allegedly-shipped-methamph",
            "2020-07-15_justice-gov_los-angeles-county-woman-pleads-guilty-to-conspiring-to-distribute-heroin-metham",
        ],
    },
    "operation-six-indicted-as-part-of-whatcom-county-fentanyl-trafficking-organization": {
        "sources": [
            "2026-04-18_justice-gov_six-indicted-part-whatcom-county-fentanyl-trafficking-organization",
            "2023-04-20_justice-gov_six-indicted-as-part-of-whatcom-county-fentanyl-trafficking-organization",
            "2023-04-20_dea-gov_six-indicted-part-whatcom-county-fentanyl-trafficking-organization",
            "2024-07-15_dea-gov_member-fentanyl-trafficking-ring-sentenced-distributing-deadly-fentanyl",
            "2025-05-09_dea-gov_final-custody-defendant-whatcom-county-drug-trafficking-ring-sentenced-8-years-prison",
            "2021-02-23_justice-gov_three-allegedly-responsible-for-distributing-thousands-of-fentanyl-pills-in-what",
        ],
    },
    "operation-three-allegedly-responsible-for-distributing-thousands-of-fentanyl-pills-in-whatcom-county-indicted-for-drug-d": {
        "sources": [
            "2026-04-18_justice-gov_three-allegedly-responsible-distributing-thousands-fentanyl-pills-whatcom-county",
            "2021-02-23_justice-gov_three-allegedly-responsible-for-distributing-thousands-of-fentanyl-pills-in-what",
            "2023-04-20_justice-gov_six-indicted-as-part-of-whatcom-county-fentanyl-trafficking-organization",
            "2023-04-20_dea-gov_six-indicted-part-whatcom-county-fentanyl-trafficking-organization",
            "2024-07-15_dea-gov_member-fentanyl-trafficking-ring-sentenced-distributing-deadly-fentanyl",
            "2025-05-09_dea-gov_final-custody-defendant-whatcom-county-drug-trafficking-ring-sentenced-8-years-prison",
        ],
    },
    "operation-member-of-lummi-nation-indicted-for-distributing-fentanyl": {
        "sources": [
            "2026-04-18_justice-gov_member-lummi-nation-indicted-distributing-fentanyl",
            "2026-02-12_fbi-gov_member-of-lummi-nation-indicted-for-distributing-fentanyl",
            "2023-04-20_justice-gov_six-indicted-as-part-of-whatcom-county-fentanyl-trafficking-organization",
            "2024-07-15_dea-gov_member-fentanyl-trafficking-ring-sentenced-distributing-deadly-fentanyl",
            "2025-05-09_dea-gov_final-custody-defendant-whatcom-county-drug-trafficking-ring-sentenced-8-years-prison",
        ],
    },
}


def wikilink_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        return text[2:-2].split("|", 1)[0].strip()
    return text


def ensure_wikilink(slug: str) -> str:
    return f"[[{slug}]]"


def normalize_url(url: str) -> str:
    parts = urlsplit(str(url or "").strip())
    if not parts.scheme or not parts.netloc:
        return ""
    return f"{parts.scheme}://{parts.netloc}{parts.path}"


def parse_source_slugs(meta: dict[str, Any]) -> list[str]:
    values = meta.get("sources") or []
    if isinstance(values, str):
        values = [values]
    out: list[str] = []
    for value in values:
        slug = wikilink_slug(value)
        if slug:
            out.append(slug)
    return out


def source_meta(slug: str) -> dict[str, Any]:
    return dict(frontmatter.load(SOURCES_DIR / f"{slug}.md").metadata)


def dedupe_source_slugs(source_slugs: list[str]) -> list[str]:
    seen_slugs: set[str] = set()
    seen_urls: set[str] = set()
    out: list[str] = []
    for slug in source_slugs:
        if not slug or slug in seen_slugs:
            continue
        path = SOURCES_DIR / f"{slug}.md"
        if not path.exists():
            continue
        meta = source_meta(slug)
        url = normalize_url(meta.get("collection_url") or meta.get("source_url") or "")
        if url and url in seen_urls:
            continue
        seen_slugs.add(slug)
        if url:
            seen_urls.add(url)
        out.append(slug)
    return out


def build_references_table(source_slugs: list[str]) -> str:
    lines = [
        "## References",
        "",
        "| # | Title | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    for idx, slug in enumerate(source_slugs, start=1):
        meta = source_meta(slug)
        title = str(meta.get("title") or slug).replace("|", " ")
        publisher = str(meta.get("publisher") or "Unknown").replace("|", " ")
        date = str(meta.get("publish_date") or "Unknown").replace("|", " ")
        url = str(meta.get("collection_url") or meta.get("source_url") or "").replace("|", "%7C")
        lines.append(f"| [{idx}] | {title} | {publisher} | {date} | {url} |")
    return "\n".join(lines) + "\n"


def replace_references_section(content: str, table: str) -> str:
    marker = "\n## References"
    idx = content.find(marker)
    if idx != -1:
        return content[:idx].rstrip() + "\n\n" + table.rstrip() + "\n"
    if content.startswith("## References"):
        return table.rstrip() + "\n"
    pattern = re.compile(r"\n## References\s*$.*", re.DOTALL)
    if pattern.search(content):
        return pattern.sub("\n" + table.rstrip() + "\n", content).rstrip() + "\n"
    return content.rstrip() + "\n\n" + table


def main() -> None:
    updated = 0
    reached_five = 0

    for slug, patch in CURATED.items():
        op_path = OPS_DIR / f"{slug}.md"
        if not op_path.exists():
            continue

        post = frontmatter.load(op_path)
        meta = post.metadata
        before_count = int(meta.get("source_count") or 0)
        before_sources = list(meta.get("sources") or [])
        before_content = post.content

        combined = dedupe_source_slugs(parse_source_slugs(meta) + list(patch["sources"]))
        if "title" in patch:
            meta["title"] = patch["title"]
        if "alias" in patch:
            meta["aliases"] = [patch["alias"]]
        meta["sources"] = [ensure_wikilink(item) for item in combined]
        meta["source_count"] = len(combined)
        meta["updated"] = TODAY
        post.content = replace_references_section(post.content, build_references_table(combined))

        if (
            before_count != meta["source_count"]
            or before_sources != meta["sources"]
            or before_content != post.content
            or ("title" in patch and meta.get("title") != patch["title"])
        ):
            op_path.write_text(frontmatter.dumps(post), encoding="utf-8")
            updated += 1
            if before_count < 5 and len(combined) >= 5:
                reached_five += 1
            print(f"{slug}: {before_count} -> {len(combined)}")

    print(f"UPDATED {updated}")
    print(f"REACHED_FIVE {reached_five}")


if __name__ == "__main__":
    main()
