---
type: operation
title: "Bavaria–Kosovo–Costa Rica–Israel International Investment-Fraud Network Extradition and Indictment (ZCB Bamberg, 2026)"
title_ko: "바이에른–코소보–코스타리카–이스라엘 국제 투자사기 네트워크 인도·기소 (밤베르크 ZCB, 2026)"
aliases:
  - "ZCB Bamberg international fraud network indictment"
  - "Bavaria call-centre fraud Costa Rica extradition 2025"
  - "Generalstaatsanwaltschaft Bamberg PM 3/2026"
case_id: CYB-2026-225
period: 3
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
  - extradition
  - indictment
  - search-seizure
outcome: success
timeframe:
  announced: 2026-01-23
  start: 2021-03
  end: 2026-01-23
  ongoing: false
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
target_entity: "International online-investment-fraud and cryptocurrency-scam call-centre network, allegedly led by a 42-year-old Israeli-Portuguese dual national, operating call centres in Kosovo (Pristina) targeting victims in Germany and worldwide; total estimated worldwide loss at least €21 million, including at least €4.5 million from German victims."
lead_agency: ""
coordinating_body: ""
participating_countries:
  - "[[germany]]"
  - "[[kosovo]]"
  - "[[costa-rica]]"
  - "[[israel]]"
participating_agencies: []
legal_basis:
  - "[[extradition]]"
  - "[[mlat-process]]"
mechanisms_used:
  - "[[extradition]]"
  - "[[mlat-process]]"
results:
  arrests: 1
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Joint Action Day in Pristina (March 2021) with Kosovo investigators dismantled call-centre infrastructure"
    - "Defendant extradited from Costa Rica to Germany in July 2025 after multi-year proceedings"
    - "Indictment filed October 2025 at the Cyber-Wirtschaftsstrafkammer of the Bamberg Regional Court"
    - "Damages: at least €4.5 million in Germany; estimated at least €21 million worldwide"
edges:
  - source_actor: "Generalstaatsanwaltschaft Bamberg — Zentralstelle Cybercrime Bayern (ZCB)"
    target_actor: "Kosovo investigative authorities (Pristina)"
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: undirected
  - source_actor: "Generalstaatsanwaltschaft Bamberg — Zentralstelle Cybercrime Bayern (ZCB)"
    target_actor: "Costa Rican judicial authorities"
    cooperation_type: extradition
    legal_basis: bilateral_MOU
    direction: directed
  - source_actor: "Generalstaatsanwaltschaft Bamberg — Zentralstelle Cybercrime Bayern (ZCB)"
    target_actor: "Israeli authorities"
    cooperation_type: evidence_transfer
    legal_basis: MLAT
    direction: directed
credibility_index: 4.2
source_tier: 1
missing_fields:
  - participating_agencies
  - lead_agency
  - coordinating_body
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "[[2026-01-23_justiz-bayern_bamberg-costa-rica-extradition-international-fraud-network]]"
created: 2026-05-16
updated: 2026-05-17
---

## Summary

In press release PM 3/2026 dated 23 January 2026, the [[germany|German]] Generalstaatsanwaltschaft Bamberg's Zentralstelle Cybercrime Bayern (Central Cybercrime Unit Bavaria, "ZCB") announced that it had filed indictment in October 2025 against a 42-year-old Israeli-Portuguese dual national identified as the alleged head of a transnational online-investment-fraud and cryptocurrency-scam call-centre network. The defendant was extradited from [[costa-rica|Costa Rica]] to Germany in July 2025 after a multi-year extradition proceeding; trial is pending at the specialised Cyber-Economic Criminal Chamber (Cyber-Wirtschaftsstrafkammer) of the Bamberg Regional Court (Landgericht Bamberg).

Likely the case represents one of Bavaria's largest cyber-enabled investment-fraud prosecutions, with at least €4.5 million in losses to German victims and an estimated minimum €21 million worldwide. The investigation involved explicit cooperation with three foreign jurisdictions: [[kosovo|Kosovo]] (operational dismantling of call-centre infrastructure via a joint Action Day in Pristina, March 2021), Costa Rica (executed the extradition), and [[israel|Israel]] (assistance regarding the suspect's Israeli nationality and identification).

## Background

