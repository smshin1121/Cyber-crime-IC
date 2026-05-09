---
type: operation
title: "Latvia Phone-Fraud Money-Mule Network Takedown — €2M Vishing Case (Latvia–Estonia–Germany–Ukraine, 2023–2026)"
title_ko: "라트비아 보이스피싱·돈세탁 조직 단속 — 4국 공조 (2023–2026)"
aliases:
  - "Latvia €2M vishing case"
  - "Valsts policija telefonkrāpšanas lieta"
  - "Latvia phone-fraud 170 money mules case"
case_id: CYB-2026-019
period: 3
operation_type: joint-investigation
status: ongoing
enforcement_type:
  - arrest
  - asset_freeze
  - extradition
outcome: partial
timeframe:
  announced: 2026-03-18
  start: 2023-09
  end: ""
  ongoing: true
crime_types:
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
crime_type: "[[online-fraud-ic]]"
target_entity: "International organised criminal group operating in Latvia since 2023, conducting vishing (telephone fraud) campaigns against EU citizens — including Latvian residents — by impersonating State Police officers and bank employees, inducing victims to install AnyDesk remote-access software and surrender internet-banking credentials, then laundering proceeds through money-mule networks and illegal crypto-asset exchangers based in Riga."
lead_agency: "[[latvia-state-police]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[latvia]]"
  - "[[estonia]]"
  - "[[germany]]"
  - "[[ukraine]]"
participating_agencies:
  - "[[latvia-state-police]]"
  - "[[eurojust]]"
legal_basis:
  - "Latvia Criminal Law (Krimināllikums) Section 177 paragraph 3 — fraud, large scale, organised group"
  - "Latvia Criminal Law Section 195 paragraph 3 — laundering of criminally obtained financial assets, large scale"
  - "Latvia Criminal Law Section 193 paragraph 2 — illegal operations involving payment instruments"
mechanisms_used:
  - "[[eurojust-coordination-meeting]]"
  - "[[extradition]]"
  - "[[asset-freezing]]"
results:
  arrests: 18
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "13 fraudulent call-centre operators detained"
    - "3 organised-crime-group members detained in Latvia (each sentenced to 3 years' deprivation of liberty)"
    - "1 group leader detained in Germany in 2024 (in cooperation with Estonian authorities), later convicted in Estonia"
    - "1 illegal crypto-asset exchanger sentenced to >6 years' deprivation of liberty in Latvia"
    - "2 fugitive suspects detained on 2026-03-12 in Ivano-Frankivsk, Ukraine (Eurojust-supported action with Ukrainian law-enforcement)"
    - "More than 170 money mules identified, of whom 90 recognised as suspects (several already prosecuted, several already convicted)"
    - "EUR 829,650 placed under arrest as criminal-process asset freeze"
    - "2 laptops and 4 mobile phones seized from Ukraine arrests"
    - "Approximately EUR 2,000,000 reported as victim losses across 35 consolidated criminal matters (2023–2024)"
edges:
  - source_actor: latvia-state-police
    target_actor: estonia
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: latvia-state-police
    target_actor: germany
    cooperation_type: extradition
    legal_basis: unknown
    direction: directed
  - source_actor: latvia-state-police
    target_actor: ukraine
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: eurojust
    target_actor: latvia-state-police
    cooperation_type: technical_assistance
    legal_basis: unknown
    direction: directed
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "indictments enumerated separately from convictions"
  - victims_notified
  - "explicit Joint Investigation Team (JIT) registration vs informal Eurojust coordination"
related_cases: []
related_operations:
  - "[[latvia-sim-box-cybercrime-as-a-service-takedown-2025]]"
challenges_encountered: []
lessons_learned:
  - "Four-jurisdiction cooperation arc (Latvia / Estonia / Germany / Ukraine) on a single vishing-plus-laundering organised crime group, with Eurojust acting as the coordinating body for the non-EU (Ukraine) extension of the case."
  - "Convict-in-third-state pattern: group leader detained in Germany in cooperation with Estonia, then convicted in Estonia rather than in Latvia where the underlying fraud victims were located. Demonstrates EU-internal flexibility in choosing the convicting jurisdiction based on evidence center of gravity."
  - "Vishing typology — impersonation of police-and-bank, AnyDesk remote-access deployment, internet-banking credential exfiltration — is recorded verbatim by a Tier-1 prosecutorial source and provides a benchmark IC fact pattern for comparable EU phone-fraud cases."
  - "Money-mule downstream layer in Riga-based illegal crypto-asset exchangers is named explicitly, with one exchanger receiving >6 years — useful precedent on sentencing severity for the laundering-conduit role distinct from the call-centre operator role."
