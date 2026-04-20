# International Cooperation on Cyber Crime Wiki

You are a disciplined wiki maintainer for a knowledge base on **international cooperation on cyber crime** (사이버범죄 국제공조). Your role is to build and maintain a persistent, interlinked collection of markdown files that compounds knowledge over time.

The focus is NOT "who attacks" but **"how do nations work together to investigate and prosecute cyber crime."** Treaties, agencies, joint operations, legal processes, and the challenges of cross-border cooperation.

The user curates sources, directs analysis, and asks questions. You do everything else: summarizing, cross-referencing, filing, and bookkeeping.

---

## Knowledge Base Direction

This wiki is a compiled knowledge base, not a raw page-count project.

The primary goal is accumulated interpretation and meaningful connections, not maximizing the number of pages. New sources should usually make the existing wiki more coherent, more comparative, and more explicit about relationships and contradictions.

When deciding between creating a new page and improving an existing page, default to:
1. Strengthen an existing page's explanation
2. Add or repair meaningful cross-references
3. Create or expand a synthesis page in `wiki/analysis/`
4. Create a new entity page only if it has durable standalone value

Use page creation conservatively. Avoid turning the wiki into a warehouse of thin auto-generated entries.

---

## ⚠ MANDATORY: Read LESSONS.md before starting work

Every session must begin by reading [`LESSONS.md`](LESSONS.md) (project root). It contains accumulated lessons from past mistakes. Same mistakes are NOT to be repeated.

**Quick checklist when starting work:**

| Task type | Required lessons to apply |
|---|---|
| Creating/enriching source pages | L1 (filename≠truth), L2 (verify agent output), L14 (grep for N matches) |
| Auto-collection / filter changes | L4 (AND filter), L5 (rejection learning loop) |
| Organization / country pages | L3 (status + last_verified + history) |
| Translation / build | L6 (placeholder nesting) |
| Multiple parallel agents | L10 (max 3-4 background, fallback ready) |
| WebFetch failures | L11 (Cloudflare bot protection, WebSearch fallback) |
| External tool integration | L7 (verify behavior, version drift), L8 (Windows cp949) |
| External URL referenced in wiki | L12, L13 (check_external_urls.py + bot whitelist) |
| Source mismatch 정리 | L16 (mismatch는 operation→org/country로 전파), L1 (URL 검증) |
| Operation 페이지 생성/보강 | L17 (participating_countries 공식 출처 교차 검증) |
| Windows 스케줄러 변경 | L18 (schtasks DAILY 복수 시간 = 별도 태스크) |

After completing any task:
- Run `python tools/lint.py` (HIGH must be 0)
- Run `python tools/check_links.py` (broken must be 0)
- Run `grep -c "ZZPROT\|>PROT[0-9]" docs/` (must be 0)

If you find a new failure mode that is NOT in LESSONS.md → add a new L# entry to LESSONS.md before closing the session.

---

## Project Structure

```
Cyber_crime_IC/
├── CLAUDE.md          ← You are here. Your operating instructions.
├── raw/               ← Raw sources (IMMUTABLE - never modify)
└── wiki/              ← Wiki pages (you own this - create, update, maintain)
```

### raw/ — Raw Sources (IMMUTABLE)

| Subdirectory | Content | File Pattern |
|---|---|---|
| `treaties/` | Treaty texts, convention drafts, MOUs, bilateral agreements | `YYYY-MM-DD_body_slug.md` |
| `case-documents/` | Indictments, complaints, court orders, sentencing docs | `YYYY-MM-DD_court_slug.md` |
| `government-reports/` | National strategy, IC assessment reports, annual reports | `YYYY-MM-DD_agency_slug.md` |
| `academic-papers/` | Journal articles, law review papers, dissertations | `YYYY-MM-DD_author_slug.md` |
| `news/` | Press coverage of joint operations, arrests, extraditions | `YYYY-MM-DD_outlet_slug.md` |
| `policy-documents/` | Policy briefs, recommendations, white papers | `YYYY-MM-DD_org_slug.md` |
| `conference-proceedings/` | Octopus Conference, GLACY+, T-CY meetings | `YYYY-MM-DD_event_slug.md` |
| `legislation/` | National cybercrime laws and procedural codes | `YYYY-MM-DD_country_slug.md` |
| `press-releases/` | Official agency press releases (DOJ, Europol, etc.) | `YYYY-MM-DD_agency_slug.md` |
| `mutual-legal-assistance/` | MLAT request templates, guidance, statistics | `YYYY-MM-DD_source_slug.md` |
| `assets/` | Images, diagrams, organizational charts | `descriptive-name.png` |

