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
import re
import shutil
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable

import httpx
import yaml


IBM_DOCS_API = "https://www.ibm.com/docs/api/v1/content/SS42VS_DSM/com.ibm.dsm.doc"
IBM_DOCS_TOPIC = "https://www.ibm.com/docs/en/dsm?topic"
LEEF_PDF_URL = "https://www.ibm.com/docs/en/SS42VS_DSM/pdf/b_Leef_format_guide.pdf"
HTTP_HEADERS = {
    "User-Agent": "tenzir-leef-generator",
    "Accept": "text/html",
}

ATTRIBUTES_TOPIC = "c_LEEF_Format_Guide_predefinedAttrrs"

# IBM Docs topics rendered into Markdown docs, in reading order.
DOC_TOPICS = (
    ("c_LEEF_Format_Guide_intro", Path("docs/overview.md")),
    ("c_LEEF_Format_Guide_LEEFeventcomps", Path("docs/event-components.md")),
    ("c_LEEF_Format_Guide_customkeys", Path("docs/custom-keys.md")),
    ("c_LEEF_Format_Guide_bestpractices", Path("docs/best-practices.md")),
    ("c_LEEF_Format_Guide_dateformat", Path("docs/date-format.md")),
)

# Public deep link to the interactive page that mirrors the attributes topic.
ATTRIBUTES_PUBLIC_URL = f"{IBM_DOCS_TOPIC}=overview-predefined-leef-event-attributes"

# Rewrites for cross-topic links inside generated docs (paths relative to the
# skill root; the renderer adjusts them per output file).
TOPIC_OUTPUTS = {
    "c_LEEF_Format_Guide_intro.html": "docs/overview.md",
    "c_LEEF_Format_Guide_LEEFeventcomps.html": "docs/event-components.md",
    "c_LEEF_Format_Guide_predefinedAttrrs.html": "attributes.yaml",
    "c_LEEF_Format_Guide_customkeys.html": "docs/custom-keys.md",
    "c_LEEF_Format_Guide_bestpractices.html": "docs/best-practices.md",
    "c_LEEF_Format_Guide_dateformat.html": "docs/date-format.md",
}

VALUE_TYPE_MAP = {
    "String": "string",
    "Date": "date",
    "Integer": "integer",
    "Integer or Keyword": "integer_or_keyword",
    "IPv4 or IPv6 Address": "ip_address",
    "MAC Address": "mac_address",
    "Boolean string": "boolean_string",
}

NORMALIZED_MAP = {"Yes": True, "No": False, "Key": None}

# Annotations for quirks IBM published in the spec itself. Verified against
# both the web guide and the PDF.
ATTRIBUTE_NOTES = {
    "identSecondlp": (
        "The published key name contains an IBM documentation typo (likely "
        "intended identSecondIp). Both the web guide and the PDF spell it "
        "identSecondlp; use the key verbatim."
    ),
    "identHostName": (
        'IBM\'s table lists "Key" instead of "Yes" or "No" in the normalized '
        "column, in both the web guide and the PDF, so normalized is null."
    ),
}

# Quirks in the rendered docs pages, outside the attribute table.
DOC_NOTES = {
    "docs/event-components.md": (
        "IBM's delimiter table labels the hex value x7c as a broken vertical "
        "bar (¦), but 0x7C is the regular pipe (|); the broken bar is "
        "0xA6. The error is IBM's and is preserved verbatim."
    ),
}

EXPECTED_KEYS = {"cat", "devTime", "devTimeFormat", "proto", "sev", "src", "dst", "usrName"}
MINIMUM_ATTRIBUTE_COUNT = 40

LIMITS_RE = re.compile(r"^Attribute\s+Limits:\s*(.+)$")
RESERVED_RE = re.compile(
    r"reserved (?:in the LEEF (?:specification|format)|for future use)", re.IGNORECASE
)


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
CODE_CLASSES = {"codeph", "systemoutput", "parmname", "option", "varname"}


@dataclass(frozen=True, slots=True)
class RenderContext:
    # Rewrites an internal topic href to a link target, or None to unlink.
    rewrite_link: Callable[[str], str | None]


