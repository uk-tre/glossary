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
    # Convert bare URLs to links
    trailing_punctuation = ".,!?)]}>'\""
    s = re.sub(
        r"""
            (?<!\]\()  # Negative lookbehind: Not preceded by ](
            (https?://[\S]+)
        """,
        r"[\1](\1)",
        s,
        flags=re.VERBOSE,
    )
    s.rstrip(trailing_punctuation)
    return s

def _external_url_icons(text):
    # Find [...](...)
    # If URL is absolute (http/https) add an external link icon
    matches = re.findall(
        r"""
            (
                \[
                    ([^]]+)  # Link text
                \]
                \(
                    (https?://[^]]+)  # Target
                \)
            )
        """,
        text,
        re.VERBOSE,
    )

    for match, link_text, link in matches:
        link_md = f"[{link_text} 🔗]({link})"
        text = text.replace(match, link_md)
    return text

def _crossref_terms(text, parent):
    # Find [...] but not [...](...)
    matches = re.findall(r"(\[[^]]+\])([^(]|$)", text)
    # Get the first capture group
    crossrefs = set(m[0] for m in matches)

    for crossref in crossrefs:
        target_term = crossref[1:-1]
        link_target = f"{parent}#term-{_slugify(target_term)}"
        link_md = f"[{target_term}]({link_target})"
        text = text.replace(crossref, link_md)
    return text


def to_glossary_html(df, category="", **kwargs):
    """
    df.to_markdown() escapes some HTML, so create a HTML table ourselves
    """
    if kwargs:
        raise ValueError(f"Unsupported kwargs: {kwargs}")

    # Don't show tags column if this is a single category
    th_tags = "" if category else "<th>Tags</th>"
    out = f"""
    <table>
        <tr>
            <th>Term</th>
            {th_tags}
            <th>Definition</th>
        </tr>
    """

    if category:
        # Duplicate rows with multiple tags, one per tag
        selected = df.explode("tags")
        selected = selected[selected["tags"] == category]
    else:
        selected = df

    for row in selected.itertuples(index=False):
        anchor = "term-" + _slugify(row.term)
        term = escape(row.term)

        if category:
            # Don't show tags column if this is a single category
            tags = ""
            # Need to link to top-level glossary since terms may not be in this category
            parent = "../../"
        else:
            tags = "".join(markdown(escape(f"[{c}](categories/{_slugify(c)})")) for c in row.tags)
            tags = f"<td>{tags}</td>"
            parent = ""

        external_urls_iconified = _external_url_icons(link_urls(row.definition))
        crossreferenced = _crossref_terms(external_urls_iconified, parent)
        # Convert markdown to HTML
        definition = markdown(
            # Escape HTML chars
            escape(
                # Treat single line break as paragraph break
                crossreferenced.replace("\n", "\n\n")
            )
        )

        row = f"""
        <tr>
            <td id="{anchor}"><a href="#{anchor}">{term}</a></td>
            {tags}
            <td>{definition}</td>
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
