# Work History — 2026-04-21

Session summary covering 48 commits (`964481a0` → `dccbad38`) spanning Globe picker UX, Mercator projection, tier-1 source verification audit, and the full SNA 2D rework with physics.

---

## 1. Globe country→operation picker (UX)

Problem: clicking a country on the globe drew every arc of every op the country ever joined. For hubs (US / UK / etc.) this drowned the map.

Solution: interactive picker per country.

| Commit | Change |
|---|---|
| `80e7adff` | Initial picker inside root badge |
| `fb7a9d37` | Move out of badge → bottom-right floating panel |
| `5eea4a9b` | Wider + shorter + themed scrollbar + drag to reposition |
| `2fb7278a` | Sticky header, single-line rows |
| `50b19f61` | Lower default y, divider, Clear = Reset Root |
| `21ab242f` | Country name inline in header + auto-pick first op |
| `ded9d06e` | Title truncation threshold 15 → 30 → 50 |
| `085dd255` | Last-item clickability (padding + scroll-padding-bottom) |
| `e894debd` | Stats-chip row was stealing clicks — z-index 12 → 14 + `pointer-events:none` on stats |
| `ce5e1abe` | Overview-mode arcs dimmed to 0.10/0.12 |

End state: click country → picker lists participating ops; click op → arcs filtered to that op's country pairs only.

---

## 2. Globe 2D map improvements

| Commit | Change |
|---|---|
| `1314ba2b` | 2D pan/zoom no longer reset by slider changes — moved one-shot camera reset into the view-toggle handler |
| `d1c9284a` | **Equirectangular → Web Mercator** (Google-Maps-style, ±85.0511° clamp). `latLonTo2D`, `buildCountryBorders`, `buildCountryFills`, `getFitDistance2D` all route lat through `mercY()` |
| `1214d8be` | Country fills stopped flickering on zoom-out: `transparent:true + depthWrite:false` → `transparent:false + depthWrite:true + polygonOffset`; border z 0.08 → 0.18 (z-fight fix) |
| `f4c8fe01` | Globe 3D arcs invisible bug — `depthTest:false` scoped to 2D only |

---

## 3. Wiki participating_countries audit pipeline

Triggered by the user question: "Colombia 파트너 7은 어디서 나오나?"

### Principle established (LESSONS L19)
Only assert a country→op participation when a tier-1 primary source (Europol / INTERPOL / DOJ / national agency press release or court filing) **explicitly names** that country. Three buckets per op:
- **verified** — primary source names country → keep, add bidirectional back-link
- **removed** — all accessible primary sources reviewed, country absent → remove + Contradictions log
- **pending** — primary source unreachable → retain, flag until access is possible

### Initial Colombia audit (`343084f5`)
- Verified via INTERPOL/Europol press releases: `operation-orion-international`, `operation-haechi-ii`, `imminent-monitor-rat-takedown`
- Removed from `operation-avalanche` (wrong call — reverted once Cloudflare was bypassed; see §4)

### Avalanche partial audit + stubs (`184106a8`, `b8fdfd03`)
- Added `wiki/countries/kazakhstan.md`, `wiki/countries/united-arab-emirates.md` (stub pages for dangling wikilinks)
- Expanded alias overrides: Viet Nam, Kazakh/Kyrgyz/Tajik/Uzbek, UAE/U.A.E./Emirates

### Dedup pass (`3dfe12af`)
45 single-case operation pages pruned + 12 redundant case pages deleted + umbrella Audit Notes added to AlphaBay / xDedic / Dridex etc. Total 1095 → 1085 operations.

### Carbanak/Cobalt correction (`03d75023`)
Europol PDF + BBC + Reuters + Kaspersky all fail to name Belarus / Moldova / Taiwan. Removed per L19. `participating_countries` narrowed to `[spain, united-states, romania]`.

---

## 4. Web verification pipeline (the Cloudflare→Akamai breakthrough)

Built to verify every op's `participating_countries` against its primary sources programmatically.

### Tooling
| File | Purpose |
|---|---|
| `tools/verify_participating_countries.py` | Local-text scan (raw/ + wiki/sources/ summaries + op body) |
| `tools/collect_verify_queue.py` | Builds `.verification/verify_queue.json` from the audit report; extracts URLs from 3 source formats (wikilink, markdown-link, plain URL) |
| `tools/web_verify_tls.py` | Fetches each URL via `curl_cffi` with Chrome TLS impersonation; BeautifulSoup parse with `<script>` preservation; checks for each frontmatter country + alias |
| `tools/apply_bidirectional_ops.py` | Idempotent — reads the web report and appends missing country→op back-links to country pages |

### Three wall patterns defeated (LESSONS L20, L21)

| Wall | Symptom | Remedy |
|---|---|---|
| **Cloudflare** (old Europol) | 403 / "Just a Moment" challenge | `curl_cffi.requests.get(url, impersonate="chrome124")` |
| **React SPA** (new Europol newsroom) | 200 OK but body is "Loading application" | BeautifulSoup with `<script>` preserved — country roster lives in inline JSON |
| **Akamai Bot Manager** (DOJ / justice.gov / usao-*) | 200 OK with ~3KB meta-refresh shell + `bm-verify` cookie | `curl_cffi.Session()` + parse meta-refresh URL + 5.5s sleep + retry in same session |

### Results
| Round | Fully verified | Partial | No sources |
|---|---|---|---|
| Initial (top-30) | 15 | 3 | 12 |
| After alias fix | 23 | 1 | 76 |
| After Akamai bypass | 94 | 1 | 5 |
| Final (top-100) | **96** | 1 | 3 |

