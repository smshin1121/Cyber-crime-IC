from __future__ import annotations

import re
from pathlib import Path

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
SOURCES_DIR = ROOT / "wiki" / "sources"

SEEDS: dict[str, list[str]] = {
    "bec-nigeria-2016": [
        "2016-12-22_justice-gov_nigerian-nationals-charged-with-operating-business-compromise-scheme",
        "2016-12-20_justice-gov_united-states-v-odufuye-and-nwoke",
        "2016-12-20_justice-gov_nigerian-nationals-charged-with-operating-business-compromise-scheme",
        "2016-12-20_dct_odufuye-nwoke-bec-indictment",
    ],
    "cyber-fraud-international-2015": [
        "2015-06-01_europol-europa-eu_international-operation-dismantles-criminal-group-of-cyber-fraudsters",
        "europol-international-cyber-fraud-dismantling-operation",
    ],
    "darkode-takedown": [
        "2015-07-15_fbi-gov_cyber-criminal-forum-taken-down",
        "2015-07-15_justice-gov_major-computer-hacking-forum-dismantled",
        "2015-07-15_justice-gov_darkode-forum-dismantled-w-d-pa",
        "2015-07-15_wdpa_darkode-indictment",
        "2015-07-01_wired-com_dozens-nabbed-takedown-cybercrime-forum-darkode",
        "2015-07-15_krebsonsecurity-com_the-darkode-cybercrime-forum-up-close",
    ],
    "fake-shopping-sites-takedown-2024": [
        "2024-12-04_europol-europa-eu_fraudulent-shopping-sites-tied-to-cybercrime-marketplace-taken-offline",
        "europol-fraudulent-shopping-sites-takedown",
        "al-jazeera-fraudulent-shopping-sites-takedown",
    ],
    "franco-israeli-ceo-fraud": [
        "2023-02-08_europol_franco-israeli-ceo-fraud-bust",
        "2023-02-08_europol-europa-eu_franco-israeli-gang-behind-eur-38-million-ceo-fraud-busted",
        "2023-02-08_europol-europa-eu_franco-israeli-ceo-fraud-gang-dismantled",
        "2023-02-08-europol-franco-israeli-ceo-fraud",
    ],
    "global-airport-action-day": [
        "2016-10-20_interpol-int_global-airport-action-day-40-countries-nab-193-suspects-in-cybercrime-sting",
        "hackread-global-airport-action-day",
        "2016-10-19_interpol-int_global-airport-action-day-targets-airline-ticket-fraudsters",
    ],
    "hive-ransomware-takedown": [
        "europol-hive-ransomware-infrastructure-takedown",
        "cbs-news-hive-ransomware-infrastructure-takedown",
        "2023-01-26_europol-europa-eu_cybercriminals-stung-as-hive-infrastructure-shut-down",
        "2023-01-26_techcrunch-com_united-states-hive-ransomware-seized",
        "2023-01-26_dw-com_us-german-authorities-block-hive-ransomware-website",
    ],
    "isoon-apt27-indictment": [
        "2025-03-05_opa_wu-haibo-isoon-indictment",
        "2025-03-05_justice-gov_justice-department-charges-12-chinese-contract-hackers-i-soon-apt27-indictment",
        "2025-03-05_justice-gov_i-soon-apt27-indictment",
        "2025-03-05_wired-com_us-charges-12-alleged-spies-in-chinas-freewheeling-hacker-for-hire-ecosystem",
    ],
    "operation-12-members-of-an-irish-high-risk-criminal-network-arrested": [
        "2024-11-01_europol-europa-eu_12-members-of-an-irish-high-risk-criminal-network-arrested",
        "2025-03-28_dia-interno-gov-it_operazione-pereira23-irish-high-risk-criminal-network",
        "2025-03-28_cde-ual-es_12-members-of-an-irish-high-risk-criminal-network-arrested",
        "2025-03-27_irishtimes-com_spanish-police-say-irelands-family-drugs-gang-enjoyed-high-economic-status-and-influence",
    ],
    "black-axe-bec-2021": [
        "2022-10-14_interpol_operation-jackal-black-axe",
        "2023-06-06_interpol_operation-jackal-black-axe-bec",
        "2023-06-06_interpol-int_operation-jackal-black-axe-bec",
        "2024-08-28_interpol_operation-jackal-iii-black-axe",
        "2024-08-28_interpol-int_operation-jackal-iii-black-axe-bec",
        "2022-10-21_vanguardngr-com_interpol-arrests-over-70-suspected-fraudsters-linked-to-black-axe-cult-in-nigeria",
    ],
    "korea-cambodia-scam-repatriation": [
        "2025-10-18_aljazeera-com_korea-cambodia-scam-centre-repatriation",
        "2025-10-18-korea-cambodia-scam-repatriation",
        "2025-10-18_aljazeera-com_south-korea-repatriates-64-scam-centre-suspects-from-cambodia",
    ],
    "korea-china-voice-phishing-qingdao": [
        "2023-09-08-korea-china-voice-phishing-qingdao",
        "2023-09-08_koreatimes-co-kr_seoul-metropolitan-police-and-chinese-police-jointly-arrest-16-voice-phishing-su",
        "2023-09-08_koreatimes-co-kr_korea-china-voice-phishing-joint-operation",
    ],
    "operation-de-fr-online-fraud-group-2026": [
        "2026-04-14_eurojust_judicial-cooperation-key-to-arresting-leaders-of-online-frau",
        "2026-03-11_eurojust-europa-eu_judicial-cooperation-key-to-arresting-leaders-of-online-fraud-group",
        "2026-03-11-eurojust-de-fr-online-fraud-group",
    ],
    "operation-eur-300m-global-credit-card-fraud-2025": [
        "2025-11-05_eurojust_eurojust-coordinates-major-operation-against-eur-300-million-global-credit-card-fraud-18",
        "2025-11-05_112wwft-nl_eurojust-coordinates-major-operation-against-eur-300-million-global-credit-card-fraud-18-arrests",
        "2025-12-22_eurojusts-cross-border-investigations-2025_credit-card-fraud-roundup",
    ],
    "zambia-golden-top-call-center": [
        "2024-04-15-bitdefender-zambia-golden-top-arrests",
        "2024-06-05-therecord-zambia-golden-top-guilty-pleas",
        "2024-06-07_apnews-com_22-chinese-nationals-sentenced-to-long-prison-terms-in-zambia-for-multinational-cybercrimes",
    ],
    "operation-endgame-phase1": [
        "2024-05-29_fbi-gov_operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-o",
        "2024-05-30_bmi-bund-de_worldwide-investigation-against-cyber-crime-crowned-by-success",
        "2024-05-30_krebsonsecurity-com_operation-endgame-hits-malware-delivery-platforms",
        "2026-04-17_europol-europa-eu_operation-endgame-official-page",
    ],
    "operation-endgame-phase2": [
        "2024-05-29_fbi-gov_operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-o",
        "2024-05-30_europol-europa-eu_largest-ever-operation-against-botnets-operation-endgame",
        "2024-05-30_europol_operation-endgame-botnet-takedown",
        "2024-05-30_krebsonsecurity-com_operation-endgame-hits-malware-delivery-platforms",
        "2025-05-22_europol-europa-eu_operation-endgame-follow-up-leads-to-detentions-and-server-takedowns",
        "2025-05-23_europol-europa-eu_operation-endgame-phase-2",
        "2025-05-23_europol-europa-eu_operation-endgame-strikes-again-the-ransomware-kill-chain-broken-at-its-source",
    ],
    "operation-french-coder-who-helped-extort-british-company-arrested-in-thailand": [
        "europol-rex-mundi-hacking-group-takedown",
        "2018-06-14_europol-europa-eu_europol-french-coder-who-helped-extort-british-company-arrested-in-thailand",
        "2018-05-18_europol-europa-eu_french-coder-who-helped-extort-british-company-arrested-in-thailand",
        "2018-06-19_welivesecurity-com_europol-and-partners-dismantle-prolific-cyber-extortion-gang",
        "2018-06-15_bleepingcomputer-com_europol-dismantles-one-of-the-internets-oldest-hacker-groups",
        "2018-06-15_securityweek-com_french-nationals-arrested-for-rex-mundi-hacks",
        "2018-06-18_infosecurity-magazine_europol-disrupts-rex-mundi-cybercrime-group",
    ],
    "rex-mundi-takedown": [
        "europol-rex-mundi-hacking-group-takedown",
        "2018-05-18_europol-europa-eu_french-coder-who-helped-extort-british-company-arrested-in-thailand",
        "2018-06-14_europol-europa-eu_europol-french-coder-who-helped-extort-british-company-arrested-in-thailand",
        "2018-06-19_welivesecurity-com_europol-and-partners-dismantle-prolific-cyber-extortion-gang",
        "2018-06-15_bleepingcomputer-com_europol-dismantles-one-of-the-internets-oldest-hacker-groups",
        "2018-06-15_securityweek-com_french-nationals-arrested-for-rex-mundi-hacks",
        "2018-06-18_infosecurity-magazine_europol-disrupts-rex-mundi-cybercrime-group",
    ],
    "operation-first-light-2024": [
        "2024-06-18_interpol_operation-first-light-2024",
        "2025-12-01_police-gov-sg_cad-report-2024-operation-first-light",
        "2024-07-01_police-gov-sg_mid-year-scams-and-cybercrime-brief-2024-operation-first-light",
        "2026-02-01_interpol-int_annual-report-2024-operation-first-light",
        "2026-04-01_interpol-int_support-for-afripol-operation-first-light",
    ],
    "operation-cyber-guardian": [
        "2025-04-08_police-gov-sg_cross-border-operation-targeting-online-child-sexual-exploitation-activities",
        "2025-04-07_korea-npa_operation-cyber-guardian-asia-csam",
        "2025-04-07_seoul-co-kr_operation-cyber-guardian",
        "2025-04-01_japan-npa_operation-cyber-guardian",
        "2025-04-07_korea-kr_operation-cyber-guardian-asia-6-country-joint-crackdown-on-child-sexual-abuse-ma",
        "2025-04-07_seoul-co-kr_asia-6-country-crackdown-on-online-child-sexual-abuse-material",
    ],
    "operation-jackal": [
        "2023-06-06-interpol-operation-jackal",
    ],
    "operation-jackal-iii": [
        "2024-08-28-interpol-operation-jackal-iii",
    ],
    "operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown": [
        "2025-02-11_europol_phobos-8base-ransomware-arrests",
        "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercr",
        "2025-02-11-europol-phobos-8base-ransomware-arrests",
        "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested",
        "2026-04-18_justice-gov_phobos-ransomware-affiliates-arrested-in-coordinated-international-disruption",
        "2025-02-11_bleepingcomputer-com_us-charges-phobos-8base-ransomware-operators",
    ],
    "operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown-3": [
        "2025-02-11_europol_phobos-8base-ransomware-arrests",
        "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercr",
        "2025-02-11-europol-phobos-8base-ransomware-arrests",
        "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested",
        "2026-04-18_justice-gov_phobos-ransomware-affiliates-arrested-in-coordinated-international-disruption",
        "2025-02-11_bleepingcomputer-com_us-charges-phobos-8base-ransomware-operators",
    ],
    "operation-sentinel-africa": [
        "2025-12-22_interpol_operation-sentinel-africa-bec",
        "2025-12-22_interpol-int_operation-sentinel-africa",
        "2025-12-22_interpol-int_574-arrests-and-usd-3-million-recovered-in-coordinated-cybercrime-operation-acro",
        "2025-12-22-interpol-operation-sentinel-africa",
    ],
    "operation-secreto": [
        "europol-operation-secreto",
        "the-record-operation-secreto",
        "2021-02-03_secretservice-gov_105-arrested-for-stealing-over-eur-12-million-from-u-s-based-banks",
        "2021-02-03_policia-es_la-policia-nacional-y-el-servicio-secreto-de-los-eeuu-desarticulan-una-organizacion",
        "2021-02-09_cisomag_operation-secreto-europol-busts-international-cybercriminal-group",
    ],
    "operation-morpheus": [
        "2024-06-28-uk-nca-operation-morpheus-cobalt-strike",
        "2024-07-03_nationalcrimeagency-gov-uk_national-crime-agency-leads-international-operation-to-degrade-illegal-versions",
        "the-hacker-news-operation-morpheus-cobalt-strike-takedown",
        "uk-nca-operation-morpheus-cobalt-strike-takedown",
        "2024-07-03_bleepingcomputer-com_europol-takes-down-593-cobalt-strike-servers-used-by-cybercriminals",
        "2024-07-03_techradar-com_hundreds-of-cobalt-strike-linked-servers-taken-down-in-major-police-operation",
    ],
    "operation-rewired": [
        "2019-09-10_fbi-gov_operation-rewired-bec-takedown",
        "2019-09-10_justice-gov_281-arrested-worldwide-coordinated-international-enforcement-operation-targeting-hundreds",
        "2019-09-10_secretservice-gov_281-arrested-worldwide-coordinated-international-enforcement-operation",
        "2019-09-11_scworld-com_operation-rewired-campaign",
        "2019-09-10_wired-com_email-scammer-global-takedown",
    ],
    "operation-nova": [
        "2020-12-22_cyberscoop-com_safe-inet-takedown-fbi-interpol",
        "2020-12-22_portswigger-net_safe-inet-vpn-service-for-cybercriminals-taken-down-in-law-enforcement-bust",
        "cyberscoop-operation-nova-safe-inet-vpn-takedown",
        "portswigger-operation-nova-safe-inet-vpn-takedown",
        "2020-12-22_bleepingcomputer-com_safe-inet-insorg-vpn-services-shut-down-by-law-enforcement",
        "2020-12-22_infosecurity-magazine_police-seize-safe-inet",
        "2020-12-24_cisomag_operation-nova-seizes-safe-inet-vpn",
    ],
    "romania-phishing-takedown-2024": [
        "2024-01-01_europol-europa-eu_hook-line-and-sinker-cybercrime-network-phishing-bank-credentials-arrested-in-ro",
        "europol-romania-phishing-network-takedown",
    ],
    "rydox-marketplace-takedown": [
        "2024-12-12_wdpa_kutleshi-rydox-indictment",
        "2024-12-12_justice-gov_united-states-v-ardit-kutleshi-and-jetmir-kutleshi",
        "2024-12-12_justice-gov_rydox-cybercrime-marketplace-shut-down-and-three-administrators-arrested",
        "2024-12-12_cyberscoop-com_rydox-cybercriminal-marketplace-seized-doj-albania-kosovo",
        "2024-12-13_technadu_kosovo-police-shuts-down-rydox-cybercrime-marketplace",
        "2024-12-13_securityaffairs-com_us-authorities-seized-marketplace-rydox",
        "2024-12-16_bitdefender-com_rydox-cybercrime-marketplace-seized-by-law-enforcement-suspected-admins-arrested",
    ],
    "simda-botnet-takedown": [
        "interpol-911-s5-botnet-dismantling",
        "2015-04-09_interpol-int_interpol-coordinates-global-operation-to-take-down-simda-botnet",
        "2015-04-13_kaspersky-com_kaspersky-lab-joins-forces-with-interpol-industry-and-law-enforcement-partners-to-disrupt-simda-botnet",
        "2015-04-13_kaspersky-com_simda-botnet-a-stealthy-malware-waiter",
        "2015-04-13_trendmicro-com_trend-micro-joins-interpol-botnet-takedown-presents-at-interpol-world-2015",
        "2015-04-15_techspot-com_interpol-led-operation-takes-down-the-botnet-that-infected-over-770k-pcs",
    ],
    "operation-source": [
        "europol-operation-source",
        "2015-04-01_europol-europa-eu_international-police-operation-targets-polymorphic-beebone-botnet",
        "2015-04-09_scworld-com_international-effort-takes-down-beebone-botnet",
        "2015-04-09_securityweek-com_authorities-takedown-beebone-botnet-international-operation",
        "2015-04-09_arstechnica_us-european-police-take-down-highly-elusive-botnet-known-as-beebone",
        "2015-04-10_wired-com_beebone-botnet-bites-the-dust",
    ],
    "operation-checkmate-blacksuit": [
        "2025-08-11_justice-gov_operation-checkmate-blacksuit",
        "2025-07-24_bleepingcomputer-com_law-enforcement-seizes-blacksuit-ransomware-leak-sites",
        "2025-07-25_scworld-com_operation-checkmate-shuts-down-blacksuits-extortion-sites",
        "2025-07-25_bitdefender-com_after-500-million-in-ransom-demands-law-enforcement-seizes-blacksuit-site",
        "2025-07-28_techradar-com_top-ransomware-group-blacksuit-has-dark-web-extortion-sites-seized-and-shut-down",
    ],
    "operation-cronos-phase1": [
        "2024-02-20_europol-europa-eu_law-enforcement-disrupt-world-s-biggest-ransomware-operation-operation-cronos-lo",
        "2024-02-20_europol-europa-eu_operation-cronos-lockbit-disrupted",
        "2024-02-20_europol_operation-cronos-lockbit",
        "2024-02-20-europol-operation-cronos-lockbit",
        "2024-10-01_europol-europa-eu_operation-cronos-phase-3",
        "2024-12-04_nationalcrimeagency-gov-uk_operation-destabilise-nca-disrupts-multi-billion-money-laundering-networks",
        "2026-01-28_gov-uk_financial-sanctions-guidance-for-ransomware",
    ],
    "operation-cronos-phase3": [
        "2024-10-01_europol-europa-eu_operation-cronos-phase-3",
        "2024-10-01_europol-europa-eu_lockbit-power-cut-four-new-arrests-operation-cronos-phase-3",
        "2024-10-01_europol-europa-eu_lockbit-power-cut-four-new-arrests-and-financial-sanctions-against-affiliates-op",
        "2024-10-01_europol_operation-cronos-lockbit-phase3",
        "2024-10-01-europol-operation-cronos-lockbit-phase3",
        "2024-02-20_europol_operation-cronos-lockbit",
        "2024-10-02_therecord-media_operation-cronos-phase-3-lockbit",
        "2026-01-28_gov-uk_financial-sanctions-guidance-for-ransomware",
    ],
    "emotet-takedown": [
        "2021-01-27-europol-emotet-disruption",
        "2021-01-27-eurojust-emotet-operation",
        "2021-01-27-doj-emotet-disruption",
        "2021-01-27_mdnc_emotet-disruption-order",
        "2026-04-17_justice-gov_documents-and-resources-related-disruption-emotet-malware-and-botnet",
    ],
    "operation-europol-105-arrested-for-stealing-over-12-million-from-us-based-banks-operation-secreto": [
        "europol-operation-secreto",
        "the-record-operation-secreto",
        "2021-02-03_secretservice-gov_105-arrested-for-stealing-over-eur-12-million-from-u-s-based-banks",
        "2021-02-03_policia-es_la-policia-nacional-y-el-servicio-secreto-de-los-eeuu-desarticulan-una-organizacion",
        "2021-02-09_cisomag_operation-secreto-europol-busts-international-cybercriminal-group",
    ],
    "operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown": [
        "2025-02-11_europol_phobos-8base-ransomware-arrests",
        "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested",
        "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercr",
        "2025-02-10_justice-gov_phobos-ransomware-affiliates-arrested-in-coordinated-international-disruption",
        "2024-11-18_justice-gov_phobos-ransomware-administrator-extradited-from-south-korea-to-face-cybercrime-c",
        "2025-02-11_bleepingcomputer-com_us-charges-phobos-8base-ransomware-operators",
        "2026-04-18_justice-gov_phobos-ransomware-affiliates-arrested-in-coordinated-international-disruption",
        "2026-04-18_justice-gov_phobos-ransomware-administrator-extradited-from-south-korea-to-face-cybercrime-c",
    ],
    "operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown-3": [
        "2025-02-11_europol_phobos-8base-ransomware-arrests",
        "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested",
        "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercr",
        "2025-02-10_justice-gov_phobos-ransomware-affiliates-arrested-in-coordinated-international-disruption",
        "2024-11-18_justice-gov_phobos-ransomware-administrator-extradited-from-south-korea-to-face-cybercrime-c",
        "2025-02-11_bleepingcomputer-com_us-charges-phobos-8base-ransomware-operators",
        "2026-04-18_justice-gov_phobos-ransomware-affiliates-arrested-in-coordinated-international-disruption",
        "2026-04-18_justice-gov_phobos-ransomware-administrator-extradited-from-south-korea-to-face-cybercrime-c",
    ],
    "operation-trojan-shield": [
        "2021-06-08_fbi-gov_fbi-and-global-partners-announce-results-of-operation-trojan-shield",
        "2021-06-08_europol-europa-eu_800-criminals-arrested-in-biggest-ever-law-enforcement-operation-against-encrypt",
        "2021-06-08-fbi-operation-trojan-shield",
        "2021-06-08-europol-trojan-shield-an0m",
        "2021-06-08_sdca_anom-enterprise-indictment",
        "2026-04-17_justice-gov_distributor-anom-hardened-encrypted-devices-sentenced-63-months-prison-racketeer",
    ],
    "qakbot-gallyamov-indictment": [
        "2023-08-29_om-nl_qakbot-onschadelijk-gemaakt",
        "2025-05-22_justice-gov_qakbot-gallyamov-indictment",
        "2025-05-22_cdca_qakbot-gallyamov-indictment",
        "2025-05-23_helpnetsecurity-com_danabot-botnet-disrupted-qakbot-leader-indicted",
        "2025-05-23_justice-gov_leader-of-qakbot-malware-conspiracy-indicted-for-involvement-in-global-ransomwar",
    ],
    "goznym-takedown": [
        "2019-05-01_europol-europa-eu_goznym-malware-cybercriminal-network-dismantled-in-international-operation",
        "2019-05-16_justice-gov_goznym-cyber-criminal-network-operating-out-of-europe-targeting-american-entitie",
        "2019-05-16_wdpa_goznym-indictment",
        "2019-12-20_justice-gov_three-members-of-goznym-cybercrime-network-sentenced-in-parallel-multi-national",
        "bbc-goznym-malware-network-dismantling",
        "2019-05-16_bleepingcomputer-com_goznym-cybercrime-group-behind-100-million-damages-dismantled",
    ],
    "operation-haechi-v": [
        "2024-12-02-digwatch-interpol-korea-5500-arrests",
        "2024-12-02-interpol-operation-haechi-v",
        "2024-12-02_interpol_operation-haechi-v",
        "2024-12-02_interpol-int_operation-haechi-v",
        "2024-12-02_interpol-int_interpol-financial-crime-operation-makes-record-5-500-arrests-operation-haechi-v",
        "2024-12-03_dig-watch_interpol-and-south-korea-lead-operation-arresting-over-5500-cybercrime-suspects",
        "2024-11-27_interpol-int-fr_operation-haechi-v-5500-arrests",
        "2024-11-27_interpol-int-es_operation-haechi-v-5500-arrests",
    ],
    "proxy-service-takedown-2026-03": [
        "2026-03-12-eurojust-proxy-service-takedown",
        "2026-03-12_eurojust-europa-eu_servers-used-for-cybercrime-around-the-world-taken-down",
        "2025-05-09_politie-nl_anyproxy-amsterdam-fbi",
        "2025-05-09_politie-nl_internationale-cybercrime-aangepakt-politie-amsterdam-en-fbi-ontmantelen-proxydi",
        "2026-03-13_cyberscoop-com_socksescort-proxy-network-botnet-takedown",
        "2026-03-13_cybernews-com_major-residential-proxy-service-socksescort-down",
        "2026-03-13_techradar-com_major-socksescort-proxy-network-powered-by-linux-malware-taken-down-by-fbi-and-other-police-forces",
    ],
    "korea-cambodia-scam-repatriation": [
        "2025-10-18-korea-cambodia-scam-repatriation",
        "2025-10-18_aljazeera-com_korea-cambodia-scam-centre-repatriation",
        "2025-10-18_aljazeera-com_south-korea-repatriates-64-scam-centre-suspects-from-cambodia",
        "2025-10-21_yna_co_kr_arrest-warrants-issued-for-48-suspects-brought-from-cambodia",
        "2026-01-28_yna_co_kr_136-scam-suspects-nabbed-by-joint-s-korea-cambodia-police-team",
        "2025-12-09_koreatimes-co-kr_trial-begins-for-46-suspects-accused-of-involvement-in-online-scams-in-cambodia",
        "2025-10-20_koreatimes-co-kr_police-seek-arrest-warrants-for-58-scam-suspects-brought-from-cambodia",
    ],
    "korea-china-voice-phishing-qingdao": [
        "2023-09-08-korea-china-voice-phishing-qingdao",
        "2023-09-08_koreatimes-co-kr_seoul-metropolitan-police-and-chinese-police-jointly-arrest-16-voice-phishing-su",
        "2023-09-08_koreatimes-co-kr_korea-china-voice-phishing-joint-operation",
        "2023-09-07_koreatimes-co-kr_police-nab-16-voice-phishing-scam-suspects-based-in-china",
        "2026-04-17_web-archive-org_articleview-html",
    ],
    "operation-de-fr-online-fraud-group-2026": [
        "2026-03-11-eurojust-de-fr-online-fraud-group",
        "2026-03-11_eurojust-europa-eu_judicial-cooperation-key-to-arresting-leaders-of-online-fraud-group",
        "2026-04-14_eurojust_judicial-cooperation-key-to-arresting-leaders-of-online-frau",
    ],
    "de-ch-crypto-mixer-takedown-2025": [
        "2025-12-01-eurojust-de-ch-crypto-mixer-takedown",
        "2025-12-01_coindesk-com_cryptomixer-takedown",
        "2025-12-01_amlintelligence-com_cryptomixer-used-to-mix-13bn-in-bitcoin",
        "2025-12-02_techradar-com_huge-cryptomixer-takedown-sees-feds-seize-over-usd30milion",
        "2025-12-01_heise-de_illegaler-cryptomixer-von-strafverfolgern-zerschlagen",
    ],
    "operation-nervone": [
        "2023-07-05_interpol_operation-nervone-opera1er-arrest",
        "2023-07-05_interpol-int_suspected-key-figure-of-notorious-cybercrime-group-arrested-in-joint-operation",
        "2021-07-05_group-ib-com_interpol-led-operation-takes-down-prolific-cybercriminal",
        "2023-07-05_group-ib_operation-nervone-opera1er",
        "2023-07-05_group-ib_top-investigations_operation-nervone",
        "2023-07-05_group-ib-fr_operation-nervone",
    ],
    "hive-ransomware-takedown": [
        "europol-hive-ransomware-infrastructure-takedown",
        "2023-01-26_europol-europa-eu_cybercriminals-stung-as-hive-infrastructure-shut-down",
        "cbs-news-hive-ransomware-infrastructure-takedown",
        "2026-04-18_justice-gov_socal-man-arrested-federal-charges-alleging-he-schemed-advertise-and-sell-hive",
        "2023-01-26_techcrunch-com_united-states-hive-ransomware-seized",
        "2023-01-26_dw-com_us-german-authorities-block-hive-ransomware-website",
    ],
    "zeus-spyeye-jit-takedown": [
        "europol-zeusspyeye-joint-investigation-team-takedown",
        "2015-06-01_europol-europa-eu_major-cybercrime-ring-dismantled-by-joint-investigation-team",
        "2015-06-30_news-sophos-com_zeus-and-spyeye-crime-syndicate-taken-down-by-europol",
        "2025-06-25_helpnetsecurity-com_the-downfall-of-a-major-cybercrime-ring-exploiting-banking-trojans",
        "2015-06-25_scworld-com_europol-takes-down-high-profile-ukraine-based-cybergang",
    ],
    "zeus-spyeye-takedown": [
        "europol-zeusspyeye-joint-investigation-team-takedown",
        "2015-06-01_europol-europa-eu_major-cybercrime-ring-dismantled-by-joint-investigation-team",
        "2015-06-30_news-sophos-com_zeus-and-spyeye-crime-syndicate-taken-down-by-europol",
        "2025-06-25_helpnetsecurity-com_the-downfall-of-a-major-cybercrime-ring-exploiting-banking-trojans",
        "2015-06-25_scworld-com_europol-takes-down-high-profile-ukraine-based-cybergang",
    ],
    "romania-phishing-takedown-2024": [
        "europol-romania-phishing-network-takedown",
        "2024-01-01_europol-europa-eu_hook-line-and-sinker-cybercrime-network-phishing-bank-credentials-arrested-in-ro",
        "2020-09-29_eurojust-europa-eu_successful-takedown-in-romania-of-an-ocg-carrying-out-elaborated-cybercrime-and-bank-frauds",
        "2020-10-13_incibe-es_operacion-internacional-contra-un-grupo-de-ciberdelincuentes",
        "2020-10-13_incibe-es_en_international-operation-against-group-cybercriminals",
        "2020-09-29_ilmetropolitano-it_hook-line-and-sinker-cybercrime-network-phishing-bank-credentials-arrested-in-romania",
    ],
    "lumma-stealer-takedown": [
        "2025-05-21_blogs-microsoft-com_disrupting-lumma-stealer-microsoft-leads-global-action-against-favored-cybercrim",
        "2025-05-21_justice-gov_lumma-stealer-domain-seizures",
        "2025-05-21_microsoft-com_lumma-stealer-breaking-down-the-delivery-techniques-and-capabilities-of-a-prolif",
        "2025-05-21_microsoft-security-blog_lumma-stealer-analysis",
        "2025-05-21_microsoft_lumma-stealer-global-action",
        "2025-05-21_bleepingcomputer-com_lumma-infostealer-malware-operation-disrupted-2300-domains-seized",
        "2025-05-21_wired-com_lumma-stealer-takedown-disrupted",
    ],
    "phobos-8base-crackdown": [
        "2025-02-11-europol-phobos-8base-ransomware-arrests",
        "2025-02-11_europol_phobos-8base-ransomware-arrests",
        "2025-02-11_europol-europa-eu_phobos-8base-ransomware-arrests",
        "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested",
        "2025-02-11_bleepingcomputer-com_us-charges-phobos-8base-ransomware-operators",
        "2025-02-11_techcrunch-com_authorities-arrest-four-suspected-8base-ransomware-operators-in-global-takedown",
        "2025-02-10_justice-gov_phobos-ransomware-affiliates-arrested-in-coordinated-international-disruption",
        "2024-11-18_justice-gov_phobos-ransomware-administrator-extradited-from-south-korea-to-face-cybercrime-c",
        "2026-04-18_justice-gov_phobos-ransomware-affiliates-arrested-coordinated-international-disruption",
        "2026-04-18_justice-gov_phobos-ransomware-administrator-extradited-south-korea-face-cybercrime-charges",
    ],
    "operation-orion-international": [
        "2024-09-26_interpol-int_20-rescued-144-arrested-in-major-child-abuse-operation-across-south-america",
        "2024-10-15_interpol-int_operation-orion-international",
        "2024-10-15_interpol-int_operation-orion-international-144-arrested-in-major-child-abuse-operation-across",
        "2024-10-15_interpol_operation-orion-international-south-america-csam",
        "2024-10-15-interpol-operation-orion-international",
    ],
    "qqaazz-money-laundering-takedown": [
        "2020-10-01_europol-europa-eu_20-arrests-in-qqaazz-multi-million-money-laundering-case",
        "europol-2bagoldmule-qqaazz-takedown",
        "2020-10-15_wdpa_nazarovi-qqaazz-indictment",
        "2020-10-15_cyberscoop-com_fbi-accuses-russian-money-laundering-qqaazz",
        "2020-10-15_justice-gov_officials-announce-international-operation-targeting-transnational-criminal-orga",
        "2020-10-15_occrp-org_pan-continental-operation-busts-money-launderers-for-europes-cybercriminals",
        "2020-10-16_amlintelligence-com_international-criminals-charged-in-laundering-investigation",
    ],
    "operation-stream-kidflix": [
        "2025-04-04-europol-operation-stream-kidflix",
        "2025-04-04_europol_operation-stream-kidflix-takedown",
        "2025-04-04_securityaffairs-com_europol-led-operation-stream-takes-down-kidflix-csam-platform",
        "2025-04-04_securityaffairs-com_operation-stream-kidflix",
    ],
    "operation-destabilise": [
        "2024-12-04_nationalcrimeagency-gov-uk_operation-destabilise-nca-disrupts-multi-billion-money-laundering-networks",
        "2024-12-04_treasury-gov_treasury-exposes-money-laundering-network-using-digital-assets-to-evade-sanctions",
        "2024-12-04_theguardian_global-investigation-exposes-alleged-billion-dollar-russian-money-laundering-network",
        "2024-12-04_wired_operation-destabilise-money-laundering",
        "2024-12-04_computerweekly-com_nca-takes-out-network-that-laundered-ransomware-payments",
    ],
    "operation-operation-orion-international-144-arrested-in-major-child-abuse-operation-across-south-america": [
        "2024-10-15_interpol-int_operation-orion-international-144-arrested-in-major-child-abuse-operation-across",
        "2024-10-15_interpol-int_operation-orion-international",
        "2024-10-15_interpol_operation-orion-international-south-america-csam",
        "2024-10-15-interpol-operation-orion-international",
    ],
    "operation-orion-international": [
        "2024-10-15_interpol-int_operation-orion-international-144-arrested-in-major-child-abuse-operation-across",
        "2024-10-15_interpol-int_operation-orion-international",
        "2024-10-15_interpol_operation-orion-international-south-america-csam",
        "2024-10-15-interpol-operation-orion-international",
    ],
    "operation-stream-kidflix": [
        "2025-04-04-europol-operation-stream-kidflix",
        "2025-04-04_europol_operation-stream-kidflix-takedown",
        "2025-04-04_securityaffairs-com_europol-led-operation-stream-takes-down-kidflix-csam-platform",
        "2025-04-04_securityaffairs-com_operation-stream-kidflix",
        "2025-04-02_bleepingcomputer-com_police-shuts-down-kidflix-child-sexual-exploitation-platform",
        "2025-05-15_eucrim_pedophile-platform-kidflix-shut-down",
    ],
    "operation-falcon": [
        "interpol-operation-falcon",
        "cyberscoop-operation-falcon",
        "2020-11-25_group-ib_operation-falcon-group-ib-helps-interpol-identify-nigerian-bec-ring-members",
        "2020-11-27_pmnewsnigeria_operation-falcon-three-nigerians-busted-for-cybercrime",
        "2020-11-27_guardian-ng_operation-falcon-nigerian-police-join-interpol-group-ib-to-arrest-three-suspected-tmt-fraudsters",
    ],
    "operation-delilah": [
        "group-ib-operation-delilah-silverterrier-bec",
        "cyberscoop-operation-delilah-silverterrier-bec",
        "2022-05-25_interpol-int_suspected-head-of-cybercrime-gang-arrested-in-nigeria",
        "2022-05-25_bleepingcomputer-com_interpol-arrests-alleged-leader-of-the-silverterrier-bec-gang",
        "2022-05-25_unit42-paloaltonetworks-com_operation-delilah-business-email-compromise-actor",
    ],
    "operation-red-card": [
        "2025-03-24-interpol-operation-red-card",
        "2025-03-24-africanews-operation-red-card",
        "2025-03-24_kaspersky_operation-red-card",
        "2025-03-24_africanews-com_cybercrime-crackdown-306-arrested-in-africa-wide-operation",
        "2025-03-24_interpol-int_more-than-300-arrests-as-african-countries-clamp-down-on-cyber-threats",
        "2025-03-24_kaspersky-com_kaspersky-supports-interpol-led-operation-red-card-resulting-in-over-300-arrests",
        "2025-03-24_techafricanews-com_red-card-for-cybercrime-interpol-and-kaspersky-crack-down-on-african-scammers",
        "2025-03-24_africanews-operation-red-card-full",
    ],
    "operation-secure-interpol": [
        "2025-04-01-interpol-operation-secure-infostealer",
        "2025-04-01_straitstimes-com_more-than-9000-malware-infected-servers-found-by-singapore-based-interpol-ope",
        "2017-04-24_freemalaysiatoday-com_interpol-finds-9000-compromised-websites",
        "2025-04-01_kaspersky-com_kaspersky-supports-interpol-operation-secure",
        "2025-04-01_helpnetsecurity-com_operation-secure-disrupts-global-infostealer-malware-operations",
    ],
    "operation-synergia-ii": [
        "2024-11-06-interpol-operation-synergia-ii",
        "kaspersky-operation-avalanche",
        "2024-11-05_kaspersky-com_interpol-operation-synergia-ii",
        "2024-11-06_group-ib-com_group-ib-supports-interpol-operation-synergia-ii",
        "2024-11-07_arstechnica-com_interpol-operation-synergia-ii-22000-malicious-ips",
    ],
    "operation-talent": [
        "2025-01-30-europol-operation-talent",
        "2025-01-30_justice-gov_cracked-and-nulled-marketplaces-disrupted-international-cyber-operation",
        "2025-01-30_cybernews-com_cracked-and-nulled-seized-in-operation-talent",
        "2025-01-31_infosecurity-magazine_operation-talent-cracked-nulled-dismantled",
        "2025-01-31_bleepingcomputer-com_operation-talent-cracked-nulled",
    ],
    "operation-lyrebird": [
        "group-ib-operation-lyrebird",
        "2021-07-06_interpol-int_suspected-key-actor-arrested-in-morocco-operation-lyrebird",
        "2021-07_portswigger-net_operation-lyrebird-cybercops-nab-moroccan-phish-and-carding-kingpin",
        "2021-09-28_technadu-com_operation-lyrebird-dr-hex-arrest",
        "2021-07-06_darkreading-com_operation-lyrebird-morocco-arrest",
    ],
    "operation-hyperion": [
        "2017-01-01_cyberscoop-com_dark-web-fbi-sting-zcash-operation-hyperion",
        "2016-11-01_fbi-gov_a-primer-on-darknet-marketplaces",
        "2016-10-31_ice-gov_international-darknet-marketplace-enforcement-operation",
        "2016-11-01_police-govt-nz_kiwi-darknet-illegal-drug-buyers-identified-during-worldwide-operation",
        "2016-10-31_om_nl_darknet-website-in-wereldwijde-actieweek-operation-hyperion",
        "2016-11-08_helpnetsecurity-com_dutch-police-takes-over-darknet-market",
    ],
    "operation-wirewire": [
        "fbi-operation-wirewire",
        "2016-12-20_dct_odufuye-nwoke-bec-indictment",
        "2016-12-22_justice-gov_nigerian-nationals-charged-with-operating-business-compromise-scheme",
        "2018-06-12_securityaffairs_operation-wirewire-bec",
        "2018-06-12_welivesecurity_com_74-people-arrested-in-us-led-crackdown-on-email-scams",
        "2018-06-12_infosecurity-magazine_bec-scammers-disrupted-in-multi-million-dollar-swoop",
    ],
    "operation-europol-french-coder-who-helped-extort-british-company-arrested-in-thailand": [
        "europol-rex-mundi-hacking-group-takedown",
        "2018-06-14_europol-europa-eu_europol-french-coder-who-helped-extort-british-company-arrested-in-thailand",
        "2018-05-18_europol-europa-eu_french-coder-who-helped-extort-british-company-arrested-in-thailand",
        "2018-06-19_welivesecurity-com_europol-and-partners-dismantle-prolific-cyber-extortion-gang",
        "2018-06-15_bleepingcomputer-com_europol-dismantles-one-of-the-internets-oldest-hacker-groups",
        "2018-06-15_securityweek-com_french-nationals-arrested-for-rex-mundi-hacks",
        "2018-06-18_infosecurity-magazine_europol-disrupts-rex-mundi-cybercrime-group",
    ],
    "operation-haechi-ii": [
        "interpol-operation-haechi-ii",
        "the-hacker-news-operation-haechi-ii",
        "2021-11-26_bleepingcomputer-com_interpol-arrests-over-1000-suspects-linked-to-cyber-crime",
        "2021-11-30_helpnetsecurity-com_massive-online-crime-crackdown-leads-to-1000-arrests",
        "2021-11-26_interpol-int_more-than-1000-arrests-and-usd-27-million-intercepted-in-massive-financial-crime-crackdown",
    ],
    "qakbot-gallyamov-indictment": [
        "2025-05-22_cdca_qakbot-gallyamov-indictment",
        "2025-05-22_justice-gov_qakbot-gallyamov-indictment",
        "2023-08-29_om-nl_qakbot-onschadelijk-gemaakt",
        "2025-05-23_helpnetsecurity-com_danabot-botnet-disrupted-qakbot-leader-indicted",
        "2023-08-30_eurojust-europa-eu_qakbot-malware-network-dismantled",
    ],
    "marketplace-a-dekhtyarchuk-indictment": [
        "2022-03-16_justice-gov_united-states-v-igor-dekhtyarchuk",
        "2022-03-22_edtx_marketplace-a-dekhtyarchuk-indictment",
        "2022-03-22_justice-gov_russian-national-indicted-in-east-texas-for-cyber-hacking-enterprise",
        "the-cyber-express-marketplace-a-dekhtyarchuk-indictment",
        "2022-03-18_fbi-gov_igor-dekhtyarchuk",
        "2022-03-24_infosecurity-magazine_us-indicts-russian-over-carding-shop",
        "2022-03-24_securityweek-com_russian-operator-cybercrime-marketplace-indicted-us",
    ],
    "zeus-spyeye-jit-takedown": [
        "europol-zeusspyeye-joint-investigation-team-takedown",
        "2015-06-30_news-sophos-com_zeus-and-spyeye-crime-syndicate-taken-down-by-europol",
        "2025-06-25_helpnetsecurity-com_the-downfall-of-a-major-cybercrime-ring-exploiting-banking-trojans",
        "2015-06-25_scworld-com_europol-takes-down-high-profile-ukraine-based-cybergang",
        "2015-06-27_thehackernews-com_europol-arrests-gang-behind-zeus-and-spyeye-banking-malware",
        "2015-06-29_techmonitor-ai_zeus-spyeye-malware-gang-members-arrested-in-ukraine",
    ],
    "zeus-spyeye-takedown": [
        "europol-zeusspyeye-joint-investigation-team-takedown",
        "2015-06-30_news-sophos-com_zeus-and-spyeye-crime-syndicate-taken-down-by-europol",
        "2025-06-25_helpnetsecurity-com_the-downfall-of-a-major-cybercrime-ring-exploiting-banking-trojans",
        "2015-06-25_scworld-com_europol-takes-down-high-profile-ukraine-based-cybergang",
        "2015-06-27_thehackernews-com_europol-arrests-gang-behind-zeus-and-spyeye-banking-malware",
        "2015-06-29_techmonitor-ai_zeus-spyeye-malware-gang-members-arrested-in-ukraine",
    ],
    "operation-contender-2": [
        "2024-04-01-interpol-operation-contender-2",
        "2024-10-08_group-ib_operation-contender-2",
        "2024-10-03_thehackernews-com_interpol-arrests-8-in-major-phishing-and-romance-fraud-crackdown-in-west-africa",
        "2024-10-01_interpol-int-fr_operation-contender-2",
    ],
    "banking-trojan-fraud-sentencing-2017": [
        "bbc-banking-trojan-fraud-sentencing",
        "2025-06-25_helpnetsecurity-com_the-downfall-of-a-major-cybercrime-ring-exploiting-banking-trojans",
        "2015-06-25_scworld-com_europol-takes-down-high-profile-ukraine-based-cybergang",
        "2015-06-27_thehackernews-com_europol-arrests-gang-behind-zeus-and-spyeye-banking-malware",
        "2015-06-29_techmonitor-ai_zeus-spyeye-malware-gang-members-arrested-in-ukraine",
    ],
    "operation-chakra-iii": [
        "2024-09-01_newsonair-gov-in_cbi-operation-chakra-iii-dismantles-virtual-asset-network",
        "2024-10-01_the420-in_operation-chakra-iii-inside-cbi-s-explosive-takedown",
        "2024-07-26_newindianexpress-com_operation-chakra-iii-cbi-arrests-43-operatives",
        "2024-07-26_indianexpress-com_cbi-busts-cyber-crime-network-operating-from-gurugram-43-arrested",
        "2024-07-26_tribuneindia-com_cbi-busts-gurugram-call-centre-that-duped-foreigners-nabs-43-cyber-criminals",
    ],
    "operation-eur-100m-illegal-financial-service-laundering-2025": [
        "2025-01-27_eurojust_illegal-financial-service-launder-millions-busted",
        "2025-01-27_eurojust-europa-eu_criminals-operating-an-illegal-financial-service-to-launder-millions-of-euros-bu",
        "2025-02-07_riskcompliance-biz_criminals-operating-an-illegal-financial-service-to-launder-millions-of-euros-busted",
        "2025-01-27_europeantimes-news_criminals-operating-an-illegal-financial-service-to-launder-millions-of-euros-busted",
    ],
    "operation-eur-3m-online-investment-fraud-2025": [
        "2025-05-13_eurojust_international-coalition-uncovers-eur-3-million-online-investment-fraud",
        "2025-05-13_eurojust-europa-eu_international-coalition-uncovers-eur-3-million-online-investment-fraud",
        "2025-05-13_securityonline-info_europol-cracks-e3m-investment-fraud-global-operation-dismantles-online-scam-network",
        "2025-05-13_globalregulatoryinsights-com_international-coalition-uncovers-eur-3-million-online-investment-fraud",
        "2025-05-08_gracechurchfcp-com_international-coalition-uncovers-e3m-online-investment-fraud",
        "2025-05-13_ilmetropolitano-it_eurojust-coalizione-internazionale-scopre-frodi-sugli-investimenti-online-da-3-mln-di-e",
    ],
    "operation-eur-600m-crypto-scam-network-2025": [
        "2025-11-04_eurojust_decisive-actions-against-cryptocurrency-scammers-earning-over-eur-600-million",
        "2025-11-04_eurojust-europa-eu_decisive-actions-against-cryptocurrency-scammers-earning-over-eur-600-m",
        "2025-11-07_trmlabs-com_eurojust-coordinates-global-crackdown-on-eu600-million-crypto-investment-fraud-network",
        "2025-11-06_thepaypers-com_crypto-scammers-steal-over-eur-600-million-now-arrested",
        "2025-11-04_112wwft-nl_decisive-actions-against-cryptocurrency-scammers-earning-over-eur-600-million",
        "2025-11-06_ifcreview-com_crypto-actions-against-cryptocurrency-scammers-earning-over-eur-600-million",
    ],
    "operation-eur-100m-crypto-investment-fraud-2025": [
        "2025-09-23_eurojust_eurojust-coordinates-action-to-halt-cryptocurrency-fraud-over-100-million-euros-a",
        "2025-09-23_eurojust-europa-eu_eurojust-coordinates-action-to-halt-cryptocurrency-fraud-of-over-100-m",
        "2025-09-23_decripto-org_eurojust-dismantles-eur-100-million-crypto-scam-five-arrests-and-seizures",
        "2025-09-23_world-border-congress_eurojust-coordinates-action-to-halt-cryptocurrency-fraud-of-over-100-million-euros-across-europe",
        "2025-09-23_721news-com_eurojust-coordinates-action-to-halt-cryptocurrency-fraud-of-over-100-million-euros-across-europe",
        "2025-09-23_112wwft-nl_eurojust-coordinates-action-to-halt-cryptocurrency-fraud-of-over-100-million-euros-across-europe",
    ],
    "operation-de-fr-online-fraud-group-2026": [
        "2026-03-11-eurojust-de-fr-online-fraud-group",
        "2026-03-11_eurojust-europa-eu_judicial-cooperation-key-to-arresting-leaders-of-online-fraud-group",
        "2026-04-14_eurojust_judicial-cooperation-key-to-arresting-leaders-of-online-frau",
        "2026-03-11_eurojust-fraud-term_online-fraud-group-france-germany",
        "2026-03-11_eurojust-cybercrime-term_online-fraud-group-france-germany",
        "2026-03-11_pressreleasepoint-com_judicial-cooperation-key-to-arresting-leaders-of-online-fraud-group",
        "2026-03-11_eurojust-germany-term_online-fraud-group-france-germany",
    ],
    "operation-eur-300m-global-credit-card-fraud-2025": [
        "2025-11-05_eurojust_eurojust-coordinates-major-operation-against-eur-300-million-global-credit-card-fraud-18",
        "2025-11-05_eurojust-europa-eu_eurojust-coordinates-major-operation-against-eur-300-million-global-credit-card",
        "2025-11-05_112wwft-nl_eurojust-coordinates-major-operation-against-eur-300-million-global-credit-card-fraud-18-arrests",
        "2025-12-22_eurojusts-cross-border-investigations-2025_credit-card-fraud-roundup",
        "2025-11-05_eurojust-fraud-term_eur-300m-global-credit-card-fraud",
        "2025-11-05_eurojust-newsroom_eur-300m-global-credit-card-fraud",
    ],
    "ddos-for-hire-sweep-2016": [
        "fbi-international-ddos-for-hire-sweep",
        "cyberscoop-international-ddos-for-hire-sweep",
        "2016-12-09_fbi-gov_international-cyber-sweep-nets-ddos-attackers",
        "2016-12-09_cyberscoop-com_ddos-europol-arrest-december-2016",
        "2016-12-12_pcworld-com_dozens-arrested-in-international-ddos-for-hire-crackdown",
        "2016-12-13_securityaffairs-com_dozens-of-teenagers-arrested-by-europol-over-ddos-attacks",
        "2016-12-13_hackread-com_europol-us-authorities-bust-ddos-attackers",
        "2016-12-16_meritalk-com_fbi-tries-to-curb-young-ddos-hackers",
    ],
    "operation-nightfury": [
        "group-ib-operation-nightfury-magecartgetbilling",
        "cyberscoop-operation-nightfury-magecartgetbilling",
        "2020-01-28_techtarget-com_3-magecart-suspects-arrested-in-interpol-operation",
        "2020-01-27_bleepingcomputer-com_first-magecart-hackers-caught-infected-hundreds-of-web-stores",
        "2020-01-25_thehackernews-com_interpol-arrests-3-indonesian-credit-card-hackers-for-magecart-attacks",
        "2020-01-28_infosecurity-magazine_suspected-magecart-hackers-arrested-in-indonesia",
    ],
    "fake-shopping-sites-takedown-2024": [
        "2024-12-04_europol-europa-eu_fraudulent-shopping-sites-tied-to-cybercrime-marketplace-taken-offline",
        "europol-fraudulent-shopping-sites-takedown",
        "2024-12-05_bleepingcomputer-com_police-shuts-down-manson-cybercrime-market-fake-shops-arrests-key-suspects",
        "2024-12-05_thehackernews-com_europol-shuts-down-manson-market-fraud-marketplace-seizes-50-servers",
        "2024-12-05_helpnetsecurity-com_manson-market-shuttered-by-law-enforcement",
        "2024-12-05_techtarget-com_police-bust-cybercrime-marketplace-phishing-network",
    ],
    "operation-germany-romania-trusted-seller-fraud-2025": [
        "2025-06-25_eurojust_large-scale-fraud-using-trusted-online-seller-accounts-uncovered",
        "2025-06-25_eurojust-europa-eu_trusted-seller-accounts-fraud-germany-romania",
        "2025-06-26_ieu-monitoring-com_eurojust-helps-uncover-large-scale-fraud-based-on-trusted-online-seller-accounts",
        "2025-06-27_immuniweb-com_cybercrime-investigations-weekly-trusted-seller-fraud",
        "2025-06-25_eurojust-fraud-term_trusted-seller-accounts-germany-romania",
    ],
    "isoon-apt27-indictment": [
        "2025-03-05_opa_wu-haibo-isoon-indictment",
        "2025-03-05_justice-gov_justice-department-charges-12-chinese-contract-hackers-i-soon-apt27-indictment",
        "2025-03-05_justice-gov_i-soon-apt27-indictment",
        "2025-03-05_wired-com_us-charges-12-alleged-spies-in-chinas-freewheeling-hacker-for-hire-ecosystem",
        "2025-03-06_infosecurity-magazine_us-charges-chinese-hackerforhire",
        "2025-03-05_bleepingcomputer-com_us-charges-chinese-hackers-linked-to-critical-infrastructure-breaches",
        "2025-03-06_thecyberwire-com_us-justice-department-charges-employees-of-chinese-it-contractor-i-soon",
    ],
    "operation-orion-international": [
        "2024-09-26_interpol-int_20-rescued-144-arrested-in-major-child-abuse-operation-across-south-america",
        "2024-10-15_interpol-int_operation-orion-international",
        "2024-10-15_interpol-int_operation-orion-international-144-arrested-in-major-child-abuse-operation-across",
        "2024-10-15_interpol_operation-orion-international-south-america-csam",
        "2024-10-15-interpol-operation-orion-international",
        "2024-09-27_the420-in_interpol-leads-to-144-arrests-and-rescues-20-child-victims-across-south-america",
        "2025-02-01_interpol-int_annual-report-2024-operation-orion-international",
    ],
    "operation-operation-orion-international-144-arrested-in-major-child-abuse-operation-across-south-america": [
        "2024-09-26_interpol-int_20-rescued-144-arrested-in-major-child-abuse-operation-across-south-america",
        "2024-10-15_interpol_operation-orion-international-south-america-csam",
        "2024-10-15-interpol-operation-orion-international",
        "2024-10-15_interpol-int_operation-orion-international",
        "2024-10-15_interpol-int_operation-orion-international-144-arrested-in-major-child-abuse-operation-across",
        "2024-09-27_the420-in_interpol-leads-to-144-arrests-and-rescues-20-child-victims-across-south-america",
        "2025-02-01_interpol-int_annual-report-2024-operation-orion-international",
    ],
    "zambia-golden-top-call-center": [
        "2024-04-15-bitdefender-zambia-golden-top-arrests",
        "2024-04-15_bitdefender-com_zambia-arrests-77-people-in-swoop-on-scam-call-centre",
        "2024-06-05-therecord-zambia-golden-top-guilty-pleas",
        "2024-06-05_therecord-media_chinese-nationals-plead-guilty-to-running-zambia-scam-operation",
        "2024-06-07_apnews-com_22-chinese-nationals-sentenced-to-long-prison-terms-in-zambia-for-multinational-cybercrimes",
        "2024-06-08_zambiamonitor-com_22-chinese-nationals-one-cameroonian-jailed-7-years-with-hard-labour-for-cybercrime",
        "2024-04-11_openzambia-com_chinese-crime-syndicate-raided-in-lusaka",
        "2024-06-11_lusakatimes-com_22-chinese-nationals-sentenced-to-long-prison-terms-in-zambia-for-multinational-cybercrimes",
    ],
    "operation-eur-100m-illegal-financial-service-laundering-2025": [
        "2025-01-27_eurojust_illegal-financial-service-launder-millions-busted",
        "2025-01-27_eurojust-europa-eu_criminals-operating-an-illegal-financial-service-to-launder-millions-of-euros-bu",
        "2025-02-07_riskcompliance-biz_criminals-operating-an-illegal-financial-service-to-launder-millions-of-euros-busted",
        "2025-01-27_europeantimes-news_criminals-operating-an-illegal-financial-service-to-launder-millions-of-euros-busted",
        "2025-01-27_eurojust-fraud-term_illegal-financial-service-laundering",
        "2025-01-27_eurojust-financial-crime-term_illegal-financial-service-laundering",
    ],
    "carding-action-2020": [
        "2020-11-26_group-ib-com_carding-action-2020",
        "2020-11-27_welivesecurity-com_europol-partners-thwart-credit-card-fraud-scheme",
        "2020-11-26_europol-europa-eu_officers-foil-fraudsters-stealing-eur-40-million-in-payment-card-scam",
        "2020-11-26_ukfinance-org-uk_dcpcu-works-with-europol-on-operation-carding-action-2020",
        "2020-12-01_cisomag-com_operation-carding-action-2020-cracks-down-credit-card-scammers",
        "2020-11-30_association-secure-transactions-eu_carding-action-by-police-prevents-e40-million-in-losses",
    ],
    "global-airport-action-day": [
        "2016-10-20_interpol-int_global-airport-action-day-40-countries-nab-193-suspects-in-cybercrime-sting",
        "2016-10-19_interpol-int_global-airport-action-day-targets-airline-ticket-fraudsters",
        "hackread-global-airport-action-day",
        "2016-10-19_helpnetsecurity-com_major-international-law-enforcement-operation-targets-airline-ticket-fraud",
        "2017-01-01_europol-socta-2017_global-action-against-airline-fraudsters",
        "2016-10-19_ilmetropolitano-it_global-action-against-airline-fraudsters-193-detained",
    ],
    "korea-china-voice-phishing-qingdao": [
        "2023-09-08-korea-china-voice-phishing-qingdao",
        "2023-09-08_koreatimes-co-kr_seoul-metropolitan-police-and-chinese-police-jointly-arrest-16-voice-phishing-su",
        "2023-09-08_koreatimes-co-kr_korea-china-voice-phishing-joint-operation",
        "2023-09-07_koreatimes-co-kr_police-nab-16-voice-phishing-scam-suspects-based-in-china",
        "2026-04-17_web-archive-org_articleview-html",
        "2023-09-07_yna-co-kr_police-nab-16-voice-phishing-scam-suspects-based-in-china",
        "2023-09-07_asiae-co-kr_16-members-of-voice-phishing-organization-based-in-qingdao-china-arrested",
    ],
    "operation-contender-2": [
        "2024-04-01-interpol-operation-contender-2",
        "2024-10-08_group-ib_operation-contender-2",
        "2024-10-08_group-ib-com_group-ib-supports-interpol-in-operation-contender-2-0-leading-to-the-arrest-of-c",
        "2024-10-03_thehackernews-com_interpol-arrests-8-in-major-phishing-and-romance-fraud-crackdown-in-west-africa",
        "2024-10-01_interpol-int-fr_operation-contender-2",
        "2024-10-02_aptantech-com_operation-contender-2-leads-to-arrests-of-8-cybercrime-suspects",
        "2024-10-04_bitdefender-com_international-phishing-ring-dismantled-in-major-interpol-sweep",
    ],
    "operation-12-members-of-an-irish-high-risk-criminal-network-arrested": [
        "2024-11-01_europol-europa-eu_12-members-of-an-irish-high-risk-criminal-network-arrested",
        "2025-03-28_dia-interno-gov-it_operazione-pereira23-irish-high-risk-criminal-network",
        "2025-03-28_cde-ual-es_12-members-of-an-irish-high-risk-criminal-network-arrested",
        "2025-03-27_irishtimes-com_spanish-police-say-irelands-family-drugs-gang-enjoyed-high-economic-status-and-influence",
        "2025-03-27_irishtimes-com_spanish-police-find-irish-family-drugs-gang-in-three-regions-seize-30m-in-drugs-four-trucks",
        "2025-03-26_irishpost-com_investigation-into-high-risk-criminal-network-sees-12-arrested-in-ireland-and-spain",
    ],
}


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def collection_url(slug: str) -> str:
    path = SOURCES_DIR / f"{slug}.md"
    if not path.exists():
        return ""
    try:
        post = frontmatter.load(path)
    except Exception:
        return ""
    return str(post.metadata.get("collection_url") or "").strip()


