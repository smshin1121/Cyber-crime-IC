# Lessons Learned — Cyber_crime_IC Wiki

이 파일은 **작업 시작 시 반드시 먼저 읽는다.** CLAUDE.md에서 자동 참조한다.
같은 시행착오를 반복하지 않기 위해 누적 관리한다.

새 교훈 추가 규칙:
1. 분류(데이터 무결성 / 자동화 / 도구 / 에이전트 운영 / 외부 의존성) 중 적절한 섹션에 추가
2. 각 항목: **상황 → 왜 실패 → 교훈 → 어떻게 적용**
3. 발견 날짜와 commit 해시 기록 (검증 가능)
4. 상위 우선순위(❗)는 절대 반복 금지 항목

---

## ❗ 데이터 무결성 (Data Integrity)

### L1. 일괄 생성된 source 페이지의 파일명-URL 불일치 (2026-04-10, 31f6da7)

- **상황**: 60개 stub source 페이지를 일괄 생성할 때 파일명을 작전명 + publisher 조합으로 만들고 URL은 별도 시드에서 가져왔다. 보강 작업에서 21건이 실제로는 다른 사건/작전을 다루는 URL이었음.
  - 예: `wired-911-s5-botnet-dismantling.md` → URL은 2016 Operation Avalanche 기사
  - 예: `cbs-news-hive-ransomware.md` → URL은 2025 Phobos 랜섬웨어 기사
- **왜 실패**: 일괄 생성 시 URL 콘텐츠를 fetch해서 검증하지 않았고, 파일명을 source of truth로 가정했다.
- **교훈**: **파일명은 절대 검증된 사실이 아니다.** Source 페이지 생성·보강 시 항상 URL을 fetch하여 실제 내용과 작전 매핑을 검증해야 한다.
- **어떻게 적용**:
  - source 페이지 생성 함수는 반드시 WebFetch + 콘텐츠 검증 단계를 포함
  - WebFetch 실패 시 WebSearch로 작전명/제목 cross-check
  - 일괄 생성 후에는 lint + cross-reference 무결성 검증 필수
  - 의심되면 `> [!warning] URL/operation mismatch` 콜아웃 추가

### L2. 에이전트 보고서의 사실 검증 없이 인용 (2026-04-10, 8c93977 → 31f6da7)

- **상황**: Tier 1 팩트체크 에이전트가 "DOJ NCET 해체는 2026 초"라고 보고했고, 이를 그대로 commit message + 페이지 본문에 반영. 외부 URL 검증 단계에서 reuters URL이 404 → 실제 사실 확인하니 **2025-04-07** Blanche 메모.
- **왜 실패**: 에이전트의 출력을 fact로 취급했음. 날짜는 특히 확인하기 쉬운데 검증 없이 통과시켰다.
- **교훈**: **에이전트 보고서는 1차 자료가 아니다.** 핵심 사실(날짜, 수치, 인명, 작전명)은 별도 검증 후 반영.
- **어떻게 적용**:
  - 에이전트 결과를 commit하기 전에 핵심 fact 1-2개는 직접 확인
  - 특히 "2026 초", "최근" 같은 모호한 날짜는 자동으로 의심
  - 외부 URL 검증 + 실제 사실 cross-check를 빌드 단계에 포함

### L3. 위키의 시점이 명시되지 않은 조직 페이지 (2026-04-10, 8c93977)

- **상황**: 사용자 지적: "경찰청 사이버수사국은 현재 없는데 위키에 있다." 위키 페이지가 2014-2021의 과거 상태를 현재처럼 기술. 한국 Budapest Convention 가입도 "2024" 잘못 기록 (실제 2023 초청, 미가입).
- **왜 실패**: organization/country 스키마에 status, last_verified, history 필드가 없었다. 시점 무관 단일 snapshot으로 작성됨.
- **교훈**: **모든 엔티티는 시점이 있다.** 과거와 현재를 한 페이지에 분리, status로 명시.
- **어떻게 적용**:
  - organization 스키마 필수 필드: `status` (active|reorganized|dissolved|renamed|planned), `dissolved_date`, `successor`, `predecessor`, `last_verified`
  - 본문 섹션 필수: `## Current Status (as of {date})` + `## History and Reorganizations`
  - last_verified > 180일이면 stale, 재검증 필요
  - 캐논 예시: `wiki/organizations/knpa-cyber-bureau.md`

---

## ❗ 자동 수집 필터링

### L4. 키워드 필터의 OR 조건이 95% noise 통과시킴 (2026-04-10, 54009a9)

