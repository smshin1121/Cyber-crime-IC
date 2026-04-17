---
type: case
title: "United States v. Ulbricht (Silk Road)"
case_number: "S1 14 Cr. 68 (KBF)"
jurisdiction: "U.S. District Court, Southern District of New York"
jurisdiction_country: "[[united-states]]"
case_type: prosecution
status: sentenced
crime_charged:
  - "[[online-fraud-ic]]"
defendants:
  - name: "Ross William Ulbricht"
    nationality: American
    status: pardoned
    sentence: "Life imprisonment (two concurrent life terms plus 40 years); pardoned 2025-01-21"
    location_at_arrest: "San Francisco, California"
  - name: "Gary Davis"
    nationality: Irish
    status: sentenced
    sentence: "78 months"
    location_at_arrest: Ireland
  - name: "Roger Thomas Clark"
    nationality: Canadian-Australian
    status: sentenced
    sentence: "20 years"
    location_at_arrest: Thailand
related_operation: "[[silk-road-takedown]]"
ic_elements:
  mlat_requests:
    - "Iceland (disputed — DOJ later acknowledged no formal MLAT)"
  extradition: "Gary Davis (Ireland to US, 2014-2018); Roger Thomas Clark (Thailand to US, 2015-2018)"
  evidence_from_abroad:
    - "Iceland (server image)"
  foreign_arrests:
    - "Ireland (Davis, 2014)"
    - "Thailand (Clark, 2015)"
  asset_freezing:
    []
cooperating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
legal_frameworks_invoked:
  - "[[mlat-process]]"
mechanisms_used:
  - "[[mlat-process]]"
key_legal_issues:
  - "[[data-sovereignty]]"
precedent_value: "Landmark — first life sentence for a cybercrime; established precedent for dark web marketplace prosecution, cryptocurrency seizure at scale, and cross-border digital evidence collection"
source_count: 2
sources:
  - "[[2015-05-29_sdny_us-v-ulbricht-sentencing]]"
  - "[[wired-operation-avalanche]]"
created: 2026-04-12
updated: 2026-04-12
summary: "United States v. Ulbricht is the landmark criminal prosecution of Ross William Ulbricht, creator and operator of the Silk Road dark web marketplace, in the Southern District of New York. Ulbricht was convicted on all seven counts on 4 February 2015 and sentenced to two concurrent life terms plus 40 years on 29 May 2015, with a forfeiture order of USD 183,961,921. At the time, this was *almost certainly* the most severe sentence ever imposed for a cybercrime."
---
## Summary

United States v. Ulbricht is the landmark criminal prosecution of Ross William Ulbricht, creator and operator of the Silk Road dark web marketplace, in the Southern District of New York. Ulbricht was convicted on all seven counts on 4 February 2015 and sentenced to two concurrent life terms plus 40 years on 29 May 2015, with a forfeiture order of USD 183,961,921. At the time, this was *almost certainly* the most severe sentence ever imposed for a cybercrime.

Ulbricht was pardoned by President Trump on 21 January 2025 after serving approximately 11 years.

## Facts

The Silk Road operated from approximately February 2011 to October 2013 as a Tor-hidden marketplace facilitating an estimated USD 1.2 billion in illegal transactions (primarily narcotics) using Bitcoin. The FBI arrested Ulbricht at the Glen Park Branch Library in San Francisco on 1 October 2013 while he was logged in as "Dread Pirate Roberts." The FBI seized approximately 173,991 BTC (~USD 33.6 million at the time).

## International Cooperation Elements

### Evidence Gathering

The FBI obtained a cloned image of the Silk Road server from Icelandic police. The server was hosted at a data center in Reykjavik. The legal basis for this cooperation is disputed: the government initially stated it had an MLAT with Iceland, but an assistant US attorney later acknowledged this was "not technically correct." The cooperation was *likely* based on informal police-to-police channels.

### Arrest and Extradition

