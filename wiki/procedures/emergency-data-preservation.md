---
type: procedure
title: "Emergency Data Preservation Request (Budapest Convention Art. 29)"
aliases:
  - "Art. 29 Preservation Request"
  - "Expedited Preservation"
  - "긴급 데이터 보전 요청"
procedure_type: evidence-preservation
legal_basis:
  - "[[budapest-convention]] Art. 29"
  - "[[budapest-convention]] Art. 30 (expedited disclosure of preserved traffic data)"
mechanisms_involved:
  - "[[24-7-network]]"
typical_participants:
  requesting: "Law enforcement investigator/prosecutor in requesting state"
  requested: "24/7 Network contact point in requested state → domestic ISP/service provider"
prerequisites:
  - "Both states must be parties to the Budapest Convention (or have bilateral arrangement)"
  - "Requesting state has ongoing criminal investigation involving electronic evidence"
  - "Data at risk of deletion, modification, or loss (urgency must be demonstrated)"
  - "Requesting state must intend to submit a formal MLA request for production within the preservation period"
average_duration: "24-72 hours (initial preservation action); 60-day preservation hold (renewable)"
steps:
  - step: 1
    actor: "Investigating officer/prosecutor"
    action: "Identify at-risk electronic evidence stored in a foreign jurisdiction — e.g., server logs, email content, subscriber data held by a foreign ISP"
    documents:
      []
    notes: "Time-critical: data retention periods vary; some providers delete logs within days"
  - step: 2
    actor: "Investigating officer"
    action: "Contact the national 24/7 contact point designated under Budapest Convention Art. 35"
    documents:
      - "Art. 29 preservation request form (if available)"
      - "Summary of investigation"
      - "Description of data to be preserved"
    notes: "In Korea, the 24/7 contact point is designated within the Supreme Prosecutors' Office (대검찰청) / KNPA (경찰청)"
  - step: 3
    actor: "National 24/7 contact point (requesting state)"
    action: "Transmit the preservation request to the 24/7 contact point of the state where data is stored, via the 24/7 Network (secure channels)"
    documents:
      - "\"Art. 29 request specifying: authority requesting"
      - "offense under investigation"
      - "data to be preserved"
      - "connection between data and offense"
      - "necessity and urgency\""
    notes: "Art. 29(2) requires: identity of requesting authority; offense summary; data description; necessity showing"
  - step: 4
    actor: "24/7 contact point (requested state)"
    action: "Receive the request and route it to the competent domestic authority for execution"
    documents:
      []
    notes: "The requested state must take measures under its domestic law to preserve the specified data"
  - step: 5
    actor: "Domestic authority (requested state)"
    action: "Execute a domestic preservation order against the service provider holding the data — provider must preserve the specified data for at least 60 days"
    documents:
      - "Domestic preservation order (form varies by jurisdiction)"
    notes: "Art. 29(7): preservation shall be for at least 60 days, to permit the requesting state to submit a formal MLA request. Dual criminality may NOT be required for preservation (Art. 29(4))"
  - step: 6
    actor: "24/7 contact point (requested state)"
    action: "Confirm preservation to the requesting state's 24/7 contact point, including any conditions or partial refusals"
    documents:
      - "Confirmation communication"
    notes: "Confirmation should be provided within hours where possible. Art. 29(5) allows refusal only if preservation is not possible under domestic law, or if the request relates to a political or military offense"
  - step: 7
    actor: "Requesting state"
    action: "Submit a formal MLA request (through MLAT or Budapest Convention Art. 31) for production of the preserved data within the 60-day preservation period"
    documents:
      - "Formal MLA request"
      - "Supporting documents required by requested state"
    notes: "Failure to submit MLA within 60 days may result in the preservation being lifted. See [[mlat-process]] for MLA procedure"
success_factors:
  - "Speed of initial identification and request submission — delay reduces preservation value"
  - "Quality and specificity of the preservation request — vague requests may be refused"
  - "24/7 contact point responsiveness in both states"
  - "Strong working relationships between 24/7 contact points"
  - "Timely follow-up with formal MLA request within the 60-day window"
common_pitfalls:
  - "Overly broad preservation requests that are rejected for lack of specificity"
  - "Failure to submit formal MLA request within the 60-day preservation period"
  - "Inadequate description of the urgency or connection between data and investigation"
  - "Requesting data from a non-Budapest party (Art. 29 only applies between parties)"
  - "Confusing preservation (Art. 29) with production (Art. 31) — preservation does NOT provide access to the data, only prevents its deletion"
  - "Insufficient domestic legal authority in the requested state for emergency preservation"
template_available: false
related_procedures:
  - "[[extradition-request]]"
source_count: 3
sources:
  - "[[2026-04-17_coe-int_about-the-convention-budapest-convention]]"
  - "[[2022-05-12_coe-int_second-additional-protocol-cets-no-224]]"
  - "[[2026-04-29_justice-gov_cloud-act-executive-agreements]]"
created: 2026-04-08
updated: 2026-04-29
status: active
---
## Summary

Emergency data preservation is the procedure used to prevent volatile electronic evidence from being deleted, overwritten, or moved before investigators can obtain it through the proper legal channel.

## Cooperation Use

Preservation is not the same as disclosure. A preservation request or order keeps data available while investigators prepare a domestic warrant, production order, MLAT request, executive-agreement request, or other lawful access process. In cross-border cases, preservation can be decisive because logs, subscriber records, cloud data, and transaction traces may have short retention periods.

## Boundary Notes

Use this page for preservation steps. Use [[electronic-evidence]] for the evidence category, [[24-7-network]] for urgent contact routing, [[mlat-process]] for formal evidence transfer, and [[cloud-act]] or [[us-uk-cloud-act-agreement]] where the source concerns a specific provider-data access framework.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2026-04-17_coe-int_about-the-convention-budapest-convention|About the Convention — Budapest Convention]] | Council of Europe | 2026-04-17 | https://www.coe.int/en/web/cybercrime/the-budapest-convention |
| [2] | [[2022-05-12_coe-int_second-additional-protocol-cets-no-224|Second Additional Protocol (CETS No. 224)]] | Council of Europe | 2022-05-12 | https://www.coe.int/en/web/cybercrime/second-additional-protocol |
| [3] | [[2026-04-29_justice-gov_cloud-act-executive-agreements|Regarding CLOUD Act Executive Agreements]] | U.S. Department of Justice | 2023-10-01 | https://www.justice.gov/es/node/1397306 |
