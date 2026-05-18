## 개요

**Operation Endgame(엔드게임 작전)**은 **봇넷 및 랜섬웨어 지원 악성코드 생태계에 대한 사상 최대 규모의 국제 법집행 작전**이다. 2024년 5월에 개시되어 2026년 현재 여전히 진행 중인 본 작전은 [[europol-ec3|Europol(유럽 경찰청)]]과 [[eurojust|Eurojust(유럽사법협력기구)]]가 공조하는 여러 단계로 수행되었으며, 최소 15개국의 법집행기관이 참여하였다.

본 작전의 전략적 혁신은 랜섬웨어 그룹을 직접 추적하는 것이 아니라 랜섬웨어 운영자가 의존하는 초기 접근 인프라인 **드로퍼 및 로더 악성코드**를 표적으로 삼은 데에 있다. 상위 공급망을 무력화함으로써 Operation Endgame은 여러 랜섬웨어 제휴자의 운영 역량을 동시에 약화시켰다.

전 단계에 걸쳐(2024년 5월부터 2025년 5월까지), Operation Endgame은 다음의 결과를 도출하였다.

- **9건 이상의 체포** 및 **20건 이상의 국제 체포영장**
- **400대 이상의 서버** 압수 또는 무력화
- **2,650개 이상의 도메인** 압수 또는 무력화
- **2,120만 유로 이상**의 암호화폐 압수
- 미국 DOJ(미국 법무부)의 **16건의 기소**(DanaBot 운영자)
- EU 최우선 수배자 명단에 **18명의 용의자** 추가

각 단계의 상세 내용은 [[operation-endgame-phase1|Phase 1 (2024년 5월)]] 및 [[operation-endgame-phase2|Phase 2 (2025년 5월)]]을 참조한다.

## Background

### The Dropper/Loader Ecosystem

드로퍼 악성코드("로더" 또는 "초기 접근 도구"라고도 불림)는 랜섬웨어 공격 체인의 핵심 1단계를 구성한다. 이 프로그램들은 보안 조치를 우회하여 침해된 시스템에 추가 악성코드를 은밀히 설치하도록 설계되었으며, 이후 랜섬웨어 운영자에게 판매되거나 활용되는 초기 접근을 제공한다.

초기에 표적이 된 6개 악성코드 패밀리 — **IcedID**, **SystemBC**, **Pikabot**, **Smokeloader**, **Bumblebee**, **Trickbot** — 는 BlackBasta, REvil, Conti와 같은 악명 높은 작전을 포함하여 최소 **15개 랜섬웨어 그룹**과 연결되어 있었다. 드로퍼 생태계는 서비스 모델로 운영된다. 운영자는 감염된 컴퓨터 네트워크를 유지하며, 일반적으로 랜섬웨어 제휴자인 최고 입찰자에게 접근 권한을 판매한다.

### Strategic Rationale

Operation Endgame 이전의 국제 랜섬웨어 집행은 일반적으로 개별 랜섬웨어 그룹 또는 그 운영자를 표적으로 삼았다. Operation Endgame은 **공급망 무력화**라는 전략적 전환을 대표하였다. 즉, 여러 랜섬웨어 그룹이 의존하는 드로퍼 인프라를 테이크다운함으로써 법집행기관은 다수의 범죄 작전을 동시에 약화시킬 수 있었다. 이 접근법은 단일 패밀리 랜섬웨어 표적화보다 집행 노력 단위당 더 큰 승수 효과를 제공한다.

### Investigation Origins

본 수사는 [[europol-ec3|Europol]]과 [[eurojust|Eurojust]]의 공조 하에 **프랑스**, **독일**, **네덜란드**가 주도하여 개시하였다. [[germany-bka|독일 BKA(연방수사청)]] 및 프랑크푸르트 검찰총장실 산하 [[germany-frankfurt-prosecutor|사이버범죄 대응 중앙사무소(ZIT)]]는 특히 압수된 데이터베이스의 디지털 신원을 실제 인물과 매칭하는 작업에서 수사 단계에서 핵심적인 역할을 수행하였으며, 이 포렌식 절차는 수개월이 소요되었다.

## Participating Parties

### Coordinating Bodies

