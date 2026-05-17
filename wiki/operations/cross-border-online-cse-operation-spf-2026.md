---
type: operation
title: "Cross-Border Online CSE Operation (SPF-led, 2026)"
aliases:
  - "Singapore-led 7-Jurisdiction OCSE Crackdown 2026"
  - "SPF Cross-Border OCSE Operation 2026"
case_id: CYB-2026-013
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - search
outcome: success
timeframe:
  announced: 2026-04-28
  start: 2026-03-23
  end: 2026-04-17
  ongoing: false
crime_types:
  - "[[csam-ic]]"
crime_type: "[[csam-ic]]"
target_entity: "Online child sexual exploitation offenders across seven Asian jurisdictions"
lead_agency: "[[singapore-police]]"
coordinating_body: "[[singapore-police]]"
participating_countries:
  - "[[singapore]]"
  - "[[hong-kong]]"
  - "[[japan]]"
  - "[[south-korea]]"
  - "[[malaysia]]"
  - "[[thailand]]"
  - "[[brunei]]"
participating_agencies:
  - "[[singapore-police]]"
  - "[[hong-kong-police]]"
  - "[[japan-npa]]"
  - "[[knpa-cyber-bureau]]"
  - "[[royal-malaysia-police]]"
  - "[[thai-royal-police]]"
legal_basis:
  - "domestic CSAM and child-protection enforcement powers of each participating jurisdiction"
  - "police-to-police coordinated enforcement"
mechanisms_used:
  - "[[informal-cooperation]]"
  - "[[public-private-cooperation]]"
results:
  arrests: 326
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "119 additional persons assisting with investigations (total subjects: 445)."
    - "382 locations raided across the seven participating countries."
    - "Subjects: 430 men, 15 women, ages 12-72."
    - "Singapore: 11 men arrested (aged 22-44) and 16 others under investigation."
    - "Devices and items seized: 116 computers, 340 handphones, 25 tablets, 140 storage devices, 16 routers."
edges:
  - source_actor: singapore-police
    target_actor: hong-kong-police
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: singapore-police
    target_actor: japan-npa
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: singapore-police
    target_actor: knpa-cyber-bureau
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: singapore-police
    target_actor: royal-malaysia-police
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: singapore-police
    target_actor: thai-royal-police
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "per-country arrest breakdown beyond Singapore"
  - "umbrella operation name (not given in the SPF release text)"
related_cases:
  []
related_operations:
  - "[[operation-cyber-guardian]]"
  - "[[frontier-plus-cross-border-anti-scam-2025]]"
challenges_encountered:
  []
lessons_learned:
  []
source_count: 1
sources:
  - "[[2026-04-28_police-gov-sg_326-arrested-119-investigated-cross-border-online-cse-operation]]"
created: 2026-05-09
updated: 2026-05-17
last_enriched: 2026-05-17
---
> [!info] Provisional / single-source
> This page is provisional and currently relies on a single tier-1 primary source (the Singapore Police Force press release of 28 April 2026). Per the wiki's preferred publication threshold, additional tier-1 corroborating sources from partner jurisdictions (HKPF, JNPA, KNPA, RMP, RTP, RBPF) should be ingested before this page is treated as fully established.

## Summary

The **Cross-Border Online CSE Operation (SPF-led, 2026)** was a seven-jurisdiction Asian police operation against online child sexual exploitation, conducted between **23 March and 17 April 2026** and announced by the [[singapore-police|Singapore Police Force]] (SPF) on **28 April 2026**. Police services from [[singapore|Singapore]], [[hong-kong|Hong Kong]], [[japan|Japan]], [[south-korea|South Korea]], [[malaysia|Malaysia]], [[thailand|Thailand]], and [[brunei|Brunei]] participated. Aggregate publicly reported results were **326 persons arrested and 119 additional persons assisting with investigations** (445 total subjects), with **382 locations raided** across the seven participating countries.

The operation extends the SPF-led regional OCSE cooperation pattern previously documented in the 2025 [[operation-cyber-guardian]] crackdown, with **Brunei** added as a seventh participating jurisdiction in 2026.

## Background

### Modus operandi

