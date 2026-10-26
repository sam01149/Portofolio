from html.parser import HTMLParser
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "index.html"


class PortfolioParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.hrefs = []
        self.translation_keys = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            self.ids.append(values["id"])
        if "href" in values:
            self.hrefs.append(values["href"])
        if "data-translate" in values:
            self.translation_keys.append(values["data-translate"])
        if "data-translate-title" in values:
            self.translation_keys.append(values["data-translate-title"])


def fail(messages):
    for message in messages:
        print(f"ERROR: {message}")
    raise SystemExit(1)


text = HTML_PATH.read_text(encoding="utf-8")
parser = PortfolioParser()
parser.feed(text)
errors = []

duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
if duplicates:
    errors.append(f"Duplicate HTML ids: {', '.join(duplicates)}")

known_ids = set(parser.ids)
for href in parser.hrefs:
    if href.startswith("#") and href != "#" and href[1:] not in known_ids:
        errors.append(f"Broken internal link: {href}")
    if href.startswith("./"):
        target = ROOT / href[2:]
        if not target.exists():
            errors.append(f"Missing local asset: {href}")

try:
    en_block, remainder = text.split("en: {", 1)[1].split("},\n        id: {", 1)
    id_block = remainder.split("\n        }\n      };", 1)[0]
except ValueError:
    fail(["Could not locate translation dictionaries."])

key_pattern = re.compile(r'^\s*"([^"]+)"\s*:', re.MULTILINE)
translation_sets = {
    "en": set(key_pattern.findall(en_block)),
    "id": set(key_pattern.findall(id_block)),
}
required = set(parser.translation_keys) | {"doc-title", "meta-desc"}
for language, available in translation_sets.items():
    missing = sorted(required - available)
    if missing:
        errors.append(f"Missing {language} translations: {', '.join(missing)}")

for pdf_name in ("CV_Samuel_Armando_Napitu_EN.pdf", "CV_Samuel_Armando_Napitu_ID.pdf"):
    pdf_path = ROOT / pdf_name
    if not pdf_path.exists() or pdf_path.stat().st_size < 5_000:
        errors.append(f"Invalid or missing PDF: {pdf_name}")

if errors:
    fail(errors)

print(
    f"PASS: {len(parser.ids)} ids, {len(required)} translated keys, "
    f"{len(parser.hrefs)} links, and both CV PDFs validated."
)
