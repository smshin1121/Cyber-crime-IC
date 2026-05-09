---
type: operation
title: "VerifTools Fake-ID Marketplace - Follow-up User Arrests (Netherlands, April 2026)"
aliases:
  - "VerifTools follow-up arrests"
  - "Politie VerifTools 2026 arrests"
  - "Operation VerifTools (NL user-side)"
case_id: "CYB-2026-NL-VERIFTOOLS"
period: 3
operation_type: arrest-sweep
status: ongoing
enforcement_type:
  - arrest
  - seizure
outcome: partial
timeframe:
  announced: 2026-04-09
  start: 2026-04-07
  end: 2026-04-08
  ongoing: true
crime_types:
  - "[[identity-theft|Identity Theft]]"
  - "[[online-fraud-ic|Online Fraud (IC)]]"
  - "[[cybercrime-infrastructure-ic|Cybercrime Infrastructure (IC)]]"
crime_type: "[[identity-theft|Identity Theft]]"
target_entity: "Identified users of the VerifTools fake-ID marketplace seized on 27 Aug 2025"
lead_agency: "[[netherlands-politie|Politie (Netherlands National Police)]]"
coordinating_body: "[[netherlands-politie|Politie - Team Cybercrime Rotterdam]]"
participating_countries:
  - "[[netherlands|Netherlands]]"
  - "[[united-states|United States]]"
participating_agencies:
  - "[[netherlands-politie|Politie - Team Cybercrime Rotterdam]]"
  - "[[netherlands-om|Openbaar Ministerie (Dutch Public Prosecution Service)]]"
  - "[[fbi|Federal Bureau of Investigation]]"
legal_basis: []
mechanisms_used:
  - "[[informal-cooperation|Informal Police-to-Police Cooperation]]"
  - "[[domain-seizure|Domain and Infrastructure Seizure]]"
  - "[[electronic-evidence|Cross-Border Electronic Evidence]]"
results:
  arrests: 8
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "amount undisclosed; cash and crypto seized during searches on 7-8 Apr 2026"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "9 additional suspects formally summoned for police questioning (ontboden), incl. 2 minors who received stop-talks (stopgesprekken)"
    - "Smartphones, laptops and weapons (or weapon-like objects) seized during nationwide searches"
    - "915,655 fake-ID images and 636,847 user accounts identified from servers seized in Aug 2025"
    - "5,169 fake Dutch documents (passports, driving licences, residence permits) catalogued"
    - "236,002 fake US documents catalogued; USD 1,468,836.98 in US-document purchases identified (Jul 2024 - Aug 2025)"
    - "Estimated EUR 3+ million revenue in VerifTools' last year of operation"
edges:
  - source_actor: "Politie - Team Cybercrime Rotterdam"
    target_actor: "FBI"
    cooperation_type: "joint_investigation"
    legal_basis: "informal"
    direction: "undirected"
  - source_actor: "Politie - Team Cybercrime Rotterdam"
    target_actor: "Openbaar Ministerie"
    cooperation_type: "joint_investigation"
    legal_basis: "bilateral_MOU"
    direction: "undirected"
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "specific MLAT instruments invoked (not disclosed in press release)"
  - "exact crypto and cash amounts seized 7-8 Apr 2026"
  - "identities of arrested suspects (withheld per Dutch privacy practice)"
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "[[2026-04-09_politie_veriftools-identity-fraud-arrests]]"
created: 2026-05-09
updated: 2026-05-09
---

> [!info] Provisional / single-source page
> This page is published below the preferred `source_count >= 5` threshold because the underlying operation is ongoing and only the Dutch national police primary source has been ingested in this pass. Additional FBI/DOJ and Dutch follow-on releases should be merged here as they are ingested rather than spawning sibling pages.

## Summary

