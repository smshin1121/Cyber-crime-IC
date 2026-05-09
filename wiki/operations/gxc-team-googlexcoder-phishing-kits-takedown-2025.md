---
type: operation
title: "GXC Team / GoogleXcoder Phishing-Kit CaaS Takedown (Spain–Brazil, 2025-10-08)"
title_ko: "GXC Team / GoogleXcoder 피싱 키트 CaaS 단속 (스페인-브라질, 2025-10-08)"
aliases:
  - "GXC Team takedown 2025"
  - "GoogleXcoder arrest Spain 2025"
  - "Guardia Civil GXC Team operation"
  - "Operation GXC Team"
case_id: CYB-2025-410
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - asset_freeze
outcome: success
timeframe:
  announced: 2025-10-08
  start: 2023
  end: 2025-10-08
  ongoing: true
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[bank-fraud-ic]]"
  - "[[malware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
target_entity: "'GXC Team' / 'GoogleXcoder' — Crime-as-a-Service (CaaS) phishing-kit operation active from 2023, principally developed by a 25-year-old Brazilian national. The CaaS sold professionally maintained phishing kits cloning Spanish banking websites and government portals (with customisation, technical support and updates), distributed to Spanish-speaking phishing crews via Telegram for hundreds of euros per day."
lead_agency: "[[spain-guardia-civil]]"
coordinating_body: ""
participating_countries:
  - "[[spain]]"
  - "[[brazil]]"
participating_agencies:
  - "[[spain-guardia-civil]]"
  - "[[brazil-ministry-of-justice-public-security]]"
  - "[[group-ib]]"
organizations:
  - "[[spain-guardia-civil]]"
  - "[[brazil-ministry-of-justice-public-security]]"
  - "[[group-ib]]"
legal_basis:
  - "Spanish criminal-procedural authority of the Juzgado de Instrucción número 1 de San Vicente de la Barquera (Cantabria) — judicial authorisation for the entries and searches in six Spanish localities and for the arrest in Cantabria"
  - "Investigative authority of the Departamento contra el Cibercrimen de la Unidad Central Operativa (UCO) of the Guardia Civil"
  - "Bilateral police-to-police cooperation with the Brazilian Federal Police (Policía Federal de Brasil) for identification and characterisation of the Brazilian-national suspect"
  - "Public-private cooperation with cybersecurity company Group-IB for technical analysis of phishing infrastructure and Telegram-based CaaS distribution"
mechanisms_used:
  - "[[informal-cooperation]]"
  - "[[public-private-cooperation]]"
  - "[[search-seizure]]"
  - "[[cryptocurrency-seizure]]"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1 arrest: the 25-year-old Brazilian national operating under the alias 'GoogleXcoder', detained in San Vicente de la Barquera (Cantabria)"
    - "Six entries-and-searches in Valladolid, Zaragoza, Barcelona, Palma de Mallorca, San Fernando and La Línea de la Concepción"
    - "Seizure of electronic devices containing phishing kits for all impersonated entities, the suspect's personal accounts and conversations with dozens of phishing customers"
    - "Six additional individuals identified as direct users of the CaaS service through more than one year of forensic analysis of seized devices and cryptocurrency transactions"
    - "Recovery of victim funds from various digital platforms (specific amount not disclosed in the cited release)"
    - "Telegram channels used by the network subject to deactivation measures"
    - "Reported impact pre-disruption: millions of euros stolen, thousands of victims, dozens of impersonated Spanish banks and government entities; Telegram criminal group named 'Robarle todo a las abuelas' ('Steal everything from grandmothers')"
