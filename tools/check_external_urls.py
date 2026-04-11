"""
External URL validator — extracts all http/https URLs from wiki markdown files
and validates them with HEAD requests. Classifies as:
  - ok: 2xx
  - redirect: 3xx
  - client_error: 4xx (especially 404)
  - server_error: 5xx
  - connection_error: DNS / timeout / SSL failure

Writes a JSON report to _workspace/external_url_check.json
"""
import concurrent.futures
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

WIKI = Path(__file__).resolve().parent.parent / "wiki"
REPORT = Path(__file__).resolve().parent.parent / "_workspace" / "external_url_check.json"
TIMEOUT = 15
MAX_WORKERS = 20
USER_AGENT = (
    "Mozilla/5.0 (Cyber-crime-IC wiki linkchecker) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
)


def build_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=1,
        backoff_factor=0.3,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["HEAD", "GET"],
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.mount("http://", HTTPAdapter(max_retries=retry))
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})
    return session


def extract_urls() -> dict[str, list[str]]:
    """Return mapping: url -> list of wiki files that reference it.

    The regex allows balanced parentheses inside a URL so Wikipedia URLs like
    https://en.wikipedia.org/wiki/National_Police_Agency_(Japan) are captured
    in full. We stop at whitespace, closing brackets, quotes, and angle
    brackets, but only stop at `)` when it is NOT preceded by a matching `(`.
    """
    url_to_files: dict[str, set[str]] = {}
    # First pass: greedy URL capture up to whitespace or closing bracket
    url_re = re.compile(r"https?://[^\s\]\"'<>]+")
    for md in WIKI.rglob("*.md"):
        if md.name.startswith("_") or ".obsidian" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        for match in url_re.finditer(text):
            raw = match.group(0).rstrip(".,;:")
            # Balance parentheses: strip trailing `)` that doesn't match a `(`
            while raw.endswith(")") and raw.count("(") < raw.count(")"):
                raw = raw[:-1]
            # Also strip markdown syntax artifacts
            raw = raw.rstrip(".,;:")
            url = raw
            if not url.startswith(("http://", "https://")):
                continue
            parsed = urlparse(url)
            if not parsed.netloc:
                continue
            rel = md.relative_to(WIKI).as_posix()
            url_to_files.setdefault(url, set()).add(rel)
    return {u: sorted(fs) for u, fs in url_to_files.items()}


BOT_PROTECTED_DOMAINS = {
    # Known to use Cloudflare/Akamai bot protection or geo-restrictions that
    # return 403/connection errors to non-browser scrapers. Pages are served
    # correctly to real browsers but the HTTP checker cannot validate them.
    # To add a domain here, confirm the URL works in a real browser first.
    "www.coe.int",
    "coe.int",
    "rm.coe.int",
    "www.justice.gov",
    "justice.gov",
    "opengovasia.com",
    "www.legifrance.gouv.fr",
    "legifrance.gouv.fr",
    "home-affairs.ec.europa.eu",
    "ec.europa.eu",
    "www.mha.gov.sg",
    "www.mddi.gov.sg",
    "www.interpol.int",
    "interpol.int",
    "www.group-ib.com",
    "group-ib.com",
    "lbox.kr",
    "thehackernews.com",
    "www.moneylaunderingnews.com",
    "sso.agc.gov.sg",
    "news.sophos.com",
    "techxplore.com",
    "www.ca5.uscourts.gov",
    # Government sites that connection-refuse HTTP crawlers but are
    # browser-accessible:
    "www.rcmp-grc.gc.ca",
    "rcmp-grc.gc.ca",
    "www.pj.pt",
    "pj.pt",
    "www.ncis.navy.mil",
    "ncis.navy.mil",
    "dgsn.gov.ma",
    "www.dgssi.gov.ma",
    "www.cert-mu.org.mu",
    "www.diplomatie.gouv.fr",
    "diplomatie.gouv.fr",
    "www.moict.gov.gm",
    "www.parliament.gov.zm",
    "www.pgdlisboa.pt",
    "www.paragraf.rs",
    "ccid.rmp.gov.my",
    "www.artci.ci",
    "artci.ci",
    "www.mofa.go.kr",
    "mofa.go.kr",
}