- **상황**: 초기 auto_collect.py 필터가 `IC_KEYWORDS = ["operation", "arrests", "europol", ...]` 단독 통과. 175 검사 → 16 false positive (이주민 밀수, 마약, 무기 거래 등).
- **왜 실패**: "operation"이 들어간 모든 Europol 보도자료 통과. 사이버 키워드를 강제하지 않음.
- **교훈**: **CYBER_KEYWORDS AND IC_KEYWORDS 양 조건 강제**. 양쪽 모두 매칭되어야 통과.
- **어떻게 적용**:
  - `is_ic_relevant()`는 반드시 두 카테고리 모두 hit 확인
  - HARD_EXCLUDE_KEYWORDS (migrant smuggling, drug trafficking, weapons)는 cyber+IC 강한 신호 시만 통과
  - SOFT_EXCLUDE_KEYWORDS (training, workshop)는 양쪽 키워드 2+ 시만 통과
  - 검증: 175 검사 → 1 승인이면 정상

### L5. 인터뷰 거부에서 학습 패턴 추출 누락 (2026-04-10, a7ff68b)

- **상황**: 사용자가 Q0001 (Europol 정책 성명)과 Q0002 (Khan 데이터 프라이버시 논문)를 모두 reject. 단순히 항목만 삭제하면 미래에 같은 종류가 반복 수집됨.
- **왜 실패**: 거부 결정에서 패턴을 추출하지 않으면 학습 안 됨.
- **교훈**: **사용자 거부는 필터 학습의 1차 자료**. 모든 reject 결정을 _workspace/rejection_log.md에 사유와 함께 기록 → 패턴 추출 → auto_collect.py 필터에 반영.
- **어떻게 적용**:
  - 거부 사유를 분석해서 POLICY_ADVOCACY_MARKERS, DATA_PRIVACY_HEAVY 같은 패턴 추출
  - 같은 종류의 항목이 재실행 시 자동 거부되는지 검증
  - 학습 검증: 175 검사 → 16 → 3 → 1로 누적 감소 확인

---

## ❗ 도구 (Tools)

### L6. 번역 placeholder의 중첩 복원 실패 (2026-04-10, 59ba5c4)

- **상황**: 사용자가 "통계 페이지에 PROT2가 보인다"고 지적. translate_content.py가 wikilink를 `__PROT0__`로 protect → table row를 `__PROT1__`로 protect (PROT0이 안에 들어감) → Google Translate가 underscore 제거 → 복원 시 실패.
- **왜 실패**: (1) underscore 플레이스홀더가 GT에 의해 mangled, (2) 단일 pass 정방향 복원이라 외부 → 내부 순서 복원 못함.
- **교훈**: **플레이스홀더는 (a) GT가 손대지 않는 형식 (uppercase ZZZ로 감싸기), (b) 중첩 복원은 역방향 + 다중 pass.**
- **어떻게 적용**:
  - 플레이스홀더 형식: `ZZPROTZZ{n}ZZENDZZ` (underscore/space/기호 없음)
  - 복원: `for _pass in range(10): for key in reversed(protected): replace(key, val)`
  - 검증: `grep "ZZPROT\|>PROT[0-9]" docs/` = 0건

### L7. codesight 1.10 두 가지 버그 회피 (2026-04-10, 54009a9)

- **상황**: `npx codesight tools -o /abs/path` → ENOENT (절대경로가 scan dir에 prepend됨). `.codesightignore`가 root scan에서 무시됨 → 위키 마크다운을 코드로 잘못 분류.
- **왜 실패**: 1.10의 기능 미완성. issue 보고된 적 없음.
- **교훈**: **외부 도구는 한 번 동작 검증 후 신뢰**. 버전 변경 후 재검증.
- **어떻게 적용**:
  - 헬퍼 스크립트로 buggy 동작 우회: `tools/codesight_scan.py`
    - 절대경로 대신 `<src>/.codesight/`에 쓰고 후처리 이동
    - 모듈별 개별 스캔 (root scan 대신 tools/, web/ 따로)
  - codesight 1.11+ 출시 시 헬퍼의 우회 로직 제거 가능한지 재검증

### L8. Windows cp949 인코딩으로 unicode 출력 실패 (2026-04-10, 54009a9 / 2026-04-13 추가)

