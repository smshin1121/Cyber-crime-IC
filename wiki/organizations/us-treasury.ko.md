## 현재 상태 (2026-04-10 기준)

**상태:** 활동 중. 재무부 해외자산통제실(OFAC)과 금융범죄단속네트워크(FinCEN)는 모두 재무부 **테러·금융정보국(TFI)** 산하에서 구조적 조직 개편 없이 계속 운영되고 있다. 가장 중대한 최근 변화는 제5순회항소법원의 *Van Loon v. Department of the Treasury* 결정에 따라 2025년 3월 **Tornado Cash가 SDN 목록에서 해제**된 것이다(아래 연혁 및 [주요 작전 및 사건](#key-operations-and-cases) 참조) [3][5][6][7].

**행정명령 체계:** 사이버 관련 OFAC 권한은 **EO 13694 (2015년 4월)** 및 그 개정안인 **EO 13757 (2016년 12월)**, 그리고 IEEPA와 CAATSA에 계속 근거를 두고 있다. 이러한 권한은 Tornado Cash 소송에도 불구하고 **폐지되지 않았으며**, 다만 Tornado Cash의 변경 불가능한 스마트 컨트랙트 지정만 무효화되었다.

**Van Loon 이후 자세:** OFAC는 믹서/텀블러 운영의 배후에 있는 **특정 가능한 개인**(Tornado Cash 공동창업자 Roman Storm 및 Roman Semenov 등 별도의 형사 기소 및 제재 대상으로 남아 있는 자 포함)을 지정할 권한을 *유지할 가능성이 높다*. 다만 외국인의 "재산"으로서 **변경 불가능한 스마트 컨트랙트 주소**를 지정할 수는 없게 되었다. 이는 2015년 이후 OFAC의 사이버 제재 권한에 가해진 *거의 확실히* 가장 중대한 법적 제약이다 [5][6][7].

**FinCEN:** 가상화폐 사업체에 대한 은행보안법(BSA) 집행을 계속하며, Egmont Group(FIU 160개+)의 미국 대표로 남아 있다. 구조적 변화는 보고되지 않았다.

**최근 우선순위 (2025–2026):** 북한/라자루스 그룹 지정; Van Loon 이후 암호화폐 믹서 집행 전략의 재조정(스마트 컨트랙트 주소가 아니라 운영자/개발자로 초점 이동); 랜섬웨어 사건에 대한 EU/영국/캐나다/호주/일본과의 공동 다자 제재 조정 지속.

## 조직 개편 연혁

| 일자 | 사건 | 출처 |
|---|---|---|
| 2015-04 | IEEPA 하에 사이버 제재 권한을 확립하는 **EO 13694** 서명 | [1] |
| 2016-12 | **EO 13757**, EO 13694를 선거 개입 행위자로 확장 | — |
| 2022-05-06 | **Blender.io** — OFAC의 가상화폐 믹서 최초 지정(라자루스 그룹 자금세탁) | — |
| 2022-08-08 | **Tornado Cash** 지정(두 번째 믹서) — SDN 목록 등재 | [1] |
| 2023-08 | Roman Semenov (Tornado Cash 공동창업자) 개별 지정 | [2] |
| 2024-11-26 | 제5순회항소법원 ***Van Loon v. Department of the Treasury*** 판결 — 변경 불가능한 스마트 컨트랙트가 외국인의 "재산"이 아니며 IEEPA 하에 OFAC 지정 대상이 될 수 없다고 판시; 원고 승소 판결을 위해 환송 | [6][7] |
| 2025-03-21 | **OFAC, Tornado Cash를 SDN 목록에서 제외**하고 관련 스마트 컨트랙트 주소를 삭제; 재무부 보도자료 SB-0057 | [5][7] |
| 2025-03-24 | 원고들은 사건이 무용지물(moot)이 아니라고 주장; 영구 금지명령에 관한 소송 계속 | [5] |

> [!warning] 법적 상태 — Tornado Cash 지정 해제 (2026-04-10 확인)
> 2026-04-10 기준으로 Tornado Cash 스마트 컨트랙트 주소는 SDN 목록에서 **계속 해제 상태**이다. 다만 Tornado Cash 창업자 **Roman Storm**과 **Roman Semenov**는 **별도 형사 기소**(SDNY, 자금세탁 공모, 제재 위반, 무허가 자금 송금업 운영) 및 개별 제재 지정 하에 있으며, 이는 *Van Loon* 판결에 영향을 받지 않았다. *Van Loon* 판결은 **코드 및 변경 불가능한 스마트 컨트랙트**에 대한 OFAC의 권한만을 제한하며, 자연인에 대한 권한은 제한하지 않는다.

## 개요

미국 재무부는 두 가지 별개의 도구를 통해 국제 사이버범죄 협력에서 중심적 역할을 수행한다:

1. **해외자산통제실(OFAC)** — 행정명령 13694(2015년 4월 발효, 2016년 12월 EO 13757로 개정) 하에 사이버범죄자, 국가 후원 사이버 행위자, 불법 가상화폐 서비스에 대한 경제 제재를 부과한다.
2. **금융범죄단속네트워크(FinCEN)** — 자금 서비스 사업자(가상화폐 거래소 및 믹서 포함)에 대한 은행보안법 요건을 집행하고, 사이버범죄 관련 자금 흐름에 관한 지침을 발행한다.

재무부 조치는 체포 및 기소에 사이버범죄 인프라의 경제적 배제를 더하여 법집행의 **승수 효과**를 발휘해 왔다. 주요 조치로는 **Tornado Cash** 및 **Blender.io** 믹서 지정(2022)과 북한 라자루스 그룹 및 연관 행위자에 대한 반복적 제재가 있다.

## 권한

### OFAC 사이버 권한

- **행정명령 13694 (2015년 4월)** — "중대한 악의적 사이버 활용 활동"에 대한 제재 권한 부여
- **행정명령 13757 (2016년 12월)** — EO 13694를 선거 개입 사이버 행위자로 확장
- **국제비상경제권한법(IEEPA)** — 근거 법률
- **CAATSA (2017)** — 러시아 특정 사이버 제재 권한 추가

### FinCEN 권한

- **은행보안법 (31 U.S.C. § 5311 이하)**
- **USA PATRIOT Act**
- **2020 자금세탁방지법(AMLA)**
- **FinCEN 2019 지침** — 가상화폐 사업 모델 관련

## 조직 구조

- **OFAC (해외자산통제실):** 제재 지정, 라이선스, 집행. 재무부 테러·금융정보국(TFI) 내.
- **FinCEN (금융범죄단속네트워크):** BSA 집행, 의심거래보고서(SAR) 분석, 금융 정보. TFI 내.
- **OFAC 컴플라이언스·집행국.**
- **재무부 사이버보안·핵심 인프라보호실(OCCIP).**

## 국제공조 역량

- **다자 제재 조정:** 미국 재무부는 효과 극대화를 위해 EU, 영국, 캐나다, 호주, 일본과 사이버 제재를 정기적으로 조율한다. 주요 랜섬웨어 사건 이후의 공동 지정 사례가 있다.
- **FinCEN의 Egmont Group 참여:** FinCEN은 Egmont Group 금융정보부서(FIU) 협의체의 미국 회원으로서, 160개 이상 외국 FIU와의 안전한 정보 공유를 가능하게 한다.
- **제재 기반 억지:** OFAC 지정은 미국 금융 시스템 접근을 차단하고 외국 컴플라이언스를 강제함으로써 지정 대상에게 전 세계적 영향을 부과한다.
- **SDN 목록 공표:** 특별지정국민(SDN) 목록은 전 세계 금융기관이 사실상의 컴플라이언스 기준으로 활용한다.

## 주요 작전 및 사건

### 가상화폐 믹서 지정

- **Blender.io (2022년 5월 6일):** OFAC의 가상화폐 믹서 최초 지정. 북한 라자루스 그룹이 Axie Infinity Ronin Bridge 해킹 수익을 세탁하는 데 이용.
- **Tornado Cash (2022년 8월 8일):** 두 번째이자 더 논쟁적이었던 믹서 지정. OFAC는 2019년 이래 70억 달러 이상의 세탁(라자루스 그룹이 도난한 4억 5,500만 달러+, 2022년 6월 Harmony Bridge 해킹 9,600만 달러, 2022년 8월 Nomad 해킹 780만 달러 포함)을 적시했다.
- **Roman Semenov (Tornado Cash 공동창업자) 지정 (2023년 8월).**

> [!info] 상태(2026-04-10 확인) — Tornado Cash 스마트 컨트랙트 주소 **지정 해제**
> **2025년 3월 21일**, OFAC는 **2024년 11월 26일** *Van Loon v. Department of the Treasury* 제5순회항소법원 판결에 따라 Tornado Cash 제재를 공식적으로 해제하고 관련 주소를 삭제하였다. 동 판결은 **변경 불가능한 스마트 컨트랙트는 IEEPA 하에서 OFAC 지정 대상인 "재산"이 될 수 없다**고 판시하였다. 작용한 표현은 법원이 "의회가 부여한 권한을 초과하였다"였으며, 제5순회법원은 원고 승소 판결을 위해 환송하였다 [6][7]. Tornado Cash 창업자(Semenov, Storm)는 *Van Loon*의 영향을 받지 않는 **별도 형사 기소** 및 **개별 표적 제재** 하에 있다. 전체 타임라인은 위의 [조직 개편 연혁](#history-and-reorganizations) 참조.

### FinCEN 집행

- **Larry Harmon / Helix 믹서 ($6,000만 민사 제재금, 2020)** — BSA 위반으로 가상화폐 믹서에 대한 FinCEN의 첫 조치.
- **랜섬웨어 권고문 (2020년 10월; 2021년 11월 갱신)** — 랜섬웨어 관련 SAR 제출에 관해 금융기관에 권고.

### 랜섬웨어 및 국가 후원 행위자 지정

- 러시아 랜섬웨어 행위자 다수 지정(Evil Corp, Conti 가담자, LockBit 어필리에이트)
- 북한 라자루스 그룹 및 연관 APT 행위자
- 이란 사이버 행위자(IRGC 연계)

## 협력 실적

재무부의 사이버범죄 협력 영향은 *대단히 가능성이 높게* 상당하지만, 전통적 법집행과는 질적으로 다르다. 체포가 아니라 **금융적 배제**를 통해 작동한다. OFAC 지정은 외국 금융기관에 대한 2차 컴플라이언스 압력을 형성하며, 이는 암호화폐 및 전통 자금의 동결에 있어 MLAT 기반 자금 회수보다 *대단히 가능성이 높게* 더 효과적이다.

## 모순 및 미해결 질문

- *Van Loon* 판결과 2025년 Tornado Cash 제재 해제는 (개인·식별 가능한 단체와 달리) **코드** 및 **변경 불가능한 스마트 컨트랙트**에 대한 OFAC 지정의 법적 지속 가능성에 관한 의문을 제기한다.
- OFAC는 사이버범죄 행위자가 대체 경로를 통해 부분적으로 회피할 수 있는 지정의 실효 영향과 억지 가치를 어떻게 균형 잡는가?
- 비미국 가상화폐 사업체에 대한 FinCEN의 BSA 집행 능력은 여전히 논쟁의 대상이다.
- 미국의 일방적 제재와 다자 도구(특히 EU 제재 절차) 간의 긴장은 종종 공동 사이버 집행을 복잡하게 한다.

## 참고문헌

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| [1] | US Treasury Sanctions Notorious Virtual Currency Mixer Tornado Cash | US Treasury | 2022-08-08 | https://home.treasury.gov/news/press-releases/jy0916 |
| [2] | Treasury Designates Roman Semenov, Co-Founder of Sanctioned Virtual Currency Mixer Tornado Cash | US Treasury | 2023-08 | https://home.treasury.gov/news/press-releases/jy1702 |
| [3] | A Legal Whirlwind Settles: Treasury Lifts Sanctions on Tornado Cash | Venable LLP | 2025-04 | https://www.venable.com/insights/publications/2025/04/a-legal-whirlwind-settles-treasury-lifts-sanctions |
| [4] | OFAC Sanctions Virtual Currency Mixer Tornado Cash and Faces Crypto Backlash | Money Laundering Watch | 2022-08 | https://www.moneylaunderingnews.com/2022/08/ofac-sanctions-virtual-currency-mixer-tornado-cash-and-faces-crypto-backlash/ |
| [5] | Treasury Department Delists Tornado Cash Following the Fifth Circuit's Decision | Steptoe LLP | 2025-03 | https://www.steptoe.com/en/news-publications/international-compliance-blog/treasury-department-delists-tornado-cash-following-the-fifth-circuits-decision.html |
| [6] | Fifth Circuit Rejects OFAC Designation of Tornado Cash Immutable Smart Contracts | Money Laundering Watch | 2024-12 | https://www.moneylaunderingnews.com/2024/12/fifth-circuit-rejects-ofac-designation-of-tornado-cash-immutable-smart-contracts/ |
| [7] | Tornado Cash Delisting (press release SB-0057) | US Department of the Treasury | 2025-03-21 | https://home.treasury.gov/news/press-releases/sb0057 |
| [8] | A Whirlwind of Change: The Delisting of Tornado Cash | Paul Hastings LLP | 2025-04 | https://www.paulhastings.com/insights/crypto-policy-tracker/a-whirlwind-of-change-the-delisting-of-tornado-cash |
| [9] | [[2025-08-27_state-gov_us-rok-japan-joint-statement-dprk-it-workers\|미 국무부 — 북한 IT 노동자에 관한 한미일 공동성명 (2025-08-27)]] | U.S. Department of State (Office of the Spokesperson) | 2025-08-27 | https://www.state.gov/releases/office-of-the-spokesperson/2025/08/u-s-rok-japan-joint-statement-on-dprk-information-technology-workers |
