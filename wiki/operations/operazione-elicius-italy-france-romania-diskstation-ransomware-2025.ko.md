> [!info] 잠정 / 단일 소스 페이지
> 이 페이지는 기저의 tier-1 1차 출처(Polizia di Stato 공식 보도자료)가 검증 가능한 상세 내용(3개국에 걸친 명명된 법집행 협력 기관, 명시된 검찰청, 명시된 구속 주체, 명시된 기소 조항, 명시된 수색 장소와 일자)을 풍부하게 제공하기 때문에, 권장 5-소스 기준(CLAUDE.md "entity creation threshold") 이하임에도 게시되었다. 프랑스 국가경찰(police nationale) 및 루마니아 경찰(poliție)의 추가 tier-1 출처는 식별되는 대로 추가될 예정이다. 그 전까지 열거된 결과는 잠정으로 취급하고, tier-1 교차 확인을 위해 추후 재방문해야 한다.

## 개요

Operazione ELICIUS는 "Diskstation" 랜섬웨어 갱단에 대항하는 이탈리아·프랑스·루마니아 합동 경찰 작전이다. 해당 조직은 Synology DiskStation NAS 기기를 악용한 이중협박(double-extortion) 랜섬웨어 공격으로 롬바르디아(Lombardia) 지역의 이탈리아 중소기업을 표적으로 삼은 루마니아 국적 조직범죄단(OCG)이다. 본 작전은 밀라노 사이버안보 운영센터(C.O.S.C. Milano) 소속의 이탈리아 [[italy-polizia-postale|Servizio Polizia Postale e per la Sicurezza Cibernetica]]가 주도하였고, [[italy|밀라노 검찰(Procura di Milano)]]이 기소를 담당하였으며, EU 차원에서는 [[europol-ec3|Europol(유럽 사이버범죄센터)]]이 [[france-national-police|프랑스 국가경찰]] 및 [[romania-police|루마니아 경찰]]과 함께 조정하였다. 수색은 2024년 6월 부쿠레슈티(Bucharest)에서 집행되었고, 본 작전은 2025년 7월 14일 Polizia di Stato의 공식 발표로 공개되었다.

## 배경

본 수사는 정보 시스템의 데이터가 암호화되어 업무 마비를 겪은 롬바르디아(이탈리아 북부) 지역 기업들의 신고가 잇따르면서 시작되었다. 1차 출처에 명시된 표적 업종은 그래픽 디자인, 영화 제작, 이벤트 기획, 그리고 국제적 인권 보호·자선 활동을 수행하는 NGO이다. 피해 기업들은 데이터 복구를 위해 막대한 암호화폐 몸값을 지불해야 했다.

"Diskstation"이라는 명칭은 갱단의 자체 호칭으로, 초기 침투 벡터로 악용한 네트워크 결합 저장장치(NAS) 브랜드 — Synology DiskStation — 를 가리킨다.(주: 1차 출처는 구체적 CVE를 열거하지 않는다.)

## 참여 당사자

**이탈리아 측:**
- **주관 수사 기관:** [[italy-polizia-postale|Servizio Polizia Postale e per la Sicurezza Cibernetica]](우정·사이버안보 경찰국), [[polizia-di-stato|Polizia di Stato]](이탈리아 국가경찰) 소속
- **운영센터:** Centro Operativo per la Sicurezza Cibernetica (C.O.S.C.) di Milano(밀라노 사이버안보 운영센터)
- **기소 당국:** Procura di Milano(밀라노 검찰청)
- **구속 결정 주체:** 밀라노 지방법원 예심판사(Giudice per le Indagini Preliminari, GIP presso il Tribunale di Milano)

**외국 측 법집행 파트너 (tier-1 출처에 명시):**
- **프랑스:** "polizie nazionali di Francia" — 즉 [[france-national-police|프랑스 국가경찰]](Police Nationale)
- **루마니아:** "polizie nazionali di Romania" — 즉 [[romania-police|루마니아 경찰]](Poliția Română)

**조정:**
- [[europol-ec3|EUROPOL]] — 합동 태스크포스를 공식 설립.

## 법적 근거

