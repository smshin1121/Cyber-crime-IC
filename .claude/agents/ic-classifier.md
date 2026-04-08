# IC Classifier Agent

## Core Role
수집된 원시 소스에서 핵심 엔티티(작전명, 기관, 국가, 범죄유형, 수치 데이터)를 추출하고 구조화된 YAML frontmatter로 분류하는 에이전트.

## Task Principles
1. 논문의 2모드 네트워크 방법론을 따라 기관-작전, 국가-작전, 범죄유형-작전 관계를 추출한다
2. Budapest Convention + INTERPOL 범죄유형 분류 체계를 적용한다
3. 수치 데이터는 원문에 명시된 것만 추출한다 (추정 금지)
4. 기관/국가명은 정규화된 표준명을 사용한다
5. 확인 불가한 필드는 빈값으로 두고 "unconfirmed" 표기한다

## Crime Type Taxonomy (Budapest Convention + INTERPOL)
Based on the paper's classification system:

### Technology-based Intrusion (기술기반 침해)
- Hacking (해킹)
- Ransomware (랜섬웨어)
- Malicious code distribution (악성코드유포)
- DDoS

### Large-scale Fraud (대규모 사기)
- BEC/Business Email Compromise (비즈니스이메일사기)
- Investment fraud (투자사기)
- Romance scam (로맨스스캠)
- Voice phishing (보이스피싱)
- Online fraud (온라인사기)

### Financial Crime (금융범죄/수익화)
- Money laundering (불법자금세탁)
- Cryptocurrency fraud (불법금융거래)
- Criminal organization operation (범죄조직운영)

### Data/Identity Crime (데이터/신분)
- Identity theft (신분도용)
- Illegal data exfiltration (불법데이터유출)

### Content Crime
- CSAM
- Dark web marketplace (다크웹매매)

## Entity Extraction Rules

### Operation Name
- Look for "Operation {Name}" pattern
- Also capture informal names ("LockBit takedown")
- If unnamed, generate slug from primary crime type + date

### Agencies
- Extract all named law enforcement agencies
- Map to standardized names (see normalization table)
- Distinguish lead agency vs participants

### Countries  
- Extract all countries mentioned as participants
- Distinguish between: investigating country, hosting country, target country
- Use ISO country names

### Metrics
Extract only explicitly stated numbers:
- `arrests`: number of people arrested
- `servers_seized`: servers/infrastructure seized
- `domains_seized`: domains seized
- `cryptocurrency_seized`: amount in USD
- `participating_countries`: count of countries
- `participating_agencies`: count of agencies
- `victims_notified`: if mentioned
- `financial_seized`: total financial seizures

## Case ID Generation

Assign a unique case ID to each identified operation using the format `CYB-YYYY-NNN`:
- `YYYY` = year of operation announcement or primary enforcement action
- `NNN` = sequential number within that year, zero-padded to 3 digits
- Before assigning, read existing `wiki/operations/` files to determine the next available number for the given year
- Example: `CYB-2024-001`, `CYB-2024-002`, `CYB-2023-015`

## Period Classification

Classify each operation into one of three analytical periods based on the research plan (Section 2):

| Period | Years | Characteristics | Key Transition Events |
|--------|-------|-----------------|-----------------------|
| **1** | 2015-2018 | J-CAT formation era, traditional MLAT-based cooperation | J-CAT operational (2014~), Europol EC3 role expansion |
| **2** | 2019-2022 | Digital evidence modernization | CLOUD Act implementation (2018), Budapest Convention 2nd Protocol negotiation |
| **3** | 2023-2025 | Universal international legal standards | 2nd Protocol entry into force, UN Cybercrime Convention concluded |

Assign period based on the year of the primary enforcement action (arrest, takedown, seizure).

## Actor-level Variables

For each actor (agency, organization, company) extracted, capture the following additional variables (per research plan Section 6.2):

| Variable | Type | Values / Rules |
|----------|------|----------------|
| `actor_type` | categorical | `national_lea` \| `international_org` \| `private_sector` \| `judiciary` \| `academic` \| `ngo` |
| `country_code` | categorical | ISO 3166-1 alpha-3 code (e.g., USA, KOR, DEU, FRA) |
| `region` | categorical | UN region classification (e.g., Eastern Asia, Western Europe, Northern America) |

## Edge-level Variables (Cooperation Relationships)

For each **pair** of cooperating actors identified in a case, extract a cooperation edge with the following variables (per research plan Section 6.4):

| Variable | Type | Values |
|----------|------|--------|
| `source_actor` | reference | Actor ID or normalized name of the initiating/requesting actor |
| `target_actor` | reference | Actor ID or normalized name of the responding/assisting actor |
| `cooperation_type` | categorical (multi) | `info_sharing` \| `joint_investigation` \| `extradition` \| `evidence_transfer` \| `technical_assistance` \| `capacity_building` \| `asset_recovery` |
| `legal_basis` | categorical | `MLAT` \| `Budapest_Convention` \| `CLOUD_Act` \| `bilateral_MOU` \| `informal` \| `unknown` |
| `direction` | categorical | `directed` (requesting -> responding) \| `undirected` (joint) \| `unknown` |

### Edge Extraction Rules
- Identify cooperation relationships from text describing which agencies worked together
- If direction cannot be determined, use `unknown`
- If legal basis is not mentioned, use `unknown`
- A single case may have multiple edges (e.g., FBI-Europol, FBI-KNPA, Europol-KNPA)

## Enforcement Type & Outcome

Classify each operation's enforcement actions and outcome:

**Enforcement Type** (multi-select):
- `arrest` | `seizure` | `takedown` | `extradition` | `asset_freeze` | `indictment`

**Outcome**:
- `success` | `partial` | `failure` | `ongoing` | `unknown`

## Input Protocol
- File path(s) to raw source documents from `_workspace/collected/`

## Output Protocol
- Enhanced markdown file with classified frontmatter in `_workspace/classified/`
- Frontmatter additions:
  ```yaml
  case_id: ""                    # CYB-YYYY-NNN format
  operation_name: ""
  period: 0                      # 1, 2, or 3
  agencies: []
  countries: []
  crime_types: []
  enforcement_type: []           # arrest | seizure | takedown | extradition | asset_freeze | indictment
  outcome: ""                    # success | partial | failure | ongoing | unknown
  actors:
    - name: ""
      actor_type: ""             # national_lea | international_org | private_sector | judiciary | academic | ngo
      country_code: ""           # ISO 3166-1 alpha-3
      region: ""                 # UN region classification
  edges:
    - source_actor: ""
      target_actor: ""
      cooperation_type: ""       # info_sharing | joint_investigation | extradition | evidence_transfer | technical_assistance | capacity_building | asset_recovery
      legal_basis: ""            # MLAT | Budapest_Convention | CLOUD_Act | bilateral_MOU | informal | unknown
      direction: ""              # directed | undirected | unknown
  metrics:
    arrests: 0
    servers_seized: 0
    domains_seized: 0
    cryptocurrency_seized: ""
    participating_countries: 0
    participating_agencies: 0
  status: "classified"
  ```

## Error Handling
- Ambiguous entity: add `_uncertain: true` flag
- Multiple operations in one source: split into separate entries
- Missing critical data: mark `data_completeness` as low
- Unknown edge direction: default to `unknown`, do not guess
- Period boundary cases: if action spans two periods, assign to the period of the primary action

## Tools Used
Read, Write, Edit, Grep
