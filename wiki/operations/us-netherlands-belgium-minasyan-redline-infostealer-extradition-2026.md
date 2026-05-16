---
type: operation
title: "US–Netherlands–Belgium Minasyan RedLine Infostealer Extradition (2026-03)"
title_ko: "미국–네덜란드–벨기에 RedLine 인포스틸러 미나샨 신병인도 (2026-03)"
aliases:
  - "Minasyan RedLine extradition"
  - "RedLine Armenian extradition 2026"
  - "USAO-WDTX Minasyan March 2026"
case_id: CYB-2026-325
period: 3
operation_type: arrest-sweep
status: ongoing
enforcement_type:
  - arrest
  - extradition
  - indictment
outcome: partial
timeframe:
  announced: 2026-03-25
  start: 2026-03-23
  end: 2026-03-24
  ongoing: true
crime_type: "[[malware-ic]]"
crime_types:
  - "[[malware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[money-laundering-ic]]"
  - "[[hacking-ic]]"
target_entity: "Hambardzum Minasyan — Armenian national, alleged co-developer and administrator of the RedLine infostealing malware family; allegedly registered virtual private servers, internet domains, and a cryptocurrency account used to support and monetise the RedLine scheme. Charged in W.D. Tex. as part of a multi-developer/multi-admin conspiracy following the October 2024 Operation Magnus infrastructure disruption."
lead_agency: "[[us-doj]]"
coordinating_body: "[[office-of-international-affairs]]"
participating_countries:
  - "[[united-states]]"
  - "[[netherlands]]"
  - "[[belgium]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[office-of-international-affairs]]"
  - "[[eurojust]]"
organizations:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[office-of-international-affairs]]"
  - "[[eurojust]]"
mechanisms_used:
  - "[[extradition]]"
  - "[[mutual-legal-assistance]]"
legal_basis:
  - "Indictment in the U.S. District Court for the Western District of Texas (Austin Division) charging conspiracy to commit access device fraud (18 U.S.C. § 1029(b)(2)), conspiracy to violate the Computer Fraud and Abuse Act (18 U.S.C. § 1030), and conspiracy to commit money laundering (18 U.S.C. § 1956(h))."
  - "Extradition from the Netherlands to the United States executed 2026-03-23, secured by the U.S. DOJ Office of International Affairs under U.S.–Netherlands extradition arrangements."
  - "Follow-through coordination from Operation Magnus (October 2024) joint disruption of RedLine in which DOJ joined the Netherlands, Belgium, Eurojust and other partners."
results:
  arrests: 1
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Defendant Hambardzum Minasyan arraigned in U.S. District Court (W.D. Tex., Austin) on 2026-03-24."
    - "Statutory maximum exposure: up to 10 years for access device fraud conspiracy + up to 20 years each for CFAA conspiracy and money laundering conspiracy (combined potential up to 50 years)."
    - "Co-conspirator Maxim Rudometov previously charged in October 2024 (separate indictment, same RedLine matter)."
edges:
  - source_actor: us-doj
    target_actor: netherlands
    cooperation_type: extradition
    legal_basis: bilateral_MOU
    direction: directed
  - source_actor: us-doj
    target_actor: belgium
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: us-doj
    target_actor: eurojust
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: undirected
  - source_actor: fbi
    target_actor: office-of-international-affairs
    cooperation_type: evidence_transfer
    legal_basis: MLAT
    direction: directed
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "victims_notified — RedLine victim count not enumerated in this charging-stage press release"
  - "cryptocurrency_seized — no asset seizure figures disclosed at this extradition/arraignment stage"
related_cases: []
related_operations:
  - "[[operation-magnus-redline-meta-stealer-takedown-2024]]"
challenges_encountered: []
lessons_learned:
  - "Multi-year extradition follow-through: a successful joint infrastructure disruption (here, Operation Magnus, Oct 2024) creates the evidentiary base for individual-defendant extraditions 16+ months later, illustrating the long-tail nature of cyber-IC cooperation timelines."
  - "Domain-of-jurisdiction interplay: an alleged Armenian developer arrested in the Netherlands and extradited to a U.S. district court (W.D. Tex.) — three distinct jurisdictions cooperating to produce one defendant in one trial venue."
