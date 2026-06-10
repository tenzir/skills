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
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable

import httpx
import yaml


DEFAULT_VERSION = "7.5.0"
DEFAULT_BASE_URL = "https://docs.fortinet.com/document/fortisiem"
DOCUMENT_SLUG = "fortisiem-event-data-model"
OVERVIEW_PAGE = "747605/overview"
HTTP_HEADERS = {"User-Agent": "tenzir-edm-generator"}
EXPECTED_TABLE_HEADERS = (
    ("Event Attribute", "Type", "Display Name", "Description"),
    ("Event Attribute", "Type", "Name", "Description"),
)
SECTION_HEADING_STYLE_MARKER = "font-size: 24px"
MAIN_CONTENT_MARKER = 'id="mc-main-content"'
MINIMUM_MODEL_PAGES = 15
ATTRIBUTE_NAME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


@dataclass(frozen=True, slots=True)
class PageRef:
    doc_id: str
    slug: str
    title: str
    url: str


@dataclass(frozen=True, slots=True)
class AttributeRecord:
    name: str
    attribute_type: str
    display_name: str
    description: str
    section: str


@dataclass(frozen=True, slots=True)
class ModelDoc:
    name: str
    page: PageRef
    summary: str
    sections: tuple[str, ...]
    attributes: tuple[AttributeRecord, ...]
    markdown: str

    @property
    def title(self) -> str:
        return self.page.title


@dataclass(frozen=True, slots=True)
class FortiSiemReference:
    version: str
    document_url: str
    overview_page: PageRef
    overview_markdown: str
    models: tuple[ModelDoc, ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--version",
        default=DEFAULT_VERSION,
        help=f"FortiSIEM Event Data Model document version (default: {DEFAULT_VERSION})",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"Fortinet document library root (default: {DEFAULT_BASE_URL})",
    )
    return parser.parse_args()


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\xa0", " ")).strip()


def clean_markdown(text: str) -> str:
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def to_slug(value: str) -> str:
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    return value.strip("_").lower() or "index"


def model_key(page_slug: str) -> str:
    return re.sub(r"-data-model$", "", page_slug).replace("-", "_")


def stable_name_key(value: str) -> tuple[str, str]:
    return value.casefold(), value


def data_model_path(name: str) -> str:
    return f"models/{name}.yaml"


def data_attribute_path(attribute_name: str) -> str:
    return f"attributes/{to_slug(attribute_name)}.yaml"


def docs_page_path(page: PageRef) -> str:
    return f"docs/{page.slug}.md"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: object) -> bool:
        return True


def dump_yaml(data: Any) -> str:
    return yaml.dump(
        data,
        Dumper=NoAliasDumper,
        allow_unicode=False,
        sort_keys=False,
        width=1_000_000,
    )


def compact_mapping(items: Iterable[tuple[str, Any]]) -> dict[str, Any]:
    return {
        key: value
        for key, value in items
        if value not in (None, "", [], (), {})
    }


def main_content_region(page_html: str, url: str) -> str:
    first = page_html.find(MAIN_CONTENT_MARKER)
    if first == -1:
        raise RuntimeError(
            f"{url}: no {MAIN_CONTENT_MARKER!r} region found; "
            "the Fortinet docs page layout changed or the request was challenged"
        )
    start = page_html.index(">", first) + 1
    second = page_html.find(MAIN_CONTENT_MARKER, start)
    end = len(page_html) if second == -1 else page_html.rfind("<", 0, second)
    region = page_html[start:end]
    # The exported article ends with a stray closing body/html pair, followed by
    # previous/next navigation and footer markup that is not article content.
    body_end = region.find("</body></html>")
    if body_end != -1:
        region = region[:body_end]
    return region


def is_section_heading(tag: str, attrs: dict[str, str | None]) -> bool:
    return tag == "p" and SECTION_HEADING_STYLE_MARKER in (attrs.get("style") or "")


