---
type: operation
title: "Operación KAERB — iServer phishing-as-a-service platform takedown (announced September 2024)"
aliases:
  - "Operation Kaerb"
  - "iServer takedown 2024"
  - "PAcCTO 2.0 / AMERIPOL / EUROPOL six-country phone-unlock phishing takedown"
case_id: CYB-2024-AR-KAERB
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search-seizure
outcome: success
timeframe:
  announced: 2024-09-24
  start: 2024-09-10
  end: 2024-09-24
  ongoing: false
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[identity-theft]]"
  - "[[organized-crime-ic]]"
  - "[[extortion-ic]]"
target_entity: "iServer phishing-as-a-service platform — a Spanish-language criminal SaaS used by 2,000+ subscriber cybercriminals (\"desbloqueadores\") to phish credentials from theft victims of stolen high-end mobile phones, enabling unauthorized device unlock and downstream fraud, extortion and data theft."
lead_agency: "[[spain-national-police]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[argentina]]"
  - "[[spain]]"
  - "[[colombia]]"
  - "[[chile]]"
  - "[[ecuador]]"
  - "[[peru]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[spain-national-police]]"
  - "[[spain-guardia-civil]]"
  - "[[group-ib]]"
legal_basis:
  - "Argentine Penal Code provisions on fraud, illegitimate access to information systems, and participation in a criminal association — operational basis for the 12 Argentine domiciliary searches and 5 arrests authorised in the Autonomous City of Buenos Aires, Santa Fe, Córdoba, and Jujuy."
  - "Spanish Criminal Code provisions on stolen-property handling, fraud, and computer offences — operational basis for the Spanish enforcement leg."
  - "Domestic substantive- and procedural-law instruments of Colombia, Chile, Ecuador, and Peru on computer fraud and organised crime, applied via AMERIPOL channels — the Argentine release does not cite specific statutes for those four jurisdictions."
  - "Informal multilateral coordination via EUROPOL (Agencia de la Unión Europea para la Cooperación Policial), AMERIPOL (Comunidad de Policías de América), and the EU-funded PAcCTO 2.0 programme; the Argentine release does not cite a specific MLAT instrument."
mechanisms_used:
  - "[[informal-cooperation]]"
results:
  arrests: 17
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "28 home searches conducted starting 10 September 2024 across the six participating countries."
    - "921 electronic devices seized in aggregate."
    - "iServer phishing-as-a-service platform dismantled; 2,000+ subscriber accounts disrupted."
    - "Argentina contributed 5 of the 17 arrests and 12 of the 28 searches; the platform administrator (apex of the criminal organisation) is described as a citizen residing in Santa Fe Province, Argentina."
    - "Estimated 483,000 victims globally (Chile 77,000; Colombia 70,000; Ecuador 42,000; Peru 41,500; Spain 30,000; Argentina 29,000; ~193,500 in other jurisdictions) — based on the platform's own internal records as cited in the Argentine release."
edges:
  - source_actor: spain-national-police
    target_actor: europol-ec3
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: argentina
    cooperation_type: info_sharing
    legal_basis: informal
    direction: directed
  - source_actor: argentina
    target_actor: colombia
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: argentina
    target_actor: chile
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: argentina
    target_actor: ecuador
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: argentina
    target_actor: peru
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: group-ib
    target_actor: europol-ec3
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: directed
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "Specific MLAT or bilateral treaty instrument invoked (the Argentine release does not name one; coordination is described in terms of EUROPOL, AMERIPOL, and PAcCTO 2.0 programmatic channels)."
  - "Per-country breakdown of the 17 arrests beyond Argentina's 5 (the Argentine release provides only Argentina's share; other-country splits would need cross-reference to Europol / national-jurisdiction releases not ingested here)."
  - "Domain seizures, server seizures and infrastructure dismantlement specifics for the iServer platform itself (the Argentine release describes the takedown at the actor / arrest level rather than the infrastructure level)."
  - "Total monetary loss to victims (the release reports a victim count of 483,000 but no aggregate fraud loss)."
  - "Procedural status of the Argentine administrator (named in secondary press as Iván David Cudde, but the primary-source Argentine release identifies the apex suspect only by Santa Fe residency)."
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "The PAcCTO 2.0 programme (Programa de Asistencia Contra el Crimen Transnacional Organizado, EU-funded) is named in the release as a coordination conduit alongside EUROPOL and AMERIPOL — a tri-modal architecture in which the EU-side coordination (EUROPOL) and the Latin American policing community (AMERIPOL) are bridged by an EU-funded technical-assistance instrument (PAcCTO 2.0). This is a documented worked example of how the Latin American leg of multinational cybercrime takedowns can be wired through PAcCTO."
  - "Public-private intelligence partnership: Group-IB is named as a private-sector contributor whose collaborative input the release describes as 'invaluable'. The operation is consistent with the Group-IB-aided EUROPOL-coordinated public-private template visible in earlier ingested operations such as [[carding-action-2020]]."
  - "Stolen-phone phishing-as-a-service: this operation documents a niche cybercrime supply chain in which a single SaaS administrator served 2,000+ downstream offenders (\"desbloqueadores\") who phished credentials needed to unlock stolen high-end devices. The Spanish-language descriptive vocabulary ('desbloqueador') for this niche subscriber role does not have a direct English-language counterpart in mainstream cybercrime literature."
