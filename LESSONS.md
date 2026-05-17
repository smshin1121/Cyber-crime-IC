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

### L21. Akamai Bot Manager(justice.gov/DOJ)는 meta-refresh + bm-verify 세션으로 뚫는다 (2026-04-21)

- **상황**: DOJ (`justice.gov`, `usao-*`) URL이 `curl_cffi` TLS 스푸핑 성공(200 OK)인데 본문이 ~3KB 짜리 `<meta http-equiv="refresh">` 페이지. 실제 기사 내용은 뒤따르지 않음.
- **원인**: Cloudflare가 아니라 Akamai Bot Manager. 첫 요청에서 `bm-verify` 쿠키를 설정하고 몇 초 뒤 meta-refresh로 같은 URL을 재요청시켜 bot 여부를 재검증.
- **돌파구**: `curl_cffi.Session()`으로 첫 요청의 쿠키 유지 → meta-refresh URL 파싱 → `time.sleep(5.5)` → 같은 세션으로 재요청 → 실제 본문(~100KB) 응답.
- **교훈**: **"200 OK인데 본문 < 8KB이고 `bm-verify` 있음 = Akamai challenge."** Cloudflare/SPA 파이프라인과 별도의 3번째 케이스로 처리. 웹 차단은 한 가지 메커니즘이 아니다.
- **어떻게 적용**:
  - `tools/web_verify_tls.py`의 `fetch_text()`가 이 challenge 패턴 감지 시 meta-refresh URL 추출 → 5.5초 대기 → 동일 session으로 재요청
  - rate limit 때문에 DOJ 페이지당 +5.5초 추가 소요 (배치 처리 시 고려)

---

### L23. operation/case 페이지의 lead_agency·coordinating_body 평문 문자열은 build_static.py가 wikilink로 오인 (2026-05-09)

- **상황**: iter 100 milestone integrity sweep에서 check_links broken 5건 발견. greek-daoe-crypto-investment-fraud-2026, hungary-romania-swatting-doxing-discord-2026, lai-chau-cambodia-bokor-transnational-online-fraud-takedown-2025 의 frontmatter `lead_agency:`/`coordinating_body:` 가 긴 평문 문자열 (예: "Készenléti Rendőrség Nemzeti Nyomozó Iroda (KR NNI) Kiberbűnözés Elleni Főosztály") 으로 채워져 있을 때, `web/build_static.py` 가 이를 미존재 wikilink target 으로 처리해 `wiki/_missing/<plain string>.html` 를 가리키는 dead link 5개 생성.
- **왜 실패**: 빌더가 `lead_agency`/`coordinating_body` field 의 plain-text 값을 entity reference 로 자동 lookup. 해당 entity page 가 없으면 "missing" page placeholder. 위키 페이지가 없는 외국 LE 기관 (특히 Hungarian/Vietnamese/Korean script 명칭) 일수록 발생 빈도 높음.
- **교훈**: **`lead_agency` / `coordinating_body` frontmatter 는 (1) `[[wikilink]]` 가 존재 entity 를 가리키거나, (2) 빈 문자열 `""` 둘 중 하나여야 한다. 평문 entity 명을 적으면 빌드 시점에 dead link 생성.** 기관 description/role 정보는 본문 prose 에 적어 보존.
- **어떻게 적용**:
  - 새 operation/case ingest 시 ingest agent 가 `lead_agency:` / `coordinating_body:` 에 평문 문자열을 넣지 못하도록 strict 규칙 추가
  - Existing pages 에서 평문 frontmatter 값 발견 시 → 빈 문자열로 교체, 본문 prose 에 동등한 정보 보존
  - `wiki/_missing/*.html` dead link 가 check_links 에 새로 떠오르면 즉시 frontmatter 점검

---

### ❗ L26. operation `## Background` must describe the crime, not just the operation (2026-05-17, iter 202 retrospective)

