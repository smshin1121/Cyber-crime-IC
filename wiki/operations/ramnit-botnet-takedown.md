---
type: operation
title: "Ramnit Botnet Takedown"
aliases:
  - "Operation Ramnit"
case_id: CYB-2015-002
period: 1
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - seizure
outcome: success
timeframe:
  announced: 2015-02-24
  start: 2015-02
  end: 2015-02-24
  ongoing: false
crime_type: "[[malware-ic]]"
target_entity: "Ramnit botnet (banking trojan)"
lead_agency: "[[uk-nca|UK National Crime Agency]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-kingdom]]"
  - "[[germany]]"
  - "[[italy]]"
  - "[[netherlands]]"
participating_agencies:
  - "[[uk-nca|UK NCA]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[eurojust]]"
legal_basis:

mechanisms_used:
  - "[[j-cat|Joint Cybercrime Action Taskforce (J-CAT)]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 300
  cryptocurrency_seized: ""
  other:
    - "Command-and-control servers shut down"
    - "~300 domains sinkholed"
    - "3.2 million infected computers disrupted"
edges:
  - source_actor: "UK NCA"
    target_actor: "Europol EC3"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Microsoft
    target_actor: "UK NCA"
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: directed
  - source_actor: Symantec
    target_actor: "Europol EC3"
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: directed
credibility_index: 4.0
source_tier: 2
missing_fields:
  - legal_basis
  - arrests
source_count: 5
sources:
  - "[[europol-europol-botnet-takedown-2023]]"
  - "[[2015-10-22_microsoft_breaking-up-a-botnet-how-ramnit-was-foiled]]"
  - "[[2015-02-25_anubisnetworks_aids-europols-european-cybercrime-centre-in-takedown-of-malicious-botnet]]"
  - "[[2015-02-25_arstechnica_europol-cracks-down-on-botnet-infecting-3-2-million-computers]]"
  - "[[2015-02-25_pcworld_europol-and-security-vendors-disrupt-massive-ramnit-botnet]]"
created: 2026-04-08
updated: 2026-04-26
operation_role: umbrella
parent_operation: ""
summary: "On 24 February 2015, the **UK National Crime Agency (NCA)** led a multinational operation to take down the **Ramnit botnet**, which had infected approximately **3.2 million computers worldwide**. The operation was coordinated through [[europol-ec3|Europol's European Cybercrime Centre (EC3)]] and the [[j-cat|Joint Cybercrime Action Taskforce (J-CAT)]], with law enforcement participation from [[germany]], [[italy]], and the [[netherlands]]."
jurisdictions:
  - "[[united-kingdom]]"
  - "[[germany]]"
  - "[[italy]]"
  - "[[netherlands]]"
organizations:
  - "[[uk-nca|UK National Crime Agency]]"
  - "[[europol-ec3]]"
  - "[[uk-nca|UK NCA]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[eurojust]]"
crime_types:
  - "[[malware-ic]]"
---
> [!info] Page corrected (2026-04-10)
> This page was originally filed as "Europol Botnet Takedown 2023" (`botnet-takedown-europol-2023.md`). Content verification of the Europol source URL confirmed this is actually the **February 2015 Ramnit botnet takedown**. Page renamed and all data corrected.

## Summary