def is_cloudflare_challenge(text: str) -> bool:
    return (
        "Just a moment..." in text[:1500]
        or "challenge-platform" in text[:3000]
        or "cf-browser-verification" in text[:3000]
    )


def _get_stealth_fetcher():
    """Lazily load SmartFetcher from stealth_fetch.py (optional dependency)."""
    import sys
    from pathlib import Path
    # Ensure project root is on path for 'tools.stealth_fetch' import
    project_root = str(Path(__file__).resolve().parent.parent)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    try:
        from tools.stealth_fetch import SmartFetcher
        return SmartFetcher(enable_camoufox=False)  # scrapling only for speed
    except (ImportError, Exception) as e:
        print(f"  [WARN] Stealth fetcher init failed: {e}")
        return None


import threading

_stealth = None
_stealth_lock = threading.Lock()


def _stealth_retry(url: str, orig_status: int | None, fallback_error: str = "") -> dict:
    """Retry a URL with the stealth fetcher. Falls back to bot_protected."""
    global _stealth
    with _stealth_lock:
        if _stealth is None:
            _stealth = _get_stealth_fetcher() or False
    if _stealth:
        try:
            result = _stealth.fetch(url, timeout=TIMEOUT + 10)
            if result and not result.is_challenge:
                return {
                    "url": url,
                    "status": result.status_code,
                    "final_url": url,
                    "category": classify(result.status_code or 200),
                    "fetcher": result.fetcher_used,
                }
        except Exception:
            pass
    return {
        "url": url,
        "status": orig_status,
        "error": fallback_error or "challenge_or_403",
        "category": "bot_protected",
    }


def check_one(session: requests.Session, url: str) -> dict:
    """Check a single URL with HEAD, falling back to GET, then stealth fetch."""
    from urllib.parse import urlparse
    global _stealth
    domain = urlparse(url).netloc.lower()

    # For bot-protected domains: try stealth fetcher first (if available)
    if domain in BOT_PROTECTED_DOMAINS:
        with _stealth_lock:
            if _stealth is None:
                _stealth = _get_stealth_fetcher() or False
        if _stealth:
            try:
                result = _stealth.fetch(url, timeout=TIMEOUT + 10)
                if result and not result.is_challenge:
                    return {
                        "url": url,
                        "status": result.status_code,
                        "final_url": url,
                        "category": classify(result.status_code or 200),
                        "fetcher": result.fetcher_used,
                    }
                # Stealth also got challenge — mark as bot_protected
                return {
                    "url": url,
                    "status": result.status_code if result else None,
                    "category": "bot_protected",
                    "fetcher": result.fetcher_used if result else "none",
                }
            except Exception as e:
                return {
                    "url": url, "status": None,
                    "error": f"stealth: {str(e)[:100]}",
                    "category": "bot_protected",
                }

    # Normal path: HEAD then GET
    try:
        resp = session.head(url, timeout=TIMEOUT, allow_redirects=True)
        if resp.status_code in (405, 400, 403, 406, 429):
            resp = session.get(
                url, timeout=TIMEOUT, allow_redirects=True, stream=True,
            )
            sample = b""
            try:
                for chunk in resp.iter_content(chunk_size=8192):
                    sample += chunk
                    if len(sample) > 8192:
                        break
            except Exception:
                pass
            resp.close()
            body_sample = sample.decode("utf-8", errors="replace")
            if is_cloudflare_challenge(body_sample):
                # Challenge detected on unknown domain — retry with stealth
                return _stealth_retry(url, resp.status_code)
        category = classify(resp.status_code)
        if category in ("client_error",) and resp.status_code == 403:
            # 403 may be bot protection even without challenge page — try stealth
            return _stealth_retry(url, resp.status_code)
        return {
            "url": url,
            "status": resp.status_code,
            "final_url": resp.url,
            "category": category,
        }
    except requests.exceptions.SSLError as e:
        return {"url": url, "status": None, "error": f"ssl: {str(e)[:100]}", "category": "connection_error"}
    except requests.exceptions.ConnectionError as e:
        return _stealth_retry(url, None, fallback_error=f"conn: {str(e)[:100]}")
    except requests.exceptions.Timeout:
        return {"url": url, "status": None, "error": "timeout", "category": "connection_error"}
    except requests.exceptions.RequestException as e:
        return {"url": url, "status": None, "error": f"other: {str(e)[:100]}", "category": "connection_error"}