| 기구 | 역할 |
|------|------|
| [[europol-ec3\|Europol EC3]] | 작전 공조; 본부에서 지휘소 운영 |
| [[eurojust\|Eurojust]] | 체포영장 및 압수 명령을 위한 사법 공조 |

### Participating Countries

**핵심 파트너(전 단계):** [[denmark|덴마크]], [[france|프랑스]], [[germany|독일]], [[netherlands|네덜란드]], [[united-kingdom|영국]], [[united-states|미국]]

**Phase 1 지원국:** [[armenia|아르메니아]], [[australia|호주]], [[bulgaria|불가리아]], [[lithuania|리투아니아]], [[portugal|포르투갈]], [[romania|루마니아]], [[switzerland|스위스]], [[ukraine|우크라이나]]

**Phase 2 추가국:** [[canada|캐나다]]

### Participating Agencies

| 국가 | 기관 |
|---------|--------|
| 국제 | [[europol-ec3\|Europol]], [[eurojust\|Eurojust]] |
| 호주 | [[australia-afp\|AFP(호주 연방경찰)]] |
| 아르메니아 | [[armenia-police\|아르메니아 경찰]] |
| 벨기에 | [[belgium-federal-police\|연방경찰]] |
| 불가리아 | [[bulgaria-police\|불가리아 경찰]] |
| 캐나다 | [[canada-rcmp\|RCMP]] |
| 덴마크 | [[denmark-police\|덴마크 경찰]] |
| 프랑스 | [[france-national-police\|국립경찰]], [[france-gendarmerie\|국가헌병대]], [[france-junalco\|JUNALCO]] |
| 독일 | [[germany-bka\|BKA]], [[germany-lka\|LKA]], [[germany-frankfurt-prosecutor\|프랑크푸르트 ZIT]] |
| 리투아니아 | [[lithuania-police\|리투아니아 경찰]] |
| 네덜란드 | [[netherlands-politie\|Politie]] |
| 포르투갈 | [[portugal-police\|포르투갈 경찰]] |
| 루마니아 | [[romania-police\|루마니아 경찰]] |
| 스위스 | [[switzerland-fedpol\|Fedpol]] |
| 우크라이나 | [[ukraine-police\|우크라이나 경찰]] |
| 영국 | [[uk-nca\|NCA(영국 국가범죄청)]] |
| 미국 | [[fbi-cyber-division\|FBI]], [[us-doj\|DOJ]], [[us-secret-service\|비밀경호국]], [[us-dcis\|DCIS]] |

### Private Sector Partners

다수의 민간 사이버보안 기업들이 위협 인텔리전스 및 인프라 식별을 포함한 기술 지원을 제공하였다. Microsoft는 Phase 2와 동시에 진행된 Lumma Stealer 무력화에 참여하여 2025년 3월부터 5월 사이에 394,000대의 감염된 Windows 머신을 식별하였다.

## Legal Framework

본 작전에는 최소 15개국의 법집행기관과 사법기관이 참여하였다. 법적 프레임워크는 다층적 도구 집합에 의존하였다.

- **[[budapest-convention|부다페스트 사이버범죄 협약]]** — 참여국 간 국경 간 사이버범죄 공조를 위한 주요 조약 프레임워크를 제공하며, 모든 참여국은 가입국이거나 공조 협정을 보유함
- **[[joint-investigation-team|공동수사팀(JIT)]]** — 다중 관할 수사 및 증거 공유를 가능하게 하기 위해 [[eurojust|Eurojust]]를 통해 정식 JIT가 설치됨
- **유럽 체포영장** — Phase 1에서 독일 당국이 발부한 10건의 체포영장 및 Phase 2의 20건의 국제 체포영장에 사용됨
- **국내 형사법** — 아르메니아 및 우크라이나에서의 체포는 국제 공조와 함께 국내 법적 권한에 따라 집행됨
- **미국 연방법** — DanaBot 운영자에 대한 16건의 기소장은 미국 컴퓨터 사기 및 관련 법령에 따라 제출됨

> [!info] Legal-basis note
> 국경 간 서버 압수에 사용된 구체적 조약 조항(예: 서비스 제공자와의 직접 협력에 관한 [[second-additional-protocol|제2추가의정서]] 조항이 사용되었는지 여부)은 공식 사법 자료의 확인이 필요하다.

## Operational Timeline

### Phase 1: 드로퍼 테이크다운 (2024년 5월)

