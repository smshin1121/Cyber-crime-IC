---
aliases:
  - "In Fraud We Trust"
  - "Infraud takedown"
case_id: CYB-2018-003
challenges_encountered:
  - "alias-to-identity attribution across a large carding forum"
  - "cross-border arrests and extradition follow-through"
  - "long-duration undercover access to criminal forum activity"
coordinating_body: "[[us-doj|US DOJ]]"
created: 2026-04-08
credibility_index: 4.1
crime_type: "[[cybercrime-forum-ic]]"
crime_types:
  - "[[cybercrime-forum-ic]]"
  - "[[carding-fraud-ic]]"
  - "[[identity-theft]]"
  - "[[dark-web-ic]]"
  - "[[malware-ic]]"
edges:
  - cooperation_type: prosecution_coordination
    direction: directed
    legal_basis: "U.S. District of Nevada superseding indictment"
    source_actor: "US DOJ"
    target_actor: "Infraud Organization defendants"
  - cooperation_type: undercover_investigation
    direction: directed
    legal_basis: "criminal investigation"
    source_actor: "Homeland Security Investigations"
    target_actor: "Infraud Organization forum"
  - cooperation_type: arrest_and_extradition_support
    direction: undirected
    legal_basis: "foreign law-enforcement cooperation; specific instruments not fully identified in public sources"
    source_actor: "United States"
    target_actor: "Thailand and other arrest jurisdictions"
enforcement_type:
  - indictment
  - arrest
  - takedown
  - extradition
lead_agency: "[[us-doj|US DOJ]]"
legal_basis:
  - "U.S. District of Nevada nine-count superseding indictment"
  - "racketeering conspiracy and cyber-enabled fraud charges"
  - "foreign arrest and extradition cooperation; country-specific instruments not fully specified in public sources"
lessons_learned:
  - "Large cybercrime-forum takedowns require years of identity resolution rather than a single infrastructure seizure."
  - "Alias-to-person mapping from specialist cybercrime reporting is useful, but official charging documents remain the controlling source for counts and legal posture."
  - "Follow-on pleas and sentencings should be linked as related cases, not merged into the 2018 takedown results."
mechanisms_used:
  - "undercover forum infiltration"
  - "superseding indictment unsealing"
  - "coordinated multi-country arrests"
  - "extradition requests and follow-on transfers"
  - "RICO-based prosecution"
  - "alias-to-identity attribution"
missing_fields:
  - "formal legal-assistance instrument for each non-U.S. arrest jurisdiction"
operation_role: umbrella
operation_type: takedown
organizations:
  - "[[us-doj|US DOJ]]"
  - "[[us-dhs|DHS / HSI]]"
  - "[[fbi-cyber-division|FBI Cyber Division]]"
outcome: success
parent_operation: ""
participating_agencies:
  - "[[us-doj|US DOJ]]"
  - "[[us-dhs|DHS / HSI]]"
  - "[[fbi-cyber-division|FBI Cyber Division]]"
  - "[[thailand-royal-police|Thai law enforcement]]"
participating_countries:
  - "[[united-states]]"
  - "[[australia]]"
  - "[[united-kingdom]]"
  - "[[france]]"
  - "[[italy]]"
  - "[[kosovo]]"
  - "[[serbia]]"
  - "[[thailand]]"
period: 1
related_cases:
  - "[[us-v-bondarenko-infraud]]"
  - "[[us-v-telusma-infraud]]"
related_operations:
  - "[[operation-us-v-bondarenko-infraud]]"
  - "[[infraud-telusma-sentencing]]"
results:
  arrests: 13
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 36
  other:
    - "포럼 최대 등록 회원 약 10,901명"
    - "실제 피해액 5억 3천만 달러 초과, 의도 피해액 22억 달러 초과"
    - "포럼 활동과 연결된 신용카드, 직불카드, 은행계좌 약 430만 건"
    - "Sergey Medvedev가 2018-02-02 방콕에서 미국 요청에 따라 체포됨"
    - "후속 기소에서 여러 Infraud 관리자와 회원의 유죄 인정 및 징역형이 확인됨"
  servers_seized: 0
  victims_notified: 0
