## 개요

Operation Kraken(크라켄 작전, AFP)은 [[australia-afp|호주 연방경찰(AFP)]]이 주도하고 [[europol-ec3|Europol(유럽 경찰청)]]이 조율한 다국적 법집행 작전으로, 전 세계 조직범죄 네트워크가 전용으로 구축·사용한 암호화 통신 플랫폼 **Ghost**를 해체하였다. 본 작전은 2024년 9월 17~18일 호주, 아일랜드, 이탈리아, 캐나다, 스웨덴 전역에서 거의 동시에 이루어진 압수수색으로 정점에 이르렀다. 플랫폼의 제작자이자 운영자로 지목된 **Jay Je Yoon Jung**(32세, 호주 뉴사우스웨일스 거주)은 시드니 Narwee 자택에서 체포되었다.

본 수사는 Europol(유럽 경찰청)의 **Operational Taskforce (OTF) NEXT**의 틀 안에서 2022년 3월에 개시되었으며 9개국이 참여하였다. AFP(호주 연방경찰)는 단말기에 전송되는 **소프트웨어 업데이트를 변조**함으로써 Ghost에 침투하는 새로운 기술적 역량을 개발하였고, 이를 통해 암호화된 통신에 실시간으로 접근할 수 있었다. 본 작전은 EncroChat(2020), Sky ECC(2021), [[operation-trojan-shield|AN0M/Operation Trojan Shield (2021)]] 등 범죄용 암호화 플랫폼에 대한 일련의 성공적인 법집행 침투 사례의 연장선상에 있다.

전 세계적으로 51명의 피의자가 체포되었으며, 운영자로부터 약 930만 호주달러(AUD) 상당의 암호화폐가 압수되었다.

## 배경

### Ghost 플랫폼

Ghost는 2015년경 Jay Je Yoon Jung이 23세 당시 제작한 것으로 알려진 암호화 통신 플랫폼이다. 합법적인 암호화 메신저 앱과 달리 Ghost는 **오로지 범죄용으로** 설계·판매되었다. 주요 기능은 다음과 같다.

- **개조된 스마트폰**: 재판매업자 네트워크를 통해 단말기 1대당 약 2,350호주달러(약 1,600미국달러)에 판매되었으며, 6개월 구독과 기술 지원이 포함됨
- **3중 암호화**: 통신을 보호하는 세 가지 별도의 암호화 표준
- **자동 삭제 메시지**: 설정 가능한 기간이 지나면 메시지가 자동 삭제됨
- **원격 초기화**: 증거 인멸을 위해 단말기의 모든 데이터를 원격으로 삭제할 수 있는 기능
- **암호화폐 결제**: 익명성 확보를 위해 암호화폐로 구독 결제 가능
- **등록 정보 불요**: 플랫폼 이용을 위한 개인정보가 요구되지 않음

해당 플랫폼은 전 세계에 "수천 명"의 이용자를 보유하였으며 1일 약 1,000건의 메시지가 송수신되었다. 서버는 **프랑스와 아이슬란드**에 위치하였고, 운영자는 **호주**에 거주하였다.

### 범죄적 활용

Ghost는 조직범죄 집단에 의해 다음과 같은 용도로 사용되었다.
- 마약 거래(헤로인, 메스암페타민, 코카인)
- 자금세탁
- 살인 청부 및 중대한 폭력 위협
- 무기 거래
- 기타 중대 조직범죄

AFP(호주 연방경찰)는 호주 내 Ghost 이용자들이 마약 거래, 자금세탁, 살인 청부, 또는 중대 폭력 위협에 관여하였다고 밝혔다.

### 범죄 플랫폼 해체의 계보

Ghost는 법집행기관이 침투 또는 해체한 일련의 범죄용 암호화 통신 플랫폼 가운데 하나이다.

| 플랫폼 | 해체 연도 | 주도 기관 | 방식 |
|----------|---------------|-------------|--------|
| EncroChat | 2020 | 프랑스/네덜란드 | 서버 침투 |
| Sky ECC | 2021 | 벨기에/네덜란드/프랑스 | 메시지 복호화 |
| AN0M | 2021 | FBI(미국 연방수사국)/AFP(호주 연방경찰) | FBI가 직접 구축한 플랫폼 |
| **Ghost** | **2024** | **AFP/Europol** | **소프트웨어 업데이트 변조** |