| 일자 | 사건 |
|------|-------|
| 2024년 이전 | 다국적 수사 단계; 운영자 식별을 위한 디지털 포렌식 |
| 2024-05-27 | 작전 개시 |
| 2024-05-27 ~ 2024-05-29 | 10개국에서 100대 이상의 서버 테이크다운; 2,000개 이상의 도메인 압수; 4건의 체포(아르메니아 1건, 우크라이나 3건); 16건의 위치 수색; 99개의 암호화폐 지갑 차단 |
| 2024-05-30 | Europol의 공개 발표; 8명의 독일인 용의자가 EU 최우선 수배자 명단에 추가 |

전체 세부정보는 [[operation-endgame-phase1]]을 참조한다.

### Smokeloader 고객 후속 조치 (2025년 4월)

| 일자 | 사건 |
|------|-------|
| 2024-05 ~ 2025-04 | BKA 및 파트너들이 압수된 Smokeloader 고객 데이터베이스를 분석하여 온라인 별명을 실제 신원과 연결 |
| 2025-04-09 | Europol이 후속 조치 발표: "Superstar"라는 행위자가 운영하는 Smokeloader 페이-퍼-인스톨 봇넷의 5명의 고객이 구금되거나 "knock-and-talk" 인터뷰의 대상이 됨 |
| 2025-04 | Smokeloader 인프라 관련 추가 서버 테이크다운 |

이 단계는 **공급자**(인프라 운영자)에서 **수요자**(범죄 목적으로 봇넷 접근을 구매한 고객)를 표적으로 한 전략적 전환을 나타냈다. 일부 구금된 용의자들은 법집행기관에 협조하여 자신의 디지털 장치 검사를 허용하였다.

### Phase 2: 랜섬웨어 킬 체인 무력화 (2025년 5월)

| 일자 | 사건 |
|------|-------|
| 2025-05-19 | Phase 2 작전 개시 |
| 2025-05-19 ~ 2025-05-22 | 300대의 서버 테이크다운; 650개의 도메인 무력화; 350만 유로 암호화폐 압수 |
| 2025-05-23 | Europol 및 Eurojust의 공개 발표; DOJ가 DanaBot 운영자에 대한 16건의 기소장 봉인 해제; 20건의 국제 체포영장 발부; 18명의 용의자가 EU 최우선 수배자 명단에 추가 |

Phase 2는 표적 집합을 확장하여 **Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, Warmcookie**를 포함시켰다. 미국 DOJ는 러시아 노보시비르스크 출신의 Aleksandr Stepanov(39세) 및 Artem Kalinkin(34세)을 포함한 16명의 러시아 국적자를 300,000대 이상의 컴퓨터를 감염시키고 5,000만 달러 이상의 추정 손해를 야기한 DanaBot 악성코드 네트워크 운영 혐의로 기소하였다.

전체 세부정보는 [[operation-endgame-phase2]]를 참조한다.

## Results and Impact

### Cumulative Results Across All Phases

| 항목 | Phase 1 (2024년 5월) | Smokeloader 후속 조치 (2025년 4월) | Phase 2 (2025년 5월) | 누적 |
|--------|-------------------|----------------------------------|-------------------|------------|
| 체포/구금 | 4 | 5 | 0 | 9 |
| 압수/테이크다운된 서버 | 100+ | 추가분 | 300 | 400+ |
| 압수/무력화된 도메인 | 2,000+ | — | 650 | 2,650+ |
| 압수된 암호화폐 | 6,900만 유로 차단(용의자 자산) | — | 350만 유로 | 2,120만 유로+(집행 총액) |
| 체포영장 | 10 | — | 20 | 30+ |
| EU 최우선 수배자 | 8 | — | 18 | 26 |
| 기소 | — | — | 16 (DanaBot) | 16 |
| 표적 악성코드 패밀리 | 6 | 1 | 7 | 13 |

### Malware Families Disrupted

