from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import html
import json
import re
import shutil
import ssl
import subprocess
import sys
import time
import threading
import unicodedata
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, quote, urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
RAW_DIR = ROOT / "raw"
REPORT_PATH = ROOT / "_workspace" / "source_text_harvest_report.json"
TODAY = datetime.now().strftime("%Y-%m-%d")

HARVEST_VENDOR = ROOT / "_workspace" / ".vendor_harvest"
if HARVEST_VENDOR.exists() and str(HARVEST_VENDOR) not in sys.path:
    sys.path.insert(0, str(HARVEST_VENDOR))

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

try:
    from stealth_fetch import SmartFetcher  # type: ignore
except Exception:  # pragma: no cover - optional dependency path
    SmartFetcher = None  # type: ignore

try:
    from doj_fetch import DOJClient  # type: ignore
except Exception:  # pragma: no cover - optional dependency path
    DOJClient = None  # type: ignore


USER_AGENT = (
    "Mozilla/5.0 (CyberCrimeIC source text harvester) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
)

URL_RE = re.compile(r"https?://[^\s\]\)>\"']+")
FRONTMATTER_URL_KEYS = ("collection_url", "source_url", "url")
TRACKING_QUERY_PREFIXES = ("utm_",)
TRACKING_QUERY_KEYS = {
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
    "ref",
    "source",
    "spm",
}

OFFICIAL_EXACT_DOMAINS = {
    "afp.gov.au",
    "atf.gov",
    "bmi.bund.de",
    "ccid.rmp.gov.my",
    "ccn-cert.cni.es",
    "cert.lv",
    "cert-mu.org.mu",
    "coe.int",
    "congress.gov",
    "courtlistener.com",
    "dea.gov",
    "dgssi.gov.ma",
    "dgsn.gov.ma",
    "diplomatie.gouv.fr",
    "direzioneinvestigativaantimafia.interno.gov.it",
    "eurojust.europa.eu",
    "europol.europa.eu",
    "fbi.gov",
    "fda.gov",
    "fiod.nl",
    "fiscalia.gov.co",
    "fondosicurezzainterna.interno.gov.it",
    "gendarmerie.interieur.gouv.fr",
    "gov.uk",
    "govinfo.gov",
    "hkreform.gov.hk",
    "ice.gov",
    "info.gov.hk",
    "interpol.int",
    "irs.gov",
    "justice.gov",
    "krcert.or.kr",
    "legco.gov.hk",
    "legifrance.gouv.fr",
    "mha.gov.sg",
    "mofa.go.kr",
    "msit.go.kr",
    "nacsa.gov.my",
    "nationalcrimeagency.gov.uk",
    "newsonair.gov.in",
    "npa.go.jp",
    "oig.dhs.gov",
    "oig.dol.gov",
    "oig.ssa.gov",
    "parliament.go.tz",
    "parliament.gov.zm",
    "police.go.kr",
    "police.gov.hk",
    "police.gov.mv",
    "police.gov.sg",
    "police.govmu.org",
    "police.govt.nz",
    "policia.gov.co",
    "politie.be",
    "politie.nl",
    "politi.dk",
    "politiet.no",
    "portugal.gov.pt",
    "rm.coe.int",
    "saps.gov.za",
    "sec.gov",
    "secretservice.gov",
    "spo.go.kr",
    "thaicert.or.th",
    "unodc.org",
    "uscc.gov",
    "uspis.gov",
    "vp.gov.lv",
    "zakon.rada.gov.ua",
}
OFFICIAL_SUFFIXES = (
    ".gov",
    ".gov.au",
    ".gov.br",
    ".gov.sg",
    ".gov.uk",
    ".gouv.fr",
    ".go.jp",
    ".go.kr",
    ".gc.ca",
    ".europa.eu",
    ".gov.hk",
    ".gov.it",
    ".gov.my",
    ".govt.nz",
)

BOILERPLATE_PATTERNS = (
    re.compile(r"^an official website of the united states government", re.I),
    re.compile(r"^official websites use \.gov", re.I),
    re.compile(r"^secure \.gov websites use https", re.I),
    re.compile(r"^share this page", re.I),
    re.compile(r"^breadcrumbs?$", re.I),
    re.compile(r"^skip to main content", re.I),
    re.compile(r"^subscribe", re.I),
)
CHALLENGE_SIGNATURES = (
    "just a moment",
    "challenge-platform",
    "cf-browser-verification",
    "checking your browser",
    "enable javascript and cookies",
    "verify you are human",
    "access denied",
    "akamai",
)


@dataclass(frozen=True)
class Candidate:
    url: str
    normalized_url: str
    title: str
    source_type: str
    publisher: str
    publish_date: str
    source_path: str
    target_raw_path: str
    reason: str
    official: bool
    needs_fetch: bool
    existing_raw_chars: int


@dataclass
class FetchResult:
    body: str
    status_code: int | None
    fetcher: str
    final_url: str
    content_type: str
    error: str = ""


