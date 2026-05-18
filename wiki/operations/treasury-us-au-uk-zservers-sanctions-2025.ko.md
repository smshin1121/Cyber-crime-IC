## 개요

**2025-02-11**, 미국 재무부 해외자산통제국(OFAC), 호주 외교통상부(DFAT), 영국 외교·연방·개발부(FCDO)는 [[ransomware-ic|LockBit 랜섬웨어]] 활동을 실질적으로 지원한 사유로 러시아 바르나울에 본사를 둔 방탄 호스팅(BPH) 사업자 **Zservers**를 공동 지정하였다. OFAC은 동시에 Zservers의 러시아 국적 운영자 2명, Alexander Igorevich Mishin과 Aleksandr Sergeyevich Bolshakov를 [[asset-freezing|행정명령 14144호로 추가 개정된 행정명령 13694호]]에 따라 지정하였다. 영국 FCDO는 같은 날 추가로 **XHOST Internet Solutions LP**(Zservers와 연계된 영국 등기 위장회사) 및 직원 4명(Ilya Sidorov, Dmitriy Bolshakov, Igor Odintsov, Vladimir Ananev)을 보충 지정하였다. 본 조치는 *거의 확실히* 러시아 BPH 인프라에 대한 2025년 미-호-영 3국 공조의 첫 번째 진입점에 해당한다.

## 배경

LockBit는 러시아 기반 서비스형 랜섬웨어(RaaS) 운영체로서, 재무부 보도자료에 따르면 "가장 광범위하게 배포된 랜섬웨어 변종 중 하나"이며 2023년 11월 중국공상은행(ICBC) 미국 브로커-딜러 공격의 책임자였다. [[operation-cronos-phase1|Operation Cronos 1단계]](2024년 2월) 및 [[operation-cronos-phase3|Operation Cronos 3단계]](2024년 5월) 단속 이후 LockBit의 누설 사이트 및 관리자 인프라는 약화되었으나 affiliate 생태계는 소멸되지 않았으며, affiliate 운영은 *방탄 호스팅* — 설계상 남용 신고에 의한 차단을 거부하고 사법기관의 교란 시도를 좌절시키는 서비스 사업자 — 을 지속적으로 필요로 하였다.

재무부 조치는 *가능성이 매우 높게* affiliate를 직접 겨냥하기보다 BPH 공급층을 공격하기 위해 설계되었다. 재무부는 본 보도자료를 2024년 Alexander Ermakov 및 Evil Corp 랜섬웨어 그룹 구성원에 대한 3국 사이버 제재의 후속으로 자리매김함으로써, 미-호-영 사이버 제재 셀이 공조를 지속하고 있음을 신호한다.

## 참여 당사자

- **미국** — OFAC(주관 지정 기관); DOJ(미국 법무부) 및 FBI(미국 연방수사국)가 보도자료에 따라 보강 수사를 지원.
- **영국** — FCDO가 Zservers + Mishin + Bolshakov를 병행 지정하고, *추가적으로* XHOST Internet Solutions LP 및 OFAC이 등재하지 않은 영국 측 4인을 지정.
- **호주** — DFAT가 자국 독자적 사이버 제재 체제에 따라 지정.
- **러시아** — Zservers 및 지정된 6인 자연인 전원(OFAC 측 2인, 영국 측 추가 4인)의 호스팅·체재 관할; 2022년 이후 러시아-서방 사법 채널의 붕괴를 고려할 때 러시아 당국의 공조는 *거의 확실히* 부재함.

> [!note] 캐나다의 역할
> 보도자료는 LockBit affiliate에 대한 2022년 수색 — Zservers IP에서 LockBit 프로그래밍 인터페이스를 실행 중이던 노트북을 확보한 증거 — 의 공을 "캐나다 사법당국"에 돌린다. 보도자료에는 구체적 캐나다 기관명이 적시되지 않는다. 이는 명시적으로 언급된 유일한 비-3국 외국 공조이다.

## 법적 근거

- **지정 권한(미국):** 행정명령 13694호(2015) — "주요 사이버 이용 악성 활동에 관여하는 일부 인물의 재산 동결" — 행정명령 14144호(2025)로 *추가 개정*. Zservers, Mishin, Bolshakov는 모두 이 권한에 따라 지정되었다.
- **지정 권한(영국):** 2020년 영국 사이버(제재) 규정 — 동일자 FCDO 등재를 통해 적용; 표준 FCDO 3국 템플릿을 고려할 때 *가능성이 매우 높은* 근거이나, 재무부 보도자료 자체는 영국 법령을 열거하지 않는다.
- **지정 권한(호주):** 2011년 독자적 제재법 / 2021년 독자적 제재(지정자·실체 및 선언자 — 주제별 제재) 수단 — 동일 3국 템플릿에 따라 DFAT 조치의 *가능성이 매우 높은* 근거.

