#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
import json
import math
import re
import statistics
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from zipfile import ZipFile

try:
    import frontmatter  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    import frontmatter  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
OPS_DIR = WIKI / "operations"
SOURCES_DIR = WIKI / "sources"
COUNTRIES_DIR = WIKI / "countries"
ORGS_DIR = WIKI / "organizations"
CRIME_DIR = WIKI / "crime-types"
IMPORT_DIR = ROOT / "_workspace" / "imports" / "data_sample"
SNA_CURRENT = ROOT / "_workspace" / "sna" / "current"
ANALYSIS_DIR = WIKI / "analysis"
SNA_HTML_DIR = ANALYSIS_DIR / "sna"

SNAPSHOT_DATE = "2026-05-04"
YEAR_MIN = 2014
YEAR_MAX = 2025

TARGET_CRIME_TYPES = {
    "ransomware-ic": "Ransomware",
    "dark-web-ic": "Dark Web",
    "csam-ic": "CSAM",
    "malware-ic": "Botnet/Malware",
    "illegal-iptv-ic": "Illegal IPTV",
}

REPORT_COLUMNS = [
    "excel_sheet",
    "excel_row",
    "year",
    "operation_name_raw",
    "operation_name_canonical_candidate",
    "source_url",
    "matched_source_slug",
    "matched_operation_slug",
    "excel_agencies",
    "wiki_agencies",
    "excel_countries",
    "wiki_countries",
    "excel_crime_types",
    "wiki_crime_types",
    "review_status",
    "review_note",
]

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
YEAR_RE = re.compile(r"(20[0-2][0-9]|201[0-9])")


def u(text: str) -> str:
    return text.encode("utf-8").decode("unicode_escape")


COUNTRY_ALIASES = {
    "united states": "united-states",
    "usa": "united-states",
    "u.s.": "united-states",
    "us": "united-states",
    u("\\ubbf8\\uad6d"): "united-states",
    "united kingdom": "united-kingdom",
    "uk": "united-kingdom",
    u("\\uc601\\uad6d"): "united-kingdom",
    "germany": "germany",
    u("\\ub3c5\\uc77c"): "germany",
    "netherlands": "netherlands",
    "holland": "netherlands",
    u("\\ub124\\ub35c\\ub780\\ub4dc"): "netherlands",
    u("\\uc624\\ub780\\ub2e4"): "netherlands",
    "italy": "italy",
    u("\\uc774\\ud0c8\\ub9ac\\uc544"): "italy",
    "spain": "spain",
    u("\\uc2a4\\ud398\\uc778"): "spain",
    "france": "france",
    u("\\ud504\\ub791\\uc2a4"): "france",
    "romania": "romania",
    u("\\ub8e8\\ub9c8\\ub2c8\\uc544"): "romania",
    "croatia": "croatia",
    u("\\ud06c\\ub85c\\uc544\\ud2f0\\uc544"): "croatia",
    "sweden": "sweden",
    u("\\uc2a4\\uc6e8\\ub374"): "sweden",
    "switzerland": "switzerland",
    u("\\uc2a4\\uc704\\uc2a4"): "switzerland",
    "china": "china",
    u("\\uc911\\uad6d"): "china",
    "canada": "canada",
    u("\\uce90\\ub098\\ub2e4"): "canada",
    "australia": "australia",
    u("\\ud638\\uc8fc"): "australia",
    u("\\uc624\\uc2a4\\ud2b8\\ub808\\uc77c\\ub9ac\\uc544"): "australia",
    "poland": "poland",
    u("\\ud3f4\\ub780\\ub4dc"): "poland",
    "belgium": "belgium",
    u("\\ubca8\\uae30\\uc5d0"): "belgium",
    "georgia": "georgia",
    u("\\uc870\\uc9c0\\uc544"): "georgia",
    "russia": "russia",
    u("\\ub7ec\\uc2dc\\uc544"): "russia",
    "ukraine": "ukraine",
    u("\\uc6b0\\ud06c\\ub77c\\uc774\\ub098"): "ukraine",
    "finland": "finland",
    u("\\ud540\\ub780\\ub4dc"): "finland",
    "norway": "norway",
    u("\\ub178\\ub974\\uc6e8\\uc774"): "norway",
    "israel": "israel",
    u("\\uc774\\uc2a4\\ub77c\\uc5d8"): "israel",
    "ireland": "ireland",
    u("\\uc544\\uc77c\\ub79c\\ub4dc"): "ireland",
    "serbia": "serbia",
    u("\\uc138\\ub974\\ube44\\uc544"): "serbia",
    "lithuania": "lithuania",
    u("\\ub9ac\\ud22c\\uc544\\ub2c8\\uc544"): "lithuania",
    "austria": "austria",
    u("\\uc624\\uc2a4\\ud2b8\\ub9ac\\uc544"): "austria",
    "south korea": "south-korea",
    "korea": "south-korea",
    u("\\ud55c\\uad6d"): "south-korea",
    u("\\ub300\\ud55c\\ubbfc\\uad6d"): "south-korea",
    "india": "india",
    u("\\uc778\\ub3c4"): "india",
    "kosovo": "kosovo",
    u("\\ucf54\\uc18c\\ubcf4"): "kosovo",
}

AGENCY_ALIASES = {
    "europol": "europol-ec3",
    "ec3": "europol-ec3",
    "europol ec3": "europol-ec3",
    u("\\uc720\\ub85c\\ud3f4"): "europol-ec3",
    "eurojust": "eurojust",
    u("\\uc720\\ub85c\\uc800\\uc2a4\\ud2b8"): "eurojust",
    "interpol": "interpol",
    u("\\uc778\\ud130\\ud3f4"): "interpol",
    "fbi": "fbi-cyber-division",
    u("\\ubbf8\\uad6d \\uc5f0\\ubc29\\uc218\\uc0ac\\uad6d"): "fbi-cyber-division",
    "doj": "us-doj",
    "us doj": "us-doj",
    u("\\ubbf8\\uad6d \\ubc95\\ubb34\\ubd80"): "us-doj",
    "bka": "germany-bka",
    u("\\ub3c5\\uc77c \\uc5f0\\ubc29\\ubc94\\uc8c4\\uc218\\uc0ac\\uccad"): "germany-bka",
    "nca": "uk-nca",
    "uk nca": "uk-nca",
    "city of london police": "uk-metropolitan-police",
    "polizia di stato": "polizia-di-stato",
    "polizia postale": "italy-polizia-postale",
    u("\\uc774\\ud0c8\\ub9ac\\uc544 \\uacbd\\ucc30"): "polizia-di-stato",
    u("\\uc774\\ud0c8\\ub9ac\\uc544 \\uacbd\\ucc30\\uccad"): "polizia-di-stato",
    "diicot": "romania-diicot",
    "romanian police": "romania-police",
    u("\\ub8e8\\ub9c8\\ub2c8\\uc544 \\uacbd\\ucc30"): "romania-police",
    "swedish police": "sweden-police",
    u("\\uc2a4\\uc6e8\\ub374 \\uacbd\\ucc30"): "sweden-police",
    "fedpol": "switzerland-fedpol",
    "switzerland fedpol": "switzerland-fedpol",
    "dutch police": "dutch-police",
    u("\\ub124\\ub35c\\ub780\\ub4dc\\uacbd\\ucc30"): "dutch-police",
    "fiod": "netherlands-fiod",
    "croatian police": "croatia-police",
}