def render_inline(node: Node | str, ctx: RenderContext) -> str:
    if isinstance(node, str):
        return escape_angle_brackets(node)
    if node.tag in SKIP_TAGS:
        return ""
    if node.tag in {"code", "samp", "kbd", "tt", "var"} or (
        node.tag == "span" and node.classes() & CODE_CLASSES
    ):
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
    if node.tag == "div" and "note" in node.classes():
        return [render_note(node, ctx)]
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


def render_note(node: Node, ctx: RenderContext) -> str:
    title_node = node.find(
        lambda element: element.tag == "span" and any(
            cls.endswith("title") for cls in element.classes()
        )
    )
    title = title_node.text().rstrip(":") if title_node else "Note"
    if title_node:
        node = Node(node.tag, node.attrs, [
            child for child in node.children if child is not title_node
        ])
    body = render_blocks(node, ctx)
    body_lines: list[str] = []
    for index, block in enumerate(body):
        if index:
            body_lines.append("")
        body_lines.extend(block.splitlines())
    if len(body) == 1 and "\n" not in body[0]:
        # Single-paragraph body: inline it after the title.
        return f"> **{title}:** {body[0]}"
    lines = [f"> **{title}:**"]
    lines.extend(f"> {line}" if line else ">" for line in body_lines)
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


def article_of(document: Node) -> Node:
    article = document.find(lambda node: node.tag == "article")
    if article is None:
        raise RuntimeError("IBM Docs topic does not contain an <article> element")
    return article


def link_rewriter(output_path: Path) -> Callable[[str], str | None]:
    def rewrite(href: str) -> str | None:
        base = href.split("#", 1)[0].split("?", 1)[0]
        if base in TOPIC_OUTPUTS:
            target = Path(TOPIC_OUTPUTS[base])
            prefix = "../" * (len(output_path.parts) - 1)
            return f"{prefix}{target.as_posix()}"
        if href.startswith(("http://", "https://")):
            return href
        # Unlinked internal topics fall back to plain text.
        return None

    return rewrite


def render_topic(html: str, output_path: Path) -> str:
    article = article_of(parse_html(html))
    ctx = RenderContext(rewrite_link=link_rewriter(output_path))
    return clean_markdown("\n\n".join(render_blocks(article, ctx)))


# --- Predefined attribute table parsing -------------------------------------


def cell_blocks(cell: Node, ctx: RenderContext) -> list[str]:
    return render_blocks(cell, ctx)


def extract_limits(blocks: list[str]) -> tuple[list[str], list[str]]:
    remaining: list[str] = []
    limits: list[str] = []
    for block in blocks:
        match = LIMITS_RE.match(block)
        if match:
            limits.append(match.group(1).strip())
        else:
            remaining.append(block)
    return remaining, limits


