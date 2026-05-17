---
type: operation
title: "LeakBase Hacker-Forum Takedown (2026)"
title_ko: "LeakBase 해커 포럼 단속 (2026)"
aliases:
  - "LeakBase takedown"
  - "LeakBase seizure"
case_id: CYB-2026-009
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - search-seizure
  - arrest
  - online-content-takedown
outcome: success
timeframe:
  announced: 2026-03-04
  start: 2026-03-03
  end: 2026-03-04
  ongoing: false
crime_type: "[[cybercrime-forum-ic]]"
crime_types:
  - "[[cybercrime-forum-ic]]"
  - "[[hacking-ic]]"
  - "[[online-fraud-ic]]"
target_entity: "LeakBase — open-web English-language forum for trading stolen data, account credentials, and cybercrime tools (142,000+ members; 215,000+ messages per unsealed affidavit)"
lead_agency: "[[fbi]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-states]]"
  - "[[australia]]"
  - "[[belgium]]"
  - "[[poland]]"
  - "[[portugal]]"
  - "[[romania]]"
  - "[[spain]]"
  - "[[united-kingdom]]"
  - "[[canada]]"
  - "[[germany]]"
  - "[[greece]]"
  - "[[kosovo]]"
  - "[[malaysia]]"
  - "[[netherlands]]"
participating_agencies:
  - "[[fbi]]"
  - "[[europol-ec3]]"
  - "[[us-doj]]"
  - "[[office-of-international-affairs]]"
organizations:
  - "[[fbi]]"
  - "[[europol-ec3]]"
  - "[[us-doj]]"
  - "[[office-of-international-affairs]]"
mechanisms_used:
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[eurojust-coordination-meeting]]"
legal_basis:

results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 2
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Forum data seized; LeakBase database (over 142,000 members, over 215,000 messages) shut down"
    - "Two LeakBase domains seized and replaced with seizure banners"
    - "Prevention messages sent to LeakBase members"
    - "Search warrants, arrests, and interviews executed in 8 countries (US, Australia, Belgium, Poland, Portugal, Romania, Spain, UK)"
    - "Investigative assistance provided by Canada, Germany, Greece, Kosovo, Malaysia, and the Netherlands"
    - "Synchronized 14-country action coordinated by Europol in The Hague on 2026-03-03 and 2026-03-04"
edges:
  - source_actor: fbi
    target_actor: europol-ec3
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: us-doj
    target_actor: europol-ec3
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - arrests
  - indictments
related_cases:
  - "[[us-v-kai-west-intelbroker-2025]]"
related_operations:
  - "[[xss-is-cybercrime-forum-takedown-2025]]"
  - "[[w3ll-phishing-kit-takedown-2026]]"
  - "[[tycoon-2fa-phishing-as-a-service-takedown-2026]]"
challenges_encountered:

lessons_learned:
  - "DOJ frames LeakBase as the latest in a sequence of large English-language hacker-forum takedowns — RaidForums (2022) and BreachForums (2023, founder convicted 2025) — suggesting the displacement-and-takedown cycle on the open-web cybercrime forum vertical is now an established US-led, Europol-coordinated pattern."
  - "Cooperation split between 'active enforcement' countries (8) and 'assistance' countries (6) is explicit in the cited tier-1 source and is captured in the body table as a non-uniform participation roster for SNA edge weighting."
source_count: 1
sources:
  - "[[2026-03-04_justice-gov_united-states-leads-dismantlement-leakbase-hacker-forum]]"
summary: "LeakBase, an open-web English-language forum that DOJ describes as one of the world's largest cybercriminal data-trading platforms (over 142,000 members, over 215,000 messages), was dismantled on 2026-03-03 and 2026-03-04 in a synchronized 14-country action coordinated by Europol in The Hague. The US lead was the FBI Salt Lake City Field Office, with prosecution by USAO-Utah and CCIPS, and the action follows the DOJ-led RaidForums (2022) and BreachForums (2023) takedowns."
created: 2026-05-08
updated: 2026-05-17
---
## Summary

