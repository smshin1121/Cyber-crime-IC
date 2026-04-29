---
title: Source Duplicate Normalization (2026-04-29)
type: analysis
created: 2026-04-29
updated: 2026-04-29
summary: "Canonical/alias normalization of duplicate source records."
source_count: 0
---
## Summary

Duplicate source records were normalized without deleting pages. Canonical source pages remain the primary records, while alternates stay addressable and carry `duplicate_of` metadata so audits can distinguish active duplicate records from preserved aliases.

- Mode: **apply**
- Source pages scanned: **4765**
- Duplicate URL groups considered: **942**
- Duplicate content-hash groups considered: **64**
- Content-hash normalization: **enabled**
- New/updated URL aliases: **2**
- New/updated content-hash aliases: **9**
- Total alias-marked source pages after normalization: **1177**

## Alias Changes

| Rank | Alias | Canonical | Reason | Key |
|---:|---|---|---|---|
| 1 | [[2025-03-24_africanews-operation-red-card-full]] | [[2025-03-24_africanews-com_cybercrime-crackdown-306-arrested-in-africa-wide-operation]] | same_collection_url | https://africanews.com/2025/03/24/cybercrime-crackdown-306-arrested-in-africa-wide-operation |
| 2 | [[2020-11-01_guardian-ng_google-vignette]] | [[2020-11-27_guardian-ng_operation-falcon-nigerian-police-join-interpol-group-ib-to-arrest-three-suspected-tmt-fraudsters]] | same_collection_url | https://guardian.ng/news/nigerian-police-join-interpol-group-ib-to-arrest-three-suspected-tmt-fraudsters |
| 3 | [[2021-01-27-doj-emotet-disruption]] | [[2021-01-27_mdnc_emotet-disruption-order]] | same_content_hash | sha256:2b95d762c8389358340e9f3df63b19d0bbb7cf7bd54b466a96026f99a2c9a2c1 |
| 4 | [[2017-07-20-doj-alphabay-shutdown]] | [[2017-07-20_justice-gov_alphabay-the-largest-online-dark-market-shut-down]] | same_content_hash | sha256:3bf6845edd75024ab1ca082c030c840fc195c4acac5b1696547c974e8c3bcc94 |
| 5 | [[2025-04-04_europol_operation-stream-kidflix-takedown]] | [[2025-04-04-europol-operation-stream-kidflix]] | same_content_hash | sha256:456c9e68d8e8375a1aa2401c8c16d9cb30b8ddaa4edd46268c2ef956b1f5d426 |
| 6 | [[2024-04-15-bitdefender-zambia-golden-top-arrests]] | [[2024-04-15_bitdefender-com_zambia-arrests-77-people-in-swoop-on-scam-call-centre]] | same_content_hash | sha256:a836c2f89a1eb2cbd352c4eb23b2c189cd018057557137c2e7283c434dffedbe |
| 7 | [[2024-06-05-therecord-zambia-golden-top-guilty-pleas]] | [[2024-06-05_therecord-media_chinese-nationals-plead-guilty-to-running-zambia-scam-operation]] | same_content_hash | sha256:b110724bcfd20174e810ff207731560dc9ecdf9a7f07bc9d9c536084153ed228 |
| 8 | [[2023-01-23_justice-gov_us-v-okpe-et-al-victim-notifications]] | [[2023-01-23_justice-gov_us-v-okpe-et-al]] | same_content_hash | sha256:c1a154522d2858b56be80c4d4a3b46fda7c93b3aa0726c98ef769f7f916d189e |
| 9 | [[2017-07-20-fbi-alphabay-takedown]] | [[2017-07-20_fbi-gov_alphabay-takedown]] | same_content_hash | sha256:ebe554e0f12df8747a8ffe557366be96e8ac2ea2e0f3b668d318a416fb285223 |
| 10 | [[2024-06-28-uk-nca-operation-morpheus-cobalt-strike]] | [[2024-07-03_nationalcrimeagency-gov-uk_national-crime-agency-leads-international-operation-to-degrade-illegal-versions]] | same_content_hash | sha256:f14e26ac55e8e5c81d36e91b89b350e0d0f1307d2c74c469d435eac33a77df04 |
| 11 | [[2021-06-08-fbi-operation-trojan-shield]] | [[2021-06-08_fbi-gov_fbi-and-global-partners-announce-results-of-operation-trojan-shield]] | same_content_hash | sha256:f36c29f175587d2564ef4dbb356d01587f3d3ff546a5dd93309a23c4270a2cd1 |