edges:
  - source_actor: spain-guardia-civil
    target_actor: brazil-ministry-of-justice-public-security
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: spain-guardia-civil
    target_actor: group-ib
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: directed
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "exact total amount of victim funds recovered (cited release describes recovery in qualitative terms only)"
  - "exact total number of phishing victims and total euro losses (cited release uses 'millions of euros' and 'thousands of victims' generically)"
  - "specific date of the arrest and search day(s) — only the announcement date 2025-10-08 is enumerated"
  - "specific number / value of cryptocurrency transactions reconstructed during forensic analysis"
  - "judicial status of the six additional identified users (charged / indicted / under investigation) — release notes investigation remains open"
  - "names of impersonated Spanish banks and government entities (cited release describes them generically as 'principal banking and public organisms')"
related_cases: []
related_operations:
  - "[[tycoon-2fa-phishing-as-a-service-takedown-2026]]"
  - "[[labhost-phishing-as-a-service-takedown-2024]]"
  - "[[operacion-kaerb-iserver-phishing-as-a-service-takedown-2024]]"
challenges_encountered: []
lessons_learned:
  - "Spanish-language Crime-as-a-Service phishing supply: the GXC Team case shows that a single Spanish-speaking developer based inside Spain can supply industrial-scale phishing tooling for cloning Spanish banks and government portals to dozens of operator crews via Telegram — making developer-side disruption (rather than only operator-side arrests) a prerequisite for materially reducing Spanish-language phishing volume."
  - "Bilateral Spain–Brazil police cooperation pattern for Lusophone / Hispanophone CaaS developers: identification of a Brazilian national operating from Spain required Brazilian Federal Police characterisation alongside Guardia Civil UCO operational tracking, illustrating that nationality-based bilateral cooperation remains decisive even when the suspect physically operates inside the requesting state."
  - "Public-private cooperation with Group-IB provided phishing-infrastructure mapping (250+ phishing sites and 9 Android-malware strains attributed to the actor in private-sector reporting) that complemented the Guardia Civil's judicial case, illustrating the Group-IB private-intelligence + national-LE pattern previously seen in Operation Falcon (Black Axe)."
  - "Telegram-based CaaS distribution (paid in cryptocurrency, with subscription-style customisation/support/updates) is reaffirmed as the dominant channel for Spanish-language phishing toolkit supply — disruption of the seller's Telegram channels is now a routine post-arrest measure."
source_count: 1
sources:
  - "[[2025-10-08_guardiacivil-es_gxc-team-googlexcoder-phishing-kits-arrest]]"
summary: "On 2025-10-08 the Guardia Civil (Spain) announced the dismantling of the GXC Team Crime-as-a-Service phishing-kit operation and the arrest of its main developer, a 25-year-old Brazilian national operating as 'GoogleXcoder'. The investigation, led by the Departamento contra el Cibercrimen of the Unidad Central Operativa (UCO) under the Juzgado de Instrucción número 1 de San Vicente de la Barquera (Cantabria), reached an alleged developer who supplied phishing kits cloning Spanish banks and government websites to dozens of phishing crews via Telegram for hundreds of euros per day. The action concluded with the suspect's arrest in San Vicente de la Barquera and six coordinated entries-and-searches across Valladolid, Zaragoza, Barcelona, Palma de Mallorca, San Fernando and La Línea de la Concepción, with seizure of phishing-kit code, customer chats, and recovery of victim funds from multiple digital platforms. Six additional individuals using the CaaS service were identified through more than one year of device-forensics and cryptocurrency-transaction reconstruction. International cooperation was provided by the Brazilian Federal Police, with private-sector technical support from Group-IB."
created: 2026-05-10
updated: 2026-05-10
---

## Summary

On **2025-10-08** the **[[spain-guardia-civil|Guardia Civil (Spain)]]** announced the dismantling of the **GXC Team** Crime-as-a-Service (CaaS) phishing operation and the arrest of its main developer, a 25-year-old **Brazilian national** operating under the alias **"GoogleXcoder"**, detained in **San Vicente de la Barquera (Cantabria)**. The investigation was led by the **Departamento contra el Cibercrimen de la Unidad Central Operativa (UCO)** of the Guardia Civil, under the judicial authority of the **Juzgado de Instrucción número 1 de San Vicente de la Barquera (Cantabria)**, with international cooperation from the **Brazilian Federal Police (Policía Federal de Brasil)** and private-sector technical support from **[[group-ib|Group-IB]]**.

