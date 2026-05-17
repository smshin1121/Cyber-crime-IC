---
type: operation
title: "Crimenetwork Relaunch Takedown (May 2026)"
aliases:
  - "Crimenetwork 2.0 takedown"
  - "Crimenetwork Neuauflage"
  - BustedAgainCrime.network
case_id: CYB-2026-266
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - seizure
  - takedown
  - asset_freeze
outcome: success
timeframe:
  announced: 2026-05-08
  start: 2026-05-06
  end: 2026-05-06
  ongoing: false
crime_types:
  - "[[dark-web-ic]]"
  - "[[cybercrime-forum-ic]]"
  - "[[drug-trafficking]]"
  - "[[online-fraud-ic]]"
  - "[[counterfeit-goods]]"
crime_type: dark-web-ic
target_entity: "Crimenetwork (relaunched darknet marketplace)"
lead_agency: "[[germany-bka]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[germany]]"
  - "[[spain]]"
  - "[[moldova]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[zit-frankfurt]]"
  - "[[spain-national-police]]"
  - "[[eurojust]]"
legal_basis:
  - "[[european-arrest-warrant]]"
mechanisms_used:
  - "[[european-arrest-warrant]]"
  - "[[eurojust-coordination-meeting]]"
  - "[[domain-seizure]]"
  - "[[cryptocurrency-seizure]]"
  - "[[marketplace-admin-liability]]"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 1
  cryptocurrency_seized: "EUR 194,000 in assets directly linked to Crimenetwork (Bitcoin, Litecoin, Monero ecosystem)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Platform takedown (relaunched 'Crimenetwork' shut down)"
    - "22,000+ user accounts secured for investigation"
    - "100+ vendor accounts documented"
    - "EUR 3.6 million+ documented platform turnover"
    - "Extensive user and transaction datasets obtained"
    - "Seizure banner deployed; bustedagaincrime.network notification site published"
edges:
  - source_actor: germany-bka
    target_actor: spain-national-police
    cooperation_type: joint_investigation
    legal_basis: European_Arrest_Warrant
    direction: directed
  - source_actor: germany-bka
    target_actor: moldova-cybercrime-centre
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: undirected
  - source_actor: zit-frankfurt
    target_actor: eurojust
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: zit-frankfurt
    target_actor: germany-bka
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - case_id
  - indictments
  - servers_seized
  - victims_notified
related_cases:
  []
related_operations:
  []
challenges_encountered:
  []
lessons_learned:
  - "Successor platforms can re-emerge within days after a takedown; sustained monitoring of the 'underground economy' ecosystem is required to detect and disrupt relaunches."
  - "European Arrest Warrant + host-state special police unit remains an effective pathway when a German-language marketplace operator is physically located in another EU member state."
  - "Inclusion of a non-EU partner (Moldova) suggests technical infrastructure spread beyond the EU; Eurojust coordination still scales to mixed EU/non-EU IC."
source_count: 2
sources:
  - "[[2026-05-08_bka_crimenetwork-relaunch-takedown-spain-arrest]]"
  - "[[2026-05-12_politia-md_crimenetwork-darknet-takedown-ini-pccocs-moldova]]"
created: 2026-05-09
updated: 2026-05-17
---
> [!info] Provisional page — below preferred publication threshold
> This page is built from two tier-1 primary sources: the **BKA / ZIT joint press release** of 8 May 2026 and the **Poliția Republicii Moldova (politia.md / INI–PCCOCS) press release** of 12 May 2026. It is still below the preferred publication threshold of `source_count >= 5` and should be enriched as additional tier-1 sources (Eurojust press release, Spanish National Police statement, court filings) are ingested.

## Summary

On Wednesday **6 May 2026**, the German Federal Criminal Police Office ([[germany-bka|BKA]]) and the Frankfurt am Main General Public Prosecutor's Office – Central Office for Combating Internet Crime ([[zit-frankfurt|ZIT]]) — together with the [[spain-national-police|Spanish Policía Nacional]], the Moldovan *Inspectoratul Național de Investigații – Centrul pentru Combaterea Crimelor Cibernetice*, and [[eurojust|Eurojust]] — shut down the relaunched version of the German-language darknet trading platform **"Crimenetwork"**. The platform's alleged 35-year-old German operator was arrested on Mallorca on the basis of a [[european-arrest-warrant|European Arrest Warrant]] (*Europäischer Haftbefehl*) executed by a special unit of the Spanish National Police. The action was announced publicly on **8 May 2026**.

