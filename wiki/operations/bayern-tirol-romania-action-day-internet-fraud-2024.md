---
type: operation
title: "Bayern-Tirol-Romania Action Day: International Internet-Fraud OCG Takedown (ZCB Bayern + Eurojust JIT, 2024-12-17)"
title_ko: "바이에른-티롤-루마니아 합동작전: 국제 인터넷사기 조직 단속 (바이에른 사이버수사센터 + Eurojust JIT, 2024-12-17)"
aliases:
  - "Action Day in Rumänien, Österreich und Bayern 2024"
  - "ZCB Bayern Mittelfranken DIICOT Tirol LKA action day 2024-12-17"
  - "Bavarian cybercrime centre internet-fraud takedown 2024 (Bayern-Tirol-Bukarest-Râmnicu Vâlcea)"
case_id: CYB-2025-152
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - asset-freeze
outcome: success
timeframe:
  announced: 2025-01-15
  start: 2023-08
  end: 2024-12-17
  ongoing: false
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[organized-crime-ic]]"
  - "[[money-laundering-ic]]"
target_entity: "International internet-fraud organised-crime group of 7 identified suspects (ages 22-38), operating from Tirol (Austria), Bukarest and Râmnicu Vâlcea (Romania), and the Regensburg area (Bayern, Germany). The OCG compromised at least 120 merchant accounts on online marketplaces and platforms, induced customers to place orders worth approximately EUR 110 million, redirected payments to network-controlled accounts, and laundered proceeds through multi-jurisdictional bank-account and money-mule layers. The group additionally engaged in real-estate fraud against at least 7 victims (EUR 17,000). 381 victims with confirmed losses of approximately EUR 192,000 for undelivered goods were identified by the joint investigation."
lead_agency: ""
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[germany]]"
  - "[[austria]]"
  - "[[romania]]"
participating_agencies:
  - "[[romania-diicot]]"
  - "[[eurojust]]"
organizations:
  - "[[romania-diicot]]"
  - "[[eurojust]]"
mechanisms_used:
  - "[[joint-investigation-team]]"
legal_basis:
  - "Joint Investigation Team (JIT) between the Zentralstelle Cybercrime Bayern of the Generalstaatsanwaltschaft Bamberg (Germany) and the Romanian prosecutorial authorities, under Eurojust participation."
  - "Domestic arrest and search warrants issued by the Amtsgericht Bamberg (Germany) executed in coordination with Austrian and Romanian counterpart authorities under their respective domestic warrant authority."
  - "Cross-border prosecution coordination among Bavarian, Austrian (Landeskriminalamt Tirol), and Romanian (DIICOT) investigators."
results:
  arrests: 5
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 381
  other:
    - "13 search locations executed simultaneously in Tirol (Austria), Bukarest and Râmnicu Vâlcea (Romania), and the Regensburg area (Bayern, Germany) on the 2024-12-17 action day."
    - "Approximately 150 police officers deployed across the three countries on the action day."
    - "5 of 7 identified male suspects (ages 22-38) arrested under cross-jurisdictional warrants."
    - "At least 120 compromised merchant accounts on online marketplaces and platforms identified."
    - "Orders worth approximately EUR 110 million induced from victims through the compromised merchant accounts."
    - "381 identified victims with confirmed losses of approximately EUR 192,000 for undelivered goods."
    - "At least 7 real-estate-fraud victims with losses of approximately EUR 17,000."
    - "Approximately EUR 70,000 cash seized on the action day."
    - "2 prosecutors and 2 IT-forensics specialists from the Zentralstelle Cybercrime Bayern assigned to the case."
edges:
  - source_actor: zcb-bayern
    target_actor: romania-diicot
    cooperation_type: joint_investigation
    legal_basis: JIT
    direction: undirected
  - source_actor: zcb-bayern
    target_actor: lka-tirol
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: eurojust
    target_actor: zcb-bayern
    cooperation_type: technical_assistance
    legal_basis: JIT
    direction: directed
  - source_actor: eurojust
    target_actor: romania-diicot
    cooperation_type: technical_assistance
    legal_basis: JIT
    direction: directed
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "Specific identities and nationalities of the 7 identified suspects (5 arrested)."
  - "Per-country breakdown of the 13 search locations (Tirol vs. Romania vs. Bayern split)."
  - "Specific online marketplaces / platforms whose merchant accounts were compromised."
  - "Indictment-stage and trial-stage charging detail (release covers only the arrest phase)."
  - "Specific cryptocurrency seized or frozen (not enumerated in the cited release)."
  - "Per-victim-state breakdown of the 381 victims (likely cross-EU but not enumerated)."
