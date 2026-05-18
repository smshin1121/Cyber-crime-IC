## 개요

Operation LadyBird는 **Emotet 봇넷(Emotet(악성코드/봇넷))** — [[europol-ec3|Europol(유럽 경찰청)]]이 "세계에서 가장 위험한 악성코드"라고 묘사한 — 을 **2021년 1월 27일** 와해시킨 다국적 법집행 작전이다. 본 작전은 [[europol-ec3|Europol EC3]]와 [[eurojust|Eurojust(유럽사법협력기구)]]가 조정하였으며, [[netherlands-politie|네덜란드 국가경찰(NHTCU)]]과 독일의 BKA(독일 연방수사청, Bundeskriminalamt)가 주된 작전 주도 기관으로 기능하였다.

**8개 국가** — [[netherlands|네덜란드]], [[germany|독일]], [[united-states|미국]], [[united-kingdom|영국]], [[france|프랑스]], [[ukraine|우크라이나]], [[canada|캐나다]], [[lithuania|리투아니아]] — 의 법집행 기관들은 약 **700개의 명령통제(C2) 서버**와 **2,000개 이상의 도메인**을 동시에 장악하고, 감염된 머신들을 법집행 통제 인프라로 우회시켰다.

본 작전은 공공 기록상 가장 기술적으로 혁신적인 봇넷 테이크다운 중 하나이다: 단순히 인프라를 차단하는 대신, 법집행 기관은 Emotet 자체의 업데이트 메커니즘을 활용하여 전 세계 감염 머신에 제거 모듈을 배포하였고, 이는 **2021년 4월 25일** 활성화되어 악성코드를 제거하였다. 그러나 결과는 **부분 성공**으로 평가되는데, Emotet이 약 10개월 후인 2021년 11월에 TrickBot 인프라를 활용하여 재구축되어 다시 출현하였기 때문이다.

## 배경

### Emotet의 진화

Emotet은 **2014년** 금융기관을 표적으로 한 뱅킹 트로이로 처음 등장하였다. 2017년경에는 정교한 **악성코드형 서비스(Malware-as-a-Service, MaaS) 플랫폼** — 침해된 시스템에 초기 접근을 제공하고 이를 다른 사이버범죄 집단에 판매하는 "로더(loader)" — 로 진화하였다. 주요 특징:

- **모듈식 아키텍처:** 뱅킹 트로이(TrickBot), 랜섬웨어(Ryuk, Conti), 정보 탈취 도구 등 추가 페이로드 배포 가능
- **스팸 인프라:** 세계 최대 규모의 스팸 봇넷 중 하나를 운영하며 매일 수백만 건의 악성 첨부 피싱 이메일 발송
- **다형성 코드:** 다운로드마다 코드를 변경하여 백신 탐지 회피
- **회복력 있는 C2 네트워크:** 중복 통신 채널을 가진 다수 국가 소재 수백 대의 서버

### 위협의 규모

2020년까지 Emotet은 **전 세계 약 160만 대의 컴퓨터**를 감염시킨 것으로 추정된다(DOJ(미국 법무부) 추정으로 2020년 4월부터 2021년 1월 사이만 해도). 본 봇넷은 전 세계에서 가장 피해 규모가 큰 일부 랜섬웨어 공격의 진입 벡터로 기능하였으며, 총 피해액은 수억 달러로 추정된다. Europol(유럽 경찰청)은 이를 사이버범죄자들에게 "문을 열어주는 도구(door opener)"로 묘사하였다 — 초기 Emotet 감염은 제휴 범죄 집단에 의한 랜섬웨어 또는 뱅킹 트로이 배포로 이어졌다.

### 수사의 기원

Emotet 인프라에 대한 수사는 약 **2019년** 시작되었으며, 네덜란드와 독일 당국이 본 봇넷의 전 세계적으로 분산된 C2 아키텍처 매핑을 주도하였다. 본 수사는 [[eurojust|Eurojust(유럽사법협력기구)]]가 지원한 [[joint-investigation-team|공동수사팀(JIT)]]을 통해 수행되었다.

## 참여 당사자

### 주도 기관