| 악성코드 | 유형 | 표적이 된 단계 | 랜섬웨어와의 연결 |
|---------|------|----------------|--------------------------|
| IcedID | 뱅킹 트로이목마 / 로더 | Phase 1 | 랜섬웨어 그룹의 초기 접근 |
| SystemBC | 프록시 / 백도어 | Phase 1 | 랜섬웨어 C2 통신 |
| Pikabot | 로더 | Phase 1 | Qakbot 후속; 초기 접근 |
| Smokeloader | 페이-퍼-인스톨 로더 | Phase 1 + 후속 조치 | 다양한 페이로드의 배포 플랫폼 |
| Bumblebee | 로더 | Phase 1 + Phase 2 | Conti/BlackBasta 제휴자의 초기 접근 |
| Trickbot | 뱅킹 트로이목마 / 로더 | Phase 1 + Phase 2 | 초기 접근; Conti 생태계 연결 |
| DanaBot | 뱅킹 트로이목마 / 봇넷 | Phase 2 | 자격증명 탈취; 랜섬웨어 배포 |
| Qakbot | 뱅킹 트로이목마 / 로더 | Phase 2 | 초기 접근; 운영자 기소됨 |
| Lactrodectus | 로더 | Phase 2 | IcedID 후속 |
| Hijackloader | 로더 | Phase 2 | 다단계 페이로드 전달 |
| Warmcookie | 로더 | Phase 2 | 피싱을 통한 초기 접근 |
| Rhadamanthys | 정보 탈취 | Phase 2 | 랜섬웨어를 가능하게 하는 자격증명 탈취 |

### Financial Impact

Phase 1에서 식별된 주요 용의자 중 한 명은 랜섬웨어 배포에 사용된 범죄 인프라 임대로부터 최소 **6,900만 유로의 암호화폐**를 벌어들였다. 6,900만 유로의 자산 동결이 확보되었으며, 총 7,000만 유로 이상의 99개 암호화폐 지갑이 다양한 암호화폐 거래소에서 차단되었다.

모든 집행 조치에 걸쳐 총 압수액은 **2,120만 유로**(약 2,400만 달러)를 초과하였다. 미국 DOJ는 또한 Qakbot 운영자 Gallyamov로부터 압수된 디지털 자산 2,400만 달러(참조: [[qakbot-gallyamov-indictment]])와 추가 비트코인 및 USDT 토큰 약 400만 달러에 대한 몰수 청구를 제기하였다.

### Impact on Ransomware Ecosystem

본 작전은 랜섬웨어 생태계에 상당한 무력화 효과를 미쳤으나, 정확한 영향을 정량화하기는 여전히 어렵다.

- 다수의 랜섬웨어 제휴자가 동시에 주요 초기 접근 채널을 상실함
- "페이-퍼-인스톨" 비즈니스 모델이 무력화되어 범죄 행위자들이 인프라를 재구축할 수밖에 없게 됨
- 압수된 고객 데이터베이스가 법집행기관이 수요자 측 행위자를 추적할 수 있게 하여, 향후 봇넷 서비스 구매에 대한 위축 효과를 창출함
- 그러나 일부 악성코드 패밀리(특히 DanaBot)는 테이크다운 이후 인프라를 재구성하는 징후를 보여, 지속적인 집행 압박이 필요함을 시사함

## Cooperation Mechanisms Used

### Europol Command Post

Europol은 Phase 1 및 Phase 2의 작전 주간 동안 헤이그 본부에서 현장 지휘소를 운영하였다. Phase 1 동안 덴마크, 프랑스, 독일, 네덜란드, 미국에서 20명 이상의 관계자가 실시간 공조를 위해 현장에 있었다. 이를 통해 다음이 가능해졌다.

- 여러 시간대에 걸친 동기화된 서버 테이크다운
- 작전일 중 예기치 못한 상황 발생 시 신속한 의사결정
- 참여 기관 간 실시간 정보 공유

### Eurojust Judicial Coordination

[[eurojust|Eurojust]]는 다음을 위한 사법 공조를 제공하였다.

- 다중 관할 체포영장(Phase 1에서 10건, Phase 2에서 20건)
- 국경 간 증거 보존 및 이전 명령
- 다양한 법체계 간 압수 명령의 공조
- 참여국 간 형사사법공조(MLA) 촉진

### Joint Investigation Teams

다중 관할 수사를 가능하게 하기 위해 정식 [[joint-investigation-team|공동수사팀(JIT)]]가 설치되었다. Eurojust가 촉진한 JIT 프레임워크는 다양한 국가의 수사관들이 통합된 법적 프레임워크 내에서 증거를 공유하고 행동을 공조할 수 있게 하여, 정식 [[mlat-process|형사사법공조조약(MLAT) 요청]]에 일반적으로 수반되는 지연을 회피할 수 있었다.