source_count: 1
sources:
  - "[[2024-09-24_argentina-gob-ar_operacion-kaerb-iserver-phishing-as-a-service-takedown]]"
created: 2026-05-09
updated: 2026-05-09
---

> [!info] Provisional / single-source page
> This page is below the preferred `source_count >= 5` publication threshold. It is retained as a tier-1 primary-source operation page because the Argentine Ministry of Security / Policía Federal Argentina issued an institutionally signed press release on `argentina.gob.ar` naming all six participating jurisdictions, the platform, the coordination architecture (EUROPOL, AMERIPOL, PAcCTO 2.0, Group-IB), aggregate enforcement totals, and per-country victim counts. Eurojust/Europol English-language coverage and Group-IB's PRNewswire release in the same news cycle independently corroborate headline figures (17 arrests, 28 searches, 921 devices, six countries, 483,000 victims). Those secondary sources should be folded in when next ingested, and the page should be promoted out of provisional status at that point.

## Summary

On **24 September 2024**, the Argentine Ministry of Security (Ministerio de Seguridad de la Nación) and the [[europol-ec3|Europol]]–[[argentina|Argentina]]–[[spain|Spain]]–[[colombia|Colombia]]–[[chile|Chile]]–[[ecuador|Ecuador]]–[[peru|Peru]] coalition announced the takedown of the **iServer phishing-as-a-service platform** in a multinational law-enforcement action codenamed **Operación KAERB** ("Break" reversed). Enforcement actions began on 10 September 2024 and produced **17 arrests**, **28 home searches**, and the seizure of **921 electronic devices** across the six participating countries. The platform had operated for at least five years, served **2,000+ subscriber cybercriminals** (Argentine-Spanish: "desbloqueadores"), and is associated with an estimated **483,000 victims globally**. The platform administrator — described in the Argentine release as a citizen residing in Santa Fe Province, Argentina — sat at the apex of the criminal organisation.

The Argentine release names the cooperation architecture explicitly: **EUROPOL** (EU-side police cooperation), **AMERIPOL** (Latin American police community), and **PAcCTO 2.0** (Programa de Asistencia Contra el Crimen Transnacional Organizado, the EU-funded technical-assistance programme bridging the two), with private-sector intelligence support from **[[group-ib|Group-IB]]**.

## Background

iServer was a Spanish-language criminal Software-as-a-Service used to industrialise phishing against the victims of mobile-phone theft. Subscriber-cybercriminals — "desbloqueadores" in the Argentine release — used iServer-generated phishing messages to trick theft victims into surrendering the credentials needed to unlock stolen high-end devices, enabling onward unauthorised access, data theft, fraud, and extortion. The administrator, residing in Santa Fe Province, Argentina, supplied the technical platform and support to the subscriber base.

The release attributes the bulk of the global victim population to Latin America: Chile (77,000), Colombia (70,000), Ecuador (42,000), Peru (41,500), Spain (30,000), and Argentina (29,000), plus approximately 193,500 in other jurisdictions. iServer had operated for at least five years and had **more than 2,000 registered subscriber accounts**.

## Participating Parties

**[[argentina|Argentina]]**
- **Ministerio de Seguridad de la Nación** — strategic lead on the Argentine side; Secretary of Security **Alejandra Monteoliva** is named as the press-conference principal. (No standalone wiki page yet.)
- **Policía Federal Argentina (PFA), División Ciberpatrullaje** — operational lead for cyberinvestigative work in Argentina; **Comisario Gustavo Cabada** is named in the release. (No standalone wiki page yet.)
- **Gendarmería Nacional Argentina (GNA)** — operational support for Argentine searches; **Comandante General Claudio Miguel Brilloni** is named in the release. (No standalone wiki page yet.)

