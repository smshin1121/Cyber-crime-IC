---
type: operation
title: "Operation Synergia III"
aliases:
  - "Synergia III"
case_id: CYB-2026-002
period: 3
operation_role: umbrella
parent_operation: ""
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - arrest
  - server-seizure
  - disruption
outcome: success
timeframe:
  announced: 2026-03-13
  start: 2025-07-18
  end: 2026-01-31
  ongoing: false
crime_type: "[[cybercrime-infrastructure-ic]]"
crime_types:
  - "[[cybercrime-infrastructure-ic]]"
  - "[[malware-ic]]"
  - "[[ransomware-ic]]"
  - "[[online-fraud-ic]]"
target_entity: "Phishing, malware, ransomware, romance-scam, and credit-card-fraud infrastructure"
lead_agency: "[[interpol-igci]]"
coordinating_body: "[[interpol-igci]]"
participating_countries:
  - "[[angola]]"
  - "[[argentina]]"
  - "[[austria]]"
  - "[[bangladesh]]"
  - "[[bolivia]]"
  - "[[bosnia-and-herzegovina]]"
  - "[[brazil]]"
  - "[[brunei]]"
  - "[[cameroon]]"
  - "[[colombia]]"
  - "[[democratic-republic-of-the-congo]]"
  - "[[france]]"
  - "[[gambia]]"
  - "[[georgia]]"
  - "[[greece]]"
  - "[[guyana]]"
  - "[[iceland]]"
  - "[[india]]"
  - "[[ireland]]"
  - "[[israel]]"
  - "[[japan]]"
  - "[[kazakhstan]]"
  - "[[kenya]]"
  - "[[latvia]]"
  - "[[macau]]"
  - "[[madagascar]]"
  - "[[malaysia]]"
  - "[[maldives]]"
  - "[[moldova]]"
  - "[[mongolia]]"
  - "[[nigeria]]"
  - "[[pakistan]]"
  - "[[paraguay]]"
  - "[[philippines]]"
  - "[[poland]]"
  - "[[singapore]]"
  - "[[south-africa]]"
  - "[[spain]]"
  - "[[sri-lanka]]"
  - "[[switzerland]]"
  - "[[tanzania]]"
  - "[[togo]]"
  - "[[turkey]]"
  - "[[uganda]]"
  - "[[ukraine]]"
  - "[[united-arab-emirates]]"
  - "[[united-kingdom]]"
  - "[[venezuela]]"
  - "[[zambia]]"
  - "[[zimbabwe]]"
jurisdictions:
  - "[[angola]]"
  - "[[argentina]]"
  - "[[austria]]"
  - "[[bangladesh]]"
  - "[[brazil]]"
  - "[[france]]"
  - "[[india]]"
  - "[[japan]]"
  - "[[kenya]]"
  - "[[macau]]"
  - "[[malaysia]]"
  - "[[nigeria]]"
  - "[[poland]]"
  - "[[singapore]]"
  - "[[south-africa]]"
  - "[[spain]]"
  - "[[switzerland]]"
  - "[[togo]]"
  - "[[ukraine]]"
  - "[[united-kingdom]]"
participating_agencies:
  - "[[interpol-igci]]"
  - "[[group-ib]]"
  - "[[trend-micro]]"
organizations:
  - "[[interpol-igci]]"
  - "[[group-ib]]"
  - "[[trend-micro]]"
mechanisms_used:
  - "[[public-private-cooperation]]"
  - "[[electronic-evidence]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "[[informal-cooperation]]"
results:
  arrests: 94
  indictments: 0
  servers_seized: 212
  domains_seized: 45000
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "More than 45,000 malicious IP addresses and servers taken down."
    - "Another 110 individuals remained under investigation."
    - "Macau authorities identified more than 33,000 phishing and fraudulent websites."
    - "Togo police arrested 10 suspects; Bangladesh police arrested 40 suspects."
credibility_index: 4.25
source_tier: 1
missing_fields:
related_cases:
related_operations:
  - "[[operation-synergia-ii]]"
  - "[[operation-secure-interpol]]"
