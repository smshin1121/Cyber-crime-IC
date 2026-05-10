---
type: operation
title: "Operation FEVER"
aliases:
  - FEVER
  - "Operacja FEVER"
  - "CBZC FEVER 2025"
case_id: CYB-2025-814
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - seizure
outcome: success
timeframe:
  announced: 2025-04-09
  start: 2025-01-01
  end: 2025-04-09
  ongoing: false
crime_types:
  - "[[csam-ic]]"
crime_type: "[[csam-ic]]"
target_entity: "Producers, distributors, and possessors of child sexual abuse material reached through dark web platforms and online forums; integrated CBZC tracks against Kidflix users and a major dark web CSAM forum."
lead_agency: "[[poland-police|CBZC (Polish Central Bureau for Combating Cybercrime)]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[poland]]"
  - "[[denmark]]"
  - "[[estonia]]"
  - "[[germany]]"
  - "[[greece]]"
  - "[[hungary]]"
  - "[[ireland]]"
  - "[[latvia]]"
  - "[[romania]]"
  - "[[spain]]"
  - "[[sweden]]"
  - "[[bulgaria]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[poland-police]]"
  - "[[europol-ec3]]"
  - "[[germany-bka]]"
  - "[[uk-nca]]"
  - "[[fbi]]"
  - "[[ncmec]]"
legal_basis:
  - "[[budapest-convention]]"
mechanisms_used:
  - "[[j-cat]]"
results:
  arrests: 166
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "98 of the 166 detentions occurred in Poland (suspects aged 22–78)."
    - "111 suspects arrested for sharing/distributing CSAM (per CBZC release)."
    - "48 pre-trial detentions ordered by Polish courts."
    - "159 searches in Poland; nearly 600 Polish officers deployed."
    - "More than 1,700 devices and data carriers seized in Poland."
    - "More than 520,000 CSAM video and image files seized in Poland."
    - "Narcotics and 3 unauthorised firearms additionally seized."
edges:
  - source_actor: poland-police
    target_actor: europol-ec3
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: poland-police
    target_actor: germany-bka
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: poland-police
    target_actor: fbi
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: undirected
  - source_actor: poland-police
    target_actor: uk-nca
    cooperation_type: info_sharing
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: fbi
    target_actor: ncmec
    cooperation_type: info_sharing
    legal_basis: bilateral_MOU
    direction: directed
credibility_index: 4.6
source_tier: 1
missing_fields:
  - victims_notified
  - domains_seized
related_cases:
  []
related_operations:
  - "[[operation-stream-kidflix]]"
challenges_encountered:
  []
lessons_learned:
  - "EU Council Presidency is being used as a political/operational anchor for member-state-led umbrella cybercrime actions; CBZC explicitly framed FEVER around Poland's H1-2025 Presidency."
  - "Umbrella ('FEVER') over named sub-operations ('Kidflix' + a CBZC–FBI dark web forum track) lets one nationally-led brand absorb cross-track results from heterogeneous bilateral and Europol-coordinated tracks."
source_count: 1
sources:
  - "[[2025-04-09_cbzc_operation-fever-largest-european-pedophile-crackdown]]"
created: 2026-05-09
updated: 2026-05-09
---
> [!info] Provisional / single-source operation page
> This page currently rests on a single tier-1 primary source (the CBZC press release of 2025-04-09). Additional Europol, NCA, FBI, and partner-country statements should be cross-walked in before promoting this page out of provisional status. Per CLAUDE.md preferred threshold (`source_count >= 5`), this page is **explicitly provisional**.

## Summary

**Operation FEVER** was a CBZC-led umbrella operation against producers, distributors, and possessors of child sexual abuse material (CSAM), organised during Poland's Presidency of the Council of the European Union (1 January – 30 June 2025) and announced publicly on 9 April 2025. The Polish Police's Centralne Biuro Zwalczania Cyberprzestępczości (CBZC), in cooperation with the Komenda Główna Policji (KGP), described FEVER as the largest CSAM-focused operation it has organised to date. CBZC reports a total of **166 detentions** across participating jurisdictions, of which **98 occurred in Poland**, with **111 of the 166** specifically arrested for sharing or distributing CSAM.

FEVER is best understood as a programmatic umbrella that absorbed at least two tracks already publicly known: the CBZC contribution to the [[operation-stream-kidflix|Kidflix takedown]] (with German police, server seized 11 March 2025 in Germany/Netherlands), and a separate CBZC–FBI investigation into a large dark web CSAM forum. Coordination ran through [[europol-ec3|Europol]] and the [[j-cat|J-CAT]] taskforce.

## Background

