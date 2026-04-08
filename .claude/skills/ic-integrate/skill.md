---
name: ic-integrate
description: "검증된 데이터를 wiki/ 구조에 자동 통합. 소스 요약, 작전, 기관, 국가, 범죄유형 페이지 생성·갱신. '위키 통합', 'integrate', '위키에 반영' 요청 시 사용."
---

# IC Integrate Skill

검증 완료된 데이터를 CLAUDE.md의 INGEST 워크플로우에 따라 wiki/에 통합한다.

## Integration Steps

### 1. Read CLAUDE.md
반드시 먼저 `CLAUDE.md`를 읽어 위키 스키마, 페이지 타입, frontmatter 형식을 확인한다.

### 2. Create Source Summary
`wiki/sources/{source-slug}.md` 생성. CLAUDE.md의 Source Summary 스키마 사용.

### 3. Create/Update Operation
`wiki/operations/{operation-slug}.md`:
- 존재 시: Read → Merge (새 데이터 추가, 고신뢰 수치로 갱신)
- 미존재 시: CLAUDE.md Operation 템플릿으로 생성

### 4. Update Entity Pages
각 정규화된 엔티티에 대해:
- `wiki/organizations/`: `operations_participated` 추가
- `wiki/countries/`: `operations_participated` 추가
- `wiki/crime-types/`: `notable_operations` 추가
- 미존재 시 스텁 생성

### 5. Bidirectional Links
`.claude/agents/ic-integrator.md`의 양방향 링크 테이블을 따라 모든 역링크 갱신.

### 6. Index Updates
- 각 카테고리 `_index.md` 테이블에 행 추가/갱신
- `wiki/index.md` 페이지 카운트 갱신
- `wiki/log.md`에 ingest 기록 추가

### 7. Obsidian Compatibility
- 모든 내부 링크는 `[[wikilink]]` 문법 사용
- 파일명은 slug 형식 (소문자, 하이픈)
- frontmatter는 유효한 YAML
- wiki/ 디렉토리가 Obsidian vault이므로 저장 즉시 Obsidian에 반영