**[[spain|Spain]]**
- [[spain-national-police|Cuerpo Nacional de Policía]] and [[spain-guardia-civil|Guardia Civil — Grupo de Delitos Telemáticos]] are referenced descriptively as the Spanish enforcement legs; the Argentine release names **Spanish Counsellor Francisco Arenas Morales** as the Spanish liaison participating in the press conference but does not specify which Spanish unit led the Spanish-side searches.

**[[colombia|Colombia]]**, **[[chile|Chile]]**, **[[ecuador|Ecuador]]**, **[[peru|Peru]]**
- "Cuerpos policiales y Fiscalías" of each jurisdiction are referenced collectively in the Argentine release. Specific Colombian / Chilean / Ecuadorian / Peruvian unit identification is not provided in the primary source ingested here. (No standalone wiki pages for these national cyber units yet.)

**Coordination architecture**
- **[[europol-ec3|Europol]] (EUROPOL)** — EU-side police-cooperation backbone.
- **AMERIPOL (Comunidad de Policías de América)** — Latin American policing community. (No standalone wiki page yet.)
- **PAcCTO 2.0 (Programa de Asistencia Contra el Crimen Transnacional Organizado)** — EU-funded technical-assistance programme bridging EUROPOL and Latin American partners. (No standalone wiki page yet.)
- **[[group-ib|Group-IB]]** — private-sector intelligence and technical support; the Argentine release describes the contribution as "invaluable".

> [!note] Wikilink coverage
> Of the participating entities, only [[europol-ec3|Europol]], [[group-ib|Group-IB]], [[spain-national-police|Cuerpo Nacional de Policía]], and [[spain-guardia-civil|Guardia Civil GDT]] currently have standalone organisation pages in this wiki. The Argentine PFA, AMERIPOL, PAcCTO 2.0, and the Colombian / Chilean / Ecuadorian / Peruvian cyber units are referenced descriptively pending future ingestion.

## Legal Framework

The Argentine release frames the operation in terms of multinational police-cooperation channels rather than a single named treaty instrument:

- **EUROPOL** is invoked as the EU-side cooperation conduit. No specific Europol regulation article is cited in the primary source.
- **AMERIPOL** is invoked as the Latin American policing community's coordination conduit. AMERIPOL is a regional cooperation organisation rather than a treaty instrument; the cooperation channel is institutional/programmatic.
- **PAcCTO 2.0** is named as the EU-funded technical-assistance programme bridging EUROPOL and AMERIPOL for transnational organised-crime cases in Latin America.
- **Domestic Argentine penal law** — the release describes "registros domiciliarios" (judicial home searches) authorised in four Argentine provinces, implying domestic Argentine federal-court authorisation; no specific Penal Code article is cited.
- **MLAT instruments** are not cited in the Argentine release.

> [!warning] Legal status check needed
> The Argentine release does not enumerate the per-country statutory bases for the searches and arrests in Spain, Colombia, Chile, Ecuador, and Peru. A second-source pass should fold in the Europol / Eurojust / national-jurisdiction releases for those legal hooks before the page is promoted out of provisional status.

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| ≥ 2019 | iServer platform begins operating ("opera desde hace al menos 5 años" as of September 2024) | argentina.gob.ar |
| 10 September 2024 | First wave of 28 home searches across six countries begins | argentina.gob.ar |
| September 2024 (in window 10-24 Sept) | 17 arrests effected across the six countries; 921 electronic devices seized | argentina.gob.ar |
| 24 September 2024 | Press conference and joint announcement by the Argentine Secretary of Security, Spanish Counsellor, PFA División Ciberpatrullaje, and Gendarmería Nacional Argentina | argentina.gob.ar |

## Results and Impact

The Argentine release reports the following aggregate results:

- **17 arrests** across Spain, Argentina, Colombia, Chile, Ecuador, and Peru.
- **28 home searches**.
- **921 electronic devices** seized.
- **5 arrests / 12 searches** specifically in Argentina, distributed across the Autonomous City of Buenos Aires (5 searches), Santa Fe (3), Córdoba (3), and Jujuy (1).
- **iServer phishing-as-a-service platform** disrupted; the apex administrator residing in Santa Fe Province, Argentina, is among those arrested.
- **Estimated victim base of 483,000** worldwide, dominated by Latin American jurisdictions: Chile (77,000), Colombia (70,000), Ecuador (42,000), Peru (41,500), Spain (30,000), Argentina (29,000), with ~193,500 in other countries.

