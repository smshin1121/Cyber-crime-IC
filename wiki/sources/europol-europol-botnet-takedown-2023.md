---
type: source
title: "Europol: Botnet taken down through international law enforcement cooperation (Ramnit, 2015)"
collection_url: "https://www.europol.europa.eu/media-press/newsroom/news/botnet-taken-down-through-international-law-enforcement-cooperation"
collection_domain: "europol.europa.eu"
source_type: "press-release"
publisher: "Europol"
publish_date: "2015-02-24"
ingest_date: "2026-04-08"
enriched_date: "2026-04-10"
language: "en"
reliability: "high"
credibility: "confirmed"
sensitivity: "public"
source_tier: 2
pages_updated:
  - "botnet-takedown-europol-2023"
key_findings:
  - "URL-TOPIC MISMATCH: The Europol URL currently linked to the 'Europol Botnet Takedown 2023' wiki operation is actually the 2015-02-24 press release on the Ramnit botnet takedown, NOT a 2023 action. The operation page title is misleading and should be corrected or the source reassigned"
  - "The actual article describes the 24 February 2015 takedown of the Ramnit botnet, which had infected ~3.2 million computers worldwide, led by the UK National Crime Agency with partner action in Germany, Italy and the Netherlands"
  - "Private-sector partners: Microsoft, Symantec and AnubisNetworks contributed technical analysis and sinkholing. Operations coordinated through Europol's Joint Cybercrime Action Taskforce (J-CAT) and EC3, with CERT-EU support"
  - "Technical action: Shutdown of command-and-control servers and redirection (sinkholing) of ~300 internet domain addresses used by the Ramnit botnet to issue instructions to infected machines"
  - "Malware capability: Ramnit enabled criminals to 'steal personal and banking information, namely passwords, and disable antivirus protection' on Windows systems — a classic banking-trojan profile"
  - "This is an important data-integrity correction — the operation page [[botnet-takedown-europol-2023]] appears to duplicate an existing [[ramnit-botnet-takedown]] case, or should be renamed and re-dated"
created: 2026-04-08
updated: 2026-04-10
---

> [!warning] Contradiction / data integrity issue
> The wiki operation page **[[botnet-takedown-europol-2023]]** records this source as evidence of a 2023 botnet takedown. However, the Europol URL and article content unambiguously describe the **2015-02-24 Ramnit botnet takedown** (led by UK NCA). The wiki operation page is *almost certainly* incorrectly dated or incorrectly scoped. Recommended actions: (a) re-date the operation to 2015-02-24, (b) rename to reference Ramnit, and (c) check for duplication with an existing Ramnit entry.

## Source

- **Publisher**: Europol (European Union Agency for Law Enforcement Cooperation)
- **URL**: <https://www.europol.europa.eu/media-press/newsroom/news/botnet-taken-down-through-international-law-enforcement-cooperation>
- **Published**: 2015-02-24
- **Source Tier**: 2 (official agency press release)
- **Reliability**: high (Europol primary source)
- **Credibility**: confirmed
- **Operations referenced**: [[botnet-takedown-europol-2023|Europol Botnet Takedown 2023 (MISMATCH — actual: Ramnit 2015)]]

## Summary

Europol's press release covers the **24 February 2015 Ramnit botnet takedown**, an international law enforcement operation led by the UK's National Crime Agency with participation from Germany, Italy and the Netherlands. Key points:

1. **Scale**: ~3.2 million computers infected worldwide
2. **Target**: Ramnit botnet (Windows banking trojan + remote access capability)
3. **Lead**: UK National Crime Agency (NCA)
4. **Partner agencies**: German Federal Police (BKA), Italian Postal and Communications Police, Dutch National High Tech Crime Unit
5. **Private sector**: Microsoft Digital Crimes Unit, Symantec, AnubisNetworks
6. **Coordinating bodies**: Europol EC3, J-CAT, CERT-EU
7. **Technical action**: C&C server shutdown + sinkholing of ~300 domain addresses

## Why this source matters

For the IC wiki this Europol release is an important **correction source** — it reveals that the [[botnet-takedown-europol-2023]] operation page is incorrectly scoped. It also independently documents the **2015 Ramnit takedown**, which is a significant Period 1 operation deserving its own page (or merge with any existing Ramnit entry).

Historically, Ramnit is notable as one of the first takedowns conducted through Europol's J-CAT framework (J-CAT was launched September 2014), making it an important precedent for EU-led multi-country botnet operations.

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| UK NCA press release 2015-02-24 | Lead agency role, sinkholing technical detail |
| Symantec blog 2015-02-25 | Technical botnet analysis, infection counts |
| Microsoft Digital Crimes Unit blog | Domain sinkholing involvement |
| BBC News 2015-02-24 | Mainstream coverage of the 3.2M figure |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Botnet taken down through international law enforcement cooperation | Europol | 2015-02-24 | https://www.europol.europa.eu/media-press/newsroom/news/botnet-taken-down-through-international-law-enforcement-cooperation |
| [2] | Ramnit botnet shut down by NCA and European cyber crime centre | UK NCA | 2015-02-24 | https://www.nationalcrimeagency.gov.uk/news/ramnit-botnet-shut-down-by-nca-and-european-cyber-crime-centre |
| [3] | Ramnit botnet takedown analysis | Symantec | 2015-02-25 | https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/ramnit-botnet |
