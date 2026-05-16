---
type: operation
title: "Spain–U.S. Calpe Hacker Arrest — 40+ Cyberattacks on Strategic Institutions (Policía Nacional + Guardia Civil + HSI + Europol, 2025)"
title_ko: "스페인-미국 칼페 해커 검거 — 전략기관 40+ 사이버공격 (Policía Nacional + Guardia Civil + HSI + Europol, 2025)"
aliases:
  - "Calpe hacker arrest February 2025"
  - "Detenido peligroso hacker 40 ciberataques organismos estratégicos"
  - "Spain Policía Nacional Guardia Civil HSI Europol hacker arrest 2025"
case_id: CYB-2025-143
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - search
  - seizure
outcome: success
timeframe:
  announced: 2025-02-05
  start: 2024-02
  end: 2025-02-04
  ongoing: false
crime_type: "[[hacking-ic]]"
crime_types:
  - "[[hacking-ic]]"
  - "[[money-laundering-ic]]"
target_entity: "Single suspect: an individual (identity not disclosed in the public source) arrested in Calpe (Alicante, Spain) on the Tuesday before 5 February 2025 (i.e., 4 February 2025). The suspect is described in the Policía Nacional press release as a hacker who, between February 2024 and late December 2024, carried out more than 40 cyberattacks against Spanish and international public and private entities, claimed those intrusions in darkweb forums under multiple pseudonyms, and held more than 50 cryptocurrency accounts with various cryptoassets at the time of the search."
lead_agency: "[[spain-national-police]]"
coordinating_body: ""
participating_countries:
  - "[[spain]]"
  - "[[united-states]]"
participating_agencies:
  - "[[spain-national-police]]"
  - "[[spain-guardia-civil]]"
  - "[[europol-ec3]]"
legal_basis:
  - "Spanish Código Penal articles on descubrimiento y revelación de secretos (arts. 197 et seq.), acceso ilícito a sistemas informáticos (art. 197 bis), daños informáticos (art. 264 et seq.), and blanqueo de capitales (arts. 301 et seq.). The press release lists the four crime headings verbatim but does not cite the underlying articles by number."
  - "Judicial search and seizure executed under Spanish Ley de Enjuiciamiento Criminal at the suspect's residence, recovering IT equipment and information on more than 50 cryptocurrency accounts."
  - "International cooperation channel for the U.S. leg: collaboration with Homeland Security Investigations (HSI) of the U.S. Department of Homeland Security; specific bilateral instrument (MLAT, informal LE channel, or Europol-mediated SIENA exchange) is not enumerated in the public source."
mechanisms_used:
  - "[[informal-cooperation]]"
  - "[[search-seizure]]"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "More than 50 cryptocurrency accounts identified at the suspect's residence; specific token types and recovered amounts not enumerated in the public source"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Diverse IT equipment seized at the suspect's residence under judicial search and submitted for forensic analysis"
    - "Investigators report the search may uncover further offences beyond the 40+ attacks already documented"
edges:
  - source_actor: spain
    target_actor: united-states
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: spain-national-police
    target_actor: spain-guardia-civil
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: spain-national-police
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: directed
credibility_index: 3.2
source_tier: 1
missing_fields:
  - "Identity of the suspect (not disclosed in the public source)"
  - "Specific bilateral instrument relied on for U.S. (HSI) cooperation"
  - "Whether U.S. predicate offences (e.g., NATO / U.S. Army database intrusions) have been or will be charged in the United States"
  - "Quantified amounts of cryptocurrency held in the 50+ identified accounts and any amount recovered or frozen"
  - "Specific Spanish criminal-code articles invoked (only the four crime headings are listed in the press release)"
  - "Identity of the Spanish investigating court / juzgado de instrucción supervising the case"
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "Spain–U.S. cyber-LE cooperation runs through multiple distinct channels: this case used Homeland Security Investigations (HSI) of DHS rather than the FBI, alongside Europol as the intergovernmental coordinator. Treating 'Spain–U.S. cyber cooperation' as a monolithic FBI channel is empirically wrong; HSI is a parallel U.S. cyber-investigations route that surfaces in cases where the underlying activity touches U.S. military or DHS-jurisdiction databases."
  - "Spanish national-security architecture for high-profile cyber-attack cases combines judicial police (Policía Nacional + Guardia Civil) with national cryptologic / signals-intelligence services (CCN / CNI). The CCN, formally part of the CNI, is described in the press release as a 'decisive collaborator' — a useful data point on the operational role of CCN-CERT-equivalent functions in Spanish cyber-attack prosecutions."
  - "Investigation triggers can switch between Spanish forces. Here, Policía Nacional opened the case in February 2024 after a private-sector complaint about a darkweb leak; the Guardia Civil UCO then developed the case after the suspect's late-December 2024 attack on Guardia Civil and Ministry of Defence databases. The two forces then executed the operational exploitation jointly. This 'force handover and rejoin' pattern is structurally specific to Spain's dual-force LE architecture and is unusual relative to single-LE-force jurisdictions."
  - "Strategic-target attribution language: the press release names NATO, U.S. Army, UN, and ICAO databases as institutional victims of a single hacker. This is one of the few cases where a Spanish LE primary source publicly enumerates intergovernmental victims of a non-state cyber actor with this granularity, providing a useful empirical anchor for downstream comparative work on cyber-attack target patterns."
