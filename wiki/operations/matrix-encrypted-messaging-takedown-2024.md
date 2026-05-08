---
type: operation
title: "MATRIX Encrypted Messaging Service Takedown (NL-FR JIT + Europol OTF, 2024-12-03)"
title_ko: "MATRIX 암호화 메시징 서비스 단속 (네덜란드-프랑스 JIT + Europol OTF, 2024-12-03)"
aliases:
  - "MATRIX takedown"
  - "Mactrix Totalsec X-quantum Q-safe takedown"
  - "Encrypted messaging service for criminals takedown 2024"
case_id: CYB-2024-203
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - infrastructure-seizure
outcome: success
timeframe:
  announced: 2024-12-03
  start: 2021
  end: 2024-12-03
  ongoing: false
crime_type: "[[cybercrime-infrastructure-ic]]"
crime_types:
  - "[[cybercrime-infrastructure-ic]]"
  - "[[organized-crime-ic]]"
target_entity: "MATRIX (a.k.a. Mactrix / Totalsec / X-quantum / Q-safe) — invitation-only encrypted messaging service made by criminals for criminals; 40+ servers across several countries with main servers in France and Germany; technically more complex than predecessor platforms Sky ECC and EncroChat. Underlying user-base messaging linked to international drug trafficking, arms trafficking, and money laundering"
lead_agency: "[[dutch-police]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[netherlands]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[italy]]"
  - "[[lithuania]]"
  - "[[spain]]"
participating_agencies:
  - "[[dutch-police]]"
  - "[[france-national-police]]"
  - "[[germany-bka]]"
  - "[[lithuania-police]]"
  - "[[spain-national-police]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
organizations:
  - "[[dutch-police]]"
  - "[[france-national-police]]"
  - "[[germany-bka]]"
  - "[[lithuania-police]]"
  - "[[spain-national-police]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
mechanisms_used:
  - "[[europol-jit]]"
  - "[[european-arrest-warrant]]"
  - "[[search-seizure]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Joint Investigation Team (JIT) between Netherlands and France set up at Eurojust"
  - "Operational Task Force (OTF) established at Europol in June 2024 between Netherlands, France, Lithuania, Italy, and Spain"
  - "European Arrest Warrant (EAW) from Netherlands executed in Spain (2 arrests)"
  - "Per-country domestic search warrants executed under each lead authority's procedural code"
results:
  arrests: 3
  indictments: 0
  servers_seized: 40
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "3 arrests on action day (1 in France; 2 in Spain under European Arrest Warrant from the Netherlands)"
    - "13 house searches (1 in France; 6 in Spain; 6 in Lithuania)"
    - "Main MATRIX servers in France and Germany taken down; 40+ servers across several countries disrupted"
    - "3-month live interception phase: 2.3 million+ messages in 33 languages intercepted and deciphered"
    - "Splash-page warning deployed on MATRIX post-takedown alerting users that authorities had intercepted the platform"
    - "Predicate offences identified in intercepted messages: international drug trafficking, arms trafficking, money laundering"
edges:
  - source_actor: dutch-police
    target_actor: france-national-police
    cooperation_type: joint_investigation
    legal_basis: europol-jit
    direction: undirected
  - source_actor: dutch-police
    target_actor: spain-national-police
    cooperation_type: arrest_assistance
    legal_basis: european-arrest-warrant
    direction: directed
  - source_actor: europol-ec3
    target_actor: dutch-police
    cooperation_type: coordination
    legal_basis: europol-otf
    direction: undirected
  - source_actor: eurojust
    target_actor: dutch-police
    cooperation_type: judicial_coordination
    legal_basis: europol-jit
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "specific names and aliases of arrestees"
  - "exact server-by-server location breakdown of the 40+ MATRIX servers"
  - "specific Dutch journalist murder case (2021) referenced as the discovery context — case is referenced but not named"
  - "post-2024-12-03 investigative spinoffs derived from the intercepted-message corpus"
related_cases: []
related_operations:
  - "[[operation-kraken-ghost-platform]]"
  - "[[operation-us-v-anom-distributors]]"
