---
type: operation
title: "Aisuru / Kimwolf IoT Botnet Takedown — Germany-Canada-United States coordinated disruption of multi-million-device DDoS botnets (BKA + ZAC NRW + US DOJ/DCIS/FBI + Canadian LE, March 2026)"
title_ko: "Aisuru / Kimwolf IoT 봇넷 단속 — 독일·캐나다·미국 공조로 수백만 IoT 기기 DDoS 봇넷 인프라 차단 (BKA + ZAC NRW + 미국 DOJ/DCIS/FBI + 캐나다 LE, 2026-03)"
aliases:
  - "Aisuru botnet takedown 2026"
  - "Kimwolf botnet takedown 2026"
  - "Aisuru Kimwolf disruption"
  - "BKA ZAC NRW Aisuru Kimwolf operation"
  - "Aisuru Kimwolf JackSkid Mossad disruption"
  - "31.4 Tbps DDoS botnet takedown"
case_id: CYB-2026-AISURU-KIMWOLF
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - infrastructure-seizure
  - search-seizure
outcome: success
timeframe:
  announced: 2026-03-20
  start: 2026-03-19
  end: 2026-03-19
  ongoing: false
crime_type: "[[ddos-ic]]"
crime_types:
  - "[[ddos-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
target_entity: "Two of the world's currently largest IoT-based DDoS botnets, Aisuru and Kimwolf, plus the C2 infrastructure used by their administrators. Aisuru is a botnet of 'mehrere Millionen' (several million) compromised Internet-of-Things devices — predominantly routers and webcams — assembled by infecting devices with weak/default credentials and exploitable firmware vulnerabilities. Kimwolf, in direct technical relation with Aisuru, comprises 'mehrere Millionen' (several million) infected devices, predominantly Android TV boxes; its compromised devices were dual-purposed both for high-volume DDoS attacks and for monetisation as a 'residential proxy' anonymisation network rented to third parties. The US-side parallel announcement also names two further botnets in the disrupted set — JackSkid and Mossad — operated under the same or related criminal infrastructure cluster."
lead_agency: "[[germany-bka]]"
coordinating_body: ""
participating_countries:
  - "[[germany]]"
  - "[[canada]]"
  - "[[united-states]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[fbi]]"
  - "[[us-doj]]"
  - "[[us-dcis]]"
  - "[[canada-rcmp-federal-policing]]"
organizations:
  - "[[germany-bka]]"
  - "[[fbi]]"
  - "[[us-doj]]"
  - "[[us-dcis]]"
  - "[[canada-rcmp-federal-policing]]"
mechanisms_used:
  - "[[informal-cooperation]]"
legal_basis:
  - "Court-authorised C2 disruption order (US): the US-side action was conducted as a 'court-authorized law enforcement operation' under FBI/DCIS authority, targeting C2 infrastructure used by the four named IoT botnets."
  - "German criminal procedure: residence searches of identified administrators in Germany executed under StPO authority by ZAC NRW / BKA."
  - "Canadian criminal procedure: residence search in Canada of the second identified administrator executed under domestic Canadian law (specific instrument not detailed in BKA release)."
  - "BSI sinkholing operation: technical disruption coordinated under the German Federal Office for Information Security's IT-security mandate (BSI law)."
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "5-digit EUR amount (per BKA release; specific figure not disclosed)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Two suspected administrators identified — one in Germany, one in Canada (per BKA release). The release records identification + residence searches but does not record arrests; legal consequences (formal charging) are described as forthcoming."
    - "Aisuru botnet C2 infrastructure disrupted: globally distributed servers and domains (specific count: not enumerated in BKA release; US DOJ side cites broader infrastructure across the four-botnet cluster)."
    - "Kimwolf botnet C2 infrastructure disrupted: globally distributed servers, including the residential-proxy rental layer."
    - "Devices compromised at peak (per BKA): 'mehrere Millionen' (several million) IoT devices per botnet — routers/webcams (Aisuru) and Android TV boxes (Kimwolf)."
    - "Combined attack volume (per US DOJ side): >300,000 DDoS attack commands across the four-botnet cluster (Aisuru >200,000; KimWolf >25,000; JackSkid >90,000; Mossad ~1,000)."
    - "Record DDoS attack attributed to the cluster (per third-party telemetry corroborating the US DOJ release): a 31.4 Tbps DDoS attack of 35-second duration in November 2025, attributed by Cloudflare to the AISURU/Kimwolf infrastructure."
    - "Evidence seized at suspect residences: 'zahlreiche Datentraeger' (numerous data carriers) and cryptocurrencies in the 5-digit EUR range."
    - "BSI (Federal Office for Information Security) sinkholing redirected botnet traffic from victim devices to controlled systems for victim-notification via German ISPs."
    - "Two further botnets named in the parallel US DOJ/FBI announcement of the same coordinated action — JackSkid and Mossad — were also disrupted; the BKA release scopes only Aisuru and Kimwolf."
