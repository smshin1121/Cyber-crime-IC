"""Print a paste-ready translation prompt for a wiki page.

Usage:
    python tools/translate_prompt.py <category> <slug>
    python tools/translate_prompt.py operations operation-cavern-nz-denmark-cyberhacking-2015

Output: a self-contained prompt that you paste into the Agent tool (or run
inline) to generate `wiki/<category>/<slug>.ko.md` — the Korean translation
sidecar required by L27.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"


GLOSSARY = """
- joint investigation → 합동수사
- joint investigation team (JIT) → 공동수사팀(JIT)
- Mutual Legal Assistance Treaty / MLAT → 형사사법공조조약(MLAT)
- mutual legal assistance / MLA → 형사사법공조
- extradition → 범죄인 인도
- European Arrest Warrant (EAW) → 유럽체포영장(EAW)
- dual criminality → 쌍방가벌성
- law enforcement → 법집행기관
- public prosecutor → 검사 / 검찰청
- search warrant → 압수수색영장
- press release → 보도자료
- official statement → 공식 성명
- victim profile → 피해자 프로파일
- modus operandi → 수법(모더스 오페란디)
- ransomware → 랜섬웨어
- phishing → 피싱
- voice phishing → 보이스피싱
- malware → 악성코드
- cyberstalking → 사이버스토킹
- swatting → 스와팅(허위신고)
- darknet / dark web → 다크넷 / 다크웹
- money laundering → 자금세탁
- cryptocurrency → 암호화폐
- seizure → 압수
- arrest → 체포
- indictment → 기소
- conviction → 유죄 판결
- sentencing → 양형
- asset forfeiture / asset recovery → 자산 몰수 / 자산 회수
- decryption key → 복호화 키
- jurisdiction → 관할권
- bilateral cooperation → 양자 협력
- multilateral cooperation → 다자 협력
- intergovernmental coordinating body → 정부간 조정 기관
- Five Eyes → Five Eyes (그대로)
- Europol / EC3 → Europol / EC3 (그대로 + 첫 언급 시 '유럽 사이버범죄센터')
- Eurojust → Eurojust (그대로 + '유럽사법협력기구')
- INTERPOL → INTERPOL (그대로 + '국제형사경찰기구')
- FBI → FBI (그대로 + 첫 언급 시 '미국 연방수사국')
- closed-doors hearing → 비공개 심리
- evidence transfer → 증거 이전
"""


def main() -> int:
    if len(sys.argv) < 3:
        sys.stderr.write(__doc__ + "\n")
        return 2
    category, slug = sys.argv[1], sys.argv[2]
    src = WIKI / category / f"{slug}.md"
    if not src.exists():
        sys.stderr.write(f"Source not found: {src}\n")
        return 1
    dst = WIKI / category / f"{slug}.ko.md"

    prompt = f"""You are translating an English wiki page into Korean for a cybercrime international cooperation wiki (사이버범죄 국제공조 위키). Read the English source at:

    {src.as_posix()}

The file has YAML frontmatter (between two `---` lines) followed by the body in English. Translate ONLY THE BODY (everything after the closing `---`) into Korean. Write the Korean translation to:

    {dst.as_posix()}

Rules — read carefully:

1. **No frontmatter** in the output. Start directly with the first `## ...` heading.

2. **Preserve every wikilink exactly.** Patterns: `[[slug]]`, `[[slug|display]]`, `[[slug\\|display]]`. The slug (before `|`) must NEVER be translated. For `[[slug|display]]` you may translate the display text. For bare `[[slug]]` either keep as-is or add a Korean display: `[[slug|한국어 표시]]`.

3. **Preserve markdown structure verbatim:**
   - `## H2` and `### H3` headings → translate the heading TEXT to Korean (e.g. `## Summary` → `## 개요`, `## Background` → `## 배경`)
   - Bullets `- item` stay as bullets
   - Numbered lists stay numbered
   - Tables stay as tables — translate cell contents, keep `|` pipes and column count
   - Blockquotes `> ...` stay as blockquotes
   - Bold `**...**` and italic `*...*` stay
   - Callouts `> [!warning]` / `> [!note]` / `> [!caution]` / `> [!info]` — keep the `[!tag]` in English, translate the content
   - Code blocks ``` ... ``` — keep contents unchanged
   - Inline code `` `code` `` — keep unchanged

4. **Canonical Korean IC/legal terminology — use these exact equivalents:**
{GLOSSARY}

5. **Tone:** factual, neutral, formal academic Korean (위키 톤). Use 평어체 (~다, ~이다, ~한다) — NEVER 존댓말.

6. **Country / city names:** translate to Hangeul on first occurrence, then use Hangeul throughout. Common: United States → 미국, United Kingdom → 영국, Germany → 독일, France → 프랑스, Netherlands → 네덜란드, China → 중국, Japan → 일본, Korea → 한국, Russia → 러시아, Ukraine → 우크라이나, Australia → 호주, New Zealand → 뉴질랜드, Denmark → 덴마크, Sweden → 스웨덴, Norway → 노르웨이, Finland → 핀란드, Spain → 스페인, Italy → 이탈리아, Romania → 루마니아, Poland → 폴란드, Czech Republic → 체코, Slovakia → 슬로바키아, Austria → 오스트리아, Switzerland → 스위스, Belgium → 벨기에, Hungary → 헝가리, Bulgaria → 불가리아, Greece → 그리스, Turkey → 튀르키예, Singapore → 싱가포르, Hong Kong → 홍콩, Thailand → 태국, Philippines → 필리핀, Indonesia → 인도네시아, Vietnam → 베트남, Malaysia → 말레이시아, Cambodia → 캄보디아, Israel → 이스라엘, Brazil → 브라질, Argentina → 아르헨티나, Mexico → 멕시코, Canada → 캐나다, India → 인도.

7. **Dates:** "16 September 2015" → "2015년 9월 16일", "Q3 2024" → "2024년 3분기", "May 2026" → "2026년 5월".

8. **Numbers and amounts:** translate currency to plain Korean. "USD 3.5 million" → "350만 미국 달러" or "USD 3.5백만". "EUR 21.2 million" → "EUR 2,120만" / "2,120만 유로". Keep the original-form number after a slash if disambiguation helps.

9. **Proper-noun organizations / units:** keep the English original at first mention with a Korean gloss in parentheses, then use the Korean gloss thereafter: "Federal Bureau of Investigation (FBI, 미국 연방수사국)" → subsequent mentions "FBI" alone. For obscure unit names ("Taskforce Pompilid"), keep English with a brief Korean descriptive gloss only once.

10. **Verbatim quotes:** if the English body uses a `> "..."` blockquote of a person's statement, keep the English original inside the blockquote and append a Korean translation as a follow-up line within the same blockquote:
    > "Original English statement..."
    >
    > (한국어 번역: ...)

11. **References table at the bottom:** keep the table structure. Translate the column header "Title" → "제목". Translate the article-title cell text. Keep Publisher, Date, and URL columns unchanged (those are not prose).

12. **Korean Involvement (한국의 참여) section:** if it already exists in the English source and is partially Korean, smooth it into fully Korean prose.

13. **Length:** the Korean translation should have approximately the same number of paragraphs and bullets as the English. Do not collapse or expand sections.

14. **Do NOT** add commentary, translator notes, or "TL;DR" sections. Do NOT skip sections.

After writing the file, report back briefly: the output file path, number of H2 sections translated, and any judgement calls you made (e.g. an ambiguous wikilink display text).
"""

    print(prompt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
