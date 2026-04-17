---
type: case
title: "United States v. Gallyamov (QakBot)"
case_number: "C.D. Cal. (sealed)"
jurisdiction: "U.S. District Court, Central District of California"
jurisdiction_country: "[[united-states]]"
case_type: "prosecution"
status: "indicted"
crime_charged:
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
defendants:
  - name: "Rustam Rafailevich Gallyamov"
    nationality: "Russian"
    status: "indicted"
    sentence: ""
    location_at_arrest: "At large (Moscow, Russia)"
related_operation: "[[qakbot-gallyamov-indictment]]"
ic_elements:
  mlat_requests: []
  extradition: ""
  evidence_from_abroad:
    - "France"
    - "Germany"
    - "Netherlands"
    - "Denmark"
    - "United Kingdom"
    - "Canada"
  foreign_arrests: []
  asset_freezing:
    - "USD 24 million+ cryptocurrency (civil forfeiture)"
cooperating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[europol-ec3]]"
  - "[[us-doj]]"
legal_frameworks_invoked:
  - "[[mutual-legal-assistance]]"
mechanisms_used:
  - "[[mutual-legal-assistance]]"
  - "[[informal-cooperation]]"
key_legal_issues:
  - "[[data-sovereignty]]"
  - "[[jurisdictional-conflicts]]"
precedent_value: "Medium — demonstrates continued prosecution despite prior botnet takedown; large-scale cryptocurrency forfeiture"
source_count: 1
sources:
  - "[[2025-05-22_cdca_qakbot-gallyamov-indictment]]"
created: 2026-04-12
updated: 2026-04-12
---

## Summary

United States v. Gallyamov is the indictment of Rustam Rafailevich Gallyamov, 48, of Moscow, Russia, for leading the QakBot malware conspiracy since 2008. The indictment was unsealed on 22 May 2025 in conjunction with Operation Endgame. Gallyamov allegedly used QakBot to build a botnet providing initial access to ransomware operators deploying ProLock, DopplePaymer, Egregor, REvil, Conti, Name Locker, Black Basta, and Cactus.

Despite the FBI's August 2023 QakBot botnet takedown (which redirected traffic and removed malware from approximately 700,000 infected computers), Gallyamov allegedly continued criminal activity through January 2025.

## Facts

QakBot (QBot/Pinkslipbot) is one of the longest-running malware families, active since 2008. It evolved from a banking trojan to a major initial-access-as-a-service platform. The DOJ filed a civil forfeiture complaint against USD 24 million+ in cryptocurrency connected to Gallyamov's operations.

## International Cooperation Elements

### Multinational Investigation

The indictment resulted from cooperation among the US, France, Germany, Netherlands, Denmark, United Kingdom, and Canada, with Europol providing coordination. This was part of the broader Operation Endgame framework.

### Asset Recovery

USD 24 million+ in cryptocurrency was seized via civil forfeiture, plus approximately USD 4 million in additional Bitcoin and USDT tokens.

## Legal Analysis

### Jurisdiction

The Central District of California appears to ground jurisdiction in the use of QakBot against US victims and in the malware's role in ransomware campaigns that touched US systems, financial channels, and investigative infrastructure.

### Key Legal Issues

- **Persistence after disruption:** The case tests how prosecutors frame liability when a botnet operator allegedly continues activity after a major law-enforcement disruption.
- **Operator-at-large prosecution:** It also highlights the practical limit of indictments against defendants who remain in Russia and outside realistic extradition reach.

### Precedent Value

**Medium to High.** The case links botnet disruption, asset forfeiture, and a later operator-focused indictment into a single enforcement arc rather than treating takedown activity as the endpoint.

## Proceedings Timeline

| Date | Event |
|------|-------|
| 2008 | QakBot malware first appears |
| 2023-08 | FBI disrupts QakBot botnet; 700,000 computers cleaned |
| 2025-01 | Gallyamov allegedly continues activity through this date |
| 2025-05-22 | Indictment unsealed in C.D. Cal. |
| 2025-05-22 | Civil forfeiture complaint filed for USD 24M+ |

## Cooperation Effectiveness

The case demonstrates that botnet takedowns alone are insufficient to stop determined operators. Gallyamov's continued activity after the 2023 takedown underscores the need for sustained legal pressure, even when arrest is not immediately feasible.

## Korean Relevance (한국 관련성)

No Korean involvement identified.

## Contradictions & Open Questions

1. Will Gallyamov ever be apprehended given his location in Russia?
2. What is the total financial impact of QakBot-facilitated ransomware attacks?
3. How effective was the August 2023 takedown if criminal activity continued for 17+ months?

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | Leader of QakBot Malware Conspiracy Indicted | DOJ OPA | 2025-05-22 | https://www.justice.gov/opa/pr/leader-qakbot-malware-conspiracy-indicted-involvement-global-ransomware-scheme |