class ModelPageParser(HTMLParser):
    """Extract the title, overview prose, section headings, and attribute tables."""

    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.overview_blocks: list[tuple[str, str, str]] = []
        self.tables: list[dict[str, Any]] = []
        self.current_section = ""
        self.body_started = False
        self.in_heading = False
        self.heading_parts: list[str] = []
        self.in_section_heading = False
        self.section_parts: list[str] = []
        self.in_table = False
        self.in_cell = False
        self.cell_parts: list[str] = []
        self.row: list[str] = []
        self.row_is_header = False
        self.block_kind: str | None = None
        self.block_parts: list[str] = []
        self.block_anchor_parts: list[str] = []
        self.in_internal_link = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "table":
            classes = (attrs_dict.get("class") or "").split()
            if "TableStyle-FortinetTable" in classes:
                self.in_table = True
                self.body_started = True
                self.tables.append({"section": self.current_section, "header": None, "rows": []})
            return
        if self.in_table:
            if tag == "tr":
                self.row = []
                self.row_is_header = False
            elif tag in {"th", "td"}:
                self.in_cell = True
                self.cell_parts = []
                if tag == "th":
                    self.row_is_header = True
            return
        if tag in {"h1", "h2"}:
            self.in_heading = True
            self.heading_parts = []
        elif is_section_heading(tag, attrs_dict):
            self.in_section_heading = True
            self.section_parts = []
            self.body_started = True
        elif tag == "li":
            self.block_kind = "li"
            self.block_parts = []
            self.block_anchor_parts = []
        elif tag == "p" and self.block_kind is None:
            self.block_kind = "p"
            self.block_parts = []
            self.block_anchor_parts = []
        elif tag == "a" and self.block_kind is not None:
            href = attrs_dict.get("href") or ""
            if href.startswith("#"):
                self.in_internal_link = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "table" and self.in_table:
            self.in_table = False
            return
        if self.in_table:
            if tag in {"th", "td"} and self.in_cell:
                self.row.append(clean_text(" ".join(self.cell_parts)))
                self.in_cell = False
            elif tag == "tr":
                if self.row:
                    table = self.tables[-1]
                    if self.row_is_header and table["header"] is None:
                        table["header"] = tuple(self.row)
                    else:
                        table["rows"].append(tuple(self.row))
                self.row = []
            return
        if tag in {"h1", "h2"} and self.in_heading:
            text = clean_text(" ".join(self.heading_parts))
            if text and not self.title:
                self.title = text
            self.in_heading = False
        elif tag == "p" and self.in_section_heading:
            self.current_section = clean_text(" ".join(self.section_parts))
            self.in_section_heading = False
        elif tag == self.block_kind:
            self.finish_block()
        elif tag == "a":
            self.in_internal_link = False

    def handle_data(self, data: str) -> None:
        if self.in_table:
            if self.in_cell:
                self.cell_parts.append(data)
            return
        if self.in_section_heading:
            self.section_parts.append(data)
        elif self.in_heading:
            self.heading_parts.append(data)
        elif self.block_kind is not None:
            self.block_parts.append(data)
            if self.in_internal_link:
                self.block_anchor_parts.append(data)

    def finish_block(self) -> None:
        text = clean_text(" ".join(self.block_parts))
        anchor_text = clean_text(" ".join(self.block_anchor_parts))
        if text and not self.body_started:
            self.overview_blocks.append((self.block_kind or "p", text, anchor_text))
        self.block_kind = None
        self.block_parts = []
        self.block_anchor_parts = []
        self.in_internal_link = False


