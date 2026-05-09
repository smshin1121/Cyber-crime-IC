---
type: operation
title: "Trilateral Sanctions on Media Land and Aeza Group Russian Bulletproof Hosting (2025)"
aliases:
  - "Media Land sanctions"
  - "Hypercore / Aeza follow-on designations"
  - "Treasury SB-0319"
  - "US-AU-UK Russian BPH sanctions 2025"
case_id: CYB-2025-111
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - asset-freeze
outcome: success
timeframe:
  announced: 2025-11-19
  start: 2025-11-19
  end: 2025-11-19
  ongoing: false
crime_types:
  - "[[ransomware-ic]]"
  - "[[ddos-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
target_entity: "Media Land LLC (St. Petersburg, Russia) — a bulletproof hosting (BPH) provider that serviced Lockbit, BlackSuit, and Play ransomware operators and DDoS actors targeting U.S. companies and critical infrastructure — together with three Media Land sister companies (ML Cloud, Media Land Technology, Data Center Kirishi) and three leadership/affiliate persons (Aleksandr Volosovik a.k.a. 'Yalishanda', general director; Kirill Zatolokin, payments and customer coordination; Yulia Pankova, financial/legal facilitator). The same trilateral action also targets the Aeza Group sanctions-evasion network: Hypercore Ltd. (UK-registered front company), Maksim Vladimirovich Makarov (new Aeza director), Ilya Vladislavovich Zakirov (corporate-structure obfuscator), Smart Digital Ideas DOO (Serbia), and Datavice MCHJ (Uzbekistan)."
lead_agency: "[[us-treasury]]"
coordinating_body: "[[us-treasury]]"
participating_countries:
  - "[[united-states]]"
  - "[[australia]]"
  - "[[united-kingdom]]"
  - "[[russia]]"
participating_agencies:
  - "[[us-treasury]]"
  - "[[fbi]]"
legal_basis:

mechanisms_used:
  - "[[asset-freezing]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "9 entities designated by OFAC under E.O. 13694, as further amended (Media Land LLC, ML Cloud, Media Land Technology, Data Center Kirishi, Hypercore Ltd., Smart Digital Ideas DOO, Datavice MCHJ — release identifies these 7 entities by name; 2 sister/front entities additionally tied to Aeza per release narrative)"
    - "5 individuals designated: Aleksandr Volosovik ('Yalishanda'), Kirill Zatolokin, Yulia Pankova (Media Land cluster); Maksim Vladimirovich Makarov, Ilya Vladislavovich Zakirov (Aeza cluster)"
    - "Coordinated trilateral designations by U.S. (OFAC), Australia (DFAT), and UK (FCDO)"
    - "CISA + international partners released parallel guidance on mitigating risks from bulletproof hosting providers"
edges:
  - source_actor: us-treasury
    target_actor: fbi
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: us-treasury
    target_actor: australia-dfat
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: us-treasury
    target_actor: uk-fcdo
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "specific SDN-list identifiers for designated persons (DOB, passport, address)"
  - "specific MLAT or Five Eyes information-sharing instrument cited"
related_cases:

related_operations:
  - "[[us-uk-prince-group-tco-huione-group-sanctions-2025]]"
  - "[[treasury-us-au-uk-zservers-sanctions-2025]]"
  - "[[treasury-aeza-group-bulletproof-hosting-sanctions-2025]]"
  - "[[treasury-evil-corp-tri-lateral-us-uk-au-sanctions-2024]]"
challenges_encountered:

lessons_learned:
  - "Sanctions evasion via cross-jurisdictional rebranding (Aeza → Hypercore via UK shell, plus Serbian and Uzbek enabler entities) requires sustained, repeated designation cycles to maintain pressure."
  - "Coordinated sanctions across three jurisdictions can target the financial-services and infrastructure layer of the ransomware ecosystem even where the underlying actors remain physically beyond extradition reach."
source_count: 1
sources:
  - "[[2025-11-19_treasury_us-au-uk-sanctions-russian-cybercrime-infrastructure-media-land]]"
created: 2026-05-09
updated: 2026-05-09
---
# Trilateral Sanctions on Media Land and Aeza Group Russian Bulletproof Hosting (2025)

## Summary

On 19 November 2025, the U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC), Australia's Department of Foreign Affairs and Trade (DFAT), and the United Kingdom's Foreign, Commonwealth and Development Office (FCDO) announced coordinated trilateral sanctions targeting **Media Land LLC**, a St. Petersburg-based bulletproof hosting (BPH) provider that supported Lockbit, BlackSuit, and Play ransomware operators as well as distributed denial-of-service (DDoS) attacks against U.S. companies and critical infrastructure (Treasury press release SB-0319; reliability: high; credibility: confirmed). The same action additionally designated a sanctions-evasion network supporting the previously-designated Aeza Group, including the UK-registered front company **Hypercore Ltd.** and enabler entities in Serbia and Uzbekistan.

