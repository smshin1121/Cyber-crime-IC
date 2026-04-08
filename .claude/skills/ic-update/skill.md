---
name: ic-update
description: "사이버범죄 국제공조 위키를 최신 사례로 업데이트. '위키 업데이트', '사례 조사', '최신 작전 수집', 'update wiki', '/ic-update' 요청 시 사용. 수집→분류→평가→검증→통합→빌드→푸시 전체 사이클을 실행."
---

# IC Wiki Update — 전체 업데이트 사이클

사이버범죄 국제공조 위키를 최신 사례로 업데이트하는 원스톱 스킬.

## Workflow

### Step 1: 수집 범위 결정

사용자 입력이 있으면 해당 주제로, 없으면 기본 검색 수행:

**기본 검색 (주제 미지정 시):**
- 최근 30일 내 사이버범죄 국제공조 작전 전체
- 키워드: cybercrime international operation arrests takedown 2025

**주제 지정 시 예시:**
- "랜섬웨어 최신 작전" → ransomware international operation
- "BEC 사례" → BEC business email compromise operation
- "한국 관련" → Korea cybercrime international cooperation

### Step 2: 중복 확인

수집 전 기존 위키 작전 목록을 확인:
```
Read wiki/operations/_index.md
```
이미 수집된 작전은 제외.

### Step 3: 파이프라인 실행

ic-pipeline 오케스트레이터 실행:
1. **Collect** — WebSearch로 소스 수집 (max 10건)
2. **Classify** — 엔티티 추출
3. **Evaluate** — 품질 평가 (PASS만 진행)
4. **Verify** — 교차 검증 + 정규화
5. **Integrate** — wiki/ 에 통합

### Step 4: 정적 사이트 재빌드

```bash
python web/build_static.py
```

### Step 5: Git 커밋 + 푸시

```bash
git add -A
git commit -m "update: {날짜} 사례 업데이트 ({N}건 추가)"
git push
```

GitHub Pages가 자동으로 갱신됨.

### Step 6: 결과 보고

업데이트 요약:
- 수집: N건 → PASS: N건 → 통합: N건
- 새 작전 페이지: {목록}
- 갱신된 페이지: {목록}
- GitHub Pages URL: https://smshin1121.github.io/Cyber-crime-IC/
