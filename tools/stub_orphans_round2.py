"""
Auto-stub the new orphan wikilinks introduced by source enrichment.
Round 2 — different categories than the original create_orphan_stubs.py.
"""
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"

NEW_OPERATIONS = {
    "alphabay-takedown": ("Operation Bayonet — AlphaBay Takedown", "darknet-marketplace"),
    "bidencash-takedown": ("BidenCash Marketplace Seizure", "carding-marketplace"),
    "cyberbunker-takedown": ("CyberBunker Bulletproof Hosting Takedown", "bulletproof-hosting"),
    "darkmarket-takedown": ("DarkMarket Marketplace Takedown", "darknet-marketplace"),
    "dridex-operations": ("Dridex Banking Trojan Operations", "banking-trojan"),
    "emotet-takedown": ("Operation LadyBird — Emotet Botnet Takedown", "botnet-takedown"),
    "operation-dark-huntor": ("Operation Dark HunTOR", "darknet-marketplace"),
    "operation-endgame": ("Operation Endgame", "botnet-takedown"),
    "operation-haechi-iii": ("Operation HAECHI III", "financial-fraud"),
    "operation-onymous": ("Operation Onymous", "darknet-marketplace"),
    "operation-power-off": ("Operation PowerOFF — DDoS-for-hire Takedowns", "ddos-for-hire"),
    "operation-rewired": ("Operation reWired", "bec"),
    "silk-road-takedown": ("Silk Road Marketplace Takedown", "darknet-marketplace"),
    "trickbot-operations": ("TrickBot Banking Trojan Operations", "banking-trojan"),
    "vpnlab-takedown": ("VPNLab.net Bulletproof VPN Takedown", "bulletproof-vpn"),
    "carding-action-2020": ("Carding Action 2020", "carding-fraud"),
}

NEW_MECHANISMS = {
    "european-arrest-warrant": "European Arrest Warrant",
    "informal-cooperation": "Informal Police Cooperation",
    "joint-investigation-team": "Joint Investigation Team (JIT)",
    "mutual-legal-assistance": "Mutual Legal Assistance",
    "public-private-cooperation": "Public-Private Cybercrime Cooperation",
    "capacity-building-ic": "Capacity Building in Cybercrime IC",
}

NEW_CRIME_TYPES = {
    "bec-crime-ic": "Business Email Compromise — IC Perspective",
    "carding-fraud-ic": "Carding Fraud — IC Perspective",
    "ddos-extortion": "DDoS Extortion — IC Perspective",
    "extortion-ic": "Extortion — IC Perspective",
}

NEW_CONCEPTS = {
    "extradition-practice": "Extradition — Practice and Variation",
    "money-mule-networks": "Money Mule Networks",
    "bulletproof-hosting": "Bulletproof Hosting",
    "cobalt-strike": "Cobalt Strike (Adversary Simulation Tool)",
    "spyeye-malware": "SpyEye Banking Trojan",
    "zeus-malware": "Zeus Banking Trojan",
}

NEW_ORGS = {
    "group-ib": ("Group-IB", "private-sector-partner"),
}

SOURCE_PAGE_REFS = [
    "bleeping-computer-andromeda-botnet-takedown",
    "bleeping-computer-goznym-takedown",
    "bleeping-computer-nemesis-market-takedown",
    "bleeping-computer-operation-falcon",
    "cbs-news-fin7-takedown",
    "cyberscoop-operation-delilah",
    "cybertalk-africa-cyber-surge-ii",
    "europol-goznym-takedown",
    "the-hacker-news-911-s5-botnet-dismantling",
    "the-hacker-news-operation-delilah",
    "the-hacker-news-operation-falcon",
    "the-record-operation-secreto",
]


