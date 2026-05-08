---
type: case
title: "United States v. Evgenii Ptitsyn (Phobos Ransomware Administrator, Korea-extradited)"
case_number: "District of Maryland (Greenbelt; specific docket number not enumerated in cited tier-1 source)"
jurisdiction: "District of Maryland (US federal prosecution); arrest and extradition source-state: South Korea"
jurisdiction_country: "[[united-states]]"
case_type: prosecution
status: pleaded-guilty
crime_charged:
  - "[[ransomware-ic]]"
  - "[[hacking-ic]]"
defendants:
  - name: "Evgenii Ptitsyn"
    nationality: "Russia"
    status: "pleaded guilty 2026-03-04 to wire fraud conspiracy (1 count); sentencing scheduled 2026-07-15; maximum penalty 20 years"
    sentence: ""
    location_at_arrest: "South Korea (extradition arrival in US: November 2024)"
related_operation: ""
ic_elements:
  mlat_requests: []
  extradition: "US-South Korea bilateral extradition. Ptitsyn was extradited from South Korea in November 2024 — the first wiki-recorded instance of South Korea extraditing a Russian ransomware administrator to the United States."
  evidence_from_abroad:
    - "[[south-korea]]"
  foreign_arrests:
    - "[[south-korea]]"
  asset_freezing: []
cooperating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[knpa]]"
  - "[[europol-ec3]]"
legal_frameworks_invoked:
  - "[[extradition]]"
  - "[[informal-cooperation]]"
mechanisms_used:
  - "[[extradition]]"
  - "[[informal-cooperation]]"
key_legal_issues:
  - "[[ransomware-ic]]"
  - "[[extradition]]"
precedent_value: "First wiki-recorded Korean-led extradition of a Russian ransomware administrator to the United States. The case is exceptionally Korea-relevant for the wiki's broader Korean cybercrime IC corpus, demonstrating that Korean cooperation extends to non-Korean-victim ransomware-administrator extradition. The 10-country cooperation roster (KR, UK, JP, ES, BE, PL, CZ, FR, RO, plus Europol and US DCCC) is one of the wider multilateral rosters in the wiki for a single ransomware-administrator case."
source_count: 2
sources:
  - "[[2026-03-04_justice-gov-md_russian-ransomware-administrator-pleads-guilty-phobos]]"
  - "[[2026-04-18_justice-gov_phobos-ransomware-administrator-extradited-south-korea-face-cybercrime-charges]]"
created: 2026-04-18
updated: 2026-05-09
last_verified: 2026-05-09
summary: "United States v. Evgenii Ptitsyn is a US federal prosecution in the District of Maryland of a 43-year-old Russian national who administered the Phobos ransomware-as-a-service. Ptitsyn was extradited from South Korea in November 2024 — the first wiki-recorded instance of Korean-led extradition of a Russian ransomware administrator to the United States. He pleaded guilty on 2026-03-04 to one count of wire fraud conspiracy. Phobos, through its affiliates, is alleged to have victimised more than 1,000 public and private entities worldwide and extorted more than USD 39 million in ransom payments. Sentencing scheduled 2026-07-15, maximum 20 years. The 10-country cooperation roster includes South Korea, United Kingdom, Japan, Spain, Belgium, Poland, Czech Republic, France, Romania, plus Europol and the US Department of Defense Cyber Crime Center."
---
## Summary

On 2026-03-04 Russian national **Evgenii Ptitsyn**, 43, pleaded guilty in the District of Maryland (Greenbelt) to one count of **wire fraud conspiracy** for his role as an administrator of **Phobos ransomware**. Phobos ransomware, through its affiliates, is alleged to have victimised more than **1,000 public and private entities** in the United States and around the world and to have extorted more than **USD 39 million** in ransom payments. Ptitsyn was extradited from **South Korea in November 2024**, making this the first wiki-recorded instance of South Korea extraditing a Russian ransomware administrator to the United States. Sentencing is scheduled for **2026-07-15** with a statutory maximum of 20 years.

## Facts

Beginning in at least **November 2020**, Ptitsyn and others conspired to deploy Phobos ransomware against public and private entities through a ransomware-as-a-service (RaaS) operating model. Per the guilty plea, the Phobos administrators developed and offered access to the ransomware to "**affiliates**," operated a darknet website to coordinate sales and distribution, and used online monikers to advertise on criminal forums and messaging platforms. Affiliates hacked into victim networks (often via stolen credentials), exfiltrated and encrypted data, and extorted payment with a double-extortion approach — encrypting data and threatening public release.

The financial-flow architecture is documented in DOJ-charging language: each Phobos deployment was assigned a unique alphanumeric string matching it to its decryption key, and each affiliate paid the decryption-key fee from a unique cryptocurrency wallet. **From December 2021 to April 2024, decryption-key fees were transferred from the unique affiliate cryptocurrency wallets to a wallet Ptitsyn controlled. Ptitsyn also received a portion of the ransomware payments made by victims.**

## International Cooperation Elements

| Element | Detail |
|---|---|
| Foreign arrest | South Korea (Ptitsyn was arrested in South Korea before extradition) |
| Custody-transfer route | South Korea → US (November 2024) |
| Extradition channel | US-South Korea bilateral extradition; specific Korean prosecutorial channel not enumerated in the cited tier-1 source |
| Foreign-resident defendant | Russian national |
| Cooperation roster (verbatim) | South Korea, United Kingdom, Japan, Spain, Belgium, Poland, Czech Republic, France, Romania, plus Europol and the US Department of Defense Cyber Crime Center |
| Multi-jurisdictional victim cohort | 1,000+ public and private entities worldwide; USD 39 million+ extorted |