CRIME_KEYWORDS = [
    ("ransomware-ic", ["ransomware", u("\\ub79c\\uc12c\\uc6e8\\uc5b4"), "digital extortion"]),
    ("dark-web-ic", ["dark web", "darknet", "dark web marketplace", u("\\ub2e4\\ud06c\\uc6f9"), u("\\ub2e4\\ud06c\\ub137"), "silk road", "alphabay"]),
    ("csam-ic", ["csam", "child sexual abuse", "child pornography", u("\\uc544\\ub3d9 \\uc131"), u("\\uc544\\ub3d9\\uc131"), u("\\uc131\\ucc29\\ucde8")]),
    ("malware-ic", ["malware", "botnet", "trojan", "infostealer", "loader", u("\\uc545\\uc131\\ucf54\\ub4dc"), u("\\ubd07\\ub137"), u("\\ud2b8\\ub85c\\uc774\\ubaa9\\ub9c8")]),
    ("illegal-iptv-ic", ["illegal iptv", "iptv", "illegal streaming", "pirate streaming", "piracy", u("\\ubd88\\ubc95 iptv"), u("\\ubd88\\ubc95 \\uc2a4\\ud2b8\\ub9ac\\ubc0d"), u("\\ud574\\uc801 \\uc2a4\\ud2b8\\ub9ac\\ubc0d"), u("\\ud53c\\ub77c\\uc2dc")]),
]

MULTINATIONAL_AGENCIES = {"europol-ec3", "eurojust", "interpol"}


@dataclass
class ExcelRecord:
    sheet: str
    row: int
    serial: str
    year: str
    operation_name: str
    crime_text: str
    agency_text: str
    country_text: str
    summary: str
    url: str


@dataclass
class SourceRecord:
    slug: str
    path: Path
    title: str
    url: str
    publisher: str
    publish_date: str


@dataclass
class OperationRecord:
    slug: str
    path: Path
    meta: dict
    title: str
    case_id: str
    year: int | None
    status: str
    role: str
    countries: list[str]
    agencies: list[str]
    crime_types: list[str]
    target_crime_types: list[str]
    sources: list[str]
    source_urls: list[str]


def normalize_url(value: str) -> str:
    value = str(value or "").strip()
    if not value:
        return ""
    parts = urlsplit(value)
    if not parts.scheme and parts.netloc == "":
        parts = urlsplit("https://" + value)
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parts.path.rstrip("/") or "/"
    query = []
    for key, val in parse_qsl(parts.query, keep_blank_values=True):
        low = key.lower()
        if low.startswith("utm_") or low in {"fbclid", "gclid", "ref", "source"}:
            continue
        query.append((key, val))
    return urlunsplit((parts.scheme.lower() or "https", host, path, urlencode(query), ""))


def slugify(value: str) -> str:
    value = str(value or "").lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def split_multi(text: str) -> list[str]:
    if not text:
        return []
    raw = re.split(r"[,;/\n]|(?:\s+-\s+)|(?:\s+and\s+)|(?:\s+및\s+)", str(text))
    return [part.strip(" .;:()[]") for part in raw if part.strip(" .;:()[]")]


def clean_op_name(value: str) -> str:
    text = str(value or "").strip()
    text = re.sub(r"\(\s*[\uac00-\ud7a3A-Za-z ]*칭\s*\)", "", text)
    text = re.sub(r"^\(?\s*tentative\s*\)?", "", text, flags=re.I)
    text = text.strip(" -")
    return text


def canonical_candidate(value: str) -> str:
    cleaned = clean_op_name(value)
    slug = slugify(cleaned)
    if slug.startswith("operation-"):
        return slug
    return f"operation-{slug}" if slug else ""


def wikilink_slugs(value: object) -> list[str]:
    items: list[object]
    if isinstance(value, list):
        items = value
    elif value in (None, ""):
        items = []
    else:
        items = [value]
    out: list[str] = []
    for item in items:
        if isinstance(item, dict):
            continue
        text = str(item or "").strip()
        if not text:
            continue
        matches = WIKILINK_RE.findall(text)
        if matches:
            out.extend(m.strip() for m in matches if m.strip())
        else:
            slug = slugify(text)
            if slug:
                out.append(slug)
    seen: set[str] = set()
    result: list[str] = []
    for slug in out:
        if slug not in seen:
            seen.add(slug)
            result.append(slug)
    return result


def listify(value: object) -> list[object]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def extract_year(meta: dict, slug: str) -> int | None:
    for key in ("case_id", "title", "title_ko"):
        match = YEAR_RE.search(str(meta.get(key) or ""))
        if match:
            return int(match.group(1))
    timeframe = meta.get("timeframe")
    if isinstance(timeframe, dict):
        for key in ("announced", "start", "end"):
            match = YEAR_RE.search(str(timeframe.get(key) or ""))
            if match:
                return int(match.group(1))
    for key in ("created", "updated"):
        match = YEAR_RE.search(str(meta.get(key) or ""))
        if match:
            return int(match.group(1))
    match = YEAR_RE.search(slug)
    return int(match.group(1)) if match else None


def read_post(path: Path):
    try:
        return frontmatter.load(path)
    except Exception:
        return frontmatter.Post({}, path.read_text(encoding="utf-8", errors="replace"))