source_count: 1
sources:
  - "[[2025-02-05_policia-es_detenido-peligroso-hacker-40-ciberataques-organismos-estrategicos]]"
created: 2026-05-16
updated: 2026-05-16
summary: "On the Tuesday before 5 February 2025 (i.e., 4 February 2025) the Spanish National Police (Policía Nacional), in a joint operation with the Spanish Guardia Civil, arrested in Calpe (Alicante, Spain) an individual described in the Policía Nacional's official press release as a hacker responsible for more than 40 cyberattacks against Spanish and international public and private entities. Named institutional victims include the Spanish Guardia Civil, the Spanish Ministry of Defence, the Fábrica Nacional de Moneda y Timbre, the Servicio Público de Empleo Estatal, the Spanish Ministry of Education and Vocational Training and Sports, the Dirección General de Tráfico, the Generalitat Valenciana, multiple Spanish universities, NATO databases, U.S. Army databases, the United Nations, and the International Civil Aviation Organization (ICAO). The suspect was charged with descubrimiento y revelación de secretos, acceso ilícito a sistemas informáticos, daños informáticos, and blanqueo de capitales. The search of the residence recovered IT equipment and information on more than 50 cryptocurrency accounts. International cooperation was explicitly named in the primary source as Spain (Policía Nacional + Guardia Civil + CCN-CNI) ↔ United States (Homeland Security Investigations, DHS), coordinated with Europol."
jurisdictions:
  - "[[spain]]"
  - "[[united-states]]"
organizations:
  - "[[spain-national-police]]"
  - "[[spain-guardia-civil]]"
  - "[[europol-ec3]]"
---

## Summary

On the **Tuesday before 5 February 2025** (i.e., **4 February 2025**), the **Spanish National Police (Policía Nacional)** and the **Guardia Civil** arrested an individual in **Calpe (Alicante province, Spain)** for alleged participation in unauthorised disclosure of secrets, illicit access to computer systems, computer damage, and money laundering ("descubrimiento y revelación de secretos, acceso ilícito a sistemas informáticos, daños informáticos y blanqueo de capitales"). The suspect is described in the official Policía Nacional press release as a hacker responsible for more than 40 cyberattacks against Spanish and international public and private entities between February 2024 and late December 2024, who claimed the intrusions in darkweb forums under multiple pseudonyms.

The search of the suspect's residence recovered diverse IT equipment, which has been submitted for forensic analysis, and revealed more than 50 cryptocurrency accounts holding various cryptoassets — described in the press release as a marker of the suspect's deep familiarity with the blockchain ecosystem.

The press release explicitly names the **decisive collaboration of the Centro Criptológico Nacional (CCN) of the Centro Nacional de Inteligencia (CNI)** on the Spanish side, and the **collaboration of EUROPOL and the Homeland Security Investigations (HSI) of the United States** on the international side. This is the operative multi-jurisdiction cooperation language for L24 purposes.

The press release was published on **5 February 2025** by the Sala de prensa of the Dirección General de la Policía (Policía Nacional, Spain) on its institutional press-release portal at `policia.es` (comunicado nota de prensa ID 16448).

