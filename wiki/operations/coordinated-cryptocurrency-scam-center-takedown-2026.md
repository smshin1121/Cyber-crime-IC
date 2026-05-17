---
type: operation
title: "Coordinated Cryptocurrency Scam-Center Takedown (Dubai-Led, 2026)"
title_ko: "조정된 암호화폐 스캠센터 단속 (두바이 주도, 2026)"
aliases:
  - "Dubai-led scam center takedown 2026"
  - "276-arrest scam center takedown"
case_id: CYB-2026-008
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - indictment
outcome: success
timeframe:
  announced: 2026-04-29
  start: 2025
  end: 2026-04
  ongoing: false
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
target_entity: "Cryptocurrency-investment scam compounds operated as 'Ko Thet Company' (a.k.a. 'Pixy'), 'Sanduo Group', and 'Giant Company' — pig-butchering schemes targeting US and other victims"
lead_agency: "[[dubai-police]]"
coordinating_body: "[[fbi]]"
participating_countries:
  - "[[united-states]]"
  - "[[united-arab-emirates]]"
  - "[[china]]"
  - "[[thailand]]"
participating_agencies:
  - "[[dubai-police]]"
  - "[[fbi]]"
  - "[[china-mps]]"
  - "[[thailand-royal-police]]"
  - "[[us-doj]]"
  - "[[us-secret-service]]"
  - "[[interpol]]"
organizations:
  - "[[dubai-police]]"
  - "[[fbi]]"
  - "[[china-mps]]"
  - "[[thailand-royal-police]]"
  - "[[us-doj]]"
  - "[[us-secret-service]]"
  - "[[interpol]]"
mechanisms_used:
  - "[[informal-cooperation]]"
  - "[[search-seizure]]"
  - "[[public-private-cooperation]]"
legal_basis:
  - "18 U.S.C. § 1349 (wire fraud conspiracy)"
  - "18 U.S.C. § 1343 (wire fraud)"
  - "18 U.S.C. §§ 1956(h), 1956(a)(2)(A), 1956(a)(2)(B)(i) (money laundering conspiracy)"
results:
  arrests: 276
  indictments: 6
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "At least 276 individuals arrested across at least nine scam centers; 275 by Dubai Police, 1 by Royal Thai Police"
    - "Six defendants charged in the Southern District of California with wire fraud and money laundering conspiracy (one indictment, two complaints)"
    - "Targeted three named operating entities: 'Ko Thet Company' (a.k.a. 'Pixy'), 'Sanduo Group', and 'Giant Company'"
    - "Investigation opened in 2025 by FBI San Diego under the Homeland Security Task Force"
edges:
  - source_actor: fbi
    target_actor: dubai-police
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: fbi
    target_actor: china-mps
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: fbi
    target_actor: thailand-royal-police
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: dubai-police
    target_actor: thailand-royal-police
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - servers_seized
  - domains_seized
  - cryptocurrency_seized
  - victims_notified
related_cases:
  []
related_operations:
  - "[[fbi-san-diego-rtp-tai-chang-tickmilleas-domain-seizure-2025]]"
challenges_encountered:
  []
lessons_learned:
  - "The DOJ release explicitly characterizes the cooperation between FBI, Dubai Police, and Chinese Ministry of Public Security as 'unprecedented', signaling a notable widening of the cooperation footprint for US-led scam-compound investigations beyond traditional Five-Eyes / EU partners."
source_count: 1
sources:
  - "[[2026-04-29_justice-gov_coordinated-takedown-scam-centers-276-arrests]]"
summary: "A 2026 multinational takedown spearheaded by the Dubai Police, under the UAE Ministry of Interior, with cooperation from the US FBI, Chinese Ministry of Public Security, and Royal Thai Police. The action arrested at least 276 individuals across at least nine scam centers tied to cryptocurrency 'pig-butchering' fraud against US victims, and the US Southern District of California unsealed federal wire fraud and money laundering charges against six defendants on 2026-04-29."
created: 2026-05-08
updated: 2026-05-17
---
## Summary

On 2026-04-29 the US Department of Justice unsealed wire fraud and money laundering charges in the Southern District of California against six defendants tied to "pig-butchering" cryptocurrency-investment scam compounds, in coordination with a multinational arrest sweep led by the [[dubai-police|Dubai Police]] under the United Arab Emirates Ministry of Interior. The DOJ release reports that Dubai Police arrested 275 individuals and the [[thailand-royal-police|Royal Thai Police]] arrested one additional defendant; in total at least 276 individuals were arrested and at least nine scam centers were dismantled.