## Participating Parties

**주도 기관:**
- [[australia-afp|호주 연방경찰(AFP)]] — Operation Kraken(국내 작전명)

**조율 기관:**
- [[europol-ec3|Europol(유럽 경찰청)]] — Operational Taskforce (OTF) NEXT
- [[eurojust|Eurojust(유럽 사법협력기구)]] — 사법 조율 및 프랑스-미국 합동수사팀(JIT) 지원

**OTF NEXT 회원:**
- [[fbi-cyber-division|FBI(미국 연방수사국)]] (OTF NEXT 공동 주도)
- [[france-gendarmerie|프랑스 헌병대]] (OTF NEXT 공동 주도)
- [[australia-afp|호주 연방경찰]]
- [[canada-rcmp|캐나다 왕립기마경찰(RCMP)]]
- [[sweden-police|스웨덴 경찰청]]
- [[netherlands-politie|네덜란드 국립경찰]]
- [[ireland-garda|아일랜드 Garda Síochána]]
- [[italy-dcsa|이탈리아 마약중앙수사국(DCSA)]]

**참여국(9개국):**
호주, 미국, 프랑스, 아일랜드, 이탈리아, 스웨덴, 캐나다, 네덜란드, 아이슬란드

**대략적 동원 인력:**
- 호주에서만 약 700명의 AFP(호주 연방경찰) 인력 투입

## Legal Framework

본 작전은 9개 관할권에 걸친 복수의 법적 근거에 의존하였다.

1. **[[budapest-convention|사이버범죄에 관한 부다페스트 협약]]** — 제29조 내지 제35조의 국제협력 조항은 당사국 간 국경을 초월한 증거 공유와 사법공조의 전반적 틀을 제공하였다.

2. **양자 MLAT(형사사법공조조약)** — 참여국 간 양자 형사사법공조조약은 공식적인 증거 요청, 특히 프랑스와 아이슬란드에서의 서버 압수를 가능하게 하였다.

3. **Europol 규정** — 국경 초월 작전 조율 및 Operational Taskforce 설치에 관한 Europol(유럽 경찰청)의 권한은 OTF NEXT를 위한 제도적 틀을 제공하였다.

4. **국내법:**
   - 호주: 1995년 형법(Criminal Code Act 1995) (통신범죄)
   - 프랑스: 형사소송법 (서버 압수)
   - 아일랜드: 형사사법법(Criminal Justice Act)
   - 이탈리아: 반마피아 법제

> [!note] Legal Basis Note
> 원용된 부다페스트 협약 및 양자 MLAT의 구체적 조항은 공개되지 않았다. 제29조 내지 제35조가 관련된다는 판단은 본 작전의 국경 초월 증거 수집 및 서버 압수 특성에 근거한다.

## Operational Timeline

| 일자 | 사건 |
|------|-------|
| ~2015 | Jay Je Yoon Jung이 Ghost 플랫폼을 제작한 것으로 알려짐 |
| 2022-03 | Europol(유럽 경찰청) OTF NEXT 하에서 Ghost에 대한 수사 개시 |
| 2022-2024 | AFP(호주 연방경찰)가 소프트웨어 업데이트 변조를 통한 Ghost 침투 기술 개발 |
| 2024-09-17 | 작전 1일차: 호주에서 압수수색 영장 집행 및 체포 개시 |
| 2024-09-18 | 작전 2일차: 아일랜드, 이탈리아, 캐나다, 스웨덴에서 거의 동시 압수수색 |
| 2024-09-18 | Jay Je Yoon Jung이 뉴사우스웨일스 Narwee 자택에서 체포됨 |
| 2024-09-18 | AFP(호주 연방경찰)와 Europol(유럽 경찰청)이 Operation Kraken을 발표하는 기자회견 개최 |
| 2024-09-18 | 프랑스 및 아이슬란드 소재 서버 압수 |
| 2024-09-18 | 총 51명 체포 발표: 호주 38명, 아일랜드 11명, 캐나다 1명, 이탈리아 1명 |
| 2024-10-03 | AFP(호주 연방경찰)가 Jung으로부터 930만 호주달러 상당의 암호화폐 압수 발표 |
| 2024-10 | Jung에게 추가 혐의 적용; 최대 26년 징역형 가능 |
| 2024-09 이후 | 아일랜드 고위험 범죄 네트워크 구성원 12명이 후속 작전에서 추가 체포됨 |

