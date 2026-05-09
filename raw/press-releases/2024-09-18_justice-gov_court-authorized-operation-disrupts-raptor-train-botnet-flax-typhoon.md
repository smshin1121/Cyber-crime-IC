---
source_url: https://www.justice.gov/opa/pr/court-authorized-operation-disrupts-worldwide-botnet-used-peoples-republic-china-state
publisher: U.S. Department of Justice — Office of Public Affairs
publish_date: 2024-09-18
ingest_date: 2026-05-09
press_release_number: 24-1173
language: en
fetch_method: doj_fetch (Akamai bm-verify session pattern per L21; chrome124 UA + cookie jar; primary canonical URL is the apostrophe-less variant)
fetch_status: 200 OK; ~89KB body; full article text recovered
ic_scope_flag: "Tier-1 Five Eyes joint cybersecurity advisory action. Explicitly named cooperation partners: France (French authorities) plus partner cyber agencies in Australia, Canada, New Zealand, and the United Kingdom (FVEY co-signers of same-day CSA). Lumen Technologies / Black Lotus Labs credited as private-sector partner. Lead: FBI San Diego + FBI Cyber Division + USAO WDPA + DOJ NSD National Security Cyber Section + DOJ Criminal Division CCIPS + DOJ Criminal Division Office of International Affairs (OIA). Court venue: U.S. District Court, Western District of Pennsylvania."
note: |
  Note on canonical URL: the apostrophe-bearing slug (`...people-s-republic...`) returns DOJ 404 as of 2026-05-09. The live canonical URL drops the apostrophe (`...peoples-republic...`). The 404 variant is the form widely cited in third-party reporting.
---

# Court-Authorized Operation Disrupts Worldwide Botnet Used by People's Republic of China State-Sponsored Hackers

**Date:** Wednesday, September 18, 2024
**Source:** U.S. Department of Justice, Office of Public Affairs (Press Release Number 24-1173)
**URL:** https://www.justice.gov/opa/pr/court-authorized-operation-disrupts-worldwide-botnet-used-peoples-republic-china-state
**Subhead:** Actors Unsuccessfully Sought to Prevent FBI's Disruption of Botnet
**Note:** "View the affidavit here." (link in original)

> [!note] Fetch note
> Primary URL form `...people-s-republic-china-state` (with apostrophe) returns DOJ Page Not Found. Canonical live URL drops the apostrophe: `...peoples-republic-china-state`. Per L21, DOJ Akamai Bot Manager interstitial pattern was traversed via `tools/doj_fetch.py` (chrome-style UA + bm-verify session). Page footer indicates "Updated February 6, 2025" but body publication date is **2024-09-18**.

## Headline Facts (verbatim from DOJ release)

- **Court-authorized law enforcement operation** disrupted a botnet of **more than 200,000 consumer devices** in the United States and worldwide.
- Court documents **unsealed in the Western District of Pennsylvania**.
- Botnet devices infected by **PRC state-sponsored hackers working for Integrity Technology Group**, a Beijing-based publicly-traded company, **known to the private sector as "Flax Typhoon."**
- Compromised device classes: **SOHO routers, IP cameras, DVRs, NAS** devices.
- Operation took control of the hackers' computer infrastructure and **sent disabling commands** through that infrastructure to malware on infected devices.
- During the operation, **Integrity Technology Group attempted a DDoS attack against the FBI's operational infrastructure** — unsuccessful.
- Integrity Technology Group's online control application was branded **"KRLab"** with a malicious-command menu tool called **"vulnerability-arsenal."**
- FBI assesses Integrity Technology Group is responsible for the China-based hacker activity industry calls **Flax Typhoon** (active since 2021 per Microsoft Threat Intelligence, targeting Taiwan and elsewhere; FBI corroborates and adds attacks against U.S. and foreign corporations, universities, government agencies, telecommunications providers, and media organizations).

## Cooperation Partners (explicitly named in the press release)