class MarkdownRenderer(HTMLParser):
    """Convert a Fortinet docs content region into Markdown for audit copies."""

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.heading_level: int | None = None
        self.heading_parts: list[str] = []
        self.in_code = False
        self.in_pre = False
        self.in_table = False
        self.in_cell = False
        self.table_header_written = False
        self.ignored_depth = 0
        self.cell_parts: list[str] = []
        self.row: list[str] = []
        self.list_item_depth = 0

    def append(self, value: str) -> None:
        if self.in_cell:
            self.cell_parts.append(value)
        elif self.heading_level is not None:
            self.heading_parts.append(value)
        else:
            self.parts.append(value)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if self.ignored_depth:
            self.ignored_depth += 1
            return
        if tag in {"script", "style"}:
            self.ignored_depth = 1
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_level = max(1, int(tag[1]) - 1)
            self.heading_parts = []
        elif is_section_heading(tag, attrs_dict):
            self.heading_level = 2
            self.heading_parts = []
        elif tag in {"p", "section", "div"}:
            if not self.list_item_depth:
                self.append("\n\n")
        elif tag == "br":
            self.append("\n")
        elif tag in {"ul", "ol"}:
            self.append("\n")
        elif tag == "li":
            self.list_item_depth += 1
            self.append("\n- ")
        elif tag == "code":
            if self.in_pre:
                return
            self.in_code = True
            self.append("`")
        elif tag == "pre":
            self.in_pre = True
            self.parts.append("\n\n```text\n")
        elif tag == "table":
            self.in_table = True
            self.table_header_written = False
            self.parts.append("\n\n")
        elif tag in {"th", "td"} and self.in_table:
            self.in_cell = True
            self.cell_parts = []

    def handle_endtag(self, tag: str) -> None:
        if self.ignored_depth:
            self.ignored_depth -= 1
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"} and self.heading_level is not None:
            self.finish_heading()
        elif tag == "p" and self.heading_level is not None:
            self.finish_heading()
        elif tag == "li" and self.list_item_depth:
            self.list_item_depth -= 1
        elif tag == "code" and self.in_code:
            self.append("`")
            self.in_code = False
        elif tag == "pre" and self.in_pre:
            self.parts.append("\n```\n\n")
            self.in_pre = False
        elif tag in {"th", "td"} and self.in_table and self.in_cell:
            self.row.append(clean_text(" ".join(self.cell_parts)))
            self.cell_parts = []
            self.in_cell = False
        elif tag == "tr" and self.in_table:
            if self.row:
                escaped = [cell.replace("|", "\\|") for cell in self.row]
                self.parts.append("| " + " | ".join(escaped) + " |\n")
                if not self.table_header_written:
                    self.parts.append("| " + " | ".join("---" for _ in escaped) + " |\n")
                    self.table_header_written = True
            self.row = []
        elif tag == "table" and self.in_table:
            self.in_table = False
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.ignored_depth:
            return
        if self.in_pre:
            self.append(data)
            return
        text = clean_text(data)
        if not text:
            return
        self.append(text + " ")

    def finish_heading(self) -> None:
        text = clean_text(" ".join(self.heading_parts))
        if text:
            self.parts.append(f"\n\n{'#' * (self.heading_level or 1)} {text}\n\n")
        self.heading_level = None
        self.heading_parts = []

    @property
    def markdown(self) -> str:
        return clean_markdown("".join(self.parts))


def render_page_markdown(region: str, url: str) -> str:
    renderer = MarkdownRenderer()
    renderer.feed(region)
    renderer.close()
    return clean_markdown(f"<!-- Source: {url} -->\n\n{renderer.markdown}")


def document_url(base_url: str, version: str) -> str:
    return f"{base_url}/{version}/{DOCUMENT_SLUG}/"


def page_url(base_url: str, version: str, doc_id: str, slug: str) -> str:
    return f"{base_url}/{version}/{DOCUMENT_SLUG}/{doc_id}/{slug}"


def fetch_page(client: httpx.Client, url: str, *, attempts: int = 4) -> str:
    for attempt in range(1, attempts + 1):
        try:
            response = client.get(url)
            response.raise_for_status()
            return response.text
        except (httpx.TransportError, httpx.HTTPStatusError) as error:
            if attempt == attempts:
                raise
            delay = 2**attempt
            print(f"warning: {url}: {error}; retrying in {delay}s", file=sys.stderr)
            time.sleep(delay)
    raise AssertionError("unreachable")


