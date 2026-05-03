---
type: analysis
title: "Project Goal and Success Criteria"
analysis_type: methodology
scope: "Project-wide research direction and operating quality gates for the cybercrime international-cooperation wiki"
confidence: high
key_judgments:
  - judgment: "The project should optimize for a verified, cooperation-centered research corpus rather than raw page growth."
    confidence: high
  - judgment: "The canonical operation corpus and absorbed follow-on records must remain analytically separate to avoid double-counting in SNA outputs."
    confidence: high
  - judgment: "Tiered source verification and explicit uncertainty notes are required before country or agency participation claims are used as network edges."
    confidence: high
sources_consulted: 5
entities_referenced:
  - "[[ic-statistics-dashboard]]"
  - "[[sna-pilot]]"
  - "[[sna-structure-and-roles]]"
generated_from: manual
query_prompt: "goal set"
created: 2026-05-03
updated: 2026-05-03
---

# Project Goal and Success Criteria

## Core Goal

The project goal is to build a source-grounded, SNA-ready knowledge base on public international cooperation against cybercrime.

The central question is not "who attacked whom." The central question is how states, law-enforcement agencies, prosecutors, courts, international organizations, and private partners cooperate across borders to investigate, disrupt, seize infrastructure, arrest suspects, extradite defendants, preserve evidence, recover assets, and prosecute cybercrime.

This goal is *high confidence* because it is consistent with the repository's operating instructions, the current overview page, the SNA analysis pages, and the data-collection plan.

## Research Scope

The core dataset should prioritize officially verifiable operation and case records from 2015 through 2025. Boundary records from 2014 and 2026 may remain in the wiki when they clarify continuity, follow-on prosecution, current legal status, or context for the main period. They should be labeled carefully in analytical exports so that period-based conclusions do not mix core observations with contextual records.

The unit of analysis is a public operation or case with:

- a cybercrime nexus;
- participation by at least two countries, law-enforcement bodies, judicial authorities, international organizations, or private-sector partners;
- a concrete enforcement action such as arrest, indictment, takedown, infrastructure seizure, asset seizure, extradition, or coordinated disruption;
- enough source detail to code at least two analytical variables.

## Success Criteria

The wiki is successful when it can support reproducible answers to these questions:

1. Which countries and agencies cooperate most frequently, and through which coordinating bodies?
2. Which mechanisms appear in practice: MLAT, 24/7 preservation, JITs, direct provider requests, informal police cooperation, extradition, or asset-freezing channels?
3. Which crime types generate the widest international networks?
4. Which operations produce arrests, seizures, takedowns, extraditions, or prosecutions, and which stop at disruption?
5. How do Europol, Eurojust, INTERPOL, DOJ-led, Korea-led, and regional African cooperation models differ?
6. Where does the public record understate cooperation because of sealed proceedings, intelligence activity, non-English reporting gaps, or non-public MLAT practice?

## Quality Gates

The project should be treated as analytically ready only when the automated checks remain clean:

- `python tools/lint.py`: 0 critical/high issues.
- `python tools/check_links.py`: 0 broken and 0 malformed links.
- `python tools/audit_integrity.py`: 0 parse errors, 0 broken wikilinks, and 0 source mismatches.
- `python tools/audit_operation_consistency.py`: 0 issues.
- `python tools/audit_content_depth.py`: 0 high-priority pages, 0 source-rich thin pages, 0 placeholder-language pages, and 0 probable crime-type mismatch flags.
- `python tools/audit_source_duplicates.py --date YYYY-MM-DD`: 0 active duplicate URL groups and 0 active duplicate content-hash groups.
- Static docs contain no unresolved translation-placeholder residue.

## Near-Term Priorities

1. Stabilize the canonical operation corpus and keep absorbed follow-on records out of operation counts.
2. Strengthen low-source canonical operations with official releases, court documents, and source pages.
3. Verify participating-country and participating-agency rosters against official or high-reliability sources before treating them as SNA edges.
4. Normalize duplicate sources into canonical source pages with explicit alias metadata.
5. File reusable findings into `wiki/analysis/` rather than leaving them only in chat history.
6. Keep Korea-relevant cooperation visible while avoiding unsupported inflation of Korea's role.

## Non-Goals

The project should not become a page-count exercise, a general cyber threat-intelligence database, or a warehouse of thin pages. New material should usually strengthen existing explanations, source coverage, cross-links, and analysis before creating new standalone pages.

## Interpretation Rule

When goals conflict, source integrity wins. It is better to have a smaller canonical corpus with explicit uncertainty than a larger network graph with unsupported country, agency, or mechanism edges.