### Database Exploitation

특히 주목할 만한 메커니즘은 후속 집행을 위한 **압수 데이터베이스의 활용**이었다. Phase 1 동안 압수된 Smokeloader 고객 데이터베이스는 온라인 별명과 사용자명을 실제 신원과 매칭하는 데 수개월을 소요한 [[germany-bka|BKA]] 수사관에 의해 체계적으로 분석되었다. 이 정보는 이후 여러 국가의 법집행 파트너들과 공유되어 2025년 4월 수요자 측 집행 물결을 가능하게 하였다.

### EU Most Wanted List

Europol의 **EU 최우선 수배자** 명단에 용의자를 추가한 것(Phase 1에서 8명, Phase 2에서 18명)은 공공 인식 메커니즘이자 국제 도주자 추적 도구로 작용하여, 용의자가 이동할 때 식별 및 체포 가능성을 높였다.

## Challenges and Friction Points

### Jurisdictional Complexity

본 작전은 서로 다른 법체계, 절차적 요건, 증거 기준을 가진 최소 15개국 간의 공조를 필요로 하였다. 동기화된 작전일은 모든 참여자가 각자의 법적 프레임워크 내에서 할당된 임무를 수행할 수 있도록 면밀한 사전 계획이 필요하였다.

### Russian-Based Suspects

미국 DOJ에 의해 기소된 16명의 DanaBot 운영자를 포함하여 식별된 다수의 용의자는 러시아에 거주한다. 현재의 지정학적 상황과 러시아와의 범죄인 인도 공조 부재를 고려할 때, 이들 용의자는 사실상 법집행 범위 밖에 있다. 국제 체포영장 및 EU 최우선 수배자 등재는 용의자가 공조 관할로 이동할 경우 체포를 위한 법적 프레임워크를 창출하지만, 러시아 내 직접 집행은 현재의 공조 채널의 실질적 범위 밖에 있다.

### Infrastructure Reconstitution

일부 표적이 된 악성코드 패밀리는 테이크다운 이후 작전을 재구성하는 징후를 보였다. 특히 DanaBot은 새로운 인프라로 재출현하였으며, 이는 운영자 체포 없이 인프라 테이크다운만으로는 일시적인 무력화만 제공한다는 점을 시사한다. 이는 일회성 조치가 아닌 지속적인 다단계 캠페인의 필요성을 강조한다.

### Demand-Side Enforcement Scale

Smokeloader 고객 후속 조치(5건의 구금)는 수요자 측 집행의 실행 가능성을 보여주었으나, 봇넷 고객 기반의 규모는 모든 사용자를 추적할 수 있는 법집행 역량을 초과한다. 우선순위 설정 및 억지 효과가 핵심 고려 사항이다.

## Lessons Learned

1. **승수 효과로서의 공급망 무력화:** 드로퍼/로더 인프라를 표적으로 삼는 것은 여러 랜섬웨어 작전을 동시에 무력화한다. 이러한 상류 접근법은 개별 랜섬웨어 그룹을 표적으로 하는 것보다 집행 노력 단위당 더 큰 영향을 제공한다.

2. **다단계 지속 캠페인:** Phase 1(2024년 5월)에서 Smokeloader 후속 조치(2025년 4월), Phase 2(2025년 5월)로의 진행은 지속적인 캠페인이 범죄 생태계에 압력을 누적적으로 가한다는 점을 보여준다. 범죄 행위자들은 어떤 인프라가 다음에 표적이 될 것인지에 대한 지속적인 불확실성에 직면한다.

3. **수요자 측 집행:** Smokeloader 고객 체포는 공급자 측(인프라 운영자)에서 수요자 측(서비스 구매자) 집행으로의 전략적 확장을 나타냈다. 이러한 "전체 생태계" 접근법은 봇넷 서비스 구매가 실제 체포 위험을 수반한다는 억지 메시지를 전달한다.

4. **데이터베이스 인텔리전스 활용:** 압수된 인프라 데이터베이스는 진행 중인 사건의 증거에 그치지 않고, 완전히 새로운 수사 라인을 가능하게 하는 인텔리전스 자산이다. Smokeloader 고객의 익명화를 해제하기 위한 수개월간의 BKA의 노력은 인프라 압수의 장기적인 수사 가치를 보여준다.

