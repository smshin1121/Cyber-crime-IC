---
type: procedure
title: "Extradition Request Procedure"
aliases:
  - Extradition
  - "범죄인 인도"
  - "International Extradition"
procedure_type: extradition-request
legal_basis:
  - "Bilateral extradition treaties"
  - "[[budapest-convention]] Art. 24"
  - "European Arrest Warrant (EU Council Framework Decision 2002/584/JHA)"
  - "UNTOC (Palermo Convention) Art. 16"
  - "Domestic extradition legislation"
mechanisms_involved:
  - "[[mlat-process]]"
  - "[[24-7-network]]"
typical_participants:
  requesting: "Requesting state: prosecution authority → central authority (Ministry of Justice/Foreign Affairs) → diplomatic channel"
  requested: "Requested state: diplomatic channel → central authority → judiciary → executive"
prerequisites:
  - "Valid arrest warrant or conviction in the requesting state"
  - "Extradition treaty or other legal basis between the two states"
  - "Dual criminality — the offense must be criminal in both states (with exceptions)"
  - "The offense must meet the minimum severity threshold (typically 1+ year imprisonment)"
  - "The person must be located in the requested state's territory"
  - "No applicable bars to extradition (political offense, nationality, double jeopardy, death penalty risk)"
average_duration: "6-24 months"
steps:
  - step: 1
    actor: "Requesting state prosecution authority"
    action: "Prepare extradition request package: diplomatic note, arrest warrant, statement of facts, applicable law, evidence of identity, assurances (if needed)"
    documents:
      - "Diplomatic note"
      - "Certified copy of arrest warrant or judgment"
      - "Statement of the offense and applicable law"
      - "\"Evidence of identity (photos"
      - "fingerprints)\""
      - "\"Assurances regarding specialty"
      - "death penalty"
      - "or detention conditions (if required)\""
    notes: "Document requirements vary significantly by treaty and requested state. Translation into the requested state's language is typically required."
  - step: 2
    actor: "Requesting state central authority"
    action: "Review the request for completeness and legal sufficiency, then transmit through diplomatic channel to the requested state"
    documents:
      - "Formal extradition request with all supporting documents"
    notes: "Central authority is typically the Ministry of Justice (법무부 in Korea) or Attorney General's office. Some bilateral treaties allow direct authority-to-authority transmission."
  - step: 3
    actor: "Requested state central authority"
    action: "Receive the request, review for formal compliance with treaty requirements, and transmit to the competent judicial authority"
    documents:
      []
    notes: "Central authority screens for basic legal sufficiency. Some states (US, UK) have extensive central authority review; others route quickly to courts."
  - step: 4
    actor: "Requested state judiciary"
    action: "Conduct judicial hearing: review dual criminality, identity, treaty compliance, bars to extradition, human rights considerations. The fugitive has the right to legal representation and to contest extradition."
    documents:
      - "Judicial extradition order or decision"
    notes: "Judicial review varies significantly: common law systems (US, UK) hold adversarial hearings; civil law systems (Germany, France, Korea) may involve a different procedural format. Human rights review (ECHR Art. 3 in Europe) is increasingly important."
  - step: 5
    actor: "Requested state executive authority"
    action: "Ministerial decision on whether to surrender the person. In many systems, the executive has final discretion even after judicial approval."
    documents:
      - "Executive surrender order"
    notes: "In some systems (Korea: 법무부장관 결정), the executive can refuse extradition on policy grounds even after judicial approval. In others (UK), the Home Secretary's role is more limited after judicial approval. In EU EAW cases, there is no executive stage."
  - step: 6
    actor: "Both states"
    action: "Physical surrender: coordinate transfer logistics, including escort, transportation, and documentation. The person is transferred to custody of the requesting state."
    documents:
      - "Surrender documentation"
      - "Transfer of custody records"
    notes: "The rule of specialty applies: the requesting state may only prosecute for the offenses specified in the extradition request (unless the requested state consents to additional charges)."
success_factors:
  - "Strong bilateral extradition treaty with clear terms"
  - "Early engagement with the requested state through diplomatic and LEA channels"
  - "Complete and well-prepared request package (reduces back-and-forth)"
  - "Provisional arrest (if available under the treaty) to prevent flight while the full request is prepared"
  - "Effective legal representation in the requested state to anticipate and address objections"
  - "Political will and diplomatic cooperation"
common_pitfalls:
  - "Incomplete or poorly translated documentation — causes delays of months for supplementation"
  - "Dual criminality failure — the offense is not criminal in the requested state (particularly for newer cyber offenses)"
  - "Nationality bar — many civil law countries (Germany, Japan, Korea) do not extradite their own nationals"
  - "Political offense exception — rarely applies to cybercrime but may be raised"
  - "Human rights challenges — claims of unfair trial, torture risk, or disproportionate sentencing in the requesting state"
  - "Competing extradition requests from multiple states"
  - "Fugitive flight during prolonged proceedings"
  - "Death penalty bar — many states refuse extradition unless the requesting state provides assurances that the death penalty will not be imposed"
template_available: false
related_procedures:
  - "[[emergency-data-preservation]]"
source_count: 2
sources:
  - "[[2026-04-29_congress-gov_korea-us-mlat-treaty-document-104-1]]"
  - "[[2024-11-18_bleepingcomputer_us-charges-phobos-ransomware-admin-after-south-korea-extradition]]"
created: 2026-04-08
updated: 2026-04-29
status: active
---
## Summary

An extradition request is the formal procedure by which one state asks another to arrest and surrender a person for prosecution or sentence enforcement. In cybercrime, extradition is often the step that turns a public indictment into a case that can actually proceed in the charging court.

## Cooperation Use

The request must usually identify charges, facts, identity, treaty basis, and supporting judicial material. Practical issues include provisional arrest, dual criminality, nationality restrictions, specialty, human-rights objections, and local litigation. Cybercrime cases add timing pressure because suspects may move between jurisdictions and because digital evidence can be handled separately from custody.

## Boundary Notes

Use this procedure page for the request workflow. Use [[extradition]] for the broader cooperation mechanism, [[dual-criminality]] for offense matching, and [[specialty-principle]] for limits on prosecuting a surrendered person beyond the extradited offenses.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2026-04-29_congress-gov_korea-us-mlat-treaty-document-104-1|Treaty with the Republic of Korea on Mutual Legal Assistance in Criminal Matters]] | Congress.gov | 1995-01-12 | https://www.congress.gov/treaty-document/104th-congress/1/document-text |
| [2] | [[2024-11-18_bleepingcomputer_us-charges-phobos-ransomware-admin-after-south-korea-extradition|US charges Phobos ransomware admin after South Korea extradition]] | BleepingComputer | 2024-11-18 | https://www.bleepingcomputer.com/news/security/us-charges-phobos-ransomware-admin-after-south-korea-extradition/ |