On 24 February 2015, the **UK National Crime Agency (NCA)** led a multinational operation to take down the **Ramnit botnet**, which had infected approximately **3.2 million computers worldwide**. The operation was coordinated through [[europol-ec3|Europol's European Cybercrime Centre (EC3)]] and the [[j-cat|Joint Cybercrime Action Taskforce (J-CAT)]], with law enforcement participation from [[germany]], [[italy]], and the [[netherlands]].

The Ramnit malware was a banking trojan that enabled criminals to steal personal and banking information, including passwords, and disable antivirus protection on infected Windows systems.

## Background

Ramnit was first identified around 2010 and evolved from a simple file infector into a full-featured banking trojan. By 2015 it had become one of the most prevalent botnets globally, with an estimated 3.2 million infections. The malware spread through social engineering attacks, typically via links in spam emails or redirects to exploit kits.

## Participating Parties

**Lead Agency**: [[uk-nca|UK National Crime Agency]]

**Law Enforcement (4 countries)**:
- [[united-kingdom]] — NCA (lead)
- [[germany]] — BKA
- [[italy]] — Italian law enforcement
- [[netherlands]] — Dutch National High Tech Crime Unit (NHTCU)

**Coordination**: [[europol-ec3|Europol EC3]], [[eurojust]], [[j-cat|J-CAT]], CERT-EU

**Private Sector Partners**:
- Microsoft — technical analysis
- Symantec — malware research and sinkholing
- AnubisNetworks — domain intelligence

## Operational Timeline

| Date | Event |
|---|---|
| ~2010 | Ramnit first observed as file infector |
| 2012-2014 | Evolution into banking trojan; infections reach millions |
| 2015-02-24 | Coordinated takedown: C&C servers shut down, ~300 domains sinkholed |
| 2015-02-24 | Europol public announcement |

## Results and Impact

- **~300 internet domain addresses** seized/sinkholed — redirected from criminal C&C to law enforcement sinkholes
- **Command-and-control servers** shut down across participating countries
- **3.2 million infected computers** disrupted from receiving criminal instructions
- **No arrests** were publicly announced as part of this operation

## Cooperation Mechanisms Used

- [[j-cat|Joint Cybercrime Action Taskforce (J-CAT)]] — operational coordination hub at Europol
- [[europol-ec3|Europol EC3]] — analytical and coordination support
- **Public-private partnership**: Microsoft, Symantec, and AnubisNetworks provided technical intelligence and sinkhole infrastructure

## Lessons Learned

1. **Sinkholing as primary disruption**: Without arrests, the operation relied on infrastructure seizure — effective for disruption but leaving operators free to rebuild
2. **J-CAT coordination model**: Ramnit was an early showcase of J-CAT's ability to coordinate multi-country botnet takedowns from The Hague
3. **PPP (public-private partnership)**: Microsoft and Symantec's intelligence was essential — law enforcement alone lacked the technical visibility

## Korean Involvement (한국의 참여)

No known Korean involvement in this operation. However, Ramnit infections were reported in South Korea, and [[south-korea]] was among the 190+ countries with affected systems.

## Contradictions & Open Questions

- **No arrests**: Despite the scale (3.2M infections), no operators were publicly charged. Whether subsequent investigations led to arrests is unclear.
- **Ramnit resurgence**: Security researchers reported Ramnit activity resuming within months of the takedown, raising questions about the long-term effectiveness of infrastructure-only disruption.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2015-02-24: Europol: Botnet taken down through international law enforcement cooperation (Ramnit, 2015).
- Microsoft, 2015-10-22: Breaking Up a Botnet - How Ramnit was Foiled.
- AnubisNetworks, 2015-02-25: AnubisNetworks Aids Europol’s European Cybercrime Centre in Takedown of Malicious Botnet.
- Ars Technica, 2015-02-25: Europol cracks down on botnet infecting 3.2 million computers.
- PCWorld, 2015-02-25: Europol and security vendors disrupt massive Ramnit botnet.

## Legal and Procedural Posture

- Recorded crime classification: malware.
- Recorded enforcement posture: Takedown and Seizure.
- The record is categorized as takedown with status completed.

## Evidence and Attribution Notes

- The operation page title is misleading and should be corrected or the source reassigned
- The actual article describes the 24 February 2015 takedown of the Ramnit botnet, which had infected ~3.2 million computers worldwide, led by the UK National Crime Agency with partner action in Germany, Italy and the Netherlands
- Private-sector partners: Microsoft, Symantec and AnubisNetworks contributed technical analysis and sinkholing.
- Operations coordinated through Europol's Joint Cybercrime Action Taskforce (J-CAT) and EC3, with CERT-EU support
- Technical action: Shutdown of command-and-control servers and redirection (sinkholing) of ~300 internet domain addresses used by the Ramnit botnet to issue instructions to infected machines
- Malware capability: Ramnit enabled criminals to 'steal personal and banking information, namely passwords, and disable antivirus protection' on Windows systems — a classic banking-trojan profile
- This is an important data-integrity correction — the operation page was renamed from botnet-takedown-europol-2023 to Ramnit Botnet Takedown after verifying the source describes the 2015 Ramnit takedown

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol: Botnet taken down through international law enforcement cooperation (Ramnit, 2015) | Europol | 2015-02-24 | https://www.europol.europa.eu/media-press/newsroom/news/botnet-taken-down-through-international-law-enforcement-cooperation |
| [2] | Breaking Up a Botnet - How Ramnit was Foiled | Microsoft | 2015-10-22 | https://blogs.microsoft.com/eupolicy/2015/10/22/breaking-up-a-botnet-how-ramnit-was-foiled/ |
| [3] | AnubisNetworks Aids Europol’s European Cybercrime Centre in Takedown of Malicious Botnet | AnubisNetworks | 2015-02-25 | https://www.anubisnetworks.com/news/community/news/anubisnetworks-aids-europols-european-cybercrime-centre-in-takedown-of-malicious-botnet |
| [4] | Europol cracks down on botnet infecting 3.2 million computers | Ars Technica | 2015-02-25 | https://arstechnica.com/tech-policy/2015/02/europol-cracks-down-on-botnet-infecting-3-2-million-computers/ |
| [5] | Europol and security vendors disrupt massive Ramnit botnet | PCWorld | 2015-02-25 | https://www.pcworld.com/article/432079/europol-and-security-vendors-disrupt-massive-ramnit-botnet.html |
