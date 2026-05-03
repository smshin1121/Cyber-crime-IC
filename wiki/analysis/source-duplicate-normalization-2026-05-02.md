---
title: Source Duplicate Normalization (2026-05-02)
type: analysis
created: 2026-05-02
updated: 2026-05-02
summary: "Canonical/alias normalization of duplicate source records."
source_count: 0
---
## Summary

Duplicate source records were normalized without deleting pages. Canonical source pages remain the primary records, while alternates stay addressable and carry `duplicate_of` metadata so audits can distinguish active duplicate records from preserved aliases.

- Mode: **apply**
- Source pages scanned: **4784**
- Duplicate URL groups considered: **961**
- Duplicate content-hash groups considered: **64**
- Content-hash normalization: **disabled**
- New/updated URL aliases: **14**
- New/updated content-hash aliases: **0**
- Total alias-marked source pages after normalization: **1199**

## Alias Changes

| Rank | Alias | Canonical | Reason | Key |
|---:|---|---|---|---|
| 1 | [[2024-10-15-interpol-operation-orion-international]] | [[2024-10-15_interpol-int_operation-orion-international-144-arrested-in-major-child-abuse-operation-across]] | same_collection_url | https://interpol.int/en/News-and-Events/News/2024/20-rescued-144-arrested-in-major-child-abuse-operation-across-South-America |
| 2 | [[2025-03-24-africanews-operation-red-card]] | [[2025-03-24_africanews-com_cybercrime-crackdown-306-arrested-in-africa-wide-operation]] | same_collection_url | https://africanews.com/2025/03/24/cybercrime-crackdown-306-arrested-in-africa-wide-operation |
| 3 | [[2025-04-07-korea-npa-operation-cyber-guardian]] | [[2025-04-07_korea-kr_operation-cyber-guardian-asia-6-country-joint-crackdown-on-child-sexual-abuse-ma]] | same_collection_url | https://korea.kr/briefing/pressReleaseView.do?newsId=156682866 |
| 4 | [[2017-07-20-dea-alphabay-shutdown]] | [[2017-07-20_dea-gov_alphabay-largest-online-dark-market-shut-down]] | same_collection_url | https://dea.gov/press-releases/2017/07/20/alphabay-largest-online-dark-market-shut-down |
| 5 | [[2024-12-02-digwatch-interpol-korea-5500-arrests]] | [[2024-12-03_dig-watch_interpol-and-south-korea-lead-operation-arresting-over-5500-cybercrime-suspects]] | same_collection_url | https://dig.watch/updates/interpol-and-south-korea-lead-operation-arresting-over-5500-cybercrime-suspects |
| 6 | [[2021-01-27_eurojust-europa-eu_major-operation-to-take-down-dangerous-malware-systems]] | [[2021-01-27-eurojust-emotet-operation]] | same_collection_url | https://eurojust.europa.eu/news/major-operation-take-down-dangerous-malware-systems |
| 7 | [[2021-06-08_europol-europa-eu_800-criminals-arrested-in-biggest-ever-law-enforcement-operation-against-encrypt]] | [[2021-06-08-europol-trojan-shield-an0m]] | same_collection_url | https://europol.europa.eu/media-press/newsroom/news/800-criminals-arrested-in-biggest-ever-law-enforcement-operation-against-encrypted-co... |
| 8 | [[europol-doublevpn-takedown]] | [[2021-06-30_europol-europa-eu_coordinated-action-cuts-off-access-to-vpn-service-used-by-ransomware-groups]] | same_collection_url | https://europol.europa.eu/media-press/newsroom/news/coordinated-action-cuts-access-to-vpn-service-used-ransomware-groups |
| 9 | [[2017-07-20_europol-europa-eu_massive-blow-to-criminal-dark-web-activities-after-globally-coordinated-operatio]] | [[2017-07-20-europol-alphabay-hansa-takedown]] | same_collection_url | https://europol.europa.eu/media-press/newsroom/news/massive-blow-to-criminal-dark-web-activities-after-globally-coordinated-operation |
| 10 | [[2021-01-27_europol-europa-eu_world-s-most-dangerous-malware-emotet-disrupted-through-global-action]] | [[2021-01-27-europol-emotet-disruption]] | same_collection_url | https://europol.europa.eu/media-press/newsroom/news/world%E2%80%99s-most-dangerous-malware-emotet-disrupted-through-global-action |
| 11 | [[2023-03-28_infosecurity-magazine_four-years-behind-bars-for-prolific-bec-scammer]] | [[2023-03-28_infosecurity-magazine-com_four-years-behind-bars-for-prolific-bec-scammer]] | same_collection_url | https://infosecurity-magazine.com/news/four-years-prolific-bec-scammer |
| 12 | [[2022-10-14_interpol_operation-jackal-black-axe]] | [[2022-10-14_interpol-int_international-crackdown-on-west-african-financial-crime-rings]] | same_collection_url | https://interpol.int/News-and-Events/News/2022/International-crackdown-on-West-African-financial-crime-rings |
| 13 | [[2023-03-29_scworld_us-convicts-nigerian-bec-scammer]] | [[2023-03-29_scworld-com_us-convicts-nigerian-bec-scammer]] | same_collection_url | https://scworld.com/brief/us-convicts-nigerian-bec-scammer |
| 14 | [[unodc-alphabay-true-crime-story]] | [[2026-04-17_unodc-org_true-crime-story-alphabay]] | same_collection_url | https://unodc.org/unodc/untoc20/truecrimestories/alphabay.html |