def discover_model_pages(region: str, base_url: str, version: str) -> tuple[PageRef, ...]:
    pattern = re.compile(
        r'<a\s+href="/document/fortisiem/[^"/]+/' + re.escape(DOCUMENT_SLUG) + r'/(\d+)/([a-z0-9-]+)"\s*>(.*?)</a>',
        re.S,
    )
    pages: list[PageRef] = []
    seen: set[str] = set()
    for match in pattern.finditer(region):
        doc_id, slug, label = match.groups()
        if slug == "overview" or slug in seen:
            continue
        seen.add(slug)
        title = clean_text(re.sub(r"<[^>]+>", "", label))
        pages.append(
            PageRef(
                doc_id=doc_id,
                slug=slug,
                title=title,
                url=page_url(base_url, version, doc_id, slug),
            )
        )
    if len(pages) < MINIMUM_MODEL_PAGES:
        raise RuntimeError(
            f"Discovered only {len(pages)} model pages on the overview page; "
            f"expected at least {MINIMUM_MODEL_PAGES}. The upstream document layout changed."
        )
    return tuple(pages)


def build_summary(blocks: list[tuple[str, str, str]]) -> str:
    sentences: list[str] = []
    pending_items: list[str] = []

    def flush() -> None:
        nonlocal pending_items
        if not pending_items:
            return
        joined = ", ".join(pending_items) + "."
        if sentences and sentences[-1].endswith(":"):
            sentences[-1] = f"{sentences[-1]} {joined}"
        else:
            sentences.append(joined)
        pending_items = []

    for kind, text, anchor_text in blocks:
        if anchor_text and anchor_text == text:
            continue
        if kind == "li":
            pending_items.append(text.rstrip("."))
            continue
        flush()
        sentences.append(text)
    flush()
    return " ".join(sentences)


def parse_attribute_rows(table: dict[str, Any], page: PageRef) -> list[AttributeRecord]:
    records: list[AttributeRecord] = []
    header = table["header"]
    for row in table["rows"]:
        if len(row) != len(header):
            raise RuntimeError(f"{page.url}: table row has {len(row)} cells: {row!r}")
        name, attribute_type, display_name, description = row
        if not name:
            continue
        if not ATTRIBUTE_NAME_PATTERN.match(name):
            print(f"warning: {page.url}: unusual attribute name {name!r}", file=sys.stderr)
        records.append(
            AttributeRecord(
                name=name,
                attribute_type=attribute_type,
                display_name=display_name,
                description=description,
                section=table["section"],
            )
        )
    if not records:
        raise RuntimeError(f"{page.url}: attribute table has no data rows")
    return records


def parse_model_page(page: PageRef, page_html: str) -> ModelDoc:
    region = main_content_region(page_html, page.url)
    parser = ModelPageParser()
    parser.feed(region)
    parser.close()
    attributes: list[AttributeRecord] = []
    sections: list[str] = []
    for table in parser.tables:
        if table["header"] not in EXPECTED_TABLE_HEADERS:
            print(
                f"note: {page.url}: skipping non-attribute table with header {table['header']!r}",
                file=sys.stderr,
            )
            continue
        if table["section"] and table["section"] not in sections:
            sections.append(table["section"])
        for record in parse_attribute_rows(table, page):
            if record in attributes:
                print(f"note: {page.url}: dropping duplicate row for {record.name!r}", file=sys.stderr)
                continue
            attributes.append(record)
    if not attributes:
        raise RuntimeError(f"{page.url}: no attribute tables found")
    title = parser.title or page.title
    return ModelDoc(
        name=model_key(page.slug),
        page=PageRef(doc_id=page.doc_id, slug=page.slug, title=title, url=page.url),
        summary=build_summary(parser.overview_blocks),
        sections=tuple(sections),
        attributes=tuple(attributes),
        markdown=render_page_markdown(region, page.url),
    )


def build_reference(version: str, base_url: str) -> FortiSiemReference:
    overview_url = page_url(base_url, version, *OVERVIEW_PAGE.split("/"))
    with httpx.Client(headers=HTTP_HEADERS, follow_redirects=True, timeout=30.0) as client:
        overview_html = fetch_page(client, overview_url)
        overview_region = main_content_region(overview_html, overview_url)
        pages = discover_model_pages(overview_region, base_url, version)
        models = tuple(parse_model_page(page, fetch_page(client, page.url)) for page in pages)
    overview_page = PageRef(
        doc_id=OVERVIEW_PAGE.split("/")[0],
        slug="overview",
        title="Overview",
        url=overview_url,
    )
    return FortiSiemReference(
        version=version,
        document_url=document_url(base_url, version),
        overview_page=overview_page,
        overview_markdown=render_page_markdown(overview_region, overview_url),
        models=models,
    )