## Results and Impact

**체포(총 51명):**
| 국가 | 체포 인원 | 비고 |
|---------|---------|---------|
| 호주 | 38명 | 플랫폼 운영자 Jay Je Yoon Jung 포함 |
| 아일랜드 | 11명 | 고위험 범죄 네트워크 구성원 |
| 캐나다 | 1명 | — |
| 이탈리아 | 1명 | Sacra Corona Unita 마피아 조직원 |
| **합계** | **51명** | |

**해체된 인프라:**
- Ghost 암호화 플랫폼 영구 해체
- 프랑스 및 아이슬란드 소재 서버 압수
- 개조 스마트폰 유통망 해체
- 재판매업자 네트워크 해체

**압수:**
- 플랫폼 운영자로부터 약 930만 호주달러(약 640만 미국달러) 상당의 암호화폐 압수
- 불법 화기 및 무기 25점 (호주)
- 불법 마약 (200kg의 유통 차단)

**위협 차단:**
- AFP(호주 연방경찰)가 Ghost 통신 감청을 토대로 50건 이상의 생명 위협 사건에 개입
- 호주 시장으로의 200kg 분량 불법 마약 유통 차단

**후속 조치:**
- 2024년 9월 이후 아일랜드에서 고위험 범죄 네트워크 관련 12명 추가 체포
- 모든 참여 관할권에서 감청된 Ghost 통신에 대한 분석 진행 중

**Jay Je Yoon Jung에 대한 혐의:**
- 범죄조직 지원
- 범죄수익 취급
- 사기 목적 신원정보 거래
- 2024년 10월 추가 혐의 적용
- 최대 26년 징역형에 처할 수 있음

## Cooperation Mechanisms Used

1. **[[europol-jit|Europol(유럽 경찰청) Operational Taskforce (OTF NEXT)]]** — 주요 조율 메커니즘으로, FBI(미국 연방수사국)와 프랑스 헌병대가 공동 주도하고 Europol(유럽 경찰청)이 호스팅을 담당하였다. OTF NEXT는 정보 공유, 기술적 침투 조율, 9개국 법집행 조치의 동기화 등을 위한 틀을 제공하였다.

2. **[[mlat-process|형사사법공조(MLA)]]** — 공식 MLA 요청은 프랑스와 아이슬란드에서의 서버 압수 및 관할권 간 증거 공유를 뒷받침하였다.

3. **[[joint-investigation-team|합동수사팀(JIT)]]** — OTF NEXT의 구조는 JIT와 유사하며, 참여 기관들이 공식 협정에 따라 자원과 증거를 공유하였다.

4. **[[informal-cooperation|비공식 경찰 간 협력]]** — 2.5년에 걸친 수사 기간(2022년 3월~2024년 9월)은 광범위한 비공식 정보 공유와 조율을 수반하였다.

5. **기술적 협력** — 소프트웨어 업데이트 변조를 통한 Ghost 침투 역량 개발은 감청 구현을 위해 서버 호스팅 국가(프랑스, 아이슬란드)와의 기술적 협력을 요구하였다.

## Challenges and Friction Points

1. **기술적 복잡성** — 3중 암호화 플랫폼에 침투하기 위해서는 새로운 기법(전송되는 소프트웨어 업데이트의 변조) 개발이 필요했다. 이는 약 2년에 걸친 상당한 연구개발 투자를 요구하였다.

2. **다관할권 조율** — 9개국 및 다수의 시간대에 걸친 압수수색의 동기화는 피의자 간 상호 통보나 증거 인멸을 방지하기 위한 광범위한 사전 기획을 필요로 하였다.