On 7-8 April 2026 the Netherlands National Police (Politie), led by Team Cybercrime Rotterdam together with the AVIM unit and coordinated with the Openbaar Ministerie, executed the first nationwide wave of user-side enforcement actions stemming from the joint Netherlands-US takedown of the VerifTools fake-ID marketplace. Eight men aged 20-34 were arrested on suspicion of identity fraud (identiteitsfraude), forgery (valsheid in geschrifte) and cybercrime-related offences; nine further suspects (including two minors) were summoned for questioning. Smartphones, laptops, cash, cryptocurrency and weapons-like objects were seized during searches. The arrests are explicitly framed as the first of multiple expected waves.

The underlying infrastructure takedown took place on 27 August 2025, when the Politie - in cooperation with the US Federal Bureau of Investigation (FBI) - took the VerifTools website offline and seized its servers. Data extracted from those servers (636,847 user accounts; 915,655 generated fake-ID images; documented purchases of 236,002 US-format IDs for USD 1.47 million) is what enabled the April 2026 user-identification round.

## Background

VerifTools was an online marketplace that generated images of forged identification documents on demand. Users uploaded a passport-style photo, entered fabricated biographical data, paid (often in cryptocurrency), and received an image suitable for bypassing image-only Know-Your-Customer (KYC) verification at banks, exchanges and other regulated services. The Dutch police characterise VerifTools as one of the largest providers of its kind, with an estimated EUR 3+ million revenue in its final year of operation.

According to data extracted from the seized servers:

- 636,847 user accounts existed on the platform between February 2021 and August 2025.
- 915,655 fake-ID images were generated between May 2023 and August 2025.
- 5,169 fake Dutch documents - passports, driving licences and residence permits - were produced.
- 236,002 fake US documents were produced; users paid USD 1,468,836.98 for them between July 2024 and August 2025.
- Some "grootgebruikers" (heavy users) generated hundreds or thousands of documents apiece.

## Participating Parties

| Country | Authority | Role |
|---|---|---|
| Netherlands | [[netherlands-politie\|Politie - Team Cybercrime Rotterdam]] | Lead investigator; server seizure (Aug 2025); user-side arrests (Apr 2026) |
| Netherlands | Politie - AVIM (Vreemdelingenpolitie, Identificatie en Mensenhandel), Rotterdam | Identity-fraud and document-fraud expertise; led by Frank van den Heuvel |
| Netherlands | [[netherlands-om\|Openbaar Ministerie]] | Charging-strategy decisions per case (prosecution / summons / stop-talk) |
| United States | [[fbi\|Federal Bureau of Investigation]] | Joint partner in the 27 Aug 2025 website takedown and server seizure |

Named spokespeople in the press release: Ruben van Well (Team Cybercrime Rotterdam) and Frank van den Heuvel (chef AVIM Rotterdam).

## Legal Framework

> [!warning] Legal status check needed
> The Politie press release does not enumerate the specific bilateral or multilateral legal instruments invoked. Identifying the exact MLA channels (e.g., [[budapest-convention|Budapest Convention]] Article 35 24/7 contact-point use, US-NL MLAT, EU-US Agreement on Mutual Legal Assistance, or informal police-to-police channels) requires ingesting the corresponding US-side primary source.

What is established from this source:

- The 27 Aug 2025 takedown of VerifTools was a joint Politie-FBI operation; the FBI's involvement is explicitly named.
- The Dutch charges are framed under domestic Dutch criminal law: identiteitsfraude, valsheid in geschrifte (forgery, max. 6 years), and "cybercrime gerelateerde strafbare feiten."
- Charging-strategy choices (prosecution vs. summons vs. stop-talk) were made in consultation with the Openbaar Ministerie.

## Operational Timeline

- **27 August 2025** - Joint Politie-FBI action takes the VerifTools website offline; servers seized.
- **September 2025 - March 2026** - Dutch police analyse server data, identify users and quantify Dutch- and US-document fraud volumes.
- **7-8 April 2026** - Nationwide first wave of user-side enforcement actions: 8 arrests, 9 summonses, searches in multiple locations.
- **9 April 2026** - Politie publishes press release announcing the wave; release last modified 22 April 2026.
- **Ongoing** - Politie states that further arrest waves will follow as the suspect list grows.

