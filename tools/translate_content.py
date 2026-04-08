"""
Wiki content translator — translates English markdown content to Korean
at build time and caches results. Only re-translates changed content.
"""
import hashlib
import json
import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"
CACHE_FILE = Path(__file__).resolve().parent.parent / "_workspace" / "translation_cache.json"

translator = GoogleTranslator(source="en", target="ko")


def _content_hash(text: str) -> str:
    """Generate hash of content for cache invalidation."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:12]


def _split_for_translation(text: str) -> list[str]:
    """Split text into chunks under 5000 chars (Google Translate limit)."""
    chunks = []
    current = []
    current_len = 0

    for line in text.split("\n"):
        line_len = len(line) + 1
        if current_len + line_len > 4500 and current:
            chunks.append("\n".join(current))
            current = [line]
            current_len = line_len
        else:
            current.append(line)
            current_len += line_len

    if current:
        chunks.append("\n".join(current))
    return chunks


def _preserve_and_translate(text: str) -> str:
    """Translate text while preserving markdown structure."""
    # Protect elements that shouldn't be translated
    protected = {}
    counter = [0]

    def protect(match):
        key = f"__PROT{counter[0]}__"
        counter[0] += 1
        protected[key] = match.group(0)
        return key

    # Protect wikilinks, URLs, code blocks, reference tables, frontmatter
    work = text
    work = re.sub(r'\[\[.*?\]\]', protect, work)
    work = re.sub(r'\[([^\]]*)\]\(https?://[^)]+\)', protect, work)
    work = re.sub(r'https?://\S+', protect, work)
    work = re.sub(r'```.*?```', protect, work, flags=re.DOTALL)
    work = re.sub(r'`[^`]+`', protect, work)
    work = re.sub(r'^\|.*\|$', protect, work, flags=re.MULTILINE)
    work = re.sub(r'> \[!.*?\].*$', protect, work, flags=re.MULTILINE)

    # Split and translate
    chunks = _split_for_translation(work)
    translated_chunks = []
    for chunk in chunks:
        if chunk.strip():
            try:
                result = translator.translate(chunk)
                translated_chunks.append(result if result else chunk)
                time.sleep(0.3)  # Rate limit
            except Exception:
                translated_chunks.append(chunk)
        else:
            translated_chunks.append(chunk)

    translated = "\n".join(translated_chunks)

    # Restore protected elements
    for key, val in protected.items():
        translated = translated.replace(key, val)

    return translated


def load_cache() -> dict:
    """Load translation cache."""
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: dict) -> None:
    """Save translation cache."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def translate_page(slug: str, content: str, cache: dict) -> str:
    """Translate a page's content, using cache if available."""
    h = _content_hash(content)
    cache_key = f"{slug}:{h}"

    if cache_key in cache:
        return cache[cache_key]

    translated = _preserve_and_translate(content)
    cache[cache_key] = translated
    return translated


def translate_all() -> dict[str, str]:
    """Translate all wiki pages and return slug->korean_content mapping."""
    cache = load_cache()
    translations = {}
    total = 0
    cached = 0
    translated = 0

    for md_file in WIKI_DIR.rglob("*.md"):
        if md_file.name.startswith("_"):
            continue

        slug = md_file.stem
        cat = md_file.parent.name
        if cat != "wiki":
            full_slug = f"{cat}/{slug}"
        else:
            full_slug = slug

        content = md_file.read_text(encoding="utf-8")
        # Extract body (after frontmatter)
        parts = content.split("---", 2)
        if len(parts) >= 3:
            body = parts[2].strip()
        else:
            body = content

        if not body:
            continue

        total += 1
        h = _content_hash(body)
        cache_key = f"{full_slug}:{h}"

        if cache_key in cache:
            translations[full_slug] = cache[cache_key]
            cached += 1
        else:
            try:
                ko = _preserve_and_translate(body)
                cache[cache_key] = ko
                translations[full_slug] = ko
                translated += 1
                if translated % 10 == 0:
                    print(f"  Translated {translated} pages...")
                    save_cache(cache)  # Periodic save
            except Exception as e:
                print(f"  Error translating {full_slug}: {e}")
                translations[full_slug] = body  # Fallback to English

    save_cache(cache)
    print(f"  Total: {total} | Cached: {cached} | New: {translated}")
    return translations


if __name__ == "__main__":
    print("=" * 60)
    print("  Wiki Content Translation")
    print("=" * 60)
    translate_all()
    print("Done.")