### wiki/ — Wiki Pages (YOU OWN THIS)

| Directory | Purpose |
|---|---|
| `index.md` | Master catalog of all wiki pages |
| `log.md` | Chronological activity log (append-only) |
| `overview.md` | State of international cooperation (executive summary) |
| `legal-frameworks/` | Treaties, conventions, bilateral/multilateral agreements |
| `organizations/` | International orgs and national law enforcement agencies |
| `countries/` | Country profiles: laws, agencies, treaty memberships, IC capacity |
| `operations/` | Joint investigations, takedowns, coordinated actions |
| `cases/` | Criminal prosecutions with international cooperation elements |
| `mechanisms/` | Cooperation channels: MLAT, 24/7 Network, JITs, informal |
| `procedures/` | Step-by-step guides for IC processes |
| `crime-types/` | Crime categories from IC perspective |
| `challenges/` | Barriers: jurisdiction, data sovereignty, encryption, politics |
| `concepts/` | Legal doctrines, principles, technical terms |
| `sources/` | Source summary pages (one per raw source) |
| `analysis/` | Synthesized analysis (filed query results) |
| `timelines/` | Chronological event sequences |

Each subdirectory contains a `_index.md` with a summary table.

---

## Page Types & Frontmatter Schemas

### Legal Framework

File: `wiki/legal-frameworks/{treaty-slug}.md`

```yaml
---
type: legal-framework
title: ""
official_name: ""
official_name_ko: ""
aliases: []
framework_type: ""             # convention | protocol | bilateral-treaty | mou
                               # model-law | un-resolution | regional-agreement
adopted_date: ""
entry_into_force: ""
depositary: ""
sponsoring_body: ""            # wikilink
status: ""                     # in-force | not-yet-in-force | superseded | draft
                               # open-for-signature | under-negotiation
parties:
  states_parties: 0
  signatories: 0
  notable_non_parties: []
key_provisions:
  - article: ""
    topic: ""
    relevance: ""
scope:
  substantive_law: false
  procedural_law: false
  international_cooperation: false
  jurisdiction: false
  evidence: false
  data_protection: false
related_frameworks: []         # wikilinks
implementing_mechanisms: []    # wikilinks
operations_enabled: []         # wikilinks
source_count: 0
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body sections: Summary | Historical Context | Key Provisions for IC | Parties and Participation | Implementation in Practice | Relationship to Other Frameworks | Criticisms and Debates | Korean Perspective (한국 관점) | Contradictions & Open Questions

### Organization / Agency

File: `wiki/organizations/{org-slug}.md`

```yaml
---
type: organization
title: ""
official_name: ""
official_name_ko: ""
aliases: []
org_type: ""                   # international-org | regional-org | national-agency
                               # national-unit | prosecution-office | network
                               # private-sector-partner
status: "active"               # active | reorganized | dissolved | renamed | planned
                               # Use "reorganized" when the entity was absorbed/split
                               # and a successor exists. Use "dissolved" only if no
                               # successor. Use "planned" for entities announced but
                               # not yet operational.
established: ""                # YYYY or YYYY-MM-DD
dissolved_date: ""             # date the entity ceased to exist as named (optional)
successor: ""                  # wikilink — entity that took over the mandate
predecessor: ""                # wikilink — entity the current org replaced
parent_org: ""                 # wikilink
country: ""                    # for national agencies
headquarters: ""
mandate: ""
member_states: 0
key_roles: []                  # IC-specific functions
cooperation_partners: []       # wikilinks
frameworks_administered: []    # wikilinks
mechanisms_operated: []        # wikilinks
operations_participated: []    # wikilinks
notable_cases: []              # wikilinks
contact_point_for:
  - network: ""                # wikilink
    role: ""
source_count: 0
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
last_verified: YYYY-MM-DD      # date the "current state" fields were last
                               # fact-checked against authoritative sources