본 조치는 범죄인 인도, MLAT, 또는 [[mutual-legal-assistance|형사사법공조]]에 의존하지 **않으며**, 러시아의 공조 없이 작동하는 순수한 경제 제재 수단이다.

## 작전 타임라인

- **2022년** — 캐나다 사법당국이 알려진 LockBit affiliate를 수색하여 Zservers가 재임대한 IP 주소에서 LockBit 프로그래밍 인터페이스를 실행 중이던 노트북을 확보. *(수사 단초.)*
- **2022년** — 러시아 사이버범죄자가 Zservers로부터 IP 주소를 구매. *거의 확실히* LockBit 채팅 서버 용도.
- **2023년** — Zservers가 러시아 IP 주소를 포함한 인프라를 LockBit affiliate에게 임대.
- **2023년** — 레바논 회사가 Zservers IP가 LockBit 랜섬웨어 공격에 사용되고 있다고 신고하자, Mishin이 Bolshakov에게 악성 사용자에게 새 IP 주소를 할당하도록 지시하면서 신고자에게는 원래 IP를 차단하였다고 통보. *(인지된 조력 증거.)*
- **2024년(전년)** — Alexander Ermakov 및 Evil Corp에 대한 미-호-영 3국 사이버 제재가 본 조치의 템플릿을 형성.
- **2025-02-11** — 3국 지정 발표. OFAC: Zservers + Mishin + Bolshakov. FCDO: 동일 3인에 더하여 XHOST Internet Solutions LP + Sidorov + Dmitriy Bolshakov + Odintsov + Ananev. DFAT: 독자적 제재 체제에 따른 병행 지정.

## 결과 및 영향

| 지정 기관 | 실체 | 개인 |
|---|---|---|
| OFAC(미국) | 1 — Zservers | 2 — Mishin, Bolshakov |
| FCDO(영국) | 2 — Zservers, XHOST Internet Solutions LP | 6 — Mishin, A. Bolshakov, Sidorov, D. Bolshakov, Odintsov, Ananev |
| DFAT(호주) | 독자적 체제에 따른 병행 등재 | 독자적 체제에 따른 병행 등재 |

LockBit 운영의 직접적 교란은 단기적으로 *가능성 낮음*이다. (i) BPH 실체가 물리적으로 러시아에 잔류하며, (ii) 서버가 압수되지 않았고, (iii) 개인이 체포되지 않았기 때문이다. 본 조치의 가치는 *가능성이 매우 높게* 기대 형성 및 공급망 비용 부과에 있다. 러시아 BPH 사업자는 더 이상 탐지되지 않는 서방 위장회사 구조를 기대할 수 없으며, Zservers 또는 XHOST를 경유하는 결제를 다루는 모든 서방 금융기관은 이제 2차 제재 위험에 노출된다. 이는 사법 교란 트랙([[operation-cronos-phase1|Cronos 1단계]], [[operation-cronos-phase3|Cronos 3단계]])을 대체하기보다는 보완한다.

## 활용된 협력 메커니즘

- **3국 정보 공유** — 미(OFAC), 영(FCDO), 호(DFAT)는 동일자에 지정을 공조하였다. 구체적 정보 공유 수단은 공개되지 않으며, 조약 기반 MLAT 요청이 아닌 *가능성이 매우 높은* 파이브 아이즈 / 사이버 제재 셀 채널을 통한 것으로 보인다.
- **국내 부처 간 공조** — 보도자료에 따라 DOJ(미국 법무부)와 FBI(미국 연방수사국)가 보강 수사를 지원.
- **외국 사법기관 입력** — 2022년 캐나다 수색이 기초 증거를 산출하였으며, 동 증거가 OFAC에 도달한 경로는 명시되지 않는다.
- **제재 체제 중첩** — 영국 FCDO는 OFAC이 효과적으로 도달할 수 없는 영국 등기 위장(XHOST Internet Solutions LP)을 추가로 지정하였다. 3국 구조는 단일 관할이 단독으로 행동할 때보다 지리적·법인적 도달 범위를 확장한다.

## 도전 과제 및 마찰 지점

- **범죄인 인도 경로 부재.** 지정된 6인 자연인은 모두 러시아 국적이며 *거의 확실히* 러시아에 체재 중이다. 현 조건에서 체포 또는 범죄인 인도는 *가능성이 매우 낮음*.
- **물리적 압수 부재.** 보도자료는 어떠한 서버, 도메인, 또는 암호화폐 압수도 기록하지 않는다 — 순수 지정 조치.
- **OFAC 본문 내 영국 보충 사항의 미확인.** XHOST + 직원 4명에 대한 영국 FCDO 지정은 OFAC 보도자료 본문에 이름으로 열거되지 않는다. 완전한 인용 정확성을 위해서는 FCDO 제재 고시와의 교차 확인이 필요하다.
- **리브랜딩 위험.** [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|2025년 11월 SB-0319 지정]]에 기록된 Aeza → Hypercore 리브랜딩 사례에서 후속적으로 확인되듯이, BPH 사업자는 통상 새로운 위장 하에 재법인화하므로 지속적 모니터링이 필요하다.