def unique_by_url(items: list[str]) -> list[str]:
    seen_slug: set[str] = set()
    seen_url: set[str] = set()
    out: list[str] = []
    for item in items:
        if not item or item in seen_slug:
            continue
        seen_slug.add(item)
        url = collection_url(item)
        if url and url in seen_url:
            continue
        if url:
            seen_url.add(url)
        out.append(item)
    return out


def existing_source_slugs(meta: dict) -> list[str]:
    values = meta.get("sources") or []
    if isinstance(values, str):
        values = [values]
    out: list[str] = []
    for value in values:
        text = str(value or "").strip()
        if text.startswith("[[") and text.endswith("]]"):
            text = text[2:-2].split("|", 1)[0].strip()
        if text and (SOURCES_DIR / f"{text}.md").exists():
            out.append(text)
    return out


def build_refs(source_slugs: list[str]) -> str:
    lines = [
        "## References",
        "",
        "| # | Title | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    for idx, slug in enumerate(source_slugs, start=1):
        post = frontmatter.load(SOURCES_DIR / f"{slug}.md")
        meta = post.metadata
        lines.append(
            f"| [{idx}] | {str(meta.get('title') or slug).replace('|', ' ')} | "
            f"{str(meta.get('publisher') or 'Unknown').replace('|', ' ')} | "
            f"{str(meta.get('publish_date') or 'Unknown').replace('|', ' ')} | "
            f"{str(meta.get('collection_url') or '').replace('|', '%7C')} |"
        )
    return "\n".join(lines) + "\n"


def replace_refs(content: str, refs: str) -> str:
    marker = "\n## References"
    idx = content.find(marker)
    if idx != -1:
        return content[:idx].rstrip() + "\n\n" + refs.rstrip() + "\n"
    if content.startswith("## References"):
        return refs.rstrip() + "\n"
    pattern = re.compile(r"\n## References\s*$.*", re.DOTALL)
    if pattern.search(content):
        return pattern.sub("\n" + refs.rstrip() + "\n", content).rstrip() + "\n"
    return content.rstrip() + "\n\n" + refs


def main() -> None:
    updated = 0
    reached_five = 0
    for slug, seed_slugs in sorted(SEEDS.items()):
        op_path = OPS_DIR / f"{slug}.md"
        if not op_path.exists():
            continue
        seeds = [s for s in seed_slugs if (SOURCES_DIR / f"{s}.md").exists()]
        if not seeds:
            continue
        post = frontmatter.load(op_path)
        meta = post.metadata
        before = int(meta.get("source_count") or 0)
        combined = unique_by_url(existing_source_slugs(meta) + seeds)
        meta["sources"] = [f"[[{s}]]" for s in combined]
        meta["source_count"] = len(combined)
        post.content = replace_refs(post.content, build_refs(combined))
        op_path.write_text(frontmatter.dumps(post), encoding="utf-8")
        updated += 1
        if before < 5 <= len(combined):
            reached_five += 1
        print(f"{slug}: {before} -> {len(combined)}")
    print(f"UPDATED {updated}")
    print(f"REACHED_FIVE {reached_five}")


if __name__ == "__main__":
    main()