edges:
  - source_actor: germany-bka
    target_actor: fbi
    cooperation_type: joint_investigation
    legal_basis: informal-cooperation
    direction: undirected
  - source_actor: germany-bka
    target_actor: us-dcis
    cooperation_type: joint_investigation
    legal_basis: informal-cooperation
    direction: undirected
  - source_actor: germany-bka
    target_actor: canada-rcmp-federal-policing
    cooperation_type: joint_investigation
    legal_basis: informal-cooperation
    direction: undirected
  - source_actor: usdoj
    target_actor: germany-bka
    cooperation_type: technical_assistance
    legal_basis: informal-cooperation
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "specific server/domain seizure counts (BKA release does not enumerate; US DOJ side gives only attack-command totals)."
  - "specific Canadian agency (BKA names only 'Strafverfolgungsbehoerden aus Kanada' without identifying RCMP, OPP, SQ, or other police; the operation page's Canadian wikilink defaults to [[canada-rcmp-federal-policing]] as the most likely federal counterpart but this is unverified)."
  - "arrest status of the two identified administrators — BKA release describes 'Festnahmen' (arrests) only obliquely as 'rechtliche Konsequenzen' (legal consequences forthcoming); searches were executed but a formal arrest/charge is not stated."
  - "exact crypto seizure amount — only 'fuenfstelliger Bereich' (5-digit EUR) is given."
  - "the BKA release scopes only Aisuru and Kimwolf, while the US DOJ release adds JackSkid and Mossad — the full combined botnet roster vs. the German subset is a known discrepancy."
related_cases: []
related_operations:
  - "[[operation-endgame-phase3]]"
  - "[[operation-power-off-2026-04]]"
challenges_encountered:
  - "[[jurisdictional-conflicts]]"
lessons_learned:
  - "First wiki record of a Germany-Canada-United States trilateral IoT-botnet takedown in Period 3 — establishes the *Western trilateral coordination* pattern as an operational alternative to the larger Europol-led multistate action weeks (Endgame, PowerOFF) for cases where the suspects are concentrated in two non-EU jurisdictions plus one EU lead."
  - "The Aisuru/Kimwolf DDoS botnets reached attack capacities of 31.4 Tbps (per Cloudflare third-party telemetry) — among the largest DDoS volumes recorded in the wiki corpus, exceeding the typical hundreds-of-Gbps range of earlier IoT botnets in the Mirai lineage. The takedown documents the *industrial scale* of contemporary IoT-botnet capacity."
  - "The Kimwolf botnet's dual-use of compromised Android TV devices (DDoS attacks + residential-proxy rental) is a structurally important pattern: it demonstrates monetisation of compromised IoT capacity through the *anonymisation-as-a-service* market in addition to the *DDoS-as-a-service* market. Compromised consumer IoT devices are increasingly multi-product."
  - "BSI sinkholing as the victim-notification channel — the German Federal Office for Information Security's role in redirecting botnet traffic to controlled systems and notifying victim citizens via their ISPs is a reproducible model for other countries' national CSIRTs in IoT-botnet disruption operations."
  - "The discrepancy between the BKA release's two-botnet scope (Aisuru, Kimwolf) and the US DOJ release's four-botnet scope (Aisuru, Kimwolf, JackSkid, Mossad) is illustrative of *jurisdiction-scoped charging*: each national authority describes the action in terms of the offences chargeable in its own legal system, even when the underlying operational coordination is shared. A reader synthesising the operation must read both releases."
  - "L24 strict compliance: BKA release explicitly names cooperating LE in Canada and the US — Canada and the US are *cooperating jurisdictions* (suspects co-located with LE searches), not adversary/origin/destination states. This contrasts with the Iter 124 Delhi Police SIMBOX case where origin/handler/C2 states were misclassified as participating_countries."
source_count: 1
sources:
  - "[[2026-03-20_bka_aisuru-kimwolf-botnet-takedown]]"