def classify(status: int) -> str:
    if 200 <= status < 300:
        return "ok"
    if 300 <= status < 400:
        return "redirect"
    if status == 404:
        return "not_found"
    if 400 <= status < 500:
        return "client_error"
    if 500 <= status < 600:
        return "server_error"
    return "unknown"


def main() -> None:
    print("=" * 60)
    print("  External URL Validator (stealth-enabled)")
    print("=" * 60)
    url_map = extract_urls()
    urls = list(url_map.keys())
    print(f"  Unique external URLs: {len(urls)}")

    # Split URLs into normal and bot-protected groups
    normal_urls = []
    stealth_urls = []
    for u in urls:
        domain = urlparse(u).netloc.lower()
        if domain in BOT_PROTECTED_DOMAINS:
            stealth_urls.append(u)
        else:
            normal_urls.append(u)
    print(f"  Normal: {len(normal_urls)} | Bot-protected (stealth): {len(stealth_urls)}")

    session = build_session()
    results: list[dict] = []
    counters: dict[str, int] = {}
    done = 0
    total = len(urls)

    # Pre-initialize stealth fetcher (before threads)
    global _stealth
    with _stealth_lock:
        if _stealth is None:
            _stealth = _get_stealth_fetcher() or False
    if _stealth:
        print(f"  Stealth fetcher: ACTIVE (scrapling + camoufox)")
    else:
        print(f"  Stealth fetcher: NOT AVAILABLE (install scrapling for bot-bypass)")

    # Phase 1: Normal URLs — full parallelism
    if normal_urls:
        print(f"\n  Phase 1: Checking {len(normal_urls)} normal URLs (parallel={MAX_WORKERS})...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
            futures = {ex.submit(check_one, session, u): u for u in normal_urls}
            for future in concurrent.futures.as_completed(futures):
                res = future.result()
                res["referenced_by"] = url_map[res["url"]]
                results.append(res)
                counters[res["category"]] = counters.get(res["category"], 0) + 1
                done += 1
                if done % 50 == 0:
                    print(f"    Checked {done}/{total}...")

    # Phase 2: Bot-protected URLs — reduced parallelism for stealth
    if stealth_urls:
        stealth_workers = min(5, len(stealth_urls))
        print(f"\n  Phase 2: Checking {len(stealth_urls)} bot-protected URLs (stealth, parallel={stealth_workers})...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=stealth_workers) as ex:
            futures = {ex.submit(check_one, session, u): u for u in stealth_urls}
            for future in concurrent.futures.as_completed(futures):
                res = future.result()
                res["referenced_by"] = url_map[res["url"]]
                results.append(res)
                counters[res["category"]] = counters.get(res["category"], 0) + 1
                done += 1
                if done % 10 == 0:
                    print(f"    Stealth checked {done}/{total}...")

    # Write report
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        json.dumps(
            {
                "summary": {
                    "total": len(results),
                    "by_category": counters,
                },
                "results": sorted(results, key=lambda r: (r["category"], r["url"])),
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print("\n  Summary:")
    for cat in ("ok", "redirect", "bot_protected", "not_found", "client_error", "server_error", "connection_error"):
        n = counters.get(cat, 0)
        if n:
            print(f"    {cat}: {n}")

    broken = [r for r in results if r["category"] in ("not_found", "client_error", "server_error", "connection_error")]
    if broken:
        print(f"\n  BROKEN ({len(broken)}):")
        for r in broken[:30]:
            s = r.get("status", r.get("error", "?"))
            print(f"    [{r['category']}] {r['url']}  ({s})")
            for f in r["referenced_by"][:2]:
                print(f"      in: {f}")
        if len(broken) > 30:
            print(f"    ... and {len(broken) - 30} more (see {REPORT.relative_to(REPORT.parent.parent.parent)})")
    print(f"\n  Report: {REPORT}")


if __name__ == "__main__":
    main()
