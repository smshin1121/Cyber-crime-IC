---
name: ic-classify
description: "수집된 사이버범죄 국제공조 소스에서 엔티티(작전명, 기관, 국가, 범죄유형, 수치)를 추출하고 분류. '분류', 'classify', '엔티티 추출' 요청 시 사용."
---

# IC Classify Skill

수집된 원시 소스를 읽고 핵심 엔티티를 추출하여 구조화된 YAML frontmatter로 분류한다.

## Extraction Checklist

소스를 읽을 때 반드시 추출할 항목:

- [ ] **Operation name**: "Operation {Name}" 패턴 또는 비공식 명칭
- [ ] **Lead agency**: 주도 기관
- [ ] **Participating agencies**: 참여 기관 전체 목록
- [ ] **Participating countries**: 참여 국가 전체 목록
- [ ] **Crime types**: Budapest Convention + INTERPOL 분류 체계 (`.claude/agents/ic-classifier.md` taxonomy 참조)
- [ ] **Arrests**: 체포 인원수
- [ ] **Servers seized**: 압수 서버수
- [ ] **Domains seized**: 압수 도메인수
- [ ] **Financial seized**: 압수 금액 (USD)
- [ ] **Cryptocurrency seized**: 암호화폐 압수 금액
- [ ] **Timeframe**: 작전 시작/종료일
- [ ] **Victims notified**: 피해자 통보 수

## Output Frontmatter

Read the source, then add these fields to the frontmatter:

```yaml
operation_name: ""
operation_type: ""           # takedown | arrest-sweep | infrastructure-seizure | joint-investigation
agencies: ["agency1", "agency2"]
lead_agency: ""
countries: ["country1", "country2"]
crime_types: ["type1", "type2"]
metrics:
  arrests: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  participating_countries: 0
  participating_agencies: 0
  victims_notified: 0
  financial_seized: ""
timeframe:
  start: ""
  end: ""
  announced: ""
status: "classified"
```

## Rules
- Only extract **explicitly stated** numbers. Never estimate.
- If a field is unclear, leave empty and add `_notes: "ambiguous"`.
- If one source covers multiple distinct operations, split into separate files.