created: 2026-05-10
updated: 2026-05-10
---

## Summary

The **Aisuru / Kimwolf IoT Botnet Takedown** (action day **19 March 2026**, announced **20 March 2026**) was a Germany-Canada-United States internationally coordinated disruption of the technical infrastructure of two of the world's currently largest Internet-of-Things-based DDoS botnets, Aisuru and Kimwolf. The German leg was led jointly by the **Central and Contact Point Cybercrime North Rhine-Westphalia (Zentral- und Ansprechstelle Cybercrime Nordrhein-Westfalen, ZAC NRW)** and the **Federal Criminal Police Office (Bundeskriminalamt, BKA)**, with technical support from the **Federal Office for Information Security (Bundesamt fuer Sicherheit in der Informationstechnik, BSI)** which sinkholed the perpetrator infrastructure. The action proceeded "gemeinsam mit Strafverfolgungsbehoerden aus Kanada und den USA" — together with law enforcement authorities from Canada and the United States. Two suspected botnet administrators were identified, with residence searches in Germany and Canada producing 'numerous data carriers' and cryptocurrencies in the 5-digit EUR range as evidence.

A parallel US Department of Justice / Federal Bureau of Investigation announcement of the same coordinated action describes a broader four-botnet disrupted set — Aisuru, Kimwolf, **JackSkid**, and **Mossad** — with the **Defense Criminal Investigative Service (DCIS)** leading the US investigation supported by the **FBI Anchorage Field Office**. The four-botnet cluster collectively launched **>300,000 DDoS attack commands** (Aisuru >200,000; Kimwolf >25,000; JackSkid >90,000; Mossad ~1,000), including a record **31.4 Tbps** DDoS attack of 35-second duration in November 2025 attributed by Cloudflare to the Aisuru/Kimwolf infrastructure.

> [!note] L24 strict compliance
> The BKA tier-1 primary source explicitly names *cooperating* jurisdictions (Canada and the United States) — both LE counterparts to BKA and locations of identified suspects. No adversary/origin/destination state attribution is being misclassified as IC participation. This satisfies the L24 requirement of ≥2 distinct countries' LE/prosecutorial cooperation explicitly acknowledged in the tier-1 primary source.

## Background

The Aisuru botnet is a multi-million-device IoT botnet predominantly compromising routers and webcams — a structural successor to the Mirai botnet lineage but reaching attack volumes that exceed Mirai-era records. The Kimwolf botnet, in direct technical relation with Aisuru (per the BKA release: "in direktem Zusammenhang"), comprises several million predominantly Android TV box devices and was used both for DDoS attacks and as a *residential proxy* network rented to third parties for anonymisation of internet activity ("Anonymisierungsschicht"). The US DOJ-side announcement adds two further related botnets — JackSkid and Mossad — to the disrupted set; per US court documents, the four botnets collectively issued more than 300,000 DDoS attack commands against victims worldwide, including IP addresses of the U.S. Department of Defense Information Network (DoDIN). A November 2025 DDoS attack of 31.4 Tbps over 35 seconds, attributed by Cloudflare to the Aisuru/Kimwolf infrastructure, is among the largest DDoS volumes ever recorded.

The takedown action followed "aufwaendige mehrmonatige Ermittlungen [...] von hohem technischem Anspruch und enger internationaler Koordination" — multi-month investigations of high technical complexity and close international coordination — predating the 19 March 2026 action day.

## Participating Parties

| Country | Lead Agency / Unit | Role |
|---|---|---|
| Germany | **Lead (German leg)** — [[germany-bka\|Bundeskriminalamt (BKA)]] + Zentral- und Ansprechstelle Cybercrime Nordrhein-Westfalen (ZAC NRW) | Investigative lead, residence searches, evidence seizure, public communication |
| Germany | Bundesamt fuer Sicherheit in der Informationstechnik (BSI) | Technical analysis, sinkholing of perpetrator infrastructure, victim-notification via German ISPs |
| United States | [[usdoj\|U.S. Department of Justice]] + [[us-dcis\|Defense Criminal Investigative Service (DCIS)]] + [[fbi\|Federal Bureau of Investigation]] (Anchorage Field Office) | Court-authorised C2 disruption, parallel charging in US jurisdiction |
| Canada | [[canada-rcmp-federal-policing\|Canadian federal LE]] (specific agency not named in BKA release) | Residence search of identified Canadian-resident administrator |