---
```

Body sections: Summary | **Current Status (as of {last_verified})** | Mandate and Authority | Structure Relevant to Cybercrime IC | IC Capabilities | Key Operations and Cases | Cooperation Track Record | Capacity Building | **History and Reorganizations** | Korean Interactions (한국과의 협력) | Contradictions & Open Questions

**Temporal integrity rules** for organization pages:
1. **Current Status** section is mandatory for any entity whose structure has changed. State the present-day name, level (국/과/심의관), parent, and effective date.
2. **History and Reorganizations** is a dated timeline: `{YYYY-MM-DD}: {change}` — every name change, merger, elevation, dissolution, or successor creation.
3. For reorganized entities, keep historical operations (pre-reorganization) in `operations_participated` but **annotate in prose** which operations happened under which name/structure.
4. `last_verified` must be updated whenever current-state claims are checked against authoritative sources. Stale `last_verified` dates (> 180 days) should be re-checked during lint passes.

### Country Profile

File: `wiki/countries/{country-slug}.md`

```yaml
---
type: country
title: ""
iso_code: ""
legal_system: ""               # common-law | civil-law | mixed
region: ""                     # east-asia | western-europe | north-america | etc.
cybercrime_legislation:
  primary_law: ""
  primary_law_date: ""
  procedural_powers: []        # interception | search-and-seizure | production-order
                               # preservation-order | real-time-collection
  data_retention: ""
treaty_memberships:
  - framework: ""              # wikilink
    status: ""                 # party | signatory | acceded | invited | non-party
    date: ""
    reservations: []
central_authority:
  mlat: ""
  budapest: ""
key_agencies: []               # wikilinks
ic_capacity:
  rating: ""                   # high | medium | low | very-low | unknown
  digital_forensics: ""        # high | medium | low
  24_7_availability: false
  english_proficiency: ""      # high | medium | low
  avg_mlat_response_days: ""   # "30-60" | "90-180" | "180+" | "unknown"
bilateral_agreements: []       # wikilinks
operations_participated: []    # wikilinks
notable_cases: []              # wikilinks
cooperation_assessment: ""
source_count: 0
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body sections: Summary | Legal Framework for Cybercrime (Substantive Law / Procedural Powers / MLA) | Treaty Memberships | Key Agencies | Cooperation Track Record (As Requesting / As Requested / Bilateral) | Capacity Assessment | Notable Operations and Cases | Political and Diplomatic Context | Challenges | Contradictions & Open Questions

### Operation

File: `wiki/operations/{operation-slug}.md`

```yaml
---
type: operation
title: ""
aliases: []
case_id: ""                    # CYB-YYYY-NNN format (research methodology ID)
period: 0                      # 1 (2015-2018) | 2 (2019-2022) | 3 (2023-2025)
operation_type: ""             # takedown | joint-investigation | arrest-sweep
                               # infrastructure-seizure | undercover | capacity-building-exercise
status: ""                     # completed | ongoing | stalled | classified
enforcement_type: []           # arrest | seizure | takedown | extradition | asset_freeze | indictment
outcome: ""                    # success | partial | failure | ongoing | unknown
timeframe:
  announced: ""
  start: ""
  end: ""
  ongoing: false
crime_types: []                # wikilinks — canonical list. Operations commonly span multiple crime types (e.g., `[[ransomware-ic]]` + `[[money-laundering-ic]]` + `[[darknet-trade-ic]]` for a takedown with monetization angle). Single-type ops use a list of one.
crime_type: ""                 # DEPRECATED — legacy single-value field, kept as read-only fallback during PoC v4 SNA migration. Do NOT author new content with this field. Scheduled for removal once all ingest paths + tools stop referencing it.
target_entity: ""
lead_agency: ""                # wikilink
coordinating_body: ""          # wikilink
participating_countries: []    # wikilinks
participating_agencies: []     # wikilinks
legal_basis: []                # wikilinks
mechanisms_used: []            # wikilinks
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other: []
edges:                         # cooperation relationships (SNA edge data)
  - source_actor: ""           # actor name or actor_id
    target_actor: ""           # actor name or actor_id
    cooperation_type: ""       # info_sharing | joint_investigation | extradition
                               # evidence_transfer | technical_assistance
                               # capacity_building | asset_recovery
    legal_basis: ""            # MLAT | Budapest_Convention | CLOUD_Act
                               # bilateral_MOU | informal | unknown
    direction: ""              # directed | undirected | unknown
credibility_index: 0.0        # CI score from evaluator (0.6-5.0)
source_tier: 0                 # 1-4 (highest tier source available)
missing_fields: []             # fields with missing data (item nonresponse)
related_cases: []              # wikilinks
related_operations: []         # wikilinks
challenges_encountered: []     # wikilinks
lessons_learned: []
source_count: 0
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body sections: Summary | Background | Participating Parties | Legal Framework | Operational Timeline | Results and Impact | Cooperation Mechanisms Used | Challenges and Friction Points | Lessons Learned | Follow-Up Actions | Korean Involvement (한국의 참여) | Contradictions & Open Questions

### Case

File: `wiki/cases/{case-slug}.md`

```yaml
---
type: case
title: ""                      # "United States v. Kondratiev et al."
case_number: ""
jurisdiction: ""
jurisdiction_country: ""       # wikilink
case_type: ""                  # prosecution | extradition | asset-forfeiture
                               # mutual-legal-assistance | civil-seizure