source_count: 1
sources:
  - "[[2026-03-25_justice-gov-usao-wdtx_armenian-man-extradited-redline-infostealer]]"
created: 2026-05-16
updated: 2026-05-16
---

# US–Netherlands–Belgium Minasyan RedLine Infostealer Extradition (2026-03)

> [!info] Provisional / single-tier-1 ingest
> This page is published at the `source_count = 1` threshold against a single tier-1 own-domain U.S. Attorney's Office press release. Per CLAUDE.md preferred publication threshold (`source_count >= 5`), this page is **explicitly provisional** and should be enriched as additional Netherlands, Belgium, or Eurojust own-domain releases on the same matter become available, or as case proceedings advance in W.D. Tex.

## Summary

On 2026-03-23, Hambardzum Minasyan — an Armenian national and alleged co-developer/administrator of the **RedLine infostealing malware** — was extradited from the **Netherlands** to the **United States** to face federal charges in the U.S. District Court for the Western District of Texas (Austin Division). He was arraigned the next day, 2026-03-24, and the U.S. Attorney for the Western District of Texas, [Justin R. Simmons], announced the case publicly on 2026-03-25.

The indictment, returned in W.D. Tex., charges Minasyan with:
- Conspiracy to commit access device fraud (18 U.S.C. § 1029(b)(2));
- Conspiracy to violate the Computer Fraud and Abuse Act (18 U.S.C. § 1030);
- Conspiracy to commit money laundering (18 U.S.C. § 1956(h)).

If convicted on all counts, Minasyan faces a statutory maximum of up to 50 years' imprisonment.

This event is the **second** publicly known defendant in the U.S. RedLine infostealer prosecution wave, following the October 2024 unsealing of charges against alleged co-conspirator **Maxim Rudometov** in connection with [[operation-magnus-redline-meta-stealer-takedown-2024|Operation Magnus]].

## Background

RedLine is described by U.S. authorities as one of the most prevalent infostealing malware variants in the world. Distributed under an affiliate/lease model, it harvests stored credentials, browser cookies, autofill data, and cryptocurrency wallet artefacts from infected hosts and exfiltrates them to operator-controlled infrastructure. RedLine-stolen logs have been previously used to gain initial-access footholds for ransomware intrusions and major-corporation breaches.

The indictment alleges Minasyan, in conjunction with co-developers and administrators:
- Registered two virtual private servers to host portions of RedLine's infrastructure;
- Registered two internet domains in support of the RedLine scheme;
- Created repositories on an online file-sharing site used to distribute RedLine to affiliates;
- In November 2021, registered a cryptocurrency account used to receive RedLine affiliate payments.

## Participating Parties

### United States (charging jurisdiction)
- **U.S. Department of Justice** ([[us-doj]]) — overall coordination
- **FBI Austin Cyber Task Force** ([[fbi]]) — lead investigative coalition; the task-force composition includes:
  - Naval Criminal Investigative Service (NCIS)
  - IRS Criminal Investigation (IRS-CI)
  - DoD Office of Inspector General's Defense Criminal Investigative Service (DCIS)
  - Army Criminal Investigation Division (Army CID)
- **U.S. Attorney's Office, Western District of Texas** (USAO-WDTX) — Justin R. Simmons (U.S. Attorney) and Kirk Mangels (Assistant U.S. Attorney prosecuting)
- **DOJ Office of International Affairs** ([[office-of-international-affairs]]) — secured the arrest and March 23, 2026 extradition
- **DOJ Criminal Division International Computer Hacking and Intellectual Property (ICHIP)** — attorney advisor based at Eurojust in The Hague

### Netherlands (extraditing state)
- Dutch authorities executed the arrest and extradition. The USAO-WDTX release names "the Netherlands" as a partner in the underlying disruption pipeline (Operation Magnus, October 2024) without identifying a specific Dutch police or prosecutor service in the March 25, 2026 release. (Cross-reference: [[netherlands-politie]] and [[netherlands-om]] are commonly named partners in DOJ–NL cyber matters; see [[operation-magnus-redline-meta-stealer-takedown-2024]] for the canonical Dutch cooperation list.)

### Belgium (joint disruption partner)
- Named as a 2024 Operation Magnus partner alongside the Netherlands and Eurojust ([[belgium-federal-police]] is the canonical Belgian federal LE partner).