The action concluded with the suspect's arrest in Cantabria and **six coordinated entries-and-searches** across Valladolid, Zaragoza, Barcelona, Palma de Mallorca, San Fernando and La Línea de la Concepción, with seizure of phishing-kit code, customer chats, and recovery of victim funds from multiple digital platforms. **Six additional individuals** using the CaaS service were identified through more than one year of device forensics and cryptocurrency-transaction reconstruction.

## Background

From **2023** onwards Spain experienced a wave of phishing campaigns impersonating major Spanish banking entities and public-administration bodies, generating thousands of victim reports and millions of euros in losses. The Guardia Civil's UCO Cybercrime Department opened an investigation aimed not only at the operator crews but at the **"brain"** designing the toolkits used by multiple criminal groups.

Investigators traced the supply chain to a developer known as **"GoogleXcoder"** running a **Crime-as-a-Service (CaaS)** business model. The developer designed and sold phishing kits capable of cloning the websites of Spanish banks and government bodies, with customisation, technical support and updates included in the subscription — a professionalised criminal structure.

Operator crews ("phishers") contacted GoogleXcoder via the Telegram messaging application, paid hundreds of euros per day for access to the kits, and used them at industrial scale: **a single day's output could include dozens of impersonated entities, thousands of deceived victims and millions of euros stolen.** One of the operator-side Telegram groups was openly named **"Robarle todo a las abuelas"** ("Steal everything from grandmothers").

The individual behind the GoogleXcoder pseudonym was unknown to law enforcement at both national and international level prior to this investigation. Locating him required complex operational tracking: he moved repeatedly between residences in different Spanish provinces, used phone lines and prepaid payment cards in fraudulent identities, and lived as a **"digital nomad"** with his family.

## Participating Parties

| Country / Sector | Authority / Partner |
|---|---|
| Spain (lead) | [[spain-guardia-civil\|Guardia Civil]] — Departamento contra el Cibercrimen de la Unidad Central Operativa (UCO) |
| Spain (judicial) | Juzgado de Instrucción número 1 de San Vicente de la Barquera (Cantabria) |
| Brazil | [[brazil-ministry-of-justice-public-security\|Brazil Ministry of Justice and Public Security]] — Policía Federal de Brasil (Federal Police of Brazil) |
| Private — technical | [[group-ib\|Group-IB]] |

## Legal Framework

- **Spanish criminal-procedural authority** of the Juzgado de Instrucción número 1 de San Vicente de la Barquera (Cantabria) — judicial authorisation for the entries and searches in six Spanish localities and for the arrest in Cantabria.
- **Investigative authority** of the Departamento contra el Cibercrimen de la Unidad Central Operativa (UCO) of the Guardia Civil under Spanish national criminal procedure.
- **Bilateral police-to-police cooperation** with the Brazilian Federal Police (Policía Federal de Brasil) — informal investigative cooperation for identification and characterisation of the Brazilian-national suspect, consistent with the [[informal-cooperation|informal police-to-police cooperation]] pattern (no MLAT or judicial-cooperation instrument is enumerated in the cited release).
- **Public-private cooperation** with [[group-ib|Group-IB]] under [[public-private-cooperation|public-private cooperation]] arrangements for technical mapping of phishing infrastructure and Telegram-based CaaS distribution.

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2023 (from) | Spain-targeted phishing campaigns impersonating Spanish banks and public bodies begin to proliferate; victim reports, losses in millions of euros and social alarm accumulate | Guardia Civil 2025-10-08 |
| (undated) | UCO Cybercrime Department opens investigation aimed at the developer behind the toolkits | Guardia Civil 2025-10-08 |
| (undated) | Investigators identify "GoogleXcoder" as the principal CaaS developer | Guardia Civil 2025-10-08 |
| (undated, action day) | Arrest of "GoogleXcoder" in San Vicente de la Barquera (Cantabria); six coordinated entries-and-searches in Valladolid, Zaragoza, Barcelona, Palma de Mallorca, San Fernando and La Línea de la Concepción; seizure of phishing-kit code, customer chats and devices | Guardia Civil 2025-10-08 |
| Post-arrest, > 1 year | Forensic analysis of devices and cryptocurrency-transaction reconstruction reconstructs full criminal scheme; six additional users of the CaaS service identified | Guardia Civil 2025-10-08 |
| 2025-10-08 | Guardia Civil announces the dismantling of the GXC Team and the arrest of its main developer | Guardia Civil 2025-10-08 |
| Ongoing | Investigation remains open; further identifications and arrests not ruled out; Telegram channels of the network subject to deactivation measures | Guardia Civil 2025-10-08 |