@dataclass
class HarvestOutcome:
    url: str
    raw_path: str
    source_path: str
    status: str
    fetcher: str = ""
    http_status: int | None = None
    word_count: int = 0
    content_hash: str = ""
    error: str = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch and parse original text for URLs linked from wiki source pages.",
    )
    parser.add_argument("--limit", type=int, default=25, help="Maximum fetch attempts.")
    parser.add_argument("--workers", type=int, default=1, help="Parallel fetch workers.")
    parser.add_argument("--progress-every", type=int, default=1, help="Print every N completed items.")
    parser.add_argument("--dry-run", action="store_true", help="Build the queue without fetching or editing files.")
    parser.add_argument("--force", action="store_true", help="Refresh raw files even if extracted text already exists.")
    parser.add_argument("--sleep", type=float, default=0.0, help="Delay between fetches in seconds.")
    parser.add_argument("--timeout", type=int, default=30, help="Fetch timeout in seconds.")
    parser.add_argument("--report", default=str(REPORT_PATH), help="JSON report path.")
    parser.add_argument("--source-glob", default="*.md", help="Glob under wiki/sources to consider.")
    parser.add_argument("--include-inline-urls", action="store_true", help="Also queue external URLs from non-source wiki pages.")
    parser.add_argument("--include-nonofficial", action="store_true", help="Attempt nonofficial URLs too.")
    parser.add_argument(
        "--allow-nonofficial-fulltext",
        action="store_true",
        help="Write full extracted text for nonofficial URLs. Use only when rights permit.",
    )
    parser.add_argument(
        "--nonofficial-mode",
        choices=("skip", "summary", "full"),
        default="skip",
        help="How to handle nonofficial sources. summary stores metadata and a short extract only.",
    )
    parser.add_argument(
        "--min-existing-chars",
        type=int,
        default=1200,
        help="Existing raw files below this body length are treated as stubs.",
    )
    parser.add_argument(
        "--min-parse-words",
        type=int,
        default=120,
        help="Minimum extracted word count required before writing a parsed raw file.",
    )
    parser.add_argument(
        "--jina-fallback",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Use r.jina.ai reader fallback for blocked pages and PDFs.",
    )
    parser.add_argument(
        "--wayback-fallback",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Use Wayback availability API when live fetches fail.",
    )
    return parser.parse_args()


def normalize_url(url: str) -> str:
    parts = urlsplit(url.strip().rstrip(".,;:"))
    query_pairs = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        low = key.lower()
        if low in TRACKING_QUERY_KEYS or any(low.startswith(prefix) for prefix in TRACKING_QUERY_PREFIXES):
            continue
        query_pairs.append((key, value))
    path = re.sub(r"/+$", "", parts.path) or "/"
    netloc = parts.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    return urlunsplit((parts.scheme.lower(), netloc, path, urlencode(query_pairs), ""))


def host_for(url: str) -> str:
    host = urlsplit(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def is_official_url(url: str) -> bool:
    host = host_for(url)
    if host in OFFICIAL_EXACT_DOMAINS:
        return True
    if any(host == domain or host.endswith("." + domain) for domain in OFFICIAL_EXACT_DOMAINS):
        return True
    return any(host == suffix.lstrip(".") or host.endswith(suffix) for suffix in OFFICIAL_SUFFIXES)


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:100] or "source"


def raw_bucket(source_type: str, url: str) -> str:
    st = source_type.lower()
    if "court" in st or "case-document" in st:
        return "case-documents"
    if "academic" in st or "paper" in st:
        return "academic-papers"
    if "report" in st or "guidance" in st or "government" in st:
        return "government-reports"
    if "policy" in st:
        return "policy-documents"
    if "legislation" in st or "treaty" in st:
        return "legislation"
    if "news" in st:
        return "news"
    if url.lower().endswith(".pdf"):
        return "government-reports" if is_official_url(url) else "policy-documents"
    return "press-releases"


def first_url(meta: dict[str, Any]) -> str:
    for key in FRONTMATTER_URL_KEYS:
        value = str(meta.get(key) or "").strip()
        if value.startswith(("http://", "https://")):
            return value
    return ""


def load_raw_url_index() -> dict[str, Path]:
    out: dict[str, Path] = {}
    for path in RAW_DIR.rglob("*.md"):
        if path.name.startswith("_"):
            continue
        try:
            meta = frontmatter.load(path).metadata
        except Exception:
            continue
        url = first_url(meta)
        if url:
            out.setdefault(normalize_url(url), path)
    return out


def raw_body_chars(path: Path) -> int:
    if not path.exists():
        return 0
    try:
        return len(frontmatter.load(path).content.strip())
    except Exception:
        return 0


def has_extracted_text(path: Path, min_chars: int) -> bool:
    if not path.exists():
        return False
    try:
        post = frontmatter.load(path)
    except Exception:
        return False
    text_status = str(post.metadata.get("text_status") or "").lower()
    if text_status in {"parsed", "summarized"} and len(post.content.strip()) >= 200:
        return True
    return "## Extracted Text" in post.content and len(post.content.strip()) >= min_chars


def computed_raw_path(source_path: Path | None, title: str, source_type: str, url: str) -> Path:
    bucket = raw_bucket(source_type, url)
    if source_path is not None:
        filename = source_path.name
    else:
        date = TODAY
        match = re.search(r"(20\d{2})[-/](\d{2})[-/](\d{2})", url)
        if match:
            date = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
        domain = host_for(url).replace(".", "-")
        filename = f"{date}_{domain}_{slugify(title)}.md"
    return RAW_DIR / bucket / filename


