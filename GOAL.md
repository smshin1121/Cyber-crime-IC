# Project Goal

## Primary Goal

Build a source-grounded, SNA-ready knowledge base on public international cooperation against cybercrime.

The project is about how countries, law-enforcement agencies, prosecutors, courts, international organizations, and private-sector partners cooperate to investigate, disrupt, seize infrastructure, arrest suspects, extradite defendants, preserve evidence, recover assets, and prosecute cybercrime. It is not primarily a threat-actor attribution database.

## Research Scope

The core research dataset should prioritize officially verifiable operation and case records from 2015 through 2025. Boundary records from 2014 and 2026 may be retained in the wiki when they clarify continuity, legal context, follow-on prosecution, or current-state interpretation, but they should be labeled and interpreted carefully in dataset outputs.

## Success Criteria

1. Every canonical operation has source-backed international-cooperation elements, including participating countries or agencies, enforcement action, legal basis where available, and results where publicly reported.
2. Absorbed follow-on records remain traceable but are not double-counted as separate canonical operations.
3. Country, agency, crime-type, mechanism, and case links are consistent enough to support reproducible two-mode and multimode SNA exports.
4. Claims about participation are supported by tier-1 or tier-2 sources whenever possible; unverified participation is flagged rather than silently asserted.
5. Analysis pages explain patterns across the corpus, including coordination models, legal mechanisms, regional gaps, Korea-related cooperation, and limitations caused by public-reporting bias.
6. The static site, indexes, and Cosmos graph build cleanly from the markdown corpus.

## Operating Metrics

The repository is in acceptable working state when:

- `python tools/lint.py` reports 0 critical/high issues.
- `python tools/check_links.py` reports 0 broken and 0 malformed links.
- `python tools/audit_integrity.py` reports 0 parse errors, 0 broken wikilinks, and 0 source mismatches.
- `python tools/audit_operation_consistency.py` reports 0 issues.
- `python tools/audit_content_depth.py` reports 0 high-priority pages, 0 source-rich thin pages, 0 placeholder-language pages, and 0 probable crime-type mismatch flags.
- `python tools/audit_source_duplicates.py --date YYYY-MM-DD` reports 0 active duplicate URL groups and 0 active duplicate content-hash groups.
- Static docs contain no unresolved translation-placeholder residue.

## Near-Term Priorities

1. Stabilize the canonical operation corpus and keep absorbed follow-on records out of operation counts.
2. Strengthen low-source canonical operation pages with official press releases, court documents, and source pages.
3. Verify participating-country and participating-agency rosters against official or high-reliability sources before using them in SNA claims.
4. Normalize duplicate source pages into canonical source records with explicit alias metadata.
5. Convert recurring review findings into durable analysis pages instead of leaving them only in chat history.
6. Keep Korea-relevant cooperation visible without overstating Korea's role where the source record is limited.

## Non-Goals

- Do not maximize page count for its own sake.
- Do not create thin standalone pages when an existing page or analysis page can carry the information better.
- Do not treat scraped titles, filenames, or agent-generated summaries as verified facts without source confirmation.
- Do not modify `raw/` files except by adding new raw sources through the documented ingest workflow.