challenges_encountered: []
lessons_learned:
  - "First wiki record of MATRIX as a discrete operation/platform name and the 4-country action-day takedown of an invitation-only encrypted-comms platform technically more complex than Sky ECC and EncroChat."
  - "First wiki record of a Europol Operational Task Force (OTF) as a discrete IC coordination mechanism class — distinct from Joint Investigation Teams (JIT), Joint Cybercrime Action Taskforce (J-CAT), and Operational Task Force at Europol HQ models documented elsewhere."
  - "Demonstrates the live-interception + splash-page-takedown pattern as a discrete encrypted-comms enforcement methodology — 3-month live interception phase produced 2.3M+ message corpus, followed by simultaneous server takedown + user-warning splash page."
  - "European Arrest Warrant (NL → ES) for 2 of 3 action-day arrests — efficient cross-border arrest mechanism within Schengen for an inter-state JIT operation."
  - "Establishes the encrypted-comms-platform takedown chronology in primary IC documentation: Sky ECC → EncroChat → Exclu → Ghost → MATRIX. Each successive platform is technically more complex than its predecessor."
source_count: 1
sources:
  - "[[2024-12-03_europol_matrix-encrypted-messaging-service-takedown]]"
summary: "On 2024-12-03, a Netherlands-France JIT at Eurojust + Europol Operational Task Force (June 2024 onwards, NL/FR/LT/IT/ES 5-country) executed the takedown of MATRIX (a.k.a. Mactrix / Totalsec / X-quantum / Q-safe), an invitation-only encrypted messaging service made by criminals for criminals with 40+ servers across several countries (main servers in France and Germany). German technical expertise + Italian Antimafia Directorate support. Action day produced 3 arrests (1 FR, 2 ES via EAW from NL) + 13 house searches (1 FR + 6 ES + 6 LT) + main-server takedowns in France and Germany. 3-month live interception phase captured 2.3 million+ messages in 33 languages, identifying intercepted messages linked to international drug trafficking, arms trafficking, and money laundering. MATRIX was first discovered on the phone of a criminal convicted for the 2021 murder of a Dutch journalist."
created: 2026-05-09
updated: 2026-05-09
---
## Summary

On **2024-12-03**, a Netherlands-France Joint Investigation Team (JIT) at **Eurojust** plus a Europol **Operational Task Force (OTF)** established in June 2024 between Netherlands, France, Lithuania, Italy, and Spain executed the takedown of **MATRIX** (also known as **Mactrix / Totalsec / X-quantum / Q-safe**) — an invitation-only encrypted messaging service "made by criminals for criminals" that was technically more complex than predecessor platforms **Sky ECC** and **EncroChat**. **40+ servers** across several countries supported MATRIX, with main servers in **France** and **Germany**. The action day produced **3 arrests** (1 in France; 2 in Spain via European Arrest Warrant from the Netherlands), **13 house searches** (1 FR + 6 ES + 6 LT), and **takedowns of the main servers in France and Germany**. Prior to the takedown, a **3-month live interception phase** captured **2.3 million+ messages in 33 languages**, with messages linked to **international drug trafficking, arms trafficking, and money laundering**.

## Background

MATRIX was first discovered by **Dutch authorities** on the phone of a criminal convicted for the **2021 murder of a Dutch journalist**. A large-scale investigation followed. The MATRIX founders believed the service was superior and more secure than previous criminal-use applications, with **invitation-only** user access and a technical infrastructure substantially more complex than Sky ECC and EncroChat.

The Dutch and French authorities began cooperating through a **JIT set up at Eurojust**. By using innovative interception technology, the authorities monitored MATRIX activity for **three months** prior to the takedown action. The Europol **Operational Task Force (OTF)** was established at Europol in **June 2024** with the Netherlands, France, Lithuania, Italy, and Spain.

## Participating Parties

