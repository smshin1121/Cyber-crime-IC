# Codex Task: Court Document Collection for 98 Operations

## Project

`C:\Users\shin1121\Desktop\Cyber_crime_IC` — a wiki tracking **international cooperation on cybercrime**. 108 operations total, 10 already have court documents linked. **98 remain.**

Read `CLAUDE.md` for full project rules, especially:
- `wiki/cases/` frontmatter schema (the Case page type)
- `raw/case-documents/` naming convention: `YYYY-MM-DD_court_slug.md`
- INGEST workflow (bidirectional links, index updates)
- Confidence language requirements

## Objective

For each of the 98 remaining operations, find and ingest publicly available **court documents** (indictments, complaints, judgments, sentencing memos, plea agreements) related to the operation.

## Tools available

### 1. Automated: `tools/collect_court_docs.py`

```bash
# Dry-run top 20 by priority score
python tools/collect_court_docs.py --dry-run --top 20

# Run for real on specific operation
python tools/collect_court_docs.py --slug silk-road-takedown

# Run all remaining (skips already-searched via state file)
python tools/collect_court_docs.py --top 98
```

This tool queries **CourtListener API** (US federal courts). It works best for:
- US-prosecuted operations (DOJ/FBI lead)
- Cases with known defendant names
- Cases with published court opinions

It does NOT cover:
- EU/Asian court systems
- Sealed cases
- Operations without identifiable defendants

### 2. Manual web search (for what the tool misses)

For operations where `collect_court_docs.py` returns 0 results:
- Search: `"<operation name>" site:justice.gov indictment`
- Search: `"<defendant name>" cybercrime sentenced`
- Search: `"<operation name>" court document case number`
- Check Europol press releases for EU case references
- Check UNODC SHERLOC (sherloc.unodc.org) for international cases

## Priority order (98 operations, descending score)

Score combines: indictment mentions (+2), sentencing language (+3), US jurisdiction (+2), EU jurisdiction (+1), ongoing status (-2).

### Batch 1 — High priority (score >= +5, 8 ops)

| Score | Slug | Notes |
|---|---|---|
| +7 | operation-power-off | DDoS-for-hire, UK/NL/US prosecution |
| +7 | operation-bakovia | Romanian phishing, FBI+DIICOT |
| +6 | operation-chakra-iii | CBI India tech support scam |
| +6 | nigerian-bec-convictions-2023 | DOJ multiple sentencings |
| +6 | marketplace-a-dekhtyarchuk-indictment | DOJ case, named defendant |
| +6 | infraud-telusma-sentencing | DOJ case, named defendant |
| +6 | black-axe-bec-2021 | FBI/INTERPOL, multiple arrests |
| +6 | banking-trojan-fraud-sentencing-2017 | DOJ sentencing |

### Batch 2 — Medium-high (score = +4, 38 ops)

```
cyberbunker-takedown, zeus-spyeye-takedown, xdedic-marketplace-takedown,
vpnlab-takedown, qqaazz-money-laundering-takedown, phobos-8base-crackdown,
operation-trojan-shield, operation-talent, operation-source,
operation-shrouded-horizon, operation-secreto, operation-pleiades,
operation-onymous, operation-nova, operation-nightfury, operation-nervone,
operation-lyrebird, operation-kraken-ghost-platform, operation-endgame-phase1,
operation-destabilise, operation-delilah, operation-cronos-phase3,
operation-cronos-phase1, operation-avalanche, myanmar-kokang-scam-compound-crackdown,
lumma-stealer-takedown, hive-ransomware-takedown, doublevpn-takedown,
ddos-for-hire-sweep-2016, darkmarket-takedown, carbanak-cobalt-takedown,
blackcat-lockeroga-kelvin-security-2023, bidencash-takedown, bec-nigeria-2016,
andromeda-botnet-takedown, alphabay-takedown, africa-cyber-surge-ii,
2bagoldmule-qqaazz
```

### Batch 3 — Medium (score = +3, 10 ops)

```
simda-botnet-takedown, rydox-marketplace-takedown, operation-wirewire,
operation-rewired, operation-hyperion, operation-heart-blocker,
operation-checkmate-blacksuit, nemesis-market-takedown,
isoon-apt27-indictment, fin7-takedown, 911-s5-botnet-takedown
```

### Batch 4 — Lower priority (score <= +2, 42 ops)

Remaining operations. Many are INTERPOL/AFRIPOL-led (non-US jurisdiction) or operations without publicly identified defendants. Court docs may not exist publicly.

