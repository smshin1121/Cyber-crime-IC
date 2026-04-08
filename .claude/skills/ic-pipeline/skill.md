---
name: ic-pipeline
description: "사이버범죄 국제공조 데이터 수집·분류·평가·검증·위키통합 파이프라인을 실행하는 오케스트레이터. '데이터 수집', '파이프라인 실행', '소스 수집', 'ingest pipeline', '국제공조 데이터', 'collect operations' 등의 요청 시 반드시 이 스킬을 사용할 것. /ic-pipeline 으로도 호출 가능."
---

# IC Pipeline Orchestrator

사이버범죄 국제공조 데이터를 웹에서 수집하고 LLM Wiki로 자동 통합하는 5단계 파이프라인.

## Execution Mode: Sub-agent (Pipeline Pattern)

```
[Orchestrator]
  → [1. Collector]  → _workspace/collected/
  → [2. Classifier] → _workspace/classified/
  → [3. Evaluator]  → _workspace/evaluated/
  → [4. Verifier]   → _workspace/verified/
  → [5. Integrator] → wiki/
```

## Agent Configuration

| Stage | Agent | Agent File | Type | Tools |
|-------|-------|-----------|------|-------|
| 1 | ic-collector | `.claude/agents/ic-collector.md` | general-purpose | WebSearch, WebFetch, Write |
| 2 | ic-classifier | `.claude/agents/ic-classifier.md` | general-purpose | Read, Write, Edit |
| 3 | ic-evaluator | `.claude/agents/ic-evaluator.md` | general-purpose | Read, Write, Grep, Glob |
| 4 | ic-verifier | `.claude/agents/ic-verifier.md` | general-purpose | Read, Write, Edit, Grep, Glob |
| 5 | ic-integrator | `.claude/agents/ic-integrator.md` | general-purpose | Read, Write, Edit, Grep, Glob |

## Workflow

### Phase 0: Preparation
1. Parse user input: search query, date range, specific sources, max results
2. Create `_workspace/` directory with subdirectories:
   ```
   _workspace/
   ├── collected/     # Stage 1 output
   ├── classified/    # Stage 2 output
   ├── evaluated/     # Stage 3 output
   ├── verified/      # Stage 4 output
   └── reports/       # Pipeline reports
   ```
3. Set defaults: date range = last 30 days, max results = 10

### Phase 1: Collection
Launch ic-collector agent:
```
Agent(
  description: "Collect IC operation data",
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "
    Read the agent definition at .claude/agents/ic-collector.md.
    Then execute the collection task:
    - Search query: {user_query or default keywords}
    - Date range: {date_range}
    - Max results: {max_results}
    - Save collected files to _workspace/collected/
    - Also save copies to raw/{appropriate-subdir}/
    - Return: list of collected file paths and summary
  "
)
```
Wait for completion. Parse returned file list.

### Phase 2: Classification
For each collected file, launch ic-classifier:
```
Agent(
  description: "Classify collected source",
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "
    Read the agent definition at .claude/agents/ic-classifier.md.
    Then classify this source:
    - Input file: {collected_file_path}
    - Save classified file to _workspace/classified/{same-filename}
    - Extract: operation name, agencies, countries, crime types, metrics
    - Return: extracted entities summary
  "
)
```
Can run in parallel for multiple files (run_in_background: true).

### Phase 3: Evaluation
For each classified file, launch ic-evaluator:
```
Agent(
  description: "Evaluate data quality",
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "
    Read the agent definition at .claude/agents/ic-evaluator.md.
    Then evaluate:
    - Input file: {classified_file_path}
    - Check against existing wiki/ and raw/ for duplicates
    - Score: reliability, credibility, topic_relevance, data_completeness
    - Save to _workspace/evaluated/{same-filename}
    - Return: PASS/REVIEW/REJECT verdict with scores
  "
)
```