def make_op_stub(title: str, op_type: str) -> str:
    return f"""---
type: operation
title: "{title}"
status: "to-be-researched"
operation_type: "{op_type}"
created: 2026-04-10
updated: 2026-04-10
last_verified: 2026-04-10
source_count: 0
sources: []
participating_countries: []
participating_agencies: []
results: {{}}
---

> [!info] Stub
> Auto-created to resolve a wikilink from an enriched source page. Needs full research and ingestion via `/ic-pipeline`. The stub exists only to maintain link integrity.

## Summary
(To be researched.)

## Background
## Participating Parties
## Results and Impact

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
"""


def make_mechanism_stub(title: str) -> str:
    return f"""---
type: mechanism
title: "{title}"
status: "stub"
created: 2026-04-10
updated: 2026-04-10
last_verified: 2026-04-10
source_count: 0
sources: []
---

> [!info] Stub
> Auto-created to resolve a wikilink. Expand when sources are ingested.

## Summary
(To be expanded.)

## Legal Basis
## How It Works
## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
"""


def make_crime_stub(title: str) -> str:
    return f"""---
type: crime-type
title: "{title}"
status: "stub"
created: 2026-04-10
updated: 2026-04-10
last_verified: 2026-04-10
source_count: 0
sources: []
---

> [!info] Stub
> Auto-created to resolve a wikilink. Expand when sources are ingested.

## Summary
(To be expanded.)

## Criminalization Landscape
## Typical IC Scenarios
## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
"""


def make_concept_stub(title: str) -> str:
    return f"""---
type: concept
title: "{title}"
status: "stub"
created: 2026-04-10
updated: 2026-04-10
last_verified: 2026-04-10
source_count: 0
sources: []
---

> [!info] Stub
> Auto-created to resolve a wikilink. Expand when sources are ingested.

## Definition
(To be expanded.)

## Relevance to IC
## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
"""


def make_org_stub(title: str, otype: str) -> str:
    return f"""---
type: organization
title: "{title}"
official_name: "{title}"
org_type: "{otype}"
status: "active"
created: 2026-04-10
updated: 2026-04-10
last_verified: 2026-04-10
source_count: 0
sources: []
---

> [!info] Stub
> Auto-created to resolve a wikilink. Expand when sources are ingested.

## Summary
(To be expanded.)

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
"""


def make_source_stub(slug: str) -> str:
    return f"""---
type: source
title: "{slug}"
status: "stub"
source_type: "news"
created: 2026-04-10
---

> [!info] Stub
> This source page was referenced from another source's cross-reference but was never created with content. Stub maintains link integrity.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
"""


def main() -> None:
    count = 0
    for slug, (title, op_type) in NEW_OPERATIONS.items():
        p = WIKI / "operations" / f"{slug}.md"
        if not p.exists():
            p.write_text(make_op_stub(title, op_type), encoding="utf-8")
            count += 1
    for slug, title in NEW_MECHANISMS.items():
        p = WIKI / "mechanisms" / f"{slug}.md"
        if not p.exists():
            p.write_text(make_mechanism_stub(title), encoding="utf-8")
            count += 1
    for slug, title in NEW_CRIME_TYPES.items():
        p = WIKI / "crime-types" / f"{slug}.md"
        if not p.exists():
            p.write_text(make_crime_stub(title), encoding="utf-8")
            count += 1
    for slug, title in NEW_CONCEPTS.items():
        p = WIKI / "concepts" / f"{slug}.md"
        if not p.exists():
            p.write_text(make_concept_stub(title), encoding="utf-8")
            count += 1
    for slug, (title, otype) in NEW_ORGS.items():
        p = WIKI / "organizations" / f"{slug}.md"
        if not p.exists():
            p.write_text(make_org_stub(title, otype), encoding="utf-8")
            count += 1
    for slug in SOURCE_PAGE_REFS:
        p = WIKI / "sources" / f"{slug}.md"
        if not p.exists():
            p.write_text(make_source_stub(slug), encoding="utf-8")
            count += 1
    print(f"Created {count} stub pages")


if __name__ == "__main__":
    main()