- **상황 (1)**: `print("✔ Task registered.")` → UnicodeEncodeError 'cp949'. 작업 등록 자체는 성공했지만 print 단계에서 오류.
- **상황 (2, 2026-04-13)**: `tools/scheduled_collect.bat`의 `REM 사이버범죄 국제공조...` 한글 주석이 cp949 cmd 환경에서 깨져서 **바로 다음 줄** `python tools\auto_collect.py` 파싱까지 오염 → `'to_collect.py'은(는) 내부 또는 외부 명령이 아닙니다`. 배치 자체는 exit 0이라 Task Scheduler는 "성공"으로 기록. state 파일 mtime이 갱신 안 된 점으로만 실패 감지 가능.
- **왜 실패**: Windows 한국어 cmd의 기본 encoding은 cp949. 파이썬 `print`는 stdout encoding 따름. **그리고 cmd.exe 자체가 .bat 파일을 cp949로 디코딩**하므로 UTF-8로 저장된 한글 주석이 non-ASCII 바이트로 읽혀 인접 라인 파싱까지 깨뜨림.
- **교훈**: **Windows 환경에서 unicode 사용 금지 영역 두 곳**:
  1. 파이썬 `print` 출력 (stdout 경유)
  2. **`.bat`/`.cmd` 파일 내용 전체** (주석 포함)
- **어떻게 적용**:
  - 파이썬: 모든 print에서 ✔ ✘ ⚠ → `[OK]` `[FAIL]` `[WARN]`, 또는 `sys.stdout.reconfigure(encoding='utf-8')`
  - 배치 파일: `REM` 주석도 ASCII-only. 파일 상단에 `ASCII-only: Korean comments corrupt parsing under cp949` 경고 주석 필수.
  - Task Scheduler 진단: `schtasks` "Last Result: 0"은 **배치 exit 코드일 뿐** 실제 성공을 의미하지 않음. state 파일 mtime 또는 로그 파일 존재 여부로 교차 검증.
  - 중요: 작업 자체와 print를 분리. print 실패해도 작업은 성공해야 함.

### L9. URL 정규식이 균형 괄호를 처리 못함 (2026-04-10, 518ef59)

- **상황**: Wikipedia URL `https://en.wikipedia.org/wiki/National_Police_Agency_(Japan)`에서 정규식 `[^)]+`가 `(Japan` 까지만 captures. fix script가 `(Japan)`로 치환했더니 파일에 `(Japan))` 이중 괄호 발생.
- **왜 실패**: URL 정규식이 균형 괄호 미지원, fix가 잘린 substring을 substring 그대로 replace.
- **교훈**: **URL 정규식은 균형 괄호 지원해야**. fix 시에도 already-correct 형태 검증.
- **어떻게 적용**:
  - URL 정규식: `https?://[^\s\]\"'<>]+` 후 `while raw.endswith(")") and raw.count("(") < raw.count(")"): raw = raw[:-1]`
  - fix script는 idempotent해야: 이미 fixed된 URL은 건드리지 않음
  - 자동 fix 후 link check로 검증

---

## ❗ 에이전트 운영

### L10. 다수 background agent 동시 실행 시 인증 오류 빈발 (2026-04-10, 23d1464)

- **상황**: 8개 background agent 동시 spawn 시 5개가 "Not logged in" 또는 529 overload로 실패. 부분 결과만 저장됨.
- **왜 실패**: 동시 인증 갱신 또는 API rate limiting.
- **교훈**: **8개 동시 background agent는 불안정**. 3-4개씩 batch로 줄이고 재시도 메커니즘 필요.
- **어떻게 적용**:
  - background agent 동시 실행은 최대 3-4개
  - 실패 시 같은 작업을 foreground 또는 직접 실행으로 fallback
  - 부분 결과 확인하여 누락된 항목만 retry
  - 에이전트가 silent하게 실패할 수 있으므로 결과 파일 존재 확인 필수

### L11. WebFetch가 자주 차단되는 사이트 패턴 (2026-04-10, 518ef59)

- **상황**: Wired, BBC, FBI.gov, Group-IB, 한국 뉴스 사이트가 WebFetch 시 403/blocked. 이들이 broken처럼 보였음.
- **왜 실패**: 이 사이트들이 Cloudflare/Akamai bot 보호. HEAD/GET requests에 challenge 페이지 반환.
- **교훈**: **WebFetch 실패 = URL dead가 아니다**. WebSearch fallback으로 같은 사실을 다른 출처에서 cross-check.
- **어떻게 적용**:
  - BOT_PROTECTED_DOMAINS whitelist (35개 도메인): coe.int, interpol.int, justice.gov, fbi.gov, rcmp-grc.gc.ca, wired.com, bbc.com 등
  - WebFetch 실패 시 WebSearch with operation name → 1차 출처(.gov, .europa.eu) 발견
  - 검증 시 Cloudflare challenge 페이지 ("Just a moment...") 감지 로직

