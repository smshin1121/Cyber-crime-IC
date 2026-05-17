---
type: operation
title: "16shop Phishing-as-a-Service Platform Takedown (INTERPOL-coordinated, 2023)"
title_ko: "16shop 피싱-as-a-Service 플랫폼 검거 (INTERPOL 조정, 2023)"
aliases:
  - "16Shop takedown 2023"
  - "INTERPOL 16shop PaaS shutdown"
  - "Indonesia-Japan 16shop phishing operator arrests 2023"
case_id: CYB-2023-016S
period: 2
operation_role: standalone
parent_operation: ""
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - seizure
outcome: success
timeframe:
  announced: 2023-08-08
  start: ""
  end: 2023-07
  ongoing: false
crime_type: "[[online-fraud-ic|Phishing-enabled Online Fraud]]"
crime_types:
  - "[[online-fraud-ic|Online Fraud]]"
  - "[[cybercrime-infrastructure-ic|Cybercrime Infrastructure]]"
  - "[[identity-theft|Identity Theft]]"
target_entity: "16shop phishing-as-a-service (PaaS) platform — administrator and two facilitators"
lead_agency: "[[interpol-igci]]"
coordinating_body: "[[interpol-igci]]"
participating_countries:
  - "[[indonesia]]"
  - "[[japan]]"
  - "[[united-states]]"
jurisdictions:
  - "[[indonesia]]"
  - "[[japan]]"
  - "[[united-states]]"
participating_agencies:
  - "[[interpol-igci]]"
  - "[[indonesia-police]]"
  - "[[japan-npa]]"
  - "[[fbi]]"
organizations:
  - "[[interpol-igci]]"
  - "[[indonesia-police]]"
  - "[[japan-npa]]"
  - "[[fbi]]"
mechanisms_used:
  - "[[interpol-i24-7|INTERPOL I-24/7]]"
  - "[[informal-cooperation|Informal Police Cooperation]]"
  - "[[public-private-cooperation|Public-Private Cooperation]]"
legal_basis:
  - "Indonesia: Electronic Information and Transactions Law (UU ITE) — domestic prosecution of administrator and facilitator"
  - "Japan: domestic Penal Code / Unauthorized Computer Access Law — domestic arrest of facilitator in Japan"
  - "INTERPOL framework: Cybercrime Directorate criminal intelligence report dispatched to Indonesian National Police"
results:
  arrests: 3
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Administrator (21-year-old man) arrested in Indonesia; electronic items and several luxury vehicles seized."
    - "One facilitator arrested in Indonesia."
    - "One facilitator arrested in Japan."
    - "16shop PaaS platform shut down."
    - "Compromised users: more than 70,000 across 43 countries."
edges:
  - source_actor: interpol-igci
    target_actor: indonesia-police
    cooperation_type: info_sharing
    legal_basis: informal
    direction: directed
  - source_actor: interpol-igci
    target_actor: japan-npa
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: indonesia-police
    target_actor: japan-npa
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: fbi
    target_actor: interpol-igci
    cooperation_type: info_sharing
    legal_basis: informal
    direction: directed
  - source_actor: fbi
    target_actor: indonesia-police
    cooperation_type: evidence_transfer
    legal_basis: informal
    direction: directed
credibility_index: 4.4
source_tier: 1
missing_fields:
  - "Specific arrest dates for administrator and each facilitator (release gives only 'last month' for one suspect, 8 August 2023 announcement)"
  - "Names / initials of the two facilitators"
  - "US-based hosting company name"
  - "Whether US prosecution will follow Indonesian / Japanese ones"
  - "Specific Indonesian ITE Law articles charged"
  - "Asset disposition for seized luxury vehicles and electronic items"
related_cases: []
related_operations:
  - "[[indonesia-fbi-mfa-bypass-phishing-syndicate-2026]]"
  - "[[w3ll-phishing-kit-takedown-2026]]"
  - "[[labhost-phishing-as-a-service-takedown-2024]]"
  - "[[tycoon-2fa-phishing-as-a-service-takedown-2026]]"
  - "[[gxc-team-googlexcoder-phishing-kits-takedown-2025]]"
challenges_encountered:
  - "Cross-jurisdiction infrastructure (Indonesia operator, US-hosted servers, Japan-based facilitator) requiring three-jurisdiction LE coordination."
  - "Indonesia is not a party to the [[budapest-convention|Budapest Convention on Cybercrime]] as of 2023, so cooperation operated outside Article 35 24/7 Network."
  - "PaaS subscription model dramatically lowers barriers to entry for downstream phishing actors, multiplying victimisation footprint (70,000+ users, 43 countries)."