The U.S. component of the action was conducted by [[us-treasury|OFAC]] in coordination with the [[fbi|Federal Bureau of Investigation]] and is **almost certainly** the largest single trilateral cyber-sanctions package against Russian BPH infrastructure announced in 2025 (high confidence, based on the on-the-record framing in the Treasury release).

## Background

Bulletproof hosting providers sell access to specialized servers and other computer infrastructure specifically designed to evade detection and defy law enforcement efforts to disrupt malicious cyber activities. Treasury describes Media Land as a "key launching pad for ransomware," tying its infrastructure to three of the highest-profile ransomware brands of the 2023-2025 period — Lockbit, BlackSuit, and Play.

The Aeza-related portion of this action is a **direct follow-on to OFAC's 1 July 2025 designation of Aeza Group LLC** and its leadership. According to Treasury, after the July 2025 designation, "Aeza leadership initiated a rebranding strategy focusing on removing any connections between Aeza and their new technical infrastructure" — most notably by routing IP infrastructure through Hypercore Ltd., a UK-registered shell, and by establishing enabler entities in Serbia (Smart Digital Ideas DOO) and Uzbekistan (Datavice MCHJ). The 19 November 2025 follow-on action is framed as maintenance of pressure against the same underlying actors.

## Designated Targets

### Media Land cluster

- **Media Land LLC** — St. Petersburg-based BPH service provider; primary target.
- **ML Cloud** — sister company whose technical infrastructure is often used in conjunction with Media Land in ransomware and DDoS attacks.
- **Media Land Technology (MLT)** — 100 percent-owned Media Land subsidiary.
- **Data Center Kirishi (DC Kirishi)** — 100 percent-owned Media Land subsidiary.
- **Aleksandr Volosovik** — general director of Media Land; advertised on cybercriminal forums under the alias **"Yalishanda"**; provided servers and troubleshooting for ransomware and DDoS actors.
- **Kirill Zatolokin** — Media Land employee responsible for collecting payment from customers and coordinating with other cyber actors.
- **Yulia Pankova** — assisted Volosovik with legal issues and handled his finances.

### Aeza Group sanctions-evasion cluster

- **Hypercore Ltd.** — UK company registered and used by Aeza Group after its July 2025 designation to move IP infrastructure and evade sanctions.
- **Maksim Vladimirovich Makarov** — new director of Aeza; made key decisions regarding Aeza Group's sanctions-evasion attempt.
- **Ilya Vladislavovich Zakirov** — helped establish new companies and payment methods to obfuscate Aeza's continuing activity.
- **Smart Digital Ideas DOO** — Serbian company used by Aeza to evade sanctions and set up technical infrastructure not publicly associated with the Aeza brand.
- **Datavice MCHJ** — Uzbek company used by Aeza for the same purpose.

## Participating Parties

- **United States** — [[us-treasury|U.S. Department of the Treasury / OFAC]] (lead U.S. agency; speaker on the record: Under Secretary for Terrorism and Financial Intelligence John K. Hurley); [[fbi|Federal Bureau of Investigation]] (coordinating law-enforcement partner); Cybersecurity and Infrastructure Security Agency (released parallel BPH-mitigation guidance).
- **Australia** — Department of Foreign Affairs and Trade (DFAT) (coordinated parallel designation; no DFAT wiki page exists at time of writing).
- **United Kingdom** — Foreign, Commonwealth and Development Office (FCDO) (coordinated parallel designation; partner on Hypercore Ltd. designation specifically given the UK incorporation of that entity; no FCDO wiki page exists at time of writing).

## Legal Framework

All U.S. designations were made pursuant to **Executive Order 13694, as amended by E.O. 13757, E.O. 14144, and E.O. 14306** (collectively, "E.O. 13694, as further amended") — the U.S. cyber-sanctions authority chain. Designations were made under several distinct prongs:

- **Cyber-enabled-activity prong**: Media Land, ML Cloud, Volosovik, and Zatolokin (responsible for or complicit in cyber-enabled activities causing disruption to or compromising integrity of computers/networks).
- **Material-assistance prong**: Pankova (assistance to Volosovik), Zakirov (assistance to Aeza), Smart Digital Ideas (assistance to Aeza).
- **Owned-or-controlled-by prong**: Media Land Technology, Data Center Kirishi (owned by Media Land); Hypercore Ltd., Datavice MCHJ (owned by or acting for Aeza).
- **Leadership prong**: Makarov (director of Aeza).

The Australian and UK measures are parallel sanctions actions under each country's own autonomous-sanctions regime; the Treasury release does not specify the exact statutory instrument used by DFAT or FCDO.

## Operational Timeline

