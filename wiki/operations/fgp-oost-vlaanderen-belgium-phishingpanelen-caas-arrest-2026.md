---
type: operation
title: "FGP East Flanders / Europol — Crime-as-a-Service Phishing-Panel Supplier Arrest (NL→BE Surrender, 2026)"
title_ko: "벨기에 동플랑드르 연방사법경찰·Europol — Crime-as-a-Service 피싱 패널 공급자 검거 (네덜란드→벨기에 인도, 2026)"
aliases:
  - "Belgium phishing panel supplier arrest 2026"
  - "FGP Oost-Vlaanderen phishingpanelen Crime-as-a-Service"
  - "Dendermonde phishing panel CaaS arrest 2026"
case_id: CYB-2026-119
period: 3
operation_type: arrest-sweep
status: ongoing
enforcement_type:
  - arrest
  - search
  - seizure
  - extradition
outcome: partial
timeframe:
  announced: 2026-04-22
  start: 2026-01-26
  end: 2026-04-16
  ongoing: true
crime_types:
  - "[[cybercrime-infrastructure-ic]]"
  - "[[online-fraud-ic]]"
  - "[[bank-fraud-ic]]"
crime_type: "[[cybercrime-infrastructure-ic]]"
target_entity: "Single suspect (20-year-old male, residence in the Netherlands) who built and sold phishing panels to fraud gangs via Telegram and other online channels; panels documented in fraud cases across Belgium, the Netherlands and 'many other European countries' (others not enumerated by the source)."
lead_agency: ""
coordinating_body: ""
participating_countries:
  - "[[belgium]]"
  - "[[netherlands]]"
participating_agencies:
  - "[[belgium-federal-police]]"
  - "[[europol-ec3]]"
legal_basis:
  - "Belgian Code of Criminal Procedure (judicial investigation directed by the investigating judge at Dendermonde)"
  - "European Arrest Warrant framework (Council Framework Decision 2002/584/JHA) — *likely* legal basis for the NL→BE surrender, but the specific instrument is not named in the source"
mechanisms_used:
  - "[[europol-ec3]]"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Multiple data carriers seized during the 26 January 2026 house search in the Netherlands."
    - "Approximately EUR 28 000 in cash seized at the Dutch search location."
    - "Suspect surrendered (overgeleverd) from the Netherlands to Belgium on 16 April 2026."
    - "Suspect remanded in custody (voorlopig aangehouden) by the Dendermonde investigating judge."
edges:
  - source_actor: "Federale Gerechtelijke Politie Oost-Vlaanderen (Belgium)"
    target_actor: "Europol"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: "Belgian judicial authorities"
    target_actor: "Dutch authorities"
    cooperation_type: extradition
    legal_basis: unknown
    direction: directed
credibility_index: 3.0
source_tier: 1
missing_fields:
  - "lead_agency (Federale Gerechtelijke Politie Oost-Vlaanderen has no dedicated wiki page; logged as the FGP regional unit of [[belgium-federal-police]] in body prose)"
  - "coordinating_body (none named beyond Europol; investigation was nationally led by the Dendermonde investigating judge)"
  - "Dutch executing agency name (likely [[netherlands-politie]] but not explicitly named)"
  - "Specific articles of Belgian criminal law charged"
  - "Full enumerated list of other European countries where panels were used"
related_cases: []
related_operations:
  - "[[tycoon-2fa-phishing-as-a-service-takedown-2026]]"
  - "[[w3ll-phishing-kit-takedown-2026]]"
  - "[[gxc-team-googlexcoder-phishing-kits-takedown-2025]]"
  - "[[operacion-kaerb-iserver-phishing-as-a-service-takedown-2024]]"
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "[[2026-04-22_police-be_phishingpanelen-leverancier-arrest]]"
created: 2026-05-10
updated: 2026-05-10
---