source_count: 1
sources:
  - "[[2026-03-18_prokuratura-lv_telephone-fraud-2-million-euros-170-money-mules]]"
created: 2026-05-09
updated: 2026-05-09
---

> [!info] Provisional page
> This page is published below the preferred normal-page source threshold (`source_count >= 5`) and is marked provisional. It is anchored on a single Tier-1 primary source from the Latvia Prosecutor General's Office (Latvijas Republikas prokuratūra) dated 2026-03-18, mirrored by the Latvia State Police (Valsts policija). It will be promoted to a fully sourced standalone page if and when additional Tier-1 corroboration (Eurojust press release, Estonian/German/Ukrainian authority releases) is ingested.

## Summary

A multi-year Latvian-led criminal investigation into an **international organised crime group conducting vishing (telephone fraud) campaigns against EU citizens** has, as of 2026-03-18, produced arrests and convictions across four jurisdictions ([[latvia|Latvia]], [[estonia|Estonia]], [[germany|Germany]], [[ukraine|Ukraine]]) and is ongoing. The case is investigated by the **2nd Division of the Cybercrime Combating Department of the Latvia State Police** ([[latvia-state-police|Valsts policija]]) and is being coordinated cross-border by the **Latvia Prosecutor General's Office (Latvijas Republikas prokuratūra)** with **[[eurojust|Eurojust]]** support.

The fraudsters posed as State Police officers and bank employees, induced victims to install **AnyDesk remote-access software** and log in to internet banking, then executed transfers using the captured credentials. Across **35 consolidated criminal matters** spanning 2023-09 through 2024-09, victim losses are estimated at approximately **EUR 2,000,000**.

To date the case has identified **more than 170 money mules** (90 recognised as suspects), detained **13 fraudulent call-centre operators**, secured **convictions of three group members in Latvia** (3 years each) and an illegal crypto-asset exchanger (>6 years), and resulted in the **detention of the group leader in Germany in 2024** (in cooperation with Estonian authorities, with subsequent conviction in Estonia). On **2026-03-12**, in a Eurojust-coordinated action with Ukrainian law-enforcement, **two fugitive suspects were detained in Ivano-Frankivsk, Ukraine**, on suspicion of organised-group money laundering. **EUR 829,650** is currently under criminal-process asset arrest.

## Background

From September 2023 onward, multiple Latvian residents reported to the State Police that they had received fraudulent telephone calls from persons posing as police officers and bank employees. The script was uniform: callers told residents that loans had allegedly been taken out in their names or that suspicious financial activity was occurring on their accounts, and asked them to help "expose the fraudsters" (Latvian: *atmaskot krāpniekus*).

Victims were instructed to install the remote-access program **AnyDesk** on a computer or mobile phone and to log in to internet banking. Once remote access and authenticated sessions were established, the fraudsters captured banking credentials and induced victims to confirm transactions executed by the criminals.

The Latvia Prosecutor General's Office release explicitly characterises the activity as **campaign-style** (Latvian: *kampaņveidīgi*), conducted by a structured organised crime group that had been operating in Latvia **since 2023** and was engaged in laundering criminally obtained funds across **European Union member states**. The group's downstream laundering layer included **illegal crypto-asset exchangers operating in Riga**.

## Participating Parties

| Role | Party |
|---|---|
| Lead investigator | [[latvia-state-police\|Latvia State Police (Valsts policija)]] — Cybercrime Combating Department, 2nd Division |
| Lead prosecutor | Latvia Prosecutor General's Office (Latvijas Republikas prokuratūra) |
| Coordinating body for cross-border action | [[eurojust\|Eurojust]] |
| Cooperating jurisdiction (group-leader detention 2024) | [[germany\|Germany]] |
| Cooperating jurisdiction (group-leader trial / conviction) | [[estonia\|Estonia]] (Estonian law-enforcement authorities) |
| Cooperating jurisdiction (2026-03-12 arrests) | [[ukraine\|Ukraine]] (Ukrainian law-enforcement authorities) |