- **Gary Davis** (alias "Libertas"), a Silk Road administrator, was arrested in Ireland in January 2014 and extradited to the US in July 2018 after fighting extradition for over four years. He was sentenced to 78 months in July 2019.
- **Roger Thomas Clark** (alias "Variety Jones"), Ulbricht's senior adviser, was arrested in Thailand in December 2015 and extradited to the US in June 2018. He was sentenced to 20 years in July 2023.

### Asset Recovery

Total cryptocurrency seized: ~173,991 BTC from initial seizures, plus ~69,370 BTC via 2020 civil forfeiture. Forfeiture order: USD 183,961,921.

## Legal Analysis

### Jurisdiction

The US asserted jurisdiction based on the criminal conduct's effects within the United States and the involvement of US-based infrastructure, despite the server being located in Iceland and the marketplace operating on the Tor network.

### Key Legal Issues

- **Server identification method**: The FBI's account of discovering the server IP via a misconfigured CAPTCHA has been disputed by security researchers.
- **MLAT with Iceland**: The government's initial misstatement about having an MLAT with Iceland raised evidentiary concerns, though the court found no grounds for suppression.
- **Corrupt investigators**: DEA Agent Carl Force and Secret Service Agent Shaun Bridges were convicted of stealing Bitcoin during the investigation, but the court found their misconduct did not affect Ulbricht's conviction.

### Precedent Value

**Landmark.** The case established precedents for: (1) life imprisonment for cybercrime; (2) large-scale cryptocurrency seizure; (3) cross-border dark web server identification and evidence collection; (4) the "successor marketplace" problem requiring sustained enforcement.

## Proceedings Timeline

| Date | Event |
|------|-------|
| 2013-10-01 | Ulbricht arrested in San Francisco |
| 2013-10-02 | Criminal complaint unsealed |
| 2014-02-04 | Superseding indictment (S1 14 Cr. 68) |
| 2015-01-13 | Trial begins (Judge Katherine B. Forrest) |
| 2015-02-04 | Guilty verdict on all seven counts |
| 2015-05-29 | Sentenced to life imprisonment; USD 183M forfeiture |
| 2017-05-31 | Second Circuit affirms conviction and sentence |
| 2018-07 | Gary Davis extradited from Ireland |
| 2019-07-19 | Davis sentenced to 78 months |
| 2023-07 | Roger Thomas Clark sentenced to 20 years |
| 2025-01-21 | Ulbricht pardoned by President Trump |

## Cooperation Effectiveness

The case demonstrated both strengths and limitations of pre-Budapest Convention international cooperation:

- **Strength**: Icelandic police cooperated rapidly and voluntarily with the FBI to provide server evidence.
- **Limitation**: The legal basis was ambiguous, creating potential evidentiary vulnerabilities.
- **Extradition**: Both the Davis (Ireland) and Clark (Thailand) extraditions ultimately succeeded but involved multi-year delays (4+ years for Davis).

## Korean Relevance (한국 관련성)

South Korea was not directly involved. However, the case is foundational precedent for Korean law enforcement's cryptocurrency tracing capabilities and dark web enforcement, including the Welcome to Video takedown (2019) where Korean authorities collaborated with IRS-CI using blockchain tracing techniques pioneered in the Silk Road investigation.

## Contradictions & Open Questions

1. The server identification method remains disputed (see [[silk-road-takedown]] for details).
2. The MLAT-with-Iceland misstatement has never been fully resolved in public filings.
3. Ulbricht's pardon does not affect the legal precedents but complicates the deterrence narrative.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | Ross Ulbricht Sentenced to Life in Prison | DOJ SDNY | 2015-05-29 | https://www.justice.gov/usao-sdny/pr/ross-ulbricht-aka-dread-pirate-roberts-sentenced-manhattan-federal-court-life-prison |
| 2 | Indictment PDF | DOJ SDNY | 2014-02-04 | https://www.justice.gov/sites/default/files/usao-sdny/legacy/2015/03/25/US%20v.%20Ross%20Ulbricht%20Indictment.pdf |
