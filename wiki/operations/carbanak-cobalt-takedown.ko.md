## 개요

스페인 당국은 Europol(유럽 경찰청) 및 기타 국제 파트너의 지원을 받아 스페인에서 Carbanak/Cobalt 은행 사기 캠페인의 배후로 추정되는 인물을 체포하였다. 체포 서사는 공식적이지만, 캠페인에 대한 기술적 이해는 여전히 Kaspersky(카스퍼스키)의 이전 보고에 크게 의존한다.

> [!note] Audit Note — Participating Countries (2026-04-21)
> Tier-1 출처 교차 점검 후 벨라루스, 몰도바, 대만은 `participating_countries`에서 제거되었다: Europol Carbanak/Cobalt PDF(1.1 MB), BBC, Reuters, Kaspersky의 Securelist 글 모두 이 세 곳 중 어느 곳도 운영 참여자로 지명하지 않는다(표적 / 피해자 지리는 논의되었으나 LE 기여는 아님). 유지된 국가 — 스페인(주도), 미국(FBI(미국 연방수사국)), 루마니아 — 는 각각 다수의 1차 출처에서 명시적으로 지명된다.

## 본 작전이 중요한 이유

Carbanak/Cobalt는 금융 침투, 은행 사기, 국경 간 법집행의 교차점에 위치하기 때문에 중요하다. 공개 출처는 본 캠페인이 소비자 자격증명 절취에 그치지 않고 금융기관을 직접 표적으로 삼은 것으로 일관되게 묘사한다.

## 참여 당사자

**주도 및 조정:**
- [[spanish-national-police|스페인 국가경찰]]
- [[europol-ec3|Europol EC3]]

**공개 보도에 지명된 파트너:**
- [[fbi]]
- 루마니아 당국
- 몰도바 당국
- 벨라루스 당국
- 대만 당국
- 민간부문 기술 기여자로 [[kaspersky-lab|Kaspersky Lab]]

## 결과

- 스페인에서 배후로 추정되는 1명 체포

## 협력 및 법적 분석

본 페이지는 두 가지 증거 층위를 의도적으로 분리한다. Europol과 스페인 경찰 보도는 체포 사건과 파트너 구성을 확립한다. Kaspersky의 보고서는 스피어피싱, 측면 이동, 은행 내부 침해, ATM 현금 인출 행위를 포함한 공격 체인을 설명한다. 이 층위들을 구분 없이 혼합하면 페이지의 투명성이 떨어진다.

또 다른 무결성 이슈는 신원이다. 본 저장소가 사용하는 현재 출처 세트는 공식 기소 문서로부터 피고인의 이름을 명확하게 확립하지 못한다. 데이터셋의 오염을 방지하기 위해, 본 페이지는 2차 보도에서 분쟁 중이거나 약하게 출처된 신원을 가져오기보다 피의자를 비공개 상태로 유지한다.

## 후속 조치

> [!warning] No public court documents found
> 본 저장소는 현재 체포 사건과 캠페인 메커니즘에 대한 강한 공개 보도를 보유하고 있으나, 체포 이후 기소에 대한 견고한 공개 사건기록 세트는 보유하고 있지 않다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2018-03-01: Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain.
- Kaspersky Securelist, 2015-02-16: The Great Bank Robbery: the Carbanak APT.
- Europol, 2026-04-18: Carbanak / Cobalt infographic.
- FBI, 2018-08-01: How Cyber Crime Group FIN7 Attacked and Stole Data from Hundreds of U.S. Companies.
- SecurityWeek, 2018-03-26: Ukrainian Suspected of Leading Carbanak Gang Arrested in Spain.

## 작전 타임라인

- 2013년: 활동 또는 수사 개시.
- 2018년 3월: 공식 발표.
- 2018년 3월: 보고된 단속 종료 시점.
- 2015-02-16: Kaspersky Securelist의 공개 출처 보도.
- 2018-03-01: Europol의 공개 출처 보도.
- 2018-03-26: SecurityWeek의 공개 출처 보도.
- 2018-08-01: FBI(미국 연방수사국)의 공개 출처 보도.
- 2026-04-18: Europol의 공개 출처 보도.

## Evidence and Attribution Notes

