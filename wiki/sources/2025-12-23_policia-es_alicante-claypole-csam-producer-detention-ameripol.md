---
type: source
title: "Spanish National Police arrests CSAM producer in Alicante and triggers AMERIPOL-coordinated co-arrest in Claypole, Buenos Aires (Argentina)"
raw_path: raw/press-releases/2025-12-23_policia-es_alicante-claypole-csam-producer-detention-ameripol.md
source_type: press-release
publisher: "Policía Nacional (Spain) — Sala de Prensa"
author: "Policía Nacional — Oficina de Prensa"
publish_date: 2025-12-23
ingest_date: 2026-05-10
language: es
reliability: high
credibility: probably-true
sensitivity: public
pages_updated:
  - "[[spain-argentina-ameripol-claypole-csam-producer-takedown-2025]]"
key_findings:
  - "Spain–Argentina bilateral CSAM investigation — Policía Nacional (Spain) Unidad Central de Ciberdelincuencia + Brigada Provincial de Policía Judicial de Alicante led the Spanish leg, opening from an NCMEC CyberTipline lead, and arrested a man in Alicante province."
  - "Argentina leg led by the Dirección de Investigaciones Cibercrimen de la Policía de la Provincia de Buenos Aires, which identified, located, and arrested the second suspect in Claypole (Buenos Aires province) — described by Argentine investigators as 'one of the leaders of an international criminal organisation' producing, marketing, and distributing CSAM with operational branches across Europe and South America."
  - "International cooperation mechanism explicitly cited: AMERIPOL (Comunidad de Policías de América) acting through its specialised cybercrime centre AC3, with the Spanish National Police liaison officer at AC3 as the coordination contact point — a hemispheric police-cooperation channel rather than a formal MLAT or JIT."
  - "Pre-existing public-private cooperation channel cited: NCMEC (US-based National Center for Missing & Exploited Children) — Spanish investigators opened the case from NCMEC-tipped leads, not from a peer-LE referral."
  - "Two arrests: one in Alicante province (Spain), one in Claypole, Buenos Aires province (Argentina); the Argentine leg also produced a domiciliary search."
created: 2026-05-10
---

## Summary

Tier-1 primary press release from Spain's [[spanish-national-police|Policía Nacional]] (Sala de Prensa, official ID 16755), dated 2025-12-23, announcing a Spain–Argentina coordinated detention against an international CSAM-producer / CSAM-distributor cell. The Spanish leg, led by the Unidad Central de Ciberdelincuencia (UCC) with the Brigada Provincial de Policía Judicial de Alicante, opened from an NCMEC CyberTipline-style lead and arrested a man in Alicante province who used cloud storage and instant-messaging applications to store and exchange large volumes of CSAM. Forensic analysis of his devices identified a counterpart in Buenos Aires province, Argentina, allegedly producing newly-created CSAM of a minor he claimed personal access to.

Spain's UCC then activated the AMERIPOL international-cooperation mechanism via the Spanish National Police liaison officer at the AMERIPOL **Centro Especializado en Cibercrimen (AC3)**. Argentine police — specifically the **Dirección de Investigaciones Cibercrimen de la Policía de la Provincia de Buenos Aires** — identified, located, and arrested the suspect in the town of Claypole (Buenos Aires province), with a search of his residence. The press release frames the Argentine subject as one of the leaders of an international criminal organisation with operational branches in Europe and South America, of which the Alicante arrestee is alleged to be a member.

## L24 evidence — explicit foreign-LE counterpart naming

The Policía Nacional release explicitly names the foreign-LE partner agency, satisfying the L24 strict ≥2-country IC cooperation requirement:

> "Las autoridades policiales en Argentina iniciaron rápidamente una investigación que se desarrolló en el marco de la estrecha cooperación internacional entre la Policía Judicial de la policía Nacional de España y la Dirección de Investigaciones Cibercrimen de la Policía de la Provincia de Buenos Aires."

> "A través de los cauces internacionales, se contactó con el Oficial de enlace de la Policía Nacional Española en el Centro Especializado en Cibercrimen (AC3) en AMERIPOL, que es la Comunidad de Policías de América y el principal mecanismo de cooperación policial de ese hemisferio."

Foreign-LE counterpart jurisdictions and institutions explicitly named:
- Argentina — **Dirección de Investigaciones Cibercrimen de la Policía de la Provincia de Buenos Aires** (Buenos Aires Provincial Police Cybercrime Investigation Directorate)
- AMERIPOL — Comunidad de Policías de América, with its **AC3** specialised cybercrime centre as the police-to-police cooperation channel
- NCMEC — referenced as the upstream public-private intelligence pipeline that started the Spanish investigation

Per L24, the only operational-LE cooperation jurisdictions are Spain and Argentina; Europe-and-South-America "ramificaciones operativas" attributed to the criminal organisation are body-prose attribution only and not recorded as `participating_countries`.

## Verification status

- **Direct fetch:** `curl_cffi` chrome124 returned HTTP 200 with a 43 KB body containing the verbatim text quoted above (collection_url: https://www.policia.es/_es/comunicacion_prensa_detalle.php?ID=16755).
- **Cross-publisher sanity check:** The same operational facts (Alicante arrest, Claypole arrest, AMERIPOL coordination, Buenos Aires Provincial Police Cybercrime Directorate, NCMEC origin lead) are reproduced by Spain's Ministerio del Interior page and by Spanish secondary outlets (Infobae España 2025-12-23, Libertad Digital 2025-12-24, A24 / Diario de Vigo / Intercomarcal 2025-12-23/24) on or shortly after 2025-12-23; consistency is high.
- **Reliability/credibility:** national police agency press release naming specific foreign counterpart unit and intergovernmental coordination channel — defaulted to high/probably-true per CLAUDE.md source-reliability table for official-agency press releases.

## Relevance to IC

Adds the first explicit Spain–Argentina CSAM-investigation primary source to the wiki, with AMERIPOL/AC3 as the named cooperation channel — a hemispheric police-cooperation mechanism that is otherwise under-represented in the corpus (most existing Spain-led cybercrime ingests run via Europol or via bilateral US/EU partners). It also demonstrates the recurrent NCMEC → national LE → AMERIPOL → counterpart-country LE escalation pattern for transnational CSAM cases that span the Atlantic.