The DOJ release characterizes the cooperation between the [[fbi|FBI]], Dubai Police, and the [[china-mps|Chinese Ministry of Public Security]] as "unprecedented", which is a notable widening of the cooperation footprint for US-led scam-compound investigations beyond the traditional Five-Eyes and EU partners. [[interpol|INTERPOL]] is named as a participating component of the FBI San Diego Homeland Security Task Force structure that conducted the US-side investigation.

## Background

### Modus operandi

The three operating entities — "Ko Thet Company" (a.k.a. "Pixy"), "Sanduo Group", and "Giant Company" — executed the "pig-butchering" (*shā zhū pán*) cryptocurrency-investment fraud pattern at industrial scale. The mechanism follows a standardized multi-stage workflow: (1) initial contact via unsolicited SMS, WhatsApp, Telegram, dating-app messages, or social-media direct messages (Meta Platforms is named as a private-sector partner because Facebook/Instagram were the primary contact-acquisition surfaces); (2) trust-building over weeks-to-months through faux romance, faux friendship, or faux mentorship dialogue scripts read from playbooks; (3) introduction of a fraudulent cryptocurrency-investment platform (often a spoofed "exchange" web/app frontend) showing fake gains on small initial deposits; (4) victim is persuaded to escalate deposits — at the withdrawal stage the platform locks the account, demands "tax/release fees", and ultimately disappears with the funds. Per the DOJ release the schemes used "phony friendship or romance" as the trust vector, with US victims persuaded to invest in fraudulent crypto platforms that the scammers fully controlled.

### Victim profile and impact

The DOJ release identifies US-jurisdiction victims, sourced through IC3 complaints and financial-record analysis, with "millions of dollars in identified victim losses". Although the release does not enumerate the exact number of victims of this specific defendant cohort, the companion Operation Level Up initiative — explicitly contextualized alongside this takedown — has notified nearly 9,000 victims and saved an estimated USD 562 million as of April 2026, indicating the order of magnitude of the broader US victim pool tied to compound-run pig-butchering. Victim demographics typically skew toward middle-aged to elderly US residents with retirement savings.

### Financial flow

Victim funds were transmitted as cryptocurrency from US-side wallets into compound-controlled wallets, then layered through additional wallets and converted, with on-chain laundering consistent with the wire fraud + money laundering conspiracy charges (18 U.S.C. §§ 1956(h), 1956(a)(2)(A), 1956(a)(2)(B)(i)) — outbound international transfers and obfuscatory transfers structured to conceal source. The DOJ release does not disclose specific wallet addresses, total cryptocurrency volume, or the laundering venue.

### Criminal organization structure

The three named operating entities were corporate-style scam compounds, each operating multiple scam centers (at least nine total dismantled). Roles distinguished by the indictment cohort: (a) **managers / executives** (Thet Min Nyi indicted by SDCA grand jury; a fugitive co-defendant), (b) **recruiters** (Awang, Chandra, Mariam charged by criminal complaint), and (c) the broader **scam-worker layer** — the 270 arrestees not federally charged in San Diego, many of whom are themselves trafficking victims coerced into reading scripts at the compounds. Defendant nationalities recorded as Myanmar (Burma) and Indonesia, consistent with the Southeast-Asian compound-economy labour-trafficking pattern. The "Tai Chang Scam Enterprise" in Burma's Karen State is named by DOJ as a related ongoing target, indicating the same regional ecosystem.

The 2026 action against the network is publicly contextualized by the DOJ alongside the FBI San Diego–Phoenix joint initiative known as Operation Level Up (since 2024), and FBI San Diego's ongoing investigation of the "Tai Chang Scam Enterprise" in Burma's Karen State.

## Participating Parties

| Role | Parties |
|---|---|
| Lead apprehending authority | [[dubai-police\|Dubai Police]] under the UAE Ministry of Interior |
| US lead investigator | [[fbi\|FBI]] San Diego Field Office (Homeland Security Task Force) |
| US prosecutorial line | US Attorney's Office for the Southern District of California; CCIPS Trial Attorneys; Office of International Affairs (all components of [[us-doj\|US DOJ]]) |
| Chinese cooperation | [[china-mps\|Chinese Ministry of Public Security]] |
| Thai apprehension and assistance | [[thailand-royal-police\|Royal Thai Police]] (Immigration Bureau, Foreign Affairs, Anti Cyber Scam Center) |
| US task-force partners | FBI, Homeland Security Investigations, DEA, ATF, US Marshals Service, US DoD, US Postal Inspection Service, NCIS, [[us-secret-service\|US Secret Service]], IRS Criminal Investigation, US Coast Guard, US Customs and Border Protection, [[interpol\|Interpol]] |
| Private-sector partner | Meta Platforms, Inc. (parent of Facebook and Instagram) |
| Source-backed participating countries | [[united-states\|United States]], [[united-arab-emirates\|United Arab Emirates]], [[china\|China]], [[thailand\|Thailand]] |
| Defendant nationalities | [[myanmar\|Myanmar]] (Burma), [[indonesia\|Indonesia]] |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2025 | FBI San Diego opens Homeland Security Task Force investigation into scam-compound network | DOJ 2026-04-29 |
| 2026-03 | Grand jury in SDCA returns indictment against Thet Min Nyi and a fugitive co-defendant | DOJ 2026-04-29 |
| 2026-04 (early) | SDCA criminal complaints charge Awang, Chandra, fugitive co-defendant, and Mariam | DOJ 2026-04-29 |
| 2026-04-22 to 2026-04-26 (approx.) | Dubai-led international action — 275 arrests in Dubai, 1 in Thailand, ≥9 scam centers dismantled | DOJ 2026-04-29 ("last week") |
| 2026-04-29 | DOJ unseals charges in San Diego and announces the action publicly (Press Release 26-411) | DOJ 2026-04-29 |