- 스페인 국가경찰은 Europol(유럽 경찰청), FBI(미국 연방수사국), 루마니아 경찰, 벨라루스 경찰, 대만 당국과 협력하여 스페인에서 Carbanak 및 Cobalt 악성코드 캠페인의 배후를 체포하였다.
- 피의자는 Carbanak, Cobalt, Anunak 악성코드를 사용하여 2013년 이래 40개 이상 국가의 100개 이상 금융기관으로부터 EUR 10억 이상을 탈취한 사이버범죄 그룹을 이끌었다.
- Kaspersky를 포함한 민간 사이버보안 기업이 수사에 기여하였다.
- Kaspersky는 Carbanak 캠페인을 소매 은행 고객이 아닌 은행을 직접 표적으로 삼은 금전적 동기의 침입 집합으로 문서화하였다.
- 보고서는 약 100개 금융기관에서 USD 10억까지의 손실을 추정했으며, 그룹의 스피어피싱, 측면 이동, ATM 현금 인출 방법을 묘사하였다.
- 본 보고서는 Europol 및 기타 공식 기관이 후일 인용한 악성코드와 침입 수법에 대한 핵심 기술 출처이다.
- 본 Kaspersky 기술 보고서는 Carbanak 캠페인에 대한 기초적인 공개 묘사이다.
- 보고서는 침입 체인을 제시하고, 직접-은행-표적 모델을 식별하며, 2018년 법집행이 규모와 수법에 대해 주장한 내용이 신뢰할 만한 이유를 설명한다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## 원시 출처 하이라이트

- FBI, 2018-01-01: 적어도 2015년부터 FIN7 구성원은 100개 이상의 미국 회사를 표적으로 고도로 정교한 악성코드 캠페인을 수행하였다.
- FBI, 2018-01-01: 더 큰 이미지를 보고 다운로드 네트워크 침입: 통제 및 데이터 유출 일단 감염되면, 침해된 피해자 컴퓨터는 전 세계에 위치한 FIN7의 지휘통제 서버 중 하나에 연결되었다.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a joint-investigation against Carbanak/Cobalt cybercrime group, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Spanish National Police and coordination to Europol Ec3, with participating or affected jurisdictions recorded as Spain, United States, Romania.

The cooperation model is documented through named agencies and partners: Spanish National Police, Europol Ec3, Fbi, Romanian Police, Kaspersky Lab; mechanisms: informal cooperation; enforcement posture: Arrest.

Operational results captured for the canonical record: 1 arrests; 100+ financial institutions in 40+ countries targeted; EUR 1 billion+ in losses publicly attributed to the campaign.

The canonical source set contains 5 reference(s): 2018 03 01 Europol Europa Eu Mastermind Behind Eur 1 Billion Cyber Bank Robbery Arrested In Spain, 2015 02 16 Securelist The Great Bank Robbery The Carbanak Apt, 2026 04 18 Europol Europa Eu Carbanak Cobalt Infographic, 2018 08 01 Fbi Gov How Cyber Crime Group Fin7 Attacked And Stole Data From Hundreds Of Us Companies, 2018 03 26 Securityweek Ukrainian Suspected Leading Carbanak Gang Arrested Spain.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | 발행자 | 일자 | URL |
|---|---|---|---|---|
| [1] | Mastermind Behind EUR 1 Billion Cyber Bank Robbery Arrested in Spain | Europol | 2018-03-01 | https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain |
| [2] | The Great Bank Robbery: the Carbanak APT | Kaspersky Securelist | 2015-02-16 | https://securelist.com/the-great-bank-robbery-the-carbanak-apt/68732/ |
| [3] | Carbanak / Cobalt infographic | Europol | 2026-04-18 | https://www.europol.europa.eu/cms/sites/default/files/documents/carbanakcobalt.pdf |
| [4] | How Cyber Crime Group FIN7 Attacked and Stole Data from Hundreds of U.S. Companies | FBI | 2018-08-01 | https://www.fbi.gov/contact-us/field-offices/seattle/news/stories/how-cyber-crime-group-fin7-attacked-and-stole-data-from-hundreds-of-us-companies |
| [5] | Ukrainian Suspected of Leading Carbanak Gang Arrested in Spain | SecurityWeek | 2018-03-26 | https://www.securityweek.com/ukrainian-suspected-leading-carbanak-gang-arrested-spain/ |