- **상황**: 60+ iters of new-ingest + 22 content-enrichment events produced op pages where `## Background` often restated the operation context ("Operation Endgame is a multi-country LE initiative since 2022...") instead of the crime substance ("what malware, what victims, what financial flow, what OCG structure"). E.g., RCMP CIT-V Surrey arrest (iter 162) Background discussed Op Endgame umbrella but not what botnet, what victims, what malware family. User audit flagged the pattern: "범죄의 구체적인 내용은 어디에 포함되어 있는가?"
- **왜 실패**: ingest agent prompts emphasised L24 (≥2-LE cooperation) and L25 (tier-1 publisher) heavily, but did not require crime-substance content in Background. Agents defaulted to copying LE cooperation language from press releases and stopping there. The wiki drifted from a *cybercrime IC knowledge base* toward a *LE cooperation event log*.
- **교훈**: **`## Background` must describe (1) modus operandi, (2) victim profile + impact, (3) financial flow if applicable, (4) criminal organization structure** — to the extent the tier-1 source(s) provide. Missing elements get an explicit one-line gap note in `Contradictions & Open Questions`. Reader of op page must be able to answer "what was the crime, who was hurt, how did it work" without leaving the page. Operation context (LE side) belongs in `Summary` and `Operational Timeline`, NOT in `Background`.
- **어떻게 적용**:
  - CLAUDE.md operation schema gains an explicit "Background section requirements" block (2026-05-17 added; appears right after operation body-sections line).
  - Future ingest agent prompts must include: "Background section: describe the crime — modus operandi, victim profile, financial flow, OCG structure. Do not restate the operation context (that belongs in Summary). If tier-1 source does not disclose one of the four elements, write an explicit gap note in Contradictions."
  - **Background-thin op pages** existing in wiki get bulk-enrichment via dedicated sweep iters (look for op pages where Background section is < 100 words OR consists entirely of operation-umbrella context with zero modus/victim detail).
  - L26 takes effect from iter 203 onward.

---

### ❗ L25. private community-news wires (e.g., Village Media affiliates) reproducing tier-1 LE releases are NOT tier-1 (2026-05-16, iter 143)

- **상황**: iter 143 ingest agent picked an OPP "Project Atlas" $70M crypto-fraud release. OPP itself does not maintain a public press-release archive on `opp.ca` or `news.ontario.ca`; the only verbatim text was distributed via Village Media community-news affiliates (orilliamatters.com, barrietoday.com, ptbotoday.ca, renfrewtoday.ca, norfolktoday.ca, sydenhamcurrent.ca, pembroketoday.ca). Agent reasoned "OPP wire-syndication" justified `source_url=orilliamatters.com`. Operation pages created and only caught at L24 strict tier-1 check before commit.
- **왜 실패**: L24 strict reads "state news wires reproducing official statements DO count" — but Village Media is not a state news wire, it is a private commercial chain. Same applies to ctvnews.ca, 99bitcoins.com, similar private aggregators (regardless of whether they quote the LE release verbatim under a "NEWS RELEASE" lede). The verbatim-reproduction does not upgrade the publisher's tier.
- **교훈**: **If a tier-1 LE/prosecutor publisher has no own-domain release URL AND no state-wire reproduction (e.g., Reuters/AP NOT in the acceptlist; BTA Bulgaria / Yonhap / ANSA / Tribrata News Polri ARE), REJECT the operation outright rather than substitute a private-wire URL.** OPP and similar Canadian provincial police, US state police, US Sheriff's offices, and small-jurisdiction LEs that rely entirely on private-wire distribution are NOT ingestible under L24 strict. Pick another operation with a recoverable tier-1 own-domain release.
- **어떻게 적용**:
  - ingest agent prompt MUST enumerate domain classes that qualify (national/sub-national police/prosecutor own-domain, .gov/.gov.uk/.gov.au, intergovernmental org own-domain, named state news wires) AND explicitly list disqualified outlets (Village Media affiliates, CTV, ANI, AP, Reuters, Bloomberg, 99bitcoins, X/Twitter)
  - if no tier-1 own-domain URL exists → REJECT and pick another candidate; do not invent justifications for private-wire substitution
  - REJECT incident itself should be logged in `wiki/log.md` (transparency: which operations were rejected and why)
  - iter 143 OPP Project Atlas was the first triggered REJECT-RETRY in this session; pattern likely to recur with Canadian provincial police (RCMP K-Division, OPP, SPVM, BC), US Sheriff's, NZ Police local releases

---

### ❗ L24. participating_countries 는 협력국만 — 공격자/원천국/도착국은 제외 (2026-05-10, iter 124)

