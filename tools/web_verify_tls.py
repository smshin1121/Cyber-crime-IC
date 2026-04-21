"""
TLS-spoofing variant of web_verify_countries.py — same pipeline, but
uses curl_cffi (Chrome TLS fingerprint impersonation) instead of a
full browser. Much faster than Playwright and bypasses Cloudflare on
most static press-release pages (Europol, Eurojust, INTERPOL, DOJ
archive, FBI, national CERTs).

Falls back to a `NotFetchable` marker if Cloudflare challenge is
unresolved or the status is non-200.

Run:
    python tools/web_verify_tls.py --limit 30
"""
from __future__ import annotations
import argparse
import json
import re
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from curl_cffi import requests as cffi_requests
from bs4 import BeautifulSoup
import yaml


ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / ".verification" / "verify_queue.json"
COUNTRIES_DIR = ROOT / "wiki" / "countries"
OUT = ROOT / ".verification" / "web_verified.md"
RAW_CACHE = ROOT / ".verification" / "web_cache"
RAW_CACHE.mkdir(parents=True, exist_ok=True)

IMPERSONATE = "chrome124"
REQUEST_TIMEOUT = 25


@dataclass
class CountryProfile:
    slug: str
    title: str
    aliases: list[str]

    def patterns(self) -> list[re.Pattern[str]]:
        # manual aliases (from ALIAS_OVERRIDES + frontmatter) are trusted even
        # if short (e.g., "UK", "US", "UAE"); auto-derived forms keep >=3 guard
        manual = {self.title, *self.aliases}
        manual.discard("")
        derived = {self.slug.replace("-", " ")}
        derived -= manual
        pats: list[re.Pattern[str]] = []
        seen: set[str] = set()
        for n in sorted(manual | derived, key=len, reverse=True):
            if n in seen:
                continue
            if n in derived and len(n) < 3:
                continue
            if len(n) < 2:
                continue
            seen.add(n)
            # Case-sensitive for all-caps 2-letter tokens to avoid false-
            # positive matches on common English words (e.g., "us"/"uk").
            flags = 0 if (len(n) <= 3 and n.isupper()) else re.IGNORECASE
            pats.append(re.compile(r"\b" + re.escape(n) + r"\b", flags))
        return pats


ALIAS_OVERRIDES: dict[str, list[str]] = {
    "united-states": ["US", "USA", "U.S.", "U.S.A.", "America", "American",
                       "Vereinigte Staaten", "Etats-Unis"],
    "united-kingdom": ["UK", "U.K.", "Britain", "British",
                        "Vereinigtes Königreich", "Royaume-Uni"],
    "lithuania": ["Litauen", "Lituanie", "Lithuanian"],
    "latvia": ["Lettland", "Lettonie", "Latvian"],
    "estonia": ["Estland", "Estonie", "Estonian"],
    "netherlands": ["Dutch", "Holland"],
    "germany": ["German"],
    "france": ["French"],
    "italy": ["Italian"],
    "spain": ["Spanish"],
    "russia": ["Russian"],
    "china": ["Chinese", "PRC"],
    "japan": ["Japanese"],
    "south-korea": ["Korea", "Korean", "Republic of Korea", "ROK"],
    "north-korea": ["DPRK"],
    "united-arab-emirates": ["UAE", "U.A.E.", "Emirates"],
    "vietnam": ["Viet Nam"],
    "kazakhstan": ["Kazakh"],
    "kyrgyzstan": ["Kyrgyz"],
    "tajikistan": ["Tajik"],
    "uzbekistan": ["Uzbek"],
    "czech-republic": ["Czechia", "Czech"],
    "czechia": ["Czech Republic", "Czech"],
    "cote-divoire": ["Ivory Coast", "Côte d'Ivoire"],
    "hong-kong": ["Hong Kong"],
    "saudi-arabia": ["Saudi Arabia", "KSA"],
    "new-zealand": ["New Zealand"],
    "south-africa": ["South Africa"],
    "bosnia-and-herzegovina": ["Bosnia", "Herzegovina", "BiH"],
    "eu-member-states": ["European Union", "EU"],
}


def _fm(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}
    return fm if isinstance(fm, dict) else {}