related_cases:

related_operations:
  - "[[romania-moldova-phishing-laundering-jit-2025]]"
  - "[[romania-phishing-takedown-2024]]"
  - "[[austria-latvia-estonia-online-scams-jit-takedown-2025]]"
  - "[[eurojust-massive-investment-fraud-hundreds-thousands-victims-2022]]"
challenges_encountered:

lessons_learned:
  - "First wiki record of a Bavarian-state-level (Zentralstelle Cybercrime Bayern of the Generalstaatsanwaltschaft Bamberg) JIT with Romanian prosecutorial authorities and Austrian state-level (LKA Tirol) participation. Establishes the German Land-level (sub-federal, non-BKA) prosecutor-led JIT pattern as a discrete IC mechanism instance distinct from BKA-coordinated federal JITs."
  - "Compromised-merchant-account internet fraud (orders worth EUR 110 million induced, but only EUR 192,000 actually transferred for undelivered goods) is a high-leverage low-yield pattern: the gross order volume is two orders of magnitude larger than the confirmed victim losses because most orders were intercepted or refunded by the platforms before disbursement. Confirms that platform-side anti-fraud controls absorb most of the fraud surface, leaving only the disbursement-completion subset as confirmed victim loss."
  - "Multi-jurisdictional OCG with operators based in three discrete EU jurisdictions (Bayern, Tirol, Romania) — distinct from the [[romania-moldova-phishing-laundering-jit-2025|Romania-Moldova phishing-laundering JIT]] pattern of a single third-country call-centre base. The Bayern-Tirol-Romania pattern is a distributed-cells variant rather than a centralised call-centre variant."
  - "Real-estate-fraud sub-line (EUR 17,000 across 7 victims) embedded within an internet-fraud OCG suggests that internet-fraud operators diversify into adjacent offline fraud types using the same money-mule and account-laundering infrastructure."
source_count: 1
sources:
  - "[[2025-01-15_polizei-bayern_action-day-rumaenien-oesterreich-bayern]]"
summary: "On 2024-12-17, the Zentralstelle Cybercrime Bayern (ZCB) of the Generalstaatsanwaltschaft Bamberg, the Polizeipräsidium Mittelfranken / Kriminalpolizei Nürnberg (Germany), the Landeskriminalamt Tirol (Austria), and the Romanian D.I.I.C.O.T (Directoratul de Investigare a Infracțiunilor de Criminalitate Organizată și Terorism) executed a coordinated tri-country action day across 13 locations in Tirol (Austria), Bukarest and Râmnicu Vâlcea (Romania), and the Regensburg area (Bayern, Germany), arresting 5 of 7 identified male suspects (ages 22-38) belonging to an international internet-fraud organised-crime group. The OCG had compromised at least 120 merchant accounts on online marketplaces and platforms, induced victims to place orders worth approximately EUR 110 million, with 381 identified victims confirming approximately EUR 192,000 in losses for undelivered goods plus at least EUR 17,000 from 7 real-estate-fraud victims; approximately EUR 70,000 in cash was seized on the action day. The action was carried out within a Joint Investigation Team with Romanian prosecutorial authorities under [[eurojust|Eurojust]] participation, with approximately 150 officers deployed across the three countries. The Bavarian Polizei joint press release announcing the arrests was issued on 2025-01-15."
created: 2026-05-16
updated: 2026-05-16
---
## Summary

On **17 December 2024**, the **Zentralstelle Cybercrime Bayern (ZCB)** of the **Generalstaatsanwaltschaft Bamberg**, the **Polizeipräsidium Mittelfranken / Kriminalpolizei Nürnberg** (Germany), the **Landeskriminalamt Tirol** (Austria), and the Romanian **D.I.I.C.O.T** (Directoratul de Investigare a Infracțiunilor de Criminalitate Organizată și Terorism) executed a coordinated **tri-country action day** across **13 locations** in **Tirol (Austria), Bukarest and Râmnicu Vâlcea (Romania), and the Regensburg area (Bayern, Germany)**. The action arrested **5 of 7 identified male suspects** (ages 22-38) of an international internet-fraud organised-crime group, with approximately **150 police officers** deployed across the three countries. The action was carried out within a **Joint Investigation Team** with Romanian prosecutorial authorities **under [[eurojust|Eurojust]] participation**. The Bavarian Polizei joint press release announcing the arrests was issued on **15 January 2025**.