def parse_attribute_rows(html: str) -> tuple[list[dict[str, Any]], list[str]]:
    article = article_of(parse_html(html))
    ctx = RenderContext(rewrite_link=link_rewriter(Path("attributes.yaml")))
    table = article.find(lambda node: node.tag == "table")
    if table is None:
        raise RuntimeError("Predefined attributes topic does not contain a table")

    attributes: list[dict[str, Any]] = []
    body = table.find(lambda node: node.tag == "tbody") or table
    for row in body.find_all(lambda node: node.tag == "tr"):
        cells = [cell for cell in row.elements() if cell.tag == "td"]
        if len(cells) != 4:
            raise RuntimeError(f"Expected 4 columns per attribute row, got {len(cells)}")
        key_cell, type_cell, normalized_cell, description_cell = cells

        key_node = key_cell.find(
            lambda node: node.tag == "span" and "parmname" in node.classes()
        )
        if key_node is None:
            raise RuntimeError(f"Attribute row has no key: {key_cell.text()!r}")
        key = key_node.text()
        continuation = "(continued)" in key_cell.text()

        # Stray text in the key cell (for example calLanguage's misplaced
        # "Attribute Limits: 2") belongs to the attribute metadata.
        key_cell_blocks = [
            block
            for block in cell_blocks(key_cell, ctx)
            if collapse_whitespace(block.replace("`", "")) not in {key, f"{key} (continued)"}
        ]
        key_cell_blocks = [
            re.sub(rf"^`{re.escape(key)}`(\s*\(continued\))?\s*", "", block)
            for block in key_cell_blocks
        ]
        key_cell_blocks = [block for block in key_cell_blocks if block]

        value_type = collapse_whitespace(type_cell.text())
        if value_type not in VALUE_TYPE_MAP:
            raise RuntimeError(f"Unknown LEEF value type {value_type!r} for key {key!r}")

        normalized_text = collapse_whitespace(normalized_cell.text())
        if normalized_text not in NORMALIZED_MAP:
            raise RuntimeError(
                f"Unexpected normalized marker {normalized_text!r} for key {key!r}"
            )

        description_blocks, limits = extract_limits(
            cell_blocks(description_cell, ctx) + key_cell_blocks
        )
        description = "\n\n".join(description_blocks)

        if continuation:
            if not attributes or attributes[-1]["key"] != key:
                raise RuntimeError(f"Continuation row for {key!r} has no preceding row")
            previous = attributes[-1]
            previous["description"] = f"{previous['description']}\n\n{description}"
            if limits:
                previous.setdefault("_limits", []).extend(limits)
            continue

        attributes.append(
            {
                "key": key,
                "type": VALUE_TYPE_MAP[value_type],
                "normalized": NORMALIZED_MAP[normalized_text],
                "description": description,
                "_limits": limits,
            }
        )

    # The prose around the table documents how QRadar handles non-normalized
    # keys; keep it as context next to the structured data.
    table_container = article.find(lambda node: "tablenoborder" in node.classes())
    notes_blocks: list[str] = []
    body_div = article.find(lambda node: node.tag == "div" and "body" in node.classes())
    if body_div is not None:
        passed_table = False
        for child in body_div.elements():
            if child is table_container or child.find(lambda node: node is table) is not None:
                passed_table = True
                continue
            if passed_table:
                notes_blocks.extend(render_block(child, ctx))
    return attributes, notes_blocks


def finalize_attributes(raw: list[dict[str, Any]]) -> list[dict[str, Any]]:
    attributes: list[dict[str, Any]] = []
    for entry in raw:
        attribute: dict[str, Any] = {
            "key": entry["key"],
            "type": entry["type"],
            "normalized": entry["normalized"],
            "description": entry["description"],
        }
        limits = list(dict.fromkeys(entry.get("_limits", [])))
        if len(limits) > 1:
            raise RuntimeError(f"Conflicting attribute limits for {entry['key']!r}: {limits}")
        if limits:
            attribute["limits"] = limits[0]
        if RESERVED_RE.search(entry["description"]):
            attribute["reserved"] = True
        if entry["key"] in ATTRIBUTE_NOTES:
            attribute["notes"] = ATTRIBUTE_NOTES[entry["key"]]
        attributes.append(attribute)
    return attributes


def validate_attributes(attributes: list[dict[str, Any]]) -> None:
    if len(attributes) < MINIMUM_ATTRIBUTE_COUNT:
        raise RuntimeError(
            f"Parsed only {len(attributes)} attributes; expected at least "
            f"{MINIMUM_ATTRIBUTE_COUNT}. The IBM page layout may have changed."
        )
    keys = [attribute["key"] for attribute in attributes]
    duplicates = {key for key in keys if keys.count(key) > 1}
    if duplicates:
        raise RuntimeError(f"Duplicate attribute keys parsed: {sorted(duplicates)}")
    missing = EXPECTED_KEYS - set(keys)
    if missing:
        raise RuntimeError(f"Expected attribute keys are missing: {sorted(missing)}")
    for attribute in attributes:
        if not attribute["description"]:
            raise RuntimeError(f"Attribute {attribute['key']!r} has an empty description")


# --- Output rendering -------------------------------------------------------


