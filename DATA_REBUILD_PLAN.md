# 데이터 재구성 작업 계획

## 목표

기존 자료를 `old/`에 백업한 뒤, `데이터 샘플.xlsx`와 현재 wiki/raw/source 데이터를 교차검증하여 다음 기준에 맞는 국제공조 SNA 분석 데이터셋과 산출물을 재구성한다.

- 분석 기간: 2014년부터 2025년까지, 총 12년
- 분석 단위: 국제공조 작전명
- 분석 대상 죄종: 랜섬웨어, 다크넷, CSAM, 봇넷·악성코드, 불법 IPTV
- 필수 추출 필드: 작전명, 참여 기관, 참여 국가, 범죄유형, URL/source
- 필수 SNA 산출물: operation-country, operation-agency, operation-crime_type 2-mode edge list

## 현재 확인된 상태

- 현재 wiki source 정합성 감사는 `4,784 / 4,784 ok` 상태다.
- 현재 wiki operation은 전체 1,085건이며, canonical-like operation은 111건이다.
- 기존 SNA 산출물은 `_workspace/sna/out/2026-04-20-d50e3208/`에 있으나 최신 커밋 기준 재생성본은 아니다.
- 기존 SNA 산출물은 5개 죄종 전용 데이터셋이 아니며, 2013년과 2026년 기록도 일부 포함한다.
- `데이터 샘플.xlsx`는 새로 추가된 untracked 파일이며, 다음 시트를 포함한다.
  - `1_데이터수집(URL)`: 67행, URL 67건
  - `2_데이터추출(국가_기관_범죄유형)`: 164행, URL 164건
  - `기관_추출`: 165행
  - `국가_추출`: 165행
  - `범죄유형_추출`: 166행
- 빠른 키워드 점검 기준으로 `데이터 샘플.xlsx`에는 랜섬웨어와 봇넷·악성코드 후보는 일부 있으나, 불법 IPTV 후보는 현재 0건으로 보인다.
- 현재 `wiki/crime-types/`에는 `illegal-iptv-ic` 계열 crime type이 없다.

## 주요 판단

`데이터 샘플.xlsx`는 바로 병합할 정답 데이터가 아니라 staging 및 교차검증 자료로 사용한다.

이유:

- 일부 작전명이 `(가칭)` 또는 일반명으로 되어 있어 기존 canonical operation과 중복될 수 있다.
- 기관, 국가, 범죄유형 표기가 한글/영문/약칭이 혼재되어 SNA node 중복을 만들 수 있다.
- source URL이 현재 wiki source와 중복되는 경우가 있으므로 URL 기준 매칭이 먼저 필요하다.
- 엑셀 내용과 현재 wiki frontmatter가 충돌할 수 있으므로 원문 확인이 필요하다.

## 백업 계획

새 작업을 시작하기 전에 기존 자료를 삭제하지 않고 `old/YYYY-MM-DD/` 아래에 복사한다.

권장 백업 대상:

- `데이터 샘플.xlsx`
- `사이버범죄 국제공조 데이터.xlsx`
- `_workspace/sna/out/`
- `wiki/analysis/sna-structure-and-roles.md`
- `wiki/analysis/sna-pilot.md`
- `wiki/analysis/sna/`
- 필요 시 현재 분석 subset 관련 CSV와 리포트

예상 백업 경로:

```text
old/2026-05-04/
```

## Canonical Crime Type 기준

새 분석 subset에서는 아래 5개만 사용한다.

| 한글 범주 | Canonical slug | 처리 방침 |
|---|---|---|
| 랜섬웨어 | `ransomware-ic` | 기존 crime type 사용 |
| 다크넷 | `dark-web-ic` | 기존 crime type 사용 |
| CSAM | `csam-ic` | 기존 crime type 사용 |
| 봇넷·악성코드 | `malware-ic` 또는 `botnet-malware-ic` | 기존 `malware-ic`를 유지할지, 새 통합 slug를 만들지 결정 필요 |
| 불법 IPTV | `illegal-iptv-ic` | 신규 crime type 생성 필요 |

권장: SNA 분석에는 5개 대분류만 쓰고, wiki 내부 세부 crime type은 별도 필드나 mapping table로 보존한다.

