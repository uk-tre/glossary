import logging

from html import escape
from markdown import markdown
import pandas as pd
from textwrap import dedent
import re
import yaml

from mkdocs_table_reader_plugin.markdown import convert_to_md_table
from mkdocs_table_reader_plugin.readers import ParseArgs
from mkdocs_table_reader_plugin.utils import kwargs_in_func, kwargs_not_in_func

logger = logging.getLogger("mkdocs.plugins")



def _slugify(s: str):
    return re.sub(r"\W", "-", s.lower())

def link_urls(s: str):
    trailing_punctuation = re.escape(".,!?)]}>'\"")
    s = re.sub(rf"(https?://[\S]+[^{trailing_punctuation}])", r"[\1](\1)", s)
    return s

def _crossref_terms(text):
    # Find [...] but not [...](...)
    matches = re.findall(r"(\[[^]]+\])([^(]|$)", text)
    # Get the first capture group
    crossrefs = set(m[0] for m in matches)

    for crossref in crossrefs:
        target_term = crossref[1:-1]
        link_target = "#term-" + _slugify(target_term)
        link_md = f"[{target_term}]({link_target})"
        text = text.replace(crossref, link_md)
    return text


def to_glossary_html(df, **kwargs):
    """
    df.to_markdown() escapes some HTML, so create a HTML table ourselves
    """
    if kwargs:
        raise ValueError(f"Unsupported kwargs: {kwargs}")

    out = """
    <table>
        <tr>
            <th>Term</th>
            <th>Tags</th>
            <th>Definition</th>
        </tr>
    """
    for row in df.itertuples(index=False):
        anchor = "term-" + _slugify(row.term)
        crossreferenced = _crossref_terms(link_urls(row.definition))
        definition = markdown(escape(crossreferenced))

        row = f"""
        <tr>
            <td id="{anchor}"><a href="#{anchor}">{escape(row.term)}</a></td>
            <td>{escape(", ".join(row.tags))}</td>
            <td>{markdown(definition)}</td>
        </tr>
        """
        out += row

    out += """
    </table>
    """

    stripped = "\n".join(line.strip() for line in out.splitlines() if line.strip())
    return stripped


@ParseArgs
def read_csv(*args, **kwargs) -> str:
    read_kwargs = kwargs_in_func(kwargs, pd.read_csv)
    df = pd.read_csv(*args, **read_kwargs)

    markdown_kwargs = kwargs_not_in_func(kwargs, pd.read_csv)
    return to_glossary_html(df, **markdown_kwargs)


@ParseArgs
def read_json(*args, **kwargs) -> str:
    read_kwargs = kwargs_in_func(kwargs, pd.read_json)
    df = pd.read_json(*args, **read_kwargs)

    markdown_kwargs = kwargs_not_in_func(kwargs, pd.read_json)
    return to_glossary_html(df, **markdown_kwargs)


@ParseArgs
def read_excel(*args, **kwargs) -> str:
    read_kwargs = kwargs_in_func(kwargs, pd.read_excel)
    df = pd.read_excel(*args, **read_kwargs)

    markdown_kwargs = kwargs_not_in_func(kwargs, pd.read_excel)
    return to_glossary_html(df, **markdown_kwargs)


@ParseArgs
def read_yaml(*args, **kwargs) -> str:
    json_kwargs = kwargs_in_func(kwargs, pd.json_normalize)
    with open(args[0]) as f:
        df = pd.json_normalize(yaml.safe_load(f), **json_kwargs)

    markdown_kwargs = kwargs_not_in_func(kwargs, pd.json_normalize)
    return to_glossary_html(df, **markdown_kwargs)


READERS = {
    "read_csv": read_csv,
    "read_excel": read_excel,
    "read_yaml": read_yaml,
    "read_json": read_json,
}