On 2026-03-03 and 2026-03-04, law enforcement agents and officers in 14 countries took synchronized action against [[cybercrime-forum-ic|LeakBase]], an open-web English-language cybercriminal forum used to buy and sell stolen data and cybercrime tools. The action was coordinated by [[europol-ec3|Europol]] in The Hague. According to an affidavit unsealed on 2026-03-03, LeakBase had over 142,000 members and more than 215,000 messages, and an enormous, continuously updated archive of hacked databases including hundreds of millions of account credentials.

The United States and other countries shut down LeakBase, seized its data and two of the forum's domains, posted seizure banners on the LeakBase sites, sent prevention messages to LeakBase members, and collected additional evidence. The operation also executed search warrants, arrests, and interviews in eight of the participating jurisdictions.

## Background

### Modus operandi

LeakBase operated as an open-web, English-language cybercrime forum — i.e., it required no Tor browser, invitation, or special credentials to access — and structured its commerce around the resale of stolen-database content harvested from third-party breaches. Per the unsealed affidavit cited in the DOJ release, the forum maintained an enormous, continuously updated archive of hacked databases including hundreds of millions of account credentials. Forum users posted, sold, and traded:

- Credit and debit card numbers (carding inventory).
- Banking account numbers and routing information.
- Username/password pairs (which the DOJ explicitly notes can facilitate downstream account takeovers — i.e., credential-stuffing and ATO chains).
- Additional sensitive business and personally identifiable information sourced from US corporations and individuals.

The forum had over 142,000 registered members and over 215,000 messages at takedown. Two domain names were used to surface the marketplace on the open web; both were seized and replaced with seizure banners on 2026-03-03.

### Victim profile and impact

The unsealed affidavit characterizes the stolen-database archive as encompassing hundreds of millions of compromised account credentials — i.e., the proximate victim population is the credential holders behind those records, not the 142,000 forum members. The DOJ release explicitly names US corporations and US individuals as a source population for the stolen data trafficked through the forum, but does not quantify per-victim losses, total laundered proceeds, or aggregate fraud volume attributable to LeakBase listings.

### Financial flow

The cited tier-1 source does not describe a specific cryptocurrency, escrow, or payment-processor flow for LeakBase transactions, and the seizure announcement records no cryptocurrency-seizure figure. The forum-economy model is consistent with the pattern previously documented in DOJ-led RaidForums (2022) and BreachForums (2023) takedowns — peer-to-peer crypto and on-platform credit systems — but specific financial-flow detail for LeakBase is not disclosed in this release.

### Criminal organization structure

DOJ explicitly contextualizes LeakBase as the latest in a sequence of major English-language cybercrime-marketplace disruptions — RaidForums (2022) and BreachForums (2023, founder convicted and sentenced in 2025) — characterising the forum-takedown vertical as a recurring US-led, Europol-coordinated enforcement target with displacement-and-takedown dynamics across successor venues. The cited release does not name a founder, administrator, moderator team, or organisational hierarchy for LeakBase itself; per-country arrest counts were not disclosed and no defendants were named, although search warrants, arrests, and interviews were executed across eight active-enforcement jurisdictions (United States, Australia, Belgium, Poland, Portugal, Romania, Spain, United Kingdom).

## Participating Parties

| Role | Parties |
|---|---|
| US lead investigator | [[fbi\|FBI]] Salt Lake City Field Office |
| US prosecutorial line | US Attorney's Office for the District of Utah; Computer Crime and Intellectual Property Section ([[us-doj\|US DOJ]] Criminal Division) |
| US international cooperation channel | [[office-of-international-affairs\|US DOJ Office of International Affairs]] |
| Coordinating body | [[europol-ec3\|Europol]] in The Hague |
| Active-enforcement countries (search warrants, arrests, interviews) | [[united-states\|United States]], [[australia\|Australia]], [[belgium\|Belgium]], [[poland\|Poland]], [[portugal\|Portugal]], [[romania\|Romania]], [[spain\|Spain]], [[united-kingdom\|United Kingdom]] |
| Assistance countries (significant cooperation, no enforcement action named) | [[canada\|Canada]], [[germany\|Germany]], [[greece\|Greece]], [[kosovo\|Kosovo]], [[malaysia\|Malaysia]], [[netherlands\|Netherlands]] |
| US domestic task-force participants | FBI San Diego Field Office, Utah Department of Public Safety, Provo Police Department |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2026-03-03 | Affidavit unsealed; synchronized action begins | DOJ 2026-03-04 (PR 26-205) |
| 2026-03-04 | Synchronized action concludes; DOJ announces takedown publicly | DOJ 2026-03-04 (PR 26-205) |

