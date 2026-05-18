## 개요

Operation Trojan Shield(트로이안 쉴드 작전, ANOM)는 [[fbi-cyber-division|FBI(미국 연방수사국)]]와 [[australia-afp|호주 연방경찰(Australian Federal Police)]]이 ANOM(FBI 운영 암호화 통신 플랫폼) 단말기를 초국가적 범죄 네트워크에 침투시키고, 이후 법원이 허가한 해당 통신에 대한 접근권을 활용해 조율된 체포 및 압수를 지원한 다년도 잠입 작전이다. FBI(미국 연방수사국) 및 Europol(유럽 경찰청)의 공식 성명은 본 작전을 암호화된 범죄 통신에 대해 수행된 사상 최대 규모의 법집행 작전으로 기술한다.

본 활동은 2021년 6월 8일 십수 개국 이상에서 동시에 체포·수색·압수가 집행되면서 공개적으로 정점에 이르렀다. 본 작전은 잠입 플랫폼 운용, 정보 공유, 다국적 증거 활용의 교차점에 위치한다는 점에서 본 위키에 중요한 의미를 갖는다.

## 배경

### Modus operandi

ANOM(FBI 운영 암호화 통신 플랫폼)은 비밀 운영자 네트워크를 통해 공급된 FBI(미국 연방수사국)/AFP(호주 연방경찰) 공동 개발 암호화 단말 플랫폼이었다. 이전의 범죄용 암호화 전화 교란 사례(예: 2018년 Phantom Secure, 2020년 EncroChat, 2021년 Sky ECC)로 인해 조직범죄단이 새로운 공급자를 모색하게 되자, 법집행 기관 및 협력 기관은 안전하다고 여겨지는 단말 생태계에 대한 수요를 활용하였다. FBI 및 SDCA 기소 자료에 따르면, ANOM 단말은 외관상 일반적인 Android 단말기에 강화된 메시지 기능이 탑재된 형태였으나, 통상적인 기능(음성 통화, 이메일, GPS)이 모두 제거되었고 계산기 아이콘 속에 은닉된 암호화 메시징 앱이 구동되었다. 범죄 최종 사용자는 단말 하나당 6개월마다 약 USD 1,500-2,500을 지불하였으며, 다른 ANOM 사용자에게만 메시지를 전송할 수 있어 순수한 범죄 트래픽 채널이 형성되었다. **사용자가 인지하지 못한 가운데, ANOM 앱은 모든 메시지 및 첨부 파일을 평문으로 FBI 통제 서버에 블라인드 복제(BCC)하였으며**, 협력 기관은 해당 트래픽을 거의 실시간으로 열람할 수 있었다. 작전 기간 동안 플랫폼은 45개 이상 언어로 작성된 약 **2,700만 건의 메시지**를 산출하였고, 여기에는 마약 운송, 무기 이동, 자금세탁 경로, 청부 살인 및 정치적 부패 자금 지급에 관한 운영 계획이 포함되었다.

### Victim profile and impact

전형적인 사이버범죄 국제공조 작전과 달리, 본 작전의 피해자군은 단일한 컴퓨터 범죄 행위의 직접 피해자가 아니라 ANOM 상에서 논의된 인신매매, 폭력, 부패 활동에 노출된 광범위한 민간 인구이다. Europol(유럽 경찰청) 및 SDCA 기소 자료에 따르면, ANOM에서 도출된 정보를 통해 최소 **150건의 임박한 살인 위협**(계획된 청부 살인 및 폭력 행위 차단)에 대한 직접 개입이 이루어졌으며, **코카인 8톤, 대마초 22톤, 메스암페타민 및 암페타민 2톤, 합성마약 전구물질 6톤, 화기 250정**과 더불어 현금 및 가상자산 **USD 4,800만 이상**이 압수되었다. 간접 피해자군에는 차단된 마약의 소비 시장, 150건 이상의 차단된 폭력 위협의 대상자, 그리고 다수 참여국 ANOM 트래픽을 통해 식별된 법집행 공무원의 부패 피해자가 포함된다.