def attribute_occurrences(reference: FortiSiemReference) -> dict[str, list[tuple[ModelDoc, AttributeRecord]]]:
    occurrences: dict[str, list[tuple[ModelDoc, AttributeRecord]]] = defaultdict(list)
    for model in reference.models:
        for record in model.attributes:
            occurrences[record.name].append((model, record))
    slugs: dict[str, str] = {}
    for name in occurrences:
        slug = to_slug(name)
        if slug in slugs and slugs[slug] != name:
            raise RuntimeError(f"attribute file collision: {slugs[slug]!r} and {name!r} both map to {slug!r}")
        slugs[slug] = name
    return dict(occurrences)


def attribute_types(reference: FortiSiemReference) -> list[str]:
    """The type vocabulary for SKILL.md: case variants merged, malformed values dropped."""
    counts: Counter[str] = Counter(
        record.attribute_type
        for model in reference.models
        for record in model.attributes
        if record.attribute_type and " " not in record.attribute_type
    )
    by_fold: dict[str, Counter[str]] = defaultdict(Counter)
    for value, count in counts.items():
        by_fold[value.casefold()][value] += count
    return sorted(
        (spellings.most_common(1)[0][0] for spellings in by_fold.values()),
        key=stable_name_key,
    )


def attribute_record_count(reference: FortiSiemReference) -> int:
    return sum(len(model.attributes) for model in reference.models)


def first_unique(values: Iterable[str]) -> list[str]:
    unique: list[str] = []
    for value in values:
        value = value.strip()
        if value and value not in unique:
            unique.append(value)
    return unique


def most_common(values: Iterable[str]) -> str:
    counts = Counter(value for value in values if value)
    if not counts:
        return ""
    best = max(counts.values())
    for value in counts:
        if counts[value] == best:
            return value
    return ""


def attribute_record_data(record: AttributeRecord, *, include_name: bool) -> dict[str, Any]:
    return compact_mapping(
        (
            ("name", record.name if include_name else ""),
            ("type", record.attribute_type),
            ("display_name", record.display_name),
            ("description", record.description),
            ("section", record.section),
        )
    )


def render_catalog_yaml(reference: FortiSiemReference) -> str:
    data = {
        "version": reference.version,
        "source": reference.document_url,
        "models": {
            model.name: compact_mapping(
                (
                    ("file", data_model_path(model.name)),
                    ("title", model.title),
                    ("source_url", model.page.url),
                    ("attributes", len(model.attributes)),
                    ("sections", list(model.sections)),
                )
            )
            for model in sorted(reference.models, key=lambda item: item.name)
        },
        "indexes": {
            "attributes": "attributes.yaml",
        },
    }
    return dump_yaml(data)


def render_model_yaml(reference: FortiSiemReference, model: ModelDoc) -> str:
    data = compact_mapping(
        (
            ("name", model.name),
            ("title", model.title),
            ("version", reference.version),
            ("source_url", model.page.url),
            ("doc", docs_page_path(model.page)),
            ("summary", model.summary),
            ("attributes", [attribute_record_data(record, include_name=True) for record in model.attributes]),
        )
    )
    return dump_yaml(data)


def render_attributes_index_yaml(occurrences: dict[str, list[tuple[ModelDoc, AttributeRecord]]]) -> str:
    return dump_yaml({name: data_attribute_path(name) for name in sorted(occurrences, key=stable_name_key)})


def render_attribute_yaml(name: str, occurrences: list[tuple[ModelDoc, AttributeRecord]]) -> str:
    ordered = sorted(occurrences, key=lambda item: item[0].name)
    data = compact_mapping(
        (
            ("name", name),
            ("summary", most_common(record.description for _, record in ordered)),
            ("types", first_unique(record.attribute_type for _, record in ordered)),
            ("display_names", first_unique(record.display_name for _, record in ordered)),
            (
                "models",
                [
                    {"name": model.name} | attribute_record_data(record, include_name=False)
                    for model, record in ordered
                ],
            ),
        )
    )
    return dump_yaml(data)