source_count: 7
source_tier: 1
sources:
  - "[[2018-02-07_justice-gov_thirty-six-defendants-indicted-for-alleged-roles-in-transnational-criminal-organ]]"
  - "[[krebs-on-security-infraud-organization-takedown]]"
  - "[[wired-infraud-organization-takedown]]"
  - "[[cbs-news-infraud-organization-takedown]]"
  - "[[voa-infraud-organization-takedown]]"
  - "[[2018-02-07_cyberscoop_infraud-doj-arrests-svyatoslav-bondarenko-sergey-medvedev]]"
  - "[[2018-02-08_abc-net-au_9407622]]"
status: completed
summary: "The Infraud Organization takedown was a US DOJ-led enforcement action against a transnational carding and identity-theft forum founded in 2010 under the slogan 'In Fraud We Trust.' Public sources support 36 indicted defendants, 13 arrests, more than USD 530 million in actual losses, more than USD 2.2 billion in intended losses, and a multi-year undercover investigation that included HSI forum access and foreign arrest support."
target_entity: "Infraud Organization cybercrime forum"
timeframe:
  announced: "2018-02-07"
  end: "2018-02-07"
  ongoing: false
  start: "2014"
title: "Infraud Organization Takedown"
title_ko: "인프라우드 조직 소탕"
type: operation
updated: 2026-04-28
---

## Summary

The Infraud Organization takedown was a U.S. Department of Justice-led enforcement action against a transnational cybercrime forum that specialized in carding, identity theft, stolen payment data, malware and related criminal services. The District of Nevada unsealed a nine-count superseding indictment on 2018-02-07 charging 36 defendants for alleged roles in the organization.

The action is retained as a canonical operation because the public record describes an operation-level disruption of the Infraud Organization, not merely a single defendant prosecution. The canonical result is 36 defendants charged and 13 arrests. Public reporting also identifies additional foreign arrest and extradition activity, including Sergey Medvedev's arrest in Bangkok on 2018-02-02 at U.S. request.

The core evidentiary record is stronger than the previous page suggested. It is not a media-only record: the source set includes an official DOJ charging announcement and multiple independent cybercrime or mainstream news accounts that corroborate the forum scale, loss figures, arrest count and undercover-investigation timeline.

## Target and Threat Model

Infraud was founded in October 2010 by Ukrainian Svyatoslav Bondarenko and used the slogan "In Fraud We Trust." The organization presented itself as a marketplace and coordination forum for purchasing and selling stolen identity data, credit-card and debit-card data, bank-account data, malware, ATM skimming tools and other cybercrime services.

The forum's operational value came from scale and trust. Source material describes roughly 10,901 registered members at peak and a structured criminal marketplace with administrators, super-moderators, vendors and escrow functions. This made the target analytically closer to a criminal-service platform than to a loose discussion board.

## Investigation and Enforcement Model

The public sources support a multi-year investigation rather than a single-day raid. CBS/AP reporting attributes the investigation start to 2014, when Homeland Security Investigations used an undercover agent inside the forum. Wired and Krebs describe the action as the result of sustained multinational coordination and long-running identity work against aliases, administrators and vendors.

The 2018 enforcement package combined a U.S. indictment with coordinated arrests and extradition follow-through. The DOJ indictment supplied the legal frame; HSI and other investigative components supplied forum access and identity resolution; foreign law-enforcement partners carried out or supported arrests in several countries.

## Participating Parties

| Actor | Role |
|---|---|
| [[us-doj\|US DOJ]] / District of Nevada | Charging authority, indictment and public enforcement announcement |
| [[us-dhs\|DHS / HSI]] | Undercover forum access and investigative work reported by CBS/AP |
| [[fbi-cyber-division\|FBI Cyber Division]] | U.S. federal cybercrime investigative partner recorded in the operation corpus |
| [[thailand-royal-police\|Thai law enforcement]] | Arrest support for Sergey Medvedev in Bangkok at U.S. request |
| Foreign law-enforcement partners | Arrest and extradition support across Australia, the United Kingdom, France, Italy, Kosovo and Serbia |