3. **법적 증거능력** — 변조된 소프트웨어 업데이트 기법을 통해 확보된 증거는, 특히 감청 요건이 엄격한 법제에서 증거능력 문제에 직면할 수 있다.

4. **암호화 논쟁** — 본 작전은 법집행기관의 암호화 통신 접근과 사생활 권리 간 논쟁을 재점화한다. Ghost는 범죄 전용이었으나, 그 기술적 수단은 이론상 합법적 플랫폼에도 적용될 수 있다.

5. **범죄자 이동** — EncroChat, Sky ECC, AN0M 해체 이후 범죄자들은 Ghost로 이동하였다. Ghost 해체 이후 후속 플랫폼은 지속되는 술래잡기식 위험으로 남아 있다.

## Lessons Learned

1. **공급망 감청(supply-chain interception)**은 암호화 플랫폼에 침투하기 위한 실효성 있는 수단이다 — 전송되는 소프트웨어 업데이트를 변조함으로써 법집행기관은 암호화 해독 없이도 실시간 접근을 확보하였다.

2. **장기 수사(2년 이상)**가 복잡한 암호화 플랫폼 사건에서는 필수적이다. 2022년 3월부터 2024년 9월까지의 기간은 법집행 조치 이전 충분한 정보 수집을 가능하게 하였다.

3. **Europol(유럽 경찰청) OTF는** 다국적 암호화 플랫폼 작전에 효과적인 조율 메커니즘이며, EncroChat과 Sky ECC에서 확립된 모델을 기반으로 한다.

4. **범죄용 암호화 플랫폼 생태계는 반복적이다** — 각 해체는 일시적으로 범죄자를 교란하지만 새 플랫폼으로의 이동을 촉진한다. 지속적인 역량 투자가 요구된다.

5. **암호화폐 압수**는 상당한 억지력이 될 수 있다 — Jung으로부터 압수된 930만 호주달러는 범죄용 플랫폼 구축의 금전적 동기와 범죄수익 회수 가능성을 보여준다.

6. **생명 위협 정보**는 핵심 부산물이다 — 수사 기간 중 개입한 50건 이상의 생명 위협 사건은 인명을 구하였고 자원 투입을 정당화하였다.

## Follow-Up Actions

> [!warning] No public court documents found
> 웹 검색(2026-04-17) 결과 본 작전과 관련하여 공개적으로 접근 가능한 법원 문서를 찾지 못하였다. 가능한 이유는 다음과 같다: 공개 법원 기록 체계가 없는 비미국 관할권, 봉인된 절차, 또는 공식 기소로 이어지지 않은 작전.


- Jay Je Yoon Jung은 호주에서 재판 대기 중이며 최대 26년 양형에 처할 수 있다.
- Ghost 정보에 따라 아일랜드 고위험 범죄 네트워크 구성원 12명이 추가 체포되었다.
- 9개 참여 관할권 전반에서 감청된 Ghost 메시지 분석이 진행 중이다.
- AFP(호주 연방경찰)는 후속 플랫폼의 범죄용 암호화 통신 환경에 대한 모니터링을 지속하고 있다.
- Europol(유럽 경찰청)은 Ghost에서 도출된 정보의 다른 조직범죄 수사 적용 가능성을 평가하고 있다.

## Korean Involvement (한국의 참여)

Operation Kraken 또는 Ghost 플랫폼 수사에 한국이 직접 참여한 사실은 알려진 바 없다. 다만 다음과 같은 점에 유의할 필요가 있다.
- 본 작전은 [[australia-afp|AFP(호주 연방경찰)]]와 한국 [[knpa|경찰청(KNPA)]] 간 양자 협력 협정이 존재한다는 점, 그리고 본 사건에서 개척된 수사 기법(소프트웨어 업데이트 침투)이 전이 가능한 역량에 해당한다는 점에서 한국 법집행기관에 시사하는 바가 있다.
- 한국의 조직범죄 집단도 암호화 통신 플랫폼을 사용하는 것으로 알려져 있으며, Ghost 사례의 교훈은 적용 가능하다.
- Jay Je Yoon Jung 사건은 한국계 호주인(코리안-오스트레일리안) 국적자가 연루된 사안이나, 본 수사의 국제협력 측면과는 무관하다.

