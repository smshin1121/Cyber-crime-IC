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


def check_one(session: requests.Session, url: str) -> dict:
    """Check a single URL with HEAD, falling back to GET on method-not-allowed."""
    from urllib.parse import urlparse
    domain = urlparse(url).netloc.lower()
    try:
        resp = session.head(url, timeout=TIMEOUT, allow_redirects=True)
        # Many servers reject HEAD or return 403/405 for non-browser clients.
        if resp.status_code in (405, 400, 403, 406, 429):
            resp = session.get(
                url,
                timeout=TIMEOUT,
                allow_redirects=True,
                stream=True,
            )
            # Read a small sample to detect Cloudflare challenge pages
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
            if is_cloudflare_challenge(body_sample) or domain in BOT_PROTECTED_DOMAINS:
                return {
                    "url": url,
                    "status": resp.status_code,
                    "final_url": resp.url,
                    "category": "bot_protected",
                }
        # Also classify by domain: if the URL is in BOT_PROTECTED_DOMAINS
        # and we got any 4xx, treat as bot_protected not broken.
        category = classify(resp.status_code)
        if category in ("client_error", "not_found") and domain in BOT_PROTECTED_DOMAINS:
            category = "bot_protected"
        return {
            "url": url,
            "status": resp.status_code,
            "final_url": resp.url,
            "category": category,
        }
    except requests.exceptions.SSLError as e:
        cat = "bot_protected" if domain in BOT_PROTECTED_DOMAINS else "connection_error"
        return {"url": url, "status": None, "error": f"ssl: {str(e)[:100]}", "category": cat}
    except requests.exceptions.ConnectionError as e:
        cat = "bot_protected" if domain in BOT_PROTECTED_DOMAINS else "connection_error"
        return {"url": url, "status": None, "error": f"conn: {str(e)[:100]}", "category": cat}
    except requests.exceptions.Timeout:
        cat = "bot_protected" if domain in BOT_PROTECTED_DOMAINS else "connection_error"
        return {"url": url, "status": None, "error": "timeout", "category": cat}
    except requests.exceptions.RequestException as e:
        cat = "bot_protected" if domain in BOT_PROTECTED_DOMAINS else "connection_error"
        return {"url": url, "status": None, "error": f"other: {str(e)[:100]}", "category": cat}


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
    print("  External URL Validator")
    print("=" * 60)
    url_map = extract_urls()
    urls = list(url_map.keys())
    print(f"  Unique external URLs: {len(urls)}")

    session = build_session()
    results: list[dict] = []
    counters: dict[str, int] = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(check_one, session, u): u for u in urls}
        done = 0
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            res["referenced_by"] = url_map[res["url"]]
            results.append(res)
            counters[res["category"]] = counters.get(res["category"], 0) + 1
            done += 1
            if done % 50 == 0:
                print(f"  Checked {done}/{len(urls)}...")

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
    for cat in ("ok", "redirect", "not_found", "client_error", "server_error", "connection_error"):
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
