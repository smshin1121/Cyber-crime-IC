---
type: operation
title: "AFP JPC3 - RMP - FBI myGov phishing-kit syndicate dismantling (Malaysia, November 2023)"
aliases:
  - "AFP eight arrests over phishing kits"
  - "Malaysian myGov phishing-kit syndicate (2023)"
  - "Borneo phishing-kit raid 2023"
case_id: ""
period: 2
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - seizure
outcome: success
timeframe:
  announced: 2023-11-27
  start: 2023-11-06
  end: 2023-11-06
  ongoing: false
crime_types:
  - "[[online-fraud-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[identity-theft]]"
  - "[[access-device-fraud]]"
crime_type: ""
target_entity: "Malaysia-based phishing-kit-as-a-service syndicate led by an alleged 35-year-old Malaysian national in Borneo. The syndicate developed and sold phishing kits replicating legitimate Government services in Australia (notably the myGov citizen-services portal), Malaysia and the United States, and was supported by money mules and dedicated server infrastructure hosted at a Malaysian technology park."
lead_agency: "[[malaysia-police]]"
coordinating_body: ""
participating_countries:
  - "[[australia]]"
  - "[[malaysia]]"
  - "[[united-states]]"
participating_agencies:
  - "[[australia-afp]]"
  - "[[malaysia-police]]"
  - "[[fbi-cyber-division]]"
legal_basis:
  []
mechanisms_used:
  - "[[informal-cooperation]]"
results:
  arrests: 8
  indictments: 0
  servers_seized: 4
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Power cables, monitors, modem and other networking equipment seized at the Malaysian technology park hosting site."
    - "60+ terabytes of data recovered across the suspect's Borneo residence and the technology-park raid, including usernames, passwords and cryptocurrency wallet seed phrases."
    - "Phishing-kit templates impersonating Australian Government myGov, Malaysian Government services, and US Government services."
edges:
  - source_actor: australia-afp
    target_actor: malaysia-police
    cooperation_type: info_sharing
    legal_basis: informal
    direction: directed
  - source_actor: fbi-cyber-division
    target_actor: malaysia-police
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: directed
  - source_actor: australia-afp
    target_actor: fbi-cyber-division
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 3.0
source_tier: 1
missing_fields:
  - legal_basis
  - case_id
  - victims_notified
related_cases:
  []
related_operations:
  - "[[gxc-team-googlexcoder-phishing-kits-takedown-2025]]"
  - "[[w3ll-phishing-kit-takedown-2026]]"
  - "[[labhost-phishing-as-a-service-takedown-2024]]"
  - "[[afp-usss-operation-wickham-changjiang-money-laundering-2023]]"
challenges_encountered:
  - "[[jurisdictional-conflicts]]"
lessons_learned:
  - "Tier-1 phishing-kit-as-a-service syndicates that target multiple Five-Eyes-aligned governments simultaneously create natural intelligence-sharing incentives across affected jurisdictions, even where formal MLA channels are not invoked."
  - "Hosting-infrastructure attribution by a third partner (here FBI) can convert two-country bilateral leads into trilateral pictures fast enough for action-day execution under domestic law in the host state."
source_count: 1
sources:
  - "[[2023-11-27_afp-gov-au_eight-arrests-malaysia-mygov-phishing-kits]]"
created: 2026-05-10
updated: 2026-05-10
---
> [!info] Provisional / source-thin
> This operation page is being seeded from a single tier-1 primary press release ([[2023-11-27_afp-gov-au_eight-arrests-malaysia-mygov-phishing-kits|AFP, 27 November 2023]]). It is below the preferred publication threshold of `source_count >= 5`. Treat the page as a stub-grade record pending corroborating primary statements from the Royal Malaysian Police (RMP / PDRM CCID) and the FBI before further enrichment.

## Summary

On 6 November 2023, the [[malaysia-police|Royal Malaysian Police (RMP / PDRM)]] arrested eight people in Malaysia following intelligence developed and shared by the [[australia-afp|Australian Federal Police]] through its Joint Policing Cybercrime Coordination Centre (JPC3). The intelligence identified an alleged 35-year-old Malaysian national in Borneo as the developer and seller of phishing kits replicating Government services in [[australia|Australia]] (notably the myGov citizen-services portal), [[malaysia|Malaysia]] and the [[united-states|United States]]. The kits were sold to other cybercriminals to harvest victim credentials at scale. The [[fbi-cyber-division|FBI]] separately linked the syndicate's hosting estate to organised crime, completing a trilateral intelligence picture before action day.

The 27 November 2023 AFP media release announcing the arrests represents the public record of the operation. No specific operation name is assigned by AFP. JPC3 is the AFP-led national unit that developed and pushed the intelligence to RMP; it is part of AFP and does not have a separate organisation page in this wiki at time of ingest.