## Per-operation workflow

### Step 1: Read the operation page

```bash
cat wiki/operations/<slug>.md
```

Extract: operation name, aliases, defendants, lead agency, timeframe, case numbers in body.

### Step 2: Run automated tool

```bash
python tools/collect_court_docs.py --slug <slug>
```

If it finds results -> proceed to Step 4.

### Step 3: Manual search (if tool found nothing)

Search the web for court documents. If nothing is publicly available, create a note:

```markdown
> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.
```

Add this note to the operation page body under "Legal Analysis" or "Follow-Up Actions" section. Then skip to Step 5.

### Step 4: Create case page + raw document

**Raw document** at `raw/case-documents/YYYY-MM-DD_court_slug.md`:

```yaml
---
title: "United States v. Doe"
court: "U.S. District Court, ..."
case_number: "1:21-cr-00345"
document_type: "indictment"  # indictment | complaint | judgment | sentencing-memo | plea-agreement
date_filed: "YYYY-MM-DD"
source_url: "https://..."
related_operation: "<slug>"
collection_date: "2026-04-17"
publisher: "US DOJ"
language: "en"
sensitivity: "public"
---

## {Case Title}

{2-3 paragraph summary: charges, IC elements, sentence if applicable}
```

**Case page** at `wiki/cases/<case-slug>.md` — follow the Case schema in CLAUDE.md exactly. See `wiki/cases/us-v-ulbricht-silk-road.md` as a complete example with all required fields.

### Step 5: Update bidirectional links

- Add `[[case-slug]]` to operation's `related_cases:` frontmatter list
- If the case involves agencies/countries already in the wiki, do NOT update their pages (the reconciler handles index consistency)

## Validation (after each batch)

```bash
# Reconcile all indexes
python tools/reconcile_indexes.py

# Quality gates
python tools/lint.py          # CRITICAL/HIGH must be 0
python tools/check_links.py   # broken must be 0

# Verify bidirectional links
python -c "
import pathlib, re
cases = [p for p in pathlib.Path('wiki/cases').glob('*.md') if p.name != '_index.md']
for p in cases:
    t = p.read_text(encoding='utf-8')
    m = re.search(r'^related_operation:\s*.*\[\[([^\]]+)\]\]', t, re.M)
    if not m:
        print(f'WARN: {p.name} has no related_operation')
        continue
    op = m.group(1)
    op_path = pathlib.Path(f'wiki/operations/{op}.md')
    if not op_path.exists():
        print(f'BROKEN: {p.name} -> {op} (operation not found)')
        continue
    op_text = op_path.read_text(encoding='utf-8')
    if p.stem not in op_text:
        print(f'MISSING BACKLINK: {op}.md does not reference {p.stem}')
    else:
        print(f'OK: {p.name} <-> {op}')
"
```

## Commit convention

One commit per batch:

```
feat: 판결문 Batch N — M개 operation court docs 수집

- raw/case-documents/: N건 생성
- wiki/cases/: N건 생성
- operations updated: N건 (related_cases 역참조)
- reconcile_indexes 실행 완료

검증: lint CRITICAL/HIGH 0, check_links broken 0
```

## Important rules

1. **Never modify `raw/` files that already exist** — only create new ones
2. **Never silently overwrite** — if a case page already exists, read it first and merge
3. **Confidence language** on all analytical statements ("almost certainly", "likely", etc.)
4. **If a case is sealed**, note existence only with `sensitivity: restricted`
5. **Preserve original metrics** verbatim (arrest counts, amounts seized, etc.)
6. **Include IC elements** in every case page: which countries cooperated, what mechanisms used (MLAT, extradition, JIT), what evidence crossed borders
7. **Korean perspective** section if Korea is involved (한국 관련성)
8. **Do NOT touch `_index.md` files** — `reconcile_indexes.py` handles those

## Expected output

- ~40-60 new raw/case-documents/ files (not all 98 ops will have findable docs)
- ~30-50 new wiki/cases/ pages
- ~50-70 operations updated with related_cases backlinks
- ~30-40 operations marked "no public court docs found"
- All quality gates passing

## Batch execution plan

| Batch | Operations | Estimated court docs | Priority |
|---|---|---|---|
| 1 | 8 (score >= +5) | ~6-8 | **Do first** |
| 2 | 38 (score = +4) | ~20-25 | Second |
| 3 | 10 (score = +3) | ~5-8 | Third |
| 4 | 42 (score <= +2) | ~5-15 | Last (many will be "not found") |
