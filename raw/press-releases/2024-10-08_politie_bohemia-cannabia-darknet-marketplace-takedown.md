# International action against world's largest darkweb market 'Bohemia/Cannabia'

**Source URL (primary, Cloudflare-blocked to WebFetch — verified via WebSearch + tier-2 mirrors):**
https://www.politie.nl/nieuws/2024/oktober/8/11-internationale-actie-tegen-werelds-grootste-darkweb-markt-bohemia-cannabia.html

**Publish date:** 2024-10-08 (Politie press release; English-language coverage 2024-10-09)
**Outlet / authority:** Politie (Dutch National Police) — National Investigation and Intervention Unit, Team High Tech Crime (THTC)
**Language of original:** Dutch (nl-NL)

> [!note] Fetch note
> The politie.nl URL returns HTTP 403 to WebFetch (per LESSONS.md L11/L13: Politie/coe.int/government sites are routinely behind Cloudflare bot protection — page is reachable in browser). Content here is reconstructed from:
> - WebSearch summary of politie.nl page (returned by Google index of the original URL)
> - The Record (Recorded Future) — 2024-10-09 — `https://therecord.media/bohemia-cannabia-dark-web-market-arrests`
> - BleepingComputer — 2024-10-09 — `https://www.bleepingcomputer.com/news/legal/dutch-police-arrest-admin-of-bohemia-cannabia-dark-web-market/`
> - The Register — 2024-10-10 — `https://www.theregister.com/2024/10/10/cannabia_bohemia_darkweb_market_investigation/`
>
> All four sources independently corroborate the same core facts (June 27 arrest at Schiphol, second arrest in Ireland, EUR 8M+ crypto, EUR 12M peak monthly turnover Sep 2023, 82,000 daily ads, 67,000 monthly transactions, partners NL+IE+UK+US, investigation start late 2022).

---

## Summary (English reconstruction from primary + tier-2 sources)

The Dutch National Police (Politie), led by the Team High Tech Crime (THTC) within the National Investigation and Intervention Unit, announced on 8 October 2024 the takedown of "Bohemia / Cannabia" — described by the Politie as the largest and longest-running darkweb marketplace ever encountered by police. The market sold illegal goods including drugs as well as cybercrime services such as malware and DDoS-for-hire.

The investigation began towards the end of 2022 and was conducted in collaboration with law enforcement in Ireland, the United Kingdom and the United States. The marketplace itself went offline at the end of 2023 following an alleged exit scam by its operators, who reportedly became aware of the police investigation.

## Arrests

- **27 June 2024** — Schiphol Airport, Amsterdam: a 20-year-old British national, identified by Politie as one of the administrators of Bohemia/Cannabia, was arrested. Electronic devices containing incriminating data and access keys to Bitcoin wallets were seized at the time of arrest. The suspect appeared before the Rotterdam court; proceedings remain in early pre-trial phases.
- **August 2024** — Ireland: a second administrator, reported in tier-2 coverage as Kevin Daniel Andrei, a 23-year-old Irish national, was arrested by Irish authorities (An Garda Síochána / Garda National Cyber Crime Bureau).

The Politie statement indicates further arrests are anticipated as analysis of seized infrastructure continues.

## Seizures

- **Cryptocurrency**: more than EUR 8 million (approx. USD 8.75 million) in virtual assets seized from the two arrested administrators (combined).
- **Servers**: multiple servers — database server, crypto server, and webserver — most located in the Netherlands. All are now under Politie control. Politie statement (verbatim, via The Record): *"All data from the database server, crypto server and webserver have been seized and will be used for further investigation."*
- **Devices**: electronic devices and Bitcoin wallet access keys recovered at Schiphol.

## Marketplace metrics (per Politie)

- Approximately **82,000 advertisements per day** worldwide.
- Approximately **67,000 transactions per month**.
- **September 2023 peak monthly turnover: EUR 12 million** (the highest figure recorded; described as the largest monthly turnover ever observed on a darkweb marketplace by Dutch police).
- Estimated administrator earnings prior to exit scam: **EUR 5 million**.
- Dutch sellers' share: at least **14,000 transactions** with combined value of approximately **EUR 1.7 million** were attributed to sellers shipping from the Netherlands.

## Cooperation partners (explicitly named in primary statement)

