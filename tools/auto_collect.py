"""
자동 RSS/뉴스 수집 스크립트
Windows Task Scheduler 또는 cron으로 주기 실행.
새 사이버범죄 국제공조 뉴스를 수집하여 raw/에 저장.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.request import urlopen, Request
from urllib.error import URLError

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "raw"
PENDING_DIR = PROJECT_ROOT / "_pending"
STATE_FILE = PROJECT_ROOT / "tools" / ".collect_state.json"

# RSS/Atom feeds to monitor
FEEDS: list[dict[str, str]] = [
    {
        "name": "Europol News",
        "url": "https://www.europol.europa.eu/rss.xml",
        "domain": "europol.europa.eu",
        "publisher": "Europol",
        "type": "press-releases",
        "reliability": "A",
    },
    {
        "name": "INTERPOL News",
        "url": "https://www.interpol.int/en/RSS/News",
        "domain": "interpol.int",
        "publisher": "INTERPOL",
        "type": "press-releases",
        "reliability": "A",
    },
    {
        "name": "DOJ Cybercrime",
        "url": "https://www.justice.gov/news/rss?topic=cybercrime",
        "domain": "justice.gov",
        "publisher": "US DOJ",
        "type": "press-releases",
        "reliability": "A",
    },
    {
        "name": "BleepingComputer",
        "url": "https://www.bleepingcomputer.com/feed/",
        "domain": "bleepingcomputer.com",
        "publisher": "BleepingComputer",
        "type": "news",
        "reliability": "C",
    },
]

# Keywords to filter for IC-relevant articles
IC_KEYWORDS = [
    "international operation", "joint operation", "coordinated operation",
    "law enforcement cooperation", "arrests", "takedown", "seized",
    "interpol", "europol", "indictment", "international cybercrime",
    "ransomware", "bec", "phishing", "operation",
]

IC_EXCLUDE = [
    "training", "workshop", "conference", "meeting", "webinar",
    "policy", "strategy", "announcement", "appointment",
]


def load_state() -> dict[str, Any]:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"seen_urls": [], "last_run": None}


def save_state(state: dict[str, Any]) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def fetch_feed(url: str) -> str | None:
    try:
        req = Request(url, headers={"User-Agent": "IC-Wiki-Bot/1.0"})
        with urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (URLError, TimeoutError) as e:
        print(f"  WARN: Failed to fetch {url}: {e}")
        return None


def parse_feed_items(xml_text: str) -> list[dict[str, str]]:
    items = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return items

    # RSS 2.0
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        desc = (item.findtext("description") or "").strip()
        pub_date = (item.findtext("pubDate") or "").strip()
        if title and link:
            items.append({
                "title": title,
                "link": link,
                "description": desc,
                "pub_date": pub_date,
            })

    # Atom
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.findall(".//atom:entry", ns):
        title = (entry.findtext("atom:title", namespaces=ns) or "").strip()
        link_el = entry.find("atom:link[@rel='alternate']", ns)
        if link_el is None:
            link_el = entry.find("atom:link", ns)
        link = link_el.get("href", "") if link_el is not None else ""
        desc = (entry.findtext("atom:summary", namespaces=ns) or "").strip()
        pub_date = (entry.findtext("atom:published", namespaces=ns) or "").strip()
        if title and link:
            items.append({
                "title": title,
                "link": link,
                "description": desc,
                "pub_date": pub_date,
            })

    return items


def is_ic_relevant(title: str, description: str) -> bool:
    text = f"{title} {description}".lower()
    if any(kw in text for kw in IC_EXCLUDE):
        if not any(kw in text for kw in ["arrest", "seize", "takedown", "indict"]):
            return False
    return any(kw in text for kw in IC_KEYWORDS)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text[:60].strip("-")


def save_pending(item: dict[str, str], feed: dict[str, str]) -> Path:
    today = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(item["title"])
    filename = f"{today}_{feed['publisher'].lower().replace(' ', '-')}_{slug}.md"

    content = f"""---
title: "{item['title']}"
collection_source: "{feed['name']}"
collection_url: "{item['link']}"
collection_domain: "{feed['domain']}"
collection_date: "{today}"
publish_date: "{item.get('pub_date', today)}"
publisher: "{feed['publisher']}"
reliability: "{feed['reliability']}"
language: "en"
status: "pending"
auto_collected: true
---

## {item['title']}

{item.get('description', '(본문을 가져오지 못했습니다. 파이프라인 실행 시 WebFetch로 보완 필요.)')}

---
*자동 수집됨. 파이프라인(`/ic-pipeline` 또는 `/ic-update`)을 실행하여 분류·평가·통합하세요.*
"""

    out_dir = PENDING_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename
    out_path.write_text(content, encoding="utf-8")

    # Also save to raw/
    raw_subdir = RAW_DIR / feed["type"]
    raw_subdir.mkdir(parents=True, exist_ok=True)
    (raw_subdir / filename).write_text(content, encoding="utf-8")

    return out_path


def main() -> None:
    print(f"=== IC Wiki Auto Collector === {datetime.now().isoformat()}")

    state = load_state()
    seen_urls = set(state.get("seen_urls", []))
    new_items: list[tuple[dict[str, str], dict[str, str]]] = []

    for feed in FEEDS:
        print(f"\nFetching: {feed['name']} ({feed['url']})")
        xml_text = fetch_feed(feed["url"])
        if not xml_text:
            continue

        items = parse_feed_items(xml_text)
        print(f"  Found {len(items)} items")

        for item in items:
            if item["link"] in seen_urls:
                continue
            if not is_ic_relevant(item["title"], item.get("description", "")):
                continue
            new_items.append((item, feed))
            seen_urls.add(item["link"])

    if not new_items:
        print("\nNo new IC-relevant items found.")
    else:
        print(f"\n{len(new_items)} new IC-relevant items found:")
        for item, feed in new_items:
            path = save_pending(item, feed)
            print(f"  + {path.name}")

    # Update state
    state["seen_urls"] = list(seen_urls)[-500:]  # Keep last 500
    state["last_run"] = datetime.now().isoformat()
    save_state(state)

    print(f"\nDone. {len(new_items)} items saved to _pending/")
    if new_items:
        print("Run '/ic-update' in Claude Code to process pending items.")


if __name__ == "__main__":
    main()
