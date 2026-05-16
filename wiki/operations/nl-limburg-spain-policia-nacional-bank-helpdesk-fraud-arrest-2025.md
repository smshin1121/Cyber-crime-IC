---
type: operation
title: "NL-ES Bank-Helpdesk Fraud Arrest in Estepona — Politie Limburg + Policia Nacional UDYCO Greco (April 2025)"
title_ko: "네덜란드-스페인 은행 헬프데스크 사기 용의자 에스테포나 검거 (림뷔르흐 사이버범죄팀 + 스페인 국가경찰 UDYCO 그레코, 2025년 4월)"
aliases:
  - "Limburg Estepona helpdesk-fraud arrest"
  - "NL-Spain Postcode Loterij impersonation cybercrime arrest 2025"
  - "Politie Limburg UDYCO Greco Costa del Sol cyberzaak"
case_id: CYB-2025-999
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - search
outcome: partial
timeframe:
  announced: 2025-04-29
  start: 2024-09
  end: 2025-04-29
  ongoing: true
crime_types:
  - "[[online-fraud-ic]]"
  - "[[bank-fraud-ic]]"
crime_type: "[[online-fraud-ic]]"
target_entity: "Dutch-orchestrated telephone bank-helpdesk fraud cell impersonating Nationale Postcode Loterij, abusing AnyDesk-style remote-access tools to seize victims' online banking sessions"
lead_agency: ""
coordinating_body: ""
participating_countries:
  - "[[netherlands]]"
  - "[[spain]]"
participating_agencies:
  - "[[netherlands-politie]]"
  - "[[spain-national-police]]"
legal_basis:
  - "[[mlat-process]]"
mechanisms_used:
  - "[[mlat-process]]"
  - "[[informal-cooperation]]"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "House searches at two co-suspect addresses in Borne and Deurningen (NL); multiple phones and laptops seized for forensic examination."
    - "Post-arrest residence search in Estepona (ES); phones and laptops seized."
edges:
  - source_actor: "Politie Limburg Team Cybercrime"
    target_actor: "Spanish Policia Nacional UDYCO Greco Costa del Sol"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: directed
credibility_index: 4.2
source_tier: 1
missing_fields:
  - "exact damage amount"
  - "total number of victims"
  - "extradition pathway and timing"
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "Costa del Sol (Spain) continues to function as an operating-from-abroad base for Dutch cyber-fraud suspects; Spanish UDYCO Greco is a recurrent specialised counterparty unit for Dutch cybercrime arrests."
source_count: 1
sources:
  - "[[2025-04-29_politie-nl_spaanse-aanhouding-limburgse-cyberzaak]]"
created: 2026-05-16
updated: 2026-05-16
---

> [!info] Provisional ingest
> Single tier-1 source (Politie NL press release, 2025-04-29). Below the 5-source publication threshold; retained as provisional documentation pending corroboration from the Spanish Policia Nacional and/or Openbaar Ministerie Parket Limburg.

## Summary

On 29 April 2025, the Spanish **Policia Nacional** unit **UDYCO Greco Costa del Sol** arrested a 33-year-old man without fixed residence in **Estepona, Spain**, on a request from the Dutch police. The suspect was linked by **Team Cybercrime Limburg** (Politie, Netherlands), under leadership of the **Openbaar Ministerie Parket Limburg**, to a telephone bank-helpdesk fraud scheme impersonating the Dutch **Nationale Postcode Loterij**. On the same day, Dutch officers from Eenheid Oost-Nederland conducted coordinated house searches at two co-suspect addresses in **Borne** and **Deurningen** (NL); phones and laptops were seized for forensic examination but no arrests followed at those sites.

Confidence in the IC characterisation: **almost certainly** an executed NL-ES bilateral cooperation case, given that the arrest is described in the Dutch national police's own press release as having been carried out by the Spanish Policia Nacional UDYCO Greco unit (single tier-1 source, primary attribution).

## Background

The Dutch investigation opened in **September 2024** after a victim reported being defrauded of hundreds of euros via a fake-lottery "overpayment refund" scheme. The fraud pattern, as described in the tier-1 source:

1. Cold-call to victim with a fake lottery-win notification.
2. Follow-up call claiming the prize was "overpaid" or that tax must be remitted.
3. Victim is directed to click a (deliberately broken) link; the caller "helpfully" walks them through installing **AnyDesk** or an equivalent remote-administration tool.
4. With remote access, the fraudster opens the victim's online banking, renames the savings account to the lottery's name, and triggers a transfer to a third-party account framed as a "refund."

Multiple victims are confirmed, but Politie Limburg has not yet released a damage total or victim count.

## Participating Parties

- **[[netherlands]]** — Politie ([[netherlands-politie]]) — Team Cybercrime Limburg + Eenheid Oost-Nederland; Openbaar Ministerie Parket Limburg (lead prosecutor)
- **[[spain]]** — [[spain-national-police|Policia Nacional]] — UDYCO Greco Costa del Sol (specialised organised-crime/drug crime unit handling transnational fraud arrests on the Costa del Sol)

## Legal Framework

The tier-1 press release does not specify the legal instrument used. Given the EU-EU context, this was **likely** (55-80%) a European Arrest Warrant or direct police-to-police channel with judicial backing via the Dutch parket and the corresponding Spanish judicial authority. [[mlat-process]] is recorded as a placeholder; the precise instrument is `missing_fields`.

## Operational Timeline

- **2024-09** — Dutch investigation opens after victim report (Politie Limburg under OM Parket Limburg leadership).
- **2024-09 to 2025-04** — Dutch-side intelligence development; suspect localised to Spain.
- **2025-04-29 morning** — Coordinated action day:
  - Arrest in Estepona (ES) by Policia Nacional UDYCO Greco Costa del Sol; follow-up residence search; phones/laptops seized.
  - House searches in Borne and Deurningen (NL) at two co-suspect addresses; phones/laptops seized; no NL-side arrests at those addresses on the day.

## Results and Impact

- 1 arrest (Estepona, Spain)
- Phones and laptops seized at 3 sites (1 ES + 2 NL)
- Investigation ongoing; Politie Limburg has explicitly stated the full case scope is not yet known.

## Cooperation Mechanisms Used

- Bilateral NL-ES law-enforcement cooperation, with the Spanish Policia Nacional acting on Dutch request.
- Synchronisation of action day across two jurisdictions (Spain arrest + NL searches same morning).
- [[informal-cooperation]] channel (police-to-police, specialised unit-to-unit) used in addition to whatever judicial instrument backed the arrest.

## Challenges and Friction Points

Suspect had **no fixed residence** (geen vaste woon- of verblijfplaats) — typical Costa del Sol cyber-fraud operating profile, which complicates pre-arrest surveillance and post-arrest extradition planning.

## Lessons Learned

- Costa del Sol (Estepona/Marbella corridor) remains a recurrent operating base for Dutch-orchestrated cyber-fraud; the Spanish UDYCO Greco specialised unit is a known and effective counterparty for Dutch cybercrime arrests.
- AnyDesk-mediated takeover of victims' online banking continues to be a productive attack vector against Dutch lottery-fraud victims — supports the broader [[bank-fraud-ic]] / remote-access-tool-abuse pattern.

## Korean Involvement (한국의 참여)

None. The case has no Korean nexus per the tier-1 source.

## Contradictions & Open Questions

- Exact legal instrument (EAW vs. spontaneous Spanish judicial cooperation) not specified.
- Extradition/transfer pathway from Spain back to the Netherlands not addressed in the press release.
- Total victim count and aggregate damage figure not yet released; the case is open and updated figures should be ingested when published.