def source_candidates(args: argparse.Namespace, raw_by_url: dict[str, Path]) -> list[Candidate]:
    candidates: list[Candidate] = []
    for source_path in sorted(SOURCES_DIR.glob(args.source_glob)):
        if source_path.name.startswith("_"):
            continue
        try:
            post = frontmatter.load(source_path)
        except Exception:
            continue
        meta = post.metadata
        url = first_url(meta)
        if not url:
            continue
        normalized = normalize_url(url)
        source_type = str(meta.get("source_type") or "web-reference")
        raw_rel = str(meta.get("raw_path") or "").strip()
        if raw_rel:
            raw_path = ROOT / raw_rel
            reason = "explicit_raw_path"
        elif normalized in raw_by_url:
            raw_path = raw_by_url[normalized]
            reason = "existing_raw_by_url"
        else:
            raw_path = computed_raw_path(source_path, str(meta.get("title") or source_path.stem), source_type, url)
            reason = "missing_raw_path"
        existing_chars = raw_body_chars(raw_path)
        needs_fetch = args.force or not has_extracted_text(raw_path, args.min_existing_chars)
        candidates.append(
            Candidate(
                url=url,
                normalized_url=normalized,
                title=str(meta.get("title") or source_path.stem),
                source_type=source_type,
                publisher=str(meta.get("publisher") or meta.get("collection_source") or ""),
                publish_date=str(meta.get("publish_date") or meta.get("date_filed") or ""),
                source_path=source_path.relative_to(ROOT).as_posix(),
                target_raw_path=raw_path.relative_to(ROOT).as_posix(),
                reason=reason,
                official=is_official_url(url),
                needs_fetch=needs_fetch,
                existing_raw_chars=existing_chars,
            )
        )
    return candidates


def inline_url_candidates(raw_by_url: dict[str, Path], known_urls: set[str], args: argparse.Namespace) -> list[Candidate]:
    if not args.include_inline_urls:
        return []
    candidates: list[Candidate] = []
    seen: set[str] = set()
    for md in sorted(WIKI_DIR.rglob("*.md")):
        if md.name.startswith("_") or ".obsidian" in md.parts or SOURCES_DIR in md.parents:
            continue
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for match in URL_RE.finditer(text):
            url = match.group(0).rstrip(".,;:")
            normalized = normalize_url(url)
            if normalized in known_urls or normalized in seen:
                continue
            seen.add(normalized)
            title = urlsplit(url).path.rstrip("/").split("/")[-1].replace("-", " ") or host_for(url)
            raw_path = raw_by_url.get(normalized) or computed_raw_path(None, title, "web-reference", url)
            candidates.append(
                Candidate(
                    url=url,
                    normalized_url=normalized,
                    title=title,
                    source_type="web-reference",
                    publisher=host_for(url),
                    publish_date="",
                    source_path=md.relative_to(ROOT).as_posix(),
                    target_raw_path=raw_path.relative_to(ROOT).as_posix(),
                    reason="inline_url_without_source_page",
                    official=is_official_url(url),
                    needs_fetch=args.force or not has_extracted_text(raw_path, args.min_existing_chars),
                    existing_raw_chars=raw_body_chars(raw_path),
                )
            )
    return candidates


def build_queue(args: argparse.Namespace) -> list[Candidate]:
    raw_by_url = load_raw_url_index()
    candidates = source_candidates(args, raw_by_url)
    known = {c.normalized_url for c in candidates} | set(raw_by_url)
    candidates.extend(inline_url_candidates(raw_by_url, known, args))

    deduped: dict[str, Candidate] = {}
    for candidate in candidates:
        current = deduped.get(candidate.normalized_url)
        if current is None:
            deduped[candidate.normalized_url] = candidate
            continue
        if current.reason == "inline_url_without_source_page" and candidate.reason != current.reason:
            deduped[candidate.normalized_url] = candidate

    def sort_key(item: Candidate) -> tuple[int, int, int, str]:
        return (
            0 if item.needs_fetch else 1,
            0 if item.official else 1,
            0 if item.reason in {"missing_raw_path", "existing_raw_by_url"} else 1,
            item.target_raw_path,
        )

    return sorted(deduped.values(), key=sort_key)


