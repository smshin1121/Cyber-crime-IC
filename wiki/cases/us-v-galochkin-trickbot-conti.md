---
type: case
title: "United States v. Galochkin et al. (TrickBot/Conti)"
case_number: "N.D. Ohio; M.D. Tenn.; 23CR1166-LAB (S.D. Cal.)"
jurisdiction: "U.S. District Courts: Northern District of Ohio, Middle District of Tennessee, Southern District of California"
jurisdiction_country: "[[united-states]]"
case_type: prosecution
status: indicted
crime_charged:
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
defendants:
  - name: "Maksim Galochkin"
    nationality: Russian
    status: indicted
    sentence: ""
    location_at_arrest: "At large (Russia)"
  - name: "Maksim Rudenskiy"
    nationality: Russian
    status: indicted
    sentence: ""
    location_at_arrest: "At large (Russia)"
  - name: "Mikhail Tsarev"
    nationality: Russian
    status: indicted
    sentence: ""
    location_at_arrest: "At large (Russia)"
  - name: "Andrey Zhuykov"
    nationality: Russian
    status: indicted
    sentence: ""
    location_at_arrest: "At large (Russia)"
  - name: "Vladimir Dunaev"
    nationality: Russian
    status: sentenced
    sentence: "64 months"
    location_at_arrest: "South Korea"
  - name: "Alla Witte"
    nationality: Latvian
    status: sentenced
    sentence: "32 months"
    location_at_arrest: "Miami, Florida"
related_operation: "[[trickbot-operations]]"
ic_elements:
  mlat_requests:
    - "South Korea"
  extradition: "Dunaev (South Korea to US, 2021)"
  evidence_from_abroad:
    []
  foreign_arrests:
    - "South Korea (Dunaev, September 2021)"
  asset_freezing:
    []
cooperating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
  - "[[us-secret-service]]"
legal_frameworks_invoked:
  - "[[mutual-legal-assistance]]"
  - "[[extradition-request]]"
mechanisms_used:
  - "[[mutual-legal-assistance]]"
key_legal_issues:
  - "[[jurisdictional-conflicts]]"
precedent_value: "High — three simultaneous indictments across three federal districts for the same criminal network; South Korea extradition demonstrates global enforcement reach"
source_count: 2
sources:
  - "[[2023-09-07_ndoh-mdtn-sdca_trickbot-conti-indictments]]"
  - "[[2015-05-29_sdny_us-v-ulbricht-sentencing]]"
created: 2026-04-12
updated: 2026-04-12
summary: "United States v. Galochkin et al. encompasses three indictments unsealed on 7 September 2023 across three federal districts, charging nine Russian nationals with conspiracies related to the TrickBot malware and Conti ransomware operations. Two additional defendants (Dunaev and Witte) were charged separately and have been convicted and sentenced. The case demonstrates the sustained prosecution approach required when initial technical disruption (October 2020) fails to permanently disable a botnet."
---
## Summary

United States v. Galochkin et al. encompasses three indictments unsealed on 7 September 2023 across three federal districts, charging nine Russian nationals with conspiracies related to the TrickBot malware and Conti ransomware operations. Two additional defendants (Dunaev and Witte) were charged separately and have been convicted and sentenced. The case demonstrates the sustained prosecution approach required when initial technical disruption (October 2020) fails to permanently disable a botnet.

## Facts

TrickBot was a modular banking trojan and botnet that infected an estimated 1-3 million devices worldwide, serving as a primary delivery mechanism for Ryuk and Conti ransomware. Conti ransomware attacked more than 900 victims worldwide in 47 US states and 31 foreign countries.

The nine defendants occupied specialized roles: Galochkin (aka "Bentley") was a leader/manager, Rudenskiy (aka "Buza") was a lead developer, Tsarev (aka "Mango") handled administration, and Zhuykov (aka "Defender") was a manager.

## International Cooperation Elements

### Arrest and Extradition — South Korea

Vladimir Dunaev, a TrickBot developer, was arrested in [[south-korea|South Korea]] in September 2021 at the request of the United States. He was extradited in October 2021, pleaded guilty in November 2023, and was sentenced to 64 months in January 2024. This arrest demonstrates South Korea's capacity for international cybercrime cooperation.

### Arrest — United States

Alla Witte, a Latvian national, was arrested in Miami in February 2021. She pleaded guilty in June 2023 and was sentenced to 32 months.

## Legal Analysis

### Jurisdiction

Three separate federal districts brought charges: the N.D. Ohio (TrickBot), M.D. Tennessee (Conti), and S.D. California (additional charges). Maximum penalties: 62 years (TrickBot), 25 years (Conti).

### Key Legal Issues

- **Multi-district charging design:** The case divides a single criminal ecosystem across multiple federal courts, raising coordination and narrative-consistency challenges.
- **Custody asymmetry:** The prosecution secured real defendants through Miami and South Korea while the core Russian defendants remain outside US reach.

### Precedent Value

**High.** The multi-district, multi-indictment approach to a single criminal network, combined with the South Korea extradition, establishes a model for sustained prosecution of Russian-origin cybercrime groups.

## Proceedings Timeline

| Date | Event |
|------|-------|
| 2020-10-12 | TrickBot disruption by US Cyber Command and Microsoft |
| 2021-02 | Alla Witte arrested in Miami |
| 2021-09 | Vladimir Dunaev arrested in South Korea |
| 2021-10 | Dunaev extradited to US |
| 2023-06 | Witte sentenced to 32 months |
| 2023-09-07 | Three indictments unsealed charging 9 defendants |
| 2023-11-30 | Dunaev pleads guilty |
| 2024-01 | Dunaev sentenced to 64 months |

## Cooperation Effectiveness

The Dunaev extradition from South Korea is *almost certainly* one of the most significant demonstrations of US-Korea cybercrime cooperation. The sustained prosecution campaign (2021-2024) produced convictions even after the initial technical disruption was assessed as having only "short-term impact."

## Korean Relevance (한국 관련성)

South Korea played a direct role: arresting Dunaev in September 2021 and extraditing him to the United States. This is a notable example of Korea's role as a reliable partner in international cybercrime enforcement, cooperating even when the criminal activity did not directly target Korean interests (한국이 직접 피해를 입지 않은 사건에서도 국제 사이버범죄 공조에 참여한 의미 있는 사례).

## Contradictions & Open Questions

1. The nine indicted Russian nationals remain at large in Russia; extradition is *highly unlikely* given current geopolitics.
2. The legal basis for US Cyber Command's offensive operations against TrickBot has not been publicly disclosed.
3. Maximum penalties of 62 years are *almost certainly* aspirational given the fugitive status of most defendants.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | Multiple Foreign Nationals Charged (TrickBot/Conti) | DOJ OPA | 2023-09-07 | https://www.justice.gov/archives/opa/pr/multiple-foreign-nationals-charged-connection-trickbot-malware-and-conti-ransomware |
| 2 | Galochkin et al. Indictment (M.D. Tenn.) | DOJ | 2023-09 | https://www.justice.gov/d9/2023-09/trickbot_conti_mdtn_indictment.pdf |
| 3 | Galochkin Indictment (S.D. Cal.) | DOJ | 2023-09 | https://www.justice.gov/d9/2023-09/trickbot_conti_sdca_indictment.pdf |