### Financial flow

ANOM을 통해 드러난 불법 자금 흐름에는 (i) 호주, 네덜란드, 독일, 미국에 걸쳐 마약 수익을 이동시킨 **대량 현금 운반 네트워크**, (ii) 인신매매 수익에 대한 **암호화폐 자금세탁**(수천만 달러 규모의 가상자산 압수), (iii) 다대륙에 걸친 부동산 및 대량 상품 거래를 통한 **무역 기반 자금세탁**, (iv) 최소 한 개 이상의 EU 회원국 등 매수된 공직자에 대한 **부패 자금 지급**이 포함된다. 플랫폼 자체는 정기 단말 구독료(단말당 6개월마다 USD 1,500-2,500, 유통 단말 12,000대 이상)를 통해 범죄 운영자/유통업자에게 수익을 창출하였으며, 이후 유통 네트워크에 대한 SDCA 기소에서 이는 RICO 수익으로 취급되었다(2026년 4월 17일 SDCA 유통업자 양형(63개월) 참조).

### Criminal organization structure

Europol(유럽 경찰청)에 따르면, ANOM 사용자 기반은 100개국 이상에서 활동하는 **300개 이상의 초국가적 범죄 신디케이트**에 걸쳐 있었다. 주요 사용자 클러스터로는 호주 무법 모터사이클 갱(OMCG), 이탈리아 조직범죄 관련자(유럽 및 남미에서 활동하는 'Ndrangheta 연계 가문 포함), 발칸 인신매매 카르텔, 홍콩 및 태국을 통해 활동하는 아시아 마약 거래 네트워크, 남미 마약 공급책 등이 식별되었다. 플랫폼 자체는 범죄조직(OCG)이 아니었으며, 기존 범죄조직에 의도적으로 침투시킨 정보 채널이었으나, ANOM 유통 네트워크(범죄 커뮤니티 내 마케팅 노드 역할을 한 지역 재판매업자의 위계 구조)는 그 자체로 SDCA ANOM Enterprise 기소([[us-v-anom-distributors]])에서 RICO 기업체로 기소되었다.

Operation Trojan Shield(트로이안 쉴드 작전, ANOM)는 공개 단계 이전에 증거적 가치를 산출하였으며, 이로 인해 본 작전은 교란 행동인 동시에 장기적 정보 수집 프로그램의 성격을 갖게 되었다.

## 참여 당사자

### Lead Agency
- [[fbi-cyber-division|FBI Cyber Division]]

### Coordinating and Core Partners
- [[australia-afp|Australian Federal Police]]
- [[europol-ec3|Europol EC3]]
- [[netherlands-politie|Dutch National Police]]
- [[sweden-police|Swedish Police Authority]]

### Participating Jurisdictions
- [[united-states|미국]]
- [[australia|호주]]
- [[netherlands|네덜란드]]
- [[sweden|스웨덴]]
- [[germany|독일]]
- [[international|기타 다수의 협력 관할권]]

## Legal Framework

공개된 기록은 잠입 권한, 사법적 감독을 받는 감청 또는 합법적 접근 메커니즘, 그리고 국경 간 증거 공유의 혼합을 시사한다. 정확한 법적 절차는 관할권별로 상이하였으나, 운영 모델은 통신 플랫폼의 잠입 배치, 메시지 트래픽에 대한 합법적 접근, 그리고 조율된 국제 증거 활용을 위한 [[mutual-legal-assistance|형사사법공조]]에 의존하였다.

## 작전 타임라인

| 일시 | 사건 |
|------|-------|
| 2018년 | ANOM 잠입 플랫폼이 범죄 네트워크에서 유통 개시 |
| 2019-2020년 | 협력 관할권 전반에서 대량 메시지 수집 및 분석 |
| 2021년 6월 8일 | 공개 발표 및 글로벌 동시 집행 단계 |

## 결과 및 영향

| 지표 | 보고된 결과 |
|--------|-----------------|
| 체포 | 800명 이상 |
| 수색 | 700건 이상 |
| 영향을 받은 범죄 신디케이트 | 300개 이상 |
| 검토된 메시지 | 2,700만 건 |
| 유통된 단말 | 12,000대 이상 |
| 마약 압수 | 코카인 8톤, 대마초 22톤 |
| 화기 압수 | 250정 |
| 현금/자산 압수 | USD 4,800만 이상 |

이 규모는 본 작전이 암호화된 통신 자체를 주요 증거 채널로 전환하였다는 점에서 의의를 갖는다. 또한 본 작전은 다국적 시점 조율이 결정적임을 보여주었다. 즉, 공개 행동 개시 이전에 정보 수집이 와해되지 않도록 체포 및 수색을 동기화해야 했다.

## Cooperation Mechanisms Used

- [[joint-investigation-team|다국적 법집행 구조를 통한 작전 조율]]
- [[mutual-legal-assistance|국경 간 증거 및 체포 지원]]
- 잠입 플랫폼 배치 및 정보 공유

## Challenges and Friction Points

- ANOM(FBI 운영 암호화 통신 플랫폼)의 비밀 신뢰성을 유지하기 위해서는 장기적 운영 규율이 요구되었다.
- 데이터셋이 방대하고 시간적으로 민감하였기에 메시지 활용은 분석상의 부담을 야기하였다.
- 증거적 가치를 산출한 동일한 플랫폼은, 임박한 폭력이 메시지를 통해 드러났을 때 개입 딜레마를 동시에 발생시켰다.

## Follow-Up Actions

Operation Trojan Shield(트로이안 쉴드 작전, ANOM)는 [[us-v-anom-distributors]] 및 그에 연계된 후속 작전 [[operation-us-v-anom-distributors]] 등 후속 기소 및 피고인 특정 집행 페이지를 산출하였다. 또한 이후 범죄 통신 서비스에 대한 합법적 접근의 한계와 가능성에 관한 논의에서 벤치마크 사례가 되었다.

## Contradictions & Open Questions

- **L26 gap — 직접적 사이버 피해자 귀속**: Operation Trojan Shield(트로이안 쉴드 작전, ANOM)의 피해자 프로필은 컴퓨터 범죄 행위의 직접적 사이버 피해자가 아닌, ANOM에서 논의된 인신매매·폭력·부패 활동에 의해 구성된다. ANOM 기반 기소를 차단된 범죄 활동 하류의 피해자군과 매핑하는 작업은 관련 사건 페이지로 위임된다.
- **L26 gap — 전체 자금세탁 회랑 지도**: 대량 현금, 암호화폐, 무역 기반, 부패 자금 지급 채널이 각각 입증되었으나, 16개 이상의 참여 관할권 전반에 걸쳐 ANOM 트래픽에서 도출된 통합 회랑 지도는 공개된 바 없다.
- **L26 gap — 범죄조직 명부**: Europol(유럽 경찰청)의 "300개 이상의 범죄 신디케이트" 표현은 집계치이다. 개별 신디케이트의 명칭, 위계 및 Operation Trojan Shield(트로이안 쉴드 작전, ANOM)에 귀속 가능한 신디케이트별 체포 수치는 각국 기소 기록에 분산되어 있으며, 통합된 바 없다.
- **각 관할권의 합법적 접근 적법성**: 합법적 접근의 근거는 협력국마다 상이하였으며 — 협력 관할권을 통한 제3국 중계(일부 보도에서 리투아니아가 중계국으로 공개적으로 식별됨)는 일부 국내 법원이 공개 단계 이후에야 다룬 증거 능력 문제를 제기하였다. 16개 이상의 관할권 전반에 걸친 법적 권한의 통합 지도는 공개된 바 없다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- US Federal Bureau of Investigation, 2021-06-08: FBI and Global Partners Announce Results of Operation Trojan Shield.
- Europol, 2021-06-08: 800 criminals arrested in biggest ever law enforcement operation against encrypted communication.
- FBI, 2021-06-08: FBI and Global Partners Announce Results of Operation Trojan Shield.
- US DOJ (Southern District of California), 2021-06-08: FBI's Encrypted Phone Platform Infiltrated Hundreds of Criminal Syndicates; Result is Massive Worldwide Takedown.
- justice.gov, 2026-04-17: Distributor of ANOM Hardened Encrypted Devices Sentenced to 63 Months in Prison for Racketeering Conspiracy.

## Evidence and Attribution Notes

- 2021년 6월 8일자 Operation Trojan Shield(트로이안 쉴드 작전, ANOM) 결과에 관한 FBI(미국 연방수사국) 공식 발표.
- 16개국 이상에서 800명 이상 체포, 2,700만 건의 암호화 메시지 검토.
- FBI(미국 연방수사국)-AFP(호주 연방경찰) 공동 개발 ANOM(FBI 운영 암호화 통신 플랫폼) 단말 플랫폼, 12,000대 이상의 단말 유통.
- Operation Trojan Shield(트로이안 쉴드 작전, ANOM)는 FBI(미국 연방수사국)와 호주 연방경찰이 ANOM(FBI 운영 암호화 통신 플랫폼) 단말을 초국가적 범죄 네트워크에 침투시키고, 법원이 허가한 통신 접근권을 활용해 조율된 체포 및 압수를 지원한 다년도 잠입 작전이다.
- FBI(미국 연방수사국) 및 Europol(유럽 경찰청)의 공식 성명은 본 작전을 암호화된 범죄 통신에 대해 수행된 사상 최대 규모의 법집행 작전으로 기술한다.
- FBI(미국 연방수사국), 네덜란드 국가경찰 및 스웨덴 경찰청이 Europol(유럽 경찰청) 및 16개 협력국의 지원을 받음.
- 700건 이상의 가택수색, 800명 이상 체포, 코카인 8톤, 대마초 22톤, 화기 250정, USD 4,800만 이상 압수.
- ANOM(FBI 운영 암호화 통신 플랫폼) 플랫폼: 12,000대 이상의 단말, 100개국 이상에 걸친 300개 이상의 범죄 신디케이트, 18개월에 걸쳐 2,700만 건의 메시지 검토.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- US Federal Bureau of Investigation, 2021-06-08: The FBI, along with the Drug Enforcement Administration, Australian Federal Police, Europol, and law enforcement partners in more than a dozen countries, are announcing the results of that covert effort, known as Operation Trojan Shield.
- US Federal Bureau of Investigation, 2021-06-08: Law enforcement has also been able to mitigate direct threat-to-life situations.
- FBI, 2021-06-08: The FBI, along with the Drug Enforcement Administration, Australian Federal Police, Europol, and law enforcement partners in more than a dozen countries, are announcing the results of that covert effort, known as Operation Trojan Shield.
- FBI, 2021-06-08: Law enforcement has also been able to mitigate direct threat-to-life situations.
- justice.gov, 2026-04-17: Attorneys Front Office Office Criminal Division Civil Division Other Agencies District History Programs Victim Witness Assistance Project Safe Neighborhoods Project Guardian Project Safe Childhood Environmental Justice ## Extraction Notes - parser: document - fetcher: doj_fetch - fetched_at: 2026-04-25T14:21:03+00:00 - final_url:

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정의 후속 행동이 아닌, ANOM(FBI 운영 암호화 통신 플랫폼) 단말에 의존하는 초국가적 조직범죄 네트워크에 대한 잠입 작전을 기술하므로 정본(canonical) 작전으로 보존된다. 본 기록은 주도 기관 책임을 Fbi Cyber Division에, 조율을 Europol Ec3에 귀속시키고 있으며, 참여 또는 영향을 받은 관할권은 미국, 호주, 네덜란드, 스웨덴, 독일, International로 기록된다.

협력 모델은 명명된 기관 및 파트너를 통해 문서화된다: Fbi Cyber Division, Australia Afp, Europol Ec3, Netherlands Politie, Sweden Police; 메커니즘: Joint Investigation Team; 법적 근거: mutual legal assistance; 집행 자세: Infiltration, Arrest, Seizure, Indictment.

정본 기록을 위해 포착된 작전 결과: 800명 체포, 암호화폐/자산 결과는 현금 및 가상자산 USD 4,800만 이상 압수로 기록, 2,700만 건 메시지 검토, 12,000대 이상 ANOM(FBI 운영 암호화 통신 플랫폼) 단말 유통, 700건 이상 수색 수행, 코카인 8톤 및 대마초 22톤 압수.

정본 출처군은 6개의 참조를 포함한다: 2021 06 08 Fbi Operation Trojan Shield, 2021 06 08 Europol Trojan Shield An0m, 2021 06 08 Fbi Gov Fbi And Global Partners Announce Results Of Operation Trojan Shield, 2021 06 08 Europol Europa Eu 800 Criminals Arrested In Biggest Ever Law Enforcement Operation Against Encrypt, 2021 06 08 Sdca Anom Enterprise Indictment, 2026 04 17 Justice Gov Distributor Anom Hardened Encrypted Devices Sentenced 63 Months Prison Racketeer.
정본 작전의 출처 하한선은 충족되나, 출처의 폭만으로 모든 하류 체포 또는 양형이 본 작전의 일부임이 입증되지는 않는다. 후속 기록은 별도로 연결되어 유지되어야 한다.
본 페이지에는 현재 프론트매터 누락 필드 플래그가 부여되어 있지 않다.
데이터셋 활용 측면에서, 본 페이지는 작전 수준의 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘 및 결과 필드는 조율된 집행 행동 전체를 기술한다. 이후의 기소, 답변 협상, 양형, 범죄인 인도 또는 자산 몰수 행동은 출처가 명시적으로 이를 새로운 다국적 작전으로 제시하지 않는 한 관련 사건 또는 흡수된 후속 기록으로 첨부되어야 한다.
출처 기록이 보다 광범위한 배경, 반복된 통신사 재게재 또는 토픽 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 그 참여 당국, 표적 인프라 또는 범죄 서비스 및 측정 가능한 집행 결과와 직접적으로 연결된 사실에 우선순위를 부여한다. 주변적 출처 제목은 독립적 분류 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정된 상태로 그리고 재현 가능하게 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | FBI and Global Partners Announce Results of Operation Trojan Shield | FBI | 2021-06-08 | https://www.fbi.gov/news/stories/fbi-global-partners-announce-results-of-operation-trojan-shield-060821 |
| [2] | 800 criminals arrested in biggest ever law enforcement operation against encrypted communication | Europol | 2021-06-08 | https://www.europol.europa.eu/media-press/newsroom/news/800-criminals-arrested-in-biggest-ever-law-enforcement-operation-against-encrypted-communication |
| [3] | FBI's Encrypted Phone Platform Infiltrated Hundreds of Criminal Syndicates; Result is Massive Worldwide Takedown | US DOJ (Southern District of California) | 2021-06-08 | https://www.justice.gov/usao-sdca/pr/fbi-s-encrypted-phone-platform-infiltrated-hundreds-criminal-syndicates-result-massive |
| [4] | Distributor of ANOM Hardened Encrypted Devices Sentenced to 63 Months in Prison for Racketeering Conspiracy | justice.gov | 2026-04-17 | https://www.justice.gov/usao-sdca/pr/distributor-anom-hardened-encrypted-devices-sentenced-63-months-prison-racketeering |
