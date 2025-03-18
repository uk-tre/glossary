#!/usr/bin/env python
import numpy as np
import pandas as pd

# https://stackoverflow.com/questions/57382525/can-i-control-the-formatting-of-multiline-strings/57383273#57383273
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString

df = pd.read_excel("UK-TRE-glossary.xlsx", sheet_name="Merged")

glossary = df.replace(np.nan, None).apply(lambda r: {
        "term": r["Term"],
        "tags": [r["Context/Tag/Category"]] if r["Context/Tag/Category"] else [],
        "definition": LiteralScalarString(r["Definition"]),
    }, axis=1)
glossary = list(glossary)

categories = sorted(set(t for r in glossary for t in r["tags"]))
glossary_terms = {"categories": categories, "glossary": glossary}

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
with open("uktre-glossary.yaml", "w") as f:
    yaml.dump(glossary_terms, f)