- **상황**: iter 124 ingest agent 가 Delhi Police IFSO SIMBOX 사기조직 단속 (인도 단독 작전) 보도자료를 ANI 뉴스와이어에서 가져와 operation page 생성. participating_countries 에 [[india]], [[taiwan]], [[cambodia]], [[pakistan]], [[nepal]], [[china]] 6개국을 모두 wikilink 함. 그러나 Delhi Police 1차 statement 는 명시적으로 "Foreign-LE counterpart agencies — none named in the primary release" 라고 acknowledged. 즉 Taiwan/Cambodia/Pakistan/Nepal/China 는 모두 *공격 인프라 origin/handler/C2/recruitment* 역할이고 LE 협력 jurisdiction 이 아님.
- **왜 실패**: L19 ("participating_countries 공식 출처 교차 검증") 이 "official source 에 언급되었으면 OK" 로 약하게 해석됨. 그러나 CLAUDE.md 의 IC scope 정의는 "≥2 countries' IC involvement" — 즉 **양국 이상의 LE/검찰이 협력한 작전**이어야 한다. 적국/원천국/도착국 표기가 IC 협력의 의미를 갖지 않는다.
- **교훈**: **`participating_countries` 는 (1) 자국 LE + (2) 1개 이상의 외국 LE/검찰이 explicit 하게 협력했다고 1차 출처에 명시된 jurisdictions 만 포함한다.** 적국/원천국/도착국은 본문 prose 에 attribution 으로만 기록. 1차 출처가 "no foreign-LE counterpart named" 라고 명시하면 → 그 작전은 **IC 작전이 아니므로 wiki/operations/ 에 들어가지 않는다** (단일국가 cybercrime 수사이므로 ingest 거부).
- **추가 강화**: **ANI India / Reuters / AP 등 사설 뉴스와이어는 tier-1 가 아니다.** 국가 통신사 (BTA Bulgaria, Tribrata News Polri, ANSA Italy, KCNA, Yonhap)이 official statement 를 그대로 reproduce 한 경우는 tier-1 으로 인정할 수 있으나, 사설 wire 는 secondary. CLAUDE.md "tier-1 primary source = national police agency, prosecutor's office, judicial body, intergovernmental org — NOT news outlets" 의 strict 해석.
- **어떻게 적용**:
  - ingest agent prompt 에 명시: "≥2-country IC requirement: At least 2 distinct countries' LE/prosecutorial agencies must have cooperated, with the cooperation explicitly acknowledged in the tier-1 primary source. Adversary/origin/destination states do NOT count."
  - "Tier-1 publisher = national police agency, prosecutor's office, judicial body, or intergovernmental org. Private news wires (e.g., ANI India, AP, Reuters) do NOT count. State news wires reproducing official statements DO count."
  - 1차 출처가 외국 LE 파트너를 명시하지 않으면 ingest 거부 → 다른 작전 선택
  - L19 의 strict 해석으로 격상 (이미 "공식 출처 교차 검증" 이지만 명시적 "협력 jurisdictions only" rule 추가)

---

### L22. nbi.gov.ph는 HTTPS TLS 핸드셰이크 실패 — HTTP plain으로 수집 (2026-05-09)

- **상황**: 필리핀 NBI 보도자료 (`http://nbi.gov.ph/press_releases/...`) 를 `curl_cffi` chrome120 으로 HTTPS 수집 시도하면 `WRONG_VERSION_NUMBER` SSL 에러로 실패. HTTPS 자체가 server-side에서 깨져 있음.
- **돌파구**: HTTP plain (`http://nbi.gov.ph/...`) 으로 동일 URL 요청하면 `HTTP/1.1 200 OK` + 정상 본문 반환. 서버가 HTTPS 리다이렉트를 강제하지 않고 HTTP로 평문 응답을 그대로 내준다.
- **증거**: iter 92 NBI Parañaque cyber-scam 보도자료 인제스트에서 curl_cffi chrome120 HTTPS = `WRONG_VERSION_NUMBER`, HTTP = 200 OK + 52KB body 확인.
- **교훈**: **L11/L20 "Cloudflare 차단" 패턴과는 다른 클래스의 1차 출처 차단**. 정부 사이트가 HTTPS 인증서 갱신 누락이나 mixed-content 설정 오류로 평문 HTTP만 정상 응답하는 케이스가 존재. HTTPS 강제 시도하다 포기하지 말고 HTTP로 fallback.
- **어떻게 적용**:
  - 정부 1차 출처 URL fetch 실패 시 fallback 순서: HTTPS curl_cffi chrome120 → HTTPS chrome124 → **HTTP plain (this lesson)** → Wayback `https://web.archive.org/web/<latest>/<URL>` → ABORT
  - 알려진 HTTP-only 도메인: `nbi.gov.ph` (필리핀 국가수사국)
  - raw 파일 frontmatter의 `source_url`은 운영 URL을 그대로 (http 포함) 기록 — 임의 https 변환 금지