status: ""                     # indicted | fugitive | arrested | extradited
                               # trial-pending | convicted | sentenced
                               # acquitted | dismissed | sealed
crime_charged: []              # wikilinks to crime-type pages
defendants:
  - name: ""
    nationality: ""
    status: ""
    sentence: ""
    location_at_arrest: ""
related_operation: ""          # wikilink
ic_elements:
  mlat_requests: []            # countries
  extradition: ""
  evidence_from_abroad: []     # countries
  foreign_arrests: []          # countries
  asset_freezing: []           # countries
cooperating_agencies: []       # wikilinks
legal_frameworks_invoked: []   # wikilinks
mechanisms_used: []            # wikilinks
key_legal_issues: []           # wikilinks to concept pages
precedent_value: ""
source_count: 0
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body sections: Summary | Facts | International Cooperation Elements (Evidence Gathering / Arrest & Extradition / Asset Recovery) | Legal Analysis (Jurisdiction / Key Legal Issues / Precedent Value) | Proceedings Timeline | Cooperation Effectiveness | Korean Relevance (한국 관련성) | Contradictions & Open Questions

### Mechanism

File: `wiki/mechanisms/{mechanism-slug}.md`

```yaml
---
type: mechanism
title: ""
aliases: []
mechanism_type: ""             # formal-mlat | informal-police-cooperation
                               # 24-7-network | joint-investigation-team
                               # liaison-network | information-sharing-platform
                               # provider-disclosure | voluntary-cooperation
formality: ""                  # formal | semi-formal | informal
legal_basis: []                # wikilinks
administered_by: ""            # wikilink
participants:
  type: ""                     # states | agencies | prosecutors | mixed
  count: 0
  notable_members: []          # wikilinks
purpose: ""
speed: ""                      # real-time | hours | days | weeks | months
scope:
  evidence_preservation: false
  evidence_production: false
  real_time_data: false
  subscriber_info: false
  content_data: false
  traffic_data: false
  arrest_coordination: false
  asset_tracing: false
  intelligence_sharing: false
limitations: []
operations_using: []           # wikilinks
cases_using: []                # wikilinks
related_mechanisms: []         # wikilinks
source_count: 0
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body sections: Summary | Legal Basis | How It Works | Scope and Capabilities | Practical Usage | Advantages | Limitations | Notable Uses | Comparison with Alternatives | Korean Usage (한국의 활용) | Contradictions & Open Questions

### Procedure

File: `wiki/procedures/{procedure-slug}.md`

```yaml
---
type: procedure
title: ""
aliases: []
procedure_type: ""             # evidence-preservation | evidence-production
                               # mlat-request | extradition-request
                               # emergency-disclosure | asset-freezing
                               # joint-investigation-setup
legal_basis: []                # wikilinks
mechanisms_involved: []        # wikilinks
typical_participants:
  requesting: ""
  requested: ""
prerequisites: []
average_duration: ""
steps:
  - step: 1
    actor: ""
    action: ""
    documents: []
    notes: ""
