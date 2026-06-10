#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "httpx>=0.28.0",
#   "pyyaml>=6.0.0",
# ]
# ///

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable
from urllib.parse import quote, unquote

import httpx
import yaml


# The CEF Implementation Standard ships as a static MadCap Flare build inside
# the SmartConnector documentation tree. The 25.1 directory is the newest
# static build; later SmartConnector releases moved to a JavaScript-only
# portal whose pages are not fetchable as plain HTML. The HTML topics in
# 25.1 are newer than the CEF v27 PDF in the same directory: they include the
# CEF 1.2 dictionary additions (zone keys, reportedResource*, threatActor,
# threatAttackID) that the PDF lacks.
CEF_BASE = (
    "https://www.microfocus.com/documentation/arcsight/"
    "arcsight-smartconnectors-25.1/cef-implementation-standard/Content/CEF"
)
CEF_PDF_URL = (
    "https://www.microfocus.com/documentation/arcsight/"
    "arcsight-smartconnectors-25.1/pdfdoc/cef-implementation-standard/"
    "cef-implementation-standard.pdf"
)
CEF_DOCUMENT_VERSION = "27"

# The full ArcSight ESM event schema lives in the Console User's Guide, also
# a static MadCap build. 7.9 is the newest release whose directory layout
# matches the fetchable pattern.
ESM_BASE = (
    "https://www.microfocus.com/documentation/arcsight/"
    "arcsight-esm-7.9/ESM_ArcSightConsole_UserGuide"
)
ESM_PDF_URL = (
    "https://www.microfocus.com/documentation/arcsight/"
    "arcsight-esm-7.9/pdfdoc/ESM_ArcSightConsole_UserGuide/"
    "ESM_ArcSightConsole_UserGuide.pdf"
)
ESM_VERSION = "7.9"
ESM_DATA_FIELDS_PAGE = "Data_Fields.htm"

HTTP_HEADERS = {
    "User-Agent": "tenzir-cef-generator",
    "Accept": "text/html",
}

EXTENSIONS_PAGE = "Chapter 2 ArcSight Extension.htm"

# CEF chapters rendered into Markdown docs, in reading order.
CEF_DOC_PAGES = (
    ("Chapter 1 What is CEF.htm", Path("docs/overview.md")),
    ("Chapter 3 Special Mappings.htm", Path("docs/special-mappings.md")),
    ("Chapter 4 User Defined Extensions.htm", Path("docs/user-defined-extensions.md")),
    ("Appendix A Date Formats.htm", Path("docs/date-formats.md")),
)

# Rewrites for cross-topic links inside generated docs (paths relative to the
# skill root; the renderer adjusts them per output file). ESM group pages are
# added at runtime once the TOC discovery resolves them.
PAGE_OUTPUTS = {
    "Chapter 1 What is CEF.htm": "docs/overview.md",
    "Chapter 2 ArcSight Extension.htm": "extensions.yaml",
    "Chapter 3 Special Mappings.htm": "docs/special-mappings.md",
    "Chapter 4 User Defined Extensions.htm": "docs/user-defined-extensions.md",
    "Appendix A Date Formats.htm": "docs/date-formats.md",
    "Data_Fields.htm": "docs/esm-data-fields.md",
}

CEF_TYPE_MAP = {
    "String": "string",
    "Integer": "integer",
    "Long": "long",
    "Double": "double",
    "Floating Point": "double",
    "IPv4 Address": "ipv4_address",
    "IPv6 address": "ipv6_address",
    "IP Address": "ip_address",
    "MAC Address": "mac_address",
    "MAC address": "mac_address",
    "Time Stamp": "timestamp",
    "TimeStamp": "timestamp",
}

# Keys that appear more than once in the upstream producer table. Anything
# else parsing as a duplicate is an error.
KNOWN_DUPLICATE_KEYS = {"dmac"}

# Quirks OpenText published in the dictionary itself, preserved as notes on
# the affected entries.
EXTENSION_NOTES = {
    "dmac": (
        "The upstream producer table lists dmac twice, in rows that differ "
        "only by a spelling fix in the description; the corrected row is kept."
    ),
}

# Quirks that apply to the generated data as a whole.
GENERAL_QUIRKS = (
    "Key names and camelCase full names in the upstream tables contain "
    "mid-word line-wrap spaces (for example `destination DnsDomain` and "
    "`deviceCustomIPv6 Address1Label`) and occasional capitalized first "
    "letters (`Device Outbound Interface`, `DeviceCustomNumber2`, `Reason`); "
    "the generator joins the fragments and lowercases the first letter to "
    "restore the documented camelCase identifiers.",
    "The CEF 1.2 additions (zone keys, reportedResource*, frameworkName, "
    "threatActor, threatAttackID) carry prose full names such as `Agent Zone "
    "Key` instead of camelCase identifiers and are listed in both the "
    "producer and the consumer table; they appear here once with audience: "
    "both, full names verbatim.",
    "Data type spellings vary upstream (`MAC Address` vs `MAC address`, "
    "`Time Stamp` vs `TimeStamp`, `Floating Point` vs `Double`); the "
    "generator normalizes them to one vocabulary in extensions.yaml. ESM "
    "data types in groups/*.yaml are copied verbatim.",
    "Several consumer-table rows have empty Meaning cells upstream; the "
    "affected entries omit the description key.",
)

