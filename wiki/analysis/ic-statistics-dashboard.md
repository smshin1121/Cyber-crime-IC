---
analysis_type: trend-report
confidence: high
created: 2026-04-08
entities_referenced:
  - "[[europol-ec3]]"
  - "[[interpol-igci]]"
  - "[[fbi-cyber-division]]"
  - "[[south-korea]]"
generated_from: manual
key_judgments:
  - confidence: high
    judgment: "Europol과 INTERPOL이 양대 조정 허브로 기능"
  - confidence: high
    judgment: "INTERPOL 주도 작전이 체포 규모에서 압도적"
  - confidence: high
    judgment: "한국이 HAECHI 시리즈를 통해 아시아-태평양 국제공조의 핵심 행위자"
scope: "2014-2025 사이버범죄 국제공조 작전 통계 (위키 수집 데이터 기반)"
sources_consulted: 4763
title: "사이버범죄 국제공조 통계 대시보드"
type: analysis
updated: 2026-04-26
---
# 사이버범죄 국제공조 통계 대시보드

> [!info] 이 페이지의 모든 데이터는 위키에 수집된 1085개 작전과 4763개 출처 페이지에서 도출되었습니다. 작전 전체 목록은 `wiki/operations/_index.md`를 참조하십시오.

---

## 1. 작전 집계 통계

### 전체 현황

| 지표 | 값 |
|------|-----|
| 총 작전 수 | 1085 |
| Period 1 (2014-2018) | 205 |
| Period 2 (2019-2022) | 222 |
| Period 3 (2023-2025) | 650 |
| 총 출처 수 | 4763 (dedicated pages) + Excel 소스 |

### 조정기관별 분포

| 조정기관 | 작전 수 | 비고 |
|---------|---------|------|
| Europol / Europol EC3 | 60 | 가장 많은 작전 조정; 랜섬웨어, 봇넷, 사기 포럼 등 |
| INTERPOL / INTERPOL IGCI | 40 | 체포 규모에서 압도적; HAECHI, Jackal, Serengeti 등 |
| DOJ / FBI (미국 주도) | 946 | 기소·압수 중심 |
| AFRIPOL | 3 | 아프리카 공동 조정 |
| Eurojust | 14 | 사법 공조 조정 |
| 양자/기타 (조정기관 없음) | 22 | 한국 양자작전 포함; 단독 기소 다수 |

### 상위 10개 작전 (CI 기준)

| 작전 | CI | 소스 수 | 주요 결과 |
|------|-----|---------|---------|
| [[operation-shrouded-horizon]] | 3.62 | 2 | 70 체포, Darkode 포럼 해체 (2015) |
| [[operation-falcon]] | 3.62 | 1 | 3 체포, 나이지리아 BEC 조직 단속 (2020) |
| [[goznym-takedown]] | 3.62 | 1 | 10 체포, $100M 피해 GozNym 악성코드 해체 (2019) |
| [[infraud-organization-takedown]] | 3.30 | 7 | 36 기소, $530M 피해 인프라우드 조직 소탕 (2018) |
| [[operation-red-card]] | 2.95 | 2 | 306 체포, 7 아프리카국 (2024-2025) |
| [[operation-haechi-ii]] | 2.95 | 1 | 1,003 체포, $27M 인터셉트 (2021) |
| [[operation-cyber-guardian]] | 2.95 | 1 | 544 체포, 6 아시아국 CSAM 단속 (2025) |
| [[ddos-for-hire-sweep-2016]] | 2.95 | 1 | 34 체포, DDoS-for-hire 국제 소탕 (2016) |
| [[911-s5-botnet-takedown]] | 2.95 | 1 | 19M+ IP 감염, 세계 최대 봇넷 해체 (2024) |
| [[operation-stream-kidflix]] | 2.55 | 1 | 79 체포, 1.8M 이용자 CSAM 플랫폼 폐쇄 (2022-2025) |

---

## 2. 조정기관별 집계 (출처 기반 20개 주요 작전)

| 지표 | Europol 작전 | INTERPOL 작전 | DOJ 작전 | 양자 작전 | 전체 합계 |
|------|-------------|--------------|---------|---------|---------|
| 작전 수 | 6 | 9 | 3 | 2 | **20** |
| 총 체포/기소 | 22+ (20 영장) | 15,473+ | 12+ (기소) | 123+ | **15,630+** |
| 서버 압수 | 470+ | 59 | 4 | - | **533+** |
| 도메인 압수/차단 | 2,650+ | 140,089+ | 9 | - | **142,748+** |
| 금융 압수/회수 | EUR 78M+ | $1.8B+ | $25M+ | - | **$2B+** |