## Results and Impact

- **1 arrest**: the 25-year-old Brazilian national operating as "GoogleXcoder", detained in San Vicente de la Barquera (Cantabria).
- **6 entries-and-searches** at residences in Valladolid, Zaragoza, Barcelona, Palma de Mallorca, San Fernando and La Línea de la Concepción.
- **Seizure** of electronic devices containing phishing-kit code for all impersonated entities, plus the suspect's personal accounts and conversations with dozens of phishing customers.
- **6 additional individuals identified** as direct users of the CaaS service through more than one year of device forensics and cryptocurrency-transaction reconstruction.
- **Recovery of victim funds** from various digital platforms (specific euro figure not disclosed in the cited release).
- **Telegram channels** used by the network subject to deactivation measures.
- **Pre-disruption impact** (qualitatively reported): "millions of euros stolen", "thousands of victims" and "dozens of impersonated entities" including Spain's principal banks and public bodies, with one operator Telegram group named "Robarle todo a las abuelas".

## Cooperation Mechanisms Used

| Mechanism | Role in this operation |
|---|---|
| [[informal-cooperation\|Informal police-to-police cooperation]] | Bilateral information exchange between the Guardia Civil and the Brazilian Federal Police for identification and characterisation of the Brazilian-national suspect; no MLAT instrument enumerated in the cited release |
| [[public-private-cooperation\|Public-private cooperation]] | Cybersecurity firm [[group-ib\|Group-IB]] supported the investigation with technical mapping of phishing infrastructure and Telegram-based CaaS distribution |
| [[search-seizure\|Search and seizure]] | Six entries-and-searches across Spain executed under judicial authorisation of the Juzgado de Instrucción número 1 de San Vicente de la Barquera |
| [[cryptocurrency-seizure\|Cryptocurrency-transaction reconstruction]] | Multi-year cryptocurrency-transaction analysis used to reconstruct the criminal scheme and identify CaaS users; partial recovery of victim funds from digital platforms |

## Challenges and Friction Points

- **Suspect anonymity prior to investigation**: GoogleXcoder was unknown to both Spanish and international law enforcement at the start of the case, requiring intelligence-led identification rather than database-matching.
- **Counter-surveillance**: the suspect lived as a "digital nomad", moving between residences in different Spanish provinces and using phone lines and prepaid cards in fraudulent identities specifically to defeat localisation.
- **Cryptocurrency-flow complexity**: forensic analysis of the seized devices and the suspect's cryptocurrency transactions ran for more than one year before the full criminal scheme could be reconstructed.
- **Operator dispersion**: the CaaS model meant that disrupting the developer did not directly arrest the dozens of phishing-operator crews using the kits; only six additional service users were identified at announcement time and the investigation remains open.

## Lessons Learned

