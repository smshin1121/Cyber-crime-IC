# LLM Wiki for International Cooperation on Cyber Crime - Design Document

> Version: 2.0 | Date: 2026-04-08 | Status: Draft
> Domain: 사이버범죄 국제공조 (International Cooperation on Cyber Crime)

---

## 1. Project Overview

### 1.1 Purpose

사이버범죄 국제공조에 관한 지식을 체계적으로 축적하기 위한 LLM 기반 위키 시스템. LLM이 원시 소스를 읽고 **지속적으로 유지보수되는 마크다운 위키**를 증분적으로 구축/갱신한다. "누가 공격하는가"가 아니라 **"국가들이 어떻게 협력하여 수사하고 기소하는가"**에 초점을 맞춘다.

### 1.2 Core Principles

| Principle | Description |
|-----------|-------------|
| **Persistent Artifact** | 위키는 누적 산출물. 소스 추가 시마다 풍부해진다 |
| **LLM as Maintainer** | 사용자는 소스 큐레이션과 질문, LLM은 요약/교차참조/정리 |
| **Source Immutability** | 원시 소스는 절대 수정하지 않는다 (append-only) |
| **Bidirectional Linking** | 모든 관계는 양방향 유지 |
| **Legal Precision** | 법적 용어와 상태에 정확성 요구 |
| **Sensitivity Awareness** | 수사/외교 민감 정보 보호 |

### 1.3 Domain: 사이버범죄 국제공조

위키가 다루는 6가지 핵심 질문:

1. **누가 협력하는가?** — organizations/, countries/
2. **어떤 권한 하에?** — legal-frameworks/
3. **어떤 채널을 통해?** — mechanisms/
4. **구체적으로 어떻게?** — procedures/
5. **무엇을 위해?** — operations/, cases/, crime-types/
6. **무엇이 장벽인가?** — challenges/, concepts/

---

## 2. Architecture

### 2.1 Three-Layer Architecture

```
┌────────────────────────────────────────────────────┐
│                    Schema Layer                      │
│           CLAUDE.md (LLM 운영 지침서)                 │
├────────────────────────────────────────────────────┤
│                    Wiki Layer                        │
│   wiki/ (LLM이 생성·유지하는 구조화된 마크다운 위키)     │
├────────────────────────────────────────────────────┤
│                Raw Sources Layer                     │
│       raw/ (불변 원시 소스 — 조약문, 판결문, 보고서 등)   │
└────────────────────────────────────────────────────┘
```

### 2.2 Directory Structure

```
Cyber_crime_IC/
├── CLAUDE.md                    # Schema — LLM 운영 지침
├── DESIGN.md                    # 본 설계문건
├── llm-wiki.md                  # 원본 패턴 문서 (참조)
│
├── raw/                         # 원시 소스 (IMMUTABLE)
│   ├── treaties/                # 조약, 협약, MOU
│   ├── case-documents/          # 기소장, 법원 명령, 판결문
│   ├── government-reports/      # 정부 보고서, 평가서
│   ├── academic-papers/         # 학술 논문, 법학 리뷰
│   ├── news/                    # 공동 수사, 체포, 인도 뉴스
│   ├── policy-documents/        # 정책 문서, 권고안, 백서
│   ├── conference-proceedings/  # Octopus Conference, GLACY+ 등
│   ├── legislation/             # 각국 사이버범죄법, 절차법
│   ├── press-releases/          # DOJ, Europol, INTERPOL 보도자료
│   ├── mutual-legal-assistance/ # MLAT 요청 템플릿, 가이드, 통계
│   └── assets/                  # 이미지, 다이어그램
│
├── wiki/                        # 위키 (LLM-GENERATED)
│   ├── index.md                 # 마스터 카탈로그
│   ├── log.md                   # 활동 로그 (append-only)
│   ├── overview.md              # 국제공조 현황 종합
│   │
│   ├── legal-frameworks/        # 조약, 협약, 양자/다자 협정
│   ├── organizations/           # 국제기구, 수사기관, 검찰
│   ├── countries/               # 국가 프로필 (법제, 역량, 실적)
│   ├── operations/              # 합동 수사, 테이크다운
│   ├── cases/                   # 국제공조 요소 포함 형사 사건
│   ├── mechanisms/              # 공조 채널 (MLAT, 24/7 Network, JIT)
│   ├── procedures/              # 절차 가이드 (증거 보전, 인도 등)
│   ├── crime-types/             # 범죄 유형별 공조 특성
│   ├── challenges/              # 장벽 (관할권, 데이터 주권 등)
│   ├── concepts/                # 법적 원칙 (쌍방가벌성, 영토주의 등)
│   ├── sources/                 # 소스 요약 (raw 1:1 대응)
│   ├── analysis/                # 합성 분석 (쿼리 결과 저장)
│   └── timelines/               # 시간순 이벤트 시퀀스
│
└── tools/                       # CLI 도구
    ├── treaty-status.py         # 조약 가입 현황 조회
    ├── country-sync.py          # 국가 데이터 동기화
    ├── lint.py                  # 위키 건강 점검
    └── search.py                # 위키 검색
```

