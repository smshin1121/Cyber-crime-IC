# participating_countries — web primary-source verification (curl_cffi)

_Run: 2026-04-21 10:21_

Fetched via curl_cffi with Chrome TLS fingerprint impersonation (bypasses Cloudflare on most static press releases). For each op in the verification queue, every country in its `participating_countries` is checked against the rendered text of all cited source URLs.

- **verified_union** — country explicitly named in ≥1 source page
- **still_missing** — country NOT found in any reachable source
- Fetch errors (Cloudflare challenge still unsolved, 403, 404 etc.) are recorded per URL

## Summary

- Operations processed: 1
- Fully verified (every frontmatter country named in a source): 1
- Partially verified: 0
- Nothing verified (all sources failed): 0

## Results

### carbanak-cobalt-takedown

**Title**: Carbanak/Cobalt Mastermind Arrest

**Participating (frontmatter, 3)**: spain, united-states, romania

**Verified via web (3)**: romania, spain, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1- | Europol | 35870 | spain, united-states, romania |  |
| https://securelist.com/the-great-bank-robbery-the-carbanak-apt/68732/ | Kaspersky Securelist | 23200 | spain, united-states |  |
| https://www.europol.europa.eu/cms/sites/default/files/documents/carbanakcobalt.p | Europol | 1137912 | united-states |  |
| https://www.fbi.gov/contact-us/field-offices/seattle/news/stories/how-cyber-crim | FBI | 8008 | united-states |  |