### Phase 4: Verification (PASS items only)
Filter: only items with evaluation verdict = PASS.
Launch ic-verifier:
```
Agent(
  description: "Verify and normalize data",
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "
    Read the agent definition at .claude/agents/ic-verifier.md.
    Then verify these sources:
    - Input files: {list of PASS files from _workspace/evaluated/}
    - Cross-validate metrics across sources for same operations
    - Normalize all entity names to wiki canonical forms
    - Check for conflicts with existing wiki pages
    - Save to _workspace/verified/{same-filename}
    - Return: verification report
  "
)
```

### Phase 5: Wiki Integration (verified items only)
Launch ic-integrator:
```
Agent(
  description: "Integrate into wiki",
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "
    Read the agent definition at .claude/agents/ic-integrator.md.
    Read CLAUDE.md for wiki schema and INGEST workflow.
    Then integrate these verified sources:
    - Input files: {list of files from _workspace/verified/}
    - Follow CLAUDE.md INGEST workflow exactly
    - Create/update: sources/, operations/, organizations/, countries/, crime-types/
    - Maintain bidirectional links
    - Update all _index.md files and wiki/index.md
    - Append to wiki/log.md
    - Return: integration report (pages created/updated)
  "
)
```

### Phase 6: Report
Generate pipeline summary in `_workspace/reports/pipeline-YYYY-MM-DD.md`:

```markdown
# Pipeline Report: {date}

## Summary
- Sources collected: N
- Sources classified: N
- Evaluation: PASS N / REVIEW N / REJECT N
- Sources verified: N
- Wiki pages created: N
- Wiki pages updated: N

## Collected Sources
| # | Title | Source | Relevance | Completeness | Verdict |
|---|-------|--------|-----------|-------------|---------|

## Wiki Changes
| Page | Action | Key Data |
|------|--------|----------|

## Issues & Notes
- {any conflicts, duplicates, or anomalies}
```

Report to user with summary.

## Error Handling

| Error | Action |
|-------|--------|
| Collection fails (no results) | Report to user, suggest alternative keywords |
| Classification ambiguity | Pass to evaluation with `_uncertain` flag |
| Evaluation REJECT | Skip remaining stages, log reason |
| Verification conflict with wiki | Flag in report, do NOT overwrite — add contradiction callout |
| Integration write failure | Retry once, then log and skip |
| Agent timeout | Log stage, report partial results |

## Data Flow

```
User Request
    ↓
[Phase 0] Parse input, create _workspace/
    ↓
[Phase 1] Collector → _workspace/collected/*.md + raw/**/*.md
    ↓
[Phase 2] Classifier → _workspace/classified/*.md (+ entities in frontmatter)
    ↓
[Phase 3] Evaluator → _workspace/evaluated/*.md (+ scores, verdict)
    ↓ (PASS only)
[Phase 4] Verifier → _workspace/verified/*.md (+ normalized, cross-checked)
    ↓
[Phase 5] Integrator → wiki/**/*.md (source, operation, org, country pages)
    ↓
[Phase 6] Report → _workspace/reports/pipeline-YYYY-MM-DD.md
    ↓
User sees: summary + Obsidian wiki updated
```

## Test Scenarios

### Normal Flow
User: "최근 랜섬웨어 국제공조 작전 데이터를 수집해줘"
1. Collector searches for ransomware international operations, collects 5-8 sources
2. Classifier extracts entities from each
3. Evaluator scores: 4 PASS, 2 REVIEW, 1 REJECT
4. Verifier validates 4 PASS items, normalizes names
5. Integrator creates 1 new operation page, updates 3 agency pages, 5 country pages
6. Report generated

### Error Flow
User: "2020년 이전 BEC 작전 수집"
1. Collector finds limited results (older data less available online)
2. Classifier handles 2 sources with sparse data
3. Evaluator: 1 PASS (data_completeness 45%), 1 REJECT (relevance 25%)
4. Verifier: 1 source verified with `low_confidence` flag
5. Integrator: creates pages with multiple `> [!warning]` callouts
6. Report notes data limitations