### 2.3 File Naming Conventions

| Directory | Pattern | Example |
|-----------|---------|---------|
| `raw/*` | `YYYY-MM-DD_source_slug.md` | `2001-11-23_coe_budapest-convention.md` |
| `legal-frameworks/` | `{treaty-slug}.md` | `budapest-convention.md` |
| `organizations/` | `{org-slug}.md` | `europol-ec3.md` |
| `countries/` | `{country-slug}.md` | `south-korea.md` |
| `operations/` | `{operation-slug}.md` | `operation-cronos.md` |
| `cases/` | `{case-slug}.md` | `us-v-kondratiev-lockbit.md` |
| `mechanisms/` | `{mechanism-slug}.md` | `mlat-process.md` |
| `procedures/` | `{procedure-slug}.md` | `emergency-data-preservation.md` |
| `crime-types/` | `{crime-type-slug}.md` | `ransomware-ic.md` |
| `challenges/` | `{challenge-slug}.md` | `data-sovereignty.md` |
| `concepts/` | `{concept-slug}.md` | `dual-criminality.md` |

---

## 3. Page Types & Frontmatter Schemas

### 3.1 Page Type Taxonomy

| Type | Directory | Description |
|------|-----------|-------------|
| `legal-framework` | `legal-frameworks/` | 조약, 협약, 양자/다자 협정, 의정서 |
| `organization` | `organizations/` | 국제기구, 수사기관, 검찰, 네트워크 |
| `country` | `countries/` | 국가별 법제, 역량, 공조 실적 프로필 |
| `operation` | `operations/` | 합동 수사, 테이크다운, 인프라 압수 |
| `case` | `cases/` | 국제공조 요소 포함 형사 기소/재판 |
| `mechanism` | `mechanisms/` | 공조 채널, 네트워크, 플랫폼 |
| `procedure` | `procedures/` | 공조 절차 가이드 (step-by-step) |
| `crime-type` | `crime-types/` | 범죄 유형별 공조 특성 및 과제 |
| `challenge` | `challenges/` | 공조 장벽, 마찰점, 정책 논쟁 |
| `concept` | `concepts/` | 법적 원칙, 교리, 기술 용어 |
| `source` | `sources/` | 원시 소스 1:1 요약 |
| `analysis` | `analysis/` | 합성 분석, 비교 연구, 갭 분석 |
| `timeline` | `timelines/` | 시간순 이벤트 시퀀스 |

### 3.2 Key Frontmatter Schemas

(각 타입별 상세 스키마는 CLAUDE.md에 정의)

**Legal Framework** 핵심 필드:
- `framework_type`: convention | protocol | bilateral-treaty | mou | model-law | un-resolution
- `status`: in-force | not-yet-in-force | superseded | draft | under-negotiation
- `parties.states_parties`, `parties.notable_non_parties`
- `scope`: substantive_law, procedural_law, international_cooperation, jurisdiction, evidence
- `implementing_mechanisms`: 이 조약이 가능하게 하는 메커니즘 (wikilinks)

**Country Profile** 핵심 필드:
- `legal_system`: common-law | civil-law | mixed
- `cybercrime_legislation`: primary_law, procedural_powers, data_retention
- `treaty_memberships`: framework별 가입 상태
- `central_authority`: MLAT/Budapest 중앙당국 정보
- `ic_capacity`: rating, digital_forensics, 24_7_availability, avg_mlat_response_days