The case is the second takedown of the same platform name within roughly seventeen months: the original Crimenetwork was dismantled in December 2024 and its prior administrator was sentenced by the Landgericht Gießen in March 2026 to 7 years 10 months in prison with a confiscation order of more than €10 million (judgment not yet final at the time of this publication).

## Background

"Crimenetwork" was, prior to its end-2024 takedown, one of the central marketplaces of the German-speaking *Underground Economy* — a long-running listing/escrow platform offering stolen data, narcotics, and forged documents. According to the BKA/ZIT release, within only a few days of the December 2024 takedown and the arrest of the then-administrator, the present suspect is alleged to have stood up an entirely new technical infrastructure under the same brand and run it as the relaunched "Crimenetwork".

By the time of the May 2026 action the relaunched platform reportedly had:

- **22,000+** registered users
- **100+** vendor accounts
- **€3.6 million+** documented turnover
- Customer base concentrated in the **German-speaking region** (DACH)

Transactions were settled in **Bitcoin**, **Litecoin**, and **Monero**. The operator collected commissions on completed sales, and vendors paid recurring monthly fees for advertising and selling licences.

## Participating Parties

| Party | Role | Country |
|---|---|---|
| [[germany-bka]] (BKA, Cybercrime division under Director Carsten Meywirth) | Lead investigative agency | Germany |
| [[zit-frankfurt]] (ZIT, GenStA Frankfurt am Main) | Lead prosecutor / coordinating judicial authority | Germany |
| Generalstaatsanwaltschaft Karlsruhe – Cybercrime-Zentrum Baden-Württemberg | Parallel domestic proceeding (commercial fraud) | Germany |
| Polizeipräsidium Offenburg | Parallel domestic action | Germany |
| Polizeipräsidium Reutlingen | Parallel domestic action | Germany |
| [[spain-national-police]] (Policía Nacional, special unit) | Executed the arrest on Mallorca | Spain |
| Inspectoratul Național de Investigații (INI) – Centrul pentru Combaterea Crimelor Cibernetice | Cyber LE participant in Joint Investigation Group (per politia.md 12 May 2026); platform infrastructure was hosted on a Moldovan company's servers | Moldova |
| Procuratura pentru Combaterea Criminalității Organizate și Cauze Speciale (PCCOCS) | Lead Moldovan prosecutor (per politia.md 12 May 2026) | Moldova |
| [[eurojust]] | Judicial coordination support | EU |

> [!note] Stub note
> The Moldovan Centrul pentru Combaterea Crimelor Cibernetice does not yet have a wiki page. It is referenced in prose only and is not listed as a wikilink to avoid orphan link creation; a stub should be created on a future ingest pass.

## Legal Framework

- **European Arrest Warrant** (*Europäischer Haftbefehl*) — basis for the cross-border arrest and surrender between Germany (issuing) and Spain (executing). See [[european-arrest-warrant]].
- **§ 127 StGB** (Strafgesetzbuch) — operating criminal online trading platforms (a relatively new German offence created specifically to cover darknet marketplace administration).
- **§§ 29a, 30a BtMG** (Betäubungsmittelgesetz) — trafficking in narcotic drugs in non-minor quantities.
- **Gewerbsmäßiger Betrug** (commercial fraud) — separate prosecution led by the Generalstaatsanwaltschaft Karlsruhe.

## Operational Timeline

| Date | Event |
|---|---|
| December 2024 | Original "Crimenetwork" platform taken down; previous administrator arrested. |
| Late December 2024 | According to the BKA/ZIT release, the present suspect allegedly begins building the relaunched platform within days of the takedown. |
| March 2026 | Landgericht Gießen sentences the previous Crimenetwork administrator to 7 years 10 months and orders confiscation of over €10 million in proceeds (not yet legally final). |
| **6 May 2026 (Wed.)** | International coordinated action: relaunched "Crimenetwork" infrastructure shut down; suspect arrested on Mallorca on a European Arrest Warrant. |
| 8 May 2026 | BKA/ZIT joint press release published. |

## Results and Impact