- **2025-07-01** — OFAC designates Aeza Group LLC and its original leadership (precursor action; not the subject of this page but factually relevant).
- **2025-11-19** — OFAC, DFAT, and FCDO simultaneously announce coordinated designations of Media Land cluster and Aeza follow-on entities; Treasury issues press release SB-0319; CISA and partners release parallel BPH-mitigation guidance.

## Results and Impact

- **Asset blocking**: All property and interests in property of the designated persons within the United States or in the possession or control of U.S. persons are blocked and must be reported to OFAC. Any entity owned 50 percent or more by one or more blocked persons is also blocked by operation of OFAC's 50 Percent Rule.
- **Secondary effects**: Financial institutions and other persons engaging in transactions with the sanctioned entities/individuals are exposed to enforcement risk.
- **Public guidance**: CISA + international partners released parallel guidance on mitigating risks from bulletproof hosting providers.

> [!note] No criminal indictments
> This action is administrative (sanctions designations) only. No criminal indictments are announced in the release. The targets remain in Russia (and, for some enabler entities, Serbia/Uzbekistan), and physical apprehension is **highly unlikely** in the near term given the absence of extradition relations with Russia for cybercrime defendants.

## Cooperation Mechanisms Used

- **Coordinated-designations diplomacy**: The most prominent mechanism here is the simultaneous, on-the-record trilateral announcement by OFAC, DFAT, and FCDO. This is a soft-law / financial-policy mechanism rather than a treaty-based MLA channel.
- **Asset freezing** ([[asset-freezing]]) — primary enforcement mechanism, via the U.S. SDN list and its UK/Australian counterparts.
- **Inter-agency coordination within the U.S.** between OFAC and the FBI (and CISA on the public-guidance side).

The release does not name any treaty-based MLAT request, Budapest Convention provision, or 24/7 Network contact; coordination appears to be through diplomatic / executive-branch channels rather than judicial cooperation.

## Challenges and Friction Points

- **Sanctions-evasion via rebranding**. The Aeza-cluster portion of this action is itself the second iteration of pressure on the same underlying actors — the July 2025 designation triggered a rebranding cycle that this November 2025 designation now targets. This pattern is **highly likely** to continue: each designation increases the cost of the next iteration but does not eliminate the underlying capability.
- **Cross-jurisdictional shell layering**. Aeza's use of UK, Serbian, and Uzbek corporate vehicles illustrates the difficulty of disrupting Russia-based BPH ecosystems through national-level designations alone; only the UK partner here has direct enforcement authority over the most significant shell (Hypercore Ltd.).
- **No physical disruption**. The action seizes neither servers nor domains nor cryptocurrency on the public record; it is purely a financial-system measure. The underlying BPH infrastructure remains operational unless and until separate kinetic disruption occurs.

## Lessons Learned

- Sustained iterative designation cycles, rather than one-shot actions, are required to maintain pressure on resilient BPH ecosystems that respond to sanctions by rebranding.
- Trilateral coordination (U.S.-UK-Australia) is feasible for cyber-sanctions and can extend the geographic reach of U.S. cyber-EO authorities into UK-registered shell entities.

## Follow-Up Actions

- Future SDN-list updates **likely** (medium confidence) as Aeza/Media Land actors continue rebranding.
- CISA's published BPH-mitigation guidance creates a public-private channel for victim and ISP-side defensive measures.

## Korean Involvement (한국의 참여)

No Korean government agency is named as a participant in this action. South Korea is not part of the trilateral coordinating group for this specific designation (high confidence, based on the press release on the record). However, Korean victims of Lockbit, BlackSuit, and Play ransomware **possibly** benefit indirectly from the disruption of supporting BPH infrastructure, and Korean financial institutions are exposed to OFAC's secondary-sanctions enforcement risk if they transact with the designated entities.

## Contradictions & Open Questions

- **Entity count**. The Treasury release narrative names a total of nine distinct entities (Media Land + ML Cloud + MLT + DC Kirishi + Hypercore + Smart Digital + Datavice = 7 entities by name, plus the textual reference to "three of its sister companies" for Media Land and "two entities" for Aeza, which is internally consistent at 5+2=7 entities by name plus the originally-designated Aeza Group itself). Cross-checking against the SDN Recent Actions list would resolve any residual ambiguity.
- **Australian and UK statutory basis**. The release does not name the specific Australian or UK sanctions-listing instrument used; this would need to be retrieved from DFAT and OFSI publications respectively.
- **DDoS victim attribution**. The release refers to "multiple distributed denial-of-service (DDOS) attacks against U.S. victim companies and critical infrastructure" but does not enumerate the victims; specific incident attribution is not on the record here.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | [[2025-11-19_treasury_us-au-uk-sanctions-russian-cybercrime-infrastructure-media-land\|United States, Australia, and United Kingdom Sanction Russian Cybercrime Infrastructure Supporting Ransomware]] | U.S. Department of the Treasury (OFAC), Press Release SB-0319 | 2025-11-19 | https://home.treasury.gov/news/press-releases/sb0319 |