5. **실시간 공조 인프라:** 여러 국가에서 20명 이상의 관계자가 참여하는 Europol 지휘소는 인프라 테이크다운에 필요한 종류의 동기화된 다중 시간대 조치를 가능하게 한다. 이러한 제도적 역량은 이러한 규모의 작전에 필수적이다.

## Follow-Up Actions

- **진행 중인 수사:** Europol은 Operation Endgame이 종료되지 않았으며 추가 집행 단계가 계획되어 있다고 명시적으로 발표하였다.
- **도주자 추적:** 30건 이상의 국제 체포영장 및 26명의 EU 최우선 수배자 등재는 용의자들이 공조 관할로 이동할 때 향후 체포를 위한 지속적인 법적 프레임워크를 창출한다.
- **DanaBot 재구성 모니터링:** Phase 2 테이크다운 이후 새로운 인프라로 재출현한 DanaBot은 지속적인 모니터링 및 잠재적인 추가 집행 조치를 필요로 한다.
- **관련 절차:** [[qakbot-gallyamov-indictment|Qakbot/Gallyamov 기소]] 및 관련 자산 몰수 절차가 미국 법원에서 진행 중이다.

## Korean Involvement (한국의 참여)

2026년 4월 현재 Operation Endgame의 어떤 단계에도 한국의 직접적인 참여는 확인되지 않았다. 한국은 Phase 1 또는 Phase 2의 참여국에 포함되지 않았다.

그러나 Operation Endgame은 다음과 같은 측면에서 한국의 사이버보안 이익과 관련성을 가진다.

- **랜섬웨어 영향:** Operation Endgame이 표적으로 한 드로퍼 악성코드 패밀리는 전 세계적으로 사용되어 왔으며, 한국 조직들도 이러한 초기 접근 채널을 통해 배포된 랜섬웨어의 피해자가 되어왔다
- **공조 모델:** 본 작전은 한국이 유럽 법집행기관과의 확대되는 협력을 통해 참여할 수 있는 다국적, Europol 공조 집행 조치의 모델을 제공한다(사이버범죄 국제공조 모델로서의 참고 가치)
- **부다페스트 협약 참여:** 한국이 [[budapest-convention|부다페스트 협약]] 프레임워크와 지속적으로 관여함에 따라, Endgame과 같은 작전의 향후 단계에 참여하는 것은 국제 사이버범죄 집행에서 한국의 역할을 강화할 수 있다

## Contradictions & Open Questions

1. **체포 수 불일치:** 일부 자료는 Phase 1에서 4건의 체포를 보고하는 반면 독일 BMI는 4건의 "일시적 구금"을 보고한다. 정식 체포와 일시적 구금의 구분은 관할에 따른 다양한 법적 프레임워크를 반영할 수 있다.

2. **재정 수치:** 6,900만 유로의 용의자 암호화폐 보유고(Phase 1), 차단된 7,000만 유로의 암호화폐 지갑, 누적 집행 압수 총액 2,120만 유로 간의 관계는 완전히 명확하지 않다. 6,900만/7,000만 유로 수치는 동결 명령의 대상이 되는 식별된 자산을 나타낼 수 있는 반면, 2,120만 유로는 실제로 압수/몰수된 자금을 나타낸다.

3. **DanaBot 출처 검증:** 16건의 DanaBot 기소 및 300,000건의 감염 수치는 주로 언론 보도(공개 자료)에서 비롯된 것이다. 공식 DOJ 기소장 본문이 명확한 확인을 제공할 것이다.

4. **재구성 비율:** 표적이 된 악성코드 패밀리들이 각 단계 이후 얼마나 빠르고 효과적으로 재구성되었는가? DanaBot은 재출현한 것으로 보고되었으나, 13개 표적 패밀리 전반에 걸친 재구성에 대한 체계적 평가는 부족하다.

5. **측정 가능한 랜섬웨어 영향:** 각 단계 이후 전 세계 랜섬웨어 배포율에 대한 정량화 가능한 효과는 무엇이었는가? 체계적 평가는 공개적으로 발표되지 않았다.