**Operation** 핵심 필드:
- `operation_type`: takedown | joint-investigation | arrest-sweep | infrastructure-seizure
- `lead_agency`, `coordinating_body`
- `participating_countries`, `participating_agencies`
- `legal_basis`, `mechanisms_used`
- `results`: arrests, indictments, servers_seized, cryptocurrency_seized

**Case** 핵심 필드:
- `case_type`: prosecution | extradition | asset-forfeiture | mutual-legal-assistance
- `status`: indicted | fugitive | arrested | extradited | convicted | sentenced
- `defendants`: name, nationality, status, sentence
- `ic_elements`: mlat_requests, extradition, evidence_from_abroad, foreign_arrests

---

## 4. Cross-Referencing Strategy

### 4.1 Cooperation-Centric Graph

| Relationship | From → To | Forward Field | Backward Field |
|---|---|---|---|
| 조약이 메커니즘 가능하게 함 | legal-framework → mechanism | `implementing_mechanisms` | `legal_basis` |
| 국가가 조약에 가입 | country → legal-framework | `treaty_memberships` | parties count |
| 기관이 작전에 참여 | organization → operation | `operations_participated` | `participating_agencies` |
| 작전이 메커니즘 사용 | operation → mechanism | `mechanisms_used` | `operations_using` |
| 사건이 작전에서 기소 | case → operation | `related_operation` | `related_cases` |
| 국가가 작전에 참여 | country → operation | `operations_participated` | `participating_countries` |
| 개념이 사건에 적용 | concept → case | `applied_in_cases` | `key_legal_issues` |
| 범죄유형이 작전 대상 | crime-type → operation | `notable_operations` | `crime_type` |
| 기관이 국가에 소속 | organization → country | `country` | `key_agencies` |

### 4.2 Graph Hub Entities

가장 많은 링크가 집중되는 허브:
1. **부다페스트 협약** — 거의 모든 국가, 메커니즘, 작전 페이지에서 참조
2. **Europol EC3 / INTERPOL IGCI** — 중앙 조정 기관
3. **MLAT 프로세스** — 가장 보편적 메커니즘
4. **미국** — 가장 많은 대형 수사/기소 관여
5. **랜섬웨어** — 현재 가장 활발한 국제공조 대상 범죄유형

---

## 5. Core Operations

### 5.1 Ingest

공통 플로우는 CTI 위키와 동일 (READ → EXTRACT → CREATE source → UPDATE entities → LINK → INDEX → LOG → FLAG).

**Source Type별 기본값:**

| Source Type | Default Reliability | Default Credibility | Primary Extraction |
|---|---|---|---|
| `treaty-text` | high | confirmed | 조항, 범위, 당사국, IC 관련 조문 |
| `case-document` | high | confirmed | 피고인, IC 요소, 법적 근거, 결과 |
| `government-report` | high | probably-true | 통계, 평가, 권고, 국가 데이터 |
| `legislation` | high | confirmed | 범죄 규정, 수사 권한, 형량 |
| `press-release` | high | probably-true | 수사 결과, 참여 기관, 공식 성명 |
| `academic-paper` | medium-high | probably-true | 법적 분석, 비교법적 프레임워크 |
| `news` | medium | possibly-true | 작전 세부사항, 체포 보도 |
| `policy-document` | medium-high | probably-true | 정책 입장, 개혁 제안 |
| `conference-proceeding` | medium | possibly-true | 전문가 의견, 실무 인사이트 |

### 5.2 Query

**실무 쿼리 (Operational):**
- 국가 공조 역량 프로필
- 메커니즘 선택 의사결정 (속도/형식성별)
- 절차 워크스루 (한국→미국 MLAT 단계별)
- 판례 선례 검색 (쌍방가벌성이 쟁점이 된 사건)

**전략 쿼리 (Strategic):**
- 지역별 공조 역량 갭 분석
- 메커니즘 비교 (MLAT vs. Budapest Art.29 vs. 직접 요청)
- 조약 영향 분석 (UN 사이버범죄 협약 발효 시 변화)
- 역량 구축 우선순위 매트릭스