### Lead U.S. agencies
- **FBI San Diego Field Office** (Special Agent in Charge Stacey Moy)
- **FBI Cyber Division**
- **U.S. Attorney's Office for the Western District of Pennsylvania** (U.S. Attorney Eric G. Olshan)
- **DOJ National Security Division — National Security Cyber Section** (AAG Matthew G. Olsen)
- **DOJ Criminal Division — Computer Crime and Intellectual Property Section (CCIPS)** (assistance)
- **DOJ Criminal Division — Office of International Affairs (OIA)** (component listed in press release footer)

### Same-day Joint Cybersecurity Advisory co-signers
> "A cybersecurity advisory describing Integrity Technology Group tactics, techniques and procedures was also published today by the **FBI**, the **National Security Agency**, **U.S. Cyber Command's Cyber National Mission Force**, and **partner agencies in Australia, Canada, New Zealand and the United Kingdom**."

This is a Five Eyes joint advisory pattern. The press release names the four FVEY partner countries but **does not name** the specific partner agencies (e.g., ASD/ACSC, CCCS, GCSB/NCSC-NZ, NCSC-UK) — those are inferred from the public record of the actual joint CSA but are NOT directly asserted in this DOJ press release text.

### Foreign government cooperation (named explicitly)
- **French authorities** — credited for "collaboration of partners" alongside Lumen.

### Private-sector partner
- **Lumen Technologies — Black Lotus Labs** — credited with first identifying and describing the botnet (named "Raptor Train" by them) in **July 2023**.

## Quote Highlights

- **Attorney General Merrick B. Garland**: "As we did earlier this year, the Justice Department has again destroyed a botnet used by PRC-backed hackers..." (reference to the May 2024 911 S5 botnet takedown context).
- **Deputy Attorney General Lisa Monaco**: "This network, managed by a PRC government contractor, hijacked hundreds of thousands of private routers, cameras, and other consumer devices..."
- **AAG Matthew G. Olsen (NSD)**: "For the second time this year, we have disrupted a botnet used by PRC proxies..."
- **FBI Deputy Director Paul Abbate**: "The FBI's unique legal authorities allowed it to lead **an international operation with partners** that collectively disconnected this botnet from its China-based hackers at Integrity Technology Group."
- **U.S. Attorney Eric G. Olshan (WDPA)**: "This court-authorized operation disrupted a sophisticated botnet designed to steal sensitive information and launch disruptive cyber attacks."
- **SAC Stacey Moy (FBI San Diego)**: "A publicly-traded, China-based company is openly selling its customers the ability to hack into and control thousands of consumer devices worldwide."

## Operational Notes
- Disabling commands "interacted with the malware's native functionality" and were "extensively tested prior to the operation." DOJ asserts the operation **did not affect legitimate functions** of, or collect content from, infected devices.
- FBI providing victim notice through ISPs to U.S. owners of affected devices.
- DOJ press release directs compromised-device reporting to FBI IC3 or CISA.

## DOJ Press Release Components (footer)
- Office of the Attorney General
- Criminal - Computer Crime and Intellectual Property Section
- **Criminal - Office of International Affairs**
- Federal Bureau of Investigation (FBI)
- National Security Division (NSD)
- Office of the Deputy Attorney General
- USAO - Pennsylvania, Western

**Topic:** National Security
**Press Release Number:** 24-1173

## Cross-Validation (companion sources, not ingested as separate raw items)

The same-day Joint Cybersecurity Advisory referenced in the DOJ release was published by FBI + NSA + USCYBERCOM CNMF + Australia/Canada/NZ/UK partner agencies — the public artifact is `CSA-PRC-LINKED-ACTORS-BOTNET.PDF` (defense.gov hosted, 2024-09-18). Lumen / Black Lotus Labs published its companion technical writeup ("Derailing the Raptor Train") on the same day.

> [!warning] Per L19 — only countries explicitly named in this primary source are asserted as participating_countries on the operation page
> Asserted cooperation: **United States** (lead), **France** (named), **Australia / Canada / New Zealand / United Kingdom** (named as joint-advisory partner countries). Specific partner agency names (e.g., ASD/ACSC, CCCS, NCSC-NZ, NCSC-UK) are NOT asserted from this source alone — they are inferable from the companion CSA but should not be linked unless that CSA is ingested as a separate raw source.