EXPECTED_PRODUCER_KEYS = {
    "act", "app", "c6a1", "cat", "cn1", "cn1Label", "cfp1", "cs1", "cs1Label",
    "deviceCustomDate1", "dhost", "dpt", "dst", "dvc", "end", "flexString1",
    "in", "msg", "out", "proto", "request", "rt", "shost", "spt", "src",
    "start", "suser",
}
EXPECTED_CONSUMER_KEYS = {"agt", "ahost", "eventId", "rawEvent", "type"}
MINIMUM_PRODUCER_COUNT = 130
MINIMUM_CONSUMER_COUNT = 45

EXPECTED_ESM_GROUP_COUNT = 18
EXPECTED_SUFFIX_PAGE_COUNT = 2
MINIMUM_ESM_FIELD_COUNT = 450
EXPECTED_ESM_ALIASES = {
    "deviceAction", "sourceAddress", "destinationAddress", "attackerAddress",
    "targetAddress", "name", "connectorSeverity", "deviceVendor", "deviceProduct",
}


class NoAliasSafeDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:
        return True


def represent_multiline_str(dumper: yaml.Dumper, data: str) -> yaml.Node:
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


NoAliasSafeDumper.add_representer(str, represent_multiline_str)


def dump_yaml(data: Any) -> str:
    return yaml.dump(
        data,
        Dumper=NoAliasSafeDumper,
        allow_unicode=True,
        sort_keys=False,
        width=88,
    )


# --- Minimal HTML DOM -------------------------------------------------------


@dataclass(slots=True)
class Node:
    tag: str
    attrs: dict[str, str | None] = field(default_factory=dict)
    children: list[Node | str] = field(default_factory=list)

    def classes(self) -> set[str]:
        return set((self.attrs.get("class") or "").split())

    def elements(self) -> list[Node]:
        return [child for child in self.children if isinstance(child, Node)]

    def find_all(self, predicate: Callable[[Node], bool]) -> list[Node]:
        found: list[Node] = []
        for child in self.elements():
            if predicate(child):
                found.append(child)
            found.extend(child.find_all(predicate))
        return found

    def find(self, predicate: Callable[[Node], bool]) -> Node | None:
        found = self.find_all(predicate)
        return found[0] if found else None

    def text(self) -> str:
        parts: list[str] = []
        for child in self.children:
            parts.append(child if isinstance(child, str) else child.text())
        return collapse_whitespace("".join(parts))