| Country | Lead Authorities |
|---|---|
| Netherlands (lead) | Team High Tech Crime of the National Investigations and Special Operations (NIS) of the Netherlands Police; Netherlands Public Prosecution Service (National Office) |
| France (JIT partner) | JUNALCO National Jurisdiction against Organised Crime; OFAC National Police Cybercrime division |
| Germany (technical expertise) | Frankfurt am Main Public Prosecutor General's Office — ZIT; German Federal Criminal Police (BKA) Serious and Organised Crime Division |
| Italy (OTF partner) | National Antimafia Directorate (D.N.A.); Central Directorate for Anti Drug Services (D.C.S.A.) |
| Lithuania (OTF partner) | Prosecutor General's Office; Lithuanian Criminal Police Bureau |
| Spain (OTF partner) | Central Investigative Court 1 and 5 of Audiencia Nacional; Investigative Court 1 of Marbella; Spanish National Police |
| Coordinating | [[europol-ec3\|Europol European Cybercrime Centre (EC3)]] (Operational Task Force from June 2024); [[eurojust\|Eurojust]] (JIT setup) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2021 | Dutch journalist murdered; convicted criminal's phone yields MATRIX as the encrypted messaging service used | Europol 2024-12-03 |
| (date not enumerated) | Dutch large-scale investigation begins; Netherlands-France JIT set up at Eurojust | Europol 2024-12-03 |
| 2024-06 | Europol Operational Task Force (OTF) established with NL/FR/LT/IT/ES (5 countries) | Europol 2024-12-03 |
| (~2024-09 to 2024-12) | 3-month live interception phase: 2.3M+ messages in 33 languages intercepted and deciphered | Europol 2024-12-03 |
| 2024-12-03 | Action day in 4 countries: 3 arrests + 13 house searches + main-server takedowns in France and Germany; splash-page warning deployed on MATRIX | Europol 2024-12-03 |

## Results and Impact

- **3 arrests** on action day: 1 in France + 2 in Spain (under European Arrest Warrant from the Netherlands).
- **13 house searches**: 1 in France + 6 in Spain + 6 in Lithuania.
- **40+ servers** disrupted; main MATRIX servers in **France** and **Germany** taken down.
- **2.3 million+ messages** in **33 languages** intercepted and deciphered during the 3-month live interception phase.
- **Splash-page warning** deployed on MATRIX post-takedown alerting users that authorities had intercepted the platform.
- **Predicate offences** identified in intercepted messages: international drug trafficking, arms trafficking, money laundering.

## Cooperation Mechanisms Used

The cited release describes four discrete IC mechanism classes for this operation:

1. **Netherlands-France Joint Investigation Team (JIT) at Eurojust** — foundational bilateral investigative instrument for the Dutch-French collaboration.
2. **Europol Operational Task Force (OTF)** established June 2024 with 5 countries — **first wiki record of OTF as a discrete IC coordination mechanism class** distinct from JIT and J-CAT.
3. **Live-interception + splash-page-takedown pattern** — 3-month live interception phase produced 2.3M+ message corpus; simultaneous server takedown + user-warning splash page deployed on action day.
4. **European Arrest Warrant (NL → ES)** — 2 of 3 action-day arrests executed in Spain under EAW from the Netherlands.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited Europol release among the participating jurisdictions. The case is recorded in the wiki for the encrypted-comms-platform takedown chronology, the Europol OTF mechanism class, and the live-interception + splash-page-takedown pattern. Korean exposure to MATRIX or its predecessor platforms (Sky ECC, EncroChat, Exclu, Ghost) is not enumerated in this source.

## Contradictions & Open Questions

- The cited release does not enumerate the specific names and aliases of the 3 arrestees.
- The exact server-by-server location breakdown of the 40+ MATRIX servers is not enumerated.
- The specific Dutch journalist murder case (2021) referenced as the MATRIX discovery context is referenced but not named.
- Post-2024-12-03 investigative spinoffs derived from the intercepted-message corpus are described as anticipated ("through legal requests, authorities will now be able to access the messages for their investigations") but not enumerated in the cited release.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2024-12-03_europol_matrix-encrypted-messaging-service-takedown\|International operation takes down another encrypted messaging service used by criminals (MATRIX)]] | Europol | 2024-12-03 | https://www.europol.europa.eu/media-press/newsroom/news/international-operation-takes-down-another-encrypted-messaging-service-used-criminals |