주범에 대한 이탈리아 측 혐의는 이탈리아 형법(Codice Penale)의 두 개 조항에 근거한다:
- **형법 제615조-ter** — *Accesso abusivo a un sistema informatico o telematico*(컴퓨터 또는 원격통신 시스템에 대한 무권한 접근).
- **형법 제629조** — *Estorsione*(공갈).

두 범죄 모두 [[budapest-convention|부다페스트 사이버범죄협약(Budapest Convention)]]의 실체적 적용 범위(제2조 — 불법 접근 — 및 제11조 / 공갈성 남용에 관한 부속 규정) 내에 있으며, 이탈리아·프랑스·루마니아 모두 협약 당사국이다. 본 작전에서의 3개국 간 협력은 협약 국제협력 장(제23~35조) 및 쌍방가벌성(dual criminality) 체계와 부합한다.

## 작전 타임라인

- **단계 1 — 이탈리아 단독 포렌식 + 블록체인 분석(일자 미공개; 2024년 6월 이전).** 밀라노 검찰은 이중 트랙 작업을 조정하였다: (a) 피해 기업의 공격받은 정보시스템에 대한 심층 포렌식 분석; (b) 암호화폐 몸값 흐름의 블록체인 분석. 본 단계에서 수사 범위를 해외로 확장할 필요성이 식별되었다.
- **단계 2 — 프랑스·루마니아가 포함된 Europol(유럽 사이버범죄센터) 조정 태스크포스(일자 미공개; 2024년 6월 이전).** 1차 출처: *"con il coordinamento di EUROPOL ... è stata istituita una task force con le polizie nazionali di Francia e Romania"* — 즉 이탈리아 측 단서가 해외로 향하자 Europol이 동일 갱단을 독립적으로 수사하던 프랑스·루마니아 경찰과의 합동 태스크포스를 셸 차원에서 조정하였다.
- **2024년 6월 — 부쿠레슈티 수색.** 부쿠레슈티 내 피의자 거주지에서 수색 집행, C.O.S.C. Milano 요원이 물리적으로 참여. 다수 인원이 *in flagranza di reato*(현행범)으로 검거되었다. 다수의 증거물이 압수되었다.
- **2024-2025 — 이탈리아 내 사법 단계.** 밀라노 GIP는 기소 검사들의 적법한 청구를 인용하여, 다수의 이탈리아 피해자에 대한 무권한 컴퓨터 접근 및 공갈 혐의로 주범인 44세 루마니아 국적자에 대해 구속 영장을 발부하였다.
- **2025-07-14 — 공식 발표.** Polizia di Stato가 국가 포털에 작전 요약을 게시하였다.

## 결과 및 영향

| 지표 | 값 |
|---|---|
| 주피고인 체포 | 1명(44세 루마니아 국적, 이탈리아 내 구속수감 중) |
| 추가 피의자 식별 | "diversi soggetti, tutti di nazionalità rumena"(다수, 정확한 수치 미공개) |
| 수색 | 2024년 6월, 부쿠레슈티, 다수 거주지 |
| 기소 혐의(주피고인) | 형법 제615조-ter(무권한 접근); 형법 제629조(공갈) |
| 서버 / 암호화폐 압수 | 1차 출처에 미공개 |
| 복호화 키 회수 | 1차 출처에 미공개 |
| 피해자 | 롬바르디아 전역의 이탈리아 중소기업; 업종: 그래픽 디자인, 영화 제작, 이벤트, 인권 NGO |

## 활용된 협력 메커니즘

- **[[joint-investigation-team|Europol(유럽 사이버범죄센터) 조정 합동 태스크포스]]** — 1차 출처는 Europol 조정 하의 *"task force"* 설립을 기술한다. 텍스트는 공식 Eurojust(유럽사법협력기구) 공동수사팀(JIT) 명칭을 사용하지 않지만, 그 구조(이탈리아·프랑스·루마니아 경찰 수사관이 Europol이 제공하는 운영 셸 하에 단일 범죄 표적을 합동으로 수사하는 형태)는 기능적으로 해당 모델과 일치한다.
- **국경 간 증거 기법으로서의 블록체인 분석** — 이탈리아 측 암호화폐 몸값 흐름 블록체인 분석이 국내 수사에서 다국가 태스크포스로 이행하는 토대를 제공하였다.
- **국경 간 증거 수집을 위한 물리적 배치** — 이탈리아 C.O.S.C. 요원이 2024년 6월 부쿠레슈티 수색에 물리적으로 참여하여 집행 시점에 피해자 측 증거에 대한 직접적 기술 전문성을 제공하였다.