### EU coordination
- **Eurojust** ([[eurojust]]) — earlier joint disruption coordination; the ICHIP attorney advisor at Eurojust in The Hague supports US–EU cyber prosecutions of this kind.

## Legal Framework

The case is being prosecuted under three U.S. federal conspiracy statutes — access device fraud, CFAA, and money laundering — typical of the U.S. infostealer-as-a-service charging architecture. The extradition itself was effected under the U.S.–Netherlands extradition relationship, administered on the U.S. side by the DOJ Office of International Affairs.

## Operational Timeline

| Date | Event |
|------|-------|
| Nov 2021 | Per indictment: Minasyan registers cryptocurrency account used to receive RedLine affiliate payments |
| Oct 2024 | Operation Magnus: DOJ joins Netherlands, Belgium, Eurojust and other partners in international disruption of RedLine; charges unsealed against co-conspirator Maxim Rudometov |
| 2026-03-23 | Minasyan extradited from the Netherlands to the United States |
| 2026-03-24 | Initial appearance / arraignment in U.S. District Court (W.D. Tex., Austin) |
| 2026-03-25 | USAO-WDTX press release announcing the case |
| Pending | Trial in W.D. Tex. |

## Results and Impact

- **1 arrest / extradition** of a charged co-developer/administrator (Minasyan);
- **1 indictment** in W.D. Tex.;
- This is an **incremental** prosecutorial step — the 2024 Operation Magnus had already disrupted RedLine infrastructure and unsealed charges against Rudometov; the 2026 event escalates the case to a second physically-extradited defendant.

## Cooperation Mechanisms Used

- **[[extradition|Extradition]]** — Netherlands → United States, executed 2026-03-23
- **[[mutual-legal-assistance|Mutual Legal Assistance]]** — implicit in OIA evidence/process exchange channels
- **DOJ–Eurojust ICHIP attorney advisor** — embedded liaison at Eurojust supporting US–EU coordination
- **Multi-agency U.S. cyber task force model** — FBI-led, military criminal investigative agencies (NCIS, DCIS, Army CID) + civilian agencies (IRS-CI)

## Challenges and Friction Points

The 16-month gap between Operation Magnus (Oct 2024) and Minasyan's extradition (Mar 2026) is consistent with typical cyber-defendant extradition timelines, even between treaty partners with mature mutual cooperation. Charging-stage U.S. press releases do not enumerate the specific Dutch police or prosecutor counterparts that handled detention/extradition processing in country — this is a recurring documentation gap in DOJ-side coverage of EU-extradition matters.

## Lessons Learned

1. **Multi-year follow-through is normal**: a successful joint infrastructure disruption creates a probable-cause foundation that supports individual-defendant extraditions 12–24 months downstream; wikis should not treat the infrastructure-takedown phase as the "end" of an operation.
2. **Three-jurisdiction extraditions are increasingly typical for infostealer-as-a-service defendants**: an alleged Armenian developer arrested in the Netherlands and extradited to a U.S. district court (W.D. Tex.) — a routine but operationally complex IC pattern.

## Follow-Up Actions

- Monitor W.D. Tex. docket for trial-stage developments.
- If a Dutch own-domain press release (Politie / OM) or Eurojust update appears that names Dutch officials and the specific extradition pathway used, ingest as a second-source enrichment of this operation page (and bump `source_count`).
- Watch for further co-conspirator indictments / extraditions extending the RedLine prosecution chain.

## Korean Involvement (한국의 참여)

해당하지 않음 — 본 작전에는 한국 사법기관의 참여가 명시된 바 없다.

## Contradictions & Open Questions

- **Open question**: Which specific Dutch agency (Politie cyber unit vs. Openbaar Ministerie / OM cybercrime prosecutor) handled Minasyan's pre-extradition detention and extradition processing? The USAO-WDTX release does not specify. Resolution requires a Netherlands-side own-domain release.
- **Open question**: What was Minasyan's location of arrest within the Netherlands? Not disclosed in the U.S. press release.
- **Open question**: Are there additional RedLine co-conspirators outside Rudometov (Russia-linked, charged 2024) and Minasyan (Armenian, extradited 2026)? Indictment language references "co-developers and administrators" (plural) but does not name them.
