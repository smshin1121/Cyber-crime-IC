---
type: operation
title: "Warzone RAT Takedown (Operation against Warzone RAT) — Malta + Nigeria arrests, U.S. domain seizure"
aliases:
  - "Warzone RAT takedown"
  - "Warzone RAT operation"
  - "Operation against Warzone RAT"
case_id: "CYB-2024-WZN"
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - seizure
  - takedown
  - indictment
outcome: success
timeframe:
  announced: 2024-02-09
  start: 2020
  end: 2024-02-13
  ongoing: false
crime_types:
  - "[[malware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[hacking-ic]]"
crime_type: "malware-ic"
target_entity: "Warzone Remote Access Trojan (RAT) malware-as-a-service distribution network (warzone.ws and 3 related domains; subscription-based RAT enabling unauthorized remote access, file-system browsing, keylogging, credential theft, webcam access)"
lead_agency: "[[fbi]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-states]]"
  - "[[australia]]"
  - "[[malta]]"
  - "[[nigeria]]"
  - "[[canada]]"
  - "[[croatia]]"
  - "[[finland]]"
  - "[[germany]]"
  - "[[japan]]"
  - "[[netherlands]]"
  - "[[romania]]"
participating_agencies:
  - "[[fbi]]"
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
  - "[[office-of-international-affairs]]"
  - "[[australia-afp]]"
  - "[[europol-ec3]]"
  - "[[nigeria-efcc]]"
  - "[[finland-nbi]]"
  - "[[germany-lka]]"
  - "[[netherlands-politie]]"
  - "[[canada-rcmp]]"
  - "[[romania-police]]"
legal_basis:
  - "[[computer-fraud-and-abuse-act]]"
  - "[[us-australia-mlat]]"
  - "[[budapest-convention]]"
mechanisms_used:
  - "[[mlat-process]]"
  - "[[mutual-legal-assistance]]"
  - "[[domain-seizure]]"
  - "[[extradition]]"
results:
  arrests: 2
  indictments: 2
  servers_seized: 0
  domains_seized: 4
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "warzone.ws plus three related domains seized by federal authorities in Boston (D. Mass.)"
    - "Indictment districts: Northern District of Georgia (Meli, 12 December 2023, four counts) and District of Massachusetts (Odinakachi, 30 January 2024, conspiracy to commit multiple computer intrusion offenses)"
    - "Defendants: Daniel Meli (27, Zabbar, Malta) — arrested 7 February 2024 by Malta Police Force at U.S. request; Prince Onyeoziri Odinakachi (31, Nigeria) — arrested 7 February 2024 by Port Harcourt Zonal Command of Nigeria's EFCC"
    - "Subscription-based RAT priced from approximately AUD $25 / USD $25 per month"
    - "Victim reporting portal established at https://wzvictims.ic3.gov"
edges:
  - source_actor: "[[fbi]]"
    target_actor: "[[australia-afp]]"
    cooperation_type: info_sharing
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: "[[fbi]]"
    target_actor: "[[europol-ec3]]"
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: "[[fbi]]"
    target_actor: "[[nigeria-efcc]]"
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: directed
  - source_actor: "[[fbi]]"
    target_actor: "[[finland-nbi]]"
    cooperation_type: technical_assistance
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: "[[fbi]]"
    target_actor: "[[netherlands-politie]]"
    cooperation_type: technical_assistance
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: "[[fbi]]"
    target_actor: "[[germany-lka]]"
    cooperation_type: technical_assistance
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: "[[fbi]]"
    target_actor: "[[canada-rcmp]]"
    cooperation_type: technical_assistance
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: "[[fbi]]"
    target_actor: "[[romania-police]]"
    cooperation_type: technical_assistance
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: "[[us-doj]]"
    target_actor: "[[malta]]"
    cooperation_type: extradition
    legal_basis: bilateral_MOU
    direction: directed