---

## ❗ 외부 의존성

### L12. 외부 URL 검증을 빌드에 포함하지 않았음 (2026-04-10, 518ef59)

- **상황**: 사용자가 "interpol.int 페이지가 죽었다. 각 링크별로 확인했나?" 지적. 기존 check_links.py는 외부 URL 건너뛰기. 1432개 외부 URL 미검증.
- **왜 실패**: 빌드 도구는 내부 링크만 체크. 외부 URL은 별도 정책 필요해서 미루다가 잊음.
- **교훈**: **외부 URL 검증은 별도 도구로, 정기 실행**. 검증 결과를 사용자에게 보고.
- **어떻게 적용**:
  - tools/check_external_urls.py: HEAD/GET + Cloudflare challenge 감지 + Wayback fallback
  - BOT_PROTECTED_DOMAINS whitelist (~35 도메인)
  - Wayback 자동 치환: archive.org/wayback/available API
  - 정기 실행: 자동 수집 스케줄과 함께
  - 100% broken 0건 달성 후 push

### L13. coe.int 등 정부 사이트 Cloudflare bot 보호 (2026-04-10, 518ef59)

- **상황**: 1차 외부 URL 검증에서 coe.int 55건이 모두 broken으로 분류. 실제로는 브라우저에서 정상 접속.
- **왜 실패**: Cloudflare가 비-브라우저 클라이언트에 challenge 페이지 + 403 반환.
- **교훈**: **정부/법집행 사이트는 거의 모두 Cloudflare 보호.** 403 = "broken" 가정 금지.
- **어떻게 적용**:
  - challenge 페이지 감지: response body에 "Just a moment..." 또는 "challenge-platform" 포함
  - 도메인 whitelist에 추가
  - 새 도메인 발견 시 브라우저로 1회 확인 후 whitelist 업데이트

---

## ❗ 작전 페이지 데이터 무결성

### L16. source mismatch가 operation 페이지 전체를 오염시킨다 (2026-04-10, 54e652d)

- **상황**: `botnet-takedown-europol-2023.md` 작전 페이지가 "2023년 봇넷 takedown"으로 기록되어 있었다. 실제로는 Europol 소스 URL이 **2015-02-24 Ramnit 봇넷 takedown** 보도자료. 날짜, 참가국, 결과 등 페이지의 모든 메타데이터가 잘못된 가정에서 생성됨.
- **왜 실패**: source 일괄 생성 시 URL 내용을 검증하지 않았고(L1), 잘못된 source → 잘못된 operation 페이지가 자동 생성됨. 이후 해당 페이지를 참조하는 다른 페이지(europol-ec3, eurojust 등)에도 잘못된 wikilink가 전파됨.
- **교훈**: **source mismatch는 단일 파일 문제가 아니라 전파된다.** 잘못된 source가 operation 페이지를 만들고, 그 operation이 org/country 페이지에 참조되면 오류가 연쇄 전파.
- **어떻게 적용**:
  - source mismatch 발견 시 → 해당 source를 참조하는 operation 페이지도 검증
  - operation 페이지 → 해당 operation을 참조하는 org/country 페이지도 검증
  - `grep -rl "잘못된-페이지명" wiki/` 로 전파 범위 확인
  - 리네임 시 모든 wikilink + _index.md 동시 갱신

### L17. participating_countries 목록은 공식 출처로 교차 검증 필수 (2026-04-10, 54e652d)

- **상황**: operation-avalanche의 participating_countries가 13개국으로 기록. Europol 공식 보도자료에는 **30개국** 명시. 본문에는 "30+ countries"라고 쓰여 있으면서 frontmatter에는 13개만 나열.
- **왜 실패**: 초기 생성 시 일부 출처만 참고하여 주요 국가만 나열. frontmatter과 본문의 일관성 검증 없음.
- **교훈**: **frontmatter 수치와 본문 서술이 불일치하면 반드시 공식 출처로 검증.** 특히 participating_countries는 Europol/INTERPOL 보도자료에서 전체 명단을 확인.
- **어떻게 적용**:
  - 작전 페이지 생성/보강 시 공식 보도자료 URL을 WebFetch하여 국가 전체 명단 추출
  - frontmatter의 `participating_countries` 배열 길이와 본문 "N countries" 서술이 일치하는지 검증
  - lint에 frontmatter-본문 수치 불일치 체크 추가 고려