lessons_learned:
  - "INTERPOL-coordinated intelligence-sharing model can substitute for treaty-based mechanisms in non-Budapest-Convention partners (Indonesia)."
  - "Private-sector partner ecosystem (Cyber Defense Institute, Group-IB, Palo Alto Networks Unit 42, Trend Micro, Cybertoolbelt) materially shaped attribution, demonstrating the operational value of the public-private cooperation model in PaaS takedowns."
  - "ASEAN-region cyber-threat intelligence project (with Japan NPA support) identified the platform — illustrating the regional-monitoring-to-takedown pipeline at INTERPOL IGCI."
source_count: 2
sources:
  - "[[2023-08-08_interpol_16shop-phishing-as-a-service-takedown-indonesia-japan]]"
  - "[[2023-08-08_antara_16shop-bareskrim-japanese-embassy-police-credit-card-hacking]]"
summary: "On 8 August 2023, INTERPOL announced the shutdown of the '16shop' phishing-as-a-service (PaaS) platform in a global investigation it coordinated, resulting in three arrests: the 21-year-old administrator and one facilitator in Indonesia (executed by the Indonesian National Police's Directorate of Cyber Crimes / Bareskrim) and a second facilitator in Japan (by Japan's National Police Agency). The platform sold phishing kits that compromised over 70,000 users across 43 countries; its servers were hosted in the United States, prompting INTERPOL liaison with the FBI through the INTERPOL NCB Washington. The case is a tier-1 INTERPOL-coordinated cybercrime takedown that explicitly names four cooperating LE entities (INTERPOL Cybercrime Directorate, POLRI Directorate of Cyber Crimes, Japan NPA, FBI / INTERPOL NCB Washington), satisfying the wiki's L24 ≥2-LE threshold. Indonesian state news wire Antara (ANTARA Foto, 8 August 2023) independently documents the Jakarta-side announcement at Bareskrim HQ, naming Brigjen Pol Adi Vivid Agustiadi Bachtiar (Dirtipidsiber Bareskrim Polri), Brigjen Pol Ahmad Ramadhan (Karo Penmas Humas Polri), and Mr. Miyagawa (Japanese Embassy police attaché) on stage, with the operative cooperation statement that 'Ditipidsiber Bareskrim Polri together with the Japanese Police party managed to secure two suspects of WNI'."
created: 2026-05-10
updated: 2026-05-17
---
# 16shop Phishing-as-a-Service Platform Takedown (INTERPOL-coordinated, 2023)

> [!info] Provisional / two-source record
> This page rests on two tier-1 primary sources — the [[2023-08-08_interpol_16shop-phishing-as-a-service-takedown-indonesia-japan|INTERPOL official news release of 8 August 2023]] (Singapore dateline) and the [[2023-08-08_antara_16shop-bareskrim-japanese-embassy-police-credit-card-hacking|ANTARA Foto Indonesian state-news-wire caption of 8 August 2023]] (Jakarta dateline) — and remains filed as a provisional INTERPOL-coordinated takedown record under the wiki's preferred 5-source threshold. It will be promoted further when (a) Indonesian-language Polri or full ANTARA newswire articles surface with charging details, (b) any Japan NPA Japanese-language release or US FBI corroborating release is ingested, or (c) Indonesian charging documents are released.

## Summary

On **8 August 2023**, **INTERPOL** announced the shutdown of the **'16shop'** phishing-as-a-service (PaaS) platform in a global investigation that it coordinated. Three arrests were made:

- The **21-year-old administrator** and **one facilitator** were arrested in **Indonesia** by the [[indonesia-police|Indonesian National Police]]'s Directorate of Cyber Crimes (Bareskrim).
- A **second facilitator** was arrested in **Japan** by [[japan-npa|Japan's National Police Agency]] (NPA).
- Electronic items and several luxury vehicles were seized from the administrator.

The 16shop PaaS sold phishing kits that compromised **more than 70,000 users across 43 countries**. Servers were hosted in the **United States**, prompting INTERPOL to liaise with the [[fbi|U.S. Federal Bureau of Investigation]] through the **INTERPOL National Central Bureau in Washington** to secure investigative information for Indonesian investigators.

The operation is recorded as a **tier-1 INTERPOL-coordinated cybercrime takedown** with four explicitly named cooperating LE entities, satisfying the wiki's L24 strict ≥2-LE requirement.

## Background

Phishing-as-a-service (PaaS) is a cybercrime business model in which skilled developers package phishing infrastructure (kits, hosting, evasion tooling, payload templates) for paid sale or subscription to a wider population of less-skilled fraudsters. The model lowers the barrier to entry for downstream phishing campaigns, multiplying their volume and victimisation footprint.

Per the INTERPOL release, **16shop** sold "phishing kits" used to defraud Internet users via email scams: victims received an email with a PDF or link redirecting to a credential-harvesting page, where credit-card and personally identifying information was stolen and used to extract money.

The release frames phishing as "the most prevalent cyber threat in the world," noting that "up to 90 per cent of data breaches are linked to successful phishing attacks." This characterisation contextualises the strategic importance of the takedown beyond the 70,000 directly compromised users.

The 16shop platform was initially flagged by INTERPOL Cybercrime Directorate analysts during an ongoing project researching cyber threats in the **ASEAN region**, supported by **Japan's National Police Agency** — illustrating the regional-monitoring-to-takedown pipeline at the INTERPOL Global Complex for Innovation (IGCI) in Singapore.

## Participating Parties

| Role | Party |
|---|---|
| **Coordinating body** | [[interpol-igci\|INTERPOL Global Complex for Innovation (IGCI)]] / INTERPOL General Secretariat Cybercrime Directorate (Singapore) |
| **Senior INTERPOL voice** | Bernardo Pillot, INTERPOL Assistant Director of Cybercrime Operations |
| **Lead arresting agency (Indonesia)** | [[indonesia-police\|Indonesian National Police]] — Directorate of Cyber Crimes (Bareskrim) |
| **Senior INP voice** | Brigadier General Adi Vivid Agustiadi Bachtiar, Director of the INP's Cyber Crime Investigation |
| **Lead arresting agency (Japan)** | [[japan-npa\|Japan's National Police Agency (NPA)]] |
| **US LE liaison** | [[fbi\|U.S. Federal Bureau of Investigation]] via the INTERPOL National Central Bureau in Washington |
| **Private-sector partners** | Cyber Defense Institute, Group-IB, Palo Alto Networks Unit 42, Trend Micro, Cybertoolbelt |

The release frames the operation as INTERPOL-coordinated but emphasises that arrests were executed by the national services — INP for both Indonesian arrests, Japan NPA for the Japanese arrest. The FBI's role is described as enabling — securing key information about US-hosted servers — rather than executing arrests.

## Legal Framework

**Indonesia (administrator and one facilitator):**

- **Electronic Information and Transactions Law** (*Undang-Undang Informasi dan Transaksi Elektronik*, "UU ITE") — Indonesia's primary cybercrime statute. The release does not specify the article(s) charged.

**Japan (second facilitator):**

- Japanese arrest under **domestic Penal Code** and/or **Unauthorized Computer Access Law** is the most likely vehicle, but the INTERPOL release does not specify the Japanese charging instrument.

**Treaty / cooperation framework:**

- **Indonesia is not a party to the [[budapest-convention|Budapest Convention on Cybercrime]]** as of 2023 (no signature, no accession). The Article 35 24/7 Network is therefore not the channel of record.
- **Japan is a party to the Budapest Convention** (signed 2001-11-23, ratified 2012-07-03), but the release does not invoke the Convention.
- The cooperation framework as described in the INTERPOL release is **INTERPOL-channel intelligence-sharing**, supplemented by direct bilateral exchanges between Japan NPA and the Indonesian National Police, and FBI liaison via the INTERPOL NCB Washington.

> [!warning] Legal status check needed
> The exact charging instrument(s) in Indonesia and Japan are not specified in the INTERPOL release. Indonesian-language POLRI / Antara coverage and any Japanese-language Japan NPA or prosecutor release should be ingested to identify the specific provisions invoked.

## Operational Timeline

| Date | Event |
|---|---|
| (date unknown) | INTERPOL Cybercrime Directorate analysts flag 16shop during an ASEAN-region cyber-threat research project supported by Japan NPA. |
| (date unknown) | Private-sector partners (CDI, Group-IB, Unit 42, Trend Micro, Cybertoolbelt) provide attribution intelligence; INTERPOL determines administrator's identity and probable Indonesian location. |
| (date unknown) | INTERPOL liaises with INTERPOL NCB Washington and FBI re: US-hosted servers. |
| (date unknown) | INTERPOL Cybercrime Directorate dispatches a criminal intelligence report to the INP Directorate of Cyber Crimes. |
| (date unknown) | INP arrests the 21-year-old administrator in Indonesia; seizes electronic items and luxury vehicles. |
| (date unknown) | Information shared between Japan NPA and INP leads to the identification and arrest of two further facilitators (one in Indonesia, one in Japan). |
| ~July 2023 | "Actions against a suspect last month" — referenced in the release as concluding the three-arrest sequence. |
| **2023-08-08** | INTERPOL publicly announces the operation from Singapore. |

The release describes the sequence — administrator first, then facilitators after Japan-Indonesia information exchange — but does not give precise dates for individual arrests.

Indonesian state news wire ANTARA (via [[2023-08-08_antara_16shop-bareskrim-japanese-embassy-police-credit-card-hacking|ANTARA Foto, 8 August 2023]], 14:55 WIB, Jakarta) independently documents the Indonesian-side public announcement at **Bareskrim Mabes Polri HQ in Jakarta** on the same day. The Antara caption identifies three officials on stage:

- **Brigadier General Pol. Adi Vivid Agustiadi Bachtiar** — Director of the Directorate of Cyber Crimes (*Dirtipidsiber*) at Bareskrim Polri (the same Polri officer quoted on the record by INTERPOL).
- **Brigadier General Pol. Ahmad Ramadhan** — Head of the Public Information Bureau (*Karo Penmas*), Public Relations Division (*Humas*) of Polri.
- **Mr. Miyagawa** — Police attaché of the Japanese Embassy for Indonesia.

The Antara caption explicitly states (verbatim): "**Ditipidsiber Bareskrim Polri together with the Japanese Police party managed to secure two suspects of WNI along with proof tools including smart phones, laptops and hardisks** in the case of a credit card hack that results in a total loss of Rp1.6 billion."

This is the L24 verbatim acknowledgment of Indonesia-Japan LE cooperation at the level of the Indonesian state news wire, complementing the INTERPOL release's same-day Singapore-side narrative.

## Results and Impact

| Metric | Value | Source |
|---|---|---|
| Arrests | 3 | INTERPOL release |
| Compromised users | >70,000 | INTERPOL release |
| Affected countries | 43 | INTERPOL release |
| Servers seized (count) | not stated | (n/a) |
| Domains seized (count) | not stated | (n/a) |
| Electronic items seized | "electronic items" (count not given) | INTERPOL release |
| Vehicles seized | "several luxury vehicles" | INTERPOL release |
| Cryptocurrency seized | not stated | (n/a) |

The release frames the platform as "shut down" but does not enumerate seized servers or domains. The 16shop URL had been a known phishing infrastructure host in industry threat reporting prior to August 2023; subsequent industry reporting from the named private-sector partners (Group-IB, Trend Micro, Palo Alto Unit 42) is the natural cross-check on the infrastructure-disposition state and is filed here as an open question pending ingestion.

## Cooperation Mechanisms Used

The cooperation pattern in this case is best characterised as **INTERPOL-coordinated multi-jurisdiction informal cooperation**, with three observable layers:

1. **Hub-and-spoke intelligence-sharing through INTERPOL HQ.** The INTERPOL Cybercrime Directorate at IGCI Singapore acted as the central analytic and coordinating point, compiling a criminal intelligence report dispatched to POLRI's Directorate of Cyber Crimes.
2. **Bilateral Japan NPA ↔ INP information exchange.** After the administrator arrest, "further information was shared between the National Police Agency of Japan and the Indonesian National Police resulting in the identification and arrest of two facilitators."
3. **INTERPOL NCB Washington / FBI liaison for US-hosted infrastructure.** Because servers were hosted in the United States, INTERPOL analysts liaised with the INTERPOL NCB Washington and the FBI to secure key information for Indonesian investigators.
4. **In-country diplomatic-LE channel via the Japanese Embassy in Jakarta.** ANTARA Foto documents that the Japanese Embassy's police attaché (Miyagawa) was physically present alongside Bareskrim leadership at the 8 August 2023 Jakarta press conference at Bareskrim HQ — confirming that Japan-Indonesia cooperation operated through both the bilateral NPA-INP channel cited by INTERPOL and the in-country diplomatic-LE channel routed through the Japanese Embassy in Jakarta.

The release also explicitly describes the role of **private-sector partners** (Cyber Defense Institute, Group-IB, Palo Alto Networks Unit 42, Trend Micro, with added support from Cybertoolbelt), placing this case as an example of [[public-private-cooperation|public-private cooperation]] in cybercrime takedowns.

The operation does **not** invoke a [[joint-investigation-team|Joint Investigation Team]] in the European sense, the Budapest Convention's [[24-7-network|Article 35 24/7 Network]], or any specific MLAT.

## Challenges and Friction Points

1. **Three-jurisdiction infrastructure footprint.** Operator in Indonesia, servers in United States, second facilitator in Japan — requiring at least three national LE services plus INTERPOL HQ coordination. Each jurisdiction's procedural framework (Indonesian ITE Law, Japanese Penal Code / Unauthorized Computer Access Law, US federal cybercrime statutes) had to be navigated separately.
2. **Indonesia non-membership of the Budapest Convention.** As of 2023, Indonesia was (and remains as of 2026-05) not a party to the Budapest Convention, so the Article 35 24/7 Network was not available; cooperation operated through INTERPOL channels and informal bilateral exchanges.
3. **PaaS subscription model.** The platform's "any person ... with a few clicks" characterisation by the senior INP voice underscores that downstream operators (the actual phishing fraudsters) were dispersed globally and not directly targeted by this operation, leaving residual demand for similar tooling.

## Lessons Learned

- **INTERPOL hub-and-spoke model can substitute for treaty channels.** A non-Budapest-Convention member (Indonesia) can be a productive partner in a cybercrime takedown when INTERPOL Cybercrime Directorate compiles and dispatches actionable criminal intelligence reports to the national service.
- **Public-private cooperation materially shaped attribution.** The release's enumeration of five named private-sector partners (CDI, Group-IB, Unit 42, Trend Micro, Cybertoolbelt) is unusual in volume and explicitness; this places 16shop alongside operations such as [[w3ll-phishing-kit-takedown-2026|W3LL]] and [[gxc-team-googlexcoder-phishing-kits-takedown-2025|GXC Team]] as cases where industry threat-intelligence vendors are visible structural participants.
- **Regional cyber-threat monitoring projects produce takedowns.** The 16shop platform was initially flagged during an ASEAN-region INTERPOL project supported by Japan NPA. This is a structural argument for sustained regional-monitoring funding as a precondition for opportunistic takedown action.

## Follow-Up Actions

- Ingest Indonesian-language POLRI / Antara coverage to identify the specific ITE Law articles charged and the names / initials of the two facilitators.
- Watch for any Japan NPA Japanese-language release or court filing concerning the Japan-arrested facilitator.
- Watch for any FBI press release or US criminal complaint relating to the US-hosted server operator or any downstream 16shop-using phishing actor.
- Re-evaluate this page for promotion to non-provisional status when ≥4 additional independent tier-1 sources are available.

## Korean Involvement (한국의 참여)

No Korean involvement is reported in the INTERPOL source. The [[knpa-cyber-bureau|Korean National Police Agency]] is not named as a cooperating service, and no Korean victim or facilitator is identified.

The case is, however, of regional relevance because it concerns a **Southeast-Asian-hosted PaaS operator targeting global victims**, a structural profile similar to the [[indonesia-fbi-mfa-bypass-phishing-syndicate-2026|2026 INP–FBI MFA-bypass PhaaS takedown]] (also Indonesia-administered, also INP-led) and to the broader Cambodia/Philippines voice-phishing dynamics that drive Korean-led operations such as [[korea-cambodia-philippines-73-extradition-2026]] and [[seoul-eastern-clark-philippines-voice-phishing-arrest-extradition-2026]]. Korean financial institutions and email systems are plausible secondary victims of a global PaaS toolkit even when not named in the announcing release.

## Contradictions & Open Questions

- **Arrest dates.** The release gives only "actions against a suspect last month" (~July 2023) for the most recent arrest in the three-arrest sequence; precise dates for the administrator and each facilitator are not provided.
- **Facilitator identities.** Names / initials of the two facilitators (one in Indonesia, one in Japan) are not given.
- **US-hosting company name.** The "company based in the United States" hosting 16shop's servers is not named; no US criminal action against the hosting provider or its operator is described.
- **Server / domain seizure state.** The release frames the platform as "shut down" but does not report seized servers or domains by count. Industry reporting from the named private-sector partners is the natural cross-check.
- **Asset disposition.** Disposition of the seized luxury vehicles and electronic items is not reported.
- **Downstream-operator pursuit.** The release does not describe whether 16shop subscribers (the downstream phishing actors using the kits) are being pursued separately by any LE partner.

> [!note] Translation note
> The INTERPOL English release uses "Indonesian National Police"; Indonesian-language sources will use "Polri" (Polisi Republik Indonesia) or "INP". "Bareskrim" is the standard short form for *Badan Reserse Kriminal* (Criminal Investigation Agency); the release names the **Directorate of Cyber Crimes** within Bareskrim as the arresting unit. For Japan, the agency is named in the release as "the National Police Agency of Japan" / "Japan's National Police Agency" — both refer to 警察庁 (Keisatsu-chō), the Japanese federal-level NPA.