## Contradictions & Open Questions

**미해결 의문점:**
1. 전 세계 Ghost 이용자의 정확한 수는 얼마인가? 출처에 따라 "수천 명"으로 다양하게 기술되어 있을 뿐 구체적 수치는 제시되지 않았다.
2. AFP(호주 연방경찰)는 변조된 소프트웨어 업데이트 기법을 통해 얼마나 많은 메시지를, 그리고 어느 기간 동안 감청하였는가?
3. 50건 이상의 "생명 위협" 개입 가운데 호주 외 관할권에 전달된 것이 있는가?
4. Ghost에서 도출된 정보로 인해 전 세계적으로 얼마나 많은 형사 사건이 처리될 것인가?
5. Ghost 해체 이후 범죄 네트워크는 어떤 후속 플랫폼으로 이동하였는가?
6. 프랑스와 아이슬란드에서 압수된 서버는 최초 51명 이외의 체포로 이어진 증거를 산출하였는가?
7. Europol(유럽 경찰청) 보도자료에는 수사가 2022년 3월에 시작되었다고 적시되어 있으나, 그 이전 AFP(호주 연방경찰) 보고에서는 그보다 앞서 최초 탐지가 있었음을 시사한다. AFP의 Ghost 발견 시점에 관한 정확한 연혁은 공개 자료에서 해소되지 않았다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Australian Federal Police, 2024-09-18: AFP Operation Kraken charges alleged head of global organised crime app.
- Eurojust, 2024-09-18: 51 arrests in wide-scale operation to take down encrypted communication platform used by organised crime groups.
- Europol, 2024-11-01: 12 members of an Irish high-risk criminal network arrested.
- Reuters, 2024-09-18: Ghost cybercrime platform dismantled in global operation, 51 arrested.
- The Register, 2024-09-18: 51 arrests made in global takedown of Ghost crime platform.
- The Record, 2024-09-18: Police announce takedown and arrest mastermind behind criminal comms platform 'Ghost'.
- Information Age / ACS, 2024-10-03: $9m in crypto seized from accused Ghost app creator.

## Evidence and Attribution Notes

- Operation Kraken(크라켄 작전, AFP)은 [[australia-afp|호주 연방경찰(AFP)]]이 주도하고, Europol(유럽 경찰청)이 운영적으로 조율하였으며, Eurojust(유럽 사법협력기구)가 프랑스-미국 합동수사팀을 통해 사법적으로 지원한 다국적 법집행 작전이다.
- 본 작전은 2024년 9월 17~18일에 호주, 아일랜드, 이탈리아, 캐나다, 스웨덴 전역에서 거의 동시에 이루어진 압수수색으로 정점에 이르렀다.
- 플랫폼의 제작자이자 운영자로 지목된 **Jay Je Yoon Jung**(32세, 호주 뉴사우스웨일스 거주)은 시드니 Narwee 자택에서 체포되었다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아닌, Ghost 암호화 통신 플랫폼에 대한 인프라 압수 작전을 기술한다는 점에서 정본(canonical) 작전으로 유지된다. 본 기록은 주도 책임을 호주 연방경찰(AFP)에, 운영적 조율을 Europol(유럽 경찰청)에, 사법 조율 증거를 Eurojust(유럽 사법협력기구)에 귀속시키며, 참여 또는 영향을 받은 관할권으로 호주, 미국, 프랑스, 아일랜드, 이탈리아, 스웨덴, 캐나다, 네덜란드, 아이슬란드를 기재한다.

협력 모델은 기관 및 파트너의 이름을 통해 문서화되어 있다: 호주 연방경찰(AFP), Europol(유럽 경찰청), Eurojust(유럽 사법협력기구), FBI(미국 연방수사국), 프랑스 헌병대, 캐나다 왕립기마경찰(RCMP), 네덜란드 국립경찰, 아일랜드 Garda Síochána, 이탈리아 마약중앙수사국(DCSA), 스웨덴 경찰청; 메커니즘: Europol Operational Taskforce(OTF), 형사사법공조, 합동수사팀, 비공식 경찰 간 협력; 법적 근거: 사이버범죄에 관한 부다페스트 협약(제29조~제35조) 및 양자 형사사법공조조약; 집행 양태: 체포, 압수, 해체.