The Polish CBZC was established in 2022 inside the Polish Police as the central national service against cybercrime. Between 2022 and 2024 CBZC executed a sequence of domestic CSAM operations — codenamed ANASTAZJA, BARBOSSA, CARLOS, DAKOTA, and ENOLA GAY — which together resulted in charges against more than 280 people aged 16–78 and seized more than two million CSAM files. FEVER is positioned in the CBZC release as the international scale-up of that domestic line of work, leveraging Poland's EU Council Presidency to mobilise bilateral and Europol-coordinated cooperation.

## Participating Parties

The CBZC press release specifically names the participating jurisdictions and bodies:

**Lead and host (Poland):**

- [[poland-police|CBZC — Centralne Biuro Zwalczania Cyberprzestępczości]] (lead organiser)
- Komenda Główna Policji (KGP — National Police Headquarters), including its Bureau against Trafficking in Human Beings of the Criminal Bureau
- Departament do Spraw Cyberprzestępczości i Informatyzacji Prokuratury Krajowej (Cybercrime and Informatisation Department of the National Public Prosecutor's Office), with prosecutors from across Poland
- KSP (Capital Police Headquarters) and voivodeship police HQs in Gdańsk, Katowice, Kraków, Lublin, Olsztyn, Poznań, Radom, Rzeszów, Wrocław, Gorzów Wielkopolski

**Partner countries invited by Polish Police (11):**

- [[denmark|Denmark]]
- [[estonia|Estonia]]
- [[germany|Germany]]
- [[greece|Greece]]
- [[hungary|Hungary]]
- [[ireland|Ireland]]
- [[latvia|Latvia]]
- [[romania|Romania]]
- [[spain|Spain]]
- [[sweden|Sweden]]
- [[bulgaria|Bulgaria]]

**Non-EU participants at international level:**

- [[united-kingdom|United Kingdom]] — [[uk-nca|National Crime Agency]]
- [[united-states|United States]] — [[fbi|Federal Bureau of Investigation]]
- United States — Homeland Security Investigations (HSI) (Departament Śledczy ds. Bezpieczeństwa Wewnętrznego)
- United States — [[ncmec|National Center for Missing & Exploited Children]]

**Coordination:**

- [[europol-ec3|Europol]] (European Cybercrime Centre)
- [[j-cat|J-CAT — Joint Cybercrime Action Taskforce]] (hosted at Europol)

## Legal Framework

The CBZC release does not enumerate specific treaty articles, but the operation is consistent with:

- The **[[budapest-convention|Council of Europe Convention on Cybercrime (Budapest Convention)]]** — basis for cross-border preservation, mutual legal assistance, and the 24/7 Network used between European parties and the United States.
- **EU framework instruments** on combating sexual abuse and exploitation of children, including the EU directive on combating sexual abuse and exploitation of children and child sexual abuse material (2011/93/EU), which obliges all EU member states named in FEVER to criminalise CSAM possession, distribution and production.
- Polish substantive law: the release notes that public presentation of pornographic content in Poland carries a penalty of up to 15 years' imprisonment.

> [!warning] Legal status check needed
> The release's reference to "up to 15 years" is consistent with Polish Criminal Code provisions on CSAM (Art. 202 §3–§4c K.k.), but the exact provision invoked in each charging document is not stated in the press release. The Budapest Convention basis is inferred from standard practice rather than asserted by CBZC; this should be confirmed against any companion Europol or Eurojust statement.

## Operational Timeline

Per the CBZC release (publication date 2025-04-09), all dated activity sits inside Poland's H1-2025 EU Council Presidency:

- **2022–2024** — Five precursor CBZC domestic operations (ANASTAZJA, BARBOSSA, CARLOS, DAKOTA, ENOLA GAY), charging 280+ people and seizing 2M+ CSAM files. These set the operational base for an internationalised umbrella.
- **From mid-2021** — Investigations against the Kidflix dark web platform begin (as reported in the Operation Stream / Kidflix track).
- **1 January 2025** — Poland assumes Presidency of the Council of the European Union; FEVER launches as the CBZC/KGP-organised international umbrella.
- **11 March 2025** — Servers of the Kidflix CSAM streaming platform (a sub-track of FEVER) seized by German and Dutch authorities.
- **By 9 April 2025** (press release date) — CBZC reports a cumulative total of **166 detentions**, including 98 in Poland; 111 arrests specifically for CSAM sharing/distribution; 48 pre-trial detentions in Poland.
- **Post-9 April 2025** — CBZC notes that device examinations were continuing, so "presented data may rise."

## Results and Impact

From the CBZC release:

- **166 suspects detained internationally**; **98 of these in Poland**, aged 22–78.
- **111 of the 166** arrested for sharing and distributing CSAM.
- **48 pre-trial detentions** ordered by Polish courts.
- **159 searches** in Poland; **~600 Polish officers** deployed.
- **>1,700 devices and data carriers** seized in Poland.
- **>520,000 CSAM video files and photographs** seized in Poland.
- Additional seizures: narcotics; **3 unauthorised firearms**.

The CBZC press release does not report figures from non-Polish jurisdictions individually beyond the 166 international total, and does not state per-country arrest counts for the 11 invited partners.

## Cooperation Mechanisms Used

The release identifies several distinct cooperation patterns under the FEVER umbrella:

1. **Europol coordination + J-CAT** — strategic and tactical coordination across the European partners, hosted at Europol.
2. **Bilateral CBZC ↔ German police** — the joint operation against the **Kidflix** platform, with the German action seizing the platform's server (with Dutch involvement, per the Operation Stream record).
3. **Bilateral CBZC ↔ FBI** — joint targeting of members of "one of the largest international forums in hidden Internet resources" trading CSAM; charges of possession and distribution against several individuals.
4. **NCMEC information sharing** — referrals from the US-based National Center for Missing & Exploited Children, which under US law receives CyberTipline reports from US providers.
5. **UK NCA participation** — at international level, alongside FBI/HSI.

## Challenges and Friction Points

The CBZC release does not enumerate specific friction points. However, generic challenges relevant to a Polish-led umbrella absorbing US, UK, and 11 EU partner tracks include:

- Differences in CSAM definitions and statutory thresholds across the 12 EU jurisdictions plus US and UK regimes.
- Cross-border evidence transfer between EU member states (EIO/Budapest 24/7) and to/from the US (MLAT or CLOUD Act + bilateral channels).
- Coordination across Europol J-CAT and parallel bilateral channels (CBZC–BKA on Kidflix; CBZC–FBI on the dark web forum) so that overlapping suspects are not double-charged or lost.

These are *plausible* friction points consistent with CSAM operations of this scale; the release itself does not name them, so they are flagged here as analytic context rather than asserted facts.

## Lessons Learned

- **Member-state-presidency-anchored umbrella operations** are emerging as a pattern: a national cybercrime bureau leverages its country's EU Council Presidency to brand and coordinate a multi-track international action.
- **Umbrella + named sub-operations** (FEVER → Kidflix; FEVER → CBZC–FBI dark web forum) is operationally efficient but creates **provenance risk for downstream wiki/analytical work**: the same arrest can be attributed to FEVER, to Kidflix/Operation Stream, or to a Europol-coordinated CSAM action depending on which press release is cited.

## Follow-Up Actions

- Cross-walk Europol's communication on the Kidflix takedown (already partly captured under [[operation-stream-kidflix]]) with the CBZC FEVER framing to deconflict counts.
- Locate and ingest companion press releases from the 11 invited EU partner agencies (BKA Germany, Spanish Guardia Civil/Policía Nacional, Romanian DIICOT/IGPR, etc.) to obtain per-country arrest figures.
- Confirm participation of HSI as a distinct US agency (currently included only by name in the Polish release; no separate HSI statement is yet ingested).

## Korean Involvement (한국의 참여)

The CBZC release **does not name South Korea** as a participating jurisdiction. South Korea is not among the 11 invited partners or the named non-EU participants (UK, US/FBI, US/HSI, NCMEC). No Korean involvement in FEVER can be asserted from this source; absence of mention is not a positive denial.

## Contradictions & Open Questions

- **Numerical attribution between FEVER and Kidflix.** CBZC says FEVER produced 166 detentions internationally and 98 in Poland; the Operation Stream / Kidflix record asserts 79 arrests worldwide tied to that platform. The two sets are not the same; FEVER's 166 includes Kidflix-related arrests (12 in Poland reached via the Kidflix track, per CBZC) plus the parallel CBZC–FBI dark web forum track plus other partner-country arrests. Until partner-country breakdowns are published, the exact split between FEVER tracks is unverifiable.
- **Per-country arrest counts** for the 11 invited EU partners (Denmark, Estonia, Germany, Greece, Hungary, Ireland, Latvia, Romania, Spain, Sweden, Bulgaria) are not given in this source; only the 98-in-Poland subtotal is asserted.
- **Operational period.** The CBZC release frames FEVER around Poland's full Presidency (H1 2025) but only reports cumulative results as of 9 April 2025. A subsequent CBZC end-of-presidency communication, if any, would be needed to capture the full operation envelope.
- **HSI vs. ICE-HSI nomenclature.** The Polish release uses the literal translation "Departament Śledczy ds. Bezpieczeństwa Wewnętrznego" alongside the abbreviation HSI. This is the US Homeland Security Investigations (a component of ICE). The wiki does not yet contain an HSI organisation page; cross-link is therefore unresolved at the time of ingest.