> [!info] Provisional / sparse-source page
> This page is built from a single tier-1 primary source: the 22 April 2026 Police.be press release. Many operational details (precise charges, full list of victim-states, executing Dutch agency, specific surrender instrument) are not stated in the source and are flagged below as such. The page should be re-evaluated as additional primary sources (Belgian prosecutor releases, Europol press release if any, court documents, or follow-up Dutch [[netherlands-politie|Politie]] communications) become available.

## Summary

On **22 April 2026** the Belgian Federal Judicial Police of East Flanders (Federale Gerechtelijke Politie Oost-Vlaanderen, FGP Oost-Vlaanderen — a regional judicial division of [[belgium-federal-police|the Belgian Federal Police]]) announced the arrest of a 20-year-old suspect for supplying *phishingpanelen* (phishing panels) — Crime-as-a-Service infrastructure used by fraud gangs to run convincing fake-bank, fake-telecom and fake-identity-app campaigns. The Belgian investigation was directed by the Dendermonde investigating judge with the East Flanders Public Prosecutor's Office (parket van Oost-Vlaanderen) and conducted "in nauwe samenwerking met Europol" (in close cooperation with [[europol-ec3|Europol]]). The suspect was arrested in the Netherlands following a **26 January 2026** house search, and **surrendered to Belgium on 16 April 2026** where he was remanded in custody.

The press release reports panels appearing in "multiple ongoing investigations across several European countries" and confirms documented use in fraud against victims in Belgium, the Netherlands and "many other European countries"; no further countries are enumerated by the source.

## Background

The supplier-level disruption fits a 2025-2026 pattern of European law enforcement targeting the upstream Crime-as-a-Service (CaaS) layer of phishing rather than only the downstream fraud crews — see [[tycoon-2fa-phishing-as-a-service-takedown-2026]], [[w3ll-phishing-kit-takedown-2026]] and [[gxc-team-googlexcoder-phishing-kits-takedown-2025]]. A *phishingpaneel* in this context is a back-end management interface that lets a buyer operate fake websites and craft convincing email/SMS lures impersonating banks, telecom operators, payment platforms or identity-verification apps; it intercepts victim credentials, codes and bank data for downstream fraud. The Belgian press release describes the suspect's distribution channel as "various online channels, including Telegram" and the proceeds as "primarily collected through virtual-currency payments."

## Participating Parties

**Countries (named in the source):**
- [[belgium|Belgium]] — investigation jurisdiction; suspect remanded by the Dendermonde investigating judge.
- [[netherlands|Netherlands]] — locus of the suspect's residence and the 26 January 2026 house search; the country from which the suspect was surrendered.