> [!warning] Source-side asymmetry
> Public reporting in this wiki is anchored on the AFP statement. RMP / PDRM CCID's own primary statement on the arrests, charges and post-arrest proceedings has not yet been ingested, and FBI's underlying infrastructure-attribution product is not public. Numerical and procedural claims (8 arrests; 60+ TB; 4 servers) are AFP-attributed, not independently verified here.

## Background

Phishing kits are templated, ready-to-deploy clones of legitimate websites that allow other criminals to harvest credentials with minimal technical skill, and they have become a core layer of the cybercrime-as-a-service economy alongside other phishing-kit operations such as [[gxc-team-googlexcoder-phishing-kits-takedown-2025|GXC Team]], [[w3ll-phishing-kit-takedown-2026|W3LL]] and [[labhost-phishing-as-a-service-takedown-2024|LabHost]]. The Malaysian syndicate's choice to clone the Australian myGov portal — Australia's primary online entry point for Medicare, the Australian Taxation Office, Centrelink and similar services — placed it directly in AFP's strategic threat focus, with the AFP citing AUD 24.6 million in Australian phishing losses in calendar year 2022 as the harm baseline.

## Participating Parties

- **Lead enforcement (host state):** [[malaysia-police|Royal Malaysian Police (RMP / PDRM CCID)]] — executed arrests, search warrants and Malaysian-law charges.
- **Lead intelligence development (requesting partner):** [[australia-afp|Australian Federal Police]] through JPC3.
- **Third-country contribution:** [[fbi-cyber-division|FBI]] — hosting-infrastructure attribution linking the syndicate to organised crime.

## Legal Framework

The AFP release does not name a specific MLAT or treaty basis. Cooperation is described in informal-channel terms — intelligence pushed from JPC3 to RMP, supported by FBI infrastructure attribution, with arrests and searches executed under domestic Malaysian authority. Any formal mutual legal assistance traffic that may have followed (e.g., for FBI/AFP receipt of digital evidence from the Malaysian seizures) is not addressed in the public release.

## Operational Timeline

- **Pre-2023 — intelligence development:** AFP JPC3 identifies a Malaysian national advertising phishing kits cloning Australian, Malaysian and US Government services and shares the intelligence with RMP.
- **2023-11-06 — action day:** RMP executes simultaneous searches at the suspect's residence in Borneo and at a Malaysian technology park hosting his servers; eight people are arrested.
- **2023-11-27 — public announcement:** AFP publishes its media release on the operation, attributing the eight arrests, 60+ TB data recovery and four-server seizure to RMP enforcement supported by AFP and FBI intelligence.

## Results and Impact

- 8 arrests in Malaysia: 1 alleged primary developer/seller (35-year-old male) plus 7 alleged money mules.
- 4 servers and supporting networking equipment seized at the Malaysian technology park.
- 60+ terabytes of data recovered, including usernames, passwords and cryptocurrency wallet seed phrases.
- Phishing-kit templates targeting Australian Government myGov, Malaysian Government services and US Government services taken offline as a consequence of the arrests and seizures.

## Cooperation Mechanisms Used

- **[[informal-cooperation|Informal police-to-police cooperation]]:** AFP-to-RMP intelligence push through JPC3 and the AFP cybercrime liaison network; FBI hosting attribution shared in parallel. The AFP release does not invoke an MLAT or a formal treaty channel.

## Challenges and Friction Points

- **Jurisdictional limits:** The alleged developer, infrastructure and money mules were all in Malaysia, while the principal victim base sat across Australia and the United States. Disrupting the syndicate therefore depended entirely on Malaysian enforcement capacity and willingness to act on partner intelligence — a recurrent feature of [[jurisdictional-conflicts|jurisdictional-conflicts in cybercrime IC]].
- **Source-side opacity:** Without a public RMP statement, downstream tracking of charges, prosecutions and any sentences is constrained from open AFP material alone.

## Lessons Learned

- Multi-government targeting (myGov + Malaysian + US Government services) creates a self-reinforcing case for trilateral cooperation: each affected state has independent grounds to develop intelligence, and any one of them can become the lead intelligence partner for the host state.
- A well-resourced national cybercrime fusion centre (here JPC3) is decisive in converting platform-impersonation telemetry into actionable, host-state-ready intelligence.

## Follow-Up Actions

- Pending corroborating RMP / PDRM CCID primary statement.
- Pending public US-side product on the FBI hosting attribution.

## Korean Involvement (한국의 참여)

No Korean agency or victim base is identified in the AFP release. The case is relevant to Korean practice as a comparator for KNPA and KISA cooperation with ASEAN partners on Government-service phishing kits, but no direct Korean role is asserted.

## Contradictions & Open Questions

- The AFP release describes the suspect's residence in "Borneo" without specifying state (Sabah, Sarawak or Labuan) — Malaysian primary reporting, when ingested, should resolve this.
- Whether any of the eight arrestees have since been charged, tried or convicted under Malaysian law is not addressed in the AFP release and remains an open follow-up.
- Whether AFP or US authorities subsequently obtained digital evidence from the seizures via formal MLA — and under what framework — is not in the public AFP record.