정본 기록상 운영 결과: 체포 51명; 암호화폐/자산 결과는 930만 호주달러(플랫폼 운영자로부터)로 기록; Ghost 암호화 통신 플랫폼 영구 해체; 플랫폼 운영자 Jay Je Yoon Jung 체포(호주 뉴사우스웨일스); 호주 38명, 아일랜드 11명, 캐나다 1명, 이탈리아 1명 체포; 50건 이상의 생명 위협 개입.

정본 출처 집합은 7개의 참고문헌을 포함한다: [1] AFP (2024-09-18), [2] Eurojust (2024-09-18), [3] Reuters (2024-09-18), [4] The Register (2024-09-18), [5] The Record (2024-09-18), [6] Information Age / ACS (2024-10-03), [7] Europol (2024-11-01).
출처 하한선은 정본 작전 요건을 충족하나, 출처의 폭만으로 모든 하류 체포 또는 양형이 본 작전의 일부임이 입증되지는 않는다. 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
현재 본 페이지에는 frontmatter상 missing-field 표지가 적용되어 있지 않다.
데이터셋 활용 측면에서, 본 페이지는 작전 수준의 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 조율된 법집행 조치 전반을 기술한다. 이후의 기소, 유죄 인정, 양형, 범죄인 인도, 또는 몰수 조치는 출처가 이를 명시적으로 새로운 다국적 작전으로 제시하지 않는 한 관련 사건 또는 흡수됨(absorbed) 후속 기록으로 연결되어야 한다.
출처 기록이 보다 광범위한 배경, 반복적인 통신사 재배포, 또는 토픽 페이지성 자료를 포함하는 경우, 본 평가는 명명된 작전, 참여 당국, 표적 인프라 또는 범죄 서비스, 그리고 측정 가능한 집행 결과에 직접 결부된 사실에 우선순위를 둔다. 주변적 출처 제목은 독립적 분류 또는 결과 증거로 취급되지 않는다.
이로써 정본 기록은 분석적으로 한정되고 재현 가능한 상태로 유지된다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | AFP Operation Kraken, 전 세계 조직범죄 앱의 수괴로 지목된 인물 기소 | Australian Federal Police | 2024-09-18 | https://www.afp.gov.au/news-centre/media-release/afp-operation-kraken-charges-alleged-head-global-organised-crime-app |
| [2] | 조직범죄집단이 사용한 암호화 통신 플랫폼 해체 광역작전에서 51명 체포 | Eurojust | 2024-09-18 | https://www.eurojust.europa.eu/news/51-arrests-wide-scale-operation-take-down-encrypted-communication-platform-used-organised-crime-groups |
| [3] | Ghost 사이버범죄 플랫폼, 전 세계 작전으로 해체되고 51명 체포 | Reuters | 2024-09-18 | https://www.reuters.com/technology/cybersecurity/ghost-cybercrime-platform-dismantled-global-operation-51-arrested-2024-09-18/ |
| [4] | Ghost 범죄 플랫폼 전 세계 해체 작전에서 51명 체포 | The Register | 2024-09-18 | https://www.theregister.com/2024/09/18/51_arrests_ghost_platform/ |
| [5] | 경찰, 범죄용 통신 플랫폼 'Ghost' 배후의 주모자 해체·체포 발표 | The Record | 2024-09-18 | https://therecord.media/ghost-encrypted-criminal-communications-takedown-arrests |
| [6] | Ghost 앱 제작 혐의자로부터 900만 달러 상당의 암호화폐 압수 | Information Age / ACS | 2024-10-03 | https://ia.acs.org.au/article/2024/9m-in-crypto-seized-from-accused-ghost-app-creator.html |
| [7] | 아일랜드 고위험 범죄 네트워크 구성원 12명 체포 | Europol | 2024-11-01 | https://www.europol.europa.eu/media-press/newsroom/news/12-members-of-irish-high-risk-criminal-network-arrested |