| 국가 | 기관 | 역할 |
|---------|--------|------|
| [[netherlands]] | [[netherlands-politie]] (NHTCU) | 인프라 인수; 업데이트 모듈 배포; 탈취된 자격 증명 복구 |
| [[germany]] | BKA(독일 연방수사청, Bundeskriminalamt) | 공동 주도; 독일 내 17대 C2 서버 압수; 검찰과 조정 |

### 조정 기관

| 조직 | 역할 |
|---|---|
| [[europol-ec3]] | 작전 조정, 정보 교차매칭, 조정 센터 |
| [[eurojust]] | 사법적 조정, JIT 지원 |

### 지원 기관

| 국가 | 기관 | 역할 |
|---------|--------|------|
| [[united-states]] | [[fbi-cyber-division]] / 미국 DOJ MDNC | 법률 지원; 미국 영토 내 인프라 압수 |
| [[united-kingdom]] | 영국 국가범죄수사국(NCA) | C2 서버 압수; 약 700대 서버 오프라인 보고 |
| [[france]] | 프랑스 국가경찰(Police Nationale) | 프랑스 관할권 내 인프라 압수 |
| [[ukraine]] | 우크라이나 사이버경찰국 | 하르키우(Kharkiv) 내 부동산 압수수색; 2명 피의자 체포 |
| [[canada]] | 캐나다 왕립기마경찰(RCMP) | 인프라 압수 지원 |
| [[lithuania]] | 리투아니아 형사경찰국 | 인프라 압수 지원 |

## 법적 근거

본 작전은 다수의 법적 협력 수단에 의존하였다:

- **[[budapest-convention|부다페스트 협약]]** (제29-35조): 당사국 간 국경 간 증거 보전 및 제공 명령의 기본 법적 근거 제공
- **[[mutual-legal-assistance|형사사법공조조약(MLAT)]]**: 양자 MLAT를 통해 관할권 간 증거 공유 및 인프라 압수 가능
- **[[joint-investigation-team|공동수사팀(JIT)]]**: 네덜란드, 독일 및 기타 EU 참여국 간 실시간 증거 공유를 위해 [[eurojust|Eurojust]]를 통해 JIT 설치
- **EU 유럽수사명령(EIO)**: EU 내부 사법 협력에 활용

우크라이나 측 체포는 우크라이나 국내 형사절차에 따라 수행되었으며, 증거는 [[mutual-legal-assistance|MLAT]] 채널을 통해 공유되었다.

## 작전 타임라인

| 일자 | 사건 |
|------|-------|
| 약 2019년 | 수사 개시; 네덜란드 및 독일 당국이 Emotet C2 인프라 매핑 시작 |
| 2020년 | [[eurojust]]를 통한 JIT 설치; 다국가 인프라 식별 가속화 |
| 2021년 1월 26일 | 8개국 전반에 걸친 협력 행동의 날 준비 완료 |
| **2021년 1월 27일** | **행동의 날**: 모든 참여국에 걸쳐 약 700대 C2 서버와 2,000개 이상 도메인 동시 압수 |
| 2021년 1월 27일 | [[netherlands-politie]]가 Emotet 자체 인프라를 통해 업데이트 모듈 배포; 감염 머신은 법집행 통제 서버로 우회 |
| 2021년 1월 27일 | 우크라이나 사이버경찰이 하르키우 내 부동산 압수수색; 2명 피의자 체포 |
| 2021년 1월 27일 | [[europol-ec3]]와 [[eurojust]]가 작전을 공개 발표 |
| 2021년 1월 27일 | DOJ(미국 법무부)가 Emotet 봇넷 와해 발표 |
| 2021년 2월 17일 | 네덜란드 경찰이 침해된 이메일 주소 430만 건 복구 발표; 피해자가 노출 여부를 확인할 수 있는 온라인 도구 출시 |
| **2021년 4월 25일** | 법집행 배포 제거 모듈 활성화; Emotet이 전 세계 감염 머신에서 자가 삭제 |
| 2021년 11월 | Emotet 봇넷이 Conti 랜섬웨어 그룹에 의해 TrickBot 인프라를 활용해 재구축되어 재출현 |

## 결과 및 영향

### 즉각적 결과