## Background

The investigation was opened by the **Policía Nacional in February 2024** following a complaint by a Madrid-based business association after a publication appeared in a specialised data-leak forum claiming to hold information extracted from the association's website. Initial investigation by the Policía Nacional confirmed that, in addition to the data exfiltration, the suspect had defaced the association's portal with a message claiming to have hacked the system.

Throughout 2024, the investigated actor carried out numerous further cyberattacks, including documented attacks on:

- the **Fábrica Nacional de Moneda y Timbre** (Spanish Royal Mint);
- the **Servicio Público de Empleo Estatal**;
- the **Ministry of Education, Vocational Training and Sports**;
- multiple Spanish universities;
- **NATO** databases;
- **U.S. Army** databases;
- the **Dirección General de Tráfico**;
- the **Generalitat Valenciana**;
- the **United Nations**;
- the **International Civil Aviation Organization (ICAO)**;
- and, in the last claimed attack, two databases of the **Guardia Civil** and the **Ministry of Defence**.

This final attack, executed in **late December 2024**, triggered the involvement of the **Unidad Central Operativa (UCO) of the Guardia Civil**, which developed the investigation and identified the same actor as the perpetrator. From that point onwards, the **Policía Nacional and Guardia Civil executed the operational exploitation jointly**, leading to the 4 February 2025 arrest in Calpe.

The suspect is described as having configured a complex technological setup using anonymous messaging and browsing applications to obscure his tracks and frustrate identification.

## Participating Parties

**Spain (national authorities)**

- **Policía Nacional (Cuerpo Nacional de Policía)** — investigative lead from February 2024; joint executor of the action day. Issuer of the public press release.
- **Guardia Civil — Unidad Central Operativa (UCO)** — case developer after the late-December 2024 attack on Guardia Civil and Ministry of Defence databases; joint executor of the action day.
- **Centro Criptológico Nacional (CCN)** of the **Centro Nacional de Inteligencia (CNI)** — described in the press release as a "decisive collaborator" of the operation on the Spanish national-security side.

**United States**

- **Homeland Security Investigations (HSI)** of the U.S. Department of Homeland Security — explicitly named in the press release as an international collaborator. No specific HSI office or attaché is named; the bilateral instrument relied on for the cooperation is not enumerated.

**Intergovernmental partner**

- **EUROPOL** — explicitly named in the press release as an international collaborator. The role is not specified beyond "colaboración"; on the basis of Europol's general mandate the role is likely Europol Cybercrime Centre (EC3) coordination and SIENA-mediated information exchange, but the press release does not specify EC3.

> [!note] L24 compliance
> Only Spain and the United States are listed in this operation page's `participating_countries` field, because they are the only two countries whose specific national authorities are explicitly named as cooperating LE/intelligence partners in the tier-1 primary source. NATO, U.S. Army, UN, and ICAO are listed as institutional victims of the suspect's cyberattacks — not as cooperating jurisdictions — and are therefore captured in the body prose, not in the cooperation frontmatter. Europol is listed as a participating intergovernmental agency via `[[europol-ec3]]` but not as a country.

> [!note] L23 compliance
> `lead_agency` is set to the existing wikilink `[[spain-national-police]]`. `coordinating_body` is left empty because no single coordinating entity is named in the primary source. `participating_agencies` contains only wikilinks to existing wiki pages (`[[spain-national-police]]`, `[[spain-guardia-civil]]`, `[[europol-ec3]]`). The Centro Criptológico Nacional / CNI and the Homeland Security Investigations (HSI) of DHS are recorded in body prose because their wiki pages do not yet exist; per L23 these are not added to frontmatter as plain text.

## Legal Framework

The press release lists four Spanish criminal-law headings without article numbers:

- **Descubrimiento y revelación de secretos** — Spanish Código Penal arts. 197 et seq. (privacy / data-access offences).
- **Acceso ilícito a sistemas informáticos** — Spanish Código Penal art. 197 bis (unauthorised access to information systems), implementing Directive 2013/40/EU on attacks against information systems.
- **Daños informáticos** — Spanish Código Penal arts. 264 et seq. (computer damage / sabotage).
- **Blanqueo de capitales** — Spanish Código Penal arts. 301 et seq. (money laundering).

