#!/usr/bin/env python
from pathlib import Path
import re
import yaml


def _slugify(s: str):
    return re.sub(r"\W", "-", s.lower())

ROOT = Path(__file__).parent / ".."

TEMPLATE = """
# %CATEGORY%

{{ read_yaml("uktre-glossary.yaml", record_path="glossary", category="%CATEGORY%") }}
"""

with open(ROOT / "assets" / "uktre-glossary.yaml") as f:
    data = yaml.safe_load(f)
categories = set(t for term in data["glossary"] for t in term["tags"])

# Check categories don't have inconsistent names
slugs = {}
for category in categories:
    slug = _slugify(category)
    if slug in slugs:
        raise ValueError(f"Category has inconsistent naming: '{slugs[slug]}' '{category}'")
    slugs[slug] = category

for slug, category in sorted(slugs.items()):
    print(f"{category:<40} {slug}")
    with open(ROOT / "docs" / "categories" / f"{slug}.md", "w") as f:
      f.write(TEMPLATE.replace("%CATEGORY%", category))