| 지표 | 값 | 출처 |
|--------|-------|--------|
| 압수/무력화된 C2 서버 | 약 700대 | NCA / Europol |
| 압수된 도메인 | 2,000개 이상 | Europol |
| 압수된 독일 내 C2 서버 | 17대 | BKA |
| 체포된 피의자 | 2명(우크라이나) | 우크라이나 사이버경찰 |
| 식별된 감염 머신 | 160만 대(2020년 4월 - 2021년 1월) | 미국 DOJ |
| 복구된 침해 자격 증명 | 이메일 주소 430만 건 + 비밀번호 | 네덜란드 국가경찰 |
| 피해자 통보 | 제거 모듈을 통해 100만 대 이상 시스템 정화 | Europol |

### 전략적 영향

1. **MaaS 생태계의 일시적 와해:** Emotet의 테이크다운은 약 10개월간 랜섬웨어 운영자(Ryuk, Conti)들로부터 주된 초기 접근 벡터를 박탈하였다
2. **선구적 피해자 구제:** 감염 머신을 정화하기 위한 법집행 통제 업데이트 배포는 규모면에서 전례 없는 것이었으며 새로운 작전 템플릿을 수립하였다
3. **정보 수확:** 압수된 인프라와 자격 증명 데이터베이스는 광범위한 사이버범죄 생태계에 대한 광범위한 정보를 제공하였다
4. **자격 증명 통보:** 네덜란드 경찰은 잠재적 피해자가 자신의 이메일 자격 증명이 침해되었는지 확인할 수 있는 온라인 도구를 구축하였다

### 한계

본 작전의 결과는 다음 이유로 **부분 성공**으로 평가된다:
- **2명**만 체포되었으며(우크라이나), 어떠한 고위 Emotet 개발자나 운영자도 공개적으로 기소되지 않았다
- 봇넷은 **2021년 11월에 재출현**하였으며, Conti 랜섬웨어 그룹과 연관된 행위자들이 TrickBot 인프라를 통해 재구축하였다
- 재출현은 핵심 운영자에 대한 체포가 동반되지 않은 인프라 테이크다운이 일시적 와해만을 제공함을 입증한다

## 활용된 협력 메커니즘

| 메커니즘 | 적용 |
|-----------|-------------|
| [[joint-investigation-team]] | [[eurojust]]를 통한 네덜란드, 독일 및 기타 EU 국가 간 공동수사팀(JIT) |
| [[europol-jit]] | Europol(유럽 경찰청)이 작전 조정 센터 운영; 교차매칭 분석 제공 |
| [[mutual-legal-assistance]] | 국경 간 증거 공유 및 인프라 압수에 MLAT(형사사법공조조약) 활용 |
| [[24-7-network]] | 인프라 매핑 단계 중 긴급 보전 요청을 위해 사용 가능 |
| DNS 싱크홀링 | 법집행이 C2 트래픽을 통제된 서버로 우회 |
| 피해자 통보 | 네덜란드 경찰이 침해 자격 증명 확인 도구 공개; 제거 모듈 배포 |

### 기술적 혁신: 제거 모듈

Operation LadyBird의 가장 기술적으로 두드러진 측면은 Emotet 자체의 업데이트 메커니즘을 통해 법집행이 만든 DLL("EmotetLoader.dll")을 배포한 것이다. 이 모듈은:

1. C2 인프라가 압수된 후 감염된 머신으로 푸시되었다
2. **2021년 4월 25일**로 시간 지연 활성화가 설정되어 있어 ISP와 CERT가 영향을 받은 조직에 통보할 약 3개월의 기간을 부여하였다
3. 활성화 시 모든 Emotet 관련 서비스를 삭제하고, 레지스트리 키를 제거하며, 실행 중인 프로세스를 종료한 후 자체 삭제되었다
4. 이 접근은 봇넷 자체 인프라를 통해 배포된 법집행 통제 업데이트가 대규모로 피해자를 보호하기 위해 운영적으로 사용된, 최초로 광범위하게 문서화된 사례였다

## 도전 및 마찰 요인

- **관할권의 복잡성:** Emotet의 C2 인프라는 수십 개국에 걸쳐 있었다; 8개 관할권 전반의 동시 조치를 조정하는 데에는 광범위한 준비가 필요하였다
- **대규모 피해자 통보:** 160만 대 감염 머신을 통보하고 정화를 보장하는 것은 물류적 도전이었다
- **"경찰 악성코드"의 법적 권한:** 피해자 머신에 제거 모듈을 배포하는 것은, 구제 목적이라 할지라도, 법집행이 제3자 시스템을 수정할 권한에 대한 법적 의문을 제기하였다
- **범죄 네트워크의 회복력:** 테이크다운에도 불구하고 기저 범죄 운영자들은 10개월 이내에 봇넷을 재구축할 지식과 관계를 유지하였다