The specific article numbers are listed here for orientation only; the press release itself only names the four crime headings in Spanish.

Cooperation legal basis:

- **Spanish judicial search and seizure** under the Ley de Enjuiciamiento Criminal recovered the IT equipment and the cryptocurrency-account information at the suspect's residence in Calpe.
- **International cooperation channel** for the U.S. leg via Homeland Security Investigations (HSI) — the specific bilateral instrument (MLAT under the 1990 U.S.–Spain MLAT, informal LE-to-LE channel, or HSI Attaché office liaison) is not enumerated in the public source.
- **Europol channel** — coordination role; specific Europol product (SIENA message, EMPACT operational action plan, EC3 analytical project) not enumerated in the public source.

> [!warning] Legal status check needed
> The Spanish criminal-code articles are inferred from the published charging headings; only the headings are stated in the press release. The bilateral U.S.–Spain instrument relied on for the HSI cooperation is not named in the source and would need to be confirmed against any future U.S. charging instrument or against Spanish judicial filings if they become public.

## Operational Timeline

- **2024-02** — Madrid-based business association files a complaint with the Policía Nacional after detecting a publication on a specialised data-leak forum claiming to hold information extracted from the association's website. Investigation opens.
- **2024 (throughout the year)** — Suspect carries out more than 40 cyberattacks against Spanish and international public and private institutions, claiming the intrusions in darkweb forums under multiple pseudonyms (up to three distinct pseudonyms documented).
- **2024-12 (late)** — Suspect attacks two databases of the Guardia Civil and the Spanish Ministry of Defence. The Unidad Central Operativa (UCO) of the Guardia Civil opens its own investigation and identifies the same actor.
- **2024-12 to 2025-02-04** — Joint operational exploitation by Policía Nacional and Guardia Civil, with decisive collaboration of CCN (CNI) on the Spanish national-security side and with EUROPOL and HSI on the international side.
- **2025-02-04** (Tuesday) — Joint arrest in Calpe (Alicante). Judicial search of the suspect's residence recovers diverse IT equipment and information on more than 50 cryptocurrency accounts. Suspect charged with descubrimiento y revelación de secretos, acceso ilícito a sistemas informáticos, daños informáticos, and blanqueo de capitales.
- **2025-02-05** — Policía Nacional publishes the official press release on its institutional Sala de prensa portal (`policia.es` comunicado ID 16448).

## Results and Impact

- **1 arrest** — identity not disclosed in the public source.
- **More than 50 cryptocurrency accounts** identified at the suspect's residence; specific token types and recovered amounts not enumerated.
- **Diverse IT equipment seized** under judicial search at the residence, submitted for forensic analysis. Investigators note that the search may uncover further offences.
- **Documented attack surface**: 40+ cyberattacks; named institutional victims span Spanish national agencies (Guardia Civil, Ministry of Defence, Fábrica Nacional de Moneda y Timbre, Servicio Público de Empleo Estatal, Ministry of Education, Dirección General de Tráfico, Generalitat Valenciana), Spanish universities, and intergovernmental victims (NATO, U.S. Army, UN, ICAO).

## Cooperation Mechanisms Used

- **Joint Policía Nacional + Guardia Civil execution** — Spain's dual-LE-force architecture executed the operational exploitation jointly after a force handover triggered by the late-December 2024 attack on Guardia Civil / Ministry of Defence databases.
- **CCN / CNI decisive collaboration** — Spanish national cryptologic / signals-intelligence services provided decisive support to the joint LE operation; the specific role (forensic, attribution, threat-intelligence) is not enumerated in the source.
- **EUROPOL coordination** — explicitly named as an international collaborator. The Europol Cybercrime Centre (EC3) is the natural Europol counterpart for this type of case and is wikilinked as `[[europol-ec3]]` in the frontmatter on that structural basis.
- **U.S. cooperation via Homeland Security Investigations (HSI)** — explicit foreign-LE cooperation channel for the U.S. leg, rather than via FBI. The press release names HSI only and does not specify FBI involvement; the HSI office and attaché chain are not named.

## Challenges and Friction Points