def xlsx_sheets(path: Path) -> dict[str, list[tuple[int, list[str]]]]:
    ns = {
        "a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
        "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    }
    rel_ns = {"pr": "http://schemas.openxmlformats.org/package/2006/relationships"}

    def col_index(ref: str) -> int:
        letters = "".join(ch for ch in ref if ch.isalpha())
        num = 0
        for ch in letters:
            num = num * 26 + ord(ch.upper()) - 64
        return max(0, num - 1)

    with ZipFile(path) as zf:
        shared: list[str] = []
        if "xl/sharedStrings.xml" in zf.namelist():
            root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
            for si in root.findall("a:si", ns):
                shared.append("".join(t.text or "" for t in si.findall(".//a:t", ns)))

        def cell_value(cell: ET.Element) -> str:
            typ = cell.attrib.get("t")
            if typ == "inlineStr":
                return "".join(t.text or "" for t in cell.findall(".//a:t", ns))
            value = cell.find("a:v", ns)
            if value is None:
                return ""
            raw = value.text or ""
            if typ == "s":
                try:
                    return shared[int(raw)]
                except Exception:
                    return raw
            if typ == "b":
                return "TRUE" if raw == "1" else "FALSE"
            return raw

        workbook = ET.fromstring(zf.read("xl/workbook.xml"))
        rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        relmap = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in rels.findall("pr:Relationship", rel_ns)
        }
        sheets: dict[str, list[tuple[int, list[str]]]] = {}
        for sheet in workbook.findall("a:sheets/a:sheet", ns):
            name = sheet.attrib["name"]
            rid = sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
            target = relmap[rid].lstrip("/")
            if not target.startswith("xl/"):
                target = "xl/" + target
            root = ET.fromstring(zf.read(target))
            rows: list[tuple[int, list[str]]] = []
            for row in root.findall("a:sheetData/a:row", ns):
                row_index = int(row.attrib.get("r", len(rows) + 1))
                values: dict[int, str] = {}
                max_col = -1
                for cell in row.findall("a:c", ns):
                    idx = col_index(cell.attrib.get("r", "A"))
                    values[idx] = cell_value(cell)
                    max_col = max(max_col, idx)
                if max_col >= 0:
                    rows.append((row_index, [values.get(i, "") for i in range(max_col + 1)]))
            sheets[name] = rows
        return sheets


def safe_sheet_filename(index: int, name: str) -> str:
    safe = re.sub(r'[<>:"/\\|?*\s]+', "_", name.strip()).strip("_")
    safe = safe.replace("(", "_").replace(")", "_")
    safe = re.sub(r"_+", "_", safe).strip("_")
    return f"{index}_{safe or 'sheet'}.csv"