The 2026 SPF release enumerates the targeted offending categories as: **production and distribution of CSAM, sexual communication with minors, commercial sexual exploitation of children, threats to distribute intimate recordings, and obscene material distribution**. Translated into operational typology, the OCSE conduct targeted spans:

- **CSAM production / distribution / possession**: peer-to-peer (P2P) sharing, social-media / encrypted-messenger distribution, cloud-storage hosting, and CSAM-forum posting. Detection workflow typically combines NCMEC CyberTipline reports (from U.S. electronic service providers reporting apparent CSAM under 18 U.S.C. § 2258A) and platform Trust & Safety referrals against domestic CSAM hash-databases, with each national service running attribution against its own subscriber base.
- **Online sexual grooming**: contact offences where adult subjects use social-media, messenger, or gaming platforms to solicit sexual conduct or imagery from minors. Detection runs through victim disclosure, platform reports, and undercover operations.
- **Commercial sexual exploitation of children (CSEC)**: paid live-streaming abuse, escort-style child-exploitation services, and subscription / pay-per-view CSAM forum operation. Detection requires payment-rail attribution and platform-side financial-flow analysis.
- **Sextortion ("threats to distribute intimate recordings")**: coercive distribution-threat schemes against minors who have shared intimate imagery, typically demanding additional imagery or money. This pattern has driven significant Asia-Pacific minor-victim self-harm cases and is a high-priority OCSE category in 2025-2026 regional enforcement.
- **Obscene-material distribution**: catch-all category for non-CSAM but illegal-under-domestic-law obscene material distributed online (varies sharply by jurisdiction — e.g., Brunei, Malaysia, and Singapore have broader obscenity statutes than other partner jurisdictions).

Each national service ran enforcement under its own domestic powers, with synchronised raid windows and SPF acting as the regional coordinator. The 116 computers, 340 mobile phones, 25 tablets, 140 storage devices, and 16 routers seized are consistent with the canonical OCSE-sweep evidence-collection pattern: residential premises raids on identified subscribers, on-site seizure of all internet-capable storage and networking devices, and forensic analysis for CSAM possession and grooming-communication recovery.

### Victim profile and impact

Victims are **children depicted in the CSAM in circulation, plus minors who were groomed, sextorted, or commercially exploited** by the 445 subjects identified across the seven jurisdictions. The SPF release does **not** publish:

- a verified victim count or identified-child count;
- the number of children rescued from active abuse during the action window;
- per-offence-category victim breakdowns (CSAM-possession victim count vs. grooming victim count vs. CSEC victim count vs. sextortion victim count);
- any victim-nationality breakdown across the seven participating jurisdictions.

The operation is **structured primarily as an offender-attribution sweep rather than a victim-rescue operation**: the 326 arrests and 119 additional subjects under investigation reflect demand-side and distribution-side OCSE-population disruption, not contact-abuser identification driven by victim disclosure. The SPF's continued participation in this annual regional model is consistent with the Asia-Pacific police view that aggressive demand-side enforcement reduces CSAM-market circulation and grooming-platform tolerance.

### Financial flow

For **CSAM possession / distribution / sextortion**, no inherent financial flow is involved — these are non-commercial offences in the targeted population. For **commercial sexual exploitation of children (CSEC)**, the SPF release does **not** publish any cryptocurrency seizure, payment-rail attribution, or financial-flow attribution. This is a significant omission given that CSEC is one of the explicitly enumerated targeted offence categories: large-scale Asia-Pacific CSEC investigations (notably the Philippines OSEC livestream-abuse cases) typically generate cryptocurrency seizures and remittance-channel attribution (Wise, Western Union, MoneyGram, regional remittance corridors). The absence is either (a) genuine — the 2026 operation focused on CSAM-population sweep and de-emphasised CSEC payment-rail work — or (b) reporting-suppressed at the regional-aggregate level and held back to individual national charging announcements. Gap is noted in Contradictions & Open Questions.

### Criminal organisation structure

Consistent with the canonical OCSE-sweep model, the 445 identified subjects are **not described as a single hierarchical organised crime group**. The targeted population structure across the seven jurisdictions is **a loose population of individually operating CSAM possessors, distributors, groomers, sextortionists, and CSEC purchasers**, connected only by their shared use of P2P networks, social-media platforms, encrypted messengers, and CSAM forums. The SPF release does not allege:

- a single named OCG or syndicate operating across the seven jurisdictions;
- a single CSAM-distribution platform or forum at the centre of the targeting (contrast with prior Welcome to Video / Darknet CSAM forum takedowns where a specific platform was the disruption target);
- a producer-distributor-consumer hierarchy with named leadership.

Subject demographics (430 men, 15 women, ages 12-72) suggest a broad-spectrum offender population rather than a coordinated network. The model is therefore **enforcement-population sweep** rather than OCG-decapitation, mirroring the structural approach of [[operation-cyber-guardian]] in 2025 and the [[aliados-por-la-infancia-vi-mpf-caba-2026|MPF CABA "Aliados por la Infancia VI" operation]] in the Latin-American hemisphere — convergent design choices across distinct multilateral OCSE-enforcement programmes.

### Series context

Online child sexual exploitation, including production, possession, distribution of child sexual abuse material (CSAM) and online sexual communication with minors, is a recurrent focus of Asia-Pacific multilateral police cooperation. Following the 2025 SPF-coordinated six-jurisdiction crackdown ([[operation-cyber-guardian]]), the 2026 edition continued the pattern of synchronised national enforcement under SPF coordination, with the [[singapore-police|SPF]] Specialised Crime Branch of the Criminal Investigation Department (CID) running the Singapore-side investigations.

## Participating Parties

| Country / Jurisdiction | Publicly named agency | Role |
|---|---|---|
| [[singapore|Singapore]] | [[singapore-police|Singapore Police Force]] (Specialised Crime Branch, CID) | Lead / coordinating |
| [[hong-kong|Hong Kong]] | [[hong-kong-police|Hong Kong Police Force]] | Participating |
| [[japan|Japan]] | [[japan-npa|National Police Agency of Japan]] | Participating |
| [[south-korea|South Korea]] | [[knpa-cyber-bureau|Korean National Police Agency]] | Participating |
| [[malaysia|Malaysia]] | [[royal-malaysia-police|Royal Malaysia Police]] | Participating |
| [[thailand|Thailand]] | [[thai-royal-police|Royal Thai Police]] | Participating |
| [[brunei|Brunei]] | Royal Brunei Police Force | Participating (new vs. 2025 edition) |

> [!note] Translation note
> The Royal Brunei Police Force does not currently have a dedicated organization page in this wiki. Its participation is recorded here in prose pending creation of a stub or full organization page in a separate ingest pass.

## Legal Framework

The SPF release does not name a formal MLAT, treaty, or INTERPOL Notice as the legal basis. Each participating service is described as acting under its own domestic CSAM and child-protection enforcement powers, with cross-border coordination conducted on a police-to-police basis. Cooperation is therefore best characterised as [[informal-cooperation|informal police cooperation]], supplemented by [[public-private-cooperation|private-sector cooperation]] indicated by the senior-officer statement that law enforcement worked alongside private-sector capabilities.

> [!warning] Legal status check needed
> The release does not explicitly invoke the [[budapest-convention|Budapest Convention]] or INTERPOL Notice mechanisms. None of the participating Asian jurisdictions are States Parties to the Budapest Convention as of the time of writing, so the cooperation is *likely* not running through that framework. Confirmation in partner-jurisdiction releases would strengthen this assessment.

## Operational Timeline

| Date | Event |
|---|---|
| 2026-03-23 | Operation period begins (synchronised enforcement window). |
| 2026-04-17 | Operation period ends. |
| 2026-04-28 | Singapore Police Force publicly announces aggregate results. |

## Results and Impact

| Metric | Detail |
|---|---|
| Persons arrested | 326 |
| Persons assisting with investigations | 119 |
| Total subjects | 445 (430 men, 15 women, ages 12-72) |
| Locations raided | 382 across seven countries |
| Singapore arrests | 11 men, aged 22-44 |
| Singapore subjects under investigation | 16 |
| Computers seized | 116 |
| Mobile phones seized | 340 |
| Tablets seized | 25 |
| Storage devices seized | 140 |
| Routers seized | 16 |

Per-country arrest breakdowns beyond Singapore are not given in the SPF release.

## Cooperation Mechanisms Used