> 참고: 이 표는 개별 출처 페이지가 있는 20개 주요 작전(dedicated source pages [1]-[20]) 데이터만 집계합니다. 나머지 62개 작전은 Excel 배치 임포트 또는 단일 출처 기반이며, 정량 데이터가 불완전한 경우가 있습니다.

---

## 3. 범죄유형별 작전 분포

| 범죄유형 | 작전 수 | 주요 작전 | 주요 조정기관 |
|---------|--------|---------|-----------|
| [[ransomware-ic|랜섬웨어]] | 7+ | Cronos Ph1/Ph3, Endgame Ph1/Ph2, Phobos, Checkmate, QakBot | Europol, DOJ |
| [[online-fraud-ic|온라인 사기]] | 7+ | HAECHI IV/V/VI, Serengeti, First Light, Jackal/III | INTERPOL |
| [[bec-ic|BEC]] | 8+ | Franco-Israeli, Jackal, Jackal III, Sentinel, HAECHI IV/V/VI, First Light | Europol, INTERPOL |
| [[voice-phishing-ic|보이스피싱]] | 6+ | Korea-China Qingdao, HAECHI IV/V/VI, First Light, Korea-Cambodia | INTERPOL, 한국 양자 |
| [[hacking-ic|해킹]] | 1+ | i-Soon/APT27 | DOJ |
| [[csam-ic|CSAM]] | 3 | Operation Stream/Kidflix, Cyber Guardian, Orion International | Europol, 한국, INTERPOL |

> 일부 작전은 복수 범죄유형에 해당하므로 합산 시 중복이 발생합니다. Excel 배치 임포트 작전의 범죄유형이 반영되어 실제 수치는 위 표보다 높을 수 있습니다.

---

## 4. 출처 다양성

| 출처 기관 | 건수 | 비율 | 신뢰도 |
|---------|------|------|--------|
| INTERPOL | 10 | 43% | A (Completely reliable) |
| Europol | 6 | 26% | A (Completely reliable) |
| US DOJ | 3 | 13% | A (Completely reliable) |
| Korea NPA | 1 | 4% | A (Completely reliable) |
| 뉴스 (Korea Times, Al Jazeera, Security Affairs) | 3 | 13% | B (Usually reliable) |
| **합계** | **23** | **100%** | |

> 추가로 62개 작전이 Excel 스프레드시트 및 기타 웹 출처에서 임포트되었으나, 개별 출처 페이지는 작성되지 않았습니다.

---

## 5. 한국 관련 작전

| 작전 | 한국의 역할 | 출처 |
|------|---------|------|
| [[operation-haechi-iv]] | INTERPOL 공동 주도 | [4] |
| [[operation-haechi-v]] | INTERPOL 공동 주도, 한-중 보이스피싱 하위작전 | [12] |
| [[operation-haechi-vi]] | INTERPOL 공동 주도, 한-UAE 하위작전 | [18] |
| [[korea-china-voice-phishing-qingdao]] | 서울경찰청 주도, 중국 청도경찰 공동 | [3] |
| [[phobos-8base-crackdown]] | Phobos 관리자 한국 내 체포 + 미국 인도 | [13] |
| [[korea-cambodia-scam-repatriation]] | 한국인 107+ 송환 주도 | [19] |
| [[isoon-apt27-indictment]] | 한국이 피해국으로 언급 | [14] |
| [[operation-cyber-guardian]] | 한국 경찰청 주도 (435/544 체포) | [23] |
| [[operation-haechi-ii]] | INTERPOL 공동 주도 | Excel |

---

## 6. 위키 커버리지 현황

| 카테고리 | 페이지 수 | 비고 |
|---------|---------|------|
| 법적 프레임워크 | 22 | 부다페스트 협약 등 |
| 기관 | 143 | 주요 기관 |
| 국가 | 110 | 국가 프로필 |
| 작전 | 1085 | 2014-2025 주요 작전 (P1: 205, P2: 222, P3: 650) |
| 메커니즘 | 27 | 공조 메커니즘 |
| 범죄유형 | 23 | 문서화된 범죄유형 |
| 개념 | 15 | 법적 개념 |
| 출처 | 4763 | 전용 출처 페이지 |
| 분석 | 22 | 본 대시보드 포함 |
| **총 페이지** | **7416** | _index 파일 및 메타파일 제외 |

---

## References