challenges_encountered:
  - "INTERPOL's public release reports a 72-country coalition, but not every jurisdiction has a detailed public action breakdown."
lessons_learned:
  - "Large-scale infrastructure operations increasingly combine public-sector action with private-sector threat-intelligence packages."
source_count: 4
sources:
  - "[[2026-03-13_interpol_synergia-iii-45000-malicious-ip-addresses]]"
  - "[[2026-03-13_group-ib_interpol-operation-synergia-3]]"
  - "[[2026-03-16_helpnetsecurity_interpol-operation-synergia-iii-cybercrime-infrastructure-takedown]]"
  - "[[2026-03-13_cybernews_interpol-takes-down-45000-malicious-websites]]"
summary: "Operation Synergia III was an INTERPOL-coordinated global cybercrime infrastructure operation conducted from July 2025 to January 2026. It involved law enforcement from 72 countries and territories, took down more than 45,000 malicious IP addresses and servers, produced 94 arrests, and seized 212 electronic devices or servers."
created: 2026-05-06
updated: 2026-05-17
---
# Operation Synergia III

## Summary

Operation Synergia III was an INTERPOL-coordinated global operation targeting infrastructure used for phishing, malware, ransomware, romance scams, credit-card fraud, and related online fraud. The action ran from 18 July 2025 to 31 January 2026 and was publicly announced on 13 March 2026.

The operation is a successor to [[operation-synergia-ii]] and reflects a broader pattern of global infrastructure disruption where private-sector telemetry is converted into actionable leads for national law-enforcement teams.

## Background

### Modus operandi

Synergia III targeted the supporting infrastructure layer of multiple cybercrime business lines rather than a single threat actor or single malware family. The 45,000+ malicious IP addresses and servers identified hosted a heterogeneous mix of attacker assets: phishing kits and credential-harvesting pages, malware command-and-control nodes, ransomware staging and exfiltration servers, romance-scam and "pig-butchering" investment-scam web frontends, sextortion delivery infrastructure, loan-fraud and identity-theft storefronts, and credit-card-fraud cash-out sites. INTERPOL's release frames the targeted infrastructure as the *connective tissue* that allowed otherwise unrelated criminal groups to scale: phishing crews would rent the same bulletproof-hosting nodes that ransomware affiliates used, romance-scam operators reused account-takeover toolkits, and credit-card-fraud cash-out shops sat on overlapping IP ranges with malware C2. Group-IB, Trend Micro, and S2W contributed threat-intelligence feeds — IP reputation data, certificate-transparency anomaly signals, and active malware C2 inventories — which national LE units then validated and acted on through domestic legal process (server seizure, hosting-provider cooperation, suspect identification).

### Victim profile and impact

Victims spanned the full cybercrime victim spectrum because the targeted infrastructure was crime-type-agnostic. The INTERPOL release highlights named victim categories: targets of romance scams and account-hijacking schemes, sextortion victims, loan-scam victims, identity-theft victims, and credit-card-fraud victims. Macau alone identified 33,000+ phishing/fraudulent websites targeting consumers of regional financial-service brands. The 1.8 million-user-class headline is not provided for Synergia III (unlike a single-platform takedown), and INTERPOL does not publish a global victim-loss estimate for the operation. The impact is therefore measured in *infrastructure denial* — 45,000 malicious nodes removed from the active attack surface — rather than in a verified victim-restitution figure.

### Financial flow

No consolidated cryptocurrency seizure or asset-freeze figure was published for Synergia III. The crime types covered span both crypto-rail monetisation (ransomware payouts, crypto-investment scams) and fiat-rail monetisation (card-not-present fraud, loan scams, romance-scam wire transfers and gift cards). Group-IB's parallel release describes intelligence packages including financial-trail data, but specific seized-funds figures, beneficial-owner attribution, or money-mule arrests as part of Synergia III are not disclosed by INTERPOL. The operation's headline outcome is infrastructure removal and arrests, not asset recovery.