> [!warning] Canadian agency identification not stated in primary source
> The BKA release names only "Strafverfolgungsbehoerden aus Kanada" (law enforcement authorities from Canada) without identifying the specific Canadian agency. The wikilink defaults to [[canada-rcmp-federal-policing]] as the most likely federal counterpart for a transnational cybercrime takedown, but this assignment is not affirmatively verified in the primary source. Provincial police forces (e.g., Ontario Provincial Police, Sûreté du Québec) cannot be ruled out without further sourcing.

## Legal Framework

- **U.S. side:** court-authorised C2 disruption order; civil/criminal infrastructure seizure under FBI/DCIS authority, with the Defense Criminal Investigative Service taking the investigative lead because DDoS attack commands had targeted IP addresses on the Department of Defense Information Network (DoDIN).
- **German side:** searches under StPO (Strafprozessordnung) authority at administrator residences in Germany; offences under German cybercrime statutes (specific provision not named in the BKA release).
- **Canadian side:** Canadian domestic criminal procedure; specific instrument not detailed in BKA release.
- **Technical disruption:** BSI sinkholing operation under the German Federal Office for Information Security's IT-security mandate (BSI law). Sinkholing is described as redirection of "Datenverkehr eines boesartigen Akteurs (z.B. eines Botnetzes) [...] um ihn von seinem urspruenglichen Ziel abzulenken und zu einem kontrollierten System zu leiten" — redirecting malicious-actor traffic from its original target to a controlled system.

## Operational Timeline

| Date | Event |
|---|---|
| 2024-2025 (early) | Multi-month international investigations into the Aisuru and Kimwolf C2 infrastructure begin (BKA release: "aufwaendige mehrmonatige Ermittlungen"). |
| 2025-10 | Per US DOJ side: Aisuru is used to seed Kimwolf, an Aisuru variant introducing a novel intra-network spreading mechanism enabling infection of devices behind user-internal NAT layers. |
| 2025-11 | 31.4 Tbps DDoS attack of 35-second duration attributed by Cloudflare to the Aisuru/Kimwolf infrastructure. |
| 2026-01 | Per US DOJ side: Kimwolf reaches >2 million infected Android TV devices. |
| **2026-03-19** | **Action day** — coordinated disruption of C2 infrastructure; residence searches at administrator addresses in Germany and Canada; evidence seizure (data carriers + 5-digit EUR cryptocurrency). |
| 2026-03-19 to 2026-03-20 | US DOJ / FBI parallel announcement of disruption of the four-botnet cluster (Aisuru, Kimwolf, JackSkid, Mossad). |
| 2026-03-20 | BKA / ZAC NRW press release. |

## Results and Impact

- **Two administrators identified** — one resident in Germany, one resident in Canada — both subjects of residence searches on the action day.
- **C2 infrastructure disrupted:** globally distributed servers and domains supporting Aisuru and Kimwolf were taken offline. The US DOJ-side scope adds JackSkid and Mossad to the disrupted infrastructure cluster.
- **Sinkholing initiated by BSI:** infected-device traffic is now redirected to a controlled system, enabling per-device victim notification through German ISPs.
- **Evidence:** "zahlreiche Datentraeger" (numerous data carriers) seized; cryptocurrency in the 5-digit EUR range secured.
- **Scope of suppressed botnets:** several million IoT devices per botnet (Aisuru: routers/webcams; Kimwolf: Android TV boxes); cumulative >300,000 DDoS attack commands from the four-botnet cluster (US DOJ side).

## Cooperation Mechanisms Used

- **Informal LE-to-LE cooperation** ([[informal-cooperation]]) appears to have been the operational backbone, with parallel court-authorised infrastructure-disruption orders in each jurisdiction. The BKA release does not identify Eurojust or a formal Joint Investigation Team (JIT), distinguishing this operation from the predominantly Eurojust-coordinated EU-internal takedowns (e.g., [[operation-endgame-phase3]]).
- **National CSIRT integration** (BSI sinkholing) as a victim-notification mechanism — a model also used in earlier German-led IoT-botnet operations.
- **Court-authorised disruption order** (US) as the legal vehicle for C2 infrastructure seizure.

## Challenges and Friction Points

