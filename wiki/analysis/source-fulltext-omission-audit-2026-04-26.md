---
title: Source fulltext omission audit
created: 2026-04-26
type: audit
status: draft
---

# Source fulltext omission audit

This audit checks raw source records that still lacked `## Extracted Text`, with emphasis on official legal texts, treaty status pages, and official public-record material that can reasonably be stored as full text with attribution.

## Scope

- Raw files without `## Extracted Text` at audit start: 3,045
- Strong official legal/treaty text candidates identified by heuristic pass: 36
- Broader official legal-signal records after re-audit: 87
- Current fulltext among broader official legal-signal records: 59
- Current non-fulltext among broader official legal-signal records: 28

Audit CSV outputs were written under `_workspace/`:

- `_workspace/non_fulltext_legal_candidate_audit.csv`
- `_workspace/official_legal_text_fulltext_audit.csv`

## Converted in this pass

The following records were upgraded from summary/stub state to fulltext:

- `raw/press-releases/2009-09-15_dre-pt_lei-n-109-2009-lei-do-cibercrime.md`
- `raw/press-releases/2014-06-27_au-int_treaty-text-and-status-chart.md`
- `raw/press-releases/2016-11-28_pgdlisboa-pt_decree-law-no-81-2016.md`
- `raw/press-releases/2025-01-01_coe-int_chart-of-signatures-and-ratifications-of-treaty-185.md`
- `raw/press-releases/2026-04-17_au-int_malabo-convention-status.md`
- `raw/press-releases/2026-04-17_coe-int_budapest-convention-chart-of-signatures-and-ratifications-cets-185.md`
- `raw/press-releases/2026-04-17_coe-int_chart-of-signatures-and-ratifications-of-treaty-185.md`
- `raw/press-releases/2026-04-17_coe-int_treaty-185-signatures-chart.md`

The two Portugal records use `license_basis: official_legal_text`. The AU and Council of Europe treaty/status records use `license_basis: treaty_status_public_record`.

## Still blocked or deferred

- `2013-08-12_artci-ci_loi-n-2013-451...`: eligible official legislative text, but available PDFs are scanned image PDFs in this environment. OCR is required before reliable fulltext storage.
- `2010-12-21_antic-cm_law-no-2010-012...`: official Cameroon cybercrime law, but direct PDF fetch either timed out or exposed no text layer. OCR or a reliable HTML source is required.
- `2018-08-22_rura-rw_law-no-60-2018...`: official Rwanda law; direct government PDFs found, but tested copies expose no text layer. OCR is required.
- `2018-12-07_ancy-gouv-tg_loi-n-2018-026...`: official Togo law; current source URL is a homepage and UNODC/government copies require either direct attachment resolution or OCR.
- CoE/UNODC general profile/news pages remain summary/stub unless they are treaty/status records or another explicit fulltext basis is established.

## Tool changes

`tools/harvest_linked_source_text.py` was updated to:

- attempt PDF text extraction through `pypdf` before fallback parsing;
- classify text-layer-empty PDFs as OCR-needed instead of silently producing short summaries;
- remove summary-only metadata when a record is upgraded to fulltext;
- prefer Jina for Council of Europe Treaty Office signature charts, where the plain HTML response is a JavaScript shell.