**Criminal organisation structure.** The 94 arrests and 110 additional individuals under investigation are split across 72 countries and territories, with public per-country breakdowns thin: Macau-led website identification, Togo with 10 arrests, and Bangladesh with 40 arrests are the named national highlights. The lack of a single named OCG or a hierarchy diagram reflects the operation's design — Synergia III was a *broad-sweep infrastructure operation* against an ecosystem of independently-operating criminal groups, not a takedown of one organised crime entity. The 94 suspects are therefore drawn from many distinct OCGs, ranging from solo operators to multi-cell phishing crews to organised romance-scam compounds. INTERPOL's release does not assert that the arrested individuals share command structure or that any subset constitutes a coherent named OCG.

## Cooperation Model

- **Global coordination:** INTERPOL coordinated law enforcement from 72 countries and territories.
- **Private-sector intelligence:** Group-IB, Trend Micro, and S2W supported the operation by tracking illegal cyber activity and identifying malicious infrastructure.
- **National actions:** Macau, Togo, and Bangladesh were publicly highlighted as national action examples, covering fraudulent websites, account-hijacking romance scams, sextortion, loan scams, identity theft, and credit-card fraud.

## Results and Impact

| Metric | Value |
|---|---:|
| Malicious IP addresses and servers taken down | 45,000+ |
| Arrests | 94 |
| Additional individuals under investigation | 110 |
| Electronic devices and servers seized | 212 |
| Phishing/fraudulent websites identified in Macau | 33,000+ |
| Participating countries and territories | 72 |

## Boundary and Non-Duplication Notes

This page records the 2025-2026 third Synergia operation and should not be merged into [[operation-synergia-ii]], which covered the separate April-August 2024 action.

## Contradictions & Open Questions

- **Per-country arrest distribution beyond Macau, Togo (10) and Bangladesh (40)** is not disclosed. The remaining 44 arrests across other participating jurisdictions are aggregated but not broken out.
- **Named OCGs or threat-actor attributions** for the 45,000+ malicious nodes are not published. The infrastructure is described as supporting phishing, malware, ransomware, romance scams, and credit-card fraud, but specific group attribution (e.g., which ransomware affiliates, which romance-scam compounds) is withheld.
- **Cryptocurrency seizure and fiat asset-freeze totals** are not provided. The headline metrics are infrastructure removal and arrests; financial-disruption metrics are absent.
- **Global victim-loss estimate** is not published. The operation is framed by infrastructure removed (45,000+) rather than verified victim harm — making cost-benefit comparison with single-platform takedowns (e.g., Operation Endgame) difficult.
- **Per-jurisdiction legal basis** for each national takedown action is not enumerated. The operation relied on informal cooperation and Interpol channels rather than a single shared legal instrument, but specific MLAT/EIO usage across the 72 jurisdictions is not documented publicly.
- **S2W contribution** is listed in INTERPOL's release alongside Group-IB and Trend Micro but is not currently captured in the participating_agencies frontmatter; it should be added when an S2W organisation stub is created.

## Evidence Notes

INTERPOL is the anchor source for scope and result figures. Group-IB confirms its contribution and repeats the 72-country, 94-arrest, 45,000-infrastructure, and 212-device/server figures. Help Net Security and Cybernews provide independent cybersecurity media confirmation.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 45,000 malicious IP addresses taken down in international cyber operation | INTERPOL | 2026-03-13 | https://www.interpol.int/News-and-Events/News/2026/45-000-malicious-IP-addresses-taken-down-in-international-cyber-operation |
| [2] | Group-IB Supports INTERPOL's Operation Synergia III, Contributing Intelligence to Global Cybercrime Takedown | Group-IB | 2026-03-13 | https://www.group-ib.com/media-center/press-releases/interpol-operation-synergia-3/ |
| [3] | 45,000 malicious IP addresses taken down, 94 suspects arrested | Help Net Security | 2026-03-16 | https://www.helpnetsecurity.com/2026/03/16/interpol-operation-synergia-iii-cybercrime-infrastructure-takedown/ |
| [4] | Interpol takes down 45,000 malicious websites in global cybercrime crackdown | Cybernews | 2026-03-13 | https://cybernews.com/news/interpol-takes-down-45000-malicious-websites/ |