---

### L20. Cloudflare/SPA 벽은 `curl_cffi` TLS impersonation + script-preserving parse로 뚫는다 (2026-04-21)

- **상황**: Europol/DOJ 등 핵심 1차 출처 URL이 `WebFetch`로는 Cloudflare 차단 (403/challenge). 이 때문에 Colombia-Avalanche 검증을 포기하고 frontmatter에서 제거하는 오판을 저질렀음.
- **돌파구**: `curl_cffi` + `impersonate="chrome124"` 로 TLS fingerprint를 Chrome처럼 위장하면 Europol 포함 대부분의 정부/기관 사이트에서 200 OK 를 돌려준다. BeautifulSoup이 `<script>` 태그를 기본 제거하지만, React SPA 페이지(예: 새 Europol newsroom)는 본문이 inline JSON에 담겨 있으므로 `<script>` 보존한 채 `get_text()` 로 추출하면 국가 명단이 드러난다.
- **증거**: Europol Avalanche 페이지의 inline JSON에 "Countries involved: Armenia, Australia, … **Colombia** … Gibraltar …" 전체 30국 roster가 직접 포함. Colombia 제거는 잘못된 결정이었고 같은 날 복원.
- **교훈**: **"Cloudflare가 막았다 ≠ 출처에 없다."** 검증 포기 전에 (1) `curl_cffi` TLS 스푸핑 시도, (2) SPA면 script-preserving parse, (3) 그래도 안 되면 Playwright/browser-use 풀 브라우저로 에스컬레이션. 최소 2-step fallback 거친 뒤에만 "not in source"라고 판정.
- **어떻게 적용**:
  - `tools/web_verify_tls.py` 가 이 3단계 파이프라인을 제공 (현재 curl_cffi + script-preserve 단계 구현)
  - 모든 web-verification 결과는 `.verification/web_verified.md` 에 누적
  - L19의 "removed" 버킷에 넣기 전에 이 도구로 한 번 더 확인 의무화

---

### L19. participating_countries는 tier-1 출처가 명시할 때만 assert — 없으면 flag, 있으면 keep (2026-04-21)

- **상황**: `operation-avalanche.md`에 Colombia 포함. Europol 공식 press release (Cloudflare로 차단), Eurojust case report PDF, Canadian Cyber Centre advisory, INTERPOL mirror 등 접근 가능한 tier-1 출처 전부에서 Colombia 미언급. frontmatter 데이터 출처가 불분명.
- **왜 실패**: 과거 ingest 때 secondary news나 AI 요약 기반으로 country list가 확장되면서, 실제 1차 출처에 없는 국가가 들어감. L17과 반대 방향의 같은 문제.
- **교훈**: **어떤 국가를 operation participant로 assert하려면 tier-1 primary source(Europol/INTERPOL/DOJ/국가기관 보도자료·법원서류)가 그 국가를 명시적으로 이름으로 호명해야 한다.**
- **어떻게 적용**:
  - 국가-작전 링크를 만들기 전에 primary source의 국가명 명시 여부 확인
  - primary source 접근이 차단되면 `retained but UNVERIFIED` 표시하되 `assertion`은 보류 (false negative 위험 방지 — 없음 ≠ 부정)
  - 접근 가능한 다수의 tier-1 출처 전수가 해당 국가를 언급하지 않을 때만 **제거 + Contradictions 섹션으로 이동**
  - 작전 페이지에 Audit Note 표로 `Verified / Removed / Pending` 분류 명시
  - country의 `operations_participated`에는 verified subset만 기재

---

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
