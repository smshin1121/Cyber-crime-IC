---
name: ic-evaluate
description: "분류된 국제공조 데이터의 품질을 평가. 신뢰도, 적합도, 완성도 채점 및 중복 탐지. '평가', 'evaluate', '품질 점검' 요청 시 사용."
---

# IC Evaluate Skill

분류된 데이터의 품질을 3개 차원에서 채점하고 PASS/REVIEW/REJECT 판정을 내린다.

## Scoring Dimensions

### 1. Source Reliability + Credibility
`.claude/agents/ic-evaluator.md`의 NATO Admiralty Code 테이블 참조.
도메인별 기본값 적용 후 내용 기반 조정.

### 2. Topic Relevance (0-100)
가산/감산 방식:
- +30: 다국적 법집행 작전 확인
- +20: 명명된 작전 + 구체적 결과
- +15: 복수 국가 기관 명시
- +10: 범죄유형 분류 가능
- +10: 정량 지표 존재
- +5: 최근 2년 내, +5: 공식 소스, +5: 한국 참여
- -10: 구체적 집행 조치 없음
- -15: 단일 국가만, -20: 정책/교육 중심

### 3. Data Completeness (0-100)
필수 필드 가중치: `.claude/agents/ic-evaluator.md`의 필드별 가중치 테이블 참조.

## Verdict

| Verdict | Criteria |
|---------|----------|
| **PASS** | relevance >= 50 AND completeness >= 40 AND NOT duplicate |
| **REVIEW** | relevance 30-49 OR completeness 30-39 |
| **REJECT** | relevance < 30 OR duplicate OR reliability E-F |