- **Anonymisation by the suspect** — the press release describes a "complex technological setup" using anonymous messaging and navigation applications, configured by the suspect to obscure his tracks and frustrate identification.
- **Multi-pseudonym claiming pattern** — the suspect claimed attacks under up to three distinct darkweb pseudonyms, complicating actor-identification before the December 2024 Guardia Civil / Defence attack provided the convergence point.
- **Identification opacity in the public source** — the suspect is not named in the press release; the specific cryptoasset types and amounts are not enumerated; the Spanish investigating court is not identified; the U.S. predicate-offence / U.S. charging instrument (if any) is not in the source.
- **Single-source dependency** — as of 2026-05-16, this operation page rests on one tier-1 primary source. Independent corroboration from HSI, U.S. court filings, or Europol press releases is not yet integrated.

## Lessons Learned

- **HSI as a parallel U.S. cyber-LE channel** — this case documents Homeland Security Investigations (HSI) of DHS as the U.S. cooperation counterparty in a Spanish cyber-attack case, with no FBI involvement named in the primary source. "Spain–U.S. cyber cooperation" therefore runs through multiple distinct U.S. channels, and HSI is one of them — especially in cases that touch DHS-relevant institutional victims (e.g., U.S. military / U.S. critical-infrastructure databases).
- **CCN / CNI as decisive support in Spanish cyber prosecutions** — the press release names CCN (the national cryptologic centre, formally part of CNI, Spain's national-intelligence service) as a decisive collaborator alongside the two LE forces. This documents the operational role of CCN-CERT-equivalent functions in Spanish cyber-attack prosecutions of named individual suspects.
- **Dual-force handover and rejoin pattern** — Spain's two-force architecture (Policía Nacional + Guardia Civil) here executed a clean handover (Policía Nacional opens in Feb 2024 → Guardia Civil UCO joins in late Dec 2024 → joint exploitation through Feb 2025), which is structurally specific to Spain and useful as a comparative reference for jurisdictions with separated municipal vs. military LE forces.
- **Public enumeration of intergovernmental victims** — this is one of the rare Spanish LE primary sources that publicly names NATO, U.S. Army, UN, and ICAO databases as victims of a single named criminal investigation. This level of public enumeration provides a useful empirical anchor for downstream analytical work on cyber-attack target patterns against intergovernmental organisations.

## Follow-Up Actions

Outstanding evidentiary tracks consistent with the public source:

- **Charging instrument** at the Spanish juzgado de instrucción supervising the case — including specific Código Penal articles invoked and any indictment progression.
- **Forensic analysis of the seized IT equipment and the 50+ cryptocurrency accounts** — including identification of the tokens held, amounts, and any recovery or freezing orders.
- **Possible U.S. parallel proceedings** — given the named U.S. Army and NATO victims and the explicit HSI cooperation, a U.S. parallel investigation (HSI, DOJ, or military) is structurally plausible but not in the public source.
- **Independent corroboration** from HSI, DHS, NATO, or U.S. military press releases.
- **Identity disclosure** in a future Spanish judicial decision or filing if proceedings progress to public charging.

## Korean Involvement (한국의 참여)

None reported in the source.

## Contradictions & Open Questions

- **Suspect identity**: not disclosed in the public source.
- **Specific Código Penal articles invoked**: not in the source — only the four crime headings are named.
- **Bilateral U.S.–Spain instrument relied on for HSI cooperation**: not invoked by name. The natural candidates are the 1990 U.S.–Spain MLAT or an informal HSI Attaché LE-to-LE channel; the source does not state which.
- **Specific cryptocurrency / token types / amounts** held in the 50+ identified accounts: not enumerated; no quantified seizure or freezing reported.
- **Europol product / project**: not specified beyond "colaboración".
- **HSI office / attaché chain**: not named.
- **U.S. parallel proceeding**: not addressed in the source — the named U.S. Army database victim creates a structural possibility of a U.S. parallel charging instrument that is not in this Spanish source.
- **Identity of the Spanish investigating juzgado de instrucción**: not in the source.

## Source

- Policía Nacional (España), Sala de prensa, "Detenido un peligroso hacker responsable de más de 40 ciberataques a organismos estratégicos", 05/02/2025 — [[2025-02-05_policia-es_detenido-peligroso-hacker-40-ciberataques-organismos-estrategicos]] — <https://www.policia.es/_es/comunicacion_prensa_detalle.php?ID=16448>
