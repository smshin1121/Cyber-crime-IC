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
    },    "operation-alleged-russian-cryptocurrency-money-launderer-extradited-to-united-states": {
        "sources": [
            "2026-04-18_justice-gov_alleged-russian-cryptocurrency-money-launderer-extradited-united-states",
            "2022-08-05_irs_alleged-russian-cryptocurrency-money-launderer-extradited-united-states",
            "2022-08-06_cbsnews_alleged-russian-crypto-crime-boss-alexander-vinnik-extradited-to-san-francisco",
            "2022-08-04_cnn_russian-accused-money-laundering-running-4b-bitcoin-exchange-extradited-us",
            "2022-08-05_moscowtimes_russian-bitcoin-suspect-extradited-to-us-from-france",
        ],
    },
    "operation-estonian-national-extradited-from-estonia-to-face-charges-of-illegal-procurement-of-u-s-electronics": {
        "sources": [
            "2026-04-18_justice-gov_estonian-national-extradited-estonia-face-charges-illegal-procurement-us-electronics",
            "2019-03-21_err_us-court-charges-two-men-of-smuggling-microchips-to-russia-via-estonia",
            "2019-03-21_cbsnews_man-accused-of-smuggling-electronics-russia-charges-san-francisco",
            "2019-07-18_winston-strawn_september-2017-indictment-alleges-charges-of-illegal-procurement-of-us-electronics",
            "2019-03-22_freightwaves_indictment-prison-time-for-illicit-us-exports",
        ],
    },
    "operation-florida-computer-programmer-arrested-for-hacking": {
        "sources": [
            "2026-04-18_justice-gov_florida-computer-programmer-arrested-hacking",
            "2016-09-02_helpnetsecurity_programmer-arrested-for-hacking-linux-kernel-organization",
            "2016-09-02_ktvu_florida-man-arrested-for-hacking-into-bay-area-computer-servers",
            "2016-09-03_fossbytes_27-year-old-programmer-arrested-for-hacking-linux-kernel-website",
            "2016-09-03_ibtimesuk_cops-arrest-florida-man-accused-hacking-linux-servers-2011",
        ],
    },
    "operation-former-employee-of-silicon-valley-company-pleads-guilty-to-damaging-ex-employers-computers": {
        "sources": [
            "2026-04-18_justice-gov_former-employee-silicon-valley-company-pleads-guilty-damaging-ex-employer-s-computers",
            "2016-06-09_theregister_sysadmin-fesses-up-to-wrecking-his-former-employers-it-systems",
            "2016-06-11_patch_former-agilent-employee-pleads-guilty-to-software-damage",
            "2016-06-12_techworm_developer-wrecks-his-companies-it-system-because-he-was-laid-off",
            "2016-06-08_databreachesnet_former-agilent-technologies-employee-pleads-guilty-to-damaging-ex-employers-computers",
        ],
    },
    "operation-international-hacker-for-hire-who-conspired-with-and-aided-russian-fsb-officers-sentenced-to-five-years-in-pri": {
        "sources": [
            "2026-04-18_justice-gov_international-hacker-hire-who-conspired-and-aided-russian-fsb-officers-sentenced-five",
            "2018-05-29_techcrunch_canadian-yahoo-hacker-gets-a-five-year-prison-sentence",
            "2018-05-30_engadget_attacker-involved-in-2014-yahoo-hack-gets-five-years-in-prison",
            "2018-05-30_bankinfosecurity_canadian-hacker-jailed-for-5-years-following-yahoo-breach",
            "2018-05-30_pymnts_yahoo-hacker-sentenced-to-five-years",
        ],
    },
    "operation-mountain-view-resident-charged-with-production-of-child-pornography-and-cyberstalking": {
        "sources": [
            "2026-04-18_justice-gov_mountain-view-resident-charged-production-child-pornography-and-cyberstalking",
            "2019-01-29_usss_secret-service-san-francisco-electronic-crimes-task-force-investigation-leads-186-month",
            "2017-05-26_patch_federal-child-porn-production-distribution-charges-filed-against-mountain-view-man",
            "2019-01-31_mountainviewvoice_mountain-view-man-sentenced-to-15-years-on-child-porn-charges",
            "2019-01-29_patch_mountain-view-man-convicted-of-child-porn-sentenced-to-15-years",
        ],
    },
    "operation-russian-hacker-sentenced-to-over-7-years-in-prison-for-hacking-into-three-bay-area-tech-companies": {
        "sources": [
            "2026-04-18_justice-gov_russian-hacker-sentenced-over-7-years-prison-hacking-three-bay-area-tech-companies",
            "2020-09-30_theregister_russian-hacker-described-as-brilliant-by-judge-gets-seven-years-linkedin-dropbox",
            "2020-09-30_cbsnews_russian-hacker-who-targeted-bay-area-tech-companies-sentenced-to-over-7-years-in-prison",
            "2020-09-29_therecord_russian-hacker-nikulin-sentenced-to-over-7-years-in-prison-for-tech-industry-breaches",
            "2020-09-30_bankinfosecurity_russian-gets-7-year-sentence-for-hacking-linkedin-dropbox",
        ],
    },
    "operation-russian-man-found-guilty-of-hacking-into-three-bay-area-tech-companies": {
        "sources": [
            "2026-04-18_justice-gov_russian-man-found-guilty-hacking-three-bay-area-tech-companies",
            "2020-07-14_theregister_guilty-russian-miscreant-who-hacked-linkedin-dropbox-formspring",
            "2020-07-11_engadget_us-court-finds-russian-national-guilty-of-hacking-linkedin-dropbox",
            "2020-07-11_securityaffairs_yevgeniy-nikulin-russian-hacker-behind-dropbox-and-linkedin-hacks-found-guilty",
            "2021-12-23_infosecurity_russian-hackers-1-7m-restitution-order-overturned",
        ],
    },
    "operation-russian-national-and-bitcoin-exchange-charged-in-21-count-indictment-for-operating-alleged-international-money": {
        "sources": [
            "2026-04-18_justice-gov_russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged",
            "2017-07-26_fdic-oig_russian-national-and-bitcoin-exchange-charged-21-count-indictment",
            "2017-07-27_lawfare_btc-e-indictment-major-blow-against-online-criminal-activity",
            "2017-07-27_occrp_us-indicts-russian-suspected-of-laundering-us4-billion-for-criminals",
            "2017-07-27_cyberscoop_fincen-fines-btc-e-110-million-for-violating-anti-money-laundering-laws",
        ],
    },
    "operation-russian-nationals-charged-with-hacking-one-cryptocurrency-exchange-and-illicitly-operating-another": {
        "sources": [
            "2026-04-18_justice-gov_russian-nationals-charged-hacking-one-cryptocurrency-exchange-and-illicitly-operating",
            "2023-06-09_usss_russian-nationals-charged-hacking-one-cryptocurrency-exchange-and",
            "2023-06-09_techcrunch_us-doj-charges-two-russians-for-hacking-crypto-exchange-mt-gox",
            "2023-06-09_therecord_russian-nationals-accused-of-mt-gox-bitcoin-heist-shifting-stolen-funds-to-btc-e",
            "2023-06-09_cyberscoop_doj-charges-two-russian-nationals-with-historic-mt-gox-hack",
        ],
    },
    "operation-san-francisco-man-sentenced-to-100-months-imprisonment-in-credit-card-fraud-and-identity-theft-case": {
        "sources": [
            "2026-04-18_justice-gov_san-francisco-man-sentenced-100-months-imprisonment-credit-card-fraud-and-identity",
            "2020-10-08_usss_san-francisco-man-sentenced-to-100-months-imprisonment-credit-card-fraud-and",
            "2020-10-10_patch_sf-man-who-funded-fancy-trips-stolen-credit-cards-sentenced",
            "2020-10-10_cbsnews_san-francisco-man-sentenced-to-prison-for-using-stolen-credit-cards-to-fund-lavish-vacations",
            "2020-10-10_thesfnews_marcus-felder-serving-prison-time-for-credit-card-fraud",
        ],
    },
    "operation-san-francisco-resident-sentenced-to-seven-years-in-prison-for-stealing-prisoner-identities-and-filing-fraudule": {
        "sources": [
            "2026-04-18_justice-gov_san-francisco-resident-sentenced-seven-years-prison-stealing-prisoner-identities-and",
            "2017-05-24_doj-opa_california-man-sentenced-prison-stealing-prisoner-identities-and-filing-fraudulent-tax",
            "2017-05-24_patch_former-san-quentin-inmate-sentenced-in-tax-scheme",
            "2017-01-24_cbsnews_former-marin-county-man-convicted-of-tax-fraud-using-inmates-identities",
            "2017-01-24_doj-ndca_former-marin-county-resident-convicted-using-prisoner-identities",
        ],
    },
    "operation-san-jose-man-pleads-guilty-to-damaging-ciscos-network": {
        "sources": [
            "2026-04-18_justice-gov_san-jose-man-pleads-guilty-damaging-cisco-s-network",
            "2020-08-26_theregister_engineer-admits-he-wiped-456-cisco-webex-vms-from-aws-after-leaving-the-biz",
            "2020-08-29_govinfosecurity_ex-cisco-engineer-pleads-guilty-in-insider-threat-case",
            "2020-08-27_itpro_ex-cisco-engineer-charged-with-wiping-webex-teams-accounts",
            "2020-12-11_bleepingcomputer_ex-cisco-engineer-who-nuked-16k-webex-accounts-goes-to-prison",
        ],
    },
    "operation-sanford-spam-king-wallace-sentenced-to-two-and-a-half-years-in-custody-for-spamming-facebook-users": {
        "sources": [
            "2026-04-18_justice-gov_sanford-spam-king-wallace-sentenced-two-and-half-years-custody-spamming-facebook-users",
            "2016-06-16_fortune_spam-king-sanford-wallace-gets-30-months-in-prison",
            "2016-06-15_theregister_spam-king-sent-down-for-30-months",
            "2016-06-16_csmonitor_why-self-proclaimed-spam-king-got-30-months-in-prison-for-facebook-hack",
            "2016-06-15_siliconangle_facebook-spammer-sanford-spam-king-wallace-given-30-months-in-jail",
        ],
    },
    "operation-former-owner-of-t-mobile-retail-store-in-eagle-rock-found-guilty-of-committing-25-million-scheme-to-illegally-": {
        "sources": [
            "2026-04-18_justice-gov_former-owner-t-mobile-retail-store-eagle-rock-found-guilty-committing-25-million-scheme",
            "2022-08-01_irs-gov_former-owner-t-mobile-retail-store-eagle-rock-25-million-unlock-scheme",
            "2022-08-03_abc7_former-eagle-rock-t-mobile-store-owner-found-guilty-25-million-unlock-scheme",
            "2022-12-18_bleepingcomputer_t-mobile-hacker-gets-10-years-25-million-phone-unlock-scheme",
            "2022-08-03_9to5mac_unlocking-t-mobile-25-million-scheme-conviction",
        ],
    },
    "operation-illinois-man-sentenced-2-years-federal-prison-operating-subscription-based-computer": {
        "sources": [
            "2026-04-18_justice-gov_illinois-man-sentenced-2-years-federal-prison-operating-subscription-based-computer",
            "2022-06-13_krebsonsecurity_downthem-ddos-for-hire-boss-gets-2-years-in-prison",
            "2022-06-14_bleepingcomputer_owner-of-downthem-ddos-service-gets-2-years-in-prison",
            "2022-06-14_therecord_illinois-man-behind-ddos-attack-service-given-2-year-prison-sentence",
            "2022-06-14_securityweek_operator-downthem-ddos-service-sentenced-24-months-prison",
        ],
    },
    "operation-international-money-launderer-sentenced-to-over-11-years-in-federal-prison-for-laundering-millions-from-cyber-": {
        "sources": [
            "2026-04-18_justice-gov_international-money-launderer-sentenced-over-11-years-federal-prison-laundering",
            "2021-09-09_bankinfosecurity_cybercrime-money-launderer-handed-11-year-sentence",
            "2021-09-09_cyberscoop_north-korean-money-laundering-case-alaumary",
            "2021-09-09_engadget_us-canadian-11-years-laundering-money-north-korean-hacking-group",
            "2021-09-10_securityaffairs_money-launderer-sentenced",
        ],
    },
    "operation-justice-dept-seizes-over-112m-in-funds-linked-to-cryptocurrency-investment-schemes-with-over-half-seized-in-lo": {
        "sources": [
            "2026-04-18_justice-gov_justice-dept-seizes-over-112m-funds-linked-cryptocurrency-investment-schemes-over-half",
            "2023-04-03_therecord_pig-butchering-cryptocurrency-scams-doj-seizes-112-million",
            "2023-04-04_bankinfosecurity_us-doj-seizes-112m-linked-pig-butchering-scams",
            "2023-04-04_helpnetsecurity_doj-cracks-down-on-cryptocurrency-fraud",
            "2023-04-03_trmlabs_doj-fbi-phoenix-crypto-seizure-112m",
        ],
    },
    "operation-marine-based-at-camp-pendleton-arrested-on-federal-charges-alleging-cyberstalking-of-young-women-in-sextortion": {
        "sources": [
            "2026-04-18_justice-gov_marine-based-camp-pendleton-arrested-federal-charges-alleging-cyberstalking-young-women",
            "2022-02-09_timesofsandiego_camp-pendleton-marine-arrested-federal-cyberstalking-charge",
            "2022-02-09_kpbs_marine-camp-pendleton-arrested-federal-cyberstalking-charge",
            "2022-05-28_abc7_johao-chavarri-camp-pendleton-marine-cyberstalking-pleads-guilty",
            "2022-09-16_nbcsandiego_camp-pendleton-marine-sentenced-sextortion-campaign",
        ],
    },
    "operation-o-c-man-admits-operating-unlicensed-atm-network-that-laundered-millions-of-dollars-of-bitcoin-and-cash-for-cri": {
        "sources": [
            "2026-04-18_justice-gov_oc-man-admits-operating-unlicensed-atm-network-laundered-millions-dollars-bitcoin-and",
            "2020-07-22_cbsnews-losangeles_yorba-linda-man-plea-deal-unlicense-bitcoin-network",
            "2020-07-23_atmmarketplace_superman29-pleads-guilty-laundering-millions-bitcoin-atms",
            "2020-07-24_blockchain-bakermckenzie_superman-29-laundering-millions-bitcoin",
            "2021-06-07_wilsontaxlaw_oc-man-sentenced-2-years-prison-laundering-bitcoin",
        ],
    },
    "operation-orange-county-man-arrested-on-federal-stalking-charge-alleging-multiyear-harassment-campaign-against-prominent": {
        "sources": [
            "2026-04-18_justice-gov_orange-county-man-arrested-federal-stalking-charge-alleging-multiyear-harassment",
            "2022-05-24_kfiam640_orange-county-man-charged-stalking-pro-gamer",
            "2022-05-26_newsantaana_oc-man-arrested-cyber-stalking-pro-gamer-and-her-family",
            "2023-07-13_newsantaana_oc-man-only-two-years-prison-stalking-female-online-gamer",
            "2023-07-13_californiainsider_orange-county-man-stalked-online-gamer-2-years",
        ],
    },
    "operation-orange-county-man-pleads-guilty-stalking-charge-harassment-campaign-against": {
        "sources": [
            "2026-04-18_justice-gov_orange-county-man-pleads-guilty-stalking-charge-harassment-campaign-against",
            "2022-05-24_kfiam640_orange-county-man-charged-stalking-pro-gamer",
            "2022-05-26_newsantaana_oc-man-arrested-cyber-stalking-pro-gamer-and-her-family",
            "2023-07-13_newsantaana_oc-man-only-two-years-prison-stalking-female-online-gamer",
            "2023-07-13_californiainsider_orange-county-man-stalked-online-gamer-2-years",
        ],
    },
    "operation-orange-county-man-pleads-guilty-to-stalking-charge-for-harassment-campaign-against-professional-online-gamer": {
        "sources": [
            "2026-04-18_justice-gov_orange-county-man-pleads-guilty-stalking-charge-harassment-campaign-against",
            "2022-05-24_kfiam640_orange-county-man-charged-stalking-pro-gamer",
            "2022-05-26_newsantaana_oc-man-arrested-cyber-stalking-pro-gamer-and-her-family",
            "2023-07-13_newsantaana_oc-man-only-two-years-prison-stalking-female-online-gamer",
            "2023-07-13_californiainsider_orange-county-man-stalked-online-gamer-2-years",
        ],
    },
    "operation-pasadena-man-who-cyberstalked-and-made-threats-to-injure-rape-and-kill-sentenced-to-more-than-3-years-in-feder": {
        "sources": [
            "2026-04-18_justice-gov_pasadena-man-who-cyberstalked-and-made-threats-injure-rape-and-kill-sentenced-more-3",
            "2021-11-15_mynewsla_pasadena-man-sentenced-over-3-years-prison-cyberstalking",
            "2021-11-15_patch_pasadena-man-3-years-prison-online-threats",
            "2021-11-16_cbsnews-losangeles_samuel-hughes-pasadena-3-years-online-threats-women",
            "2021-11-16_audacy-knxnews_pasadena-man-sentenced-3-years-cyberstalking",
        ],
    },
    "operation-san-gabriel-valley-man-admits-cyberstalking-two-teenage-girls": {
        "sources": [
            "2026-04-18_justice-gov_san-gabriel-valley-man-admits-cyberstalking-two-teenage-girls",
            "2020-04-21_nbclosangeles_covina-man-accused-cyberstalking-teenage-girls",
            "2020-04-21_mynewsla_covina-man-arrested-allegedly-cyberstalking-teenage-girls",
            "2020-04-28_mynewsla_judge-denies-pretrial-release-covina-cyberstalking",
            "2021-04-15_infosecurity-magazine_us-imprisons-sadistic-sextortionist",
        ],
    },
    "operation-san-gabriel-valley-man-admits-to-cyberstalking-two-teenage-girls": {
        "sources": [
            "2026-04-18_justice-gov_san-gabriel-valley-man-admits-cyberstalking-two-teenage-girls",
            "2020-04-21_nbclosangeles_covina-man-accused-cyberstalking-teenage-girls",
            "2020-04-21_mynewsla_covina-man-arrested-allegedly-cyberstalking-teenage-girls",
            "2020-04-28_mynewsla_judge-denies-pretrial-release-covina-cyberstalking",
            "2021-04-15_infosecurity-magazine_us-imprisons-sadistic-sextortionist",
        ],
    },
    "operation-san-gabriel-valley-man-sentenced-to-more-than-4-years-in-federal-prison-for-role-in-36-9-million-global-digita": {
        "sources": [
            "2026-04-18_justice-gov_san-gabriel-valley-man-sentenced-more-4-years-federal-prison-role-369-million-global",
            "2025-09-08_hoodline_san-gabriel-valley-man-sentenced-369-million-international-digital-asset-scam",
            "2025-09-08_mynewsla_sgv-man-sentenced-prison-369m-digital-investment-scam",
            "2025-09-08_thefederalnewswire_san-gabriel-valley-man-sentenced-international-crypto-scam",
            "2025-09-09_yahoo-finance_california-man-51-months-cambodia-crypto-scam",
        ],
    },
    "operation-santa-clarita-man-found-guilty-of-producing-child-pornography": {
        "sources": [
            "2026-04-18_justice-gov_santa-clarita-man-found-guilty-producing-child-pornography",
            "2023-05-22_mynewsla_santa-clarita-man-found-guilty-producing-child-pornography",
            "2023-05-23_hometownstation_canyon-country-man-found-guilty-producing-possessing-child-pornography",
            "2023-08-25_ktla_former-socal-navy-seal-sentenced-filming-minors-hidden-cameras",
            "2024-03-21_californiachildsexualabuseattorney_santa-clarita-man-sentenced-20-years",
        ],
    },
    "operation-socal-man-arrested-on-federal-charges-alleging-he-schemed-to-advertise-and-sell-hive-computer-intrusion-malwar": {
        "sources": [
            "2026-04-18_justice-gov_socal-man-arrested-federal-charges-alleging-he-schemed-advertise-and-sell-hive",
            "2024-04-11_hoodline_san-fernando-valley-man-indicted-selling-hive-malware",
            "2024-04-13_bleepingcomputer_firebird-rat-creator-seller-arrested-us-australia",
            "2024-04-15_securityweek_two-people-arrested-australia-us-development-sale-hive-rat",
            "2024-04-15_hackread_fbi-afp-arrest-developer-firebird-hive-rat",
        ],
    },
    "operation-texas-man-sentenced-to-9-months-in-federal-prison-for-operating-website-that-offered-computer-attack-services": {
        "sources": [
            "2024-07-15_justice-gov_united-states-v-jeremiah-sam-evans-miller",
            "2024-02-16_therecord_astrostress-booter-service-ddos-for-hire-charges-filed",
            "2024-07-18_cyberinsider_astrostress-operator-prison-sentence-thousands-ddos-attacks",
            "2024-07-22_cybersecuritynews_authorities-arrested-ddos-attack-service-provider",
            "2024-07-24_hackerdose_texas-man-jailed-ddos-attack-website",
        ],
    },
    "operation-two-southern-california-men-who-supplied-fentanyl-sold-to-darknet-customers-in-all-50-states-sentenced-to-fede": {
        "sources": [
            "2025-01-13_cdca_ruiz-navia-darknet-sentencing",
            "2023-11-07_foxla_2-socal-men-charged-darknet-drugs-50-states",
            "2023-11-07_kesq_two-socal-men-charged-darknet-124k-fentanyl-laced-pills",
            "2025-01-13_mynewsla_two-men-sentenced-15-17-years-fentanyl-dealing",
            "2025-01-14_hoodline_two-southern-california-men-sentenced-fentanyl-dark-web",
        ],
    },
    "operation-us-v-adan-ruiz-and-omar-navia": {
        "sources": [
            "2025-01-13_justice-gov_united-states-v-adan-ruiz-and-omar-navia",
            "2023-11-07_foxla_2-socal-men-charged-darknet-drugs-50-states",
            "2023-11-07_kesq_two-socal-men-charged-darknet-124k-fentanyl-laced-pills",
            "2025-01-13_mynewsla_two-men-sentenced-15-17-years-fentanyl-dealing",
            "2025-01-14_hoodline_two-southern-california-men-sentenced-fentanyl-dark-web",
        ],
    },
    "operation-two-sudanese-nationals-indicted-for-alleged-role-in-anonymous-sudan-cyberattacks-on-hospitals-government-facil": {
        "sources": [
            "2026-04-18_justice-gov_two-sudanese-nationals-indicted-alleged-role-anonymous-sudan-cyberattacks-hospitals",
            "2024-10-16_therecord_anonymous-sudan-brothers-charged-ddos-attacks-hospital-critical-infrastructure",
            "2024-10-16_cbsnews_2-sudanese-brothers-charged-cyber-attack-for-hire-gang",
            "2024-10-17_krebsonsecurity_sudanese-brothers-arrested-anonsudan-takedown",
            "2024-10-17_theregister_two-alleged-operators-anonymous-sudan-named-charged",
        ],
    },
    "operation-us-v-ahmed-salah-yousif-omer-and-alaa-salah-yusuuf-omer": {
        "sources": [
            "2026-04-18_justice-gov_two-sudanese-nationals-indicted-alleged-role-anonymous-sudan-cyberattacks-hospitals",
            "2024-10-16_therecord_anonymous-sudan-brothers-charged-ddos-attacks-hospital-critical-infrastructure",
            "2024-10-16_cbsnews_2-sudanese-brothers-charged-cyber-attack-for-hire-gang",
            "2024-10-17_krebsonsecurity_sudanese-brothers-arrested-anonsudan-takedown",
            "2024-10-17_theregister_two-alleged-operators-anonymous-sudan-named-charged",
        ],
    },
    "operation-us-v-aleksandr-stepanov-and-artem-aleksandrovich-kalinkin": {
        "sources": [
            "2026-04-18_justice-gov_16-defendants-federally-charged-connection-danabot-malware-scheme-infected-computers",
            "2025-05-22_intel471_danabot-malware-disrupted-threat-actors-named",
            "2025-05-22_crowdstrike_partners-doj-disrupt-danabot-malware-operators",
            "2025-05-23_helpnetsecurity_operation-endgame-danabot-botnet-disrupted-qakbot-leader",
            "2025-05-23_bitdefender_16-charged-danabot-malware-russia",
        ],
    },
    "operation-us-v-alex-scott-roberts": {
        "sources": [
            "2026-04-18_justice-gov_chatsworth-man-sentenced-more-7-years-prison-cyberstalking-campaigns-against-victims",
            "2020-11-09_patch_chatsworth-man-accused-cyberstalking-two-sisters",
            "2023-02-24_mynewsla_chatsworth-man-faces-sentencing-stalking-cases",
            "2023-02-27_wrdw_man-7-years-cyberstalking-california-georgia",
            "2023-02-27_wdef_chatsworth-man-sentenced-7-years-prison-cyberstalking",
        ],
    },
    "operation-us-v-amir-hossein-golshan": {
        "sources": [
            "2026-04-18_justice-gov_alleged-sim-swapper-charged-hacking-instagram-influencers-accounts-get-money-and",
            "2023-02-13_vice_sim-swapper-amir-golshan-instagram-influencers-dates",
            "2023-11-28_theregister_serial-cybercriminal-scammer-sentenced",
            "2023-11-29_bleepingcomputer_sim-swapper-8-years-prison-account-hacks-crypto-theft",
            "2023-12-04_bitdefender_la-man-sentenced-eight-years-prison-sim-swapping",
        ],
    },
    "operation-deepdotweb-administrator-pleads-guilty-money-laundering-conspiracy": {
        "sources": [
            "2026-04-18_justice-gov_deepdotweb-administrator-pleads-guilty-money-laundering-conspiracy",
            "2021-03-31_cyberscoop_deepdotweb-boss-pleads-guilty-to-laundering-millions",
            "2022-01-26_cyberscoop_co-operator-of-deepdotweb-sentenced-to-more-than-8-years-for-money-laundering",
            "2022-01-28_bankinfosecurity_darknet-market-search-engine-operator-gets-8-year-sentence",
            "2026-03-21_wikipedia_deepdotweb",
        ],
    },
    "operation-euclid-ohio-man-pleads-guilty-distribution-fentanyl-he-ordered-china-and-sold": {
        "sources": [
            "2026-04-18_justice-gov_euclid-ohio-man-pleads-guilty-distribution-fentanyl-he-ordered-china-and-sold",
            "2018-04-03_cbsnews_its-easy-to-buy-opioids-on-the-so-called-darknet-fbi-says",
            "2018-08-13_triblive_ohio-man-accused-of-buying-fentanyl-from-china-selling-it-on-the-dark-web",
            "2018-08-15_patch_fentanyl-dark-web-and-china-how-a-euclid-man-built-a-drug-ring",
            "2018-03-28_13abc_ohio-man-charged-with-selling-fentanyl-ordered-from-china",
        ],
    },
    "operation-fayette-county-man-admits-making-hoax-emergency-phone-calls-to-elicit-an-armed-police-response-practice-is-kno": {
        "sources": [
            "2026-04-18_justice-gov_fayette-county-man-admits-making-hoax-emergency-phone-calls-elicit-armed-police",
            "2019-09-11_cbspittsburgh_fayette-county-man-pleads-guilty-to-making-hoax-emergency-calls",
            "2019-09-11_postgazette_swatting-hoax-guilty-plea-pittsburgh-online-gaming",
            "2019-09-12_triblive_fayette-county-man-pleads-guilty-in-florida-swatting-incident-after-online-gaming-dispute",
            "2019-09-13_dexerto_gamer-confesses-swatting-online-opponent-pleads-guilty",
        ],
    },
    "operation-greene-county-man-indicted-cyberstalking-and-interstate-threats": {
        "sources": [
            "2026-04-18_justice-gov_greene-county-man-indicted-cyberstalking-and-interstate-threats",
            "2022-03-23_cbspittsburgh_greene-co-man-pleads-guilty-to-federal-cyberstalking-charges",
            "2021-01-27_pacer_usa-v-levicky-2-21-cr-00019-pawd",
            "2022-08-05_justice-gov_carmichaels-man-sentenced-3-years-cyberstalking",
            "2022-08-05_shorenewsnetwork_carmichaels-man-sentenced-to-3-years-for-cyberstalking",
        ],
    },
    "operation-moldovan-botnet-operator-indicted-for-role-in-conspiracy-to-unlawfully-access-thousands-of-infected-computers-": {
        "sources": [
            "2026-04-18_justice-gov_moldovan-botnet-operator-indicted-role-conspiracy-unlawfully-access-thousands-infected",
            "2024-04-17_bleepingcomputer_moldovan-charged-for-operating-botnet-used-to-push-ransomware",
            "2024-04-17_cyberinsider_botnet-operator-charged-with-major-cyber-crimes-in-the-us",
            "2024-04-16_secretservice_moldovan-botnet-operator-indicted-role-conspiracy",
            "2024-04-16_fbi_alexander-lefterov-most-wanted-cyber",
        ],
    },
    "operation-moldovan-sentenced-for-distributing-multifunction-malware-package": {
        "sources": [
            "2018-12-06_justice-gov_moldovan-sentenced-for-distributing-multifunction-malware-package",
            "2018-12-06_postgazette_moldova-andrey-ghinkul-smilex-sentenced-time-served-bugat-malware-case-deported",
            "2018-12-06_triblive_moldova-man-sentenced-in-federal-court-in-pittsburgh-cyber-conspiracy-that-stole-millions",
            "2015-10-13_fbi-pittsburgh_bugat-botnet-administrator-arrested-and-malware-disabled",
            "2018-12-10_scmagazine_moldovian-sentenced-for-stealing-millions-using-bugat-banking-malware",
        ],
    },
    "operation-new-jersey-man-sentenced-to-prison-after-pleading-guilty-to-posting-restricted-information-to-social-media": {
        "sources": [
            "2026-04-18_justice-gov_new-jersey-man-sentenced-prison-after-pleading-guilty-posting-restricted-information",
            "2021-08-03_newsweek_new-jersey-man-gets-16-months-doxxing-federal-judge",
            "2021-08-03_patch_paramus-man-sentenced-pa-threatening-federal-judge",
            "2021-08-03_abajournal_new-jersey-man-gets-prison-time-for-posting-federal-judges-home-address",
            "2021-08-02_postgazette_william-kaetz-paramus-nj-judge-ranjan-sentenced-16-months",
        ],
    },
    "operation-one-defendant-sentenced-to-prison-and-another-ordered-detained-pretrial-this-week-in-separate-cyberstalking-ca": {
        "sources": [
            "2026-04-18_justice-gov_one-defendant-sentenced-prison-and-another-ordered-detained-pretrial-week-separate",
            "2024-02-05_observerreporter_washington-man-sentenced-to-prison-after-pleading-guilty-to-federal-cyberstalking-charge",
            "2024-02-02_yahoo_washington-man-sentenced-cyberstalking-ex",
            "2022-07-15_justice-gov_washington-pa-man-charged-cyberstalking",
            "2022-07-16_observerreporter_washington-man-facing-federal-cyberstalking-charges",
        ],
    },
    "operation-pittsburgh-man-charged-threatening-communications-and-impeding-fbi-investigation-1": {
        "sources": [
            "2026-04-18_justice-gov_pittsburgh-man-charged-threatening-communications-and-impeding-fbi-investigation-1",
            "2021-01-07_triblive_feds-former-pitt-student-threatened-fbi-agents-celebrated-attacks-on-us",
            "2021-01-08_hstoday_pittsburgh-man-accused-of-threatening-surveilling-fbi-headquarters-in-dc",
            "2021-01-07_postgazette_khaled-miah-pittsburgh-charged-alleged-threats-fbi-agents",
            "2021-01-07_gwu-extremism_khaled-miah-affidavit-criminal-complaint",
        ],
    },
    "operation-pittsburgh-man-charged-with-threatening-communications-and-impeding-fbi-investigation": {
        "sources": [
            "2026-04-18_justice-gov_pittsburgh-man-charged-threatening-communications-and-impeding-fbi-investigation-1",
            "2021-01-07_triblive_feds-former-pitt-student-threatened-fbi-agents-celebrated-attacks-on-us",
            "2021-01-08_hstoday_pittsburgh-man-accused-of-threatening-surveilling-fbi-headquarters-in-dc",
            "2021-01-07_postgazette_khaled-miah-pittsburgh-charged-alleged-threats-fbi-agents",
            "2021-01-07_gwu-extremism_khaled-miah-affidavit-criminal-complaint",
        ],
    },
    "operation-pittsburgh-man-indicted-on-cyberstalking-charge": {
        "sources": [
            "2026-04-18_justice-gov_pittsburgh-man-indicted-cyberstalking-charge",
            "2024-01-25_cbspittsburgh_pittsburgh-man-charged-cyberstalking-ex-girlfriend",
            "2024-01-25_yahoo_pittsburgh-man-federally-charged-cyberstalking",
            "2024-01-25_postgazette_scott-man-indicted-on-federal-cyberstalking-charge",
            "2024-02-02_justice-gov_one-defendant-sentenced-prison-and-another-ordered-detained-pretrial-week-separate",
        ],
    },
    "operation-pittsburgh-resident-and-darknet-drug-trafficker-sentenced-to-nearly-six-years-in-prison-on-federal-drug-traffi": {
        "sources": [
            "2025-05-12_wdpa_vlastos-darknet-sentencing",
            "2025-05-13_explorejeffersonpa_pa-resident-and-darknet-drug-trafficker-sentenced",
            "2025-05-12_legalnewsline_pittsburgh-man-sentenced-to-nearly-six-years-for-drug-trafficking-and-firearms-offenses",
            "2024-08-15_govinfo_usa-v-vlastos-2-24-cr-00214-pawd",
            "2025-05-12_justice-gov_pittsburgh-resident-and-darknet-drug-trafficker-sentenced-nearly-six-years-prison",
        ],
    },
    "operation-robinson-twp-man-pleads-guilty-in-international-investigation-into-darknet-sale-of-child-exploitation-videos-a": {
        "sources": [
            "2026-04-18_justice-gov_robinson-twp-man-pleads-guilty-international-investigation-darknet-sale-child",
            "2020-08-19_patch_robinson-man-pleads-guilty-to-child-pornography-charges",
            "2020-08-19_cbspittsburgh_robinson-man-guilty-child-porn-charges",
            "2020-08-19_postgazette_anthony-bellisario-robinson-pleads-guilty-darknet-child-pornography-investigation",
            "2021-10-12_justice-gov_suburban-pittsburgh-man-sentenced-7-years-prison-violating-child-sexual-exploitation",
        ],
    },
    "operation-russian-national-charged-in-hacking-scheme-targeting-pittsburgh-national-golf-course": {
        "sources": [
            "2026-04-18_justice-gov_russian-national-charged-hacking-scheme-targeting-pittsburgh-national-golf-course",
            "2018-11-29_cbspittsburgh_russian-man-charged-hacking-pittsburgh-national-golf-course",
            "2018-11-29_postgazette_russia-hacking-pittsburgh-national-golf-course-gibsonia-west-deer-ilya-kulkov",
            "2018-11-29_triblive_feds-russian-man-hacked-west-deer-golf-course-computer-to-shop-on-ebay",
            "2018-11-30_scmagazine_russian-national-charged-with-hacking-pittsburgh-golf-course-to-commit-fraud",
        ],
    },
    "operation-san-antonio-man-sentenced-for-january-2018-threats-made-against-players-and-fans-at-nfl-playoff-game-at-heinz-": {
        "sources": [
            "2026-04-18_justice-gov_san-antonio-man-sentenced-january-2018-threats-made-against-players-and-fans-nfl",
            "2018-11-27_cbspittsburgh_sentencing-man-threatens-kill-steelers-fans-players",
            "2018-01-14_cnn_mass-shooting-threat-pittsburgh-steelers-playoff-game",
            "2018-01-14_espn_man-arrested-terroristic-threat-jacksonville-jaguars-pittsburgh-steelers-game",
            "2018-11-27_wfmj_man-to-serve-18-months-for-shooting-threat-at-nfl-playoffs",
        ],
    },
    "operation-siemens-contract-employee-intentionally-damaged-computers-planting-logic-bombs-programs": {
        "sources": [
            "2026-04-18_justice-gov_siemens-contract-employee-intentionally-damaged-computers-planting-logic-bombs-programs",
            "2019-12-18_bleepingcomputer_siemens-contractor-jailed-for-sabotage-with-logic-bombs",
            "2019-06-25_theregister_thats-a-sticky-siemens-situation-former-coder-blows-his-logic-bomb",
            "2019-12-18_securityweek_former-siemens-contractor-sentenced-prison-planting-logic-bombs",
            "2019-12-17_postgazette_software-contractor-david-tinley-prison-logic-bombs-siemens-sabotage",
        ],
    },
    "operation-six-russian-gru-officers-charged-in-connection-with-worldwide-deployment-of-destructive-malware-and-other-disr": {
        "sources": [
            "2026-04-18_justice-gov_six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware",
            "2020-10-19_cyberscoop_us-charges-russian-gru-officers-for-notpetya-other-major-hacks",
            "2020-10-20_infosecuritymagazine_us-indicts-gru-officers-notpetya-olympics-attacks",
            "2020-10-19_bankinfosecurity_6-russians-indicted-for-notpetya-campaign-other-attacks",
            "2020-10-19_fbi_gru-hackers-destructive-malware-and-international-cyber-attacks",
        ],
    },
    "operation-south-carolina-man-charged-with-interstate-stalking-and-aggravated-id-theft-targeting-pennsylvania-resident": {
        "sources": [
            "2026-04-18_justice-gov_south-carolina-man-charged-interstate-stalking-and-aggravated-id-theft-targeting",
            "2018-08-14_postgazette_cyber-stalker-nathaniel-earl-dunlap-dakota-james-harassment-neighbor-federal-prison",
            "2017-07-28_triblive_dakota-james-impersonator-pleads-guilty-in-federal-court",
            "2018-08-14_rawstory_man-went-bizarre-lengths-harass-neighbor-suspected-black-friend",
            "2017-07-28_justice-gov_south-carolina-man-pleads-guilty-interstate-stalking-charge",
        ],
    },
    "operation-south-carolina-man-sentenced-to-30-months-in-prison-for-interstate-stalking": {
        "sources": [
            "2026-04-18_justice-gov_south-carolina-man-sentenced-30-months-prison-interstate-stalking",
            "2018-08-14_postgazette_cyber-stalker-nathaniel-earl-dunlap-dakota-james-harassment-neighbor-federal-prison",
            "2017-07-28_triblive_dakota-james-impersonator-pleads-guilty-in-federal-court",
            "2018-08-14_rawstory_man-went-bizarre-lengths-harass-neighbor-suspected-black-friend",
            "2017-07-28_justice-gov_south-carolina-man-pleads-guilty-interstate-stalking-charge",
        ],
    },
    "operation-three-members-of-goznym-cybercrime-network-sentenced-in-parallel-multi-national-prosecutions-in-pittsburgh-and": {
        "sources": [
            "2026-04-18_justice-gov_three-members-goznym-cybercrime-network-sentenced-parallel-multi-national-prosecutions",
            "2019-12-20_bleepingcomputer_goznym-gang-members-behind-100-million-damages-sentenced",
            "2019-12-20_cyberscoop_goznym-georgian-bulgarian-cybercriminals-sentenced-doj",
            "2019-12-23_securityweek_three-goznym-malware-operators-sentenced",
            "2019-12-20_postgazette_goznym-malware-leaders-pittsburgh-convicted-sentenced-prosecuted-country-georgia-europe",
        ],
    },
    "operation-us-v-anthony-bellisario": {
        "sources": [
            "2026-04-18_justice-gov_robinson-twp-man-pleads-guilty-international-investigation-darknet-sale-child",
            "2020-08-19_patch_robinson-man-pleads-guilty-to-child-pornography-charges",
            "2020-08-19_cbspittsburgh_robinson-man-guilty-child-porn-charges",
            "2020-08-19_postgazette_anthony-bellisario-robinson-pleads-guilty-darknet-child-pornography-investigation",
            "2021-10-12_justice-gov_suburban-pittsburgh-man-sentenced-7-years-prison-violating-child-sexual-exploitation",
        ],
    },
    "operation-us-v-ardit-kutleshi-and-jetmir-kutleshi": {
        "sources": [
            "2024-12-12_justice-gov_united-states-v-ardit-kutleshi-and-jetmir-kutleshi",
            "2024-12-12_justice-gov_rydox-cybercrime-marketplace-shut-down-and-three-administrators-arrested",
            "2024-12-12_cyberscoop-com_rydox-cybercriminal-marketplace-seized-doj-albania-kosovo",
            "2024-12-13_technadu_kosovo-police-shuts-down-rydox-cybercrime-marketplace",
            "2024-12-13_securityaffairs-com_us-authorities-seized-marketplace-rydox",
        ],
    },
    "operation-us-v-daniel-marsico": {
        "sources": [
            "2026-04-18_justice-gov_pittsburgh-man-indicted-cyberstalking-charge",
            "2024-01-25_cbspittsburgh_pittsburgh-man-charged-cyberstalking-ex-girlfriend",
            "2024-01-25_yahoo_pittsburgh-man-federally-charged-cyberstalking",
            "2024-01-25_postgazette_scott-man-indicted-on-federal-cyberstalking-charge",
            "2024-02-02_justice-gov_one-defendant-sentenced-prison-and-another-ordered-detained-pretrial-week-separate",
        ],
    },
    "operation-former-employee-of-house-member-sentenced-to-prison-term-on-charges-in-cyberstalking-case": {
        "sources": [
            "2026-04-18_justice-gov_former-employee-house-member-sentenced-prison-term-charges-cyberstalking-case",
            "2018-03-08_washingtonpost_us-house-member-still-feels-exposed-stripped-by-ex-aides-cyberstalking-crimes",
            "2018-01-23_washingtonpost_two-ex-staffers-plead-guilty-in-release-of-explicit-images-of-us-house-member-husband",
            "2018-01-23_courthousenews_ex-staffers-plead-guilty-to-circulating-explicit-images-of-house-member",
            "2018-03-08_wjla_ex-house-staffer-sentenced-for-stealing-distributing-nude-images-of-congresswoman",
        ],
    },
    "operation-man-pleads-guilty-to-charges-of-stealing-senate-information-illegally-posting-restricted-personal-information-": {
        "sources": [
            "2026-04-18_justice-gov_man-pleads-guilty-charges-stealing-senate-information-illegally-posting-restricted",
            "2019-04-05_rollcall_senate-doxxing-suspect-pleads-guilty-faces-over-2-years-in-prison",
            "2018-10-03_washingtontimes_jackson-cosko-democratic-operative-charged-doxxing-senators",
            "2019-06-19_thedailybeast_ex-senate-staffer-jackson-cosko-sentenced-4-years-doxxing-five-senators",
            "2019-06-19_washingtonpost_ex-senate-staffer-sentenced-4-years-doxing-gop-senators-kavanaugh-confirmation",
        ],
    },
    "operation-us-v-district-man": {
        "sources": [
            "2026-04-18_justice-gov_restricted-personal-information-us-senators-website",
            "2018-10-03_washingtontimes_jackson-cosko-democratic-operative-charged-doxxing-senators",
            "2019-04-05_rollcall_senate-doxxing-suspect-pleads-guilty-faces-over-2-years-in-prison",
            "2019-06-19_washingtonpost_ex-senate-staffer-sentenced-4-years-doxing-gop-senators-kavanaugh-confirmation",
            "2019-06-19_thedailybeast_ex-senate-staffer-jackson-cosko-sentenced-4-years-doxxing-five-senators",
        ],
    },
    "operation-two-former-employees-of-house-member-indicted-on-federal-charges-in-cyberstalking-case": {
        "sources": [
            "2026-04-18_justice-gov_two-former-employees-house-member-indicted-federal-charges-cyberstalking-case",
            "2017-07-13_cbsnews_ex-house-employees-allegedly-circulated-nude-photos-of-congress-member",
            "2018-01-23_washingtonpost_two-ex-staffers-plead-guilty-in-release-of-explicit-images-of-us-house-member-husband",
            "2018-01-23_courthousenews_ex-staffers-plead-guilty-to-circulating-explicit-images-of-house-member",
            "2018-03-08_washingtonpost_us-house-member-still-feels-exposed-stripped-by-ex-aides-cyberstalking-crimes",
        ],
    },
    "operation-new-york-man-sentenced-to-24-months-in-prison-for-internet-offenses-including-doxing-swatting-making-a-false-b": {
        "sources": [
            "2026-04-18_justice-gov_new-york-man-sentenced-24-months-prison-internet-offenses-including-doxing-swatting",
            "2016-07-12_krebsonsecurity_serial-swatter-stalker-and-doxer-mir-islam-gets-just-1-year-in-jail",
            "2016-07-12_washingtontimes_mir-islam-hacker-sentenced-targeting-nra-boss-lawmakers-cybercrimes",
            "2016-07-11_lieu-house-gov_lieu-statement-sentencing-of-his-swatting-perpetrator",
            "2016-07-15_sophos_serial-swatter-stalker-and-doxer-mir-islam-given-2-years-prison",
        ],
    },
    "operation-notorious-hacker-sentenced-to-18-months-in-prison": {
        "sources": [
            "2026-04-18_justice-gov_notorious-hacker-sentenced-18-months-prison",
            "2023-11-16_securityweek_draftkings-hacker-sentenced-to-18-months-in-prison",
            "2023-11-15_securityaffairs_draftkings-hacker-sentenced-prison-ordered-pay-1-4-million",
            "2023-11-15_justice-gov_us-v-thomas-mccormick-case-page",
            "2023-11-16_cyberwebspider_draftkings-hacker-prison-sentence",
        ],
    },
    "operation-ohio-man-pleads-guilty-for-unlawfully-stealing-over-712-seized-bitcoin-subject-to-forfeiture-in-brothers-pendi": {
        "sources": [
            "2026-04-18_justice-gov_ohio-man-pleads-guilty-unlawfully-stealing-over-712-seized-bitcoin-subject-forfeiture",
            "2023-01-06_coindesk_brother-of-criminal-bitcoin-mixing-ceo-pleads-guilty-stealing-712-bitcoins-irs",
            "2023-04-21_therecord_brother-helix-crypto-mixer-jailed-stealing-bitcoin",
            "2023-01-09_chainalysis_investigation-larry-gary-harmon-helix-mixer",
            "2023-04-21_justice-gov-opa_man-sentenced-for-stealing-over-712-bitcoin-subject-forfeiture",
        ],
    },
    "operation-us-v-gary-james-harmon": {
        "sources": [
            "2026-04-18_justice-gov_ohio-man-pleads-guilty-unlawfully-stealing-over-712-seized-bitcoin-subject-forfeiture",
            "2023-01-06_coindesk_brother-of-criminal-bitcoin-mixing-ceo-pleads-guilty-stealing-712-bitcoins-irs",
            "2023-04-21_therecord_brother-helix-crypto-mixer-jailed-stealing-bitcoin",
            "2023-01-09_chainalysis_investigation-larry-gary-harmon-helix-mixer",
            "2023-04-21_justice-gov-opa_man-sentenced-for-stealing-over-712-bitcoin-subject-forfeiture",
        ],
    },
    "operation-physician-sentenced-to-18-years-in-prison-for-operating-a-pill-mill-from-his-northwest-d-c-medical-practice": {
        "sources": [
            "2026-04-18_justice-gov_physician-sentenced-18-years-prison-operating-pill-mill-his-northwest-dc-medical",
            "2025-06-26_dea-gov_physician-sentenced-18-years-prison-operating-pill-mill-northwest-dc",
            "2025-06-26_hhs-oig_physician-sentenced-18-years-pill-mill-northwest-dc",
            "2025-06-26_wjla_maryland-doctor-pill-mill-northwest-dc-okafor",
            "2025-06-26_oig-dc_physician-sentenced-18-years-pill-mill",
        ],
    },
    "operation-tennessee-man-indicted-on-federal-charges-in-cyberstalking-and-identity-theft-case": {
        "sources": [
            "2026-04-18_justice-gov_tennessee-man-indicted-federal-charges-cyberstalking-and-identity-theft-case",
            "2019-12-19_fbi-gov_cyberstalker-sentenced-maliska",
            "2019-06-17_justice-gov_tennessee-man-pleads-guilty-cyberstalking",
            "2018-07-13_minclaw_civil-case-leads-to-federal-cyberstalking-charges",
            "2018-07-12_bitdefender_tennessee-man-sentenced-17-years-identity-theft",
        ],
    },
    "operation-three-former-department-of-homeland-security-employees-sentenced-in-scheme-to-defraud-the-united-states": {
        "sources": [
            "2026-04-18_justice-gov_three-former-department-homeland-security-employees-sentenced-scheme-defraud-united",
            "2024-01-26_dhs-oig_three-former-dhs-employees-sentenced-scheme-defraud",
            "2024-01-26_uspsoig_three-former-dhs-employees-sentenced-defraud",
            "2024-01-31_law360_three-ex-dhs-staffers-prison-probation-software-theft",
            "2024-01-31_nextgov_former-dhs-employees-sentenced-software-databases-theft",
        ],
    },
    "operation-three-individuals-arrested-for-involvement-in-darknet-narcotics-trafficking-involving-pills-pressed-with-fenta": {
        "sources": [
            "2026-04-18_justice-gov_three-individuals-arrested-involvement-darknet-narcotics-trafficking-involving-pills",
            "2021-02-25_uspis_three-individuals-arrested-darknet-narcotics-fentanyl",
            "2021-04-21_leagle_us-v-teixeira-spencer-21-145",
            "2021-04-21_govinfo_us-courts-dcd-1-21-cr-00145",
            "2021-02-25_wftv_florida-men-bitcoin-darknet-fentanyl-pills",
        ],
    },
    "operation-three-individuals-sentenced-in-darknet-narcotics-trafficking-conspiracy-involving-distribution-of-pills-presse": {
        "sources": [
            "2023-03-22_ddc_ogando-dawodu-spencer-darknet-sentencing",
            "2023-03-22_fda-gov_three-individuals-sentenced-darknet-narcotics-fentanyl",
            "2021-02-25_uspis_three-individuals-arrested-darknet-narcotics-fentanyl",
            "2021-04-21_leagle_us-v-teixeira-spencer-21-145",
            "2021-04-21_govinfo_us-courts-dcd-1-21-cr-00145",
        ],
    },
    "operation-us-v-alex-ogando-olatunji-dawodu-and-luis-spencer": {
        "sources": [
            "2023-03-22_justice-gov_united-states-v-alex-ogando-olatunji-dawodu-and-luis-spencer",
            "2023-03-22_fda-gov_three-individuals-sentenced-darknet-narcotics-fentanyl",
            "2021-02-25_uspis_three-individuals-arrested-darknet-narcotics-fentanyl",
            "2021-04-21_leagle_us-v-teixeira-spencer-21-145",
            "2021-04-21_govinfo_us-courts-dcd-1-21-cr-00145",
        ],
    },
    "operation-maryland-man-sentenced-to-30-months-in-prison-for-cyberstalking-former-girlfriend-and-threatening-workplace-vi": {
        "sources": [
            "2026-04-18_justice-gov_maryland-man-sentenced-30-months-prison-cyberstalking-former-girlfriend-and-threatening",
            "2020-02-13_thedailybeast_feds-ex-nsa-employee-cyberstalked-girlfriend-two-years",
            "2019-07-25_cryptome_us-v-spann-court-filing",
            "2020-08-17_congressheightsontherise_maryland-man-sentenced-30-months-cyberstalking",
            "2020-02-14_bemorelegal_maryland-man-charged-cyberstalking",
        ],
    },
    "operation-us-v-brandon-spann": {
        "sources": [
            "2026-04-18_justice-gov_maryland-man-sentenced-30-months-prison-cyberstalking-former-girlfriend-and-threatening",
            "2020-02-13_thedailybeast_feds-ex-nsa-employee-cyberstalked-girlfriend-two-years",
            "2019-07-25_cryptome_us-v-spann-court-filing",
            "2020-08-17_congressheightsontherise_maryland-man-sentenced-30-months-cyberstalking",
            "2020-02-14_bemorelegal_maryland-man-charged-cyberstalking",
        ],
    },
    "operation-two-arrested-for-alleged-conspiracy-to-launder-4-5-billion-in-stolen-cryptocurrency": {
        "sources": [
            "2026-04-18_justice-gov_two-arrested-alleged-conspiracy-launder-45-billion-stolen-cryptocurrency",
            "2022-02-08_washingtonpost_lichtenstein-morgan-arrested-bitcoin-bitfinex",
            "2022-02-08_ice-gov_hsi-partners-bitfinex-laundering-arrests",
            "2022-02-08_coindesk_judge-stops-release-bitfinex-hack-laundering-suspects",
            "2022-02-08_justice-gov_us-v-ilya-lichtenstein-and-heather-morgan-case-page",
        ],
    },
    "operation-us-v-celeste-santifer": {
        "sources": [
            "2026-04-18_justice-gov_virginia-woman-sentenced-prison-fraudulently-ordering-cell-phones-behalf-her-non-profit",
            "2023-05-04_wusa9_former-ymca-employee-sentenced-41-months-cell-phones",
            "2022-09-09_courtlistener_us-v-santifer-docket",
            "2023-05-08_alxnow_alexandria-woman-sentenced-41-months-wire-fraud",
            "2023-05-04_patch_fraudulent-cell-phone-resales-alexandria-woman",
        ],
    },
    "operation-us-v-david-brian-pate-and-jose-luis-fung-hou": {
        "sources": [
            "2026-04-18_justice-gov_american-darknet-vendor-and-costa-rican-pharmacist-charged-narcotics-and-money-laundering",
            "2020-08-04_cointelegraph_darknet-vendor-pharmacist-270-million-bitcoin-drug-trade",
            "2020-08-05_qcostarica_renowned-costa-rican-doctor-accused-darknet",
            "2020-08-05_infosecurity-magazine_silk-road-vendor-indicted-narcotics",
            "2020-08-04_americanbar_doj-charges-american-darknet-suppliers-costa-rican-pharmacist",
        ],
    },
    "operation-us-v-dutch-national": {
        "sources": [
            "2026-04-18_justice-gov_dutch-national-charged-takedown-obscene-website-selling-over-2000-real-rape-and-child",
            "2020-03-12_washingtonpost_dark-scandals-website-shut-down-arrest-netherlands",
            "2020-03-12_ice-gov_dutch-national-takedown-dark-scandals",
            "2020-03-12_coindesk_us-charges-dutch-national-crypto-funded-child-porn-site",
            "2020-03-12_stltoday_crypto-exchanges-online-child-sex-abuse-profiteer",
        ],
    },
    "operation-us-v-eric-council": {
        "sources": [
            "2026-04-18_justice-gov_guilty-plea-hacking-secs-x-account-caused-bitcoin-value-spike",
            "2025-05-16_justice-gov-opa_alabama-man-sentenced-14-months-sec-x-hack",
            "2025-05-16_cnbc_sec-bitcoin-hack-alabama-man-sentenced-14-months",
            "2024-10-17_washingtontimes_eric-council-jr-arrested-sec-social-media-hack",
            "2025-05-17_coindesk_alabama-man-sentenced-hacking-secs-social-media-fake-bitcoin-etf",
        ],
    },
    "operation-us-v-evan-tangeman": {
        "sources": [
            "2026-04-18_justice-gov_guilty-plea-and-superseding-indictment-announced-social-engineering-scheme-stole-263",
            "2025-12-08_irs-gov_guilty-plea-superseding-indictment-263-million-cryptocurrency",
            "2025-12-08_decrypt_ninth-defendant-pleads-guilty-263m-crypto-scheme",
            "2025-12-08_theblock_22-year-old-guilty-263-million-crypto-syndicate",
            "2025-12-08_ktla_socal-man-laundered-263-million-stolen-crypto",
        ],
    },
    "operation-us-v-four-international-hacking-suspects": {
        "sources": [
            "2026-04-18_justice-gov_four-international-hacking-suspects-charged-racketeering",
            "2019-06-06_krebsonsecurity_darkode-racketeering-indictment-pdf",
            "2019-06-06_total-slovenia-news_us-charges-nicehash-founder-skorjanc",
            "2019-06-09_scworld_court-unseals-darkode-hacking-forum-indictment",
            "2019-08-15_cybersecurityventures_hack-blotter-q3-2019",
        ],
    },
    "operation-us-v-four-russian-government-employees": {
        "sources": [
            "2026-04-18_justice-gov_four-russian-government-employees-charged-two-historical-hacking-campaigns-targeting",
            "2022-03-24_fbi-gov_russian-government-employees-charged-hacking-campaigns",
            "2022-03-24_darkreading_russian-state-sponsored-trisis-dragonfly-energy-indictment",
            "2022-03-25_techcrunch_us-charges-four-russian-spies-saudi-oil-us-nuclear",
            "2022-03-24_cyberscoop_doj-charges-russians-trisis-critical-infrastructure",
        ],
    },
    "operation-us-v-haider-ali-and-arian-taherzadeh": {
        "sources": [
            "2026-04-18_justice-gov_virginia-man-sentenced-federal-prison-conspiring-impersonate-federal-law-enforcement",
            "2023-12-08_secretservice_dc-man-sentenced-impersonate-federal-law-enforcement",
            "2022-04-07_washingtonpost_man-posed-as-dhs-worker-pakistani-intelligence",
            "2022-04-08_cbsnews_two-men-posing-federal-agents-indicted",
            "2023-08-09_fox5dc_virginia-man-impersonated-federal-agent-sentenced-six-years",
        ],
    },
    "operation-russian-malware-developer-arrested-and-extradited-to-the-united-states": {
        "sources": [
            "2023-02-22_justice-gov_united-states-v-dariy-pankov",
            "2023-02-23_theregister_suspected-russian-nlbrute-malware-boss-extradited-to-us",
            "2023-02-22_cyberscoop_russian-national-accused-of-developing-selling-malware-appears-in-us-court",
            "2023-02-22_therecord_russian-accused-of-developing-password-cracking-tool-extradited-to-us",
            "2023-02-23_securityaffairs_alleged-author-of-nlbrute-malware-was-extradited-to-us",
        ],
    },
    "operation-russian-malware-developer-pleads-guilty-to-conspiracy-to-commit-wire-and-computer-fraud": {
        "sources": [
            "2026-04-18_justice-gov_russian-malware-developer-pleads-guilty-conspiracy-commit-wire-and-computer-fraud",
            "2023-09-14_securityaffairs_dariy-pankov-nlbrute-malware-author-pleads-guilty",
            "2023-09-14_securityweek_extradited-russian-hacker-behind-nlbrute-malware-pleads-guilty",
            "2023-09-15_hackread_russian-malware-developer-behind-nlbrute-extradited-pleads-guilty",
            "2023-09-15_bitdefender_russian-malware-developer-behind-nlbrute-faces-five-years-in-prison",
        ],
    },
    "operation-ukrainian-cyber-criminal-extradited-for-decrypting-the-credentials-of-thousands-of-computers-across-the-world-": {
        "sources": [
            "2021-09-08_mdfl_ivanov-tolpintsev-xdedic-extradition",
            "2021-09-09_tampafreepress_ukrainian-cyber-criminal-extradited-to-tampa-faces-17-years",
            "2021-09-08_bleepingcomputer_ukrainian-extradited-for-selling-2000-stolen-logins-per-week",
            "2021-09-08_therecord_ukrainian-indicted-for-running-brute-force-botnet-selling-hacked-pc-accounts",
            "2021-09-09_rferl_ukrainian-extradited-to-us-to-face-hacking-charges",
        ],
    },
    "operation-ssndob-marketplace-administrator-pleads-guilty-to-charges-related-to-his-operation-of-a-series-of-websites-tha": {
        "sources": [
            "2026-04-18_justice-gov_ssndob-marketplace-administrator-pleads-guilty-charges-related-his-operation-series",
            "2023-08-11_bleepingcomputer_ssndob-cybercrime-market-admin-faces-15-years-after-pleading-guilty",
            "2023-08-14_infosecurity_ssndob-marketplace-admin-pleads-guilty",
            "2023-08-11_flashpoint_ssndob-marketplace-admin-pleads-guilty-to-fraud-trafficking-pii",
            "2023-08-12_databreaches_ssndob-marketplace-admin-guilty-plea",
        ],
    },
    "operation-nigerian-national-sentenced-to-more-than-six-years-in-federal-prison-for-international-tax-fraud-scheme": {
        "sources": [
            "2022-12-05_justice-gov_united-states-v-allen-levinson",
            "2022-02-03_irs-ci_nigerian-citizen-extradited-from-uk-arraigned-wire-fraud-stolen-tax-information",
            "2021-12-08_doj-opa_nigerian-national-extradited-from-united-kingdom-to-face-fraud-charges",
            "2022-12-13_fij_nigerian-linked-with-dark-web-wanted-to-defraud-us-govt-of-63m",
            "2022-12-19_accountingtoday_tax-fraud-blotter-standing-corrected-levinson",
        ],
    },
    "operation-rico-conspirators-responsible-for-nationwide-computer-intrusions-and-tax-fraud-sentenced-to-federal-prison": {
        "sources": [
            "2026-04-18_justice-gov_rico-conspirators-responsible-nationwide-computer-intrusions-and-tax-fraud-sentenced",
            "2023-12-19_tampafreepress_9-rico-conspirators-in-florida-sentenced-for-cybercrimes-millions-in-tax-fraud",
            "2024-01-08_progressiveaccountant_ptin-thieves-sentenced",
            "2022-11-22_irs-ci_band-of-cybercriminals-responsible-for-computer-intrusions-nationwide-indicted-rico",
            "2023-12-21_databreaches_rico-conspirators-sentenced-computer-intrusions-tax-fraud",
        ],
    },
    "operation-jumbotron-hacker-and-prolific-child-molester-sentenced-to-220-years-in-federal-prison": {
        "sources": [
            "2026-04-18_justice-gov_jumbotron-hacker-and-prolific-child-molester-sentenced-220-years-federal-prison",
            "2024-03-26_jacksonvilletoday_jumbotron-hacker-sex-offender-220-years",
            "2024-03-26_cbsmiami_jumbotron-hacker-jaguars-stadium-220-years",
            "2024-03-26_nbcmiami_jumbotron-hacker-sex-offender-220-years",
            "2024-03-26_foxnews_jumbotron-hacker-sentenced-220-years-child-sex-abuse-material",
        ],
    },
    "operation-st-augustine-serial-child-molester-convicted-of-hacking-jumbotron-child-exploitation-offenses-sex-offender-reg": {
        "sources": [
            "2026-04-18_justice-gov_st-augustine-serial-child-molester-convicted-hacking-jumbotron-child-exploitation",
            "2023-11-17_washingtontimes_samuel-arthur-thompson-sex-offender-found-guilty-jumbotron",
            "2023-11-21_jacksonvilletoday_sex-offender-convicted-of-hacking-jaguars-jumbotron",
            "2024-03-27_yahoosports_ex-jaguars-employee-hacked-jumbotron-sentenced-220",
            "2024-03-26_outkick_former-jacksonville-jaguars-employee-hacked-jumbotron-sentenced",
        ],
    },
    "operation-pennsylvania-man-convicted-of-distributing-fentanyl-analogue-that-killed-orlando-woman": {
        "sources": [
            "2026-04-18_justice-gov_pennsylvania-man-convicted-distributing-fentanyl-analogue-killed-orlando-woman",
            "2018-04-27_dea_pennsylvania-man-sentenced-life-distributing-fentanyl-analogue-orlando-woman",
            "2018-04-27_seattletimes_man-gets-life-fatal-synthetic-opioid-overdose-achey",
            "2018-04-30_darknetlive_alphabay-vendor-etiking-sentenced-to-life-in-prison",
            "2018-04-12_chainalysis_analyzing-fentanyl-dealer-cryptocurrency-transactions",
        ],
    },
    "operation-u-s-based-conspirators-sentenced-to-prison-for-international-tax-scheme": {
        "sources": [
            "2023-11-29_mdfl_adejumo-jinadu-xdedic-sentencing",
            "2023-08-21_occrp_us-two-plead-guilty-to-transnational-tax-fraud-scheme",
            "2023-12-03_accountingtoday_tax-fraud-blotter-fishy-adejumo-jinadu",
            "2023-08-21_shorenewsnetwork_guilty-pleas-transnational-tax-fraud-scheme",
            "2021-09-15_zebranews_adetunji-adejumo-nigerian-fraudsters-federally-charged-wire-fraud-conspiracy",
        ],
    },
    "operation-us-v-adetunji-adejumo-and-ibrahim-jinadu": {
        "sources": [
            "2023-11-29_justice-gov_united-states-v-adetunji-adejumo-and-ibrahim-jinadu",
            "2023-08-21_occrp_us-two-plead-guilty-to-transnational-tax-fraud-scheme",
            "2023-12-03_accountingtoday_tax-fraud-blotter-fishy-adejumo-jinadu",
            "2023-08-21_shorenewsnetwork_guilty-pleas-transnational-tax-fraud-scheme",
            "2021-09-15_zebranews_adetunji-adejumo-nigerian-fraudsters-federally-charged-wire-fraud-conspiracy",
        ],
    },
    "operation-us-v-and-prolific-child-molester": {
        "sources": [
            "2026-04-18_justice-gov_jumbotron-hacker-and-prolific-child-molester-sentenced-220-years-federal-prison",
            "2024-03-26_jacksonvilletoday_jumbotron-hacker-sex-offender-220-years",
            "2024-03-26_cbsmiami_jumbotron-hacker-jaguars-stadium-220-years",
            "2024-03-26_nbcmiami_jumbotron-hacker-sex-offender-220-years",
            "2024-03-26_foxnews_jumbotron-hacker-sentenced-220-years-child-sex-abuse-material",
        ],
    },
    "operation-rico-conspirator-convicted-at-trial": {
        "sources": [
            "2026-04-18_justice-gov_rico-conspirator-convicted-trial",
            "2023-11-08_wsbt_man-convicted-dickenson-elan-making-millions-fake-tax-info",
            "2022-11-22_patch_clearwater-man-among-cybercriminals-accused-stealing-millions",
            "2023-11-08_foxillinois_dickenson-elan-rico-conspiracy-conviction",
            "2022-11-22_isssource_8-indicted-for-sophisticated-attacks",
        ],
    },
    "operation-us-v-at-trial": {
        "sources": [
            "2026-04-18_justice-gov_rico-conspirator-convicted-trial",
            "2023-11-08_wsbt_man-convicted-dickenson-elan-making-millions-fake-tax-info",
            "2022-11-22_patch_clearwater-man-among-cybercriminals-accused-stealing-millions",
            "2023-11-08_foxillinois_dickenson-elan-rico-conspiracy-conviction",
            "2022-11-22_isssource_8-indicted-for-sophisticated-attacks",
        ],
    },
    "operation-us-v-bookman-dark-web": {
        "sources": [
            "2025-04-10_mdfl_bookman-dark-web-fentanyl-sentencing",
            "2025-04-10_tampafreepress_largo-dealers-dark-web-fentanyl-montana-overdose-15-years",
            "2025-04-11_myfloridanews_florida-man-sentenced-15-years-dark-web-drug-distribution",
            "2025-04-11_newsbreak_florida-dark-web-fentanyl-dealer-sentenced-15-years",
            "2025-04-10_publicnow_dark-web-fentanyl-distributor-sentenced-more-than-15-years",
        ],
    },
    "operation-lakeland-man-pleads-guilty-to-receiving-child-sex-abuse-videos-from-the-largest-darknet-child-pornography-webs": {
        "sources": [
            "2026-04-18_justice-gov_lakeland-man-pleads-guilty-receiving-child-sex-abuse-videos-largest-darknet-child",
            "2021-03-30_wfla_doj-lakeland-man-used-bitcoin-to-buy-child-porn-on-darknet",
            "2019-10-16_wtsp_florida-men-among-hundreds-charged-in-worldwide-child-porn-website-takedown",
            "2019-10-17_patch_2-florida-men-accused-in-worldwide-kiddie-porn-bust",
            "2019-10-16_ice_south-korean-national-and-hundreds-others-charged-worldwide-takedown-largest-darknet",
        ],
    },
    "operation-lakeland-man-sentenced-to-more-than-9-years-in-federal-prison-for-downloading-and-possessing-child-sex-abuse-v": {
        "sources": [
            "2026-04-18_justice-gov_lakeland-man-sentenced-more-9-years-federal-prison-downloading-and-possessing-child-sex",
            "2021-07-01_tampafreepress_lakeland-man-gets-over-9-years-in-federal-prison-for-child-porn",
            "2021-07-01_shorenewsnetwork_lakeland-man-sentenced-9-years-darkweb-csam",
            "2021-07-02_goldrushcam_lakeland-florida-man-sentenced-9-years-darkweb-csam",
            "2019-10-16_ice_south-korean-national-and-hundreds-others-charged-worldwide-takedown-largest-darknet",
        ],
    },
    "operation-ceres-man-pleads-guilty-cyberstalking-two-victims": {
        "sources": [
            "2026-04-18_justice-gov_ceres-man-pleads-guilty-cyberstalking-two-victims",
            "2023-11-13_justice-gov_ceres-man-sentenced-cyberstalking-two-victims",
            "2020-08-13_yahoo-news_airbnb-host-son-secretly-filmed-guest-shower-blackmail",
            "2023-11-14_cerescourier_ceres-man-sentenced-cyberstalking-two-women-airbnb",
            "2020-06-05_cbs-sacramento_ceres-man-recording-airbnb-guest-cyberstalking",
        ],
    },
    "operation-us-v-bryan-connor-herrell": {
        "sources": [
            "2020-09-01_justice-gov_united-states-v-bryan-connor-herrell",
            "2020-09-02_bleepingcomputer_alphabay-dark-web-marketplace-moderator-gets-11-years-in-prison",
            "2020-09-02_engadget_alphabay-moderator-sentenced-11-years",
            "2020-09-01_cbs-colorado_bryan-herrell-aurora-sentenced-prison-international-dark-web-business",
            "2020-09-02_decrypt_darknet-moderator-paid-bitcoin-sentenced-11-years",
        ],
    },
    "operation-us-v-chaloner-saintillus-dark-web": {
        "sources": [
            "2024-02-05_edca_chaloner-saintillus-dark-web-sentencing",
            "2023-04-06_justice-gov_florida-man-pleads-guilty-selling-fentanyl-over-dark-web",
            "2020-12-08_justice-gov_florida-man-indicted-selling-fentanyl-darknet-cryptocurrency",
            "2020-12-09_cbs12_delray-beach-man-indicted-fentanyl-cryptocurrency",
            "2023-04-07_thecyberpost_ncidetf-arrested-chlnsaint-vendor-list",
        ],
    },
    "operation-tattoo-shop-owner-pleads-guilty-to-distributing-heroin-and-methamphetamine-on-the-darknet": {
        "sources": [
            "2020-03-05_justice-gov_united-states-v-jason-keith-arnold",
            "2022-02-17_justice-gov_tattoo-shop-owner-sentenced-7-years-prison-distributing-heroin-methamphetamine",
            "2019-04-05_dea-gov_fentanyl-heroin-darknet-vendors-indicted",
            "2022-02-18_uspsoig-gov_arizona-man-sentenced-11-years-conspiracy-narcotics-dark-web",
            "2022-02-19_appeal-democrat_arizona-man-sentenced-dark-web-drug-sales",
        ],
    },
    "operation-us-v-jason-arnold-dark-web": {
        "sources": [
            "2020-03-05_edca_jason-arnold-darknet-plea",
            "2022-02-17_justice-gov_tattoo-shop-owner-sentenced-7-years-prison-distributing-heroin-methamphetamine",
            "2019-04-05_dea-gov_fentanyl-heroin-darknet-vendors-indicted",
            "2022-02-18_uspsoig-gov_arizona-man-sentenced-11-years-conspiracy-narcotics-dark-web",
            "2020-03-04_12news_owner-chandler-tattoo-parlor-charged-trafficking-drugs-darknet",
        ],
    },
    "operation-us-v-jason-keith-arnold-and-david-white": {
        "sources": [
            "2026-04-18_justice-gov_tattoo-shop-owner-sentenced-more-7-years-prison-distributing-heroin-and-methamphetamine",
            "2022-02-17_justice-gov_tattoo-shop-owner-sentenced-7-years-prison-distributing-heroin-methamphetamine",
            "2019-04-05_dea-gov_fentanyl-heroin-darknet-vendors-indicted",
            "2022-02-18_uspsoig-gov_arizona-man-sentenced-11-years-conspiracy-narcotics-dark-web",
            "2020-03-04_manteca-bulletin_4-charged-drug-trafficking-darknet",
        ],
    },
    "operation-us-v-catherine-stuckey-dark-web": {
        "sources": [
            "2020-07-15_edca_catherine-stuckey-darknet-plea",
            "2024-05-10_justice-gov_final-calicartel-defendant-pleads-guilty-dark-web-heroin-methamphetamine-cocaine",
            "2023-06-06_justice-gov_dark-web-traffickers-heroin-methamphetamine-cocaine-prosecuted",
            "2020-07-19_darkweblink_california-beauty-pleads-guilty-distributing-drugs-10-years",
            "2020-07-20_dnstats_cali-man-pleads-guilty-running-calicartel-account",
        ],
    },
    "operation-us-v-eddy-steven-sandoval-lopez": {
        "sources": [
            "2026-04-18_justice-gov_nicaraguan-national-pleads-guilty-conspiring-distribute-cocaine-and-marijuana-darknet",
            "2019-06-03_ice-gov_nicaraguan-national-pleads-guilty-conspiring-distribute-cocaine-marijuana-darknet",
            "2019-06-03_dea-gov_nicaraguan-national-pleads-guilty-cocaine-marijuana-darknet",
            "2018-06-21_justice-gov_two-sacramento-men-indicted-distributing-cocaine-marijuana-dark-web-marketplaces",
            "2018-06-22_softpedia_duo-accused-dark-web-drug-dealing-faces-20-years-prison",
        ],
    },
    "operation-us-v-devin-shanahan": {
        "sources": [
            "2026-04-18_justice-gov_final-calicartel-defendant-pleads-guilty-dark-web-heroin-methamphetamine-and-cocaine",
            "2021-10-08_justice-gov_ventura-county-man-pleads-guilty-dark-web-narcotics-distribution-conspiracy",
            "2023-06-06_justice-gov_dark-web-traffickers-heroin-methamphetamine-cocaine-prosecuted",
            "2021-10-09_uspsoig-gov_california-man-operating-dark-web-vendor-account-pleads-guilty-conspiracy",
            "2024-05-11_darknetlive_operators-calicartel-drugs-vendor-account-sentenced",
        ],
    },
    "operation-us-v-ian-hoffmann": {
        "sources": [
            "2026-04-18_justice-gov_dark-web-traffickers-heroin-methamphetamine-and-cocaine-prosecuted",
            "2021-10-08_justice-gov_ventura-county-man-pleads-guilty-dark-web-narcotics-distribution-conspiracy",
            "2024-05-10_justice-gov_final-calicartel-defendant-pleads-guilty-dark-web-heroin-methamphetamine-cocaine",
            "2021-10-09_uspsoig-gov_california-man-operating-dark-web-vendor-account-pleads-guilty-conspiracy",
            "2021-10-09_shorenewsnetwork_ventura-county-man-pleads-guilty-dark-web-narcotics-distribution-conspiracy",
        ],
    },
    "operation-us-v-holly-adams-dark-web": {
        "sources": [
            "2025-06-03_edca_holly-adams-dark-web-fentanyl-sentencing",
            "2025-06-03_irs-gov_dark-web-fentanyl-dealer-sentenced-federal-prison",
            "2022-05-12_justice-gov_sacramento-grand-jury-indicts-riverside-county-man-woman-fentanyl-distribution-money-laundering",
            "2025-06-04_actionnewsnow_woman-sentenced-12-years-federal-prison-fentanyl-dark-web",
            "2022-05-13_irs-gov_sacramento-grand-jury-indicts-riverside-county-fentanyl-money-laundering",
        ],
    },
    "operation-us-v-holly-danielle-adams-and-devlin-hosner": {
        "sources": [
            "2026-04-18_justice-gov_southern-california-woman-pleads-guilty-fentanyl-distribution-and-money-laundering",
            "2025-06-03_irs-gov_dark-web-fentanyl-dealer-sentenced-federal-prison",
            "2022-05-12_justice-gov_sacramento-grand-jury-indicts-riverside-county-man-woman-fentanyl-distribution-money-laundering",
            "2025-06-04_actionnewsnow_woman-sentenced-12-years-federal-prison-fentanyl-dark-web",
            "2022-05-13_irs-gov_sacramento-grand-jury-indicts-riverside-county-fentanyl-money-laundering",
        ],
    },
    "operation-us-v-devlin-hosner-and-holly-adams": {
        "sources": [
            "2026-04-18_justice-gov_southern-california-man-pleads-guilty-fentanyl-and-methamphetamine-distribution",
            "2025-06-03_irs-gov_dark-web-fentanyl-dealer-sentenced-federal-prison",
            "2022-05-12_justice-gov_sacramento-grand-jury-indicts-riverside-county-man-woman-fentanyl-distribution-money-laundering",
            "2025-06-04_actionnewsnow_woman-sentenced-12-years-federal-prison-fentanyl-dark-web",
            "2022-05-13_irs-gov_sacramento-grand-jury-indicts-riverside-county-fentanyl-money-laundering",
        ],
    },
    "operation-us-v-fatukala-cocaine-dark-web": {
        "sources": [
            "2023-11-17_edca_fatukala-yamamoto-mina-hollis-dark-web-sentencing",
            "2023-06-06_justice-gov_dark-web-traffickers-heroin-methamphetamine-cocaine-prosecuted",
            "2023-01-26_dea-gov_seventh-defendant-pleads-guilty-large-scale-sacramento-cocaine-heroin",
            "2023-12-15_dea-gov_ninth-defendant-pleads-guilty-large-scale-sacramento-cocaine-heroin",
            "2023-01-26_cslea_seventh-defendant-pleads-guilty-sacramento-drug-trafficking-conspiracy",
        ],
    },
    "operation-us-v-fatukala-yamamoto-mina-and-hollis": {
        "sources": [
            "2023-11-17_justice-gov_united-states-v-fatukala-yamamoto-mina-and-hollis",
            "2023-06-06_justice-gov_dark-web-traffickers-heroin-methamphetamine-cocaine-prosecuted",
            "2023-01-26_dea-gov_seventh-defendant-pleads-guilty-large-scale-sacramento-cocaine-heroin",
            "2023-12-15_dea-gov_ninth-defendant-pleads-guilty-large-scale-sacramento-cocaine-heroin",
            "2023-01-26_cslea_seventh-defendant-pleads-guilty-sacramento-drug-trafficking-conspiracy",
        ],
    },
    "operation-us-v-jaziz-jesahias-cea": {
        "sources": [
            "2026-04-18_justice-gov_former-national-guard-member-sentenced-20-years-prison-using-internet-commit-child",
            "2021-04-29_justice-gov_former-national-guard-member-pleads-guilty-internet-sexual-exploitation-qatar",
            "2022-03-18_fox40_galt-man-former-national-guard-20-years-prison-child-exploitation",
            "2021-04-30_cbs-sanfrancisco_former-california-national-guardsman-guilty-trading-child-porn-overseas",
            "2021-04-30_fox40_former-california-national-guard-pleads-guilty-child-pornography",
        ],
    },
    "operation-us-v-anthony-dalton-wolff": {
        "sources": [
            "2026-04-18_justice-gov_arizona-man-indicted-offenses-involving-sexual-exploitation-minor",
            "2024-09-13_fox10phoenix_arizona-man-indicted-attempting-lure-minor-undercover-agent",
            "2024-09-13_yahoo-news_arizona-man-indicted-attempting-lure-minor",
            "2024-09-13_hoodline_arizona-man-indicted-attempting-arrange-sexual-encounter-minor-dark-web",
            "2024-09-13_facebook-fox10phoenix_anthony-dalton-wolff-42-surprise-indicted-suspect",
        ],
    },
    "operation-us-v-international-travel": {
        "sources": [
            "2026-04-18_justice-gov_two-indictments-charge-international-travel-engage-illicit-sexual-activity-minors-0",
            "2023-07-12_justice-gov_danish-national-arrested-fresno-airport-illicit-sexual-activity-minors",
            "2023-07-13_justice-gov-archives_two-indictments-international-travel-illicit-sexual-activity-minors",
            "2024-09-30_justice-gov_sacramento-man-sentenced-life-buying-children-other-child-exploitation",
            "2017-08-23_ice-gov_sacramento-man-indicted-traveling-overseas-have-sex-children",
        ],
    },
    "operation-us-v-dequan-lamar-mitchell": {
        "sources": [
            "2026-04-18_justice-gov_vallejo-man-indicted-illegal-firearm-possession",
            "2026-02-13_dailyrepublic_vallejo-man-indicted-illegal-firearm-possession",
            "2026-02-13_actionnewsnow_vallejo-man-indicted-federal-grand-jury-illegal-possession-firearm",
            "2026-02-13_crimevoice_grand-jury-indicts-vallejo-man-illegal-possession-firearm",
            "2026-02-05_pressdemocrat_vallejo-man-caught-selling-stolen-gun-jail-furlough-murder",
        ],
    },
    "operation-us-v-evan-hayes": {
        "sources": [
            "2026-04-18_justice-gov_two-individuals-sentenced-conspiracy-charges-involving-sale-fraudulent-identity",
            "2022-04-04_justice-gov-archives_two-individuals-sentenced-conspiracy-sale-fraudulent-identity-documents-darknet",
            "2022-04-05_wivb_buffalo-man-woman-italy-sentenced-selling-fake-ids",
            "2022-04-05_benzinga_fake-new-york-drivers-licenses-darknet-market-two-men-sentenced",
            "2022-04-05_justice-gov_two-individuals-sentenced-conspiracy-charges-fraudulent-identity-documents",
        ],
    },
    "operation-two-stockton-residents-charged-with-sexual-exploitation-of-a-minor": {
        "sources": [
            "2026-04-18_justice-gov_two-stockton-residents-charged-sexual-exploitation-minor",
            "2020-06-19_fox40_federal-officials-charge-2-stockton-residents-sexual-exploitation-child",
            "2020-06-19_hoodline_top-stockton-news-teen-shot-walnut-workers-rally",
            "2020-12-08_justice-gov_stockton-man-charged-sexual-exploitation-minor",
            "2021-12-15_justice-gov_stockton-man-pleads-guilty-attempted-sexual-exploitation-minor",
        ],
    },
    "operation-us-v-jonathan-michael-thornton-and-katherine-leann-herrera": {
        "sources": [
            "2026-04-18_justice-gov_two-stockton-residents-charged-sexual-exploitation-minor",
            "2020-06-19_fox40_federal-officials-charge-2-stockton-residents-sexual-exploitation-child",
            "2020-06-19_hoodline_top-stockton-news-teen-shot-walnut-workers-rally",
            "2020-12-08_justice-gov_stockton-man-charged-sexual-exploitation-minor",
            "2021-12-15_justice-gov_stockton-man-pleads-guilty-attempted-sexual-exploitation-minor",
        ],
    },
    "operation-sacramento-sex-offender-pleads-guilty-to-distributing-child-pornography-on-the-dark-web": {
        "sources": [
            "2026-04-18_justice-gov_sacramento-sex-offender-pleads-guilty-distributing-child-pornography-dark-web",
            "2025-02-24_justice-gov_sacramento-man-sentenced-24-years-running-multiple-dark-web-child-sexual-abuse-websites",
            "2025-02-24_justice-gov-opa_man-sentenced-24-years-running-dark-web-child-sexual-abuse-websites",
            "2025-02-25_actionnewsnow_sacramento-man-24-years-4-months-running-multiple-dark-web-child-sex-abuse-websites",
            "2025-02-25_yahoo-news_california-man-sentenced-24-years-prison-dark-web-child-porn",
        ],
    },
    "operation-sacramento-woman-pleads-guilty-to-conspiracy-to-distribute-fentanyl": {
        "sources": [
            "2026-04-18_justice-gov_sacramento-woman-pleads-guilty-conspiracy-distribute-fentanyl",
            "2024-08-29_justice-gov_sacramento-area-group-charged-shipping-fentanyl-pills-across-united-states",
            "2025-06-23_justice-gov_sacramento-woman-pleads-guilty-fentanyl-distribution",
            "2025-06-23_goldenstatetoday_sacramento-woman-pleads-guilty-distributing-fentanyl",
            "2025-07-21_dea-gov_sacramento-man-sentenced-9-years-fentanyl-meth-trafficking",
        ],
    },
    "operation-two-individuals-sentenced-for-conspiracy-charges-involving-the-sale-of-fraudulent-identity-documents-on-the-da": {
        "sources": [
            "2026-04-18_justice-gov_two-individuals-sentenced-conspiracy-charges-involving-sale-fraudulent-identity",
            "2022-04-04_justice-gov-archives_two-individuals-sentenced-conspiracy-sale-fraudulent-identity-documents-darknet",
            "2022-04-05_wivb_buffalo-man-woman-italy-sentenced-selling-fake-ids",
            "2022-04-05_benzinga_fake-new-york-drivers-licenses-darknet-market-two-men-sentenced",
            "2022-04-05_ice-gov_darknet-vendor-fraudulent-identity-documents-sentenced",
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