## Legal Analysis

### Jurisdiction

US federal jurisdiction in the District of Maryland attached through the wire fraud conspiracy count, with US-jurisdiction victims among the 1,000+ worldwide cohort. Defendant was extradited from South Korea in November 2024.

### Key Legal Issues

- **Wire fraud conspiracy** (1 count, 20-year statutory maximum).
- **Phobos administrator-tier prosecution** — Ptitsyn is the first wiki-recorded named Phobos administrator (distinct from affiliate-tier defendants).
- **Korea-as-extradition-state** — first wiki-recorded record of South Korea extraditing a Russian ransomware administrator to the United States.

### Precedent Value

This case is precedent-setting in the wiki corpus on three axes:

1. **Korean extradition of a non-Korean defendant for a non-Korean-victim case** — extends the public-record Korean extradition cooperation pathway to Russia-resident, US-victim ransomware-administrator prosecution.
2. **Phobos administrator-tier prosecution with public-record financial-flow detail** — the December 2021 to April 2024 affiliate-wallet → administrator-wallet transfer pattern is captured directly in DOJ-charging language.
3. **10-country multilateral cooperation roster** — one of the wider multilateral cooperation rosters in the wiki for a single ransomware-administrator case (South Korea + 9 European/Asian partners plus Europol and US DCCC).

## Proceedings Timeline

| Date | Event |
|---|---|
| November 2020 (approx.) | Ptitsyn and co-conspirators begin Phobos ransomware operation |
| December 2021 — April 2024 | Documented period of decryption-key-fee flows from affiliate wallets to Ptitsyn-controlled wallet |
| (date not enumerated in source) | Ptitsyn arrested in South Korea |
| November 2024 | Ptitsyn extradited from South Korea to the United States |
| 2026-03-04 | Ptitsyn pleads guilty in D.Maryland to wire fraud conspiracy |
| 2026-07-15 | Sentencing scheduled |

## Cooperation Effectiveness

The case exemplifies a Korea-led extradition pathway for a Russian ransomware administrator, with explicit DOJ acknowledgement of "law enforcement partners in South Korea, the United Kingdom, Japan, Spain, Belgium, Poland, Czech Republic, France, Romania, and Europol, and the U.S. Department of Defense Cyber Crime Center." The multi-jurisdictional victim cohort and the multi-country cooperation roster make this one of the most coordinated ransomware-administrator extraditions in the wiki corpus.

## Korean Relevance (한국 관련성)

This case is **directly Korea-led**. Korea acted as the extradition source-state, sending Ptitsyn to the United States for prosecution in November 2024. The South Korean extradition pathway is named first in the verbatim DOJ cooperation roster, ahead of the European partners. The case is therefore directly project-relevant for the Korean cybercrime IC corpus and demonstrates Korean cooperation in non-Korean-victim ransomware-administrator extradition. Phobos victims include public and private entities worldwide, and Korean victims may be among the 1,000+ cohort, although specific Korean victim attribution is not enumerated in the cited tier-1 release.

The case adds one more Korean cooperation data point to the wiki corpus alongside:
- The 2025-11-01 [[korea-china-anti-scam-mou-2025|Korea-China bilateral anti-scam MOU]].
- The 2025-11-10 [[korea-cambodia-joint-task-force-mou-2025|Korea-Cambodia Joint Task Force MOU]].
- The 2026-03-03 [[korea-philippines-police-mou-2026-revision|Korea-Philippines police MOU revision]].
- The 2026-04-27 [[korea-cambodia-philippines-73-extradition-2026|Korea-Cambodia-Philippines 73-person extradition]].

## Contradictions & Open Questions

- The specific Korean prosecutorial channel for the Ptitsyn extradition is not enumerated in the cited tier-1 release. Korean MOJ International Criminal Affairs Division and the Seoul High Court are likely candidates but are not directly named.
- The exact date of Ptitsyn's arrest in South Korea (prior to November 2024 extradition) is not enumerated in the cited release.
- The full Phobos affiliate cohort beyond Ptitsyn and the prior-noted [[phobos-8base-crackdown|2025-02 Phobos/8Base operation]] arrests is not itemised in this administrator-tier release.
- Specific Korean-jurisdiction victims among the 1,000+ Phobos cohort are not enumerated.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2026-03-04_justice-gov-md_russian-ransomware-administrator-pleads-guilty-phobos\|Russian Ransomware Administrator Pleads Guilty to Wire Fraud Conspiracy]] | US DOJ USAO-Maryland | 2026-03-04 | https://www.justice.gov/usao-md/pr/russian-ransomware-administrator-pleads-guilty-wire-fraud-conspiracy |
| [2] | [[2026-04-18_justice-gov_phobos-ransomware-administrator-extradited-south-korea-face-cybercrime-charges\|Phobos Ransomware Administrator Extradited from South Korea to Face Cybercrime Charges]] | US DOJ | 2024-11 (extradition); collected 2026-04-18 | https://www.justice.gov/opa/pr/phobos-ransomware-administrator-extradited-south-korea-face-cybercrime-charges |