class TreeBuilder(HTMLParser):
    VOID_TAGS = {"area", "base", "br", "col", "hr", "img", "input", "link", "meta", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("document")
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = Node(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in self.VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.stack[-1].children.append(Node(tag, dict(attrs)))

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data: str) -> None:
        if data:
            self.stack[-1].children.append(data)


def parse_html(text: str) -> Node:
    builder = TreeBuilder()
    builder.feed(text)
    return builder.root


def collapse_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def escape_angle_brackets(text: str) -> str:
    # Bare placeholders like <timestamp> parse as raw HTML open tags in GFM
    # and vanish from rendered output; code spans and fenced blocks bypass
    # this escaping.
    return text.replace("<", "\\<")


# --- HTML to Markdown -------------------------------------------------------


BLOCK_TAGS = {
    "article",
    "aside",
    "div",
    "h1",
    "h2",
    "h3",
    "h4",
    "main",
    "nav",
    "ol",
    "p",
    "pre",
    "section",
    "table",
    "ul",
}
SKIP_TAGS = {"aside", "nav", "script", "style", "head", "caption", "colgroup"}


def is_admonition(node: Node) -> bool:
    return node.tag == "div" and any(
        cls.startswith("Admonition") for cls in node.classes()
    )


@dataclass(frozen=True, slots=True)
class RenderContext:
    # Rewrites an internal topic href to a link target, or None to unlink.
    rewrite_link: Callable[[str], str | None]


def render_inline(node: Node | str, ctx: RenderContext) -> str:
    if isinstance(node, str):
        return escape_angle_brackets(node)
    if node.tag in SKIP_TAGS:
        return ""
    if node.tag in {"code", "samp", "kbd", "tt", "var"}:
        code = node.text()
        return f" `{code}` " if code else ""
    content = "".join(render_inline(child, ctx) for child in node.children)
    if node.tag in {"em", "i", "cite", "dfn"}:
        text = collapse_whitespace(content)
        return f" *{text}* " if text else ""
    if node.tag in {"strong", "b"}:
        text = collapse_whitespace(content)
        return f" **{text}** " if text else ""
    if node.tag == "a":
        label = collapse_whitespace(content)
        href = node.attrs.get("href") or ""
        if not label:
            return ""
        if not href or href.startswith("#"):
            return label
        target = ctx.rewrite_link(href)
        return f"[{label}]({target})" if target else label
    if node.tag == "br":
        return " "
    return content


def finish_paragraph(buffer: list[str]) -> str | None:
    text = collapse_whitespace("".join(buffer))
    buffer.clear()
    # Drop space padding around inline code/emphasis markers.
    text = re.sub(r"\s+([.,;:)])", r"\1", text)
    text = re.sub(r"\(\s+", "(", text)
    return text or None


def render_blocks(node: Node, ctx: RenderContext) -> list[str]:
    blocks: list[str] = []
    buffer: list[str] = []

    def flush() -> None:
        paragraph = finish_paragraph(buffer)
        if paragraph:
            blocks.append(paragraph)

    for child in node.children:
        if isinstance(child, str):
            buffer.append(escape_angle_brackets(child))
            continue
        if child.tag in SKIP_TAGS:
            continue
        if child.tag not in BLOCK_TAGS:
            buffer.append(render_inline(child, ctx))
            continue
        flush()
        blocks.extend(render_block(child, ctx))
    flush()
    return blocks


def render_block(node: Node, ctx: RenderContext) -> list[str]:
    if node.tag in SKIP_TAGS:
        return []
    if node.tag in {"h1", "h2", "h3", "h4"}:
        level = int(node.tag[1])
        return [f"{'#' * level} {node.text()}"]
    if node.tag == "p":
        paragraph = finish_paragraph([render_inline(child, ctx) for child in node.children])
        return [paragraph] if paragraph else []
    if node.tag in {"ul", "ol"}:
        return [render_list(node, ctx)]
    if node.tag == "table":
        return render_table(node, ctx)
    if node.tag == "pre":
        return [f"```\n{node.text()}\n```"]
    if is_admonition(node):
        return [render_admonition(node, ctx)]
    return render_blocks(node, ctx)


def render_list(node: Node, ctx: RenderContext, indent: int = 0) -> str:
    ordered = node.tag == "ol"
    lines: list[str] = []
    items = [child for child in node.elements() if child.tag == "li"]
    for index, item in enumerate(items, start=1):
        marker = f"{index}." if ordered else "-"
        prefix = " " * indent + f"{marker} "
        continuation = " " * len(prefix)
        item_blocks = render_blocks(item, ctx)
        if not item_blocks:
            continue
        first, *rest = item_blocks
        lines.append(prefix + first)
        for block in rest:
            for line in block.splitlines():
                lines.append(continuation + line)
    return "\n".join(lines)


def render_admonition(node: Node, ctx: RenderContext) -> str:
    # MadCap admonitions carry the label as a leading bold inline (for
    # example "<b>TIP</b>: ..."), so the rendered blocks already start with
    # the bolded title; wrapping them in a blockquote is enough.
    body = render_blocks(node, ctx)
    lines: list[str] = []
    for index, block in enumerate(body):
        if index:
            lines.append(">")
        lines.extend(f"> {line}" if line else ">" for line in block.splitlines())
    return "\n".join(lines)


def table_cell(node: Node, ctx: RenderContext) -> str:
    lines: list[str] = []
    for block in render_blocks(node, ctx):
        for line in block.splitlines():
            # Blockquote markers do not survive inside table cells.
            line = re.sub(r"^>\s?", "", line)
            if line:
                lines.append(line)
    return "<br>".join(lines).replace("|", "\\|")


def render_table(node: Node, ctx: RenderContext) -> list[str]:
    blocks: list[str] = []
    caption = node.find(lambda element: element.tag == "caption")
    if caption:
        blocks.append(f"*{caption.text()}*")
    rows = node.find_all(lambda element: element.tag == "tr")
    if not rows:
        return blocks
    table_lines: list[str] = []
    header_cells = [
        cell for cell in rows[0].elements() if cell.tag in {"th", "td"}
    ]
    header = [table_cell(cell, ctx) for cell in header_cells]
    table_lines.append("| " + " | ".join(header) + " |")
    table_lines.append("|" + "|".join(" --- " for _ in header) + "|")
    for row in rows[1:]:
        cells = [cell for cell in row.elements() if cell.tag in {"th", "td"}]
        table_lines.append(
            "| " + " | ".join(table_cell(cell, ctx) for cell in cells) + " |"
        )
    blocks.append("\n".join(table_lines))
    return blocks


def clean_markdown(text: str) -> str:
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


# --- Topic rendering --------------------------------------------------------


def main_content_of(document: Node) -> Node:
    content = document.find(
        lambda node: node.attrs.get("id") == "mc-main-content"
    )
    if content is None:
        raise RuntimeError("Page does not contain the mc-main-content container")
    return content


def link_rewriter(
    page_outputs: dict[str, str], output_path: Path
) -> Callable[[str], str | None]:
    def rewrite(href: str) -> str | None:
        base = unquote(href.split("#", 1)[0].split("?", 1)[0])
        name = base.rsplit("/", 1)[-1]
        if name in page_outputs:
            target = Path(page_outputs[name])
            prefix = "../" * (len(output_path.parts) - 1)
            return f"{prefix}{target.as_posix()}"
        if href.startswith(("http://", "https://", "mailto:")):
            return href
        # Unlinked internal topics fall back to plain text.
        return None

    return rewrite


def render_page(
    html: str, page_outputs: dict[str, str], output_path: Path
) -> str:
    content = main_content_of(parse_html(html))
    ctx = RenderContext(rewrite_link=link_rewriter(page_outputs, output_path))
    return clean_markdown("\n\n".join(render_blocks(content, ctx)))


# --- Fetching ---------------------------------------------------------------


def fetch_page(client: httpx.Client, url: str) -> str:
    # Missing pages on the documentation host redirect to a soft-404 page
    # that ends in HTTP 200, so redirects are disabled and treated as
    # failures.
    response = client.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Fetching {url} returned HTTP {response.status_code}")
    return response.text


def cef_page_url(page: str) -> str:
    return f"{CEF_BASE}/{quote(page)}"


def esm_page_url(path: str) -> str:
    return f"{ESM_BASE}/{path.lstrip('/')}"


# --- CEF extension dictionary parsing ---------------------------------------


def normalize_key(raw: str) -> str:
    joined = re.sub(r"\s+", "", raw)
    if not joined:
        raise RuntimeError("Encountered an empty CEF key name")
    return joined[0].lower() + joined[1:]


def normalize_full_name(raw: str) -> str:
    collapsed = collapse_whitespace(raw)
    if not collapsed:
        return collapsed
    if " " not in collapsed:
        # Single-token names occasionally start uppercase upstream
        # (DeviceCustomNumber2, Reason); all documented full names are
        # camelCase identifiers.
        return collapsed[0].lower() + collapsed[1:]
    if collapsed[0].islower():
        # A space inside a camelCase identifier is a line-wrap artifact.
        return collapsed.replace(" ", "")
    # Prose-style full names of the CEF 1.2 additions stay verbatim.
    return collapsed


def parse_length(raw: str) -> int | str | None:
    text = collapse_whitespace(raw)
    if not text:
        return None
    if text.isdigit():
        return int(text)
    return text


def parse_extension_tables(html: str, page_outputs: dict[str, str]) -> list[dict[str, Any]]:
    content = main_content_of(parse_html(html))
    ctx = RenderContext(rewrite_link=link_rewriter(page_outputs, Path("extensions.yaml")))
    tables = content.find_all(lambda node: node.tag == "table")
    if len(tables) != 2:
        raise RuntimeError(
            f"Extension dictionary page has {len(tables)} tables; expected the "
            "producer and consumer tables"
        )

    def parse_table(table: Node, audience: str) -> list[dict[str, Any]]:
        entries: list[dict[str, Any]] = []
        body = table.find(lambda node: node.tag == "tbody") or table
        for row in body.find_all(lambda node: node.tag == "tr"):
            cells = [cell for cell in row.elements() if cell.tag in {"td", "th"}]
            if len(cells) != 6:
                raise RuntimeError(
                    f"Expected 6 columns per extension row, got {len(cells)}"
                )
            version_cell, key_cell, name_cell, type_cell, length_cell, meaning_cell = cells
            value_type = collapse_whitespace(type_cell.text())
            if value_type not in CEF_TYPE_MAP:
                raise RuntimeError(f"Unknown CEF data type {value_type!r}")
            description = "\n\n".join(render_blocks(meaning_cell, ctx))
            entries.append(
                {
                    "key": normalize_key(key_cell.text()),
                    "full_name": normalize_full_name(name_cell.text()),
                    "type": CEF_TYPE_MAP[value_type],
                    "length": parse_length(length_cell.text()),
                    "audience": audience,
                    "since": collapse_whitespace(version_cell.text()),
                    "description": description,
                }
            )
        return entries

    producer_entries = parse_table(tables[0], "producer")
    consumer_entries = parse_table(tables[1], "consumer")

    extensions: dict[str, dict[str, Any]] = {}
    for entry in producer_entries:
        key = entry["key"]
        if key in extensions:
            if key not in KNOWN_DUPLICATE_KEYS:
                raise RuntimeError(f"Unexpected duplicate producer key {key!r}")
            # The duplicate rows differ only by a spelling fix; keep the row
            # without the misspelling.
            if "seperated" in extensions[key]["description"]:
                extensions[key] = entry
            continue
        extensions[key] = entry
    for entry in consumer_entries:
        key = entry["key"]
        if key in extensions:
            previous = extensions[key]
            if previous["type"] != entry["type"]:
                raise RuntimeError(
                    f"Key {key!r} has conflicting types across the producer "
                    f"and consumer tables"
                )
            previous["audience"] = "both"
            continue
        extensions[key] = entry

    result = list(extensions.values())
    for entry in result:
        if entry["length"] is None:
            del entry["length"]
        if not entry["description"]:
            del entry["description"]
        if entry["key"] in EXTENSION_NOTES:
            entry["notes"] = EXTENSION_NOTES[entry["key"]]
    return result


def validate_extensions(extensions: list[dict[str, Any]]) -> None:
    producer_count = sum(
        1 for entry in extensions if entry["audience"] in {"producer", "both"}
    )
    consumer_count = sum(
        1 for entry in extensions if entry["audience"] in {"consumer", "both"}
    )
    if producer_count < MINIMUM_PRODUCER_COUNT:
        raise RuntimeError(
            f"Parsed only {producer_count} producer keys; expected at least "
            f"{MINIMUM_PRODUCER_COUNT}. The page layout may have changed."
        )
    if consumer_count < MINIMUM_CONSUMER_COUNT:
        raise RuntimeError(
            f"Parsed only {consumer_count} consumer keys; expected at least "
            f"{MINIMUM_CONSUMER_COUNT}. The page layout may have changed."
        )
    keys = {entry["key"] for entry in extensions}
    missing = (EXPECTED_PRODUCER_KEYS | EXPECTED_CONSUMER_KEYS) - keys
    if missing:
        raise RuntimeError(f"Expected extension keys are missing: {sorted(missing)}")
    for entry in extensions:
        # Some consumer-table rows have empty Meaning cells upstream; every
        # producer key must carry a description.
        if entry["audience"] != "consumer" and not entry.get("description"):
            raise RuntimeError(f"Extension {entry['key']!r} has an empty description")
        if " " in entry["key"]:
            raise RuntimeError(f"Extension key {entry['key']!r} contains whitespace")


# --- ESM event schema parsing ------------------------------------------------


def discover_esm_group_pages(client: httpx.Client) -> list[tuple[str, str]]:
    """Returns (title, page path) pairs for the Data Fields group pages."""
    help_system = fetch_page(client, esm_page_url("Data/HelpSystem.xml"))
    toc_match = re.search(r'Toc="([^"]+)"', help_system)
    if toc_match is None:
        raise RuntimeError("HelpSystem.xml does not name a TOC file")
    toc = fetch_page(client, esm_page_url(toc_match.group(1)))

    chunk_count_match = re.search(r"numchunks:(\d+)", toc)
    prefix_match = re.search(r"prefix:'([^']+)'", toc)
    if chunk_count_match is None or prefix_match is None:
        raise RuntimeError("The ESM TOC file has an unexpected structure")
    toc_dir = toc_match.group(1).rsplit("/", 1)[0]

    index_to_url: dict[int, str] = {}
    index_to_title: dict[int, str] = {}
    for chunk in range(int(chunk_count_match.group(1))):
        chunk_js = fetch_page(
            client,
            esm_page_url(f"{toc_dir}/{prefix_match.group(1)}{chunk}.js"),
        )
        for match in re.finditer(
            r"'([^']+)':\{i:\[([\d,]+)\],t:\[((?:'[^']*',?)+)\]", chunk_js
        ):
            url = match.group(1)
            indices = [int(value) for value in match.group(2).split(",")]
            titles = re.findall(r"'([^']*)'", match.group(3))
            for index, title in zip(indices, titles):
                index_to_url[index] = url
                index_to_title[index] = title

    tree_start = toc.find("tree:")
    if tree_start < 0:
        raise RuntimeError("The ESM TOC file does not contain a tree")
    tree_text = toc[tree_start + len("tree:"):]
    depth = 0
    for position, character in enumerate(tree_text):
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                tree_text = tree_text[: position + 1]
                break
    tree = json.loads(re.sub(r"([{,])([a-z]+):", r'\1"\2":', tree_text))

    data_fields_indices = {
        index
        for index, url in index_to_url.items()
        if url.endswith(f"/{ESM_DATA_FIELDS_PAGE}")
    }

    def find_node(node: dict[str, Any]) -> dict[str, Any] | None:
        if node.get("i") in data_fields_indices:
            return node
        for child in node.get("n", []):
            found = find_node(child)
            if found is not None:
                return found
        return None

    data_fields_node = find_node(tree)
    if data_fields_node is None:
        raise RuntimeError("The ESM TOC does not contain the Data Fields topic")
    pages: list[tuple[str, str]] = []
    for child in data_fields_node.get("n", []):
        index = child["i"]
        pages.append((index_to_title[index], index_to_url[index]))
    if not pages:
        raise RuntimeError("The Data Fields topic has no group pages")
    return pages


def group_slug(title: str) -> str:
    slug = title.lower()
    slug = slug.removesuffix(" group")
    return re.sub(r"\s+", "_", slug.strip())


def split_group_content(content: Node) -> tuple[list[Node], Node]:
    """Splits a group page into leading narrative nodes and the data table."""
    narrative: list[Node] = []
    table: Node | None = None
    for child in content.elements():
        if child.tag == "table":
            table = child
            break
        if child.tag != "h1":
            narrative.append(child)
    if table is None:
        raise RuntimeError("Group page does not contain a data table")
    return narrative, table


def is_suffix_table(table: Node) -> bool:
    rows = table.find_all(lambda node: node.tag == "tr")
    header = [cell for cell in rows[0].elements() if cell.tag in {"th", "td"}]
    return len(header) == 2


def parse_group_page(
    title: str, page: str, html: str, page_outputs: dict[str, str]
) -> dict[str, Any]:
    slug = group_slug(title)
    output_path = Path(f"groups/{slug}.yaml")
    content = main_content_of(parse_html(html))
    ctx = RenderContext(rewrite_link=link_rewriter(page_outputs, output_path))
    narrative, table = split_group_content(content)
    description_blocks: list[str] = []
    for node in narrative:
        description_blocks.extend(render_block(node, ctx))

    fields: list[dict[str, Any]] = []
    notes: list[str] = []
    body = table.find(lambda node: node.tag == "tbody") or table
    rows = body.find_all(lambda node: node.tag == "tr")
    for row in rows:
        cells = [cell for cell in row.elements() if cell.tag in {"td", "th"}]
        if cells and cells[0].tag == "th":
            continue
        if len(cells) != 5:
            # Single-cell rows carry table-wide notes (for example the geo
            # field caveat repeated in the address groups).
            note = "\n\n".join(
                block for cell in cells for block in render_blocks(cell, ctx)
            )
            if note:
                notes.append(note)
            continue
        label_cell, alias_cell, type_cell, turbo_cell, description_cell = cells
        alias = re.sub(r"\s+", "", alias_cell.text())
        if not alias:
            raise RuntimeError(f"Group {title!r} has a field without a script alias")
        turbo_text = collapse_whitespace(turbo_cell.text())
        field_entry: dict[str, Any] = {
            "label": label_cell.text(),
            "alias": alias,
            "type": collapse_whitespace(type_cell.text()),
            "turbo_level": int(turbo_text) if turbo_text.isdigit() else turbo_text,
            "description": "\n\n".join(render_blocks(description_cell, ctx)),
        }
        fields.append(field_entry)

    group: dict[str, Any] = {
        "name": slug,
        "title": title,
        "source_url": esm_page_url(page),
        "description": "\n\n".join(description_blocks),
    }
    if notes:
        group["notes"] = notes
    group["fields"] = fields
    return group


def validate_esm_groups(groups: list[dict[str, Any]]) -> None:
    if len(groups) != EXPECTED_ESM_GROUP_COUNT:
        raise RuntimeError(
            f"Parsed {len(groups)} ESM field groups; expected "
            f"{EXPECTED_ESM_GROUP_COUNT}. The Data Fields TOC may have changed."
        )
    field_count = sum(len(group["fields"]) for group in groups)
    if field_count < MINIMUM_ESM_FIELD_COUNT:
        raise RuntimeError(
            f"Parsed only {field_count} ESM fields; expected at least "
            f"{MINIMUM_ESM_FIELD_COUNT}."
        )
    aliases = {
        field_entry["alias"] for group in groups for field_entry in group["fields"]
    }
    missing = EXPECTED_ESM_ALIASES - aliases
    if missing:
        raise RuntimeError(f"Expected ESM script aliases are missing: {sorted(missing)}")
    for group in groups:
        for field_entry in group["fields"]:
            if not field_entry["description"]:
                raise RuntimeError(
                    f"ESM field {field_entry['alias']!r} has an empty description"
                )


# --- Crosswalk ----------------------------------------------------------------


def crosswalk_extensions(
    extensions: list[dict[str, Any]], groups: list[dict[str, Any]]
) -> int:
    alias_to_groups: dict[str, list[str]] = {}
    for group in groups:
        for field_entry in group["fields"]:
            alias_to_groups.setdefault(field_entry["alias"], []).append(group["name"])
    matched = 0
    for entry in extensions:
        esm_groups = alias_to_groups.get(entry["full_name"])
        if esm_groups:
            entry["esm_groups"] = esm_groups
            matched += 1
    if matched < MINIMUM_PRODUCER_COUNT // 2:
        raise RuntimeError(
            f"Only {matched} extension full names resolve to ESM script "
            "aliases; the schema sources are likely out of sync"
        )
    return matched


# --- Output rendering ---------------------------------------------------------


def render_extensions_yaml(extensions: list[dict[str, Any]]) -> str:
    data: dict[str, Any] = {
        "cef_document_version": CEF_DOCUMENT_VERSION,
        "source": cef_page_url(EXTENSIONS_PAGE),
        "description": (
            "Predefined CEF extension keys from the ArcSight extension "
            "dictionary. Use these keys in the extension field whenever they "
            "match the data; add user-defined extensions only when no "
            "predefined key fits. audience: producer keys are set by devices "
            "and connectors that emit CEF; audience: consumer keys are set "
            "by ArcSight after ingestion and must not be set by event "
            "producers; audience: both marks the CEF 1.2 additions listed in "
            "both upstream tables. full_name is the expanded ArcSight field "
            "name; esm_groups names the ESM event schema groups (see "
            "catalog.yaml) that carry the field. since is the CEF "
            "specification version that introduced the key."
        ),
        "extensions": extensions,
    }
    return dump_yaml(data)


def render_catalog_yaml(groups: list[dict[str, Any]]) -> str:
    data: dict[str, Any] = {
        "esm_version": ESM_VERSION,
        "source": esm_page_url(f"Content/ESM_UserGuide/{ESM_DATA_FIELDS_PAGE}"),
        "description": (
            "ArcSight ESM event schema groups. Every processed event is a "
            "flat record of data fields; each group page documents the "
            "fields of one schema area. Use the script alias, not the label, "
            "in filters, rules, and CEF full names. Data types are copied "
            "verbatim from the OpenText pages. The geographical and resource "
            "attribute suffixes that expand fields like attackerGeo* are "
            "documented in docs/field-suffixes.md."
        ),
        "groups": [
            {
                "name": group["name"],
                "title": group["title"],
                "file": f"groups/{group['name']}.yaml",
                "fields": len(group["fields"]),
                "source_url": group["source_url"],
            }
            for group in groups
        ],
    }
    return dump_yaml(data)


def render_group_yaml(group: dict[str, Any]) -> str:
    data = dict(group)
    data["esm_version"] = ESM_VERSION
    ordered = {
        key: data[key]
        for key in ("name", "title", "esm_version", "source_url", "description", "notes", "fields")
        if key in data
    }
    return dump_yaml(ordered)


def render_skill_markdown() -> str:
    return clean_markdown(
        "\n".join(
            [
                "---",
                "name: tenzir-cef",
                "description: >-",
                "  Answer questions and produce mappings for ArcSight CEF (Common Event",
                "  Format), the OpenText/Micro Focus SIEM interchange format, and the",
                "  ArcSight ESM event schema behind it: CEF headers, severity, escaping",
                "  rules, the predefined extension dictionary, custom and flex fields",
                "  (cs1-cs6, cn1-cn3, cfp1-cfp4, flexString, flexDate), user-defined",
                "  extensions, date formats, and ESM data fields with script aliases.",
                "  Use when generating, parsing, validating, or mapping logs to or from",
                "  CEF, building ArcSight SmartConnector or FlexConnector integrations,",
                "  ingesting CEF into a SIEM such as Microsoft Sentinel",
                "  CommonSecurityLog, or when the user mentions CEF payloads,",
                "  pipe-delimited CEF:0 headers, or ArcSight event fields.",
                "---",
                "",
                "# Common Event Format",
                "",
                "CEF (Common Event Format) is ArcSight's text-based event interchange format, now maintained by OpenText. A CEF event is a single line consisting of an optional syslog prefix, a pipe-delimited header, and a flat list of space-separated `key=value` extensions:",
                "",
                "```",
                "CEF:Version|Device Vendor|Device Product|Device Version|Device Event Class ID|Name|Severity|[Extension]",
                "```",
                "",
                "Use [extensions.yaml](extensions.yaml) as the authoritative reference for the predefined extension keys: exact key spelling, expanded full name, data type, length, producer/consumer audience, and the CEF specification version that introduced the key. If a key is not present there, it is not a predefined CEF extension.",
                "",
                "Behind CEF sits the ArcSight ESM event schema: every CEF full name is an ESM script alias (for example `act` expands to `deviceAction` in the Device group). Use [catalog.yaml](catalog.yaml) to pick a schema group and `groups/<group>.yaml` for its fields.",
                "",
                "## Data files",
                "",
                "- Use [extensions.yaml](extensions.yaml) to look up predefined CEF extension keys.",
                "- Use [catalog.yaml](catalog.yaml) to choose an ESM event schema group, then `groups/<group>.yaml` for its data fields.",
                "- Use [docs/overview.md](docs/overview.md) for the CEF header fields, severity, and character encoding and escaping rules.",
                "- Use [docs/special-mappings.md](docs/special-mappings.md) for the documented firewall, anti-virus, email, wireless, and IPv6 mapping conventions.",
                "- Use [docs/user-defined-extensions.md](docs/user-defined-extensions.md) for naming and limitations of non-predefined keys.",
                "- Use [docs/date-formats.md](docs/date-formats.md) for the accepted timestamp formats.",
                "- Use [docs/esm-data-fields.md](docs/esm-data-fields.md) for how ESM labels, script aliases, and turbo levels relate.",
                "- Use [docs/field-suffixes.md](docs/field-suffixes.md) for the geographical and resource attribute suffixes.",
                "- Use [source.md](source.md) for upstream provenance and counts.",
                "",
                "## Format rules",
                "",
                "- Encode CEF events as UTF-8.",
                "- The header has seven pipe-delimited fields followed by the extension field; none of the seven may be omitted.",
                "- Escape `\\` as `\\\\` and `|` as `\\|` in header values; the pipe needs no escaping in extension values.",
                "- Escape `=` as `\\=` in extension values; newlines are allowed only in extension values, as `\\n` or `\\r`.",
                "- Severity is an integer 0-10 or one of Unknown, Low, Medium, High, Very-High; higher means more important.",
                "- The Device Event Class ID uniquely identifies the event type per product and is at most 1023 characters.",
                "- Extensions are `key=value` pairs separated by single spaces; each key may appear at most once.",
                "- Prefer predefined keys from [extensions.yaml](extensions.yaml); never set keys whose audience is consumer when producing events.",
                "- Pair every custom and flex field with its Label counterpart (for example `cs1` with `cs1Label`) and keep labels unique within an event.",
                "- Name user-defined extensions `VendornameProductnameExplanatoryKeyName`, alphanumeric and as short as possible; never reuse a predefined key name.",
                "- Express timestamps as milliseconds since epoch or one of the formats in [docs/date-formats.md](docs/date-formats.md).",
                "",
                "## Question routing",
                "",
                "- **What does key X mean, what type or length does it have, who may set it?** Use [extensions.yaml](extensions.yaml).",
                "- **How do I build or parse the CEF header, escape characters, or encode severity?** Read [docs/overview.md](docs/overview.md).",
                "- **Which ESM field backs a CEF key, or what fields does schema group X contain?** Follow `esm_groups` in [extensions.yaml](extensions.yaml) into [catalog.yaml](catalog.yaml) and `groups/<group>.yaml`.",
                "- **How do I map firewall, anti-virus, email, wireless, or IPv6 events?** Read [docs/special-mappings.md](docs/special-mappings.md).",
                "- **There is no predefined key for my data.** Read [docs/user-defined-extensions.md](docs/user-defined-extensions.md).",
                "- **How do I encode timestamps?** Read [docs/date-formats.md](docs/date-formats.md).",
                "- **What do labels, script aliases, and turbo levels mean in ESM?** Read [docs/esm-data-fields.md](docs/esm-data-fields.md).",
                "- **What do the Geo or resource attribute suffixes mean?** Read [docs/field-suffixes.md](docs/field-suffixes.md).",
                "- **What upstream source backs this skill?** Use [source.md](source.md).",
                "",
            ]
        )
    )


def render_source_page(
    extensions: list[dict[str, Any]],
    groups: list[dict[str, Any]],
    suffix_pages: list[tuple[str, str]],
    crosswalk_matches: int,
) -> str:
    producer_count = sum(
        1 for entry in extensions if entry["audience"] in {"producer", "both"}
    )
    consumer_count = sum(
        1 for entry in extensions if entry["audience"] in {"consumer", "both"}
    )
    both_count = sum(1 for entry in extensions if entry["audience"] == "both")
    field_count = sum(len(group["fields"]) for group in groups)
    lines = [
        "# Source",
        "",
        "This skill is generated from two OpenText (Micro Focus) ArcSight documents: the CEF Implementation Standard from the SmartConnector documentation, and the Data Fields reference of the ESM Console User's Guide. The structured YAML files are the primary agent-facing reference; the Markdown docs carry the surrounding format guidance.",
        "",
        f"- **CEF document version**: `{CEF_DOCUMENT_VERSION}` (the HTML topics additionally carry the CEF 1.2 dictionary additions that postdate the PDF)",
        f"- **Predefined extension keys**: `{len(extensions)}` ({producer_count} producer, {consumer_count} consumer, {both_count} in both tables)",
        f"- **ESM version**: `{ESM_VERSION}`",
        f"- **ESM event schema groups**: `{len(groups)}` with `{field_count}` data fields",
        f"- **Extension keys resolved to ESM groups**: `{crosswalk_matches}`",
        f"- **PDF edition of the CEF standard**: {CEF_PDF_URL}",
        f"- **PDF edition of the Console User's Guide**: {ESM_PDF_URL}",
        "",
        "## Source pages",
        "",
        f"- [`{EXTENSIONS_PAGE}`]({cef_page_url(EXTENSIONS_PAGE)}) -> [extensions.yaml](extensions.yaml)",
    ]
    for page, output_path in CEF_DOC_PAGES:
        lines.append(
            f"- [`{page}`]({cef_page_url(page)}) -> "
            f"[{output_path.as_posix()}]({output_path.as_posix()})"
        )
    lines.append(
        f"- [`{ESM_DATA_FIELDS_PAGE}`]"
        f"({esm_page_url(f'Content/ESM_UserGuide/{ESM_DATA_FIELDS_PAGE}')}) -> "
        "[docs/esm-data-fields.md](docs/esm-data-fields.md)"
    )
    for group in groups:
        lines.append(
            f"- [`{group['title']}`]({group['source_url']}) -> "
            f"[groups/{group['name']}.yaml](groups/{group['name']}.yaml)"
        )
    for title, page in suffix_pages:
        lines.append(
            f"- [`{title}`]({esm_page_url(page)}) -> "
            "[docs/field-suffixes.md](docs/field-suffixes.md)"
        )
    lines.extend(
        [
            "",
            "## Known spec quirks",
            "",
        ]
    )
    for quirk in GENERAL_QUIRKS:
        lines.append(f"- {quirk}")
    for key in sorted(EXTENSION_NOTES):
        lines.append(f"- `{key}`: {EXTENSION_NOTES[key]}")
    return clean_markdown("\n".join(lines))


def write_docs(output_dir: Path, docs: dict[Path, str]) -> None:
    shutil.rmtree(output_dir, ignore_errors=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    for relative_path, content in sorted(docs.items()):
        path = output_dir / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()

    with httpx.Client(headers=HTTP_HEADERS, follow_redirects=False, timeout=30.0) as client:
        extensions_html = fetch_page(client, cef_page_url(EXTENSIONS_PAGE))
        cef_html = {page: fetch_page(client, cef_page_url(page)) for page, _ in CEF_DOC_PAGES}
        esm_pages = discover_esm_group_pages(client)
        data_fields_html = fetch_page(
            client, esm_page_url(f"Content/ESM_UserGuide/{ESM_DATA_FIELDS_PAGE}")
        )
        esm_html = {page: fetch_page(client, esm_page_url(page)) for _, page in esm_pages}

    # Split the Data Fields children into 5-column field groups and 2-column
    # attribute-suffix pages, and register their output paths for link
    # rewriting before rendering anything.
    group_pages: list[tuple[str, str]] = []
    suffix_pages: list[tuple[str, str]] = []
    page_outputs = dict(PAGE_OUTPUTS)
    for title, page in esm_pages:
        content = main_content_of(parse_html(esm_html[page]))
        table = content.find(lambda node: node.tag == "table")
        if table is None:
            raise RuntimeError(f"ESM page {page!r} does not contain a table")
        name = page.rsplit("/", 1)[-1]
        if is_suffix_table(table):
            suffix_pages.append((title, page))
            page_outputs[name] = "docs/field-suffixes.md"
        else:
            group_pages.append((title, page))
            page_outputs[name] = f"groups/{group_slug(title)}.yaml"
    if len(suffix_pages) != EXPECTED_SUFFIX_PAGE_COUNT:
        raise RuntimeError(
            f"Found {len(suffix_pages)} attribute-suffix pages; expected "
            f"{EXPECTED_SUFFIX_PAGE_COUNT}"
        )

    extensions = parse_extension_tables(extensions_html, page_outputs)
    validate_extensions(extensions)

    groups = [
        parse_group_page(title, page, esm_html[page], page_outputs)
        for title, page in group_pages
    ]
    validate_esm_groups(groups)
    crosswalk_matches = crosswalk_extensions(extensions, groups)

    docs: dict[Path, str] = {
        Path("SKILL.md"): render_skill_markdown(),
        Path("extensions.yaml"): render_extensions_yaml(extensions),
        Path("catalog.yaml"): render_catalog_yaml(groups),
        Path("source.md"): render_source_page(
            extensions, groups, suffix_pages, crosswalk_matches
        ),
        Path("docs/esm-data-fields.md"): render_page(
            data_fields_html, page_outputs, Path("docs/esm-data-fields.md")
        ),
        Path("docs/field-suffixes.md"): clean_markdown(
            "\n\n".join(
                render_page(esm_html[page], page_outputs, Path("docs/field-suffixes.md")).rstrip()
                for _, page in suffix_pages
            )
        ),
    }
    for page, output_path in CEF_DOC_PAGES:
        docs[output_path] = render_page(cef_html[page], page_outputs, output_path)
    for group in groups:
        docs[Path(f"groups/{group['name']}.yaml")] = render_group_yaml(group)

    write_docs(output_dir, docs)
    field_count = sum(len(group["fields"]) for group in groups)
    print(
        f"Generated ArcSight CEF skill with {len(extensions)} extension keys "
        f"and {field_count} ESM fields in {len(groups)} groups in {output_dir}"
    )


if __name__ == "__main__":
    main()