The structured country list records countries directly tied to arrests or operational support in the source set: United States, Australia, United Kingdom, France, Italy, Kosovo, Serbia and Thailand. Sources also describe defendants and administrators from other countries, including Ukraine, Russia, Moldova and North Macedonia, but defendant nationality is not the same as participating-country status.

## Results and Impact

| Metric | Source-supported value |
|---|---:|
| Defendants charged | 36 |
| Arrests | 13 |
| Forum peak membership | 10,901 |
| Actual losses | More than USD 530 million |
| Intended losses | More than USD 2.2 billion |
| Payment records associated with forum activity | Approximately 4.3 million |
| Publicly identified core foreign arrest | Sergey Medvedev in Bangkok, 2018-02-02 |

No reliable source in the current page source set gives a confirmed domain-seizure or server-seizure count for the Infraud takedown. Those fields remain zero in metadata to avoid inventing infrastructure results from a prosecution-centered record.

## Defendant and Case Structure

The indictment named Svyatoslav Bondarenko, also known as "Obnon," "Rector" and "Helkern," as the founder of Infraud. Sergey Medvedev, also known as "Stells" and "segmed," is described in source material as a co-founder, payment-system operator and later forum administrator or owner after Bondarenko disappeared in 2015.

Krebs on Security contributes the strongest open-source alias-to-identity mapping for several forum actors, including Jose Gamboa, Andrey Sergeevich Novak and Sergey Kozerev. The operation page should use those mappings as investigative context, while treating the DOJ indictment as controlling for charges and official counts.

Follow-on prosecution outcomes are related case material, not new operation results. Later records include guilty pleas and sentencings for defendants such as Sergey Medvedev, Marko Leopard and John Telusma. Those records should remain linked as related cases or absorbed follow-on pages rather than being merged into the 2018 operation totals.

## Legal and Procedural Posture

The controlling legal event was the unsealing of a nine-count superseding indictment in the U.S. District Court for the District of Nevada. The source set identifies racketeering conspiracy and cyber-enabled fraud conduct, with related charges covering identity theft, wire fraud, access-device or payment-card fraud and computer-fraud activity.

Public sources do not identify the exact formal legal-assistance instrument used for each non-U.S. arrest jurisdiction. The page therefore records foreign arrest and extradition support as operational cooperation, while carrying `formal legal-assistance instrument for each non-U.S. arrest jurisdiction` as a missing field.

## Operational Timeline

| Date | Event |
|---|---|
| 2010-10 | Infraud Organization founded under the "In Fraud We Trust" slogan |
| 2014 | HSI undercover access to the forum reportedly began |
| 2018-02-02 | Sergey Medvedev arrested in Bangkok at U.S. request |
| 2018-02-07 | DOJ announced the unsealing of the District of Nevada indictment charging 36 defendants |
| 2018-02-07 to 2018-02-08 | Public reporting described coordinated arrests across multiple countries |
| 2020 to 2022 | Follow-on guilty pleas and sentencings documented the prosecution phase for several Infraud members |

## Source Coverage

- US DOJ, 2018-02-07: official indictment announcement and controlling charge count.
- Krebs on Security, 2018-02-08: specialist cybercrime reporting with alias-to-identity mapping and carding-market context.
- Wired, 2018-02-08: narrative account of the takedown, forum longevity, 16-country cooperation framing and 13-arrest/36-charge result.
- CBS News/AP, 2018-02-09: Medvedev arrest in Bangkok, HSI undercover-investigation start date and cross-border arrest context.
- VOA, 2018-02-09: Thai arrest and extradition angle, useful for the cooperation record but secondary to DOJ and CBS/AP.
- CyberScoop, 2018-02-07: independent cyber-trade confirmation of Bondarenko/Medvedev roles and loss figures.
- ABC News Australia, 2018-02-08: Australian-angle corroboration for the global cybercrime-ring arrest story.