6. **Phase 1 서버 위치:** 서버는 불가리아, 캐나다, 독일, 리투아니아, 네덜란드, 루마니아, 스위스, 영국, 미국, 우크라이나에서 압수되었으나, 국가별 분포는 상세히 명시되지 않았다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2024-05-30: 봇넷에 대한 사상 최대 규모의 작전이 드로퍼 악성코드 생태계를 타격 — Operation Endgame.
- FBI, 2024-05-29: Operation Endgame: 사이버 범죄자 네트워크에 대한 공조 글로벌 법집행 조치.
- 독일 BMI, 2024-05-30: 사이버 범죄에 대한 전 세계적 수사가 성공으로 결실.
- Europol, 2025-04-09: Operation Endgame 후속 조치로 5건의 구금 및 심문, 서버 테이크다운 진행.
- Europol, 2025-05-23: Operation Endgame 재도전: 랜섬웨어 킬 체인이 그 근원에서 무력화됨.
- Europol, 2026-04-17: Operation Endgame — 공식 페이지.
- KrebsOnSecurity, 2024-05-30: 'Operation Endgame', 악성코드 배포 플랫폼 타격.
- The Hacker News, 2025-05-23: The Hacker News: 미국이 DanaBot 악성코드 네트워크를 해체(Operation Endgame Phase 2).

## Evidence and Attribution Notes

- Operation Endgame Phase 1은 봇넷에 대한 사상 최대 규모의 국제 조치로서 2024년 5월 27–29일에 수행됨
- 표적이 된 드로퍼 악성코드 패밀리: IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot
- 4건의 체포(아르메니아 1건, 우크라이나 3건), 10개국에서 100대 이상의 서버 테이크다운, 2,000개 이상의 도메인 압수
- 핵심 용의자는 범죄 인프라 임대로부터 최소 6,900만 유로의 암호화폐를 축적함
- 악성코드 드로퍼는 BlackBasta, REvil, Conti를 포함한 최소 15개 랜섬웨어 그룹과 연결됨
- 2024년 5월 27일과 29일 사이에 **Operation Endgame** — 봇넷에 대한 사상 최대 규모의 국제 조치 — 는 IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot을 포함한 드로퍼 악성코드 패밀리를 표적으로 함.
- 덴마크, 프랑스, 독일, 미국의 20명 이상의 관계자로 구성된 지휘소를 통해 Europol 본부에서 공조된 본 작전은 4건의 체포, 10개국에 걸친 100대 이상의 서버 테이크다운, 2,000개 이상의 도메인 압수로 이어짐.
- 이러한 악성코드 드로퍼는 BlackBasta, REvil, Conti를 포함한 최소 15개 랜섬웨어 그룹과 연결된 초기 접근 벡터의 역할을 함.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- FBI, 2024-05-29: 우크라이나, 포르투갈, 루마니아, 리투아니아, 불가리아, 스위스의 법집행기관은 용의자 체포 또는 면담, 수색 실시, 서버 압수 또는 테이크다운을 위한 경찰 조치를 지원함.
- FBI, 2024-05-29: 2024년 5월 28일부터, 이러한 종류의 첫 공조 국제 작전에 12개국이 참여하여 다수의 악성코드 변종을 무력화하기 위해 수색을 실시하고, 대상자를 심문 또는 체포하며, 100대 이상의 서버를 테이크다운 또는 무력화함.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인별 후속 조치가 아닌 랜섬웨어를 가능하게 하는 드로퍼/로더 악성코드 생태계(IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot, DanaBot, Qakbot, Bumblebee, Lactrodectus, Hijackloader, Warmcookie, Rhadamanthys)에 대한 테이크다운을 기술하므로 정식 작전으로 보존된다. 본 기록은 주된 책임을 Europol EC3에, 공조를 Europol EC3에 귀속시키며, 참여 또는 영향을 받은 관할로는 호주, 아르메니아, 불가리아, 캐나다, 덴마크, 프랑스, 독일, 리투아니아, 네덜란드, 포르투갈, 루마니아, 스위스, 우크라이나, 영국, 미국을 기록한다.

공조 모델은 명명된 기관 및 파트너를 통해 문서화된다. Europol EC3, Eurojust, Australia AFP, Armenia Police, Belgium Federal Police, Bulgaria Police, Canada RCMP, Denmark Police, FBI Cyber Division, France Gendarmerie. 메커니즘으로는 Europol JIT 및 공동수사팀(JIT). 법적 근거는 부다페스트 협약. 집행 자세는 체포, 압수, 테이크다운, 자산 동결, 기소.