def urllib_fetch(url: str, timeout: int) -> FetchResult:
    req = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,text/plain;q=0.8,*/*;q=0.5",
        },
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            body = raw.decode("utf-8", errors="replace")
            return FetchResult(
                body=body,
                status_code=getattr(resp, "status", None),
                fetcher="urllib",
                final_url=resp.geturl(),
                content_type=resp.headers.get("content-type", ""),
            )
    except (HTTPError, URLError, OSError, TimeoutError) as exc:
        return FetchResult("", None, "urllib", url, "", error=str(exc))


def pdftotext_fetch(url: str, timeout: int) -> FetchResult:
    pdftotext = shutil.which("pdftotext")

    req = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/pdf,*/*;q=0.5",
        },
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            status = getattr(resp, "status", None)
            final_url = resp.geturl()
            content_type = resp.headers.get("content-type", "")
    except (HTTPError, URLError, OSError, TimeoutError) as exc:
        if "CERTIFICATE_VERIFY_FAILED" not in str(exc):
            return FetchResult("", None, "pdftotext", url, "", error=str(exc))
        try:
            with urlopen(req, timeout=timeout, context=ssl._create_unverified_context()) as resp:
                raw = resp.read()
                status = getattr(resp, "status", None)
                final_url = resp.geturl()
                content_type = resp.headers.get("content-type", "")
        except (HTTPError, URLError, OSError, TimeoutError) as retry_exc:
            return FetchResult("", None, "pdftotext", url, "", error=str(retry_exc))

    if not raw.startswith(b"%PDF") and "application/pdf" not in content_type.lower():
        return FetchResult("", status, "pdftotext", final_url, content_type, error="not_pdf")

    tmp_root = ROOT / "_workspace" / "tmp"
    tmp_root.mkdir(parents=True, exist_ok=True)
    tmp_path = tmp_root / f"ccic_pdf_{threading.get_ident()}_{time.time_ns()}"
    tmp_path.mkdir(parents=True, exist_ok=False)
    try:
        pdf_path = tmp_path / "source.pdf"
        txt_path = tmp_path / "source.txt"
        pdf_path.write_bytes(raw)
        parser = "pypdf"
        parser_error = ""
        text = ""
        try:
            from pypdf import PdfReader  # type: ignore

            reader = PdfReader(str(pdf_path))
            text = "\n\n".join((page.extract_text() or "").strip() for page in reader.pages).strip()
        except Exception as exc:
            parser_error = str(exc)

        if not text:
            parser = "pymupdf"
            try:
                import fitz  # type: ignore

                with fitz.open(str(pdf_path)) as doc:
                    text = "\n\n".join((page.get_text("text") or "").strip() for page in doc).strip()
            except Exception as exc:
                parser_error = str(exc)

        if not text and pdftotext and "miktex" not in pdftotext.lower():
            parser = "pdftotext"
            try:
                subprocess.run(
                    [pdftotext, "-layout", "-enc", "UTF-8", str(pdf_path), str(txt_path)],
                    check=True,
                    capture_output=True,
                    timeout=timeout,
                )
                text = txt_path.read_text(encoding="utf-8", errors="replace").strip() if txt_path.exists() else ""
            except (subprocess.SubprocessError, OSError) as exc:
                parser_error = str(exc)
    finally:
        shutil.rmtree(tmp_path, ignore_errors=True)

    if not text:
        return FetchResult("", status, parser, final_url, content_type, error=parser_error or "pdf_text_layer_empty_ocr_needed")
    return FetchResult(text, status, f"{parser}+urllib", final_url, "text/plain")


def curl_cffi_fetch(url: str, timeout: int) -> FetchResult:
    try:
        from curl_cffi import requests as curl_requests  # type: ignore
    except Exception as exc:
        return FetchResult("", None, "curl_cffi", url, "", error=str(exc))
    try:
        response = curl_requests.get(
            url,
            timeout=timeout,
            impersonate="chrome124",
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
            },
            allow_redirects=True,
        )
        return FetchResult(
            body=response.text or "",
            status_code=response.status_code,
            fetcher="curl_cffi",
            final_url=str(response.url),
            content_type=response.headers.get("content-type", ""),
            error="" if response.ok else f"HTTP {response.status_code}",
        )
    except Exception as exc:
        return FetchResult("", None, "curl_cffi", url, "", error=str(exc))