### Modus operandi
The network ran a classic **cold-call online-investment-fraud** / **cryptocurrency-scam** call-centre operation of the kind that has dominated European LE cybercrime caseloads since 2019. Trained call-centre agents working from premises in **Pristina, Kosovo** contacted German and worldwide victims (variously by cold-call, online advertising lead-generation, or trading-platform sign-up referral) and persuaded them to deposit funds into purported online-investment platforms — typically Forex/CFD trading interfaces or branded cryptocurrency-trading dashboards — that were in fact controlled by the network. Victim deposits were displayed back as paper-gain account balances on a fake trading interface ("turbo-charged returns"), inducing further deposits, while withdrawal requests were stalled, conditioned on additional "tax / verification / margin" payments, and ultimately denied. The 2021 joint Action Day with Kosovar investigators in Pristina established that the entire call-centre infrastructure and trading-platform back-end were physically located in Kosovo, consistent with the broader **Western-Balkans call-centre fraud belt** pattern documented by Europol and Eurojust across 2022–2025 ([[de-cy-bg-se-online-investment-fraud-cyprus-call-centres-2024]], parallel Bulgarian / Albanian operations).

### Victim profile and impact
- **Principal injured jurisdiction**: Germany — **at least €4.5 million** in confirmed losses from German victims. The Bavarian KPI Neu-Ulm investigation was opened on the basis of clustered German victim complaints, indicating organic detection through retail-victim reporting channels rather than through inter-agency intelligence handover.
- **Worldwide damages**: estimated **at least €21 million** across multiple jurisdictions (the release does not enumerate the per-country distribution outside Germany; the worldwide-versus-German ratio of ~4.7× implies a substantial non-German victim base, consistent with a multilingual call-centre operation).
- **Victim demographic**: not specified in the release. The Western-Balkans call-centre-fraud pattern typically targets **middle-aged retail investors** drawn by lead-generation advertising for "high-yield Forex / crypto" platforms; whether this network specifically targeted retirees or a younger demographic is *unknown* from the tier-1 source.
- **Victim notification status**: not disclosed in PM 3/2026. Under German criminal procedure (StPO § 406d ff.), identified victims of the indicted defendant will be afforded *Nebenklage* (joinder) and information rights through the Bamberg Landgericht trial phase.

### Financial flow
- **Inflows**: victim deposits via SEPA bank transfer and (likely) cryptocurrency on-ramp purchases routed into purported "investment platform" accounts. The release does not specify the receiving payment-processor or bank-account chain.
- **Internal routing**: per the gewerbs- und bandenmäßig (commercial-and-organised-gang) charging theory under § 263 Abs. 1, 3 Nr. 1, Abs. 5 StGB, deposits were funnelled through multi-layer corporate vehicles and converted between fiat and cryptocurrency to obscure beneficial ownership before settling with the network's principals.
- **Outflows**: the release does not quantify amounts laundered, recovered, or held in restraint at the time of indictment. Asset-tracing across Kosovo and Israel formed part of the MLA workstream (Israeli-authorities cooperation specifically cited).
- **Cryptocurrency seizure**: not asserted on the operation page (the frontmatter `cryptocurrency_seized` field is empty). The release does not report a final seizure figure, suggesting asset-recovery proceedings remain ongoing in parallel with the criminal trial.

### Criminal organisation structure
- **Principal defendant**: 42-year-old male, dual **Israeli–Portuguese** nationality (name withheld per German press code). Identified by the ZCB as the **alleged head** ("mutmasslicher Kopf") of the network — a single-leader characterisation typical of Western-Balkans call-centre fraud cases, where one Israeli/Israeli-diaspora operator typically supplies the operational architecture and recruits local-language call-centre staff in the Balkans host country.
- **Operating jurisdiction split**: leadership / financial-flow control allegedly in Israel and (later) Costa Rica; operational call-centre staff in Kosovo; victim base predominantly in Germany.
- **Co-defendants**: the release announces **one principal indictment** of the alleged ringleader. Co-defendant arrests during the 2021 Action Day in Pristina are referenced ("gemeinsamen Action Day") but the total number of additional defendants and the disposition of any Kosovo-domestic prosecutions are not disclosed in the German release.
- **Flight pattern**: the principal defendant fled to **Costa Rica** after the March 2021 Pristina Action Day, triggering issuance of a German national arrest warrant on which an **INTERPOL Red Notice** was based. Costa Rica's eventual extradition in July 2025 reflects the country's pattern of cooperation with European cybercrime prosecutors despite the absence of a comprehensive bilateral extradition treaty (cf. similar 2023–2025 extraditions to Germany and the Netherlands).
- **Structural fit**: the case fits the **Israeli-diaspora-led / Western-Balkans-hosted / German-victim-targeted** call-centre fraud archetype that Bavaria's ZCB and Frankfurt's ZIT have prosecuted repeatedly since 2020. This is *not* a hierarchical mafia-style OCG but a project-based fraud enterprise with the principal supplying the playbook and infrastructure and Kosovar staff supplying the call-floor labour.

