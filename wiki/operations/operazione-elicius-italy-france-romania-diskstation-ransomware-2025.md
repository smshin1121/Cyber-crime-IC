---
type: operation
title: "Operazione ELICIUS — Italy-France-Romania Joint Task Force vs. \"Diskstation\" NAS Ransomware Gang (2024-2025)"
aliases:
  - "Operation Elicius"
  - "Operazione Elicius"
  - "Diskstation ransomware takedown"
  - "Italy-Romania Diskstation gang dismantling"
case_id: "CYB-2025-ELI"
period: 3
operation_type: "joint-investigation"
status: "completed"
enforcement_type:
  - arrest
  - seizure
  - indictment
outcome: "partial"
timeframe:
  announced: 2025-07-14
  start: 2024-06-01
  end: 2025-07-14
  ongoing: false
crime_types:
  - "[[ransomware-ic]]"
  - "[[extortion-ic]]"
crime_type: "ransomware-ic"
target_entity: "\"Diskstation\" ransomware gang (Romanian-nationality OCG, Synology DiskStation NAS exploitation)"
lead_agency: "[[italy-polizia-postale]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[italy]]"
  - "[[france]]"
  - "[[romania]]"
participating_agencies:
  - "[[polizia-di-stato]]"
  - "[[italy-polizia-postale]]"
  - "[[france-national-police]]"
  - "[[romania-police]]"
  - "[[europol-ec3]]"
legal_basis:
  - "[[budapest-convention]]"
mechanisms_used:
  - "[[joint-investigation-team]]"
results:
  arrests: 1
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Multiple Romanian-nationality suspects identified across the criminal chain (count not disclosed in primary source)."
    - "Several persons caught in flagrante delicto during June 2024 Bucharest searches at suspects' residences."
    - "Primary suspect (44-year-old Romanian national) placed in pre-trial custody in prison by GIP Tribunale di Milano."
    - "Charges: art. 615-ter Italian Criminal Code (Accesso abusivo a un sistema informatico o telematico — unauthorised access) and art. 629 (Estorsione — extortion)."
edges:
  - source_actor: "italy-polizia-postale"
    target_actor: "france-national-police"
    cooperation_type: "joint_investigation"
    legal_basis: "Budapest_Convention"
    direction: "undirected"
  - source_actor: "italy-polizia-postale"
    target_actor: "romania-police"
    cooperation_type: "joint_investigation"
    legal_basis: "Budapest_Convention"
    direction: "undirected"
  - source_actor: "europol-ec3"
    target_actor: "italy-polizia-postale"
    cooperation_type: "technical_assistance"
    legal_basis: "bilateral_MOU"
    direction: "directed"
  - source_actor: "italy-polizia-postale"
    target_actor: "romania-police"
    cooperation_type: "evidence_transfer"
    legal_basis: "Budapest_Convention"
    direction: "directed"
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "exact suspect count beyond the lead defendant"
  - "ransom amounts paid / demanded (not disclosed in primary release)"
  - "specific Synology DiskStation CVEs exploited (referenced only by gang moniker)"
  - "victim count (described as 'numerose società' but not enumerated)"
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "[[2025-07-14_polizia-di-stato_operazione-elicius-diskstation-ransomware]]"
created: 2026-05-10
updated: 2026-05-10
---

> [!info] Provisional / single-source page
> This page is published below the preferred 5-source threshold (CLAUDE.md "entity creation threshold") because the underlying tier-1 primary source (Polizia di Stato official press release) provides extensive verifiable detail (named LE partners across three countries, named prosecution office, specific custody actor, specific charge articles, specific search location and date). Additional tier-1 sources from France's police nationale and Romania's poliție will be added as identified. Until then, treat enumerated results as preliminary and check back for tier-1 corroboration.

## Summary

Operazione ELICIUS is a joint Italy-France-Romania police operation against the "Diskstation" ransomware gang, a Romanian-nationality organised criminal group that targeted small and medium-sized Italian enterprises across the Lombardy region with double-extortion ransomware attacks exploiting Synology DiskStation NAS appliances. The operation was led by the Italian [[italy-polizia-postale|Servizio Polizia Postale e per la Sicurezza Cibernetica]] from the Centro Operativo per la Sicurezza Cibernetica (C.O.S.C.) Milano, prosecuted by the [[italy|Procura di Milano]], and coordinated at EU level by [[europol-ec3|Europol]] with [[france-national-police|French national police]] and [[romania-police|Romanian Police]] as foreign LE partners. Searches were executed in June 2024 in Bucharest; the operation became publicly known on 14 July 2025 when the Polizia di Stato published the announcement.