| # | Source | Publisher | Date | URL |
|---|--------|----------|------|-----|
| [1] | Franco-Israeli CEO fraud gang dismantled | Europol | 2023-02-08 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/franco-israeli-gang-behind-eur-38-million-ceo-fraud-busted) |
| [2] | Operation Jackal: Black Axe BEC | INTERPOL | 2023-06-06 | [원본](https://www.interpol.int/News-and-Events/News/2023/Closing-ranks-on-West-African-organized-crime-more-than-EUR-2-million-seized-in-Operation-Jackal) |
| [3] | Korea-China voice phishing joint operation | Korea Times | 2023-09-08 | [원본](https://www.koreatimes.co.kr/www/nation/2024/07/113_358692.html) |
| [4] | Operation HAECHI IV | INTERPOL | 2023-12-19 | [원본](https://www.interpol.int/News-and-Events/News/2023/USD-300-million-seized-and-3-500-suspects-arrested-in-international-financial-crime-operation) |
| [5] | Operation Cronos: LockBit disrupted | Europol | 2024-02-20 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-disrupt-worlds-biggest-ransomware-operation) |
| [6] | Operation First Light 2024 | INTERPOL | 2024-06-18 | [원본](https://www.interpol.int/News-and-Events/News/2024/USD-257-million-seized-in-global-police-crackdown-against-online-scams) |
| [7] | Operation Endgame: botnet takedown | Europol | 2024-05-30 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem) |
| [8] | Operation Jackal III: Black Axe BEC | INTERPOL | 2024-08-28 | [원본](https://www.interpol.int/en/News-and-Events/News/2024/INTERPOL-operation-strikes-major-blow-against-West-African-financial-crime) |
| [9] | Operation Synergia II | INTERPOL | 2024-11-06 | [원본](https://www.interpol.int/News-and-Events/News/2024/INTERPOL-cyber-operation-takes-down-22-000-malicious-IP-addresses) |
| [10] | Operation Cronos Phase 3 | Europol | 2024-10-01 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/lockbit-power-cut-four-new-arrests-and-financial-sanctions-against-affiliates) |
| [11] | Operation Serengeti | INTERPOL | 2024-11-26 | [원본](https://www.interpol.int/en/News-and-Events/News/2024/Major-cybercrime-operation-nets-1-006-suspects) |
| [12] | Operation HAECHI V | INTERPOL | 2024-12-02 | [원본](https://www.interpol.int/News-and-Events/News/2024/INTERPOL-financial-crime-operation-makes-record-5-500-arrests-seizures-worth-over-USD-400-million) |
| [13] | Phobos/8Base ransomware arrests | Europol | 2025-02-11 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown) |
| [14] | i-Soon/APT27 indictment | US DOJ | 2025-03-05 | [원본](https://www.justice.gov/opa/pr/justice-department-charges-12-chinese-contract-hackers-and-law-enforcement-officers-global) |
| [15] | Operation Endgame Phase 2 | Europol | 2025-05-23 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-strikes-again-ransomware-kill-chain-broken-its-source) |
| [16] | QakBot/Gallyamov indictment | US DOJ | 2025-05-22 | [원본](https://www.justice.gov/archives/opa/pr/leader-qakbot-malware-conspiracy-indictment-involvement-global-ransomware-scheme) |
| [17] | Operation Checkmate: BlackSuit | US DOJ | 2025-08-11 | [원본](https://www.justice.gov/opa/pr/justice-department-announces-coordinated-disruption-actions-against-blacksuit-royal) |
| [18] | Operation HAECHI VI | INTERPOL | 2025-09-25 | [원본](https://www.interpol.int/en/News-and-Events/News/2025/USD-439-million-recovered-in-global-financial-crime-operation) |
| [19] | Korea-Cambodia scam centre repatriation | Al Jazeera / Korea Herald | 2025-10-18 | [원본](https://www.aljazeera.com/news/2025/10/20/south-korea-police-seek-warrants-for-repatriated-scam-centre-suspects) |
| [20] | Operation Sentinel Africa | INTERPOL | 2025-12-22 | [원본](https://www.interpol.int/en/News-and-Events/News/2025/574-arrests-and-USD-3-million-recovered-in-coordinated-cybercrime-operation-across-Africa) |
| [21] | Operation Orion International | INTERPOL | 2024-10-15 | [원본](https://www.interpol.int/en/News-and-Events/News/2024/20-rescued-144-arrested-in-major-child-abuse-operation-across-South-America) |
| [22] | Operation Stream / Kidflix | Security Affairs / TRM Labs | 2025-04-04 | [원본](https://securityaffairs.com/176270/cyber-crime/operation-stream-kidflix-takedown.html) |
| [23] | Operation Cyber Guardian | Korea NPA / Seoul Shinmun | 2025-04-07 | [원본](https://www.seoul.co.kr/news/society/2025/04/07/20250407500065) |