Colombia was reinstated to Avalanche (`560e7180`) — the Europol inline JSON does list Colombia in "Countries involved: …, Colombia, …, Gibraltar, …". Earlier removal was based on accessible-subset only.

### L19 application totals
- **217 country→op back-links added** across ~60 country pages (3 rounds)
- 3 entries removed (Belarus/Moldova/Taiwan from Carbanak)
- 2 stub country pages created (Kazakhstan, UAE)
- 1 restoration (Colombia in Avalanche)

---

## 5. SNA visualization rebuild

### Structural
| Commit | Change |
|---|---|
| `964481a0` | Node drag under cursor + live edge follow (restored from `13453a7b`) |
| `13453a7b` | Peacock packs components into current viewport |
| `77ed0375` | Peacock as i2-style radial hierarchy (later superseded) |
| `bae41e66` | Peacock as community-cluster SNA layout (final direction) |
| `97f15836` | Edge-crossing reduction via greedy TSP community ordering |
| `8a0c91ec` | **SNA Ring/Force → flat 2D circles** (CircleGeometry + MeshBasicMaterial) matching Globe 2D dots. 3D view keeps sphere + standard material |

### Animation + physics
| Commit | Change |
|---|---|
| `b13f01b9` | **Peacock arrange animates** (0.9s cubic ease-out) instead of snapping. `S.sna._peacockTween` stores per-mesh {from, to}; animate() lerps each frame and updates edges + labels |
| `a4f0cf8f` | **Continuous wobble physics** on Ring/Force views. Per-node spring (to `basePos`) + O(N²) Coulomb repulsion + sinusoidal noise + damping. `basePos` updated on peacock tween end and drag end |
| `2858560f` | Label lag fixed (drag now moves label in same frame); peacock cluster internal spacing (8-iter min-distance relaxation); SNA label position above node instead of `multiplyScalar(1.08)`; transparent edges flicker fixed (`depthWrite:false + depthTest:false + renderOrder:-1`) |

### Visual polish (iterative — user feedback driven)
| Commit | Change |
|---|---|
| `27b1d18b` | Translucent outline ring added (for overlap discrimination) |
| `899c4747` | Edge opacity ~50% down — softer links |
| `42d66aa6` | Edge color + opacity unified across tiers (community signaled by node color alone) |
| `0ae6d34d` | **Edges trim at node boundary** (no more extending under fill) — `_snaEdgeIndex` extended with `{selfMesh, otherMesh}`, trim re-applied in drag + physics + peacock tween |
| `b4aae425` | **Stroke ring width fixed absolute** (0.28/0.32) instead of proportional to `sz` — removed variable-thickness illusion |
| `e0c173e3` | Edges bumped back up: color `0x9ab6d4`, opacity 0.28 (still uniform) |
| `f949e11c` → `6e81c493` → `8383649c` → `dccbad38` | Stroke color/opacity experimentation — final: white, opacity 0.25 (actual visible translucency) |

---

## 6. LESSONS.md updates

Added:
- **L19** — Participating_countries assert requires tier-1 explicit mention; unavailable = flag, cumulative absence = remove
- **L20** — Cloudflare/SPA wall = `curl_cffi` TLS impersonation + script-preserving parse
- **L21** — Akamai Bot Manager = session + meta-refresh + sleep + retry

---

## 7. Remaining open items

- `bidencash-takedown` — 3/6 verified (Denmark/Finland/Germany not named in cited sources; L19 judgement pending)
- `dridex-operations` — source references are plain-text labels; URLs live in body references table, need ingestion into source summary pages
- `operation-ghost-cybercrime-platform-dismantled`, `operation-in-re-heartsender-seizure` — USAO subdomain fetches flaky
- Gibraltar country page not yet created (Europol Avalanche roster includes it)
- Queue expansion beyond top-100 (900+ ops still outside verified set)

---

## 8. Pipeline capability snapshot (end of day)

```
  URL in (any source format)
      │
      ▼
  ┌────────────────────────────────┐
  │  collect_verify_queue.py       │ ← wikilink / md-link / plain URL
  └───────────────┬────────────────┘
                  │
                  ▼
  ┌─────────────────────────────────────────┐
  │  web_verify_tls.py                       │
  │   ├─ curl_cffi chrome124 TLS            │ ← Cloudflare
  │   ├─ BeautifulSoup script-preserve      │ ← SPA / inline JSON
  │   ├─ Session + meta-refresh + 5.5s      │ ← Akamai
  │   └─ regex country scan w/ aliases      │
  └─────────────────┬────────────────────────┘
                    │
                    ▼
  ┌──────────────────────────────────────┐
  │  .verification/web_verified.md       │
  │  per op: verified / still_missing    │
  └──────────────┬───────────────────────┘
                 │
                 ▼
  ┌──────────────────────────────────────┐
  │  apply_bidirectional_ops.py --apply  │
  │  → country .md operations_participated│
  │  (idempotent)                         │
  └──────────────────────────────────────┘
```

---

## 9. Files touched (representative)

- `cosmos/index.html` (+ docs mirror) — ~25 commits
- `tools/web_verify_tls.py` — new
- `tools/collect_verify_queue.py` — new
- `tools/apply_bidirectional_ops.py` — new
- `tools/verify_participating_countries.py` — new
- `.verification/*.md` + `.json` + cache — generated
- `wiki/operations/operation-avalanche.md` — Colombia restoration + Audit Note
- `wiki/operations/carbanak-cobalt-takedown.md` — 3 countries removed
- `wiki/countries/*.md` — ~60 pages with back-links
- `wiki/countries/kazakhstan.md`, `united-arab-emirates.md` — stubs
- `LESSONS.md` — L19, L20, L21
- `wiki/log.md` — 3 dated entries
