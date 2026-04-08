---
name: ic-collect
description: "사이버범죄 국제공조 관련 뉴스, 보도자료, 보고서를 웹에서 수집하여 raw/에 저장. '소스 수집', '뉴스 수집', 'collect', '자료 모아줘' 요청 시 사용."
---

# IC Collect Skill

사이버범죄 국제공조 관련 소스를 웹에서 수집하여 `raw/` 디렉토리에 구조화된 마크다운으로 저장한다.

## Procedure

1. **Search**: WebSearch로 검색. 키워드는 `.claude/agents/ic-collector.md`의 Search Strategy 섹션 참조.
2. **Fetch**: 상위 결과에 대해 WebFetch로 본문 수집.
3. **Filter**: 3-Stage Selection 적용 (제목 스캔 → 전문 확인 → 중복 제거).
4. **Save**: 통과한 소스를 `raw/{source-type}/YYYY-MM-DD_source_slug.md`로 저장.

## File Format

```markdown
---
title: "Operation Cronos: LockBit ransomware gang disrupted"
collection_source: "Europol"
collection_url: "https://www.europol.europa.eu/..."
collection_domain: "europol.europa.eu"
collection_date: "2026-04-08"
publish_date: "2024-02-20"
language: "en"
status: "collected"
---

## Summary
(3-5 paragraph digest of the source)

## Key Data Points
- Arrests: X
- Countries involved: X
- Agencies named: X, Y, Z
- Seizures: ...

## Original Text Excerpts
(Relevant quotes with context)
```

## Source Type Routing

| Domain Pattern | raw/ Subdirectory |
|---|---|
| interpol.int, europol.europa.eu, justice.gov, police.go.kr | `press-releases/` |
| reuters.com, bbc.com, bleepingcomputer.com, therecord.media | `news/` |
| academic journals, arxiv | `academic-papers/` |
| coe.int, unodc.org | `government-reports/` |
| Other | `news/` |
