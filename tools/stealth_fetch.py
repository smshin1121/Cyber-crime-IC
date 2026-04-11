"""
Unified stealth fetcher for the IC wiki project.

Provides a 3-tier fetching strategy:
  1. urllib (fast, zero-dependency, for APIs/RSS feeds)
  2. Scrapling Fetcher (curl_cffi-based, browser impersonation)
  3. Camoufox StealthyFetcher (Firefox fork, C++ fingerprint spoofing)

Domain-aware routing: known bot-protected domains skip directly to
the stealth tier. Unknown domains try fast path first, escalate on
Cloudflare challenge detection.

Usage:
  from tools.stealth_fetch import SmartFetcher
  fetcher = SmartFetcher()
  result = fetcher.fetch("https://www.europol.europa.eu/...")
  if result:
      print(result.body[:200])
      print(f"Fetched via: {result.fetcher_used}")
"""
from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Protocol
from urllib.parse import urlparse
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError


# ---------------------------------------------------------------------------
# Result type
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FetchResult:
    url: str
    status_code: int | None
    body: str
    fetcher_used: str       # "urllib" | "scrapling" | "camoufox"
    is_challenge: bool      # True if Cloudflare challenge detected
    elapsed_ms: int


# ---------------------------------------------------------------------------
# Bot-protected domains (from check_external_urls.py L11/L13)
# ---------------------------------------------------------------------------

BOT_PROTECTED_DOMAINS: set[str] = {
    # International organizations
    "coe.int", "www.coe.int", "rm.coe.int", "search.coe.int",
    "interpol.int", "www.interpol.int",
    "europol.europa.eu", "www.europol.europa.eu",
    "eurojust.europa.eu", "www.eurojust.europa.eu",
    "enisa.europa.eu", "www.enisa.europa.eu",
    # US government
    "justice.gov", "www.justice.gov",
    "fbi.gov", "www.fbi.gov",
    "ice.gov", "www.ice.gov",
    "treasury.gov", "home.treasury.gov",
    "cisa.gov", "www.cisa.gov",
    "state.gov", "www.state.gov",
    # UK
    "nationalcrimeagency.gov.uk", "www.nationalcrimeagency.gov.uk",
    "ncsc.gov.uk", "www.ncsc.gov.uk",
    # Other government
    "rcmp-grc.gc.ca", "www.rcmp-grc.gc.ca",
    "bka.de", "www.bka.de",
    "politie.nl", "www.politie.nl",
    "afp.gov.au", "www.afp.gov.au",
    "npa.go.jp", "www.npa.go.jp",
    # Media (known to block bots)
    "wired.com", "www.wired.com",
    "bbc.com", "www.bbc.com", "bbc.co.uk", "www.bbc.co.uk",
    "reuters.com", "www.reuters.com",
    "nytimes.com", "www.nytimes.com",
    "washingtonpost.com", "www.washingtonpost.com",
    # Security vendors
    "group-ib.com", "www.group-ib.com",
    "recordedfuture.com", "www.recordedfuture.com",
    # Korean
    "police.go.kr", "www.police.go.kr",
    "spo.go.kr", "www.spo.go.kr",
}


# ---------------------------------------------------------------------------
# Cloudflare challenge detection
# ---------------------------------------------------------------------------

CHALLENGE_SIGNATURES = [
    "just a moment",
    "challenge-platform",
    "cf-browser-verification",
    "checking your browser",
    "enable javascript and cookies",
    "ray id:",
    "cloudflare",
    "please wait while we verify",
]


def _is_challenge(body: str) -> bool:
    """Detect Cloudflare/Akamai challenge pages."""
    if not body or len(body) > 50_000:
        return False
    lower = body[:5000].lower()
    return sum(1 for sig in CHALLENGE_SIGNATURES if sig in lower) >= 2


# ---------------------------------------------------------------------------
# Fetcher: urllib (Tier 1 — fast, zero-dependency)
# ---------------------------------------------------------------------------

class UrllibFetcher:
    """Basic urllib fetcher. Works for RSS feeds, APIs, and unprotected pages."""

    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    )

    def fetch(self, url: str, timeout: int = 15) -> FetchResult | None:
        t0 = time.monotonic()
        try:
            req = Request(url, headers={
                "User-Agent": self.USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
            })
            with urlopen(req, timeout=timeout) as resp:
                body = resp.read().decode("utf-8", errors="replace")
                elapsed = int((time.monotonic() - t0) * 1000)
                challenge = _is_challenge(body)
                return FetchResult(
                    url=url,
                    status_code=resp.status,
                    body=body,
                    fetcher_used="urllib",
                    is_challenge=challenge,
                    elapsed_ms=elapsed,
                )
        except (URLError, HTTPError, TimeoutError, OSError):
            return None


# ---------------------------------------------------------------------------
# Fetcher: Scrapling (Tier 2 — curl_cffi browser impersonation)
# ---------------------------------------------------------------------------

class ScraplingFetcher:
    """Scrapling Fetcher with curl_cffi browser impersonation."""

    def __init__(self) -> None:
        from scrapling import Fetcher as _Fetcher  # type: ignore
        self._fetcher_cls = _Fetcher

    def fetch(self, url: str, timeout: int = 20) -> FetchResult | None:
        t0 = time.monotonic()
        try:
            page = self._fetcher_cls.get(
                url,
                stealthy_headers=True,
                follow_redirects=True,
                timeout=timeout,
            )
            body = page.html_content if hasattr(page, "html_content") else str(page)
            elapsed = int((time.monotonic() - t0) * 1000)
            status = page.status if hasattr(page, "status") else 200
            challenge = _is_challenge(body)
            return FetchResult(
                url=url,
                status_code=status,
                body=body,
                fetcher_used="scrapling",
                is_challenge=challenge,
                elapsed_ms=elapsed,
            )
        except Exception as e:
            print(f"  [scrapling] Failed {url}: {e}")
            return None