## Source Findings

- DOJ and the District of Nevada source set support 36 charged defendants and more than USD 530 million in actual losses.
- Wired, Krebs and CBS/AP independently support the 13-arrest figure and the forum's 2010 origin.
- Wired and VOA support roughly 10,900 active or registered members and approximately 4.3 million payment-card or bank-account records tied to the forum.
- CBS/AP and VOA identify Sergey Medvedev's arrest in Bangkok as a distinct foreign-arrest event preceding the public DOJ announcement.
- Krebs provides the most detailed open-source mapping of forum aliases to real-world identities and vendor roles.
- The sources do not support treating every later Infraud sentencing as a new international operation.

## Data Quality Notes

The earlier version of this page incorrectly had `source_count: 7` with an empty `sources` list. That made the rendered page and the graph layer disagree with the reference table. This version repairs the source list and replaces numeric parser titles such as `9407622`, `31160664` and `4246130` with source records that have meaningful titles.

The previous page also described the record as media-only even though official DOJ material exists. The page now records `source_tier: 1` because the canonical fact pattern is anchored in a DOJ charging announcement, then supplemented by specialist and mainstream reporting.

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes the takedown of the Infraud Organization as a criminal forum and enterprise. Defendant-specific pleas, extraditions and sentencings should attach to this record as related cases or absorbed follow-on pages.

The operation-level facts that should be used for quantitative analysis are: 36 charged defendants, 13 arrests, more than USD 530 million in actual losses, more than USD 2.2 billion in intended losses, roughly 10,901 forum members, and documented cross-border arrest support in at least the countries listed in metadata.

The source floor is met. Remaining uncertainty concerns the exact formal legal-assistance mechanism used for each foreign arrest and the full public accounting of all 36 defendants after the indictment.

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Thirty-Six Defendants Indicted for Alleged Roles in Transnational Criminal Organization Responsible for More Than $530 Million in Losses from Cybercrimes | US DOJ (District of Nevada) | 2018-02-07 | [원본](https://www.justice.gov/usao-nv/pr/thirty-six-defendants-indicted-alleged-roles-transnational-criminal-organization) |
| [2] | U.S. Arrests 13, Charges 36 in 'Infraud' Cybercrime Forum Bust | Krebs on Security | 2018-02-08 | [원본](https://krebsonsecurity.com/2018/02/u-s-arrests-13-charges-36-in-infraud-cybercrime-forum-bust/) |
| [3] | Inside the Takedown of Infraud, the Notorious Cybercrime Forum | Wired | 2018-02-08 | [원본](https://www.wired.com/story/infraud-feds-takedown-cybercrime/) |
| [4] | U.S., Russia, cybercrime: Dark Web market suspect Sergey Medvedev arrested in Thailand | CBS News / AP | 2018-02-09 | [원본](https://www.cbsnews.com/news/us-russia-cybercrime-dark-web-market-suspect-sergey-medvedev-thailand/) |
| [5] | Thais Arrest Alleged Russian Cybercrime Market Operator | Voice of America | 2018-02-09 | [원본](https://www.voanews.com/a/thais-arrest-alleged-russian-cybercrime-market-operator/4246130.html) |
| [6] | Infraud cybercrime ring, responsible for $530 million worth of fraud, broken up by DOJ | CyberScoop | 2018-02-07 | [원본](https://cyberscoop.com/infraud-doj-arrests-svyatoslav-bondarenko-sergey-medvedev/) |
| [7] | Infraud: Australian among 36 arrested in global cybercrime ring | ABC News Australia | 2018-02-08 | [원본](https://www.abc.net.au/news/2018-02-08/infraud-australian-among-36-arrested-in-global-cybercrime-ring/9407622) |
