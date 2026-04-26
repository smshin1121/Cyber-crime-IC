---
type: case
title: "xDedic 2024 Prosecution Roundup Case Wrapper"
case_number: "xDedic 2024 roundup compatibility record"
jurisdiction: "U.S. District Court, Middle District of Florida"
jurisdiction_country: "[[united-states]]"
case_type: prosecution
status: absorbed
crime_charged:
  - "[[cybercrime-forum-ic]]"
  - "[[online-fraud-ic]]"
  - "[[identity-theft]]"
  - "[[ransomware-ic]]"
defendants:

related_operation: "[[xdedic-marketplace-takedown]]"
ic_elements:
  mlat_requests:

  extradition: ""
  evidence_from_abroad:

  foreign_arrests:

  asset_freezing:

cooperating_agencies:
  - "[[us-doj]]"
legal_frameworks_invoked:
  - "[[informal-cooperation]]"
mechanisms_used:
  - "[[informal-cooperation]]"
key_legal_issues:
  - "[[online-fraud-ic]]"
precedent_value: "Source-derived official action page; procedural enrichment from primary filings may still be needed."
source_count: 1
sources:
  - "[[2024-01-04_justice-gov_19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-th]]"
created: 2026-04-18
updated: 2026-04-26
summary: "Absorbed case wrapper for the January 2024 xDedic prosecution roundup. The substantive umbrella record is [[xdedic-marketplace-takedown]], and defendant-specific cases are maintained on their individual case pages."
aliases:
  - "19 Individuals Worldwide Charged In Transnational Cybercrime Investigation Of The xDedic Marketplace"
  - "19 Individuals Worldwide Charged In Transnational Cybercrime Investigation Of The xDedic Marketplace"
---
## Summary

This page is not an independent criminal case. It is an absorbed compatibility wrapper created from the January 2024 DOJ xDedic roundup title. The substantive umbrella operation is [[xdedic-marketplace-takedown]], while individual prosecutions are maintained on defendant-specific case pages such as [[us-v-habasescu-xdedic]], [[us-v-pankov-xdedic]], [[us-v-levinson-xdedic]], [[us-v-mcneely-xdedic]], and [[us-v-omotosho-xdedic]].

The DOJ roundup is still important evidence. It explains that xDedic sold access credentials and PII tied to compromised servers worldwide, that the marketplace listed more than 700,000 compromised servers, and that buyers used those resources for tax fraud, identity-theft fraud, ransomware-enabling access, and other illegal activity. It also ties the 2019 infrastructure seizure to later extraditions, convictions, and sentencings.

## Scope

- Canonical operation: [[xdedic-marketplace-takedown]]
- Purpose: preserve generated links without presenting the roundup title as a separate defendant case
- Source treatment: cite the DOJ roundup once and avoid multiplying identical source URLs across generated case wrappers
- Case modeling rule: individual defendants should be represented by their own case pages, not by title-derived placeholder defendant names

## Corrected Modeling

The original generated page treated words from the press-release title as defendant names and described the page as a metadata placeholder. That was incorrect. The DOJ source is a prosecution roundup for the xDedic enforcement set, not a standalone case caption. The correct model is an umbrella operation with separate defendant-specific case pages and absorbed compatibility wrappers for older generated links.

## Source Deduplication

This wrapper intentionally uses one canonical source. Earlier records produced multiple source pages with the same DOJ URL, which made reference tables look more authoritative than they were. Those repeated source URLs belong in the duplicate-source audit, while this wrapper should remain a single-reference compatibility page.


## Case Note

This wrapper should not be used to count an additional defendant, additional indictment, or additional prosecution beyond the xDedic umbrella set. It exists because earlier automation created case pages from a press-release headline. The corrected data model keeps the factual prosecution details in defendant-specific records and uses this page only to prevent broken links while preserving the audit trail of the cleanup.


## Modeling Boundary

The January 2024 roundup is best treated as a source for the umbrella operation because it aggregates many defendants and procedural outcomes. When the same headline is modeled as a case page, it can inflate the case count and make it appear that there is a separate prosecution named after the press release. This corrected wrapper prevents that: it keeps one source citation, points readers to the umbrella operation, and leaves defendant-level facts to the actual case records. The case wrapper also records why the duplicate exists, so future cleanup can merge or redirect it without reintroducing title-derived defendant names or repeated references. It should not be counted as an additional prosecution outcome in quantitative analysis.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| 1 | 19 Individuals Worldwide Charged In Transnational Cybercrime Investigation Of The xDedic Marketplace | US DOJ (Middle District of Florida) | 2024-01-04 | https://www.justice.gov/usao-mdfl/pr/19-individuals-worldwide-charged-transnational-cybercrime-investigation-xdedic |