## 교훈

1. **인프라 압수는 필요조건이나 충분조건은 아니다:** 핵심 개발자와 운영자를 체포하지 않으면 범죄 네트워크는 재구축될 수 있다. 2021년 11월의 Emotet 재출현은 봇넷 테이크다운이 보완적인 체포 작전을 요구함을 입증하였다
2. **공동수사팀(JIT)이 혁신적 작전을 가능케 한다:** 공동수사팀(JIT) 구조는 관할권 전반에 걸친 법집행 통제 업데이트 모듈의 전례 없는 배포를 용이하게 하였다
3. **대규모 피해자 구제는 실현 가능하다:** 시간 지연 제거 접근은 법집행이 전 세계적으로 피해자 머신을 구제할 수 있음을 입증하였으나, 권한과 책임에 관한 거버넌스 의문을 제기한다
4. **민관 협력이 필수적이다:** ISP, CERT, 보안 업체는 제거 모듈 활성화 전 3개월 기간 동안의 피해자 통보에서 핵심적 역할을 수행하였다
5. **향후 작전을 위한 템플릿:** Operation LadyBird의 접근은 [[operation-endgame-phase1|Operation Endgame]](2024)을 포함한 후속 봇넷 작전에 직접적 영향을 미쳤다

## 한국의 참여

한국은 Operation LadyBird의 **8개 참여국에 포함되지 않았다**. 그러나 본 작전은 다음과 같은 측면에서 한국의 사이버 보안 이익과 관련이 있다:

- **한국 내 Emotet 감염:** 한국은 Emotet C2 인프라가 식별된 국가들 중 하나였으나, 주된 호스팅 위치는 아니었다
- **하류 랜섬웨어 영향:** Emotet은 Ryuk 및 Conti 랜섬웨어의 주된 전달 메커니즘으로 기능하여 한국 조직들의 노출을 야기하였다
- **TrickBot 연결고리:** 테이크다운 이후 Emotet 재구축에 사용된 악성코드인 TrickBot의 추정 개발자가 2022년 한국에서 체포되었으며, 이는 한국이 광범위한 사이버범죄 집행 생태계에서 차지하는 역할을 보여준다
- **작전 템플릿:** Operation LadyBird에서 입증된 협력 모델은 한국이 참여한 후속 작전, 예컨대 [[europol-ec3|Europol]] 조정의 [[phobos-8base-crackdown|Phobos/8Base 단속]](2025) 등에 적용되었다

> [!note]
> 한국의 [[europol-ec3|Europol]] J-CAT(공동 사이버범죄 행동 태스크포스, Joint Cybercrime Action Taskforce) 참여는 봇넷 작전에 관한 정보 공유 채널을 제공하나, Operation LadyBird 당시 한국은 J-CAT 참여국이 아니었다.

## 모순점 및 미해결 문제

1. **체포 인원 불일치:** Europol과 DOJ 보도자료는 정확한 체포 인원을 명시하지 않고 "와해"에 초점을 둔다. 우크라이나 사이버경찰은 하르키우에서 2명 체포를 보고하였으나, 일부 미디어 소스는 더 높은 수치를 보고하였다. 1차 출처 일관성에 근거할 때 2명 체포 수치가 가장 잘 뒷받침된다.

2. **서버 수의 변동:** Europol은 "수백 대의 서버"를 보고하였고, 영국 NCA는 약 700대를 인용하였으며, BKA는 독일 내에 17대를 보고하였다. 이 수치는 호환된다(총 700대, 독일 내 17대). 그러나 정확한 수치는 백업/중계 노드 포함 여부에 따라 변동될 수 있다.

3. **Emotet의 재출현과 운영자 정체성:** 원본 Emotet의 동일 운영자가 TrickBot/Conti 인프라를 활용해 봇넷을 재구축하였을 수 있다. 그렇다면 우크라이나에서의 2명 체포는 핵심 개발 팀을 검거하지 못한 것이다. Emotet 운영자와 Conti 그룹의 관계는 미해결 문제로 남는다.