def render_attributes_yaml(
    attributes: list[dict[str, Any]], parsing_notes: list[str]
) -> str:
    data: dict[str, Any] = {
        "leef_version": "2.0",
        "source": ATTRIBUTES_PUBLIC_URL,
        "description": (
            "Predefined LEEF event attributes. Use these keys in the event "
            "payload whenever they match the data; add custom keys only when "
            "no predefined attribute fits. Keys with normalized: true are "
            "parsed into normalized QRadar event fields automatically; "
            "normalized: false keys require a custom event property to "
            "surface in the QRadar Log Activity tab. Keys with reserved: "
            "true are reserved in the LEEF specification but not implemented "
            "in QRadar."
        ),
        "parsing_notes": "\n\n".join(parsing_notes),
        "attributes": attributes,
    }
    return dump_yaml(data)


def render_skill_markdown() -> str:
    return clean_markdown(
        "\n".join(
            [
                "---",
                "name: tenzir-leef",
                "description: >-",
                "  Answer questions and produce mappings for IBM LEEF (Log Event",
                "  Extended Format), the QRadar event format: LEEF 1.0/2.0 headers,",
                "  delimiters, predefined event attributes, custom event keys,",
                "  devTime/devTimeFormat timestamps, and syslog transport. Use when",
                "  generating, parsing, validating, or mapping logs to or from LEEF,",
                "  building QRadar or JSA integrations and DSMs, or when the user",
                "  mentions LEEF payloads, QRadar log formats, QID mapping, or",
                "  key=value events with a LEEF: header.",
                "---",
                "",
                "# Log Event Extended Format",
                "",
                "LEEF (Log Event Extended Format) is IBM's event format for QRadar. A LEEF event is a single line consisting of an optional syslog header, a pipe-delimited LEEF header, and a flat list of `key=value` event attributes.",
                "",
                "The latest LEEF version is 2.0, which this skill documents. LEEF 2.0 adds one optional header field to LEEF 1.0: a delimiter character for the event attributes. Both header layouts are covered in [LEEF event components](docs/event-components.md).",
                "",
                "Use [attributes.yaml](attributes.yaml) as the authoritative reference for the predefined event attributes: exact key spelling, value type, normalization behavior, limits, and reserved status. If an attribute is not present there, it is not a predefined LEEF attribute.",
                "",
                "## Data files",
                "",
                "- Use [attributes.yaml](attributes.yaml) to look up predefined event attributes.",
                "- Use [docs/overview.md](docs/overview.md) for what LEEF is and how QRadar discovers LEEF event sources.",
                "- Use [docs/event-components.md](docs/event-components.md) for the syslog header, the LEEF 1.0/2.0 header fields, and delimiter rules.",
                "- Use [docs/custom-keys.md](docs/custom-keys.md) and [docs/best-practices.md](docs/best-practices.md) for non-predefined keys.",
                "- Use [docs/date-format.md](docs/date-format.md) for `devTime`/`devTimeFormat` patterns.",
                "- Use [source.md](source.md) for upstream provenance and counts.",
                "",
                "## Format rules",
                "",
                "- Encode LEEF events as UTF-8.",
                "- A LEEF 2.0 event has the shape `<syslog header> LEEF:2.0|Vendor|Product|Version|EventID|DelimiterCharacter|key=value<delim>key=value...`; the syslog header and the delimiter field are optional.",
                "- A LEEF 1.0 header has no delimiter field: `LEEF:1.0|Vendor|Product|Version|EventID|`; attributes are always tab-separated.",
                "- The LEEF 2.0 delimiter is a single character or a hex value prefixed with `0x` or `x` followed by 1-4 hex digits (for example `^`, `x5E`, or `0x09`); when omitted, tab is the default.",
                "- The EventID must be static across product languages and at most 255 characters; use `cat` to subdivide an EventID further.",
                "- Attribute order is not enforced, but each key may appear only once per payload.",
                "- Prefer predefined attribute keys from [attributes.yaml](attributes.yaml); create custom keys only when no predefined attribute fits, keep them single-word alphanumeric, and never reuse a predefined key name.",
                "- Express event time with `devTime`; pair it with `devTimeFormat` (a Java SimpleDateFormat pattern) unless `devTime` is a 10- or 13-digit epoch value.",
                "",
                "## Question routing",
                "",
                "- **What does attribute X mean, what type is it, what are its limits?** Use [attributes.yaml](attributes.yaml).",
                "- **How do I build or parse the LEEF header or pick a delimiter?** Read [docs/event-components.md](docs/event-components.md).",
                "- **Which syslog header formats are accepted?** Read [docs/event-components.md](docs/event-components.md).",
                "- **How do I encode timestamps?** Read [docs/date-format.md](docs/date-format.md) together with the `devTime` and `devTimeFormat` entries in [attributes.yaml](attributes.yaml).",
                "- **There is no predefined key for my data.** Read [docs/custom-keys.md](docs/custom-keys.md) and [docs/best-practices.md](docs/best-practices.md).",
                "- **How does QRadar discover and categorize LEEF events?** Read [docs/overview.md](docs/overview.md).",
                "- **What upstream source backs this skill?** Use [source.md](source.md).",
                "",
            ]
        )
    )