## Background

The investigation began following a wave of complaints filed by companies operating in the Lombardy region (Lombardia, northern Italy) that had had the data on their information systems encrypted, resulting in operational paralysis. Targeted sectors named in the primary source: graphic design, film production, event organisation, and NGOs active internationally in civil-rights protection and charity. To recover their data, victims would have had to pay heavy cryptocurrency ransoms.

The "Diskstation" moniker is the gang's self-attribution and refers to the brand of network-attached storage (NAS) appliances — Synology DiskStation — whose vulnerabilities the gang exploited as initial access vector. (Note: the primary source does not enumerate specific CVEs.)

## Participating Parties

**Italian side:**
- **Lead investigative agency:** [[italy-polizia-postale|Servizio Polizia Postale e per la Sicurezza Cibernetica]] (Postal Police and Cyber Security Service), part of the [[polizia-di-stato|Polizia di Stato]] (Italian State Police)
- **Operations centre:** Centro Operativo per la Sicurezza Cibernetica (C.O.S.C.) di Milano
- **Prosecution authority:** Procura di Milano (Milan Public Prosecutor's Office)
- **Pre-trial custody actor:** Giudice per le Indagini Preliminari (GIP) presso il Tribunale di Milano

**Foreign LE partners (named in tier-1 source):**
- **France:** "polizie nazionali di Francia" — i.e. [[france-national-police|French national police]] (Police Nationale)
- **Romania:** "polizie nazionali di Romania" — i.e. [[romania-police|Romanian Police]] (Poliția Română)

**Coordination:**
- [[europol-ec3|EUROPOL]] — formally established the joint task force.

## Legal Framework

The Italian charges against the principal suspect rest on two articles of the Italian Criminal Code:
- **Art. 615-ter c.p.** — *Accesso abusivo a un sistema informatico o telematico* (unauthorised access to a computer or telecommunications system).
- **Art. 629 c.p.** — *Estorsione* (extortion).

Both offences are within the substantive scope of the [[budapest-convention|Budapest Convention on Cybercrime]] (Articles 2 — illegal access — and 11 / accompanying provisions for extortion-type abuse), of which Italy, France, and Romania are all parties. Cooperation across the three jurisdictions in this operation aligns with the Convention's chapter on international cooperation (Articles 23-35) and its dual-criminality framework.

## Operational Timeline

- **Phase 1 — Italian-only forensic + blockchain analysis (date not disclosed; pre-June 2024).** Procura di Milano coordinated dual-track work: (a) deep forensic analysis of victim companies' attacked information systems; (b) blockchain analysis of cryptocurrency ransom flows. This phase identified the need to extend investigative reach abroad.
- **Phase 2 — Europol-coordinated task force with France and Romania (date not disclosed; pre-June 2024).** The primary source: *"con il coordinamento di EUROPOL ... è stata istituita una task force con le polizie nazionali di Francia e Romania"* — i.e. once Italian leads pointed abroad, Europol shell-coordinated a joint task force with French and Romanian police, who were already independently investigating the same gang.
- **June 2024 — Bucharest searches.** Searches executed at suspects' residences in Bucharest, with operators from C.O.S.C. Milano physically participating. Several persons caught *in flagranza di reato* (in flagrante delicto). Numerous evidentiary elements seized.
- **2024-2025 — judicial phase in Italy.** The Milan GIP, on the conforming request of the prosecuting public ministers, ordered pre-trial detention in prison for the principal suspect — a 44-year-old Romanian national — on charges of unauthorised computer access and extortion against numerous Italian victims.
- **2025-07-14 — public announcement.** Polizia di Stato published the operation summary on its national portal.

## Results and Impact

| Metric | Value |
|---|---|
| Lead-defendant arrests | 1 (44-year-old Romanian national, in pre-trial custody in Italy) |
| Additional suspects identified | "diversi soggetti, tutti di nazionalità rumena" (multiple, exact count not disclosed) |
| Searches | June 2024, Bucharest, multiple residences |
| Charges (lead defendant) | Art. 615-ter c.p. (unauthorised access); art. 629 c.p. (extortion) |
| Servers / cryptocurrency seized | Not disclosed in primary source |
| Decryption keys recovered | Not disclosed in primary source |
| Victims | Italian SMEs across Lombardy; sectors: graphic design, film production, events, civil-rights NGOs |

## Cooperation Mechanisms Used

- **[[joint-investigation-team|Joint task force under Europol coordination]]** — primary source describes a *"task force"* established with Europol coordination. The text does not use the formal Eurojust JIT label, but the structure (Italian, French, and Romanian police investigators jointly working a single criminal target with Europol providing the operational shell) is functionally consistent with that model.
- **Blockchain analysis as cross-border evidentiary technique** — Italian-side blockchain analysis of cryptocurrency ransom flows underpinned the move from domestic investigation to multinational task force.
- **Cross-border evidentiary deployment** — Italian C.O.S.C. operators physically participated in the June 2024 Bucharest searches, providing first-hand technical expertise on victim-side evidence at the time of execution.

## Challenges and Friction Points

The primary release does not enumerate friction points. Inferable challenges (low confidence, derived from operation type rather than explicit source statements):
- Identifying suspects across jurisdictions requires sustained Europol-coordinated information exchange — Italian leads had to be merged with parallel French and Romanian leads on the same gang.
- Custody pathway suggests the principal suspect was either arrested in flagrante during the Bucharest searches (per primary source: *"cogliere alcuni soggetti in flagranza di reato"*) and subsequently surrendered to Italian custody, likely via European Arrest Warrant — the primary source does not explicitly confirm the EAW route.

## Lessons Learned

The primary source does not articulate explicit lessons. The structural takeaway worth recording:
- **Synology DiskStation NAS exploitation as an OCG ransomware vector** — first wiki record of a Europol-coordinated takedown specifically tied to NAS-appliance exploitation (vs. RDP / VPN / phishing initial access). Future Italian / EU records on similar gangs should be cross-linked here.
- **Italian C.O.S.C. (Centro Operativo per la Sicurezza Cibernetica)** as the operational locus for cross-border physical deployment of Italian police investigators — likely-replicable pattern for future Italy-Romania ransomware cases given the well-documented Romanian organised-cybercrime nexus.

## Follow-Up Actions

The primary source explicitly notes that criminal responsibility, in compliance with the presumption of innocence, can only be definitively established by an irrevocable conviction at the conclusion of the trial. Therefore status = `completed` for the investigative-and-arrest phase, but trial outcome is pending and unrecorded.

## Korean Involvement (한국의 참여)

No Korean involvement — neither [[south-korea|Republic of Korea]] LE/prosecution nor Korean victims are mentioned in the primary source. Recorded here for completeness per CLAUDE.md operational rule 12.

## Contradictions & Open Questions

> [!info] Open data points (single-source ingest)
> 1. **Total number of suspects identified.** Primary source: "diversi soggetti, tutti di nazionalità rumena" (several persons, all of Romanian nationality) — exact count not disclosed.
> 2. **Total ransom paid by Italian victims.** Not disclosed.
> 3. **Specific Synology DiskStation CVEs exploited.** The "Diskstation" gang label points to Synology NAS exploitation but no CVE list in primary source.
> 4. **Custody handover mechanism.** Whether the 44-year-old Romanian principal was surrendered to Italy via EAW, by extradition, or after voluntary travel is not disclosed.
> 5. **French national police involvement scope.** French police are named twice in the primary source as task force participant but the source does not detail what specific French investigative actions were undertaken — only that the French police were "anch'esse impegnate nell'individuazione dei responsabili degli attacchi" (also engaged in identifying those responsible for the attacks). Future French-side primary sources should be cross-checked.
> 6. **Eurojust formal JIT vs. ad-hoc Europol task force.** Primary source uses *"task force"*, not *"squadra investigativa comune"* / JIT. Whether a formal Eurojust JIT was opened is unrecorded.