**한국 특화 쿼리:**
- 한국 검찰의 대미 MLAT 요청 절차
- 부다페스트 협약 가입 후 실무 변화
- 한국 참여 국제 공동수사 사례
- 한국-미국 사이버범죄 공조 현황

### 5.3 Lint

**CRITICAL:** 양방향 링크 깨짐, 고아 페이지, 출처 누락, 조약 가입 불일치, 법적 상태 모순
**HIGH:** 낡은 페이지(180일+), 법적 근거 누락(작전), 국가 프로필 불완전, IC 요소 없는 사건
**MEDIUM:** 인덱스 미등록, 미문서화 개념, 절차 미완성, 한국 관점 누락
**LOW:** frontmatter 불완전, 명명 규칙 위반, 다국어 용어표 미작성

---

## 6. Domain-Specific Considerations

### 6.1 민감도 분류 (Sensitivity)

TLP 대신 법/수사 도메인에 맞는 민감도 분류:

| Level | Description | Wiki Handling |
|---|---|---|
| `public` | 공개 법원 문서, 보도자료, 조약문 | 제한 없이 기록 |
| `restricted` | 비공개 운영 세부, 내부 평가 | `> [!caution] Restricted` callout + 기밀 삭제 |
| `confidential` | 진행 중 수사, 외교 통신, 봉인 기소장 | 내용 기록 금지. 존재와 주제만 기록 |

### 6.2 법적 정밀성 (Legal Precision)

- "법 위의 법"과 "실무상의 법"을 구분
- 조약/법률의 **구체적 조문** 인용 (이름만이 아닌)
- 법적 정보의 **기준 일자** 명시
- 구속력 있는 문서와 비구속 문서 구분
- 정확한 법적 용어: signature ≠ ratification ≠ accession

### 6.3 다국어 법률 용어

- 영어를 위키 주 언어로 사용
- 한국어 번역을 괄호로 병기: "dual criminality (쌍방가벌성)"
- 개념 페이지에 다국어 용어표 유지
- 번역 불확실성 시 `> [!note] Translation note` 사용

### 6.4 법체계 차이

- Common Law (영미법): 대심주의, 판례법, 검찰 증거개시
- Civil Law (대륙법/한국): 직권주의 요소, 성문법, 판사 주도 수사
- 이 차이가 증거 수집, 생산명령, 인도에 미치는 영향을 국가/절차 페이지에 기술

### 6.5 외교적 고려

- 국가 공조 의지에 대한 가치 판단은 복수 소스 + 신뢰도 언어 필수
- 국가/법체계에 대한 비하적 표현 금지
- 조약 협상에서 모든 유의미한 입장 균형 있게 제시
- 조약 미가입 이유의 단순화 금지

---

## 7. Implementation Phases

### Phase 1: Foundation (완료)
- [x] Git 저장소 초기화
- [x] 디렉토리 구조 생성
- [x] CLAUDE.md, DESIGN.md 작성
- [x] 초기 wiki 파일 생성

### Phase 2: Core Content Bootstrap
- [ ] 부다페스트 협약 페이지 작성 (핵심 허브 엔티티)
- [ ] 주요 국제기구 페이지 (INTERPOL, Europol EC3, FBI Cyber)
- [ ] 한국 관련 기관 페이지 (경찰청 사이버수사국, 대검찰청)
- [ ] 주요 메커니즘 페이지 (MLAT, 24/7 Network, JIT)
- [ ] 핵심 개념 페이지 (쌍방가벌성, 영토주의 원칙)

### Phase 3: First Ingest Cycle
- [ ] 5-10개 고품질 소스 수집 (조약문, 주요 판례, 보고서)
- [ ] 인제스트 워크플로우 검증
- [ ] CLAUDE.md 튜닝

### Phase 4: Tooling
- [ ] `tools/lint.py` 구현
- [ ] `tools/search.py` 구현
- [ ] `tools/treaty-status.py` 구현

### Phase 5: Steady State
- [ ] 정기 소스 수집 + 인제스트 루틴
- [ ] 월간 린트 패스
- [ ] 분석 쿼리 → analysis 페이지 축적