> [!warning] Per L1 — file slug uses the apostrophe-less canonical URL form
> The DOJ slug containing `peoples-republic-china-state` is the canonical live URL. The widely-cited variant with `people-s-republic` is a 404 redirect candidate. Both forms preserved in source frontmatter and source-summary `collection_url` for diagnostic clarity.

## Extracted Press Release Body (verbatim, normalized whitespace)

The Justice Department today announced a court-authorized law enforcement operation that disrupted a botnet consisting of more than 200,000 consumer devices in the United States and worldwide. As described in court documents unsealed in the Western District of Pennsylvania, the botnet devices were infected by People's Republic of China (PRC) state-sponsored hackers working for Integrity Technology Group, a company based in Beijing, and known to the private sector as "Flax Typhoon."

The botnet malware infected numerous types of consumer devices, including small-office/home-office (SOHO) routers, internet protocol (IP) cameras, digital video recorders (DVRs), and network-attached storage (NAS) devices. The malware connected these thousands of infected devices into a botnet, controlled by Integrity Technology Group, which was used to conduct malicious cyber activity disguised as routine internet traffic from the infected consumer devices. The court-authorized operation took control of the hackers' computer infrastructure and, among other steps, sent disabling commands through that infrastructure to the malware on the infected devices. During the course of the operation, there was an attempt to interfere with the FBI's remediation efforts through a distributed denial-of-service (DDoS) attack targeting the operational infrastructure that the FBI was utilizing to effectuate the court's orders. That attack was ultimately unsuccessful in preventing the FBI's disruption of the botnet.

[Quotes from AG Garland, DAG Monaco, AAG Olsen (NSD), FBI Deputy Director Abbate, U.S. Attorney Olshan (WDPA), and SAC Moy (FBI San Diego) — see "Quote Highlights" above.]

According to the court documents, the botnet was developed and controlled by Integrity Technology Group, a publicly-traded company headquartered in Beijing. The company built an online application allowing its customers to log in and control specified infected victim devices, including with a menu of malicious cyber commands using a tool called "vulnerability-arsenal." The online application was prominently labelled "KRLab," one of the main public brands used by Integrity Technology Group.

The FBI assesses that Integrity Technology Group, in addition to developing and controlling the botnet, is responsible for computer intrusion activities attributed to China-based hackers known by the private sector as "Flax Typhoon." Microsoft Threat Intelligence described Flax Typhoon as nation-state actors based out of China, active since 2021, who have targeted government agencies and education, critical manufacturing, and information technology organizations in Taiwan, and elsewhere. The FBI's investigation has corroborated Microsoft's conclusions, finding that Flax Typhoon has successfully attacked multiple U.S. and foreign corporations, universities, government agencies, telecommunications providers, and media organizations.

A cybersecurity advisory describing Integrity Technology Group tactics, techniques and procedures was also published today by the FBI, the National Security Agency, U.S. Cyber Command's Cyber National Mission Force, and partner agencies in Australia, Canada, New Zealand and the United Kingdom.

The government's malware disabling commands, which interacted with the malware's native functionality, were extensively tested prior to the operation. As expected, the operation did not affect the legitimate functions of, or collect content information from, the infected devices. The FBI is providing notice to U.S. owners of devices that were affected by this court-authorized operation. The FBI is contacting those victims through their internet service provider, who will provide notice to their customers.

The FBI's San Diego Field Office and Cyber Division, the U.S. Attorney's Office for the Western District of Pennsylvania, and the National Security Cyber Section of the Justice Department's National Security Division led the domestic disruption effort. Assistance was also provided by the Criminal Division's Computer Crime and Intellectual Property Section. These efforts would not have been successful without the collaboration of partners, including French authorities, and Lumen Technologies' threat intelligence group, Black Lotus Labs, which first identified and described this botnet, which it named Raptor Train, in July 2023.

If you believe you have a compromised computer or device, please visit the FBI's Internet Crime Complaint Center (IC3) or report online to CISA. You may also contact your local FBI field office directly.

The FBI continues to investigate Integrity Technology Group's and Flax Typhoon's computer intrusion activities.