def render_skill_markdown(reference: FortiSiemReference) -> str:
    types = ", ".join(f"`{value}`" for value in attribute_types(reference))
    return clean_markdown(
        "\n".join(
            [
                "---",
                "name: tenzir-edm",
                "description: Answer questions about the FortiSIEM Event Data Model (EDM), Fortinet's normalized event attribute model. Use when the user asks about the FortiSIEM EDM, FortiSIEM event attributes, attribute types or display names, FortiSIEM data models or event categories, FortiSIEM parser attribute mapping, or mapping events into FortiSIEM.",
                "---",
                "",
                "# FortiSIEM Event Data Model (EDM)",
                "",
                "The FortiSIEM Event Data Model describes how FortiSIEM normalizes parsed log data into named event attributes, grouped into data models per event category.",
                "EDM is this skill's shorthand for the model; Fortinet itself uses no acronym.",
                "Use this skill to choose the right data model, inspect event attributes, explain attribute types and display names, and map events into FortiSIEM event attributes for built-in or custom parsers.",
                "",
                "The generated YAML files are the authoritative reference for this skill.",
                "If an attribute, type, display name, or data model is not present in the YAML data, say that it is not documented here.",
                "Use [source.md](source.md) only as the final provenance anchor for the documented FortiSIEM version and raw page copies.",
                "",
                "## How the FortiSIEM event data model fits together",
                "",
                f"FortiSIEM normalizes events into flat records of typed event attributes, documented as {len(reference.models)} data models, one per event category.",
                "The base event data model lists attributes present in every FortiSIEM event, split into attributes set automatically by the parsing framework and attributes a parser must set.",
                "Every other data model adds the attributes relevant to one event category, on top of the base attributes.",
                "Each data model's `summary` names example event types that follow it; the full event type list lives in the FortiSIEM product under Resources > Event Types.",
                "",
                "An event attribute is a typed name contract: the same attribute keeps its name, type, and meaning across all data models that use it.",
                f"Attribute types use a small vocabulary: {types}.",
                "Type values in the YAML data are copied verbatim from the Fortinet pages, which contain occasional case variants and errors; treat case-insensitive matches as the same type.",
                "A few attributes have empty type, display name, and description cells upstream; when a type is missing, use the documented `src` or `dest` counterpart attribute, such as `srcVLAN` for `destVLAN`, as the guide.",
                "Attribute names are camelCase and use role prefixes: `src` for the source of the activity, `dest` for its destination, `host` for the host the event refers to, and `ph` for attributes set by the FortiSIEM (Phoenix) framework itself, such as `phRecvTime` and `phEventCategory`.",
                "Display names are the human-readable labels shown in the FortiSIEM GUI; use attribute names, not display names, in parsers and queries.",
                "Some data models group attributes into named sections, recorded per attribute in the `section` key.",
                "",
                "This document covers the curated cross-device data models only.",
                "The full FortiSIEM attribute dictionary (thousands of attributes) is only browsable in the product under Admin > Device Support > Event Attributes; treat attributes outside the YAML data as undocumented here.",
                "",
                "## Data files",
                "",
                "- Use [catalog.yaml](catalog.yaml) to choose a data model and find the model data file.",
                "- Use `models/<model>.yaml` to map an event into one data model.",
                "- Use [attributes.yaml](attributes.yaml) directly as the attribute-name to attribute-file manifest.",
                "- Use `attributes/<attribute>.yaml` for attribute meaning across data models.",
                "- Use `docs/<page>.md` for the raw Fortinet page content backing a data model.",
                "",
                "## Mapping rules",
                "",
                "- Start from the event category, choose the data model in [catalog.yaml](catalog.yaml), then load the model file.",
                "- Populate the base event attributes first, then the attributes of the selected data model that the source provides.",
                "- Keep attribute names exactly as documented; they are case-sensitive camelCase identifiers.",
                "- Match the documented attribute type when producing values; convert source values rather than changing the attribute.",
                "- Reuse an existing attribute with the same meaning before inventing a source-specific name; check `attributes/<attribute>.yaml` for cross-model meaning.",
                "- When no documented attribute fits, keep the original source field name and say that the attribute is not documented here.",
                "",
                "## Question routing",
                "",
                "| Question pattern | Start here |",
                "| --- | --- |",
                "| Which data model fits this event? | [catalog.yaml](catalog.yaml), then the selected model file |",
                "| What attributes does data model X contain? | `models/<model>.yaml` |",
                "| What does attribute Y mean, and where is it used? | [attributes.yaml](attributes.yaml), then `attributes/<attribute>.yaml` |",
                "| Which attributes does every event carry? | [models/base_event.yaml](models/base_event.yaml) |",
                "| What did the original Fortinet page say? | `docs/<page>.md` |",
                "| Which FortiSIEM version backs this data? | [source.md](source.md) |",
                "",
                "For provenance, the documented FortiSIEM version, and raw page copies, use [source.md](source.md) as the last anchor.",
                "",
            ]
        )
    )