def build_country_index() -> dict[str, CountryProfile]:
    out: dict[str, CountryProfile] = {}
    for md in COUNTRIES_DIR.glob("*.md"):
        if md.name.startswith("_"):
            continue
        fm = _fm(md)
        slug = md.stem
        title = str(fm.get("title") or slug).strip()
        # strip leading "Republic of", "Kingdom of", etc. to match shorter forms
        aliases: list[str] = []
        aliases_raw = fm.get("aliases") or []
        if isinstance(aliases_raw, str):
            aliases_raw = [aliases_raw]
        aliases.extend(str(a).strip() for a in aliases_raw if a)
        short = re.sub(r"^(Republic of|Kingdom of|Federal Republic of|"
                       r"People's Republic of|State of|Commonwealth of|"
                       r"Principality of)\s+", "", title, flags=re.IGNORECASE).strip()
        if short and short != title:
            aliases.append(short)
        aliases.extend(ALIAS_OVERRIDES.get(slug, []))
        out[slug] = CountryProfile(slug=slug, title=title, aliases=aliases)
    return out


def cache_path(url: str) -> Path:
    h = re.sub(r"[^a-z0-9]+", "-", url.lower())[:150]
    return RAW_CACHE / f"{h}.txt"


def fetch_text(url: str) -> tuple[str, str | None]:
    """Return (text, error). Uses cache if present."""
    cache = cache_path(url)
    if cache.exists() and cache.stat().st_size > 200:
        return cache.read_text(encoding="utf-8", errors="replace"), None
    try:
        sess = cffi_requests.Session()
        r = sess.get(url, impersonate=IMPERSONATE,
                     timeout=REQUEST_TIMEOUT, allow_redirects=True)
    except Exception as exc:  # noqa: BLE001
        return "", f"fetch_error: {str(exc)[:150]}"
    if r.status_code != 200:
        return "", f"http_{r.status_code}"
    html = r.text
    low = html.lower()
    # Akamai Bot Manager challenge: page is ~3KB with a meta-refresh pointing
    # to the same URL plus a bm-verify cookie now set in the session. Wait a
    # few seconds and retry with the same session.
    if "bm-verify" in low and "meta http-equiv=\"refresh\"" in low and len(html) < 8000:
        m = re.search(r'content="[0-9]+;\s*URL=\'([^\']+)', html, re.IGNORECASE)
        if m:
            redirect = m.group(1)
            if redirect.startswith("/"):
                from urllib.parse import urlparse
                root = urlparse(url)
                redirect = f"{root.scheme}://{root.netloc}{redirect}"
            time.sleep(5.5)
            try:
                r = sess.get(redirect, impersonate=IMPERSONATE,
                             timeout=REQUEST_TIMEOUT, allow_redirects=True)
                if r.status_code == 200 and len(r.text) > 8000:
                    html = r.text
                    low = html.lower()
            except Exception:
                pass
    if "just a moment" in low and "cf-chl" in low and len(html) < 20000:
        return "", "cloudflare_challenge"
    if "bm-verify" in low and len(html) < 8000:
        return "", "akamai_challenge"
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["style", "noscript", "svg"]):
        tag.decompose()
    # keep <script> content: for React SPAs like Europol, the country
    # roster is embedded as a JSON string inside inline scripts.
    # get_text with a separator still gives us textual content for regex.
    text = soup.get_text(separator=" ", strip=True)
    # Europol SPA: if visible text is just "Loading application", also
    # pull script bodies directly.
    if "loading application" in text.lower() and len(text) < 600:
        script_blobs = " ".join(s.get_text(" ", strip=True)
                                for s in BeautifulSoup(html, "html.parser")
                                .find_all("script"))
        text = f"{text}\n[SCRIPT_BLOB]\n{script_blobs}\n[END]"
    if len(text) < 100:
        return "", "empty_body"
    cache.write_text(text, encoding="utf-8")
    return text, None


def scan(text: str, countries: dict[str, CountryProfile],
         candidates: list[str]) -> dict[str, bool]:
    out: dict[str, bool] = {}
    for slug in candidates:
        p = countries.get(slug)
        if not p:
            out[slug] = False
            continue
        out[slug] = any(pat.search(text) for pat in p.patterns())
    return out