| Country | Agency / Role |
|---|---|
| Netherlands | Politie — Team High Tech Crime (THTC), National Investigation and Intervention Unit. Lead. |
| Netherlands | Openbaar Ministerie (OM) — public prosecution; Rotterdam court forum. |
| Ireland | An Garda Síochána (Garda National Cyber Crime Bureau implied via tier-2 coverage). |
| United Kingdom | National Crime Agency (NCA) — referenced in tier-2 coverage of the Politie statement. |
| United States | "U.S. law enforcement" — partner. The Record specifically references the U.S. Department of Justice; not all secondary sources independently confirm a specific U.S. agency. |

> [!warning] Source coverage divergence
> One tier-2 source (The Record, 2024-10-09) listed Germany's Bundeskriminalamt (BKA) among partners. This is **not** corroborated by other tier-2 sources (BleepingComputer, The Register) that summarised the same Politie statement, nor surfaced in WebSearch excerpts of the politie.nl page. Until the primary Politie/Eurojust release is fetched directly, **Germany / BKA is NOT asserted as a participant** on the operation page (per LESSONS.md L17 and L19: tier-1 explicit naming required).

## Eurojust / Europol

The October 2024 Politie press release (per available WebSearch and tier-2 coverage) does not explicitly cite Eurojust coordination meetings or a formal Joint Investigation Team (JIT) for the Bohemia/Cannabia operation itself. A separate, related Europol-coordinated action — **Operation RapTor** — was referenced by Politie in a follow-on May 2025 statement as the umbrella for buyer/seller arrests using data extracted from the seized Bohemia infrastructure. Operation RapTor included Europol coordination and additional countries (US, UK, Brazil, Austria, Spain, Germany, France, Switzerland) but is a downstream operation distinct from the original Bohemia takedown.

> [!note] Coordinating-body uncertainty
> Until the primary politie.nl statement and any matching Eurojust release are fetched directly, the operation page conservatively records **no formal coordinating body** for the original takedown and treats Operation RapTor as a downstream, separately-coded operation.

## Key quotes (verbatim, via tier-2)

- **Stan Duijf**, head of operations unit, National Investigation and Intervention Unit (Politie), via The Register (2024-10-10): *"By conducting criminal investigations and prosecuting these criminals, it becomes clear that the dark web is not at all as anonymous as users may think."*
- **Politie statement** (via The Record): *"All data from the database server, crypto server and webserver have been seized and will be used for further investigation."*

## Legal framework

No specific treaty (Budapest Convention, etc.) is explicitly cited in the public Politie statement reproduced in tier-2 coverage. The cooperation appears to have proceeded on standard NL–IE–UK–US bilateral and informal police channels plus Dutch criminal procedure for the Schiphol arrest and the Rotterdam prosecution.

## Source-mismatch and verification audit

- Primary URL (politie.nl) HTTP 403 to WebFetch — Cloudflare bot protection, browser-accessible. Cross-checked via three independent tier-2 outlets and one WebSearch index excerpt; all agree on the core facts above. Per L11 / L20, additional fetches with TLS impersonation can be attempted later via `tools/web_verify_tls.py`.
- Date of public announcement: 2024-10-08 (Politie press release). The 2024-06-27 date in the original task brief refers to the Schiphol arrest itself, not the public release.
- Marketplace name: dual market — Bohemia + Cannabia (sister market under common administration). Operation page records both.
- Participating countries: only NL + IE + UK + US asserted (verified). Germany not asserted absent tier-1 confirmation.

---

## Raw fetch attempts log

```
2026-05-09 ingest by ingest agent
- WebFetch politie.nl/en/news/2024/june/27/...    -> HTTP 403
- WebFetch eurojust.europa.eu/.../bohemia        -> HTTP 404 (URL doesn't exist; Eurojust did not appear to issue a release)
- WebFetch europol.europa.eu/.../bohemia          -> HTTP 404 (Europol did not appear to issue a release)
- WebFetch politie.nl/nieuws/2024/oktober/8/...  -> HTTP 403 (Cloudflare; URL exists per WebSearch index)
- WebFetch web.archive.org/.../politie.nl/...    -> "Claude Code is unable to fetch from web.archive.org"
- WebFetch therecord.media/bohemia-cannabia...    -> 200 OK, full content
- WebFetch bleepingcomputer.com/.../bohemia-...   -> 200 OK, summary content
- WebFetch theregister.com/2024/10/10/cannabia... -> 200 OK, full content
- WebSearch site:politie.nl Bohemia Cannabia      -> primary URL discovered: 2024-oktober-8 page
- WebSearch site:eurojust.europa.eu Bohemia       -> no direct hit; Eurojust release not found
```