def render_source_page(attributes: list[dict[str, Any]]) -> str:
    normalized_count = sum(1 for attribute in attributes if attribute["normalized"] is True)
    reserved_count = sum(1 for attribute in attributes if attribute.get("reserved"))
    lines = [
        "# Source",
        "",
        "This skill is generated from the IBM QRadar LEEF Version 2 format guide, fetched from the IBM Docs content API. The structured [attributes.yaml](attributes.yaml) is the primary agent-facing reference; the Markdown docs carry the surrounding format guidance.",
        "",
        f"- **Predefined attributes**: `{len(attributes)}`",
        f"- **Normalized attributes**: `{normalized_count}`",
        f"- **Reserved (not implemented in QRadar)**: `{reserved_count}`",
        f"- **PDF edition of the guide**: {LEEF_PDF_URL}",
        "",
        "## Source topics",
        "",
        f"- Predefined LEEF event attributes: [`{ATTRIBUTES_TOPIC}`]({IBM_DOCS_API}/{ATTRIBUTES_TOPIC}.html) -> [attributes.yaml](attributes.yaml)",
    ]
    for topic, output_path in DOC_TOPICS:
        lines.append(
            f"- [`{topic}`]({IBM_DOCS_API}/{topic}.html) -> "
            f"[{output_path.as_posix()}]({output_path.as_posix()})"
        )
    lines.extend(
        [
            "",
            "## Known spec quirks preserved verbatim",
            "",
        ]
    )
    for key in sorted(ATTRIBUTE_NOTES):
        lines.append(f"- `{key}`: {ATTRIBUTE_NOTES[key]}")
    for path in sorted(DOC_NOTES):
        lines.append(f"- [{path}]({path}): {DOC_NOTES[path]}")
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


def fetch_topic(client: httpx.Client, topic: str) -> str:
    response = client.get(f"{IBM_DOCS_API}/{topic}.html")
    response.raise_for_status()
    return response.text


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()

    with httpx.Client(headers=HTTP_HEADERS, follow_redirects=True, timeout=30.0) as client:
        attributes_html = fetch_topic(client, ATTRIBUTES_TOPIC)
        topic_html = {topic: fetch_topic(client, topic) for topic, _ in DOC_TOPICS}

    raw_attributes, parsing_notes = parse_attribute_rows(attributes_html)
    attributes = finalize_attributes(raw_attributes)
    validate_attributes(attributes)

    docs: dict[Path, str] = {
        Path("SKILL.md"): render_skill_markdown(),
        Path("attributes.yaml"): render_attributes_yaml(attributes, parsing_notes),
        Path("source.md"): render_source_page(attributes),
    }
    for topic, output_path in DOC_TOPICS:
        docs[output_path] = render_topic(topic_html[topic], output_path)

    write_docs(output_dir, docs)
    print(f"Generated IBM LEEF skill with {len(attributes)} attributes in {output_dir}")


if __name__ == "__main__":
    main()