# ---------------------------------------------------------------------------
# Fetcher: Camoufox (Tier 3 — Firefox fork, C++ fingerprint spoofing)
# ---------------------------------------------------------------------------

class CamoufoxFetcher:
    """Camoufox stealth browser — Firefox fork with real fingerprint spoofing."""

    def __init__(self) -> None:
        from camoufox.sync_api import Camoufox  # type: ignore
        self._camoufox_cls = Camoufox

    def fetch(self, url: str, timeout: int = 30) -> FetchResult | None:
        t0 = time.monotonic()
        try:
            with self._camoufox_cls(headless=True) as browser:
                page = browser.new_page()
                page.goto(url, timeout=timeout * 1000, wait_until="domcontentloaded")
                body = page.content()
                elapsed = int((time.monotonic() - t0) * 1000)
                challenge = _is_challenge(body)
                return FetchResult(
                    url=url,
                    status_code=200,
                    body=body,
                    fetcher_used="camoufox",
                    is_challenge=challenge,
                    elapsed_ms=elapsed,
                )
        except Exception as e:
            print(f"  [camoufox] Failed {url}: {e}")
            return None


# ---------------------------------------------------------------------------
# SmartFetcher — domain-aware routing with auto-escalation
# ---------------------------------------------------------------------------

class SmartFetcher:
    """Unified fetcher with 3-tier fallback and domain-aware routing.

    For known bot-protected domains: skip urllib, go straight to scrapling/camoufox.
    For unknown domains: try urllib first, escalate on challenge detection.
    """

    def __init__(
        self,
        bot_protected_domains: set[str] | None = None,
        enable_camoufox: bool = True,
    ) -> None:
        self._domains = bot_protected_domains or BOT_PROTECTED_DOMAINS.copy()
        self._urllib = UrllibFetcher()
        self._scrapling: ScraplingFetcher | None = None
        self._camoufox: CamoufoxFetcher | None = None
        self._enable_camoufox = enable_camoufox
        self._scrapling_available: bool | None = None
        self._camoufox_available: bool | None = None

    def fetch(self, url: str, timeout: int = 15) -> FetchResult | None:
        """Fetch a URL with automatic strategy selection."""
        domain = urlparse(url).netloc.lower()

        # Fast path: known bot-protected domain → skip to stealth
        if any(domain == d or domain.endswith("." + d) for d in self._domains):
            result = self._try_scrapling(url, timeout + 10)
            if result and not result.is_challenge:
                return result
            # Scrapling failed or still challenge → try camoufox
            if self._enable_camoufox:
                result = self._try_camoufox(url, timeout + 15)
                if result and not result.is_challenge:
                    return result
            return result  # Return whatever we got (may be None or challenge)

        # Normal path: try urllib first
        result = self._urllib.fetch(url, timeout)
        if result and not result.is_challenge:
            return result

        # Challenge detected or failure → escalate to scrapling
        stealth_result = self._try_scrapling(url, timeout + 10)
        if stealth_result and not stealth_result.is_challenge:
            # Auto-learn: add this domain for future fast-path
            self._domains.add(domain)
            return stealth_result

        # Last resort: camoufox
        if self._enable_camoufox:
            camo_result = self._try_camoufox(url, timeout + 15)
            if camo_result and not camo_result.is_challenge:
                self._domains.add(domain)
                return camo_result
            return camo_result

        return stealth_result or result

    def _try_scrapling(self, url: str, timeout: int) -> FetchResult | None:
        if self._scrapling_available is False:
            return None
        if self._scrapling is None:
            try:
                self._scrapling = ScraplingFetcher()
                self._scrapling_available = True
            except ImportError:
                self._scrapling_available = False
                return None
        return self._scrapling.fetch(url, timeout)

    def _try_camoufox(self, url: str, timeout: int) -> FetchResult | None:
        if self._camoufox_available is False:
            return None
        if self._camoufox is None:
            try:
                self._camoufox = CamoufoxFetcher()
                self._camoufox_available = True
            except ImportError:
                self._camoufox_available = False
                return None
        return self._camoufox.fetch(url, timeout)


# ---------------------------------------------------------------------------
# Convenience function (drop-in replacement for auto_collect.fetch_url)
# ---------------------------------------------------------------------------

_default_fetcher: SmartFetcher | None = None


def smart_fetch(url: str, timeout: int = 15) -> str | None:
    """Drop-in replacement for auto_collect.fetch_url().

    Returns the page body as a string, or None on failure.
    """
    global _default_fetcher
    if _default_fetcher is None:
        _default_fetcher = SmartFetcher()
    result = _default_fetcher.fetch(url, timeout)
    if result is None:
        return None
    return result.body


# ---------------------------------------------------------------------------
# CLI self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    test_urls = [
        "https://www.europol.europa.eu/media-press/newsroom/news",
        "https://www.interpol.int/en/News-and-Events/News",
        "https://api.openalex.org/works?search=cybercrime&per-page=1",
    ]

    if len(sys.argv) > 1:
        test_urls = sys.argv[1:]

    fetcher = SmartFetcher()
    for url in test_urls:
        print(f"\n--- {url}")
        result = fetcher.fetch(url)
        if result:
            print(f"  Status: {result.status_code}")
            print(f"  Fetcher: {result.fetcher_used}")
            print(f"  Challenge: {result.is_challenge}")
            print(f"  Elapsed: {result.elapsed_ms}ms")
            print(f"  Body: {len(result.body)} chars")
            print(f"  Preview: {result.body[:150]}...")
        else:
            print("  [FAIL] No result")