정식 기록에 포착된 작전 결과: 9건의 체포; 16건의 기소; 400대의 서버 압수; 2,650개 도메인 압수; 암호화폐/자산 결과는 2,120만 유로 이상(전 단계 누적)으로 기록; 20건의 국제 체포영장 발부; 18명의 용의자가 EU 최우선 수배자 명단에 추가; 10건의 국제 체포영장(Phase 1).

정식 자료 집합은 9건의 참조 자료를 포함한다: 2024 05 30 Europol Operation Endgame Botnet Takedown, 2024 05 29 FBI Gov Operation Endgame Coordinated Worldwide Law Enforcement Action Against Network O, 2024 05 30 Bmi Bund De Worldwide Investigation Against Cyber Crime Crowned By Success, 2025 04 09 Europol Europa Eu Operation Endgame Follow Up Leads To Five Detentions And Interrogations As Well, 2025 05 23 Europol Operation Endgame Phase2, 2026 04 17 Europol Europa Eu Operation Endgame Official Page, 추가 3건.
자료 하한선은 정식 작전에 부합하지만, 자료의 광범위함만으로는 모든 하방 체포 또는 선고가 본 작전의 일부임을 증명하지 못한다. 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
현재 본 페이지에는 frontmatter의 missing-field 플래그가 없다.
데이터셋 활용 측면에서, 본 페이지는 작전 수준의 통합 기준점으로 다루어져야 한다. 국가, 기관, 메커니즘, 결과 필드는 공조 집행 조치 전체를 기술한다. 이후의 기소, 답변, 선고, 범죄인 인도, 또는 몰수 조치는 자료가 명시적으로 새로운 다국적 작전으로 제시하지 않는 한 관련 사건 또는 흡수된 후속 기록으로 첨부되어야 한다.
자료 기록이 보다 광범위한 배경, 반복된 통신사 재게재, 또는 주제 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 그 참여 당국, 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과에 직접 연결된 사실에 우선순위를 부여한다. 주변적인 자료 제목은 독립적인 분류 또는 결과 증거로 다루어지지 않는다.
이는 정식 기록이 분석적으로 한정되고 재현 가능한 상태를 유지하도록 한다.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 봇넷에 대한 사상 최대 규모의 작전이 드로퍼 악성코드 생태계를 타격 — Operation Endgame | Europol | 2024-05-30 | https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem |
| [2] | Operation Endgame: 사이버 범죄자 네트워크에 대한 공조 글로벌 법집행 조치 | FBI | 2024-05-29 | https://www.fbi.gov/news/press-releases/operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-of-cybercriminals |
| [3] | 사이버 범죄에 대한 전 세계적 수사가 성공으로 결실 | German BMI | 2024-05-30 | https://www.bmi.bund.de/SharedDocs/kurzmeldungen/EN/2024/05/endgame.html |
| [4] | Operation Endgame 후속 조치로 5건의 구금 및 심문, 서버 테이크다운 진행 | Europol | 2025-04-09 | https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-follow-leads-to-five-detentions-and-interrogations-well-server-takedowns |
| [5] | Operation Endgame 재도전: 랜섬웨어 킬 체인이 그 근원에서 무력화됨 | Europol | 2025-05-23 | https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-strikes-again-ransomware-kill-chain-broken-its-source |
| [6] | Operation Endgame — 공식 페이지 | Europol | 2026-04-17 | https://www.europol.europa.eu/operations-services-and-innovation/operations/operation-endgame |
| [7] | 'Operation Endgame', 악성코드 배포 플랫폼 타격 | KrebsOnSecurity | 2024-05-30 | https://krebsonsecurity.com/2024/05/operation-endgame-hits-malware-delivery-platforms/ |
| [8] | The Hacker News: 미국이 DanaBot 악성코드 네트워크를 해체(Operation Endgame Phase 2) | The Hacker News | 2025-05-23 | https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html |
| [9] | DanaBot 봇넷 무력화, QakBot 리더 기소 | Help Net Security | 2025-05-23 | https://www.helpnetsecurity.com/2025/05/23/operation-endgame-danabot-botnet-disrupted-qakbot-leader-indicted/ |