---

## ❗ 도구 / 인프라

### L18. Windows schtasks는 DAILY에 복수 시간 미지원 (2026-04-10, 54e652d)

- **상황**: 자동 수집을 1일 3회(아침/점심/저녁)로 변경하려 했으나, `schtasks /SC DAILY /ST` 은 단일 시간만 지원. 하나의 태스크에 07:00,12:00,19:00 을 동시에 지정 불가.
- **왜 실패**: Windows Task Scheduler의 `/SC DAILY` 는 하루 1회 실행만 지원. 복수 시간은 별도 태스크로 분리해야.
- **교훈**: **3회/일 스케줄 = 3개 별도 태스크.** 태스크명에 AM/NOON/PM 접미사로 구분. 레거시 단일 태스크는 자동 제거.
- **어떻게 적용**:
  - `register_scheduler.py`가 `_parse_schedules("07:00,12:00,19:00")` → 3개 `(CyberCrimeIC_AM, 07:00)` 등으로 분리
  - `register` 시 레거시 `CyberCrimeIC_AutoCollect` 자동 삭제
  - `status` 시 3개 모두 확인 + 레거시 잔존 경고

---

## 메타 교훈

### L14. 사용자가 작은 결함을 지적하면 같은 패턴이 N개 더 있다

- **상황**: 사용자가 "Wired Infraud 페이지 내용이 별로 없다" 한 페이지 지적. 검사하니 60개 동일 stub 발견.
- **왜 실패**: 일괄 생성 작업의 일관된 결함이 한 번에 모든 페이지에 적용됨.
- **교훈**: **사용자가 1개 지적 → grep 패턴으로 N개 검색**. 한 페이지만 고치고 끝내지 말 것.
- **어떻게 적용**:
  - 결함 발견 시: 동일 패턴 검색 (`grep -L "key_findings:.*[a-zA-Z]" wiki/sources/*.md`)
  - 1건 수정 후 N건 일괄 처리 도구 작성
  - 사용자에게 "이 패턴이 전체 N건 발견됨, 일괄 처리하겠다"고 보고

### L15. PoC + 시범 실행으로 검증 후 양산

- **상황**: 자동 수집 필터 강화 + auto_collect 확장 → 실제 1회 실행 → 16 false positive → 필터 보강 → 1 승인까지 반복. 인터뷰 학습 → 재실행 검증.
- **교훈**: **새 도구 추가 시 반드시 1회 시범 실행 + 결과 검증 후 commit**. 코드만 추가하고 동작 안 보면 버그 누적.
- **어떻게 적용**:
  - 새 자동화 도구는 dry-run 또는 1회 실제 실행 후 결과 확인
  - 결과가 기대와 다르면 즉시 보강
  - 양산 적용 (스케줄 등록) 전에 사용자 검토

---

## 작업 시작 시 점검 체크리스트

새 작업/세션 시작 시 이 항목을 확인:

- [ ] LESSONS.md를 읽었는가?
- [ ] 작업 영역(데이터 / 자동화 / 도구 / 에이전트)에 해당하는 lesson을 인지했는가?
- [ ] 새 source/operation 페이지 생성이라면 → L1, L2 (URL 검증, 에이전트 보고 검증)
- [ ] source mismatch 정리라면 → L16 (전파 범위: source→operation→org/country 순서로 추적)
- [ ] operation 페이지 생성/보강이라면 → L17 (participating_countries 공식 출처 교차 검증)
- [ ] 자동 수집 관련이라면 → L4, L5 (양 조건 필터, 학습 루프)
- [ ] 새 외부 도구 사용이라면 → L7, L8 (버그 회피, 인코딩)
- [ ] 스케줄러 변경이라면 → L18 (schtasks DAILY 복수 시간 = 별도 태스크)
- [ ] 다수 background agent 사용한다면 → L10 (3-4개 한도, 부분 실패 대비)
- [ ] WebFetch 실패라면 → L11 (WebSearch fallback)
- [ ] 빌드 후 → check_links + check_external_urls + ZZPROT grep
- [ ] 사용자가 1건 결함 지적 → L14 (grep으로 N건 검색)

새 lesson 추가 시:
1. 해당 카테고리에 L<번호> 추가
2. (날짜, commit hash) 명시
3. 상위 우선순위라면 ❗ 표시
4. MEMORY.md에 한 줄 인덱스 추가 (선택)