## Results and Impact

- 276+ individuals arrested across at least nine scam centers (275 by Dubai Police, 1 by Royal Thai Police).
- Six defendants charged in the Southern District of California with wire fraud and money laundering conspiracy.
- Three named scam-compound operators identified: Ko Thet Company (a.k.a. "Pixy"), Sanduo Group, Giant Company.
- Millions of dollars in identified victim losses across US-jurisdiction victims, sourced through IC3 complaints and financial-record analysis.
- Operation Level Up (related FBI San Diego–Phoenix initiative) has saved victims an estimated USD 562 million by notifying nearly 9,000 victims as of April 2026.

## Cooperation Mechanisms Used

The DOJ release does not name a specific formal instrument such as MLAT, an extradition request, or a joint investigation team. Cooperation is described in the language of "unprecedented" coordination among the FBI, Dubai Police, and Chinese Ministry of Public Security, with the Royal Thai Police providing apprehension assistance. The pattern is consistent with [[informal-cooperation|informal police-to-police cooperation]] supplemented by domestic charging instruments (US grand jury indictment and criminal complaints) and a private-sector data partnership with Meta Platforms, Inc. The release does not describe the legal basis for the apprehensions in Dubai or Thailand or any subsequent extradition path to the United States.

## Korean Involvement (한국의 참여)

The DOJ release does not name South Korean agencies or victims among the cooperating jurisdictions or among the publicly identified victim or defendant cohort. South Korea is therefore not added to `participating_countries` for this operation. The case is included in the wiki primarily for the rare US–UAE–China–Thailand cooperation pattern and the public-record pig-butchering investigation methodology, which is directly relevant to Korean voice-phishing and investment-fraud cooperation cases tracked elsewhere in this wiki.

## Contradictions & Open Questions

- The exact action-day window is described only as "last week" relative to the 2026-04-29 release; exact dates of the Dubai and Thailand operations are not specified.
- The legal basis for cooperation with the Chinese Ministry of Public Security is not described in the public release; whether information sharing flowed through formal channels (such as direct law-enforcement liaison) or under bilateral arrangements is not stated.
- The release does not enumerate the specific Dubai Police unit, the specific China MPS bureau, or the specific Royal Thai Police unit beyond the named RTP components (Immigration Bureau, Foreign Affairs, Anti Cyber Scam Center).
- Whether the 270 arrested but not federally charged in San Diego face local prosecution in the UAE or Thailand, or repatriation to source jurisdictions, is not described in the cited source.
- **L26 gap — Victim count for this specific defendant cohort:** The cited DOJ release does not enumerate the precise number of victims attributable to the six SDCA defendants or to the "Ko Thet"/"Sanduo"/"Giant" entities specifically; it cites only aggregate "millions of dollars in identified victim losses" and references Operation Level Up's 9,000-victim figure as broader context.
- **L26 gap — Financial flow specifics:** No wallet addresses, on-chain laundering venue/mixer, fiat off-ramp jurisdictions, or aggregate cryptocurrency volume tied to this defendant cohort is enumerated in the cited tier-1 source.
- **L26 gap — OCG hierarchy resolution:** The compound-management hierarchy (whether the three named entities share an upstream owner, whether the compound managers report to a Karen-State or Cambodian/Myanmar-border syndicate parent) is not enumerated in the release.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2026-04-29_justice-gov_coordinated-takedown-scam-centers-276-arrests\|Coordinated Takedown of Scam Centers Leads to at Least 276 Arrests; Alleged Managers and Recruiters Charged in San Diego]] | US DOJ (Office of Public Affairs), Press Release 26-411 | 2026-04-29 | https://www.justice.gov/opa/pr/coordinated-takedown-scam-centers-leads-least-276-arrests-alleged-managers-and-recruiters |
