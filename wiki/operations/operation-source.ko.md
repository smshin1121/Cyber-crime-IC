## 개요

2015년 4월, Europol(유럽형사경찰기구)과 네덜란드 첨단기술범죄수사대(Netherlands High Tech Crime Unit)는 FBI(미국 연방수사국), EU 회원국 기관들 및 주요 사이버보안 기업들과 협력하여 다형성(polymorphic) Beebone 봇넷을 무력화하기 위한 Operation Source(소스 작전)를 수행하였다. 본 작전은 100개 이상의 명령제어(C&C) 서버 도메인을 차단함으로써, 금융정보 탈취형 악성코드, 랜섬웨어, 루트킷 및 가짜 백신 소프트웨어의 유포를 교란하였다.

## Participating Parties

**Lead Agencies:**
- Europol European Cybercrime Centre (EC3) (유럽 사이버범죄 센터)
- Joint Cybercrime Action Taskforce (J-CAT) (공동 사이버범죄 대응 태스크포스)
- Netherlands High Tech Crime Unit (NHTCU) (네덜란드 첨단기술범죄수사대)

**Key Partners:**
- FBI (미국)
- Intel Security
- Kaspersky Lab
- Shadowserver

**Participating Countries:**
네덜란드, 미국, EU 회원국(독일, 프랑스, 이탈리아 등).

## Results

- **100개 이상의 명령제어(C&C) 도메인** 차단
- 다형성 Beebone 봇넷 무력화
- 랜섬웨어, 금융 악성코드, 루트킷 유포 교란

## Follow-Up Actions

> [!warning] No public court documents found
> 웹 검색(2026-04-17) 결과 본 작전에 대해 공개적으로 접근 가능한
> 법원 제출 문서가 확인되지 않았다. 가능한 사유로는 공개 법원
> 기록 체계가 없는 비미국 관할권, 봉인된 절차, 또는 본 작전이
> 공식 기소로 이어지지 않았을 가능성을 들 수 있다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2015-04-09: Europol: International Police Operation Targets Polymorphic Beebone Botnet (Operation Source).
- SC Media, 2015-04-09: International effort takes down Beebone botnet.
- SecurityWeek, 2015-04-09: Authorities Takedown Beebone Botnet in International Operation.
- Ars Technica, 2015-04-09: US, European police take down highly elusive botnet known as Beebone.
- Wired, 2015-04-10: Beebone Botnet bites the dust.

## Operational Timeline

- 2015년 4월: 활동 또는 수사 개시.
- 2015년 4월: 공식 발표.
- 2015년 4월: 보고된 집행 종결 시점.
- 2015-04-09: Ars Technica, Europol, SC Media, SecurityWeek로부터의 공개 자료 보도.
- 2015-04-10: Wired로부터의 공개 자료 보도.

## Legal and Procedural Posture

- 기록된 범죄 분류: 악성코드 및 랜섬웨어.
- 기록된 집행 형태: 테이크다운 및 압수.
- 본 기록은 테이크다운으로 분류되며 상태는 completed(완료)이다.

## Evidence and Attribution Notes

- Europol EC3, 공동 사이버범죄 대응 태스크포스(J-CAT), 그리고 네덜란드 첨단기술범죄수사대(NHTCU)는 2015년 4월 8일 협력 국제 작전을 통해 Beebone(W32/Worm-AAEH) 다형성 봇넷을 싱크홀링(sinkholing)하였다
- 본 봇넷은 악성코드 통신에 사용되는 명령제어(C&C) 도메인을 등록·정지·압수하는 방식으로 무력화되었으며, 서버 압수가 아닌 싱크홀 방식이 사용되었다
- W32/Worm-AAEH 계열의 고유 다형성 샘플 500만 개가 식별되었으며, 2013~2014년 동안 195개국 23,000개 시스템에서 205,000개 이상의 샘플이 수집되었다
- 테이크다운 시점에 약 12,000대의 컴퓨터가 실제 감염 상태였으나, Europol은 추가 감염 사례가 다수 존재할 가능성을 지적하였다; 미국이 가장 많은 감염을 기록하였고, 일본·인도·대만이 그 뒤를 이었다
- 본 작전에서 Beebone은 다른 악성코드의 유포 매개체로 사용되었다: 금융 자격증명 탈취 도구, 랜섬웨어, 루트킷, 가짜 백신 소프트웨어 — 따라서 본 테이크다운은 복수의 악성코드 계열에 대한 효과를 배가하는 작용을 하였다
- 참여 기관: Europol EC3(조정 역할), J-CAT, 네덜란드 NHTCU, FBI, 미국 국가사이버수사합동태스크포스(National Cyber Investigative Joint Task Force), Eurojust(사법 조정), 그리고 민간 파트너 Intel Security, Kaspersky Lab, Shadowserver, F-Secure, Symantec, TrendMicro
- Operation Source는 이후 Operations Avalanche(2016), Andromeda(2017), Endgame(2024-2025)에서 보다 정교화될 봇넷 테이크다운의 민관 파트너십(PPP) 모델의 초기 사례에 해당한다
- SC Media는 Operation Source가 싱크홀링 및 도메인 압수를 통해 Beebone 봇넷을 표적으로 삼았다고 보도하였다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 행위가 아니라 Beebone Botnet(다형성)에 대한 테이크다운을 기술하므로, 정본 작전(canonical operation)으로서 유지된다. 본 기록은 주도 책임을 Europol EC3에, 조정 역할을 Europol EC3에 귀속시키며, 참여 또는 영향을 받은 관할권으로 네덜란드, 미국, EU 회원국을 기록하고 있다.