credibility_index: 4.5
source_tier: 1
missing_fields: []
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "AFP threat-identification at the intelligence stage (2020) was the trigger that allowed FBI Boston/Atlanta to develop a U.S. prosecutorial case against the seller (Meli) and a major customer-support actor (Odinakachi)."
  - "Coordinated arrests in Malta and Nigeria on the same day (7 Feb 2024) demonstrate that simultaneous arrests in non-EU jurisdictions can be staged through Europol coordination plus bilateral channels (DOJ Office of International Affairs)."
  - "Domain seizure (warzone.ws + 3 related) preceded the arrest announcement by 2 days (DOJ release 9 Feb; AFP release 13 Feb) — typical sequencing for malware-as-a-service takedowns to disrupt customer access before publicity."
source_count: 2
sources:
  - "[[2024-02-13_afp-gov-au_warzone-rat-takedown-malta-arrest]]"
created: 2026-05-10
updated: 2026-05-10
---

## Summary

The Warzone RAT takedown was an international law enforcement action against the infrastructure and key personnel behind the Warzone Remote Access Trojan, a subscription-based malware-as-a-service tool sold from at least 2018 (and tied via the seller to an earlier "Pegasus RAT" via "Skynet-Corporation" since at least 2012). On 9 February 2024, the U.S. Department of Justice announced the seizure of `warzone.ws` and three related domains (D. Mass.) and unsealed two indictments — Daniel Meli (27, Malta) in the Northern District of Georgia and Prince Onyeoziri Odinakachi (31, Nigeria) in the District of Massachusetts — both arrested on 7 February 2024 by, respectively, the Malta Police Force and the Port Harcourt Zonal Command of Nigeria's Economic and Financial Crimes Commission.

On 13 February 2024 the [[australia-afp|Australian Federal Police]] published its own media release (the primary source for this page) crediting the AFP's Cyber Command with identifying Warzone as an emerging cyber threat in 2020 and providing the intelligence that led to the Maltese arrest. The operation was "coordinated with international partners in large part through" the [[europol-ec3|Europol European Cybercrime Center]] (DOJ).

The DOJ acknowledged "valuable assistance" from the law enforcement authorities of Australia, Canada, Croatia, Finland, Germany (specifically the State Police Force of Saxony / [[germany-lka|LKA Saxony]]), Japan (Ministry of Justice), Malta, the Netherlands ([[netherlands-politie|Dutch National Police]]), Nigeria ([[nigeria-efcc|EFCC]]), Romania ([[romania-police|Romanian National Police]]) and the United States — eleven countries in total counting the U.S.

> [!note] Translation note
> Source documents are entirely in English; the term "Remote Access Trojan (RAT)" is preserved as the English term of art used uniformly by AFP, DOJ, and EC3.

## Background

According to the DOJ charging documents:

- Daniel Meli, of Zabbar, Malta, "since at least 2012" offered malware products and services for sale to cybercriminals through online computer-hacking forums. He allegedly assisted cybercriminals seeking to use RATs and offered teaching tools for sale, including an eBook. He sold the Warzone RAT and previously the "Pegasus RAT" through an online criminal organization called "Skynet-Corporation," and provided online customer support to purchasers of both RATs.
- Prince Onyeoziri Odinakachi, between June 2019 and no earlier than March 2023, "provided online customer support to individuals who purchased and used the Warzone RAT malware."
- The AFP states it identified Warzone as an emerging cyber threat in 2020, when the AFP Cyber Command "assisted in the identification of persons of interest and the coordination of intelligence related to the criminal network."

Warzone was distributed via deceptive email attachments and links to seemingly legitimate websites where users would download the software. Capabilities documented in DOJ filings and AFP release: bypass security; remote computer access; browse file systems; take screenshots; record keystrokes; steal usernames and passwords; access webcams. AFP additionally notes that Warzone "enabled other criminal activities such as ransomware attacks and harvesting of information that could lead to identity theft and phishing campaigns."