- **[[jurisdictional-conflicts]] — overlapping but non-identical charging scope:** the BKA release scopes the disrupted set as two botnets (Aisuru, Kimwolf), while the US DOJ release scopes the disrupted set as four botnets (adding JackSkid, Mossad). This is an artefact of jurisdiction-specific charging — each national authority describes the action in terms of offences chargeable in its own system — but it forces synthesisers to read both releases to obtain the full operational picture.
- **Attribution scoping:** the BKA release does not identify the specific Canadian LE agency that conducted the Canadian-leg residence search, leaving the wikilink to [[canada-rcmp-federal-policing]] as a default rather than an affirmatively verified attribution.
- **Suspect status:** the BKA release uses "rechtliche Konsequenzen" (legal consequences forthcoming) rather than "Festnahmen" (arrests) — suggesting the action day produced search/identification but not necessarily formal arrest/charge of the two suspects, which may reflect either a factual constraint or a cautious German prosecutorial communications posture pre-charging.

## Lessons Learned

1. **Germany-Canada-US trilateral IoT-botnet takedown** is a viable operational pattern alongside the larger Europol-led multistate action weeks. When suspects are concentrated in two non-EU jurisdictions plus one EU lead, a focused trilateral with national-CSIRT (BSI) integration appears to scale the disruption without requiring a JIT.
2. **Industrial-scale IoT-botnet capacity** is now demonstrably in the **30+ Tbps DDoS regime** (Cloudflare-attributed 31.4 Tbps attack from this cluster). The wiki's earlier IoT-botnet records (Mirai-era) are an order of magnitude smaller; this operation establishes the contemporary capacity baseline.
3. **Compromised IoT devices increasingly multi-product:** Kimwolf's dual-use as DDoS muscle + residential-proxy anonymisation rental documents the *anonymisation-as-a-service* monetisation track in addition to the *DDoS-as-a-service* track. Future IoT-botnet takedowns should expect to find both.
4. **National CSIRT integration as victim-notification channel:** the BSI sinkholing + ISP-notification model is reproducible in other jurisdictions with national CSIRT capacity, and is a counterpart to LE infrastructure seizure rather than an alternative.
5. **Per-jurisdiction charging-scope discrepancies are normal:** the BKA-2 vs. DOJ-4 botnet count discrepancy is *not* a contradiction but a structural feature of multi-jurisdiction takedown announcements. Wiki synthesis should always aggregate both releases.
6. **L24 strict-compliance pattern:** all three named jurisdictions (Germany, Canada, United States) are *cooperating* jurisdictions, with LE in each conducting actions. No origin/destination/adversary state is being misclassified as IC participant. This contrasts with the Iter 124 anti-pattern (Delhi Police SIMBOX) and demonstrates the correct application of the strict L24 rule.

## Follow-Up Actions

- **Charging:** legal consequences against the two identified administrators are described as forthcoming. Future updates should track whether arrests/charges in Germany and Canada actually proceed and on what statutes.
- **Victim notification:** BSI is expected to continue per-device notifications to German citizens via ISPs based on sinkholed traffic; victim-notification reach beyond Germany via Canadian/US CSIRT counterparts is not specified in the cited release.
- **Botnet revival monitoring:** as discussed in third-party telemetry analyses, IoT-botnet ecosystems frequently rebuild from new C2 infrastructure within weeks of a takedown. Future iterations of this page should track whether Aisuru/Kimwolf or successor botnets re-emerge in mid-2026.

## Korean Involvement (한국의 참여)

No Korean LE involvement is named in the BKA release or the parallel US DOJ release. Korean victim-device counts are not enumerated; Korea is not listed as a jurisdiction with LE counterparts in the trilateral. (Per L24 strict reading: Korean involvement cannot be asserted absent explicit tier-1 sourcing.)

## Contradictions & Open Questions

- **Two-vs-four botnet scope discrepancy** between the BKA and US DOJ releases — already discussed under "Challenges and Friction Points." Treated as jurisdiction-scoped charging, not contradiction.
- **Unidentified Canadian agency** — the BKA release names only "Strafverfolgungsbehoerden aus Kanada" without specifying RCMP / OPP / SQ / other. Wikilink defaults to [[canada-rcmp-federal-policing]] as the most likely federal counterpart for a transnational cybercrime takedown, but this is unverified.
- **Suspect status** — searches conducted, but the BKA release uses "rechtliche Konsequenzen" (legal consequences forthcoming) rather than affirmative "Festnahme" (arrest) or "Anklage" (indictment). Open whether formal charging has occurred as of the cited release date.
- **Cryptocurrency seizure exact amount** — only "fuenfstelliger Bereich" (5-digit EUR) is given. Order-of-magnitude figure usable for the wiki, but the exact amount is undisclosed.