**Agencies (named in the source):**
- Federale Gerechtelijke Politie Oost-Vlaanderen (FGP Oost-Vlaanderen) — Federal Judicial Police, East Flanders division, the lead investigating police service. It is a regional judicial unit of [[belgium-federal-police|the Belgian Federal Police]]; no standalone wiki page exists for the East Flanders division so it is recorded here in prose.
- Parket van Oost-Vlaanderen (East Flanders Public Prosecutor's Office) — judicial direction of the investigation. Not a current wiki entity.
- [[europol-ec3|Europol]] — explicitly named as a cooperating partner ("in samenwerking met Europol", "in nauwe samenwerking met Europol").
- The Dutch executing agency for the 26 January 2026 house search and arrest is **not explicitly named** in the source. It is *likely* [[netherlands-politie|Politie Nederland]], but this is not stated.

## Legal Framework

- The Belgian investigation was conducted under Belgian criminal procedure, directed by the **onderzoeksrechter te Dendermonde** (investigating judge at Dendermonde) in cooperation with the East Flanders Public Prosecutor's Office. Specific articles of the Belgian Criminal Code or Code of Criminal Procedure that ground the suspect's charges are **not stated in the source**.
- The NL→BE surrender on 16 April 2026 is *almost certainly* an exercise of the [[european-arrest-warrant|European Arrest Warrant]] framework (Council Framework Decision 2002/584/JHA of 13 June 2002 on the European arrest warrant and the surrender procedures between Member States), which is the standard inter-EU instrument for such surrenders. The press release uses the term "overgeleverd" (surrendered), which is the EAW terminology. However, the specific instrument is **not named in the source**.

## Operational Timeline

| Date | Event |
|---|---|
| 2026-01-26 | House search executed in the Netherlands at the 20-year-old suspect's address; multiple data carriers and approximately EUR 28 000 in cash seized. Arrest follows. |
| 2026-04-16 | Suspect surrendered ("overgeleverd") from the Netherlands to Belgium. Remanded in custody (voorlopig aangehouden) by the Dendermonde investigating judge. |
| 2026-04-22 | Press release published by Police.be. |

## Results and Impact

- **1 arrest** of the supplier of phishing panels.
- Seizures: multiple data carriers; approximately **EUR 28 000 in cash**.
- The press release does not quantify the total number of victims, total fraud loss, or number of downstream gang customers identified.
- Likely follow-on impact: investigators in other EU countries can match seized data carriers against ongoing national phishing investigations. The press release frames the panels as appearing in "multiple ongoing investigations across various European countries", which *likely* enables further downstream prosecutions, although no specific spin-off case is announced.

## Cooperation Mechanisms Used

- **Europol coordination** — explicitly named twice in the press release as the cross-border cooperation partner for the Belgian investigation. The role appears to be analytical/coordination support across the multiple national phishing investigations into which the suspect's panels surfaced; no specific Europol product (e.g. an EMPACT operational action day, an OTF/J-CAT joint task force, or an Operational Task Force) is named in the source.
- **NL→BE surrender** — *likely* under the [[european-arrest-warrant|European Arrest Warrant]] framework, although the specific instrument is not named.
- The press release does **not** mention [[eurojust|Eurojust]], a Joint Investigation Team, or formal MLA requests. Their absence in the source is not evidence they were not used; it simply means the source does not assert it.

## Challenges and Friction Points

Not specifically discussed in the source. *Likely* challenges, by inference from comparable phishing-kit cases (e.g. [[tycoon-2fa-phishing-as-a-service-takedown-2026]], [[gxc-team-googlexcoder-phishing-kits-takedown-2025]]), include:
- Attribution of individual fraud incidents to the supplier rather than to the downstream gangs that bought the panels.
- Tracing virtual-currency proceeds back to the supplier (the press release notes proceeds were "primarily collected through virtual-currency payments" but does not state that any cryptocurrency was seized).
- Multi-jurisdiction victim identification across "many" unenumerated European countries.

These are inferred, not asserted in the source.

## Lessons Learned

Not stated in the source.

## Follow-Up Actions

- Belgian judicial proceedings continue: the suspect is remanded "in het belang van het verdere onderzoek" (in the interest of further investigation) — i.e. the investigation phase is *ongoing* as of 22 April 2026.
- The press release closes with public-awareness guidance for citizens, including reporting suspicious messages to verdacht@safeonweb.be (Belgium's national reporting channel).

## Korean Involvement (한국의 참여)

No Korean involvement is reported in the source. Not applicable to this operation as published.

## Contradictions & Open Questions

- **Other European countries**: The source repeatedly references "various European countries" and "many other European countries" but does not enumerate them. *Almost certainly* additional EU member states are involved as victim or downstream-investigation jurisdictions, but until tier-1 sources name them, no further `participating_countries` entries should be added.
- **Dutch executing agency**: The 26 January 2026 house search and initial arrest in the Netherlands necessarily involved a Dutch executing authority. The source does not name it. *Likely* [[netherlands-politie|Politie]] (national police) acting on a Belgian European Arrest Warrant, but this is not asserted by the source.
- **Specific charges**: Belgian Criminal Code articles under which the suspect was charged are not stated in the source.
- **Surrender instrument**: Not explicitly named (see Legal Framework). Recording as "*likely* EAW" pending confirmation.
- **Case ID note**: Assigned `CYB-2026-119` (next free 3-digit slot in the 2026 series at time of ingest, 2026-05-10).