def jina_fetch(url: str, timeout: int) -> FetchResult:
    jina_url = f"https://r.jina.ai/{url}"
    req = Request(
        jina_url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/plain, text/markdown, */*",
            "X-With-Links": "true",
        },
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return FetchResult(
                body=body,
                status_code=getattr(resp, "status", None),
                fetcher="jina",
                final_url=url,
                content_type=resp.headers.get("content-type", "text/plain"),
            )
    except (HTTPError, URLError, OSError, TimeoutError) as exc:
        return FetchResult("", None, "jina", url, "", error=str(exc))


def wayback_available(url: str, timeout: int) -> str:
    api = f"https://archive.org/wayback/available?url={quote(url, safe='')}"
    req = Request(api, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception:
        return ""
    snapshot = data.get("archived_snapshots", {}).get("closest", {})
    if snapshot.get("available") and snapshot.get("url"):
        return str(snapshot["url"])
    return ""


def wayback_fetch(url: str, timeout: int) -> FetchResult:
    snapshot_url = wayback_available(url, timeout)
    if not snapshot_url:
        return FetchResult("", None, "wayback", url, "", error="no_snapshot")
    result = jina_fetch(snapshot_url, timeout)
    if result.body:
        result.fetcher = "wayback+jina"
        result.final_url = snapshot_url
        return result
    result = curl_cffi_fetch(snapshot_url, timeout)
    if result.body:
        result.fetcher = "wayback+curl_cffi"
        return result
    result = urllib_fetch(snapshot_url, timeout)
    if result.body:
        result.fetcher = "wayback+urllib"
        return result
    return FetchResult("", None, "wayback", snapshot_url, "", error=result.error or "snapshot_fetch_failed")


def url_variants(url: str) -> list[str]:
    variants = [url]
    parts = urlsplit(url)
    if parts.query:
        variants.append(urlunsplit((parts.scheme, parts.netloc, parts.path, "", "")))
    host = host_for(url)
    if host == "europol.europa.eu":
        variants.append(url.replace("/media-press/newsroom/news/", "/newsroom/news/"))
        variants.append(url.replace("/newsroom/news/", "/media-press/newsroom/news/"))
    if host == "admin.dea.gov":
        variants.append(url.replace("://admin.dea.gov/", "://www.dea.gov/"))
    if host == "secretservice.gov":
        variants.append(url.replace("/press/releases/", "/newsroom/releases/"))
        variants.append(url.replace("/newsroom/releases/", "/press/releases/"))
    out: list[str] = []
    seen: set[str] = set()
    for variant in variants:
        if variant not in seen:
            seen.add(variant)
            out.append(variant)
    return out


def acceptable_fetch_result(result: FetchResult, args: argparse.Namespace, url: str) -> FetchResult | None:
    if not result.body:
        return None
    if looks_like_challenge(result.body):
        return None
    if looks_like_pdf_body(result.body) or "application/pdf" in result.content_type.lower():
        if args.jina_fallback:
            fallback = jina_fetch(url, args.timeout)
            if fallback.body and not looks_like_pdf_body(fallback.body) and not looks_like_challenge(fallback.body):
                return fallback
        result.content_type = "application/pdf"
        result.error = result.error or "pdf_binary"
    return result


def fetch_single_url(url: str, args: argparse.Namespace, smart_fetcher: Any, doj_client: Any) -> FetchResult:
    last_error = ""

    if "coe.int" in host_for(url) and "module=signatures-by-treaty" in url and args.jina_fallback:
        result = acceptable_fetch_result(jina_fetch(url, args.timeout), args, url)
        if result:
            return result
        last_error = result.error if result else last_error

    if url.lower().endswith(".pdf"):
        result = acceptable_fetch_result(pdftotext_fetch(url, args.timeout), args, url)
        if result:
            return result
        last_error = result.error if result else last_error

    if url.lower().endswith(".pdf") and args.jina_fallback:
        result = acceptable_fetch_result(jina_fetch(url, args.timeout), args, url)
        if result:
            return result

    if "justice.gov" in host_for(url) and doj_client is not None:
        try:
            body = doj_client.fetch(url)
            result = acceptable_fetch_result(FetchResult(body, 200, "doj_fetch", url, "text/html"), args, url)
            if result:
                return result
            last_error = "challenge_or_pdf_or_empty"
        except Exception as exc:
            last_error = str(exc)

    result = acceptable_fetch_result(curl_cffi_fetch(url, args.timeout), args, url)
    if result and (result.status_code is None or result.status_code < 400):
        return result

    if smart_fetcher is not None:
        try:
            smart_result = smart_fetcher.fetch(url, timeout=args.timeout)
            if smart_result:
                result = acceptable_fetch_result(
                    FetchResult(
                        body=smart_result.body,
                        status_code=smart_result.status_code,
                        fetcher=smart_result.fetcher_used,
                        final_url=smart_result.url,
                        content_type="text/html",
                        error="challenge" if smart_result.is_challenge else "",
                    ),
                    args,
                    url,
                )
                if result:
                    return result
                last_error = "challenge_or_empty"
        except Exception as exc:
            last_error = str(exc)

    result = acceptable_fetch_result(urllib_fetch(url, args.timeout), args, url)
    if result:
        return result

    if args.jina_fallback:
        result = acceptable_fetch_result(jina_fetch(url, args.timeout), args, url)
        if result:
            return result

    if args.wayback_fallback:
        result = acceptable_fetch_result(wayback_fetch(url, args.timeout), args, url)
        if result:
            return result

    return FetchResult("", None, "fetch_chain", url, "", error=last_error or "all_fetch_methods_failed")


def fetch(candidate: Candidate, args: argparse.Namespace, smart_fetcher: Any, doj_client: Any) -> FetchResult:
    url = candidate.url
    last = FetchResult("", None, "fetch_chain", url, "", error="")
    for variant in url_variants(url):
        result = fetch_single_url(variant, args, smart_fetcher, doj_client)
        if result.body:
            return result
        last = result
    return last


def looks_like_pdf_body(body: str) -> bool:
    return body.lstrip().startswith("%PDF-")


def looks_like_challenge(body: str) -> bool:
    lower = body[:8000].lower()
    hits = sum(1 for signature in CHALLENGE_SIGNATURES if signature in lower)
    return hits >= 2 or ("access denied" in lower and len(body) < 5000)


def extract_title(body: str) -> str:
    patterns = [
        r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+name=["\']title["\'][^>]+content=["\']([^"\']+)["\']',
        r"<h1[^>]*>(.*?)</h1>",
        r"<title[^>]*>(.*?)</title>",
        r"^Title:\s*([^\n]+)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, body, flags=re.I | re.S | re.M)
        if match:
            return clean_text(match.group(1))[:300]
    return ""


def html_scope_candidates(body: str) -> list[tuple[str, str]]:
    cleaned = re.sub(r"<(script|style|noscript|svg)\b[^>]*>.*?</\1>", " ", body, flags=re.I | re.S)
    candidates: list[tuple[str, str]] = []
    for name, pattern in [
        ("doj_node_body", r'<div[^>]+class=["\'][^"\']*node-body[^"\']*["\'][^>]*>(.*?)</div>\s*<div[^>]+class=["\'][^"\']*node-bundle'),
        ("field_body", r'<div[^>]+class=["\'][^"\']*field--name-body[^"\']*["\'][^>]*>(.*?)</div>'),
        ("article", r"<article\b[^>]*>(.*?)</article>"),
        ("main", r"<main\b[^>]*>(.*?)</main>"),
    ]:
        for match in re.finditer(pattern, cleaned, flags=re.I | re.S):
            text = strip_html(match.group(1))
            if len(text) > 300:
                candidates.append((name, text))
    candidates.append(("document", strip_html(cleaned)))
    return candidates


def strip_html(fragment: str) -> str:
    fragment = re.sub(r"<\s*br\s*/?>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"</\s*(p|div|li|h[1-6]|tr|section|article|main)\s*>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return clean_text(fragment)


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    lines: list[str] = []
    for raw in text.splitlines():
        line = re.sub(r"\s+", " ", raw).strip()
        if not line:
            continue
        if any(pattern.search(line) for pattern in BOILERPLATE_PATTERNS):
            continue
        lines.append(line)
    return "\n\n".join(lines).strip()


def extract_readable_text(body: str, content_type: str, url: str, fallback_title: str) -> tuple[str, str, str]:
    if "application/pdf" in content_type.lower() or looks_like_pdf_body(body):
        return extract_title(body), "", "pdf_binary_unparsed"
    if content_type.startswith("text/plain") or body.startswith("Title: "):
        title = extract_title(body) or fallback_title
        return title, postprocess_text(clean_text(body), title, url), "plain"

    title = extract_title(body) or fallback_title
    candidates = html_scope_candidates(body)
    parser, text = max(candidates, key=lambda row: len(row[1]))
    return title, postprocess_text(text, title, url), parser


def postprocess_text(text: str, title: str, url: str) -> str:
    paragraphs = split_paragraphs(text)
    host = host_for(url)
    if host == "interpol.int":
        paragraphs = trim_interpol(paragraphs, title)
    paragraphs = trim_footer(paragraphs)
    paragraphs = dedupe_paragraphs(paragraphs)
    return "\n\n".join(paragraphs).strip()


def split_paragraphs(text: str) -> list[str]:
    paragraphs = [part.strip() for part in re.split(r"\n{2,}", text) if part.strip()]
    return [part for part in paragraphs if part not in {"/", '" />'}]


def trim_interpol(paragraphs: list[str], title: str) -> list[str]:
    if not paragraphs:
        return paragraphs
    title_norm = normalize_space(title).lower()
    title_indexes = [
        idx for idx, paragraph in enumerate(paragraphs)
        if normalize_space(paragraph).lower() == title_norm
    ]
    start = 0
    for idx in title_indexes:
        window = paragraphs[idx + 1: idx + 6]
        if any(is_dateline_or_article_lede(item) for item in window):
            start = idx
    end = len(paragraphs)
    for idx, paragraph in enumerate(paragraphs[start:], start):
        if normalize_space(paragraph).lower() in {"connect with us", "contact interpol"}:
            end = idx
            break
    return paragraphs[start:end]


def is_dateline_or_article_lede(text: str) -> bool:
    stripped = text.strip()
    if len(stripped) > 120:
        return True
    return bool(re.match(r"^[A-Z][A-Z .'-]{2,20}\s+[-\u2013]", stripped))


def trim_footer(paragraphs: list[str]) -> list[str]:
    footer_markers = {
        "connect with us",
        "contact interpol",
        "careers",
        "procurement",
        "cookie policy",
        "privacy policy",
        "terms of use",
        "site map",
        "cookie management",
    }
    out: list[str] = []
    for paragraph in paragraphs:
        norm = normalize_space(paragraph).lower()
        if norm in footer_markers:
            break
        out.append(paragraph)
    return out


def dedupe_paragraphs(paragraphs: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for paragraph in paragraphs:
        norm = normalize_space(paragraph).lower()
        if not norm or norm in seen:
            continue
        seen.add(norm)
        out.append(paragraph)
    return out


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def remove_generated_sections(content: str) -> str:
    for heading in ("Extracted Text", "Extraction Notes"):
        content = re.sub(
            rf"\n*##\s+{re.escape(heading)}\s*\n.*?(?=\n##\s+|\Z)",
            "\n",
            content,
            flags=re.S,
        )
    return content.strip()


def build_raw_post(candidate: Candidate, fetch_result: FetchResult, title: str, text: str, parser: str) -> frontmatter.Post:
    raw_path = ROOT / candidate.target_raw_path
    if raw_path.exists():
        post = frontmatter.load(raw_path)
    else:
        post = frontmatter.Post({}, "")

    meta = post.metadata
    meta.setdefault("title", title or candidate.title)
    if not meta.get("collection_source"):
        meta["collection_source"] = candidate.publisher or host_for(candidate.url)
    meta["collection_url"] = candidate.url
    meta["final_url"] = fetch_result.final_url or candidate.url
    meta["collection_domain"] = host_for(candidate.url)
    meta.setdefault("collection_date", TODAY)
    if not meta.get("publish_date") and candidate.publish_date:
        meta["publish_date"] = candidate.publish_date
    else:
        meta.setdefault("publish_date", "")
    meta.setdefault("language", "en")
    meta["status"] = "collected"
    meta["text_status"] = "parsed"
    meta["fetcher"] = fetch_result.fetcher
    meta["http_status"] = fetch_result.status_code
    meta["content_type"] = fetch_result.content_type
    meta["content_hash"] = sha256_text(text)
    meta["word_count"] = word_count(text)
    meta["extraction_date"] = TODAY
    meta["storage_mode"] = "fulltext"
    meta.pop("stored_word_count", None)
    meta.pop("copyright_policy", None)
    if candidate.source_path:
        meta["source_page"] = candidate.source_path

    content = remove_generated_sections(post.content)
    if not content:
        content = f"## Summary\n\nSource text harvested from {candidate.url}."
    notes = [
        f"- parser: {parser}",
        f"- fetcher: {fetch_result.fetcher}",
        f"- fetched_at: {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}",
        f"- final_url: {fetch_result.final_url or candidate.url}",
    ]
    content = (
        content.rstrip()
        + "\n\n## Extracted Text\n\n"
        + text.strip()
        + "\n\n## Extraction Notes\n\n"
        + "\n".join(notes)
        + "\n"
    )
    post.content = content
    return post


def short_extract(text: str, max_words: int = 80) -> str:
    words = re.findall(r"\S+", text.strip())
    if len(words) <= max_words:
        return " ".join(words)
    return " ".join(words[:max_words]).rstrip(".,;:") + "..."


def build_summary_raw_post(candidate: Candidate, fetch_result: FetchResult, title: str, text: str, parser: str) -> frontmatter.Post:
    raw_path = ROOT / candidate.target_raw_path
    if raw_path.exists():
        post = frontmatter.load(raw_path)
    else:
        post = frontmatter.Post({}, "")

    meta = post.metadata
    meta.setdefault("title", title or candidate.title)
    if not meta.get("collection_source"):
        meta["collection_source"] = candidate.publisher or host_for(candidate.url)
    meta["collection_url"] = candidate.url
    meta["final_url"] = fetch_result.final_url or candidate.url
    meta["collection_domain"] = host_for(candidate.url)
    meta.setdefault("collection_date", TODAY)
    if not meta.get("publish_date") and candidate.publish_date:
        meta["publish_date"] = candidate.publish_date
    else:
        meta.setdefault("publish_date", "")
    meta.setdefault("language", "en")
    meta["status"] = "collected"
    meta["text_status"] = "summarized"
    meta["fetcher"] = fetch_result.fetcher
    meta["http_status"] = fetch_result.status_code
    meta["content_type"] = fetch_result.content_type
    meta["content_hash"] = sha256_text(text)
    meta["word_count"] = word_count(text)
    meta["stored_word_count"] = min(word_count(text), 80)
    meta["extraction_date"] = TODAY
    meta["copyright_policy"] = "summary-only"
    if candidate.source_path:
        meta["source_page"] = candidate.source_path

    content = remove_generated_sections(post.content)
    if not content:
        content = f"## Summary\n\nSource metadata harvested from {candidate.url}."
    content = (
        content.rstrip()
        + "\n\n## Extracted Summary\n\n"
        + short_extract(text)
        + "\n\n## Extraction Notes\n\n"
        + "\n".join([
            f"- parser: {parser}",
            f"- fetcher: {fetch_result.fetcher}",
            f"- fetched_at: {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}",
            f"- final_url: {fetch_result.final_url or candidate.url}",
            "- storage_mode: summary-only",
        ])
        + "\n"
    )
    post.content = content
    return post


def update_source_metadata(candidate: Candidate, content_hash: str, words: int, fetcher: str) -> None:
    source_rel = candidate.source_path
    if not source_rel or not source_rel.startswith("wiki/sources/"):
        return
    source_path = ROOT / source_rel
    if not source_path.exists():
        return
    post = frontmatter.load(source_path)
    meta = post.metadata
    meta["raw_path"] = candidate.target_raw_path
    meta["text_status"] = "parsed"
    meta["content_hash"] = content_hash
    meta["word_count"] = words
    meta["extraction_date"] = TODAY
    meta["last_fetcher"] = fetcher
    meta["storage_mode"] = "fulltext"
    meta.pop("stored_word_count", None)
    meta.pop("copyright_policy", None)
    post.metadata = meta
    source_path.write_text(frontmatter.dumps(post), encoding="utf-8")


def update_source_summary_metadata(candidate: Candidate, content_hash: str, words: int, fetcher: str) -> None:
    source_rel = candidate.source_path
    if not source_rel or not source_rel.startswith("wiki/sources/"):
        return
    source_path = ROOT / source_rel
    if not source_path.exists():
        return
    post = frontmatter.load(source_path)
    meta = post.metadata
    meta["raw_path"] = candidate.target_raw_path
    meta["text_status"] = "summarized"
    meta["content_hash"] = content_hash
    meta["word_count"] = words
    meta["stored_word_count"] = min(words, 80)
    meta["extraction_date"] = TODAY
    meta["last_fetcher"] = fetcher
    meta["copyright_policy"] = "summary-only"
    post.metadata = meta
    source_path.write_text(frontmatter.dumps(post), encoding="utf-8")


def harvest_one(candidate: Candidate, args: argparse.Namespace, smart_fetcher: Any, doj_client: Any) -> HarvestOutcome:
    raw_path = ROOT / candidate.target_raw_path
    if not candidate.needs_fetch and not args.force:
        return HarvestOutcome(candidate.url, candidate.target_raw_path, candidate.source_path, "skipped_existing")

    if not candidate.official and not args.include_nonofficial and args.nonofficial_mode == "skip":
        return HarvestOutcome(candidate.url, candidate.target_raw_path, candidate.source_path, "skipped_nonofficial")

    if not candidate.official and args.nonofficial_mode == "skip":
        return HarvestOutcome(candidate.url, candidate.target_raw_path, candidate.source_path, "skipped_nonofficial_fulltext_policy")

    fulltext_allowed = candidate.official or args.allow_nonofficial_fulltext or args.nonofficial_mode == "full"

    fetch_result = fetch(candidate, args, smart_fetcher, doj_client)
    if not fetch_result.body:
        return HarvestOutcome(
            candidate.url,
            candidate.target_raw_path,
            candidate.source_path,
            "fetch_failed",
            fetcher=fetch_result.fetcher,
            http_status=fetch_result.status_code,
            error=fetch_result.error or "empty body",
        )
    if looks_like_challenge(fetch_result.body):
        return HarvestOutcome(
            candidate.url,
            candidate.target_raw_path,
            candidate.source_path,
            "fetch_failed",
            fetcher=fetch_result.fetcher,
            http_status=fetch_result.status_code,
            error="challenge_or_access_denied",
        )

    title, text, parser = extract_readable_text(
        fetch_result.body,
        fetch_result.content_type,
        candidate.url,
        candidate.title,
    )
    words = word_count(text)
    if words < args.min_parse_words:
        return HarvestOutcome(
            candidate.url,
            candidate.target_raw_path,
            candidate.source_path,
            "parse_failed",
            fetcher=fetch_result.fetcher,
            http_status=fetch_result.status_code,
            word_count=words,
            error=f"extracted text below {args.min_parse_words} words",
        )

    if fulltext_allowed:
        post = build_raw_post(candidate, fetch_result, title, text, parser)
    else:
        post = build_summary_raw_post(candidate, fetch_result, title, text, parser)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_text(frontmatter.dumps(post), encoding="utf-8")
    content_hash = str(post.metadata.get("content_hash") or "")
    if fulltext_allowed:
        update_source_metadata(candidate, content_hash, words, fetch_result.fetcher)
        status = "parsed"
    else:
        update_source_summary_metadata(candidate, content_hash, words, fetch_result.fetcher)
        status = "summarized"
    return HarvestOutcome(
        candidate.url,
        candidate.target_raw_path,
        candidate.source_path,
        status,
        fetcher=fetch_result.fetcher,
        http_status=fetch_result.status_code,
        word_count=words,
        content_hash=content_hash,
    )


def write_report(path: Path, queue: list[Candidate], outcomes: list[HarvestOutcome], args: argparse.Namespace) -> None:
    counters: dict[str, int] = {}
    for candidate in queue:
        key = "candidate_official" if candidate.official else "candidate_nonofficial"
        counters[key] = counters.get(key, 0) + 1
        if candidate.needs_fetch:
            counters["needs_fetch"] = counters.get("needs_fetch", 0) + 1
    for outcome in outcomes:
        counters[f"outcome_{outcome.status}"] = counters.get(f"outcome_{outcome.status}", 0) + 1

    payload = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "dry_run": args.dry_run,
        "limit": args.limit,
        "counters": counters,
        "queue_sample": [asdict(item) for item in queue[:100]],
        "outcomes": [asdict(item) for item in outcomes],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


_THREAD_STATE = threading.local()


def worker_harvest(item: Candidate, args: argparse.Namespace) -> HarvestOutcome:
    smart_fetcher = getattr(_THREAD_STATE, "smart_fetcher", None)
    if smart_fetcher is None and SmartFetcher is not None:
        smart_fetcher = SmartFetcher(enable_camoufox=False)
        _THREAD_STATE.smart_fetcher = smart_fetcher

    doj_client = getattr(_THREAD_STATE, "doj_client", None)
    if doj_client is None and DOJClient is not None:
        doj_client = DOJClient()
        _THREAD_STATE.doj_client = doj_client

    return harvest_one(item, args, smart_fetcher, doj_client)


def main() -> int:
    args = parse_args()
    queue = build_queue(args)
    actionable = [item for item in queue if item.needs_fetch]
    selected = actionable[: args.limit]

    outcomes: list[HarvestOutcome] = []
    if args.dry_run:
        for item in selected:
            status = "would_fetch" if item.official or args.include_nonofficial else "would_skip_nonofficial"
            outcomes.append(HarvestOutcome(item.url, item.target_raw_path, item.source_path, status))
    else:
        workers = max(1, args.workers)
        if workers == 1:
            smart_fetcher = SmartFetcher(enable_camoufox=False) if SmartFetcher is not None else None
            doj_client = DOJClient() if DOJClient is not None else None
            for idx, item in enumerate(selected, 1):
                print(f"[{idx}/{len(selected)}] {item.url}")
                outcome = harvest_one(item, args, smart_fetcher, doj_client)
                outcomes.append(outcome)
                if idx % max(1, args.progress_every) == 0 or idx == len(selected):
                    print(f"  -> {outcome.status} {outcome.word_count} words via {outcome.fetcher}")
                write_report(Path(args.report), queue, outcomes, args)
                if args.sleep and idx < len(selected):
                    time.sleep(args.sleep)
        else:
            print(f"Running with {workers} workers")
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
                future_map = {}
                for item in selected:
                    future = executor.submit(worker_harvest, item, args)
                    future_map[future] = item
                    if args.sleep:
                        time.sleep(args.sleep)

                for idx, future in enumerate(concurrent.futures.as_completed(future_map), 1):
                    item = future_map[future]
                    try:
                        outcome = future.result()
                    except Exception as exc:
                        outcome = HarvestOutcome(
                            item.url,
                            item.target_raw_path,
                            item.source_path,
                            "exception",
                            error=str(exc),
                        )
                    outcomes.append(outcome)
                    if idx % max(1, args.progress_every) == 0 or idx == len(selected):
                        print(
                            f"[{idx}/{len(selected)}] {outcome.status} "
                            f"{outcome.word_count} words via {outcome.fetcher} - {item.url}"
                        )
                    write_report(Path(args.report), queue, outcomes, args)

    report = Path(args.report)
    write_report(report, queue, outcomes, args)

    print("tools/harvest_linked_source_text.py")
    print(f"  candidates: {len(queue)}")
    print(f"  needs_fetch: {len(actionable)}")
    print(f"  selected: {len(selected)}")
    print(f"  dry_run: {args.dry_run}")
    print(f"  report: {report.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