4. **피해자 구제의 법적 권한:** 피해자 머신에 제거 모듈을 배포하는 법적 근거는 관할권마다 다르다. 공개된 법적 이의 제기는 보고되지 않았으나, 본 관행은 비례성과 권한에 관한 미해결 의문을 제기한다.

> [!warning] 결과 한정
> Operation LadyBird는 성공으로 널리 보도되었으나, **일시적 와해**에 그쳤다. 2021년 11월의 Emotet 재출현은 핵심 운영자에 대한 체포가 동반되지 않은 인프라 중심 테이크다운의 한계를 입증한다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2021-01-27: 전 세계 조치를 통해 와해된 세계에서 가장 위험한 악성코드 EMOTET.
- 미국 법무부 (공보실), 2021-01-27: 국제 사이버 작전에서 와해된 Emotet 봇넷.
- Eurojust, 2021-01-27: 위험한 악성코드 시스템 와해를 위한 주요 작전.
- 미국 노스캐롤라이나 중부지구 연방검찰청(DOJ), 2021-01-27: 국제 사이버 작전에서 와해된 Emotet 봇넷.
- 미국 DOJ (OPA / M.D.N.C.), 2021-01-27: 국제 사이버 작전에서 와해된 Emotet 봇넷.

## Evidence and Attribution Notes

- 8개국 작전(NL, DE, US, UK, FR, LT, CA, UA)을 Europol/Eurojust가 조정.
- Emotet은 랜섬웨어와 뱅킹 트로이를 배포하는 '로더(loader)' MaaS로 운영됨.
- 수백 대의 C2 서버 압수; 새로운 '내부로부터의(from the inside)' 인프라 테이크다운으로 묘사됨.
- 미국 DOJ 추정: 2020년 4월 – 2021년 1월 사이 160만 대 컴퓨터 감염.
- 미국 측 법률 지원과 미국 영토 내 인프라 압수 확인.
- Eurojust 발표가 JIT(공동수사팀) 지원 역할을 확인.
- 네덜란드, 독일 및 기타 EU 참여국 간 사법 조정.
- Emotet 인프라 관련 민사 조치의 미국 측 관할로서 MDNC 확인.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- 미국 법무부 (공보실), 2021-01-27: Department of Justice title="About" title="News" title="Guidance & Resources" Justice.gov Office of Public Affairs Emotet Botnet Disrupted In International Cyber Operation This is archived content from the U.S.
- 미국 법무부 (공보실), 2021-01-27: ﻿"The Emotet malware and botnet infected hundreds of thousands of computers throughout the United States, including our critical infrastructure, and caused millions of dollars in damage to victims worldwide," said Acting Deputy Attorney General John Carlin.
  > (한국어 번역: "Emotet 악성코드와 봇넷은 핵심 인프라를 포함한 미국 전역의 수십만 대의 컴퓨터를 감염시켰으며, 전 세계 피해자들에게 수백만 달러의 피해를 일으켰다"고 존 칼린(John Carlin) 미국 법무부 차관 직무대행은 말했다.)
- 미국 노스캐롤라이나 중부지구 연방검찰청(DOJ), 2021-01-27: Attorney's Office, Middle District of North Carolina Emotet Malware Infected More than 1.6 Million Victim Computers and Caused Hundreds of Millions of Dollars in Damage Worldwide WASHINGTON – The Justice Department today announced its participation in a multinational operation involving actions in the United States, Canada, France.
- 미국 노스캐롤라이나 중부지구 연방검찰청(DOJ), 2021-01-27: "The Emotet malware and botnet infected hundreds of thousands of computers throughout the United States, including our critical infrastructure, and caused millions of dollars in damage to victims worldwide," said Acting Deputy Attorney General John Carlin.
  > (한국어 번역: "Emotet 악성코드와 봇넷은 핵심 인프라를 포함한 미국 전역의 수십만 대의 컴퓨터를 감염시켰으며, 전 세계 피해자들에게 수백만 달러의 피해를 일으켰다"고 존 칼린(John Carlin) 미국 법무부 차관 직무대행은 말했다.)