def verify_op(op: dict, countries: dict[str, CountryProfile]) -> dict:
    results: list[dict] = []
    hits_union: set[str] = set()
    pc = op["participating_countries"]
    for src in op["source_urls"]:
        url = src["url"]
        text, err = fetch_text(url)
        if text:
            hits = scan(text, countries, pc)
            found = [c for c, f in hits.items() if f]
            hits_union.update(found)
            results.append({
                "url": url,
                "publisher": src.get("publisher", ""),
                "char_count": len(text),
                "found": found,
                "missing": [c for c, f in hits.items() if not f],
                "error": None,
            })
        else:
            results.append({
                "url": url,
                "publisher": src.get("publisher", ""),
                "char_count": 0,
                "found": [],
                "missing": list(pc),
                "error": err,
            })
        time.sleep(1.5)  # polite rate limiting
    return {
        "op_slug": op["op_slug"],
        "op_title": op["op_title"],
        "pc": pc,
        "verified_union": sorted(hits_union),
        "still_missing": sorted(set(pc) - hits_union),
        "sources": results,
    }


def render_report(entries: list[dict]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# participating_countries — web primary-source verification (curl_cffi)",
        "",
        f"_Run: {now}_",
        "",
        "Fetched via curl_cffi with Chrome TLS fingerprint impersonation "
        "(bypasses Cloudflare on most static press releases). For each op "
        "in the verification queue, every country in its "
        "`participating_countries` is checked against the rendered text of "
        "all cited source URLs.",
        "",
        "- **verified_union** — country explicitly named in ≥1 source page",
        "- **still_missing** — country NOT found in any reachable source",
        "- Fetch errors (Cloudflare challenge still unsolved, 403, 404 etc.) "
        "are recorded per URL",
        "",
    ]
    total = len(entries)
    fully = [e for e in entries if not e["still_missing"] and e["pc"]]
    partial = [e for e in entries if e["still_missing"] and e["verified_union"]]
    none_verified = [e for e in entries if not e["verified_union"]]
    lines += [
        "## Summary",
        "",
        f"- Operations processed: {total}",
        f"- Fully verified (every frontmatter country named in a source): {len(fully)}",
        f"- Partially verified: {len(partial)}",
        f"- Nothing verified (all sources failed): {len(none_verified)}",
        "",
        "## Results",
        "",
    ]
    for e in entries:
        lines += [f"### {e['op_slug']}", ""]
        lines.append(f"**Title**: {e['op_title']}")
        lines.append("")
        lines.append(f"**Participating (frontmatter, {len(e['pc'])})**: "
                     f"{', '.join(e['pc']) or '—'}")
        lines.append("")
        lines.append(f"**Verified via web ({len(e['verified_union'])})**: "
                     f"{', '.join(e['verified_union']) or '—'}")
        lines.append("")
        lines.append(f"**Still missing ({len(e['still_missing'])})**: "
                     f"{', '.join(e['still_missing']) or '—'}")
        lines.append("")
        lines.append("| URL | Publisher | Chars | Found | Error |")
        lines.append("|---|---|---:|---|---|")
        for s in e["sources"]:
            lines.append(
                f"| {s['url'][:80]} | {s.get('publisher','')} | "
                f"{s.get('char_count',0)} | "
                f"{', '.join(s.get('found',[]))[:120]} | "
                f"{s.get('error') or ''} |"
            )
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--op", type=str, default=None)
    args = ap.parse_args()

    if not QUEUE.exists():
        print(f"[tls-verify] missing {QUEUE}", file=sys.stderr)
        return 1
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))
    if args.op:
        queue = [q for q in queue if q["op_slug"] == args.op]
    elif args.limit:
        queue = queue[: args.limit]

    countries = build_country_index()
    print(f"[tls-verify] processing {len(queue)} ops", flush=True)

    entries: list[dict] = []
    for i, op in enumerate(queue, 1):
        print(f"[tls-verify] ({i}/{len(queue)}) {op['op_slug']} — "
              f"{len(op['source_urls'])} URL(s)", flush=True)
        result = verify_op(op, countries)
        entries.append(result)
        OUT.write_text(render_report(entries), encoding="utf-8")
        v = len(result["verified_union"])
        m = len(result["still_missing"])
        print(f"              verified={v}, still_missing={m}", flush=True)

    print(f"[tls-verify] report -> {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