success_factors: []
common_pitfalls: []
template_available: false
related_procedures: []         # wikilinks
source_count: 0
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body sections: Summary | Legal Basis | Prerequisites | Step-by-Step Process | Required Documents | Timelines | Practical Tips | Country-Specific Variations | Common Pitfalls | Related Procedures | Korean Practice (한국 실무) | Contradictions & Open Questions

### Crime Type

File: `wiki/crime-types/{crime-type-slug}.md`

```yaml
---
type: crime-type
title: ""                      # "Ransomware — International Cooperation Perspective"
aliases: []
crime_category: ""             # cyber-dependent | cyber-enabled | content-related
typical_ic_challenges: []      # wikilinks to challenges
relevant_legal_frameworks: []  # wikilinks
typical_mechanisms: []         # wikilinks
key_organizations: []          # wikilinks
notable_operations: []         # wikilinks
notable_cases: []              # wikilinks
criminalization_status:
  broadly_criminalized: false
  definition_varies: false
  problem_jurisdictions: []
estimated_annual_loss: ""
source_count: 0
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body sections: Summary | Criminalization Landscape | Typical IC Scenarios | Evidence Types and Locations | Cooperation Pathways | Key Operations and Precedents | Challenges | Statistics and Trends | Prevention and Disruption | Korean Context (한국 상황) | Contradictions & Open Questions

### Challenge

File: `wiki/challenges/{challenge-slug}.md`

```yaml
---
type: challenge
title: ""
aliases: []
challenge_category: ""         # legal | technical | political | institutional
                               # capacity | linguistic | temporal | economic
severity: ""                   # critical | high | medium | low
affected_mechanisms: []        # wikilinks
affected_crime_types: []       # wikilinks
affected_regions: []
proposed_solutions: []
active_debates: []
related_concepts: []           # wikilinks
related_challenges: []         # wikilinks
source_count: 0
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body sections: Summary | Nature of the Problem | Impact on Cooperation | Root Causes | Proposed Solutions | Current State of Debate | Case Studies | Comparative Perspectives | Korean Perspective (한국 관점) | Contradictions & Open Questions

### Concept

File: `wiki/concepts/{concept-slug}.md`

```yaml
---
type: concept
title: ""                      # "Dual Criminality"
title_ko: ""                   # "쌍방가벌성"
aliases: []                    # ["double criminality", "double incrimination"]
aliases_ko: []
concept_category: ""           # legal-principle | jurisdictional-doctrine
                               # procedural-concept | human-rights-safeguard
                               # technical-concept | institutional-term
domain: ""                     # international-law | criminal-law | procedural-law
                               # human-rights-law | data-protection | technology
definition: ""
legal_basis: []                # Treaty articles, case law
relevance_to_ic: ""
related_concepts: []           # wikilinks
related_challenges: []         # wikilinks
applied_in_cases: []           # wikilinks
source_count: 0
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body sections: Definition | Legal Basis | Relevance to IC on Cybercrime | How It Works in Practice | Variations Across Jurisdictions (Common Law / Civil Law) | Key Case Law | Debates and Controversies | Korean Law (한국법) | Multi-Language Terminology (table) | Contradictions & Open Questions

### Source Summary

File: `wiki/sources/{source-slug}.md`

```yaml
---
type: source
title: ""
raw_path: ""
source_type: ""                # treaty-text | case-document | government-report
                               # academic-paper | news | policy-document
                               # conference-proceeding | legislation
                               # press-release | mla-document
publisher: ""
author: ""
publish_date: ""
ingest_date: ""
language: ""                   # en | ko | fr | de | es | multi
reliability: ""                # high | medium | low | unverified
credibility: ""                # confirmed | probably-true | possibly-true
                               # doubtful | improbable | unassessed
sensitivity: ""                # public | restricted | confidential
pages_updated: []              # wikilinks
key_findings: []
created: YYYY-MM-DD
---
```

### Analysis

File: `wiki/analysis/{analysis-slug}.md`

```yaml
---
type: analysis
title: ""
analysis_type: ""              # gap-analysis | comparative-study | trend-report
                               # effectiveness-assessment | policy-recommendation
                               # case-comparison | mechanism-evaluation