- 미국 DOJ (OPA / M.D.N.C.), 2021-01-27: Department of Justice title="About" title="News" title="Guidance & Resources" Justice.gov Office of Public Affairs Emotet Botnet Disrupted In International Cyber Operation This is archived content from the U.S.
- 미국 DOJ (OPA / M.D.N.C.), 2021-01-27: ﻿"The Emotet malware and botnet infected hundreds of thousands of computers throughout the United States, including our critical infrastructure, and caused millions of dollars in damage to victims worldwide," said Acting Deputy Attorney General John Carlin.
  > (한국어 번역: "Emotet 악성코드와 봇넷은 핵심 인프라를 포함한 미국 전역의 수십만 대의 컴퓨터를 감염시켰으며, 전 세계 피해자들에게 수백만 달러의 피해를 일으켰다"고 존 칼린(John Carlin) 미국 법무부 차관 직무대행은 말했다.)

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아니라 Emotet 봇넷 인프라 및 운영자에 대한 테이크다운을 기술하므로 정본 작전으로 유지된다. 본 기록은 주도 책임을 Netherlands Politie에, 조정을 Europol Ec3에 귀속시키며, 참여 또는 영향 받은 관할권은 Netherlands, Germany, United States, United Kingdom, France, Ukraine, Canada, Lithuania로 기록된다.

협력 모델은 명시된 기관과 파트너를 통해 문서화된다: Netherlands Politie, Europol Ec3, Eurojust, Fbi Cyber Division; 메커니즘: Joint Investigation Team, Europol Jit, 24 7 Network; 법적 근거: Budapest Convention과 형사사법공조; 집행 자세: Takedown, Arrest, Seizure.

정본 기록을 위한 작전 결과: 체포 2명; 서버 압수 700대; 도메인 압수 2,000개; 피해자 통보 1,000,000명; 네덜란드 경찰이 침해된 이메일 주소 430만 건 복구; 법집행이 감염 머신에 제거 모듈 배포(2021-04-25 활성화); Emotet 봇넷이 2021년 11월 TrickBot 인프라를 통해 재출현.

정본 출처 집합은 4개의 참조를 포함한다: 2021 01 27 Europol Emotet Disruption, 2021 01 27 Eurojust Emotet Operation, 2021 01 27 Doj Mdnc Emotet, 2021 01 27 Mdnc Emotet Disruption Order.
출처 하한선은 정본 작전 기준을 충족하나, 출처의 폭이 모든 하류 체포나 형 선고가 본 작전의 일부임을 그 자체로 증명하지는 않는다; 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
본 페이지가 여전히 보유하는 알려진 메타데이터 공백: Cryptocurrency Seized 및 Full List Of National Agencies Beyond Lead Participants.
데이터셋 활용 시 본 페이지는 작전 수준 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘 및 결과 필드는 조정된 집행 조치 전체를 기술한다. 이후 기소, 답변, 형 선고, 인도 또는 몰수 조치는 출처가 이를 새로운 다국적 작전으로 명시적으로 제시하지 않는 한 관련 사건으로 첨부되거나 후속 기록으로 흡수되어야 한다.
출처 기록이 광범위한 배경, 반복된 통신사 재게재 또는 주제 페이지 자료를 포함하는 경우, 본 평가는 명시된 작전, 그 참여 당국, 그 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과와 직접 결부된 사실을 우선시한다. 주변적 출처 제목은 독립적 분류나 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고 재현 가능한 것으로 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | 발행처 | 일자 | URL |
|---|---|---|---|---|
| [1] | 전 세계 조치를 통해 와해된 세계에서 가장 위험한 악성코드 EMOTET | Europol | 2021-01-27 | https://www.europol.europa.eu/media-press/newsroom/news/world%E2%80%99s-most-dangerous-malware-emotet-disrupted-through-global-action |
| [2] | 국제 사이버 작전에서 와해된 Emotet 봇넷 | 미국 DOJ (OPA / M.D.N.C.) | 2021-01-27 | https://www.justice.gov/archives/opa/pr/emotet-botnet-disrupted-international-cyber-operation |
| [3] | 위험한 악성코드 시스템 와해를 위한 주요 작전 | Eurojust | 2021-01-27 | https://www.eurojust.europa.eu/news/major-operation-take-down-dangerous-malware-systems |
| [4] | 국제 사이버 작전에서 와해된 Emotet 봇넷 | 미국 노스캐롤라이나 중부지구 연방검찰청(DOJ) | 2021-01-27 | https://www.justice.gov/usao-mdnc/pr/emotet-botnet-disrupted-international-cyber-operation |
