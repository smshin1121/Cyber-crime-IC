from __future__ import annotations

import json
import re
from http.cookiejar import CookieJar
from typing import Optional
from urllib.parse import urljoin
from urllib.error import HTTPError
from urllib.request import HTTPCookieProcessor, Request, build_opener


USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


class DOJClient:
    def __init__(self) -> None:
        self.cookies = CookieJar()
        self.opener = build_opener(HTTPCookieProcessor(self.cookies))

    def _request(self, url: str, *, method: str = "GET", data: bytes | None = None, referer: str | None = None) -> str:
        req = Request(url, data=data, method=method)
        req.add_header("User-Agent", USER_AGENT)
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
        if data is not None:
            req.add_header("Content-Type", "application/json")
        if referer:
            req.add_header("Referer", referer)
        try:
            with self.opener.open(req, timeout=60) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            return exc.read().decode("utf-8", errors="replace")

    def _solve_interstitial(self, base_url: str, html: str) -> Optional[str]:
        bm_match = re.search(r'"bm-verify"\s*:\s*"([^"]+)"', html)
        i_match = re.search(r"var i = (\d+);", html)
        n_match = re.search(r'Number\("(\d+)" \+ "(\d+)"\)', html)
        if not (bm_match and i_match and n_match):
            return None
        bm_verify = bm_match.group(1)
        pow_value = int(i_match.group(1)) + int(n_match.group(1) + n_match.group(2))
        verify_url = urljoin(base_url, "/_sec/verify?provider=interstitial")
        payload = json.dumps({"bm-verify": bm_verify, "pow": pow_value}).encode("utf-8")
        response = self._request(verify_url, method="POST", data=payload, referer=base_url)
        try:
            data = json.loads(response)
        except json.JSONDecodeError:
            return None
        if data.get("location"):
            return urljoin(base_url, str(data["location"]))
        return base_url

    def fetch(self, url: str) -> str:
        html = self._request(url)
        if "Akamai" not in html or "/_sec/verify?provider=interstitial" not in html:
            return html
        resolved = self._solve_interstitial(url, html)
        if not resolved:
            return html
        return self._request(resolved, referer=url)