## 교훈

- **BPH 계층은 지정 가능하다.** affiliate가 아닌 호스팅 사업자를 제재 표적으로 취급하는 것은 affiliate가 신속히 대체할 수 없는 의존성을 공격한다.
- **3국 구조가 도달 범위를 확장한다.** 영국 FCDO는 OFAC이 단독으로 등재하지 않은 영국 등기 위장(XHOST) 및 추가 4인을 포착함으로써, 지정 권한을 관할별로 분산시키는 가치를 보여준다.
- **운영자 단위 "서비스 데스크" 증거가 중요하다.** 2023년 IP 교체 사건(Mishin이 Bolshakov에게 새 IP 발급을 지시하면서 신고자에게는 거짓을 고지)은 인지된 조력과 단순한 수동적 호스팅을 구별하는 세밀한 운영 기록이며, 향후 BPH 사업자 지정의 증거 템플릿으로 *가능성이 매우 높게* 반복될 것이다.
- **9개월 지속압박 체인의 첫 진입점.** 2025년 2월 Zservers 조치, 2025년 7월 Aeza Group 조치, 2025년 11월 [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|Media Land + Hypercore 지정(SB-0319)]]은 의도된 9개월 미-호-영 BPH 제재 트랙을 형성한다. 본 위키 페이지는 이 체인 패턴을 세 개의 분산된 조치가 아니라 하나의 트랙으로서 기록하는 최초의 문헌이다.

## 후속 조치

- *가능성이 매우 높게* 2025년 7월 Aeza Group 지정(트랙 내부의 후속편; 아직 독립적 위키 작전 페이지로 문서화되지 않음).
- 2025-11-19 [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|Media Land + Hypercore 지정(SB-0319)]] — 별개의 BPH 클러스터(Media Land LLC 및 세 자매회사, 그리고 Aeza 리브랜딩 위장 Hypercore Ltd.)를 동일 3국 템플릿에 따라 제재함으로써 9개월 체인을 마감.
- FBI/CISA의 BPH 사업자 위험 지표 권고문 지속(2025년 11월 조치에 병행 지침이 동반됨).

## 한국의 참여

직접적 한국 측 참여는 없다. 한국은 3국 미-호-영 BPH 제재 트랙의 지정 당사자가 아니다. 간접적인 한국 관련성은 다음과 같다.

- 국경 간 랜섬 결제를 처리하는 한국 금융기관 및 가상자산사업자는 Zservers, XHOST Internet Solutions LP, Mishin, Bolshakov에 추적 가능한 자금을 처리할 경우 2차 제재 위험에 노출된다. KoFIU(한국 금융정보분석원)의 일반적 관행은 OFAC SDN 목록(특별지정 국적자)에 정합한다.
- Zservers 인프라를 사용한 LockBit affiliate의 한국 피해 실체는 BPH 공급망 교란으로부터 간접적 편익을 받으나, 본 보도자료는 한국 피해자를 명시하지 않는다.
- 3국 트랙이 향후 라운드에서 한국 또는 일본을 포함한 4국 구조로 확장될 가능성은 roughly even chance에 해당하나, 본 보도자료에는 해당 확장의 공개 신호가 나타나지 않는다.

## 모순 및 미해결 질문

- **영국 보충 수치.** 재무부 본문은 Zservers + Mishin + Bolshakov만 지정하나, 영국 FCDO는 추가로 XHOST Internet Solutions LP 및 4인을 지정하였다. 영국 단독 피지정자와 증거 기반의 일대일 정확한 대응은 OFAC 보도자료에서 확립되지 않는다.
- **캐나다 기관 신원.** "캐나다 사법당국" — RCMP인지, 주(provincial) 기관인지 — 가 특정되지 않는다.
- **Aeza Group 보도 공백.** 중간 단계(2025년 7월) Aeza Group 지정은 [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|2025년 11월 Media Land 조치]]에 언급되나, 본 위키에 아직 독립적 작전 페이지가 부재하다. 이 공백을 메우면 9개월 체인의 문서화가 완결된다.
- **정보 공유 수단.** OFAC, FCDO, DFAT가 동일자 지정을 공조한 구체적 채널은 공개되지 않으며, *가능성이 매우 높게* 파이브 아이즈 사이버 제재 셀이나 확인되지 않는다.