- **Arrests:** 1 (35-year-old German national, on Mallorca, Spain).
- **Platform takedown:** Relaunched "Crimenetwork" infrastructure abgeschaltet; seizure banner served to former users.
- **User notification:** A dedicated notification site, `bustedagaincrime.network`, was published as the law enforcement landing page for former users — a deliberate naming reference to the prior ("BustedCrime") takedown.
- **Asset seizure:** Approximately **€194,000** in assets directly tied to the platform was provisionally secured.
- **Data:** Extensive user and transaction datasets were obtained and are expected to seed downstream investigations into the platform's vendors and customers (predominantly German-speaking).

## Cooperation Mechanisms Used

- **[[european-arrest-warrant|European Arrest Warrant (EAW)]]** — primary instrument enabling the Mallorca arrest.
- **[[eurojust-coordination-meeting|Eurojust coordination]]** — judicial coordination of the multi-jurisdictional action; cited explicitly in the BKA/ZIT release.
- **Bilateral cybercrime cooperation Germany–Moldova** — Moldovan CCCC participation suggests use of informal/bilateral cybercrime cooperation with a non-EU partner whose jurisdiction was relevant to the platform's technical infrastructure.
- **[[domain-seizure]]** — public seizure banner deployed at the platform's web addresses.
- **[[cryptocurrency-seizure]]** — provisional securing of crypto-denominated assets connected to the platform's commission flows.
- **[[marketplace-admin-liability]]** — substantive criminal liability under the German § 127 StGB regime for operating a criminal online marketplace.

## Challenges and Friction Points

- **Rapid relaunch problem:** The BKA/ZIT release explicitly notes that the new infrastructure was stood up "within days" of the December 2024 takedown. This compresses the window between disruption and re-emergence and stresses the IC model that traditionally follows a single-takedown narrative.
- **Cross-border physical residence:** The operator was a German national living abroad in another Schengen state — without the EAW + a host-state special unit available, an arrest of this profile would otherwise depend on slower extradition procedures.
- **Mixed EU / non-EU partnership:** Moldovan participation hints that technical infrastructure (or supporting actors) reached beyond the EU. Coordinating an EU-internal EAW arrest with a non-EU technical partner adds judicial-cooperation complexity that was absorbed by Eurojust here.

## Lessons Learned

- **Continuity monitoring** of brand-revival darknet platforms should be standard after any high-profile takedown.
- **The EAW remains the workhorse instrument** for in-EU arrests of German-speaking marketplace operators; a special police unit for the actual execution is decisive given operational security risks.
- **Joint EU/non-EU operational coordination via Eurojust** is feasible even when one of the partners (Moldova) sits outside EU jurisdiction.

## Follow-Up Actions

- Pending: criminal trial of the arrested suspect in Germany on charges under § 127 StGB and §§ 29a, 30a BtMG, in addition to the parallel commercial-fraud proceeding led by the Generalstaatsanwaltschaft Karlsruhe.
- Pending: investigative exploitation of the seized user and transaction datasets.
- Pending: confirmation/finalization of the Landgericht Gießen judgment against the predecessor administrator.

## Korean Involvement (한국의 참여)

According to the BKA/ZIT primary source, *no Korean agencies, suspects, or victims are named*. Likely confidence: **highly likely** that this case has no direct ROK nexus, given the platform's German-speaking user base and DACH-region customer profile; this can be revised if further sources indicate otherwise.

## Contradictions & Open Questions

- **Action date vs. announcement date:** The release dates the operative action to "Mittwoch" (Wednesday), which corresponds to 6 May 2026; the press release itself is dated 8 May 2026. Frontmatter records both `start: 2026-05-06` and `announced: 2026-05-08` accordingly.
- **Server count:** The release does not enumerate the number of servers seized; only the platform shutdown and the seizure banner are described. `servers_seized: 0` here means *not stated*, not *zero*.
- **Indictment status:** The release announces an arrest on a European Arrest Warrant and refers to the Karlsruhe parallel proceeding; it does not state that a German indictment (Anklageschrift) has yet been filed against the present suspect. `indictments: 0` therefore reflects current state-of-record, not a final outcome.
- **Moldovan unit name:** The release names the Moldovan partner as *Inspectoratul Național de Investigații – Centrul pentru Combaterea Crimelor Cibernetice*. No wiki page exists yet for this unit; a future stub or organization page should clarify whether it is the same as / parent of / subordinate to the Moldovan IGP cybercrime structures already referenced elsewhere.
