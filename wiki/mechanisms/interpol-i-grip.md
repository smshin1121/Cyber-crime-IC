---
type: mechanism
title: "INTERPOL I-GRIP (Global Rapid Intervention of Payments)"
aliases:
  - I-GRIP
  - "Global Rapid Intervention of Payments"
  - "INTERPOL Anti-Money Laundering Rapid Response Protocol"
mechanism_type: information-sharing-platform
formality: semi-formal
legal_basis:
  - "INTERPOL Constitution Art. 2 (mutual assistance)"
  - "National anti-money laundering / proceeds of crime legislation"
administered_by: "[[interpol-igci]]"
participants:
  type: agencies
  count: 0
  notable_members:
    - "[[knpa-cyber-bureau]]"
    - "[[interpol-igci]]"
purpose: "A rapid payment interception mechanism that enables INTERPOL member countries to request the freezing or interception of fraudulently obtained funds as they move across borders through the banking system, before the funds are withdrawn or laundered beyond recovery."
speed: hours-days
scope:
  evidence_preservation: false
  evidence_production: false
  real_time_data: false
  subscriber_info: false
  content_data: false
  traffic_data: false
  arrest_coordination: false
  asset_tracing: true
  intelligence_sharing: true
limitations:
  - "Depends on speed of financial institution response — banking hours and processes vary"
  - "Limited to funds still in the banking system — cryptocurrency and cash withdrawals not covered"
  - "Requires rapid identification of recipient accounts and financial intermediaries"
  - "Effectiveness diminishes rapidly with time — funds must be intercepted before they are moved or withdrawn"
  - "No independent legal authority — relies on domestic laws in each country"
  - "Not all INTERPOL member countries have integrated I-GRIP into their NCB workflows"
operations_using:
  - "[[operation-haechi-v]]"
  - "[[operation-haechi-vi]]"
  - "[[operation-first-light-2024]]"
cases_using:
  []
related_mechanisms:
  - "[[mlat-process]]"
  - "[[24-7-network]]"
source_count: 2
sources:
  - "[[2024-06-18_interpol_operation-first-light-2024]]"
  - "[[2024-11-27_interpol-int-fr_operation-haechi-v-5500-arrests]]"
created: 2026-04-08
updated: 2026-04-29
status: active
---
## Summary

INTERPOL's I-GRIP framing is used in this corpus for rapid intervention against cyber-enabled financial crime, especially when funds can still be frozen, recalled, or traced shortly after a fraud event.

## Cooperation Use

The strongest linked examples are Operation First Light and HAECHI-series records. Those operations show a financial-disruption pattern: local reports and bank data identify fraud flows, INTERPOL coordination helps connect jurisdictions, and participating authorities move quickly to intercept proceeds or arrest suspects. The mechanism should be read as rapid operational coordination rather than a substitute for domestic seizure law.

## Boundary Notes

Use this page when the source explicitly emphasizes INTERPOL rapid intervention or financial recovery coordination. Use [[asset-freezing]] for legal restraint of funds, [[money-mule-networks]] for the cash-out layer, and [[public-private-cooperation]] when banks or payment platforms are the main cooperation channel.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2024-06-18_interpol_operation-first-light-2024|USD 257 million seized in global police crackdown against online scams - Operation First Light 2024]] | INTERPOL | 2024-06-18 | https://www.interpol.int/News-and-Events/News/2024/USD-257-million-seized-in-global-police-crackdown-against-online-scams |
| [2] | [[2024-11-27_interpol-int-fr_operation-haechi-v-5500-arrests|Une opération INTERPOL de lutte contre la criminalité financière aboutit à l'arrestation record de 5 500 personnes]] | INTERPOL | 2024-11-27 | https://www.interpol.int/fr/Actualites-et-evenements/Actualites/2024/INTERPOL-financial-crime-operation-makes-record-5-500-arrests-seizures-worth-over-USD-400-million |