- **Developer-side disruption is decisive for Spanish-language phishing supply.** A single Spanish-speaking CaaS developer based inside Spain was identified as the principal toolkit supplier for an entire wave of Spain-targeted phishing campaigns from 2023; arrest of the developer (rather than only operators) is the lever that materially reduces Spanish-language phishing volume.
- **Bilateral Spain–Brazil police cooperation is a recurring pattern for Lusophone / Hispanophone CaaS developers.** Identifying a Brazilian-national developer operating from Spain required Brazilian Federal Police characterisation alongside Guardia Civil UCO tracking — nationality-based bilateral cooperation remains decisive even when the suspect physically operates inside the requesting state.
- **Public-private cooperation with Group-IB** provided phishing-infrastructure mapping that complemented the Guardia Civil's judicial case, repeating the Group-IB + national-LE pattern previously seen in [[operacion-kaerb-iserver-phishing-as-a-service-takedown-2024|Operation KAERB / iServer]] (Group-IB intelligence powering an Argentine-led, multinational-supported takedown).
- **Telegram-based CaaS distribution remains the dominant channel** for Spanish-language phishing-toolkit supply: paid in cryptocurrency, structured as a subscription-style service with customisation/support/updates. Deactivation of the seller's Telegram channels is now a routine post-arrest measure.

## Follow-Up Actions

- The investigation remains formally open, with further identifications and arrests not ruled out by the Guardia Civil.
- Digital evidence seized during the entries-and-searches continues to be analysed and may produce additional identifications of CaaS users.
- Telegram channels associated with the network have been targeted for deactivation; further platform-side cooperation actions are anticipated.

## Korean Involvement (한국의 참여)

본 작전 발표(2025-10-08, [[spain-guardia-civil|Guardia Civil 1차 출처]])에는 한국 또는 한국 법집행기관의 직접 참여가 명시되어 있지 않다. 본 사건은 스페인을 대상으로 한 스페인어권 피싱 CaaS 공급 차단에 초점이 맞춰져 있어 한국 직접 관련성은 낮다.

다만 다음 두 가지 측면은 한국 사이버수사 실무에 시사점을 가진다:

1. **Telegram 기반 CaaS 공급망의 발달자(developer) 추적 모델**: 운영자(operator) 검거가 아니라 키트를 만드는 개발자에 대한 단일-피의자 추적·정밀 검거 + 자금흐름 1년 분석 모델은, Telegram·VK 기반 한국어 피싱 키트 공급망 수사에도 직접 이전 가능한 패턴.
2. **민간(Group-IB) ↔ 국가 LE 분업 모델**: 인프라 매핑은 민간 CTI 회사가 담당하고, 사법 개입은 국가 LE가 전담하는 분업 구조가 [[operacion-kaerb-iserver-phishing-as-a-service-takedown-2024|Operation KAERB]] 등 다른 다국적 사건에서도 반복적으로 관찰되며, 한국 KISA / KNPA의 민간-공공 협력 설계 시 참고 가치가 있다.

## Contradictions & Open Questions

- **Exact victim and loss figures.** The cited release uses qualitative descriptors ("millions of euros", "thousands of victims", "dozens of entities") without enumerating exact totals — open question for follow-up tier-1 sources.
- **Specific names of impersonated Spanish banks and government bodies.** The cited release describes the impersonated entities only generically as "principal organismos públicos" and "entidades bancarias más importantes de España".
- **Specific date of the arrest and search day(s).** Only the announcement date 2025-10-08 is enumerated; the action day itself is not separately dated in the cited release.
- **Judicial status of the six additional CaaS users.** It is not specified whether the six identified users have been charged, indicted, or remain under investigation; the release states that the investigation remains open.
- **Magnitude of cryptocurrency-transaction reconstruction.** The release describes "more than one year" of forensic analysis but does not enumerate the number of transactions, wallets, or platforms involved.
- **Relationship to private-sector reporting (Group-IB).** Private-sector reporting from Group-IB attributes 250+ phishing sites and nine strains of Android malware to the same actor; this exceeds the scope described in the Guardia Civil release, which focuses on phishing-kit development and does not explicitly enumerate Android-malware strains. The Guardia Civil 2025-10-08 release is treated as the canonical primary source; Group-IB's broader attributions are noted as parallel private-sector technical analysis pending tier-1 LE corroboration.
