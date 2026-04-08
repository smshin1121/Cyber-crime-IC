---
name: ic-verify
description: "평가 통과 데이터의 교차 검증, 엔티티 정규화, 위키 일관성 확인. '검증', 'verify', '교차 확인' 요청 시 사용."
---

# IC Verify Skill

평가를 통과한 데이터의 정확성을 교차 검증하고 위키와의 일관성을 확인한다.

## Verification Steps

### 1. Cross-Source Validation
동일 작전에 대한 복수 소스가 있을 때:
- 수치 데이터 비교 (arrests, seizures, countries)
- 불일치 시 고신뢰 소스의 수치를 primary로 채택
- 불일치 내역을 `verification_notes`에 기록

### 2. Entity Normalization
`.claude/agents/ic-verifier.md`의 정규화 테이블을 사용하여:
- 기관명 → wiki canonical slug
- 국가명 → ISO standard + wiki slug
- 범죄유형 → taxonomy canonical name

### 3. Wiki Consistency
기존 `wiki/` 페이지를 읽어서:
- 해당 작전이 이미 문서화되어 있는지 확인
- 모순되는 수치/정보가 있는지 확인
- 스텁 페이지에 추가할 정보가 있는지 확인

### 4. Output
검증 결과를 frontmatter에 추가:
```yaml
agencies_normalized: []
countries_normalized: []
crime_types_normalized: []
cross_source_verified: false
wiki_conflicts: []
verification_notes: ""
status: "verified"
```