## Participating parties

| Country | Agency / authority | Role |
|---|---|---|
| [[germany]] | Kriminalpolizeiinspektion Neu-Ulm (Bavarian State Police) | Lead operational investigator |
| [[germany]] | Zentralstelle Cybercrime Bayern at Generalstaatsanwaltschaft Bamberg | Lead prosecuting authority; international cooperation; indictment filed October 2025 |
| [[germany]] | Landgericht Bamberg — Cyber-Wirtschaftsstrafkammer | Trial court (pending) |
| [[kosovo]] | Kosovo investigative authorities (Pristina) | Joint Action Day partner (March 2021): coordinated searches and call-centre infrastructure dismantling |
| [[costa-rica]] | Costa Rican judicial authorities | Executed German extradition request; surrendered defendant July 2025 |
| [[israel]] | Israeli authorities | Identification and asset-tracing assistance regarding suspect (Israeli national) |

> [!note] Frontmatter strict-IC compliance
> No wiki entity page exists for the Kriminalpolizeiinspektion Neu-Ulm, Generalstaatsanwaltschaft Bamberg / Zentralstelle Cybercrime Bayern, Kosovo investigative authorities, Costa Rican judicial authorities, or Israeli authorities; per L23, `lead_agency`, `coordinating_body`, and `participating_agencies` are left empty in frontmatter and the role information is preserved in prose only.

## Legal framework

- **Extradition treaty basis**: Germany–Costa Rica bilateral extradition arrangements (no comprehensive bilateral extradition treaty in force; surrender was based on reciprocity-and-MLA principles under Costa Rican domestic extradition law). See [[extradition]].
- **Joint investigation Germany–Kosovo (2021)**: conducted under German Strafprozessordnung (StPO) § 92 ff. (Rechtshilfe in Strafsachen) and Kosovo's MLA framework; see [[mlat-process]]. EU pre-accession cooperation channels via Eurojust were also available.
- **INTERPOL Red Notice**: international arrest warrant on Bamberg's German national warrant — fugitive notice that triggered Costa Rica's apprehension.
- **Charge under German law**: § 263 Abs. 1, 3 Nr. 1, Abs. 5 StGB (gewerbs- und bandenmäßiger Betrug — commercial and organized-gang fraud); additional money-laundering charges (§ 261 StGB) likely.

## Operational timeline

| Date | Event |
|---|---|
| ~ 2018–2020 | Network allegedly operates online-investment-fraud / crypto-scam call centres from Pristina, Kosovo, targeting German and worldwide victims |
| 2020–2021 | Bavarian State Police (KPI Neu-Ulm) opens investigation following German victim complaints; ZCB Bamberg assumes prosecutorial lead |
| March 2021 | Joint Action Day with Kosovo investigative authorities in Pristina: coordinated searches, evidence seizure, call-centre infrastructure dismantled |
| ~ 2021–2022 | Defendant flees to Costa Rica; INTERPOL Red Notice issued on Bamberg arrest warrant |
| ~ 2022–2025 | Costa Rican judicial extradition proceedings (multi-year process under Costa Rican domestic extradition law) |
| July 2025 | Defendant extradited from Costa Rica to Germany; placed in pre-trial detention |
| October 2025 | ZCB files indictment at Landgericht Bamberg Cyber-Wirtschaftsstrafkammer |
| 23 January 2026 | Generalstaatsanwaltschaft Bamberg publishes PM 3/2026 announcing the indictment |
| pending | Trial proceedings |

## Results and impact

- **1 indictment** filed in October 2025 (defendant in custody following July 2025 extradition).
- **Damages**: at least €4.5 million from German victims; estimated minimum €21 million worldwide.
- **Infrastructure**: call-centre operations in Pristina dismantled (2021 Action Day).
- **Precedent value**: confirms Costa Rica's willingness to extradite cyber-enabled-fraud fugitives to Germany on reciprocity basis even absent a comprehensive bilateral treaty; demonstrates Bavaria–Kosovo investigative-cooperation channel for cybercrime call-centre takedowns.

## Cooperation mechanisms used