협력 모델은 명시된 기관 및 파트너를 통해 문서화되어 있다: Europol EC3, J-CAT, 네덜란드 NHTCU, FBI, Intel Security, Kaspersky Lab, Shadowserver; 집행 형태: 테이크다운 및 압수.

정본 기록을 위한 작전 결과: 100개 도메인 압수; 100개 이상의 명령제어 도메인 차단; 다형성 Beebone 봇넷 무력화.

정본 자료군은 5건의 참고자료를 포함한다: Europol Operation Source, 2015 04 09 Scworld Com International Effort Takes Down Beebone Botnet, 2015 04 09 Securityweek Com Authorities Takedown Beebone Botnet International Operation, 2015 04 09 Arstechnica Us European Police Take Down Highly Elusive Botnet Known As Beebone, 2015 04 10 Wired Com Beebone Botnet Bites The Dust.
자료 최저 기준은 정본 작전 요건을 충족하나, 자료 다양성만으로는 모든 하위 체포 또는 양형이 본 작전의 일부임이 입증되지 않으므로, 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
본 페이지가 여전히 보유한 메타데이터 누락: Legal Basis 및 Mechanisms Used.
데이터셋 활용 시 본 페이지는 작전 단위 집약점(operation-level aggregation point)으로 취급되어야 한다: 국가·기관·메커니즘 및 결과 필드는 조정된 집행 행위 전체를 기술한다. 이후의 기소, 답변(plea), 양형, 인도, 또는 자산 몰수 행위는, 해당 자료가 명시적으로 새로운 다자간 작전으로 제시하지 않는 한, 관련 사건 또는 흡수된 후속 기록으로 부착되어야 한다.
자료 기록에 광범위한 배경, 반복되는 통신사 재게재, 또는 주제 페이지 자료가 포함되어 있는 경우, 본 평가는 명시된 작전, 그 참여 당국, 그 표적 인프라 또는 범죄 서비스, 그리고 측정 가능한 집행 결과와 직접 연결되는 사실을 우선시한다. 주변적인 자료 제목은 독립적인 분류 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고 재현 가능한 상태로 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol: 다형성 Beebone 봇넷을 표적으로 한 국제 경찰 작전 (Operation Source) | Europol | 2015-04-09 | https://www.europol.europa.eu/media-press/newsroom/news/international-police-operation-targets-polymorphic-beebone-botnet |
| [2] | 국제적 노력, Beebone 봇넷을 무력화하다 | SC Media | 2015-04-09 | https://www.scworld.com/news/international-effort-takes-down-beebone-botnet |
| [3] | 당국, 국제 작전을 통해 Beebone 봇넷을 테이크다운하다 | SecurityWeek | 2015-04-09 | https://www.securityweek.com/authorities-takedown-beebone-botnet-international-operation/ |
| [4] | 미국·유럽 경찰, Beebone으로 알려진 고은밀(highly elusive) 봇넷을 테이크다운하다 | Ars Technica | 2015-04-09 | https://arstechnica.com/information-technology/2015/04/us-european-police-take-down-highly-elusive-botnet-known-as-beebone/ |
| [5] | Beebone 봇넷, 종말을 맞다 | Wired | 2015-04-10 | https://www.wired.com/beyond-the-beyond/2015/04/beebone-botnet-bites-dust |