## Results and Impact

- LeakBase database (140K+ members, 215K+ messages) shut down.
- Two domains used by the forum seized and replaced with seizure banners.
- Prevention messages sent to LeakBase members.
- Search warrants, arrests, and interviews executed in eight participating jurisdictions; the public release does not enumerate per-country arrest counts.
- The DOJ describes the takedown as one in a sequence of marketplace-disruption operations including [RaidForums (2022)] and [BreachForums (2023, with the founder convicted in 2025)].

## Cooperation Mechanisms Used

The cited tier-1 source describes the action as a "synchronized" action "coordinated" by Europol in The Hague — consistent with a [[eurojust-coordination-meeting|coordination meeting at the Hague]] pattern (recognizing that the cited release names Europol rather than Eurojust as the coordinating body) supporting parallel domestic enforcement actions in eight participating jurisdictions and intelligence/evidence-sharing assistance from six more. Domestic US enforcement was anchored by FBI Salt Lake City. The release does not name a specific MLAT, JIT, or extradition instrument; the legal-basis classification therefore follows the [[search-seizure|domestic search-and-seizure]] and [[domain-seizure|domain seizure]] instruments executed in each participating jurisdiction.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited DOJ release as either an active-enforcement or an assistance country. The case is included in the wiki for the 14-country US-led / Europol-coordinated cooperation pattern, the explicit lineage with prior DOJ-led English-language forum takedowns (RaidForums, BreachForums), and the credential-theft / stolen-data trading methodology, all of which are directly relevant to comparative analysis of Korean credential-theft and account-takeover IC posture tracked elsewhere in this wiki.

## Contradictions & Open Questions

- The two seized LeakBase domains are not named in the cited release.
- Per-country arrest counts are not described in the cited release; the public source attributes "search warrants, arrests, and interviews" collectively to the eight active-enforcement countries.
- The hosting infrastructure of LeakBase is not described in the cited DOJ release; secondary reporting (Malay Mail) attributes Malaysia-hosted servers to Malaysia's MACC, which would also explain Malaysia's inclusion in the assistance roster, but Malaysia's specific role is not described in the tier-1 DOJ source itself.
- No defendant or operator of LeakBase is named in the cited release; the founder/administrator's identity and any indictment under seal are not disclosed in this source.
- **L26 gap — financial flow**: the cited DOJ release does not disclose the specific cryptocurrency, escrow, or payment-channel mechanics used inside the LeakBase economy; aggregate proceeds and laundering pathways are not quantified.
- **L26 gap — victim quantification**: the cited DOJ release does not quantify per-victim losses or aggregate fraud volume traceable to LeakBase listings; the "hundreds of millions of account credentials" figure is the archive scale, not a downstream-loss figure.
- **L26 gap — OCG structure**: no LeakBase founder, administrator, or moderator hierarchy is named in the cited release; the takedown is described as forum-platform disruption rather than as the dismantling of an identified organised criminal group.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2026-03-04_justice-gov_united-states-leads-dismantlement-leakbase-hacker-forum\|United States Leads Dismantlement of One of the World's Largest Hacker Forums]] | US DOJ (OPA), Press Release 26-205 | 2026-03-04 | https://www.justice.gov/opa/pr/united-states-leads-dismantlement-one-worlds-largest-hacker-forums |