## Legal Framework

- **Substantive offences (Latvia)**: Criminal Law (*Krimināllikums*) Section 177 paragraph 3 (*krāpšana lielā apmērā organizētā grupā* — fraud on a large scale committed in an organised group); Section 195 paragraph 3 (*noziedzīgi iegūtu finanšu līdzekļu legalizēšana lielā apmērā* — laundering of criminally obtained financial assets, large scale); Section 193 paragraph 2 (*nelikumīgas darbības ar maksāšanas līdzekļiem* — illegal operations involving payment instruments).
- **Cross-border cooperation framework**: cooperation with [[estonia|Estonia]] is described in the release without specifying the formal instrument; the 2024 detention of the group leader **in Germany** strongly suggests use of the [[european-arrest-warrant|European Arrest Warrant]] framework (binding among Latvia/Estonia/Germany), but the release does not name it explicitly. The [[ukraine|Ukraine]] arm of the operation on 2026-03-12 is described as cooperation with Ukrainian law-enforcement and **[[eurojust|Eurojust]]**, with the Latvia Prosecutor General's Office as the requesting authority.

> [!warning] Legal status check needed
> The release does not explicitly cite the European Arrest Warrant, the European Investigation Order, or a registered Joint Investigation Team. The wiki record uses the more general [[eurojust-coordination-meeting]] and [[extradition]] mechanism tags rather than asserting [[european-arrest-warrant]] or [[joint-investigation-team]] without a primary-source reference.

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2023 (since) | International organised crime group operating in Latvia, laundering proceeds in EU member states | prokuratura.lv 2026-03-18 |
| 2023-09 → 2024-09 | Victim reports to Latvia State Police; multiple criminal proceedings opened | prokuratura.lv 2026-03-18 |
| 2024 (date unspecified) | Group leader detained in Germany in cooperation with Estonian authorities | prokuratura.lv 2026-03-18 |
| 2024 (post-detention) | Group leader convicted in Estonia | prokuratura.lv 2026-03-18 |
| 2024–2026 (ongoing) | 3 group members detained in Latvia, each sentenced to 3 years; 1 illegal crypto-asset exchanger sentenced to >6 years; 13 call-centre operators detained | prokuratura.lv 2026-03-18 |
| 2026-03-12 | 2 fugitive suspects detained in Ivano-Frankivsk, Ukraine (Eurojust-supported action with Ukrainian law-enforcement and Latvia Prosecutor General's Office); 2 laptops + 4 mobile phones seized | prokuratura.lv 2026-03-18 |
| 2026-03-18 | Latvia Prosecutor General's Office publishes case summary | prokuratura.lv 2026-03-18 |

## Results and Impact

- **Arrests / detentions** (cumulative across 2024–2026):
  - 13 fraudulent call-centre operators (Latvia)
  - 3 organised-crime-group members in Latvia (each sentenced to 3 years' deprivation of liberty)
  - 1 group leader in Germany (2024), convicted in Estonia
  - 1 illegal crypto-asset exchanger in Latvia (sentenced to >6 years)
  - 2 fugitive suspects detained in Ivano-Frankivsk, Ukraine (2026-03-12)
- **Money-mule layer**: more than 170 individuals identified, 90 recognised as suspects, several prosecuted, several convicted.
- **Asset measures**: EUR 829,650 placed under criminal-process arrest.
- **Reported victim losses**: approximately EUR 2,000,000 across 35 consolidated criminal matters (2023–2024).
- **Evidence seized in Ukraine arrests**: 2 laptops, 4 mobile phones, plus other unspecified evidence.

## Cooperation Mechanisms Used

The release names three explicit cooperation arcs:

1. **Latvia ↔ Estonia (2024)** — cooperation between Latvia State Police and Estonian law-enforcement authorities led to the detention of the group leader **in Germany**, with the leader subsequently convicted in Estonia. The convicting jurisdiction is the cooperating partner rather than either the country of detention (Germany) or the country of victim losses (Latvia).
2. **Latvia ↔ Germany (2024)** — operational detention; the release does not specify the formal extradition or arrest-warrant instrument used.
3. **Latvia ↔ Ukraine + [[eurojust|Eurojust]] (2026-03-12)** — Latvia Prosecutor General's Office coordinated with Ukrainian law-enforcement authorities and Eurojust to detain two fugitive suspects in Ivano-Frankivsk. This is the non-EU extension arc of the case.

[[asset-freezing|Asset freezing]] (criminal-process arrest of EUR 829,650) is recorded as an additional mechanism.

## Challenges and Friction Points

- **Tracing money-mule layer at scale**: identifying 170+ money mules and the downstream illegal crypto-asset exchangers required a sustained 2023–2026 investigation; the release notes that some money mules have been prosecuted while others remain at the suspect stage.
- **Fugitive flight to non-EU jurisdiction**: two suspects fled to Ukraine after EU-internal arrests of co-conspirators, requiring Eurojust-coordinated action with Ukrainian authorities to extend the case beyond EU mutual-recognition mechanisms.
- **Convict-in-third-state pattern**: the group leader was detained in Germany but tried and convicted in Estonia. The release does not explain why Estonia was the convicting forum rather than Latvia (the country of underlying victim losses).

## Lessons Learned

- Four-jurisdiction phone-fraud-and-laundering cases can be sustained through Eurojust coordination plus bilateral law-enforcement cooperation, even where the specific formal instruments (EAW, EIO, JIT) are not enumerated in the public release.
- Sentencing severity is differentiated by role: call-centre operators (collective detention without individual sentences disclosed), front-line group members (3 years each in Latvia), illegal crypto-asset exchanger (>6 years in Latvia), with the laundering-conduit role attracting the heaviest individual sentence in the disclosed Latvian segment.
- The AnyDesk + impersonation-of-police-and-bank vector is reported here verbatim by a Tier-1 prosecutorial source and is consistent with the broader EU phone-fraud typology.

## Follow-Up Actions

- The criminal investigation is **ongoing** as of 2026-03-18.
- Further proceedings against the remaining 80 of the 170+ identified money mules are anticipated.
- The Ukraine-detained suspects' subsequent surrender, prosecution, or transfer status is not described in the release.

## Korean Involvement (한국의 참여)

None reported. South Korea is not named in the cited Tier-1 source as a participating jurisdiction or victim country. The AnyDesk + impersonation-of-police vector is structurally similar to typologies used in Korean voice-phishing cases but the present case has no direct Korean nexus.

## Contradictions & Open Questions

- The release does not name the formal cross-border instruments (European Arrest Warrant, European Investigation Order, registered Joint Investigation Team) used in the 2024 Germany detention or the 2024–2026 Estonia convictions.
- The release does not state why the convicting forum for the group leader was Estonia rather than Latvia.
- The release does not enumerate indictments separately from convictions — `results.indictments` is left at 0 pending corroborating sources.
- The relationship (if any) of this network to the separate [[latvia-sim-box-cybercrime-as-a-service-takedown-2025|Latvia SIM-box CaaS network takedown (October 2025)]] — also led by the Latvia State Police Cybercrime Combating Department — is not addressed in the release.
- The release does not name individual defendants, the specific Estonian and German authorities involved, or the Ukrainian law-enforcement body.
- Whether [[europol-ec3|Europol]] participated in the case (alongside Eurojust) is not stated in the release.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2026-03-18_prokuratura-lv_telephone-fraud-2-million-euros-170-money-mules\|Izkrāpti 2 miljoni eiro: Valsts policija telefonkrāpšanas lietā noskaidro vairāk nekā 170 naudas mūļus un nelikumīgos kriptoaktīvu mainītājus]] | Latvijas Republikas prokuratūra | 2026-03-18 | https://www.prokuratura.lv/lv/aktualitates/2026/aktualitates/izkrapti-2-miljoni-eiro-valsts-policija-telefonkrapsanas-lieta-noskaidro-vairak-neka-170-naudas-mulus-un-nelikumigos-kriptoaktivu-mainitajus-3712 |