Subscription pricing as low as **AUD $25 / month** (AFP) / **USD $25 / month** (DOJ filings).

## Participating Parties

**Lead investigative agencies (U.S.):** [[fbi-cyber-division|FBI Cyber Division]] via the [[fbi|FBI]] Boston Field Office and Atlanta Field Office; investigation prosecuted by AUSAs Bethany L. Rupert and Michael Herskowitz (N.D. Ga., Meli) and AUSA James R. Drabick (D. Mass., Odinakachi); seizure warrants obtained by AUSAs James R. Drabick and Carol E. Head (D. Mass.).

**Lead investigative agency (Australia):** [[australia-afp|AFP]] Cyber Command; AFP International Network coordinated intelligence sharing.

**Coordinating body:** [[europol-ec3|Europol European Cybercrime Centre (EC3)]].

**Justice/extradition coordination:** [[us-doj|U.S. Department of Justice]] Criminal Division and [[office-of-international-affairs|Office of International Affairs]].

**Arresting authorities:**
- Malta — Malta Police Force; Office of the Attorney General of Malta; Malta Ministry for Justice. (No dedicated wikilink for Malta Police Force exists in this wiki yet; relationship to the [[malta|Malta]] country profile is captured in the [[malta|country page]] for now and a Malta Police Force entity page may be created in a future iteration.)
- Nigeria — Port Harcourt Zonal Command of [[nigeria-efcc|Nigeria's Economic and Financial Crimes Commission]].

**Technical assistance with infrastructure (per DOJ):**
- [[canada-rcmp|Royal Canadian Mounted Police]] (Canada)
- Croatian Ministry of the Interior Criminal Police Directorate (Croatia — no dedicated wiki entity page yet; recorded in this prose pending future stub)
- [[finland-nbi|Finland's National Bureau of Investigation]] (Finland)
- State Police Force of Saxony (Germany) — represented as [[germany-lka|Germany LKA]] (Saxony LKA in particular; the German federal-state structure means each Land has its own LKA)
- [[netherlands-politie|Dutch National Police]] (Netherlands)
- Japan Ministry of Justice (Japan — represented in prose as a justice ministry; the operational analogue [[japan-npa|Japan NPA]] / [[japan-jc3|JC3]] are the cybercrime-execution counterparts though DOJ specifically credits the Ministry of Justice for MLAT-type coordination)
- [[romania-police|Romanian National Police]] (Romania)

## Legal Framework

- **U.S. statutes (charging instrument):** Computer Fraud and Abuse Act ([[computer-fraud-and-abuse-act]]) — counts include conspiracy, obtaining authorized access to protected computers to obtain information, illegally selling and advertising an interception device, and causing unauthorized damage to protected computers. Maximum sentences range from 5 to 10 years per count, plus supervised release and fines.
- **International cooperation legal basis:** [[mlat-process|MLAT process]] generally; for U.S.-Australia intelligence cooperation see [[us-australia-mlat]]. For non-EU partners (Malta, Nigeria), DOJ Office of International Affairs coordinated MLAT/extradition channels. The United States is seeking the extradition of Meli from Malta to the Northern District of Georgia.
- **Convention basis:** [[budapest-convention|Budapest Convention on Cybercrime]] — Malta, Australia, Canada, Croatia, Finland, Germany, Japan, the Netherlands, Romania, and the United States are all parties; Nigeria is not (as of 2024). The Convention was likely the soft framework underpinning preservation/production cooperation among the European parties (Article 23–35), although neither the AFP nor DOJ release explicitly cites article numbers.

## Operational Timeline

- **2012**: According to U.S. charging documents, Daniel Meli begins selling RAT-family malware (Pegasus RAT, then Warzone RAT) on hacking forums.
- **2018–2020**: Warzone RAT becomes widely subscribed-to (typical contemporaneous threat-intel reporting; corroborated by AFP statement that the AFP "identified Warzone as an emerging cyber threat in 2020").
- **2020**: AFP Cyber Command identifies Warzone as an emerging cyber threat; AFP begins assisting in identification of persons of interest and intelligence coordination with international partners.
- **June 2019 – March 2023**: Per DOJ charging document, Odinakachi provides online customer support to Warzone RAT users.
- **12 December 2023**: Federal grand jury in N.D. Georgia returns indictment against Daniel Meli (four offenses).
- **30 January 2024**: Federal grand jury in D. Massachusetts returns indictment against Prince Onyeoziri Odinakachi (conspiracy to commit multiple computer intrusion offenses).
- **7 February 2024**: Coordinated arrests — Meli arrested in Malta by Malta Police Force at the request of the United States, with support from Office of the Attorney General of Malta, FBI, and DOJ. Meli makes initial appearance before a Magistrate Judge in Valletta. Odinakachi arrested in Nigeria by Port Harcourt Zonal Command of EFCC.
- **9 February 2024**: DOJ Press Release 24-163 announces domain seizures (`warzone.ws` plus three related domains) and unsealing of both indictments. FBI launches victim portal at `https://wzvictims.ic3.gov`.
- **13 February 2024**: AFP issues media release crediting the AFP Cyber Command and the AFP International Network for intelligence and partner coordination with Europol and FBI.

## Results and Impact

- **2 arrests** (Meli in Malta; Odinakachi in Nigeria), both on 7 February 2024.
- **2 federal indictments unsealed** (N.D. Ga. and D. Mass.).
- **4 internet domains seized** by federal authorities in Boston (D. Mass.): `warzone.ws` and three related domains.
- **Malware-as-a-service infrastructure dismantled**: AFP states "the joint operation also targeted the infrastructure of the network, shutting down sites and host servers to limit the software being used by more cyber criminals in the future."
- **Customer data preserved for follow-up**: AFP notes "police had gained a substantial amount of data in the lead up to the arrest, including about those who had previously purchased the Warzone software," and that follow-up investigation with Europol and FBI will continue.
- **Victim reporting**: FBI launched `wzvictims.ic3.gov` (DOJ).

> [!warning] Legal status check needed
> Extradition of Meli to the United States was sought as of 9 February 2024 but the AFP/DOJ releases do not record the extradition outcome. This page should be revisited when the extradition decision and any subsequent plea or trial outcome are reported by tier-1 sources.

## Cooperation Mechanisms Used

- **Europol coordination ([[europol-ec3|EC3]])** — DOJ states the international effort was "coordinated with international partners in large part through Europol." This corresponds to the EC3 case-coordination model rather than a formal Joint Investigation Team. ([[europol-jit]] is *not* mentioned in either release.)
- **DOJ Office of International Affairs** ([[office-of-international-affairs]]) — "provided substantial assistance during the investigation" (DOJ).
- **Bilateral law-enforcement-to-law-enforcement intelligence sharing** — AFP-FBI ("AFP International Network with partners like Europol and the FBI"); FBI-Malta Police; FBI-EFCC.
- **[[domain-seizure|Domain seizure]]** under D. Mass. court orders (warzone.ws + 3).
- **[[extradition]]** request from the United States to Malta for Meli.
- **[[mlat-process|MLAT-type judicial cooperation]]** for evidence and arrests in Malta and Nigeria, both non-EU jurisdictions reached via DOJ OIA channels rather than EIO ([[european-investigation-order]] would not apply outside the EU).

## Challenges and Friction Points

- **Extradition**: Sought from Malta but not yet confirmed in tier-1 sources at the time of this page's creation.
- **Jurisdictional fragmentation of customer base**: AFP indicates "those who had previously purchased the Warzone software" are dispersed worldwide. Effective enforcement against thousands of subscribers is a multi-year proposition; comparable to follow-on enforcement after the [[imminent-monitor-rat-takedown|Imminent Monitor RAT takedown]] (2019) and the [[fin7-takedown|FIN7 actions]].
- **Multi-jurisdiction prosecutorial split**: Two separate U.S. districts (N.D. Ga. for the seller; D. Mass. for a customer-support actor and for the domain seizures) reflects the difficulty of consolidating cybercrime cases when conduct, victims, and defendants are spread across the U.S.

## Lessons Learned

- AFP threat-identification at the intelligence stage (2020) was the trigger for the eventual U.S. prosecutorial case. International cyber-threat intelligence pipelines (AFP → FBI / EC3) can convert technical-threat reporting into criminal charges over a 3–4 year horizon.
- Coordinated same-day arrests across non-EU jurisdictions (Malta + Nigeria, 7 February 2024) are achievable via DOJ Office of International Affairs and Europol coordination even where neither defendant is in an EU member state.
- Domain seizure preceded arrest announcement by 2 days (DOJ release 9 Feb; AFP release 13 Feb), a typical sequencing for malware-as-a-service takedowns.

## Follow-Up Actions

- Track Meli extradition outcome (Malta → U.S.).
- Track Odinakachi U.S. extradition / trial proceedings.
- Track follow-on enforcement against Warzone RAT *customers* (AFP and DOJ both signaled this is a continuing investigation).
- Build a Malta Police Force organization page (currently absent) and a Croatian Ministry of the Interior Criminal Police Directorate stub if a future operation requires it.

## Korean Involvement (한국의 참여)

No Korean agency is named in either the AFP or DOJ press release among acknowledged law-enforcement partners. South Korea is a Budapest Convention invitee but not a party as of the operation date; routine RAT-takedown cooperation with Korea typically flows through Korean National Police Agency cyber bureau ([[knpa-cyber-bureau]]) and KISA ([[kisa]]) on a bilateral or [[interpol-i24-7|INTERPOL I-24/7]] basis rather than via Europol's EC3.

> [!note] Korean perspective gap
> If subsequent reporting (DOJ superseding indictment, FBI follow-on victim notifications, or AFP secondary actions) confirms Korean victims of Warzone RAT or Korean follow-on enforcement against subscribers, this section should be expanded.

## Contradictions & Open Questions

- The AFP release (13 February 2024) describes the operation as "joint" between AFP, Europol, and FBI, with the Maltese arrest credited to the Malta Police Force "following intelligence provided by the AFP." The DOJ release (9 February 2024) describes the international effort as "led by FBI special agents in Boston and Atlanta and coordinated with international partners in large part through Europol," and credits the Malta arrest to "a coordinated operation by the Malta Police Force and the Office of the Attorney General of Malta, with the support of the FBI and Justice Department," without explicitly naming the AFP as the source of intelligence. **Assessment**: the two narratives are *complementary* rather than contradictory — AFP emphasizes its own Cyber Command 2020 threat identification as the upstream intelligence, while DOJ emphasizes FBI's downstream prosecutorial leadership.
- DOJ acknowledges "Japan Ministry of Justice" but not Japan's National Police Agency. The wiki has [[japan-npa]] and [[japan-jc3]] entity pages but no Ministry-of-Justice org page; the participating-agencies frontmatter therefore does not list a Japan entity (the country [[japan]] remains in `participating_countries`). A Japan Ministry of Justice organization page may be warranted in a future iteration.
- DOJ specifically credits the **State Police Force of Saxony** (a Land-level LKA), not the federal [[germany-bka|BKA]]. The participating-agencies frontmatter therefore links to [[germany-lka|Germany LKA]] generally; a Saxony-specific LKA stub may be warranted if subsequent operations also implicate Saxony LKA.
- "Pegasus RAT" mentioned in DOJ charging documents as a predecessor to Warzone (sold by Meli through "Skynet-Corporation") is unrelated to the NSO Group commercial spyware product also called Pegasus.