The cooperation pattern is consistent with the SPF-led 2025 six-jurisdiction OCSE crackdown ([[operation-cyber-guardian]]):

- A shared, time-bounded operational window with synchronised national enforcement.
- SPF acting as the coordinating service.
- Each participating service acting under domestic legal authority.
- Private-sector technical cooperation referenced in the senior-officer statement, suggesting platform/provider engagement on detection of CSAM-related conduct.

The release explicitly highlights that "by bringing together law enforcement efforts and private sector capabilities, we can intervene swiftly to identify and arrest offenders" (Deputy Commissioner Zhang Weihan, SPF).

## Challenges and Friction Points

The single-source state of this page limits assessment of friction points. Likely structural challenges in any seven-jurisdiction Asian OCSE operation include divergent CSAM legal definitions and age-of-consent thresholds, varying procedural powers for production orders against messaging providers, and the absence of a shared regional procedural treaty. None of these are explicitly discussed in the SPF release.

## Lessons Learned

The release does not enumerate lessons. The continuity from the 2025 [[operation-cyber-guardian]] to this 2026 edition is *likely* (medium confidence) evidence that the SPF-coordinated regional model has been judged useful enough by participating services to repeat and expand (Brunei added). This is a tentative inference, not a stated finding.

## Follow-Up Actions

Not specified in the release.

## Korean Involvement (한국의 참여)

The [[knpa-cyber-bureau|Korean National Police Agency]] is named as a participating agency. The SPF release does not give a Korean-side arrest breakdown. In the prior 2025 [[operation-cyber-guardian]] edition, Korean authorities accounted for the majority of publicly reported subjects (435 of 544); whether a similar share holds in 2026 cannot be determined from the SPF release alone. Korean-side reporting from KNPA or domestic Korean media would be the natural cross-check.

## Contradictions & Open Questions

- **Operation name**: The SPF release does not give the 2026 edition an umbrella name analogous to "Cyber Guardian". It is therefore filed here under a descriptive title rather than under a publicly attested operation name.
- **Per-country breakdown**: Only the Singapore subset is given (11 + 16). Breakdowns for Hong Kong, Japan, South Korea, Malaysia, Thailand, and Brunei are not in the SPF release.
- **Relationship to Operation Cyber Guardian**: Whether this is a formal sequel to [[operation-cyber-guardian]] or a parallel-but-distinct operation is not stated in the SPF release. Structural and personnel continuity (SPF coordination, CID Specialised Crime Branch, OCSE focus, synchronised window) makes a sequel relationship *likely* (medium confidence), but this is an inference.
- **Legal mechanism**: No MLAT, treaty article, or INTERPOL Notice is explicitly invoked. Whether parts of the operation used INTERPOL channels (for example via [[interpol-i24-7|I-24/7]] or [[interpol-asean-desk|the INTERPOL ASEAN desk]]) cannot be confirmed from this single source.
- **Brunei addition**: The expansion to seven jurisdictions with the addition of the Royal Brunei Police Force is a notable development; the rationale for its addition is not given in the release.
- **L26 Background gap — victim count and rescue count**: The SPF release does not publish a verified victim count, identified-child count, number-rescued-from-active-abuse count, or per-offence-category victim breakdown. The operation reads as an offender-attribution sweep rather than a victim-rescue operation, but the absence of an explicit "no children rescued" or "N children identified" statement leaves the rescue dimension undocumented.
- **L26 Background gap — CSEC financial-flow attribution**: Commercial sexual exploitation of children (CSEC) is named as a targeted offence category, but the SPF release publishes no cryptocurrency seizure, payment-rail attribution, remittance-channel attribution, or other financial-flow data. This is anomalous for a CSEC-inclusive operation and suggests either de-emphasis of CSEC payment work in 2026 or aggregation-level reporting-suppression. Partner-jurisdiction releases (RTP Thailand, RMP Malaysia in particular) should be cross-checked to close this gap.
- **L26 Background gap — OCG vs. population sweep characterisation**: The release does not affirm whether the 445 subjects were connected through any single CSAM platform, forum, or syndicate, or whether they are independently operating offenders identified through separate national leads. Default characterisation here is "population sweep" rather than "OCG decapitation" but partner-jurisdiction releases may add OCG attribution that the SPF aggregate release suppresses.