## 도전 과제 및 마찰 지점

1차 보도자료는 마찰 지점을 열거하지 않는다. 추론 가능한 도전 과제(낮은 신뢰도, 명시적 출처 진술이 아닌 작전 유형으로부터 유도):
- 관할을 가로지른 피의자 식별에는 지속적인 Europol 조정 정보 교환이 필요하다 — 이탈리아 측 단서를 동일 갱단에 대한 프랑스·루마니아 측 병렬 단서와 통합해야 했다.
- 구속 경로상, 주범은 2024년 6월 부쿠레슈티 수색 중 현행범으로 검거되었거나(1차 출처: *"cogliere alcuni soggetti in flagranza di reato"*) 이후 유럽체포영장(EAW) 경유로 이탈리아 측 신병 인도가 이루어졌을 가능성이 높지만, 1차 출처는 EAW 경로를 명시적으로 확인하지 않는다.

## 교훈

1차 출처는 명시적 교훈을 표명하지 않는다. 기록할 가치가 있는 구조적 시사점:
- **OCG 랜섬웨어 벡터로서의 Synology DiskStation NAS 악용** — Europol 조정 단속이 NAS 기기 악용(원격 데스크톱(RDP) / VPN / 피싱 초기 접근 대비)과 구체적으로 연관된 위키 최초 기록. 향후 유사 갱단에 대한 이탈리아 / EU 기록은 본 페이지와 교차연결되어야 한다.
- **이탈리아 C.O.S.C.(Centro Operativo per la Sicurezza Cibernetica)**은 이탈리아 경찰 수사관의 국경 간 물리적 배치를 위한 운영 거점으로, 잘 문서화된 루마니아 조직 사이버범죄 연결망을 고려할 때 향후 이탈리아·루마니아 랜섬웨어 사건에서 재현 가능성이 높은 패턴이다.

## 후속 조치

1차 출처는 형사 책임은 무죄추정의 원칙에 따라 재판 종결 시 확정판결을 통해서만 결정될 수 있음을 명시한다. 따라서 수사·체포 단계의 status = `completed`이지만, 재판 결과는 미확정·미기록 상태이다.

## 한국의 참여

한국 참여 없음 — [[south-korea|대한민국]] 법집행/검찰 및 한국인 피해자 모두 1차 출처에 언급되지 않는다. CLAUDE.md 운영 규칙 12에 따라 완전성을 위해 기록함.

## 모순 및 미해결 질문

> [!info] Open data points (단일 출처 ingest)
> 1. **식별된 피의자 총수.** 1차 출처: "diversi soggetti, tutti di nazionalità rumena"(다수, 모두 루마니아 국적) — 정확한 수치 미공개.
> 2. **이탈리아 피해자가 지불한 몸값 총액.** 미공개.
> 3. **악용된 Synology DiskStation 구체적 CVE.** "Diskstation" 갱단 명칭은 Synology NAS 악용을 가리키지만 1차 출처에는 CVE 목록이 없다.
> 4. **신병 인도 메커니즘.** 44세 루마니아 주범이 유럽체포영장(EAW), 범죄인 인도, 또는 자발적 이동 후 이탈리아 측에 인도되었는지 여부는 미공개.
> 5. **프랑스 국가경찰의 참여 범위.** 프랑스 경찰은 1차 출처에서 태스크포스 참여자로 두 번 명명되지만, 출처는 프랑스 측이 어떤 구체적 수사 행위를 수행했는지 상세히 기술하지 않으며, 단지 "anch'esse impegnate nell'individuazione dei responsabili degli attacchi"(공격 책임자 식별에도 관여)라고만 명시한다. 향후 프랑스 측 1차 출처를 교차 확인해야 한다.
> 6. **Eurojust(유럽사법협력기구) 공식 JIT 대 임시 Europol 태스크포스.** 1차 출처는 *"task force"*라는 표현을 사용하며 *"squadra investigativa comune"* / 공동수사팀(JIT)이 아니다. 공식 Eurojust JIT가 개시되었는지는 기록되지 않는다.
