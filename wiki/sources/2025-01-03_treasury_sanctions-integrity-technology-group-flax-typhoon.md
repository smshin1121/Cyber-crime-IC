---
type: source
title: "Treasury Sanctions Technology Company for Support to Malicious Cyber Group (Integrity Technology Group / Flax Typhoon, OFAC, 3 January 2025)"
raw_path: "raw/press-releases/2025-01-03_treasury_sanctions-integrity-technology-group-flax-typhoon.md"
source_type: press-release
publisher: "U.S. Department of the Treasury — Office of Foreign Assets Control (OFAC)"
author: "U.S. Department of the Treasury, Office of Public Affairs"
publish_date: 2025-01-03
ingest_date: 2026-05-09
language: en
reliability: high
credibility: confirmed
sensitivity: public
pages_updated:
  - "[[treasury-integrity-technology-group-flax-typhoon-sanctions-2025]]"
key_findings:
  - "On 3 January 2025, OFAC designated Integrity Technology Group, Incorporated (Beijing-based) under Executive Order 13694 as amended by EO 13757 for its role in computer intrusion incidents attributed to Flax Typhoon (PRC state-sponsored, active since 2021)."
  - "Flax Typhoon used Integrity Tech infrastructure for network exploitation activities against multiple U.S. victims between summer 2022 and fall 2023; Flax Typhoon is described as targeting U.S. critical infrastructure sectors and operating against networks in North America, Europe, Africa, and Asia (particular focus on Taiwan)."
  - "The OFAC designation is a U.S. unilateral targeted sanction; no coordinated parallel sanctions by UK/Australia/Canada/New Zealand are documented in this release. The Five Eye reference applies only to the prior September 18, 2024 joint cybersecurity advisory (companion to the DOJ Raptor Train takedown)."
  - "This designation is the targeted-sanction companion to the DOJ court-authorized Raptor Train botnet disruption (Press Release 24-1173, September 18, 2024) — Treasury sanctioned the corporate entity behind Flax Typhoon approximately 3.5 months after DOJ disrupted its botnet infrastructure."
  - "Quoted official: Bradley T. Smith, Acting Under Secretary of the Treasury for Terrorism and Financial Intelligence."
created: 2026-05-09
---

# Source Summary — Treasury Sanctions Integrity Technology Group (Flax Typhoon), 3 January 2025

## What it is

U.S. Department of the Treasury Office of Foreign Assets Control (OFAC) press release **jy2769**, dated **3 January 2025**, announcing the designation of **Integrity Technology Group, Incorporated** (Beijing-based) under **Executive Order 13694** (cyber sanctions authority, April 2015) as amended by **EO 13757** (December 2016).

## Why it matters for IC

- This is the **targeted-sanction companion** to the DOJ court-authorized Raptor Train botnet disruption (DOJ Press Release 24-1173, 18 September 2024). It demonstrates the **U.S. multi-instrument response pattern** to PRC-contractor cyber operations: court-authorized infrastructure takedown (DOJ + FBI) + cybersecurity attribution (FVEY joint advisory) + targeted financial sanctions (Treasury OFAC), staged over ~3.5 months.
- It is a **unilateral U.S. action**, not a multilateral sanctions coordination — IC scope is borderline. Compare with the EU/UK coordinated Russia-cyber sanctions or the FVEY APT31 designations where parallel UK FCDO action was issued the same day. Here no parallel partner-state designation is documented.
- It establishes a precedent for **naming and freezing assets of a publicly-traded foreign cybersecurity contractor** assessed by the FBI as the entity behind a named state-sponsored APT (Flax Typhoon = Integrity Technology Group).

## Reliability & Credibility

- **Reliability: high** — official U.S. Treasury OFAC press release (tier-1 primary source); confirmed by three independent secondary mirrors (Alston & Bird, Industrial Cyber, GlobalSecurity.org) plus contemporaneous reporting (TechCrunch, Cybersecurity Dive, ASIS, MeriTalk).
- **Credibility: confirmed** — official designation announcement; legal effect (asset blocking) is binding on U.S. persons.
- **Sensitivity: public**.

## Fetch caveat (per LESSONS.md L11)

The primary URL `https://home.treasury.gov/news/press-releases/jy2769` returned WebFetch timeout during ingest. Body content was reconstructed from three independent secondary mirrors. The raw source file documents this reconstruction transparently. Primary fetch should be retried later for verbatim authoritative text capture.

## Notable Quote

> "The Treasury Department will not hesitate to hold malicious cyber actors and their enablers accountable for their actions."
> — Bradley T. Smith, Acting Under Secretary of the Treasury for Terrorism and Financial Intelligence (3 Jan 2025)

## Companion sources to ingest separately

- **DOJ Press Release 24-1173** (18 September 2024) — court-authorized Raptor Train takedown (already ingested as `[[2024-09-18_justice-gov_court-authorized-operation-disrupts-raptor-train-botnet-flax-typhoon]]`).
- **FBI / NSA / CNMF + AU/CA/NZ/UK Joint Cybersecurity Advisory** (18 September 2024) — TTPs and Integrity Tech support role for Flax Typhoon.
- **Lumen / Black Lotus Labs technical writeup** ("Derailing the Raptor Train") — independent telemetry and the >260,000-device peak figure.