## 엑셀 활용 절차

1. `데이터 샘플.xlsx`를 CSV로 추출한다.
2. 각 시트를 `_workspace/imports/data_sample/` 아래에 저장한다.
3. URL을 정규화한다.
4. 현재 `wiki/sources/*.md`의 `url` 또는 source URL과 매칭한다.
5. 매칭 결과를 다음으로 분류한다.
   - 기존 source와 URL 일치
   - URL은 신규이나 operation 후보가 기존 wiki와 유사
   - URL과 operation 모두 신규
   - URL 접근 또는 원문 확인 필요
6. operation명, 연도, URL, 내용 요약을 기준으로 기존 `wiki/operations/*.md`와 매칭한다.
7. 엑셀의 기관/국가/범죄유형 추출값과 wiki frontmatter를 비교한다.
8. 불일치 항목은 바로 덮어쓰지 않고 review CSV로 남긴다.

## 교차검증 산출물

최소한 아래 파일을 생성한다.

```text
_workspace/imports/data_sample/extracted_urls.csv
_workspace/imports/data_sample/matched_existing_sources.csv
_workspace/imports/data_sample/matched_existing_operations.csv
_workspace/imports/data_sample/new_candidate_operations.csv
_workspace/imports/data_sample/field_discrepancies.csv
_workspace/imports/data_sample/out_of_scope_2014_2025_or_non_ic.csv
_workspace/imports/data_sample/needs_manual_review.csv
```

각 CSV에는 최소한 다음 컬럼을 둔다.

- `excel_sheet`
- `excel_row`
- `year`
- `operation_name_raw`
- `operation_name_canonical_candidate`
- `source_url`
- `matched_source_slug`
- `matched_operation_slug`
- `excel_agencies`
- `wiki_agencies`
- `excel_countries`
- `wiki_countries`
- `excel_crime_types`
- `wiki_crime_types`
- `review_status`
- `review_note`

## 필터링 기준

새 분석 subset에 포함하려면 아래를 모두 만족해야 한다.

- 연도 또는 작전 기간이 2014년부터 2025년 사이에 속한다.
- 5개 대상 죄종 중 하나 이상에 해당한다.
- URL/source가 1건 이상 존재한다.
- 국제공조 근거가 있다.
  - 참여 국가 2개 이상, 또는
  - 다국적 기관/공조기관이 명시되어 있고 원문상 국제공조가 확인됨
- 작전 단위로 중복 제거되어 있다.
- 단순 국내 사건, 단일 피고인 후속 판결, 일반 정책 문서, 법령 소개 문서는 제외한다.

## 작전명 처리 기준

- 원문에 공식 작전명이 있으면 그대로 사용한다.
- 원문에 공식 작전명이 없으면 `(가칭)` 작전명을 허용하되, canonical slug에는 설명형 이름을 사용한다.
- 같은 사건을 여러 기사에서 다르게 부르는 경우 하나의 canonical operation에 통합한다.
- 후속 판결, 기소, 선고, 몰수는 독립 작전이 아니라 related case 또는 absorbed follow-on record로 둔다.

## 기관·국가·범죄유형 정규화

기관은 가능한 한 영문 slug로 통일한다.

예:

- `FBI`, `미국 연방수사국` -> `fbi-cyber-division` 또는 관련 FBI slug
- `DOJ`, `미국 법무부` -> `us-doj`
- `Europol`, `유로폴` -> `europol-ec3` 또는 `europol`
- `Eurojust`, `유로저스트` -> `eurojust`
- `INTERPOL`, `인터폴` -> `interpol`

국가는 ISO/영문 slug로 통일한다.

예:

- `미국` -> `united-states`
- `영국` -> `united-kingdom`
- `독일` -> `germany`
- `네덜란드` -> `netherlands`

범죄유형은 5개 대분류로 mapping한다.

예:

- `랜섬웨어`, `ransomware`, `digital extortion` -> `ransomware-ic`
- `다크넷`, `다크웹`, `darknet`, `dark web marketplace` -> `dark-web-ic`
- `아동 성착취물`, `CSAM`, `child sexual abuse material`, `child pornography` -> `csam-ic`
- `봇넷`, `악성코드`, `트로이목마`, `malware`, `botnet`, `trojan` -> `malware-ic` 또는 `botnet-malware-ic`
- `불법 IPTV`, `illegal IPTV`, `illegal streaming`, `pirate streaming` -> `illegal-iptv-ic`

## 불법 IPTV 보강

현재 가장 큰 결손은 불법 IPTV다.

필요 작업:

1. `illegal-iptv-ic` crime type 문서 생성
2. 2014~2025년 국제공조 사례 수집
3. 공식 출처 또는 신뢰 가능한 보도 source 생성
4. operation 문서 생성
5. 기관/국가/범죄유형 edge에 반영

후보 키워드:

```text
illegal IPTV international law enforcement operation
pirate IPTV Europol operation
illegal streaming Eurojust IPTV
Operation Creative IPTV law enforcement
Operation 404 IPTV
Operation Taken Down IPTV
Operation Kratos IPTV piracy
anti-piracy IPTV police Europol Eurojust
```

## SNA 산출물

새 subset 기준으로 아래를 생성한다.

```text
_workspace/sna/current/manifest.json
_workspace/sna/current/nodes_operations.csv
_workspace/sna/current/nodes_countries.csv
_workspace/sna/current/nodes_agencies.csv
_workspace/sna/current/nodes_crimetypes.csv
_workspace/sna/current/edges_op_country.csv
_workspace/sna/current/edges_op_agency.csv
_workspace/sna/current/edges_op_crimetype.csv
_workspace/sna/current/metrics_centrality_country.csv
_workspace/sna/current/metrics_centrality_agency.csv
_workspace/sna/current/metrics_centrality_crimetype.csv
_workspace/sna/current/metrics_cohesion.json
_workspace/sna/current/metrics_components.json
```

시각화 산출물:

```text
wiki/analysis/sna/country-network.html
wiki/analysis/sna/agency-network.html
wiki/analysis/sna/crime-type-network.html
```

분석 문서:

```text
wiki/analysis/sna-2014-2025-six-crime-types.md
```

## 완료 조건

완료 전 아래를 모두 확인한다.

- `old/YYYY-MM-DD/` 백업 존재
- `데이터 샘플.xlsx` 각 시트가 CSV로 추출됨
- 엑셀 URL과 기존 source URL 교차검증 리포트 생성
- 신규 operation 후보와 기존 operation 매칭 리포트 생성
- field discrepancy 리포트 생성
- 2014~2025 범위 밖 operation 0건
- 5개 대상 죄종 외 operation 0건
- 각 included operation에 source URL 1건 이상
- 각 included operation에 참여기관, 참여국가, 범죄유형이 비어 있지 않음
- operation-country edge list 생성
- operation-agency edge list 생성
- operation-crime_type edge list 생성
- SNA metrics 생성
- SNA 시각화 생성
- wiki/source 정합성 감사 통과
- wiki lint 통과
- integrity audit 통과
- static build 통과
- link checker 통과
- 커밋 및 원격 push 완료

## 검증 명령 후보

```powershell
python tools\audit_source_url_content_alignment.py --date 2026-05-04
python tools\lint.py
python tools\audit_integrity.py
python tools\audit_operation_consistency.py
py -3.7 web\build_static.py
python tools\check_links.py
git diff --check --no-color
git status --short --branch
```

SNA 재생성은 기존 `tools/sna_analysis.py`를 그대로 쓰기 전에 5개 죄종/2014~2025 subset 필터를 반영해야 한다.

## 다음 세션 첫 작업

다음 Codex 세션을 시작하면 아래 순서로 진행한다.

1. 이 파일을 읽는다.
2. 새 goal을 생성한다.
3. 작업 전 `git status --short --branch`를 확인한다.
4. `old/YYYY-MM-DD/` 백업을 만든다.
5. `데이터 샘플.xlsx`를 `_workspace/imports/data_sample/`로 CSV 추출한다.
6. URL/source/operation 교차검증 리포트를 먼저 만든다.
7. 리포트 검토 후 병합 및 신규 수집으로 넘어간다.