## Results and Impact

| Metric | Value |
|---|---|
| Arrests (NL, 7-8 Apr 2026) | 8 men, age 20-34 |
| Summons / questioning orders | 9 (7 men 18-35, 2 girls 15-16) |
| Stop-talks (minors) | 2 |
| Searches | Nationwide (specific count not disclosed) |
| Items seized | Phones, laptops, weapons-like objects, cash, cryptocurrency |
| Platform user accounts identified | 636,847 |
| Fake-ID images generated and catalogued | 915,655 |
| Estimated VerifTools revenue (last year) | EUR 3+ million |
| Fake Dutch documents catalogued | 5,169 |
| Fake US documents catalogued | 236,002 (USD 1,468,836.98 in sales, Jul 2024 - Aug 2025) |

## Cooperation Mechanisms Used

- **Joint operational action with the FBI** for the August 2025 infrastructure takedown - the only foreign authority named in the Dutch release. The press release does not specify whether this was conducted via formal MLAT, the [[budapest-convention|Budapest Convention]] 24/7 channel, or [[informal-cooperation|informal police-to-police cooperation]].
- **[[domain-seizure|Domain and infrastructure seizure]]** as the upstream evidence-generation step that made the user-side arrests possible.
- **[[electronic-evidence|Cross-border electronic evidence]]** flow: data extracted from servers seized in the Netherlands (with FBI partnership) drove identification of users worldwide, including in the Netherlands.
- **Domestic prosecution-channel discretion**: Politie + Openbaar Ministerie jointly decided per suspect whether to charge, summon, or apply a stop-talk.

## Challenges and Friction Points

- **Volume vs. capacity** - 636,847 identified accounts globally; only a small Dutch subset is being actioned in this wave. The press release frames further waves as inevitable but does not commit to a timeline.
- **Minor users** - the wave caught 15- and 16-year-old girls among the summoned suspects; the police chose stop-talks rather than prosecution, illustrating the diversion options Dutch practice uses for juvenile cyber-offenders.
- **KYC ecosystem dependency** - the police explicitly note ongoing dialogue with KYC providers, indicating that disrupting the user base alone is insufficient; the demand-side problem is structural to image-only KYC.
- **Source visibility on US side** - the Politie release does not disclose the US legal instruments used. Without ingesting the FBI/DOJ counterpart release, the IC mechanism is partially opaque.

## Lessons Learned

- **Server seizure as multiplier** - the value of the August 2025 joint action is demonstrated by the user-side enforcement that followed; the press release deliberately frames the takedown as "the start" rather than the end of the case.
- **Public communication of enforcement discretion** - Politie and Openbaar Ministerie publicly explain why some suspects are arrested while others are summoned or merely warned, which is unusual transparency for a cybercrime case.

## Follow-Up Actions

- Further arrest waves announced ("Dit is zeker niet de laatste serie aanhoudingen").
- Outreach to KYC providers to harden image-only verification.
- Outreach to sectors disproportionately affected by VerifTools-enabled fraud.
- Notification of identity-theft victims whose data was used to generate fake documents.

## Korean Involvement (한국의 참여)

None reported in this primary source. The press release names only the Netherlands and the United States. Korean nationals or [[knpa-cyber-bureau|KNPA Cyber Investigation Bureau]] involvement is not mentioned and should not be inferred.

## Contradictions & Open Questions

- The press release attributes the 27 Aug 2025 takedown to a Politie-FBI cooperation; an independent US-side primary source (DOJ/FBI press release) is needed to confirm the precise US legal instruments and the USD 6.4 million asset-seizure figure that has appeared in secondary reporting. Until ingested, those secondary figures are NOT asserted on this page.
- "Cryptocurrency seized" amount during the 7-8 April 2026 searches is not quantified in the release.
- Whether any suspects identified outside the Netherlands have been actioned by FBI or third-country partners is not addressed by this Dutch source.