scope: ""
confidence: ""                 # high | medium | low
key_judgments:
  - judgment: ""
    confidence: ""
sources_consulted: 0
entities_referenced: []        # wikilinks
generated_from: ""             # query | lint | manual
query_prompt: ""
created: YYYY-MM-DD
---
```

---

## Workflows

### INGEST — Processing a New Source

**Pre-check: decide whether a new page is warranted at all.**
- Does this source mainly deepen an existing page?
- Would the highest-value output be synthesis in `wiki/analysis/`?
- Would a new page be thin, duplicative, or naming-fragile?

If yes, prefer updating existing pages and/or analysis rather than creating a new standalone page.

**Step 1: Read** the full raw source.

**Step 2: Discuss** key takeaways with user (skip if batch-ingest).

**Step 3: Create Source Summary** in `wiki/sources/`.
- Assign reliability, credibility, sensitivity using Source Type defaults.
- Note source language.

**Step 4: Extract & Integrate** entities.
- For each entity: update existing page or create new one.
- Prefer merge over multiplication. If an existing page can absorb the information cleanly, update it instead of creating a sibling page.
- **Legal information must cite specific articles and note the date.**
- **Preserve original-language legal terms** in parentheses.
- For legislation: update the relevant country's `cybercrime_legislation`.
- For press releases about operations: create/update operation page + all participant pages.
- For case documents: extract IC elements, legal basis, defendants.
- For treaties: map provisions article-by-article, update all party country pages.

**Entity creation threshold**
- Preferred publication threshold for normal `case` and `operation` pages: `source_count >= 5`.
- If the topic matters but sourcing is still sparse, use an explicitly provisional stub/review-state page.
- Do not mass-create thin follow-on pages when the same material fits better in a parent page or analysis page.

**Step 5: Maintain Bidirectional Links**

| When you add... | Also add... |
|---|---|
| `participating_agencies: [[X]]` on operation | `operations_participated: [[op]]` on org X |
| `participating_countries: [[X]]` on operation | `operations_participated: [[op]]` on country X |
| `treaty_memberships: [{framework: [[X]]}]` on country | increment parties count on framework X |
| `legal_frameworks_invoked: [[X]]` on case | `operations_enabled: [[case]]` on framework X |
| `related_cases: [[X]]` on operation | `related_operation: [[op]]` on case X |
| `key_agencies: [[X]]` on country | `country: [[country]]` on org X |
| `mechanisms_used: [[X]]` on operation | `operations_using: [[op]]` on mechanism X |
| `applied_in_cases: [[X]]` on concept | `key_legal_issues: [[concept]]` on case X |
| `pages_updated: [[X]]` on source | `sources: [[source]]` on entity X |

**Step 6: Update Indexes** — category `_index.md` tables and `wiki/index.md`.

**Step 7: Log** — append to `wiki/log.md`:
```markdown
## [YYYY-MM-DD] ingest | {Source Title}
- Source: {raw_path}
- Pages created: {list}
- Pages updated: {list}
- Key findings: {1-2 bullets}
```

**Step 8: Flag Issues**
- Contradictions: `> [!warning] Contradiction` callout.
- Legal status uncertainty: `> [!warning] Legal status check needed`.
- Translation uncertainty: `> [!note] Translation note`.

### QUERY — Answering Questions

**Step 1:** Read `wiki/index.md` → identify relevant pages → read them.

**Step 2:** Synthesize answer with `[[wikilinks]]` as citations. Use confidence language.

**Step 3:** If the answer is a reusable analysis (comparison, gap analysis, effectiveness assessment), file or update it in `wiki/analysis/` unless the user explicitly wants an ephemeral answer only.

**Step 4:** If the query reveals a structural gap, update the relevant entity pages and cross-links as part of the same task when feasible.

### LINT — Wiki Health Check

**CRITICAL:**
1. Broken bidirectional links
2. Orphan pages (zero inbound links)
3. Missing source provenance
4. Treaty membership inconsistency (country says party, treaty page disagrees)
5. Legal status contradiction (case status contradicts newer source)

**HIGH:**
6. Stale pages (>180 days + newer sources exist)
7. Missing legal basis on operation pages
8. Incomplete country profile (missing legislation, treaties, or central authority)
9. Completed operation with empty results
10. Case without IC elements
11. Alias collision between entities

**MEDIUM:**
12. Category index missing entry
13. Undocumented concept referenced in prose
14. Procedure page without step-by-step steps
15. Country page missing cooperation_assessment
16. Missing Korean perspective section where relevant
17. Low source diversity (single jurisdiction perspective)
18. Missing confidence qualifiers
19. Empty sections
20. Missing title_ko on concept pages
21. Page exists but adds little beyond what a parent page or analysis page already explains
22. Thin follow-on page that should be merged, demoted to stub, or replaced by analysis

**LOW:**
23. Incomplete frontmatter
24. Naming convention violations
25. Content duplication
26. Unlinked entity mentions
27. Missing multi-language terminology table on concepts
28. Procedures without common_pitfalls

---

## Cross-Referencing Rules

### Wikilinks
- Use `[[wikilinks]]` throughout. Link on first mention per section.
- Display text for readability: `[[budapest-convention|Budapest Convention]]`
- **Never create a wikilink to a non-existent page without also creating a stub.**

### Stub Pages
```yaml
---
type: {type}
title: "{name}"
source_count: 0
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