## Background

Investigations were initiated in **August 2023** by the **Zentralstelle Cybercrime Bayern (ZCB)** of the **Generalstaatsanwaltschaft Bamberg** in conjunction with the **Polizeipräsidium Mittelfranken / Kriminalpolizei Nürnberg**, targeting an internationally operating internet-fraud organised-crime group. The OCG compromised at least **120 merchant accounts** on online marketplaces and platforms, induced customers to place orders worth approximately **EUR 110 million**, and redirected payments to network-controlled accounts. Of those induced orders, **381 identified victims** suffered confirmed losses of approximately **EUR 192,000** for undelivered goods; the gap between induced order volume and confirmed victim loss reflects platform-side anti-fraud interception and refund of most orders before disbursement. The group additionally engaged in real-estate fraud against at least **7 victims** with losses of approximately **EUR 17,000**.

## Participating Parties

| Role | Parties |
|---|---|
| German lead investigating prosecutor's office | Zentralstelle Cybercrime Bayern (ZCB) of the Generalstaatsanwaltschaft Bamberg |
| German lead investigating police body | Polizeipräsidium Mittelfranken / Kriminalpolizei Nürnberg |
| Austrian state-level partner | Landeskriminalamt Tirol |
| Romanian partner | [[romania-diicot|D.I.I.C.O.T — Directoratul de Investigare a Infracțiunilor de Criminalitate Organizată și Terorism]] |
| Coordinating EU body | [[eurojust|European Union Agency for Criminal Justice Cooperation (Eurojust)]] |
| Issuing court (Germany) | Amtsgericht Bamberg |
| Participating countries | [[germany|Germany]], [[austria|Austria]], [[romania|Romania]] |

> [!note] No wiki entity yet
> The Zentralstelle Cybercrime Bayern (ZCB) of the Generalstaatsanwaltschaft Bamberg, the Polizeipräsidium Mittelfranken, and the Landeskriminalamt Tirol do not yet have dedicated wiki organization pages. Per L23, `lead_agency` is left empty in the frontmatter and the agency names are preserved in prose; `coordinating_body` is set to the wiki-existing [[eurojust|Eurojust]] page. When stub pages are created for the Bavarian state-level cybercrime prosecutor and the Tyrolean state criminal police office, this operation page should be relinked.

## Legal Framework

The tri-country action day rests on three discrete legal instruments:

1. **Joint Investigation Team (JIT)** — with Romanian prosecutorial authorities, under [[eurojust|Eurojust]] participation. The JIT is the primary structural cooperation vehicle of the operation.
2. **Domestic arrest and search warrants** — issued by the Amtsgericht Bamberg (Germany) and executed in coordination with Austrian and Romanian counterpart authorities under their respective domestic warrant authority.
3. **Cross-border prosecution coordination** — among Bavarian (ZCB Bayern + Polizeipräsidium Mittelfranken), Austrian (Landeskriminalamt Tirol), and Romanian (DIICOT) investigators, with simultaneous execution of warrants in all three jurisdictions.

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2023-08 | ZCB Bayern initiates joint investigation with Polizeipräsidium Mittelfranken | Polizei Bayern 2025-01-15 |
| 2024-12-17 | Tri-country action day: 13 search locations in Tirol + Bukarest + Râmnicu Vâlcea + Regensburg area; 5 of 7 suspects arrested | Polizei Bayern 2025-01-15 |
| 2025-01-15 | Joint press release issued by Polizei Bayern and ZCB | Polizei Bayern 2025-01-15 |

## Results and Impact

- **5 male suspects arrested** of 7 identified (ages 22-38).
- **13 locations searched** simultaneously across the three countries on the action day.
- **Approximately 150 police officers** deployed across Tirol, Romania, and Bayern.
- **At least 120 compromised merchant accounts** identified on online marketplaces and platforms.
- **Orders worth approximately EUR 110 million** induced from victims through the compromised merchant accounts.
- **381 identified victims** with confirmed losses of approximately **EUR 192,000** for undelivered goods.
- **At least 7 real-estate-fraud victims** with losses of approximately **EUR 17,000**.
- **Approximately EUR 70,000 cash seized** on the action day.
- **2 prosecutors and 2 IT-forensics specialists** from ZCB Bayern assigned to the case.

## Cooperation Mechanisms Used

The cited release describes three discrete IC mechanism classes operating in parallel:

1. **Eurojust-participated JIT** — the primary structural cooperation vehicle between ZCB Bayern (Germany) and the Romanian prosecutorial authorities, with Eurojust participation. This is a state-level (Land-level, not federal BKA) Germany–Romania prosecutorial JIT.
2. **Tri-country coordinated simultaneous warrant execution** — Bavarian, Austrian (LKA Tirol), and Romanian (DIICOT) investigators simultaneously executed search and arrest warrants in their respective jurisdictions on the action day, under coordination by the German lead prosecutor's office.
3. **Cross-border prosecution coordination** — the press release explicitly frames the action as "länderübergreifenden Strafverfolgung bayerischer, österreichischer und rumänischer Ermittler" (cross-border prosecution by Bavarian, Austrian, and Romanian investigators), with Eurojust as the EU-level coordinating body.

## Challenges and Friction Points

- **Multi-jurisdictional OCG**: Operators were distributed across three discrete EU jurisdictions (Bayern, Tirol, Romania) rather than concentrated in a single third-country call-centre base. This distributed-cells pattern requires multiple simultaneous domestic warrant executions rather than a single foreign-LE-led raid.
- **Platform-side anti-fraud interception**: Of approximately EUR 110 million in induced order volume, only approximately EUR 192,000 in confirmed victim losses materialised (a ~0.17% loss-realisation rate). The order-volume figure overstates actual fraud yield by two orders of magnitude; only the disbursement-completion subset translated to confirmed victim loss.
- **Cross-EU victim distribution**: Victims were distributed across the European Union (381 identified), raising the question (not addressed in the release) of whether additional Member States are running parallel domestic prosecutions or contributing evidence under the same JIT.

## Lessons Learned

- First wiki record of a **Bavarian state-level (ZCB Bayern, Land-level prosecutor) JIT** with Romanian prosecutorial authorities and Austrian state-level (LKA Tirol) participation. Establishes the German Land-level (sub-federal, non-BKA) prosecutor-led JIT pattern as a discrete IC mechanism instance distinct from BKA-coordinated federal JITs.
- **Compromised-merchant-account internet fraud** induces gross order volumes (here EUR 110 million) two orders of magnitude larger than confirmed victim losses (EUR 192,000). Platform-side anti-fraud controls absorb most of the fraud surface; only the disbursement-completion subset materialises as confirmed victim loss.
- **Distributed-cells OCG pattern** (operators in Bayern + Tirol + Romania) is distinct from the centralised-call-centre OCG pattern recorded in [[romania-moldova-phishing-laundering-jit-2025|the Romania-Moldova phishing-laundering JIT]] and requires multiple simultaneous domestic warrant executions rather than a single foreign-LE-led raid.
- **Adjacent-fraud diversification**: The same OCG ran real-estate fraud (EUR 17,000 / 7 victims) alongside internet fraud, suggesting that money-mule and account-laundering infrastructure built for internet fraud is reused for offline fraud types.

## Follow-Up Actions

The cited release covers only the arrest phase. Indictment- and trial-stage charging detail, identification of the 2 unarrested suspects of the 7 identified, and per-country breakdown of the 13 search locations are not enumerated in the cited release. Follow-on tier-1 sources from the Generalstaatsanwaltschaft Bamberg, the DIICOT, or the Landeskriminalamt Tirol should be sought to enrich the post-arrest prosecution record.

## Korean Involvement (한국의 참여)

South Korea is **not named** in the cited Bavarian Polizei release among the participating jurisdictions, the OCG's suspect nationalities, the search-location countries, or the victim cohort. The case is recorded in the wiki for the German Land-level (ZCB Bayern) prosecutorial JIT pattern, the tri-country distributed-cells OCG variant, and the platform-side anti-fraud interception lesson. Korean exposure to similar compromised-merchant-account internet fraud schemes operating from European jurisdictions is *not specifically attested* in this release; comparable Korean-exposure cases are tracked separately in the [[knpa-cambodia-bavet-romance-scam-vietnam-arrests-2025|KNPA-side cyber-fraud corpus]].

## Contradictions & Open Questions

- Per-country breakdown of the 13 search locations (Tirol vs. Romania vs. Bayern split) is not enumerated in the cited release.
- Specific online marketplaces / platforms whose merchant accounts were compromised are not identified by name.
- Identities and nationalities of the 7 suspects (5 arrested, 2 unarrested) are not enumerated.
- Specific cryptocurrency seized or frozen on the action day is not enumerated (only the EUR 70,000 cash seizure is reported).
- Indictment-stage charging detail is not in scope of the arrest-phase press release.