Aggregate monetary loss to victims is not reported in the primary source.

## Cooperation Mechanisms Used

- **EUROPOL coordination** — EU-side police-cooperation backbone for the operation.
- **AMERIPOL coordination** — Latin American policing community coordination across Argentina, Colombia, Chile, Ecuador, and Peru.
- **PAcCTO 2.0** — EU-funded technical-assistance programme used as the bridging instrument between EUROPOL and AMERIPOL for the LATAM leg.
- **Public-private intelligence partnership** — [[group-ib|Group-IB]] supplied intelligence and technical contribution that the Argentine release describes as "invaluable".
- **Bilateral diplomatic presence** — the Spanish Counsellor (Francisco Arenas Morales) participated in the Argentine press conference, suggesting embassy-level liaison support for the Spain–Argentina leg.
- **Informal cooperation channels** — see [[informal-cooperation]] for the broader pattern; no specific MLAT instrument is cited in the Argentine release.

## Challenges and Friction Points

The primary source does not enumerate friction points encountered during the operation. The cooperation architecture (EUROPOL + AMERIPOL + PAcCTO 2.0 + private-sector partner) is presented as having functioned smoothly. Implicit challenges that secondary-source coverage would need to address:

- Coordinating simultaneous searches across two continents and six legal systems on the same day (10 September 2024).
- Translating victim-count evidence drawn from the platform's own records into per-jurisdiction prosecutorial cases.
- Mapping iServer subscriber accounts ("desbloqueadores") to identifiable real-world offenders across six jurisdictions, of which only 17 arrests resulted from a 2,000+ subscriber population.

## Lessons Learned

- **PAcCTO 2.0 as a documented LATAM-side coordination instrument** — this operation is a worked example of how the EU-funded PAcCTO programme bridges EUROPOL and AMERIPOL for transnational cybercrime takedowns whose enforcement footprint sits primarily in Latin America. Argentina is named as the LATAM-side operational lead.
- **Phishing-as-a-service for stolen-device unlock as a discrete cybercrime supply chain** — the iServer model documents a niche in which a single SaaS administrator served 2,000+ downstream "unlocker" cybercriminals; the niche has its own Argentine-Spanish vocabulary ("desbloqueador") with no direct English equivalent in mainstream cybercrime literature.
- **Public-private intelligence template** — Group-IB's intelligence contribution is consistent with the EUROPOL-coordinated public-private template visible in [[carding-action-2020]] and other Group-IB-supported operations recorded in this wiki.

## Follow-Up Actions

The Argentine release advises Argentine victims to file complaints via line 134, the official complaints website, or by email, providing the IMEI of the stolen device. No information is provided on follow-up indictments, extraditions, or asset-recovery procedures in any of the six jurisdictions.

## Korean Involvement (한국의 참여)

None reported. Korea is not named in the primary source as a participating jurisdiction or as a victim jurisdiction. The "~193,500 victims in other countries" residual category in the iServer victim distribution is not broken down further in the primary source, and no Korean-language secondary coverage is ingested here.

## Contradictions & Open Questions

- **Per-country arrest split outside Argentina** — the primary source confirms 5 arrests in Argentina but does not report per-country splits for Spain, Colombia, Chile, Ecuador, or Peru. Cross-reference to Europol / Eurojust / national-jurisdiction releases is required.
- **Apex suspect identification** — the Argentine release identifies the platform administrator only by residency (Santa Fe Province, Argentina). Spanish-language secondary coverage names the suspect as Iván David Cudde, but that identification is not asserted from this primary record. A primary-source charging instrument would be required to record the name with confidence.
- **iServer infrastructure status** — the release describes the takedown at the actor / arrest level, not at the infrastructure level. Whether iServer servers, domains, or back-end administration components were seized is not stated.
- **Aggregate victim losses** — 483,000 victims are reported, but no aggregate monetary loss figure is provided.
- **MLAT vs informal channel distinction** — the release attributes coordination to EUROPOL, AMERIPOL, PAcCTO 2.0, and a public-private partnership, but does not specify whether any specific MLAT instrument was invoked for evidence transfer or extradition. The page conservatively classifies the cooperation as informal pending second-source verification.