def write_csv(path: Path, rows: list[dict[str, object]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_plain_csv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def export_workbook(path: Path) -> tuple[dict[str, list[tuple[int, list[str]]]], dict[str, Path]]:
    sheets = xlsx_sheets(path)
    IMPORT_DIR.mkdir(parents=True, exist_ok=True)
    written: dict[str, Path] = {}
    for idx, (name, rows) in enumerate(sheets.items(), 1):
        out = IMPORT_DIR / safe_sheet_filename(idx, name)
        max_width = max((len(row) for _idx, row in rows), default=0)
        with out.open("w", newline="", encoding="utf-8-sig") as handle:
            writer = csv.writer(handle)
            for _row_idx, row in rows:
                writer.writerow(row + [""] * (max_width - len(row)))
        written[name] = out
    return sheets, written


def row_dict(header: list[str], row: list[str]) -> dict[str, str]:
    return {header[i].strip(): (row[i].strip() if i < len(row) else "") for i in range(len(header))}


def get_first(data: dict[str, str], *keys: str) -> str:
    for key in keys:
        if key in data and data[key].strip():
            return data[key].strip()
    return ""


def supplemental_values(sheets: dict[str, list[tuple[int, list[str]]]], marker: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for name, rows in sheets.items():
        if marker not in name or not rows:
            continue
        header = rows[0][1]
        for _row_idx, row in rows[1:]:
            data = row_dict(header, row)
            serial = get_first(data, u("\\uc5f0\\ubc88"))
            if not serial:
                continue
            vals = [v for k, v in data.items() if k not in {u("\\uc5f0\\ubc88"), u("\\uc791\\uc804\\uba852")} and v]
            out[serial] = ", ".join(vals)
    return out


def build_excel_records(sheets: dict[str, list[tuple[int, list[str]]]]) -> list[ExcelRecord]:
    agencies_by_serial = supplemental_values(sheets, u("\\uae30\\uad00_\\ucd94\\ucd9c"))
    countries_by_serial = supplemental_values(sheets, u("\\uad6d\\uac00_\\ucd94\\ucd9c"))
    crimes_by_serial = supplemental_values(sheets, u("\\ubc94\\uc8c4\\uc720\\ud615_\\ucd94\\ucd9c"))
    records: list[ExcelRecord] = []
    for sheet_name, rows in sheets.items():
        if not rows or not (sheet_name.startswith("1_") or sheet_name.startswith("2_")):
            continue
        header = rows[0][1]
        for row_idx, row in rows[1:]:
            data = row_dict(header, row)
            serial = get_first(data, u("\\uc5f0\\ubc88"))
            url = get_first(data, u("\\ucd9c\\ucc98"))
            if not any(row) or not url:
                continue
            year = get_first(data, u("\\uc5f0\\ub3c4"))
            operation = get_first(data, u("\\uc791\\uc804\\uba85"), u("\\uc791\\uc804\\uba852"))
            agency = get_first(data, u("\\ucc38\\uc5ec\\uae30\\uad00(\\uae30\\ubcf8 \\ud55c\\uae00, \\uc800\\uba85\\ud55c \\uae30\\uad00\\ub9cc \\uc601\\ubb38)"))
            country = get_first(data, u("\\ucc38\\uc5ec\\uad6d\\uac00(\\ud55c\\uae00)"))
            crime = get_first(data, u("\\uc8c4\\uba85(\\ud55c\\uae00)"))
            records.append(
                ExcelRecord(
                    sheet=sheet_name,
                    row=row_idx,
                    serial=serial,
                    year=year,
                    operation_name=operation,
                    crime_text=crimes_by_serial.get(serial) or crime,
                    agency_text=agencies_by_serial.get(serial) or agency,
                    country_text=countries_by_serial.get(serial) or country,
                    summary=get_first(data, u("\\ub0b4\\uc6a9")),
                    url=url,
                )
            )
    return records


def normalize_country_list(text: str) -> list[str]:
    values: list[str] = []
    for part in split_multi(text):
        low = re.sub(r"\s+", " ", part.lower().strip())
        low = re.sub(r"\([^)]*\)", "", low).strip()
        slug = COUNTRY_ALIASES.get(low)
        if not slug:
            slug = COUNTRY_ALIASES.get(part.strip())
        if slug:
            values.append(slug)
    return sorted(set(values))


def normalize_agency_list(text: str) -> list[str]:
    values: list[str] = []
    lower_full = text.lower()
    for key, slug in AGENCY_ALIASES.items():
        if key.lower() in lower_full:
            values.append(slug)
    for part in split_multi(text):
        low = re.sub(r"\s+", " ", part.lower().strip())
        low = re.sub(r"\([^)]*\)", "", low).strip()
        if low in AGENCY_ALIASES:
            values.append(AGENCY_ALIASES[low])
    return sorted(set(values))


def normalize_crime_types(text: str) -> list[str]:
    low = str(text or "").lower()
    values: list[str] = []
    for slug, keywords in CRIME_KEYWORDS:
        if any(keyword.lower() in low for keyword in keywords):
            values.append(slug)
    return sorted(set(values))


def load_sources() -> dict[str, SourceRecord]:
    sources: dict[str, SourceRecord] = {}
    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        post = read_post(path)
        meta = post.metadata
        url = str(meta.get("collection_url") or meta.get("url") or "").strip()
        sources[path.stem] = SourceRecord(
            slug=path.stem,
            path=path,
            title=str(meta.get("title") or path.stem),
            url=url,
            publisher=str(meta.get("publisher") or ""),
            publish_date=str(meta.get("publish_date") or ""),
        )
    return sources


def source_slug_from_item(item: object) -> str:
    if isinstance(item, dict):
        for key in ("source", "slug", "page", "target"):
            if key in item:
                return source_slug_from_item(item[key])
        return ""
    text = str(item or "").strip()
    match = WIKILINK_RE.search(text)
    if match:
        return match.group(1).split("/")[-1].strip()
    if re.fullmatch(r"[a-z0-9][a-z0-9._-]+", text):
        return text
    return ""


def load_operations(sources: dict[str, SourceRecord]) -> dict[str, OperationRecord]:
    ops: dict[str, OperationRecord] = {}
    for path in sorted(OPS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        post = read_post(path)
        meta = post.metadata
        if str(meta.get("type") or "").strip() != "operation":
            continue
        src_slugs = [source_slug_from_item(item) for item in listify(meta.get("sources"))]
        src_slugs = [slug for slug in src_slugs if slug]
        crime_types = wikilink_slugs(meta.get("crime_types")) or wikilink_slugs(meta.get("crime_type"))
        countries = wikilink_slugs(meta.get("participating_countries"))
        agencies = wikilink_slugs(meta.get("participating_agencies"))
        for extra in ("lead_agency", "coordinating_body"):
            for slug in wikilink_slugs(meta.get(extra)):
                if slug not in agencies:
                    agencies.append(slug)
        ops[path.stem] = OperationRecord(
            slug=path.stem,
            path=path,
            meta=meta,
            title=str(meta.get("title") or path.stem),
            case_id=str(meta.get("case_id") or ""),
            year=extract_year(meta, path.stem),
            status=str(meta.get("status") or "").lower().strip(),
            role=str(meta.get("operation_role") or "").lower().strip(),
            countries=sorted(set(countries)),
            agencies=sorted(set(agencies)),
            crime_types=sorted(set(crime_types)),
            target_crime_types=sorted(set(crime_types) & set(TARGET_CRIME_TYPES)),
            sources=src_slugs,
            source_urls=[sources[s].url for s in src_slugs if s in sources and sources[s].url],
        )
    return ops


def op_name_score(left: str, op: OperationRecord) -> float:
    left_clean = slugify(clean_op_name(left).replace("operation", ""))
    if not left_clean:
        return 0.0
    candidates = {
        slugify(op.slug.replace("operation", "")),
        slugify(op.title.replace("operation", "")),
        slugify(str(op.meta.get("title_ko") or "").replace("operation", "")),
    }
    best = 0.0
    left_tokens = set(left_clean.split("-"))
    for candidate in candidates:
        if not candidate:
            continue
        cand_tokens = set(candidate.split("-"))
        overlap = len(left_tokens & cand_tokens)
        if left_tokens and cand_tokens:
            best = max(best, overlap / max(1, min(len(left_tokens), len(cand_tokens))))
        if left_clean in candidate or candidate in left_clean:
            best = max(best, 0.9)
    return best


def report_row(
    rec: ExcelRecord,
    matched_source: str = "",
    matched_operation: str = "",
    wiki_agencies: list[str] | None = None,
    wiki_countries: list[str] | None = None,
    wiki_crimes: list[str] | None = None,
    status: str = "",
    note: str = "",
) -> dict[str, object]:
    return {
        "excel_sheet": rec.sheet,
        "excel_row": rec.row,
        "year": rec.year,
        "operation_name_raw": rec.operation_name,
        "operation_name_canonical_candidate": canonical_candidate(rec.operation_name),
        "source_url": rec.url,
        "matched_source_slug": matched_source,
        "matched_operation_slug": matched_operation,
        "excel_agencies": ";".join(normalize_agency_list(rec.agency_text)),
        "wiki_agencies": ";".join(wiki_agencies or []),
        "excel_countries": ";".join(normalize_country_list(rec.country_text)),
        "wiki_countries": ";".join(wiki_countries or []),
        "excel_crime_types": ";".join(normalize_crime_types(rec.crime_text)),
        "wiki_crime_types": ";".join(wiki_crimes or []),
        "review_status": status,
        "review_note": note,
    }


def build_reports(excel_records: list[ExcelRecord], sources: dict[str, SourceRecord], ops: dict[str, OperationRecord]) -> None:
    url_to_sources: dict[str, list[str]] = defaultdict(list)
    for source in sources.values():
        norm = normalize_url(source.url)
        if norm:
            url_to_sources[norm].append(source.slug)
    source_to_ops: dict[str, list[str]] = defaultdict(list)
    for op in ops.values():
        for source_slug in op.sources:
            source_to_ops[source_slug].append(op.slug)

    extracted: list[dict[str, object]] = []
    matched_sources: list[dict[str, object]] = []
    matched_operations: list[dict[str, object]] = []
    new_candidates: list[dict[str, object]] = []
    discrepancies: list[dict[str, object]] = []
    out_of_scope: list[dict[str, object]] = []
    manual_review: list[dict[str, object]] = []

    for rec in excel_records:
        year = int(float(rec.year)) if str(rec.year).replace(".", "", 1).isdigit() else None
        excel_countries = normalize_country_list(rec.country_text)
        excel_agencies = normalize_agency_list(rec.agency_text)
        excel_crimes = normalize_crime_types(rec.crime_text)
        source_matches = sorted(url_to_sources.get(normalize_url(rec.url), []))
        matched_source = source_matches[0] if source_matches else ""
        op_matches: list[str] = []
        for source_slug in source_matches:
            op_matches.extend(source_to_ops.get(source_slug, []))
        if not op_matches:
            scored = sorted(
                ((op_name_score(rec.operation_name, op), op.slug) for op in ops.values()),
                reverse=True,
            )
            if scored and scored[0][0] >= 0.86:
                op_matches.append(scored[0][1])
        matched_op_slug = sorted(set(op_matches))[0] if op_matches else ""
        matched_op = ops.get(matched_op_slug) if matched_op_slug else None

        scope_notes: list[str] = []
        if year is None or not (YEAR_MIN <= year <= YEAR_MAX):
            scope_notes.append("year_outside_2014_2025_or_missing")
        if not excel_crimes:
            scope_notes.append("no_target_five_crime_type_detected")
        if len(excel_countries) < 2 and not (set(excel_agencies) & MULTINATIONAL_AGENCIES):
            scope_notes.append("no_clear_international_cooperation_signal")

        base_status = "matched" if matched_op_slug else ("source_matched" if matched_source else "new_or_unmatched")
        base_note = ";".join(scope_notes) if scope_notes else ""
        extracted_row = report_row(
            rec,
            matched_source,
            matched_op_slug,
            matched_op.agencies if matched_op else [],
            matched_op.countries if matched_op else [],
            matched_op.target_crime_types if matched_op else [],
            base_status,
            base_note,
        )
        extracted.append(extracted_row)

        if matched_source:
            matched_sources.append(extracted_row)
        if matched_op:
            matched_operations.append(extracted_row)
            diff_notes: list[str] = []
            if excel_countries and set(excel_countries) != set(matched_op.countries):
                diff_notes.append("countries")
            if excel_agencies and not set(excel_agencies).issubset(set(matched_op.agencies)):
                diff_notes.append("agencies")
            if excel_crimes and set(excel_crimes) != set(matched_op.target_crime_types):
                diff_notes.append("crime_types")
            if diff_notes:
                row = dict(extracted_row)
                row["review_status"] = "field_discrepancy"
                row["review_note"] = "diff:" + ",".join(diff_notes)
                discrepancies.append(row)
                manual_review.append(row)
        else:
            if not scope_notes:
                row = dict(extracted_row)
                row["review_status"] = "new_candidate_operation"
                row["review_note"] = "No existing operation matched by source URL or operation-name similarity."
                new_candidates.append(row)
                manual_review.append(row)
            elif matched_source:
                row = dict(extracted_row)
                row["review_status"] = "source_without_operation_match"
                row["review_note"] = "Source URL exists, but no linked operation was found; " + ";".join(scope_notes)
                manual_review.append(row)

        if scope_notes:
            row = dict(extracted_row)
            row["review_status"] = "out_of_scope_or_non_ic"
            row["review_note"] = ";".join(scope_notes)
            out_of_scope.append(row)

    write_csv(IMPORT_DIR / "extracted_urls.csv", extracted, REPORT_COLUMNS)
    write_csv(IMPORT_DIR / "matched_existing_sources.csv", matched_sources, REPORT_COLUMNS)
    write_csv(IMPORT_DIR / "matched_existing_operations.csv", matched_operations, REPORT_COLUMNS)
    write_csv(IMPORT_DIR / "new_candidate_operations.csv", new_candidates, REPORT_COLUMNS)
    write_csv(IMPORT_DIR / "field_discrepancies.csv", discrepancies, REPORT_COLUMNS)
    write_csv(IMPORT_DIR / "out_of_scope_2014_2025_or_non_ic.csv", out_of_scope, REPORT_COLUMNS)
    write_csv(IMPORT_DIR / "needs_manual_review.csv", manual_review, REPORT_COLUMNS)

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "excel_records": len(excel_records),
        "matched_existing_sources": len(matched_sources),
        "matched_existing_operations": len(matched_operations),
        "new_candidate_operations": len(new_candidates),
        "field_discrepancies": len(discrepancies),
        "out_of_scope_2014_2025_or_non_ic": len(out_of_scope),
        "needs_manual_review": len(manual_review),
    }
    (IMPORT_DIR / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


def include_operation(op: OperationRecord) -> tuple[bool, str]:
    if op.status not in {"completed", "ongoing"}:
        return False, "status_not_completed_or_ongoing"
    if op.status == "absorbed" or op.role == "follow-on":
        return False, "absorbed_or_follow_on"
    if op.year is None or not (YEAR_MIN <= op.year <= YEAR_MAX):
        return False, "year_outside_2014_2025_or_missing"
    if not op.target_crime_types:
        return False, "no_target_crime_type"
    if not op.source_urls:
        return False, "no_source_url"
    if not op.agencies:
        return False, "no_participating_agencies"
    if not op.countries:
        return False, "no_participating_countries"
    if len(op.countries) < 2 and not (set(op.agencies) & MULTINATIONAL_AGENCIES):
        return False, "no_clear_international_cooperation"
    return True, "included"


def load_node_title(base: Path, slug: str) -> dict[str, str]:
    path = base / f"{slug}.md"
    if not path.exists():
        return {"title": slug}
    post = read_post(path)
    meta = post.metadata
    out = {"title": str(meta.get("title") or slug)}
    for key in ("region", "iso_code", "org_type", "country", "parent_org", "crime_category"):
        val = meta.get(key)
        if isinstance(val, list):
            out[key] = ";".join(str(x) for x in val)
        else:
            out[key] = str(val or "")
    return out


def graph_from_edges(edges: list[tuple[str, str]], prefix: str) -> dict[str, set[str]]:
    adj: dict[str, set[str]] = defaultdict(set)
    for op, node in edges:
        a = f"op::{op}"
        b = f"{prefix}::{node}"
        adj[a].add(b)
        adj[b].add(a)
    return adj


def bfs_dist(adj: dict[str, set[str]], start: str) -> dict[str, int]:
    dist = {start: 0}
    queue: deque[str] = deque([start])
    while queue:
        cur = queue.popleft()
        for nxt in adj.get(cur, set()):
            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
    return dist


def connected_components(adj: dict[str, set[str]]) -> list[set[str]]:
    remaining = set(adj)
    comps: list[set[str]] = []
    while remaining:
        start = next(iter(remaining))
        seen = set(bfs_dist(adj, start))
        comps.append(seen)
        remaining -= seen
    comps.sort(key=len, reverse=True)
    return comps


def betweenness(adj: dict[str, set[str]]) -> dict[str, float]:
    nodes = list(adj)
    cb = dict.fromkeys(nodes, 0.0)
    for s in nodes:
        stack: list[str] = []
        pred: dict[str, list[str]] = {w: [] for w in nodes}
        sigma = dict.fromkeys(nodes, 0.0)
        sigma[s] = 1.0
        dist = dict.fromkeys(nodes, -1)
        dist[s] = 0
        queue: deque[str] = deque([s])
        while queue:
            v = queue.popleft()
            stack.append(v)
            for w in adj[v]:
                if dist[w] < 0:
                    queue.append(w)
                    dist[w] = dist[v] + 1
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)
        delta = dict.fromkeys(nodes, 0.0)
        while stack:
            w = stack.pop()
            for v in pred[w]:
                if sigma[w]:
                    delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != s:
                cb[w] += delta[w]
    n = len(nodes)
    if n > 2:
        scale = 1.0 / ((n - 1) * (n - 2))
        for node in cb:
            cb[node] *= scale
    return cb


def eigenvector(adj: dict[str, set[str]], iterations: int = 100, tol: float = 1e-9) -> dict[str, float]:
    nodes = list(adj)
    if not nodes:
        return {}
    score = {node: 1.0 / math.sqrt(len(nodes)) for node in nodes}
    for _ in range(iterations):
        nxt = {node: sum(score[n] for n in adj[node]) for node in nodes}
        norm = math.sqrt(sum(v * v for v in nxt.values())) or 1.0
        nxt = {node: val / norm for node, val in nxt.items()}
        if max(abs(nxt[node] - score[node]) for node in nodes) < tol:
            return nxt
        score = nxt
    return score


def mode2_projection(adj: dict[str, set[str]], mode_nodes: list[str]) -> dict[str, set[str]]:
    projected: dict[str, set[str]] = {node: set() for node in mode_nodes}
    for node in mode_nodes:
        for op_node in adj.get(node, set()):
            for other in adj.get(op_node, set()):
                if other != node and other in projected:
                    projected[node].add(other)
    return projected


def transitivity(projected: dict[str, set[str]]) -> float:
    triples = 0
    triangles = 0
    for node, neigh in projected.items():
        d = len(neigh)
        triples += d * (d - 1) // 2
        ns = list(neigh)
        for i in range(len(ns)):
            for j in range(i + 1, len(ns)):
                if ns[j] in projected.get(ns[i], set()):
                    triangles += 1
    return (triangles / triples) if triples else 0.0


def graph_metrics(adj: dict[str, set[str]], op_nodes: list[str], mode_nodes: list[str], edge_count: int) -> tuple[dict, dict[str, dict[str, float]]]:
    comps = connected_components(adj) if adj else []
    sizes = [len(c) for c in comps]
    n = len(adj)
    if n > 1:
        fragmentation = 1.0 - sum(s * (s - 1) for s in sizes) / (n * (n - 1))
    else:
        fragmentation = 0.0
    largest = comps[0] if comps else set()
    distances = []
    eccentricities = []
    for node in largest:
        dist = bfs_dist(adj, node)
        vals = [d for target, d in dist.items() if target in largest and target != node]
        distances.extend(vals)
        eccentricities.append(max(vals) if vals else 0)
    avg_distance = statistics.mean(distances) if distances else 0.0
    diameter = max(eccentricities) if eccentricities else 0
    radius = min(eccentricities) if eccentricities else 0
    btw = betweenness(adj) if adj else {}
    eig = eigenvector(adj)
    centrality: dict[str, dict[str, float]] = {}
    for node in mode_nodes:
        dist = bfs_dist(adj, node)
        reachable = len(dist) - 1
        total_dist = sum(d for target, d in dist.items() if target != node)
        closeness = (reachable / total_dist) * (reachable / (n - 1)) if total_dist and n > 1 else 0.0
        centrality[node] = {
            "degree": len(adj.get(node, set())) / max(1, len(op_nodes)),
            "betweenness": btw.get(node, 0.0),
            "closeness": closeness,
            "eigenvector": eig.get(node, 0.0),
        }
    projected = mode2_projection(adj, mode_nodes)
    metrics = {
        "nodes": n,
        "edges": edge_count,
        "density": edge_count / max(1, len(op_nodes) * len(mode_nodes)),
        "components": len(comps),
        "component_sizes": sizes[:20],
        "largest_component_size": sizes[0] if sizes else 0,
        "fragmentation": fragmentation,
        "avg_distance_largest_cc": avg_distance,
        "diameter_largest_cc": diameter,
        "radius_largest_cc": radius,
        "transitivity_mode2_projection": transitivity(projected),
    }
    return metrics, centrality


def render_network_html(kind: str, edges: list[tuple[str, str]], op_titles: dict[str, str], node_titles: dict[str, str], out: Path) -> None:
    ops = sorted({op for op, _node in edges})
    nodes = sorted({node for _op, node in edges})
    width = 1400
    height = 900
    cx = width / 2
    cy = height / 2
    op_radius = 240
    node_radius = 390

    def pos(index: int, total: int, radius: float) -> tuple[float, float]:
        if total <= 1:
            return cx, cy
        angle = (2 * math.pi * index / total) - math.pi / 2
        return cx + radius * math.cos(angle), cy + radius * math.sin(angle)

    op_pos = {slug: pos(i, len(ops), op_radius) for i, slug in enumerate(ops)}
    node_pos = {slug: pos(i, len(nodes), node_radius) for i, slug in enumerate(nodes)}
    lines = []
    for op, node in edges:
        x1, y1 = op_pos[op]
        x2, y2 = node_pos[node]
        lines.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="edge" />')
    circles = []
    for slug, (x, y) in op_pos.items():
        title = html.escape(op_titles.get(slug, slug))
        circles.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" class="op"><title>{title}</title></circle>')
    for slug, (x, y) in node_pos.items():
        label = html.escape(node_titles.get(slug, slug))
        short = html.escape(slug[:28])
        circles.append(
            f'<g><circle cx="{x:.1f}" cy="{y:.1f}" r="10" class="mode"><title>{label}</title></circle>'
            f'<text x="{x:.1f}" y="{y + 24:.1f}" text-anchor="middle">{short}</text></g>'
        )
    doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{html.escape(kind.title())} SNA Network</title>
  <style>
    body {{ margin: 0; font-family: Arial, sans-serif; color: #1f2937; background: #f8fafc; }}
    header {{ padding: 16px 22px; background: #111827; color: white; }}
    header h1 {{ margin: 0; font-size: 20px; }}
    header p {{ margin: 6px 0 0; color: #d1d5db; }}
    svg {{ width: 100%; height: calc(100vh - 76px); background: white; }}
    .edge {{ stroke: #94a3b8; stroke-width: 0.8; opacity: 0.42; }}
    .op {{ fill: #334155; opacity: 0.85; }}
    .mode {{ fill: #0f766e; stroke: #042f2e; stroke-width: 1.2; }}
    text {{ font-size: 10px; fill: #334155; pointer-events: none; }}
  </style>
</head>
<body>
  <header>
    <h1>{html.escape(kind.title())} Network, 2014-2025 Five-Crime Subset</h1>
    <p>{len(ops)} operations, {len(nodes)} {html.escape(kind)} nodes, {len(edges)} edges. Hover nodes for labels.</p>
  </header>
  <svg viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(kind)} SNA network">
    {''.join(lines)}
    {''.join(circles)}
  </svg>
</body>
</html>
"""
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")


def build_sna(ops: dict[str, OperationRecord]) -> list[OperationRecord]:
    included: list[OperationRecord] = []
    excluded: list[list[object]] = []
    for op in ops.values():
        ok, reason = include_operation(op)
        if ok:
            included.append(op)
        else:
            excluded.append([op.slug, reason])
    included.sort(key=lambda op: (op.year or 0, op.slug))

    SNA_CURRENT.mkdir(parents=True, exist_ok=True)
    op_titles = {op.slug: op.title for op in included}
    country_edges = sorted((op.slug, c) for op in included for c in op.countries)
    agency_edges = sorted((op.slug, a) for op in included for a in op.agencies)
    crime_edges = sorted((op.slug, c) for op in included for c in op.target_crime_types)

    write_plain_csv(
        SNA_CURRENT / "nodes_operations.csv",
        ["slug", "title", "year", "case_id", "status", "source_count"],
        [[op.slug, op.title, op.year or "", op.case_id, op.status, len(op.source_urls)] for op in included],
    )
    countries = sorted({c for _op, c in country_edges})
    agencies = sorted({a for _op, a in agency_edges})
    crimes = sorted({c for _op, c in crime_edges})
    write_plain_csv(
        SNA_CURRENT / "nodes_countries.csv",
        ["slug", "title", "iso_code", "region"],
        [[slug, load_node_title(COUNTRIES_DIR, slug).get("title", slug), load_node_title(COUNTRIES_DIR, slug).get("iso_code", ""), load_node_title(COUNTRIES_DIR, slug).get("region", "")] for slug in countries],
    )
    write_plain_csv(
        SNA_CURRENT / "nodes_agencies.csv",
        ["slug", "title", "org_type", "country", "parent_org"],
        [[slug, load_node_title(ORGS_DIR, slug).get("title", slug), load_node_title(ORGS_DIR, slug).get("org_type", ""), load_node_title(ORGS_DIR, slug).get("country", ""), load_node_title(ORGS_DIR, slug).get("parent_org", "")] for slug in agencies],
    )
    write_plain_csv(
        SNA_CURRENT / "nodes_crimetypes.csv",
        ["slug", "title", "crime_category"],
        [[slug, load_node_title(CRIME_DIR, slug).get("title", slug), load_node_title(CRIME_DIR, slug).get("crime_category", "")] for slug in crimes],
    )
    write_plain_csv(SNA_CURRENT / "edges_op_country.csv", ["op_slug", "country_slug"], [list(row) for row in country_edges])
    write_plain_csv(SNA_CURRENT / "edges_op_agency.csv", ["op_slug", "agency_slug"], [list(row) for row in agency_edges])
    write_plain_csv(SNA_CURRENT / "edges_op_crimetype.csv", ["op_slug", "crime_type_slug"], [list(row) for row in crime_edges])
    write_plain_csv(SNA_CURRENT / "excluded_operations.csv", ["slug", "reason"], excluded)

    op_nodes = [f"op::{op.slug}" for op in included]
    graphs = {
        "country": (graph_from_edges(country_edges, "country"), [f"country::{c}" for c in countries], len(country_edges)),
        "agency": (graph_from_edges(agency_edges, "agency"), [f"agency::{a}" for a in agencies], len(agency_edges)),
        "crime_type": (graph_from_edges(crime_edges, "crime_type"), [f"crime_type::{c}" for c in crimes], len(crime_edges)),
    }
    cohesion: dict[str, dict] = {}
    components: dict[str, dict] = {}
    centralities: dict[str, dict[str, dict[str, float]]] = {}
    for kind, (adj, mode_nodes, edge_count) in graphs.items():
        metrics, centrality = graph_metrics(adj, op_nodes, mode_nodes, edge_count)
        cohesion[kind] = metrics
        components[kind] = {"count": metrics["components"], "sizes": metrics["component_sizes"]}
        centralities[kind] = centrality

    (SNA_CURRENT / "metrics_cohesion.json").write_text(json.dumps(cohesion, ensure_ascii=False, indent=2), encoding="utf-8")
    (SNA_CURRENT / "metrics_components.json").write_text(json.dumps(components, ensure_ascii=False, indent=2), encoding="utf-8")

    def centrality_rows(kind: str, prefix: str) -> list[list[object]]:
        rows = []
        for node, vals in centralities[kind].items():
            slug = node.split("::", 1)[1]
            rows.append([slug, vals["degree"], vals["betweenness"], vals["closeness"], vals["eigenvector"]])
        rows.sort(key=lambda row: row[1], reverse=True)
        return rows

    write_plain_csv(SNA_CURRENT / "metrics_centrality_country.csv", ["slug", "degree", "betweenness", "closeness", "eigenvector"], centrality_rows("country", "country"))
    write_plain_csv(SNA_CURRENT / "metrics_centrality_agency.csv", ["slug", "degree", "betweenness", "closeness", "eigenvector"], centrality_rows("agency", "agency"))
    write_plain_csv(SNA_CURRENT / "metrics_centrality_crimetype.csv", ["slug", "degree", "betweenness", "closeness", "eigenvector"], centrality_rows("crime_type", "crime_type"))

    country_titles = {slug: load_node_title(COUNTRIES_DIR, slug).get("title", slug) for slug in countries}
    agency_titles = {slug: load_node_title(ORGS_DIR, slug).get("title", slug) for slug in agencies}
    crime_titles = {slug: load_node_title(CRIME_DIR, slug).get("title", slug) for slug in crimes}
    render_network_html("country", country_edges, op_titles, country_titles, SNA_HTML_DIR / "country-network.html")
    render_network_html("agency", agency_edges, op_titles, agency_titles, SNA_HTML_DIR / "agency-network.html")
    render_network_html("crime type", crime_edges, op_titles, crime_titles, SNA_HTML_DIR / "crime-type-network.html")

    validation = {
        "out_of_range_included_operations": [op.slug for op in included if op.year is None or not (YEAR_MIN <= op.year <= YEAR_MAX)],
        "outside_target_crime_included_operations": [op.slug for op in included if not set(op.target_crime_types) <= set(TARGET_CRIME_TYPES)],
        "missing_source_url_included_operations": [op.slug for op in included if not op.source_urls],
        "missing_required_field_included_operations": [
            op.slug for op in included if not (op.agencies and op.countries and op.target_crime_types)
        ],
    }
    manifest = {
        "snapshot_date": SNAPSHOT_DATE,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "analysis_period": [YEAR_MIN, YEAR_MAX],
        "target_crime_types": TARGET_CRIME_TYPES,
        "included_operations_count": len(included),
        "excluded_operations_count": len(excluded),
        "exclusion_reason_counts": dict(Counter(reason for _slug, reason in excluded)),
        "nodes": {"operations": len(included), "countries": len(countries), "agencies": len(agencies), "crime_types": len(crimes)},
        "edges": {"op_country": len(country_edges), "op_agency": len(agency_edges), "op_crimetype": len(crime_edges)},
        "validation": validation,
        "required_outputs": [
            "manifest.json",
            "nodes_operations.csv",
            "nodes_countries.csv",
            "nodes_agencies.csv",
            "nodes_crimetypes.csv",
            "edges_op_country.csv",
            "edges_op_agency.csv",
            "edges_op_crimetype.csv",
            "metrics_centrality_country.csv",
            "metrics_centrality_agency.csv",
            "metrics_centrality_crimetype.csv",
            "metrics_cohesion.json",
            "metrics_components.json",
        ],
    }
    (SNA_CURRENT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    write_analysis_page(included, manifest, cohesion)
    return included


def top_centrality(path: Path, n: int = 8) -> list[tuple[str, float]]:
    if not path.exists():
        return []
    rows = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            try:
                rows.append((row["slug"], float(row["degree"])))
            except Exception:
                continue
    rows.sort(key=lambda item: item[1], reverse=True)
    return rows[:n]


def write_analysis_page(included: list[OperationRecord], manifest: dict, cohesion: dict) -> None:
    crime_counts = Counter(c for op in included for c in op.target_crime_types)
    country_top = top_centrality(SNA_CURRENT / "metrics_centrality_country.csv", 10)
    agency_top = top_centrality(SNA_CURRENT / "metrics_centrality_agency.csv", 10)
    crime_top = top_centrality(SNA_CURRENT / "metrics_centrality_crimetype.csv", 10)

    def table(rows: list[tuple[str, float]], label: str) -> str:
        out = [f"| {label} | Degree |", "|---|---:|"]
        for slug, degree in rows:
            out.append(f"| [[{slug}]] | {degree:.3f} |")
        return "\n".join(out)

    lines = [
        "---",
        'type: analysis',
        'title: "SNA Rebuild: 2014-2025 Five Cybercrime Categories"',
        "analysis_type: dataset-rebuild",
        'scope: "Operation-country, operation-agency, and operation-crime_type two-mode networks filtered to 2014-2025 and five target crime categories."',
        "confidence: medium",
        f"created: {SNAPSHOT_DATE}",
        f"updated: {SNAPSHOT_DATE}",
        "---",
        "",
        "## Summary",
        "",
        f"This rebuild uses `{SNA_CURRENT.relative_to(ROOT).as_posix()}/manifest.json` as the current SNA manifest. It includes **{manifest['included_operations_count']}** operations from **{YEAR_MIN}-{YEAR_MAX}** whose operation frontmatter has at least one source URL, participating agencies, participating countries, and at least one of the five target crime categories.",
        "",
        "The five-category crime filter is intentionally narrower than the older PoC SNA output. Crime-type edges are collapsed to `ransomware-ic`, `dark-web-ic`, `csam-ic`, `malware-ic`, and `illegal-iptv-ic`; other wiki crime categories are not exported into this subset.",
        "",
        "## Output Manifest",
        "",
        "| Artifact | Value |",
        "|---|---:|",
        f"| Operations | {manifest['nodes']['operations']} |",
        f"| Countries | {manifest['nodes']['countries']} |",
        f"| Agencies | {manifest['nodes']['agencies']} |",
        f"| Crime types | {manifest['nodes']['crime_types']} |",
        f"| Operation-country edges | {manifest['edges']['op_country']} |",
        f"| Operation-agency edges | {manifest['edges']['op_agency']} |",
        f"| Operation-crime_type edges | {manifest['edges']['op_crimetype']} |",
        "",
        "## Crime-Type Coverage",
        "",
        "| Crime type | Included operations |",
        "|---|---:|",
    ]
    for slug in TARGET_CRIME_TYPES:
        lines.append(f"| [[{slug}]] | {crime_counts.get(slug, 0)} |")
    lines.extend(
        [
            "",
            "## Centrality Snapshots",
            "",
            "### Countries",
            "",
            table(country_top, "Country"),
            "",
            "### Agencies",
            "",
            table(agency_top, "Agency"),
            "",
            "### Crime Types",
            "",
            table(crime_top, "Crime type"),
            "",
            "## Cohesion",
            "",
            "| Network | Nodes | Edges | Density | Components | Largest component |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for kind in ("country", "agency", "crime_type"):
        m = cohesion[kind]
        lines.append(
            f"| {kind} | {m['nodes']} | {m['edges']} | {m['density']:.4f} | {m['components']} | {m['largest_component_size']} |"
        )
    lines.extend(
        [
            "",
            "## Visualizations",
            "",
            "- [Country network](sna/country-network.html)",
            "- [Agency network](sna/agency-network.html)",
            "- [Crime-type network](sna/crime-type-network.html)",
            "",
            "## Validation Notes",
            "",
            f"- Out-of-range included operations: {len(manifest['validation']['out_of_range_included_operations'])}",
            f"- Included operations outside the target crime set: {len(manifest['validation']['outside_target_crime_included_operations'])}",
            f"- Included operations without source URLs: {len(manifest['validation']['missing_source_url_included_operations'])}",
            f"- Included operations missing required agency/country/crime fields: {len(manifest['validation']['missing_required_field_included_operations'])}",
            "",
            "The source workbook cross-check reports are under `_workspace/imports/data_sample/` and are treated as review evidence, not as an automatic overwrite of wiki operation frontmatter.",
            "",
        ]
    )
    (ANALYSIS_DIR / "sna-2014-2025-five-crime-types.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild data-sample imports and current five-crime SNA subset.")
    parser.add_argument("--workbook", default=str(ROOT / "데이터 샘플.xlsx"))
    args = parser.parse_args()

    workbook = Path(args.workbook)
    if not workbook.is_absolute():
        workbook = ROOT / workbook
    if not workbook.exists():
        print(f"Workbook not found: {workbook}", file=sys.stderr)
        return 2

    sheets, written = export_workbook(workbook)
    excel_records = build_excel_records(sheets)
    sources = load_sources()
    ops = load_operations(sources)
    build_reports(excel_records, sources, ops)
    included = build_sna(ops)

    print(f"Workbook sheets exported: {len(written)}")
    print(f"Excel URL records: {len(excel_records)}")
    print(f"Current SNA included operations: {len(included)}")
    print(f"Import reports: {IMPORT_DIR.relative_to(ROOT)}")
    print(f"SNA current: {SNA_CURRENT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