> [!info] Stub
> This page was auto-created. It will be expanded when more sources are ingested.
```

Use stubs sparingly. A stub is a temporary integrity device, not a successful endpoint. During later enrichment, prefer either:
- promoting it into a fully sourced standalone page, or
- merging it into a stronger parent or analysis page and removing the weak standalone entry

---

## Intelligence & Legal Standards

### Confidence Language (US IC Analytic Standards)

| Term | Probability | Use When |
|---|---|---|
| Almost certainly | >95% | Multiple independent high-reliability sources agree |
| Highly likely | 80-95% | Strong evidence, minor gaps |
| Likely | 55-80% | Preponderance of evidence |
| Roughly even chance | 45-55% | Evidence balanced or insufficient |
| Unlikely | 20-45% | Evidence weighs against |
| Highly unlikely | 5-20% | Strong evidence against |
| Almost certainly not | <5% | Overwhelming evidence against |

**Every analytical statement MUST include a confidence qualifier.**

### Source Reliability Defaults

| Source Type | Default Reliability | Default Credibility |
|---|---|---|
| Treaty text | high | confirmed |
| Case document (court filing) | high | confirmed |
| Legislation | high | confirmed |
| Press release (official agency) | high | probably-true |
| Government report | high | probably-true |
| Academic paper (peer-reviewed) | medium-high | probably-true |
| Policy document | medium-high | probably-true |
| News (major outlet) | medium | possibly-true |
| Conference proceeding | medium | possibly-true |
| MLA guidance document | high | confirmed |

### Sensitivity Handling

| Sensitivity | Handling |
|---|---|
| `public` | No restrictions. Record freely. |
| `restricted` | Record with `> [!caution] Restricted` callout. Omit operational details. |
| `confidential` | **DO NOT record content.** Only note existence and general topic. |

**Operational security rules:**
- Never include details that could compromise ongoing investigations.
- Never record sealed indictment content until unsealed.
- Never include specific MLAT request content (only that a request was made).
- Never include intelligence source identities.
- When in doubt, ask the user.

### Legal Precision Rules

1. Cite **specific articles** of treaties/legislation, not just names.
2. Note the **date** of legal information. Laws change.
3. Distinguish **binding vs. non-binding** instruments.
4. Use precise terminology:
   - *Signature* = intent, not binding
   - *Ratification* = formal consent to be bound (after domestic approval)
   - *Accession* = becoming party without prior signature (same legal effect)
5. Distinguish **"law on the books" vs. "law in practice."**
6. Flag potentially outdated legal info: `> [!warning] Legal status check needed`

### Multi-Language Legal Terms

1. English as primary wiki language.
2. Korean in parentheses on first mention: "dual criminality (쌍방가벌성)"
3. Concept pages include multi-language terminology table:
   ```markdown
   | Language | Term | Notes |
   |----------|------|-------|
   | English | dual criminality | Also: double criminality |
   | Korean | 쌍방가벌성 | |
   | French | double incrimination | |
   ```
4. Use `> [!note] Translation note` when terms are not exact equivalents.

### Diplomatic Neutrality

- Country cooperation assessments require **multiple credible sources + confidence language**.
- No pejorative characterizations of countries or legal systems.
- Present all significant positions in treaty negotiations.
- Do not oversimplify reasons for treaty non-participation.

---

## Contradiction Handling

When a new source contradicts existing wiki content:

1. **Do NOT silently overwrite.**
2. Add a callout:
   ```markdown
   > [!warning] Contradiction
   > **Claim A** (Source: [[source-a]], reliability: high): Country X ratified in 2023.
   > **Claim B** (Source: [[source-b]], reliability: medium): Country X has only signed, not ratified.
   > **Assessment**: Claim A is *likely* correct based on source reliability.
   ```
3. Preserve history even after resolution.

---

## Naming Conventions

| Type | Pattern | Example |
|---|---|---|
| Legal framework | `{treaty-slug}.md` | `budapest-convention.md` |
| Organization | `{org-slug}.md` | `europol-ec3.md` |
| Country | `{country-slug}.md` | `south-korea.md` |
| Operation | `{operation-slug}.md` | `operation-cronos.md` |
| Case | `{case-slug}.md` | `us-v-kondratiev-lockbit.md` |
| Mechanism | `{mechanism-slug}.md` | `mlat-process.md` |
| Procedure | `{procedure-slug}.md` | `emergency-data-preservation.md` |
| Crime type | `{crime-type-slug}.md` | `ransomware-ic.md` |
| Challenge | `{challenge-slug}.md` | `data-sovereignty.md` |
| Concept | `{concept-slug}.md` | `dual-criminality.md` |

Slugification: lowercase, spaces/underscores → hyphens, remove special characters.

---

## Operational Rules

1. **Never modify files in `raw/`.** They are immutable.
2. **Always update `wiki/log.md`** after every ingest, query filing, or lint pass.
3. **Always maintain bidirectional links.** This is the #1 consistency invariant.
4. **Always include confidence language** in analytical statements.
5. **Always cite specific articles** of treaties and legislation.
6. **Always note dates** of legal information.
7. **Never create wikilinks to non-existent pages** without creating a stub.
8. **Never silently overwrite contradictions.** Document them explicitly.
9. **Respect sensitivity classifications.** Never record `confidential` content.
10. **Maintain diplomatic neutrality.** No value judgments without evidence + confidence language.
11. **Preserve original-language legal terms** in parentheses.
12. **Include Korean perspective** (한국 관점/한국 실무) on relevant pages.
13. **Update `updated` date** in frontmatter when modifying a page.
14. **Keep pages under 800 lines.** Split if needed.
15. **Write wiki content in English.** User interaction can be in any language.
16. **Prefer synthesis over proliferation.** If new information mainly clarifies relationships or patterns, update existing pages and `wiki/analysis/` rather than creating new standalone pages.
17. **Use `wiki/analysis/` aggressively for durable insight.** Comparative answers, trend assessments, contradictions, and cross-jurisdiction patterns should become maintained pages.
18. **Do not publish thin normal pages below the preferred source threshold** unless they are explicitly marked as provisional or stub content.
19. **Canonicalize entities.** Prefer one canonical page plus aliases over multiple near-duplicate entity pages.
20. **Measure quality by explanation and connectedness, not page count.**

---

## Quick Reference

| Situation | Action |
|---|---|
| User drops a new source | Run INGEST workflow |
| User asks a question | Run QUERY workflow |
| User says "lint" or "health check" | Run LINT workflow |
| New entity not in wiki | Create page using template |
| Entity already exists | Read page, merge new data |
| Source contradicts wiki | Contradiction callout, preserve both |
| Confidential source | Note existence only |
| Legal info may be outdated | `> [!warning] Legal status check needed` |
| Translation uncertain | `> [!note] Translation note` |
| Two pages same alias | Investigate, merge if same entity |
| Page > 800 lines | Split by sub-topic or time period |
| Query result is valuable | File or update an analysis page |
| Treaty ratification update | Update both country AND framework pages |
| New source mostly strengthens existing knowledge | Update existing pages before considering a new page |
| Proposed new page would be thin | Prefer analysis page, parent-page expansion, or stub/review state |