def render_source_page(reference: FortiSiemReference) -> str:
    occurrences = attribute_occurrences(reference)
    lines = [
        "# Source",
        "",
        "This skill is generated from the Fortinet FortiSIEM Event Data Model documentation HTML. The generated YAML files are the primary agent-facing reference; use this page only when provenance or raw source lookup is needed.",
        "",
        f"- **FortiSIEM version**: `{reference.version}`",
        f"- **Document root**: [{reference.document_url}]({reference.document_url})",
        f"- **Overview page**: [docs/overview.md](docs/overview.md) ([upstream]({reference.overview_page.url}))",
        f"- **Generated data models**: `{len(reference.models)}`",
        f"- **Generated distinct attributes**: `{len(occurrences)}`",
        f"- **Generated attribute records**: `{attribute_record_count(reference)}`",
        "",
        "Markdown conversions of the Fortinet documentation pages are copied under `docs/` for audit and parser debugging.",
        "",
        "## Model source pages",
        "",
    ]
    for model in sorted(reference.models, key=lambda item: item.name):
        lines.append(
            f"- [{model.name}]({data_model_path(model.name)}): "
            f"[{docs_page_path(model.page)}]({docs_page_path(model.page)}) "
            f"([upstream]({model.page.url}))"
        )
    return clean_markdown("\n".join(lines))


def build_docs(reference: FortiSiemReference) -> dict[Path, str]:
    occurrences = attribute_occurrences(reference)
    docs: dict[Path, str] = {
        Path("SKILL.md"): render_skill_markdown(reference),
        Path("source.md"): render_source_page(reference),
        Path("catalog.yaml"): render_catalog_yaml(reference),
        Path("attributes.yaml"): render_attributes_index_yaml(occurrences),
        Path(docs_page_path(reference.overview_page)): reference.overview_markdown,
    }
    for model in reference.models:
        docs[Path(data_model_path(model.name))] = render_model_yaml(reference, model)
        docs[Path(docs_page_path(model.page))] = model.markdown
    for name, model_records in occurrences.items():
        docs[Path(data_attribute_path(name))] = render_attribute_yaml(name, model_records)
    return docs


def write_docs(output_dir: Path, docs: dict[Path, str]) -> None:
    shutil.rmtree(output_dir, ignore_errors=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    for relative_path, content in sorted(docs.items()):
        write_file(output_dir / relative_path, content)


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    reference = build_reference(args.version, args.base_url.rstrip("/"))
    docs = build_docs(reference)
    write_docs(output_dir, docs)
    occurrences = attribute_occurrences(reference)
    print(
        f"Generated FortiSIEM Event Data Model skill in {output_dir}: "
        f"{len(reference.models)} models, {len(occurrences)} distinct attributes, "
        f"{attribute_record_count(reference)} attribute records"
    )


if __name__ == "__main__":
    main()
