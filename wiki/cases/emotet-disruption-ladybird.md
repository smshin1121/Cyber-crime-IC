---
type: case
title: "Emotet Botnet Disruption — Operation LadyBird"
case_number: "M.D.N.C. (disruption order)"
jurisdiction: "U.S. District Court, Middle District of North Carolina (US component); Ukraine (criminal prosecution)"
jurisdiction_country: "[[united-states]]"
case_type: mutual-legal-assistance
status: arrested
crime_charged:
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
defendants:
  - name: "Two unnamed Ukrainian nationals"
    nationality: Ukrainian
    status: arrested
    sentence: "Up to 12 years (Ukrainian law)"
    location_at_arrest: "Kharkiv, Ukraine"
related_operation: "[[emotet-takedown]]"
ic_elements:
  mlat_requests:
    - Ukraine
    - Germany
    - Lithuania
    - Canada
  extradition: ""
  evidence_from_abroad:
    - Netherlands
    - Germany
    - "United Kingdom"
    - France
    - Lithuania
    - Canada
    - Ukraine
  foreign_arrests:
    - "Ukraine (2 suspects)"
  asset_freezing:
    []
cooperating_agencies:
  - "[[netherlands-politie]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[fbi-cyber-division]]"
  - "[[germany-bka]]"
legal_frameworks_invoked:
  - "[[budapest-convention]]"
  - "[[mutual-legal-assistance]]"
mechanisms_used:
  - "[[joint-investigation-team]]"
  - "[[24-7-network]]"
key_legal_issues:
  - "[[data-sovereignty]]"
  - "[[jurisdictional-conflicts]]"
precedent_value: "High — first large-scale law enforcement-controlled malware remediation (uninstall module deployed to infected machines worldwide via botnet's own update mechanism)"
source_count: 3
sources:
  - "[[2021-01-27_mdnc_emotet-disruption-order]]"
created: 2026-04-12
updated: 2026-04-26
summary: "The Emotet disruption (Operation LadyBird) was an internationally coordinated law enforcement action on 27 January 2021 to take down the Emotet botnet, described by Europol as \"the world's most dangerous malware.\" Eight countries participated: Netherlands, Germany, United States, United Kingdom, France, Lithuania, Canada, and Ukraine. The operation seized approximately 700 C2 servers and 2,000+ domains, arrested two suspects in Kharkiv, Ukraine, and — in a technically innovative move — deployed a law enforcement-controlled uninstall module to infected machines worldwide, activating on 25 April 2021."
---
## Summary

The Emotet disruption (Operation LadyBird) was an internationally coordinated law enforcement action on 27 January 2021 to take down the Emotet botnet, described by Europol as "the world's most dangerous malware." Eight countries participated: Netherlands, Germany, United States, United Kingdom, France, Lithuania, Canada, and Ukraine. The operation seized approximately 700 C2 servers and 2,000+ domains, arrested two suspects in Kharkiv, Ukraine, and — in a technically innovative move — deployed a law enforcement-controlled uninstall module to infected machines worldwide, activating on 25 April 2021.

The case is notable because the US component was a disruption order (not a named prosecution), while the Ukrainian component involved criminal arrests under domestic law.

## Facts

Emotet infected over 1.6 million computers worldwide between April 2020 and January 2021, with approximately 45,000 in the United States. The botnet served as a malware-as-a-service platform, providing initial access to Ryuk and Conti ransomware operators. A school district in the Middle District of North Carolina suffered USD 1.4 million in losses.

## International Cooperation Elements

### Joint Investigation Team

A JIT was established via [[eurojust|Eurojust]] enabling real-time evidence sharing between the Netherlands, Germany, and other EU participants.

### Multi-Country Infrastructure Seizure

- **Netherlands (NHTCU)**: Took control of Emotet infrastructure and deployed the uninstall module
- **Germany (BKA)**: Seized 17 C2 servers
- **Ukraine (Cyberpolice)**: Raided premises in Kharkiv, arrested 2 suspects
- **United Kingdom (NCA)**: Reported ~700 servers taken offline
- **United States (FBI)**: Obtained court-authorized disruption order in M.D.N.C.

### Victim Remediation

Dutch police recovered 4.3 million compromised email addresses and launched an online tool for victims to check exposure.

## Legal Analysis

### Jurisdiction

The US component relied on a court-authorized disruption order tied to infected machines and victim harm within the Middle District of North Carolina, while the arrests and many infrastructure actions were carried out under separate European and Ukrainian authorities.

### Key Legal Issues

- **Remote remediation authority:** The operation raised unusual questions about whether law enforcement can alter malware behavior on victim machines at global scale even for cleanup purposes.
- **Split enforcement model:** The case combines a US judicial disruption order with foreign criminal arrests, illustrating how botnet response can be legally fragmented across jurisdictions.

### Precedent Value

**High.** The deployment of a law enforcement-controlled update/uninstall module through the botnet's own infrastructure is *almost certainly* unprecedented in scale. This approach raised novel legal and ethical questions about law enforcement modifying software on private computers, even for remediation purposes.

## Proceedings Timeline

| Date | Event |
|------|-------|
| ~2019 | Investigation begins (Netherlands, Germany lead) |
| 2020 | JIT established via Eurojust |
| 2021-01-27 | Action day: ~700 servers and 2,000+ domains seized; 2 arrested in Ukraine |
| 2021-02-17 | Dutch police announce 4.3M compromised emails recovered |
| 2021-04-25 | Uninstall module activates; Emotet self-deletes from infected machines |
| 2021-11 | Emotet resurfaces via TrickBot infrastructure |

## Cooperation Effectiveness

The operation *almost certainly* represents one of the most effective multi-country botnet takedowns in history in terms of immediate impact. However, the **partial** outcome (Emotet resurfaced ~10 months later) demonstrates that infrastructure disruption without arresting all key operators provides only temporary relief.

## Korean Relevance (한국 관련성)

No Korean involvement identified.

## Contradictions & Open Questions

1. No named individuals were charged in US federal court — the US component was a disruption order, not a prosecution.
2. What happened to the two Ukrainian suspects? Were they convicted?
3. Emotet resurfaced in November 2021 — how were the operators able to rebuild?

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- US DOJ (OPA / M.D.N.C.), 2021-01-27: Emotet Botnet Disrupted in International Cyber Operation.

## Evidence and Attribution Notes

- On 27 January 2021, the Department of Justice announced the disruption of the Emotet botnet, described by Europol as "the world's most dangerous malware," in an internationally coordinated operation known as Operation LadyBird.
- Legal Action (US Component) The FBI obtained a court-authorized operation in the Middle District of North Carolina.
- Foreign law enforcement, working in collaboration with the FBI, replaced Emotet malware on servers in their jurisdictions with a law enforcement-created file designed to sever communication between infected computers and the botnet's operators.
- The remediation ran from approximately 25 January through 25 April 2021.

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | Emotet Botnet Disrupted in International Cyber Operation | DOJ OPA | 2021-01-27 | https://www.justice.gov/archives/opa/pr/emotet-botnet-disrupted-international-cyber-operation |
| 2 | Emotet Disruption (M.D.N.C.) | DOJ M.D.N.C. | 2021-01-27 | https://www.justice.gov/usao-mdnc/pr/emotet-botnet-disrupted-international-cyber-operation |
| 3 | Documents Related to Emotet Disruption | DOJ | 2021-01 | https://www.justice.gov/opa/documents-and-resources-related-disruption-emotet-malware-and-botnet |