- **Joint Action Day** (Germany–Kosovo, March 2021) — coordinated cross-border searches and arrests; an informal but operationally tight cooperation pattern increasingly common between EU member states and Western Balkans candidate jurisdictions in cybercrime matters. See [[extradition]] and [[mlat-process]].
- **MLA evidence transfer** (Israel → Germany) for identification and asset-tracing of the Israeli-national suspect.
- **Extradition** (Costa Rica → Germany, July 2025) — bilateral surrender on reciprocity basis under Costa Rican domestic extradition law and INTERPOL Red Notice.

## Challenges and friction points

- **Multi-year extradition delay**: defendant fled in approximately 2021–2022; Costa Rican extradition only executed July 2025 — likely 3–4 year proceeding, characteristic of non-treaty extradition channels.
- **Dual nationality complications**: defendant holds Israeli and Portuguese citizenship; could in principle have invoked nationality-bar defences in some jurisdictions, but Costa Rica does not bar extradition of third-country nationals.
- **Evidence chain across three foreign jurisdictions** (Kosovo, Costa Rica, Israel) — typical of complex cyber-fraud cases requiring sustained MLA coordination over multiple years.

## Lessons learned

- Sub-national German prosecutor's offices' specialised central cybercrime units (ZCB Bayern, ZIT Frankfurt, ZAC Köln) increasingly operate as the operational locus for transnational cyber-fraud cases — a structural feature of German federalism that contrasts with the centralised national-prosecutor model in many EU member states.
- Costa Rica continues to serve as a notable extradition partner for European cybercrime prosecutors despite the absence of a comprehensive treaty regime (cf. similar 2023–2025 extraditions to Germany and the Netherlands).
- Pristina remains a recurring operational node for European-language call-centre fraud (cf. parallel Bulgarian/Albanian/Kosovar call-centre takedowns in 2023–2026).

## Korean involvement (한국의 참여)

본 작전에는 한국 수사·검찰 기관의 참여가 1차 출처에 명시되지 않음. 한국 관점의 시사점은, (1) 코스타리카가 비조약 호혜 원칙으로 사이버범죄 도주범을 유럽으로 인도한 선례를 한국이 유사 사건에서 참고할 수 있다는 점, (2) 독일 주(州)검찰의 특별 사이버 중점 부서(ZCB Bayern, ZIT Frankfurt) 모델이 한국 검찰의 사이버수사 조직 강화 논의에 시사점을 줄 수 있다는 점이다.

## Contradictions & open questions

- The primary release does not name a specific Kosovo agency by official title (e.g., Kosovo Police, Special Prosecution Office of the Republic of Kosovo — SPRK). Body prose preserves the generic "Kosovo investigative authorities" formulation pending future enrichment.
- The release does not specify the total number of co-defendants charged in the broader network — only the principal indictment of the alleged ringleader is announced. Co-defendant arrests during the 2021 Action Day in Pristina are referenced but not enumerated.
- Defendant's name not disclosed (German press code); follow-up via court reporting on trial commencement may surface additional identifying detail.

### L26 Background gap notes

> [!note] L26 gap — financial-flow quantification
> The release does not quantify (a) the receiving payment-processor or bank-account chain into which victim deposits were funnelled, (b) the cryptocurrency on-ramps used, (c) total laundered amount versus seized/restrained amount, or (d) the route of fund extraction to the principal defendant's possession in Costa Rica. Asset-tracing across Kosovo and Israel is referenced operationally but not quantified.

> [!note] L26 gap — victim demographic profile
> PM 3/2026 does not disclose the age, occupation or socioeconomic profile of the victim cohort, nor the per-country distribution of the ~€21M worldwide damages outside the €4.5M German share. Whether the network specifically targeted retirees, professionals, or a younger crypto-curious demographic is *unknown* from the tier-1 source.

> [!note] L26 gap — co-defendant disposition
> The number of additional defendants charged in the broader network is not stated; Kosovo-domestic prosecutions arising from the 2021 Action Day are referenced but not enumerated. Whether the Kosovar call-centre staff were prosecuted in Kosovo, in Germany, or not at all remains undisclosed in the tier-1 source.

> [!note] L26 gap — victim-restitution programme
> The release does not describe any victim-restitution mechanism, asset-recovery distribution plan, or *Adhäsionsverfahren* (German criminal-procedure civil-claim joinder) framework for the German victim cohort.

## Sources

- [[2026-01-23_justiz-bayern_bamberg-costa-rica-extradition-international-fraud-network]] — Generalstaatsanwaltschaft Bamberg PM 3/2026 (23 January 2026), `justiz.bayern.de`.
