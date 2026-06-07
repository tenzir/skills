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
import csv
import html
import json
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urldefrag, urljoin, urlparse

import httpx
import yaml


BASE_FIELDS = ("_time", "host", "source", "sourcetype")
SPLUNKBASE_URL = "https://splunkbase.splunk.com/app/1621"
HTTP_HEADERS = {
    "User-Agent": "tenzir-splunk-cim-generator",
}
DOCS_VERSION_RE = re.compile(r"common-information-model/([0-9]+(?:\.[0-9]+)*)(?:/|$)")
IGNORED_DOC_TAGS = {"script", "style", "svg", "button", "details", "textarea"}
IGNORED_DOC_CLASSES = {"code-language-label"}


@dataclass(frozen=True, slots=True)
class DocsPage:
    path: str
    url: str
    title: str
    version: str
    version_id: str
    last_modified: str
    markdown: str
    file: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app-dir", required=True, help="Path to an unpacked Splunk_SA_CIM app directory")
    parser.add_argument("--output-dir", required=True, help="Generated skill output directory")
    parser.add_argument(
        "--docs-url",
        required=True,
        help="Splunk CIM docs page to use as the 8.5 TOC/documentation root",
    )
    return parser.parse_args()


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def to_slug(value: str) -> str:
    value = value.replace("DLP", "Dlp").replace("JVM", "Jvm").replace("DNS", "Dns")
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    return value.strip("_").lower() or "index"


def to_field_slug(value: str) -> str:
    leading_underscores = re.match(r"_+", value)
    prefix = leading_underscores.group(0) if leading_underscores else ""
    return f"{prefix}{to_slug(value)}"


def stable_key(value: str) -> tuple[str, str]:
    return value.casefold(), value


def unique_sorted(values: list[str] | tuple[str, ...]) -> list[str]:
    return sorted({value for value in values if value}, key=stable_key)


def unique_ordered(values: list[str] | tuple[str, ...]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def clean_text(value: object) -> str:
    text = "" if value is None else str(value)
    text = html.unescape(text.replace("\xa0", " "))
    return re.sub(r"\s+", " ", text).strip()


def clean_markdown(text: str) -> str:
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def convert_conf_value(value: str) -> object:
    value = value.strip()
    if value.casefold() == "true":
        return True
    if value.casefold() == "false":
        return False
    if re.fullmatch(r"-?[0-9]+", value):
        return int(value)
    return value


def read_splunk_conf(path: Path) -> dict[str, dict[str, object]]:
    stanzas: dict[str, dict[str, object]] = {}
    current: str | None = None
    if not path.exists():
        return stanzas
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"\[([^\]]+)\]", line)
        if match:
            current = match.group(1).strip()
            stanzas.setdefault(current, {})
            continue
        if current is None or "=" not in line:
            continue
        key, value = line.split("=", 1)
        stanzas[current][key.strip()] = convert_conf_value(value)
    return stanzas


def data_model_path(name: str) -> str:
    return f"data/models/{to_slug(name)}.yaml"


def data_field_path(name: str) -> str:
    return f"data/fields/{to_field_slug(name)}.yaml"


def data_lookup_path(name: str) -> str:
    return f"data/lookups/{to_slug(name)}.yaml"


def docs_page_path(path: str) -> str:
    rel = path.strip("/")
    rel = re.sub(r"^en/", "", rel)
    rel = re.sub(r"^data-management/common-information-model/[0-9.]+/?", "", rel)
    return f"docs/pages/{to_slug(rel or 'index')}.md"


def docs_version_from_url(url: str) -> str:
    match = DOCS_VERSION_RE.search(urlparse(url).path)
    return match.group(1) if match else ""


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


def compact_mapping(items: list[tuple[str, Any]] | tuple[tuple[str, Any], ...]) -> dict[str, Any]:
    return {
        key: value
        for key, value in items
        if value not in (None, "", [], (), {})
    }


def app_version(app_conf: dict[str, dict[str, object]], manifest: dict[str, Any]) -> str:
    launcher = app_conf.get("launcher", {})
    version = launcher.get("version")
    if version:
        return str(version)
    return str(manifest.get("info", {}).get("id", {}).get("version", ""))


def lookup_value(value: object) -> object:
    if value is None:
        return ""
    value = str(value).strip()
    if value.casefold() == "true":
        return True
    if value.casefold() == "false":
        return False
    if value.startswith(("[", "{")):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    return value


def lookup_row(row: dict[str, str]) -> dict[str, object]:
    return {key: lookup_value(value) for key, value in row.items()}


def lookup_values(rows: list[dict[str, str]], field: str) -> list[object]:
    values: list[object] = []
    seen: set[tuple[str, str]] = set()
    for row in rows:
        normalized = lookup_value(row.get(field, ""))
        if normalized == "":
            continue
        key = (type(normalized).__name__, json.dumps(normalized, sort_keys=True))
        if key in seen:
            continue
        seen.add(key)
        values.append(normalized)
    return values


def lookup_data(record: dict[str, Any]) -> dict[str, Any]:
    columns = record["columns"]
    rows = record["rows"]
    if not columns:
        return {
            "name": record["name"],
        }

    if len(columns) == 1 or (len(columns) == 2 and columns[1] == "is_visible"):
        field = columns[0]
        return compact_mapping(
            (
                ("name", record["name"]),
                ("field", field),
                ("values", lookup_values(rows, field)),
            )
        )

    key = columns[0]
    if len(columns) == 2:
        target = columns[1]
        mappings = []
        for row in rows:
            source_value = lookup_value(row.get(key, ""))
            if source_value == "":
                continue
            mappings.append(
                {
                    "from": source_value,
                    "to": lookup_value(row.get(target, "")),
                }
            )
        return compact_mapping(
            (
                ("name", record["name"]),
                ("key", key),
                ("maps_to", target),
                ("mappings", mappings),
            )
        )

    return compact_mapping(
        (
            ("name", record["name"]),
            ("key", key),
            ("fields", columns if not rows else []),
            ("entries", [lookup_row(row) for row in rows if lookup_value(row.get(key, "")) != ""]),
        )
    )


def parse_lookup_files(app_dir: Path) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, str]]]]:
    lookup_records: list[dict[str, Any]] = []
    field_to_lookups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for path in sorted((app_dir / "lookups").glob("*"), key=lambda item: item.name.casefold()):
        if not path.is_file():
            continue
        if not (path.name.endswith(".csv") or path.name.endswith(".csv.default")):
            continue
        lookup_name = path.name
        if lookup_name.endswith(".csv.default"):
            lookup_name = lookup_name[: -len(".csv.default")]
        elif lookup_name.endswith(".csv"):
            lookup_name = lookup_name[: -len(".csv")]
        text = path.read_text(encoding="utf-8")
        rows = list(csv.DictReader(text.splitlines())) if text.strip() else []
        columns = list(rows[0].keys()) if rows else []
        if not columns and text.strip():
            reader = csv.reader(text.splitlines())
            columns = next(reader, [])
        record = {
            "name": lookup_name,
            "file": data_lookup_path(lookup_name),
            "columns": columns,
            "rows": rows,
        }
        lookup_records.append(record)
        for column in columns:
            field_to_lookups[column].append(
                {
                    "name": lookup_name,
                    "file": data_lookup_path(lookup_name),
                }
            )
    return lookup_records, dict(field_to_lookups)


def field_from_json(
    field: dict[str, Any],
    *,
    source: str | None = None,
    calculation: dict[str, Any] | None = None,
    include_name: bool = True,
) -> dict[str, Any]:
    comment = field.get("comment") if isinstance(field.get("comment"), dict) else {}
    name = str(field.get("fieldName") or "")
    display_name = field.get("displayName")
    record = compact_mapping(
        (
            ("name", name if include_name else ""),
            ("display_name", display_name if display_name and display_name != name else ""),
            ("source", source),
            ("type", field.get("type")),
            ("description", clean_text(comment.get("description"))),
            ("expected_values", comment.get("expected_values")),
            ("field_search", field.get("fieldSearch")),
        )
    )
    for key, value in (
        ("required", field.get("required")),
        ("recommended", comment.get("recommended")),
        ("ta_relevant", comment.get("ta_relevant")),
        ("multivalue", field.get("multivalue")),
        ("hidden", field.get("hidden")),
    ):
        if value:
            record[key] = value
    if calculation:
        record["calculation"] = compact_mapping(
            (
                ("id", calculation.get("calculationID")),
                ("type", calculation.get("calculationType")),
                ("expression", calculation.get("expression")),
                ("input_field", calculation.get("inputField")),
            )
        )
    return record


def field_occurrence(
    field: dict[str, Any],
    *,
    model: str,
    dataset: str,
    source: str,
    calculation: dict[str, Any] | None = None,
) -> dict[str, Any]:
    details = field_from_json(field, calculation=calculation)
    name = details.pop("name", "")
    return compact_mapping(
        (
            ("name", name),
            ("model", model),
            ("dataset", dataset),
            ("source", source),
            *details.items(),
        )
    )


def dataset_tags(obj: dict[str, Any]) -> list[str]:
    comment = obj.get("comment") if isinstance(obj.get("comment"), dict) else {}
    tags = comment.get("tags") if isinstance(comment, dict) else None
    return list(tags) if isinstance(tags, list) else []


def dataset_description(obj: dict[str, Any]) -> str:
    comment = obj.get("comment") if isinstance(obj.get("comment"), dict) else {}
    return clean_text(comment.get("description"))


def dataset_kind(name: str, object_by_name: dict[str, dict[str, Any]]) -> str:
    current = object_by_name.get(name)
    seen: set[str] = set()
    while current:
        parent = str(current.get("parentName") or "")
        if parent == "BaseSearch":
            return "search"
        if parent == "BaseEvent":
            return "event"
        if parent in seen:
            break
        seen.add(parent)
        current = object_by_name.get(parent)
    return "dataset"


def parent_chain(name: str, object_by_name: dict[str, dict[str, Any]]) -> list[str]:
    chain: list[str] = []
    current = object_by_name.get(name)
    seen: set[str] = set()
    while current:
        parent = str(current.get("parentName") or "")
        if not parent:
            break
        chain.append(parent)
        if parent in {"BaseEvent", "BaseSearch"}:
            break
        if parent in seen:
            break
        seen.add(parent)
        current = object_by_name.get(parent)
    return list(reversed(chain))


def infer_deprecated(model_name: str, model: dict[str, Any]) -> bool:
    text = " ".join(
        clean_text(value)
        for value in (
            model_name,
            model.get("displayName"),
            model.get("description"),
        )
    )
    return "deprecated" in text.casefold()


def model_data(
    model: dict[str, Any],
    fallback_name: str,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    model_name = str(model.get("modelName") or fallback_name)
    objects = model.get("objects") or []
    object_by_name = {str(obj.get("objectName")): obj for obj in objects}
    children_by_parent: dict[str, list[str]] = defaultdict(list)
    for obj in objects:
        parent = str(obj.get("parentName") or "")
        if parent:
            children_by_parent[parent].append(str(obj.get("objectName")))

    effective_cache: dict[str, dict[str, dict[str, Any]]] = {}
    constraints_cache: dict[str, list[str]] = {}

    def field_record(
        field: dict[str, Any],
        *,
        source: str,
        calculation: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        details = field_from_json(field, calculation=calculation, include_name=False)
        return compact_mapping(
            (
                ("source", source),
                *details.items(),
            )
        )

    def base_fields() -> dict[str, dict[str, Any]]:
        return {
            field_name: {
                "source": "base",
            }
            for field_name in BASE_FIELDS
        }

    def inherited_field(record: dict[str, Any], *, inherited_from: str) -> dict[str, Any]:
        return compact_mapping(
            (
                ("source", "inherited"),
                ("inherited_from", inherited_from),
                *(
                    (key, value)
                    for key, value in record.items()
                    if key not in {"source", "inherited_from"}
                ),
            )
        )

    def effective_fields(object_name: str) -> dict[str, dict[str, Any]]:
        if object_name in effective_cache:
            return effective_cache[object_name]
        obj = object_by_name[object_name]
        parent = str(obj.get("parentName") or "")
        fields: dict[str, dict[str, Any]] = {}
        if parent in object_by_name:
            fields.update(
                {
                    field_name: inherited_field(record, inherited_from=parent)
                    for field_name, record in effective_fields(parent).items()
                }
            )
        elif parent in {"BaseEvent", "BaseSearch"}:
            fields.update(base_fields())
        for field in obj.get("fields") or []:
            field_name = str(field.get("fieldName") or "")
            if not field_name:
                continue
            fields[field_name] = field_record(field, source="declared")
        for calculation in obj.get("calculations") or []:
            for field in calculation.get("outputFields") or []:
                field_name = str(field.get("fieldName") or "")
                if not field_name:
                    continue
                fields[field_name] = field_record(
                    field,
                    source="calculated",
                    calculation=calculation,
                )
        effective_cache[object_name] = {
            field_name: fields[field_name]
            for field_name in sorted(fields, key=stable_key)
        }
        return effective_cache[object_name]

    def local_constraints(object_name: str) -> list[str]:
        obj = object_by_name[object_name]
        return [
            str(item.get("search"))
            for item in obj.get("constraints") or []
            if item.get("search")
        ]

    def effective_constraints(object_name: str) -> list[str]:
        if object_name in constraints_cache:
            return constraints_cache[object_name]
        obj = object_by_name[object_name]
        parent = str(obj.get("parentName") or "")
        constraints: list[str] = []
        if parent in object_by_name:
            constraints.extend(effective_constraints(parent))
        constraints.extend(local_constraints(object_name))
        constraints_cache[object_name] = unique_ordered(constraints)
        return constraints_cache[object_name]

    datasets: dict[str, dict[str, Any]] = {}
    field_occurrences: list[dict[str, Any]] = []
    for obj in objects:
        name = str(obj.get("objectName"))
        kind = dataset_kind(name, object_by_name)
        for field in obj.get("fields") or []:
            field_name = str(field.get("fieldName") or "")
            if not field_name:
                continue
            field_occurrences.append(
                field_occurrence(
                    field,
                    model=model_name,
                    dataset=name,
                    source="declared",
                )
            )

        for calculation in obj.get("calculations") or []:
            for field in calculation.get("outputFields") or []:
                field_name = str(field.get("fieldName") or "")
                if not field_name:
                    continue
                field_occurrences.append(
                    field_occurrence(
                        field,
                        model=model_name,
                        dataset=name,
                        source="calculated",
                        calculation=calculation,
                    )
                )

        display_name = obj.get("displayName")
        datasets[name] = compact_mapping(
            (
                ("display_name", display_name if display_name and display_name != name else ""),
                ("kind", kind),
                ("description", dataset_description(obj)),
                ("tags", dataset_tags(obj)),
                ("constraints", effective_constraints(name)),
                ("fields", effective_fields(name)),
                ("inherits", parent_chain(name, object_by_name)),
                ("children", unique_sorted(children_by_parent.get(name, []))),
                ("search", obj.get("baseSearch")),
            )
        )

    data = compact_mapping(
        (
            ("name", model_name),
            (
                "display_name",
                model.get("displayName") if model.get("displayName") and model.get("displayName") != model_name else "",
            ),
            ("description", clean_text(model.get("description"))),
            ("deprecated", True if infer_deprecated(model_name, model) else None),
            ("root_datasets", [name for name, dataset in datasets.items() if dataset.get("inherits", [None])[-1] in {"BaseEvent", "BaseSearch"}]),
            ("datasets", datasets),
        )
    )
    return data, field_occurrences


class TocLinkParser(HTMLParser):
    def __init__(self, docs_version: str) -> None:
        super().__init__()
        self.docs_version = docs_version
        self.links: list[str] = []
        self.pdf_links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        for attr in ("href", "data-href", "data-nav-href"):
            href = attrs_dict.get(attr)
            if not href:
                continue
            if f"common-information-model/{self.docs_version}" not in href:
                continue
            if href.casefold().endswith(".pdf") or ".pdf?" in href.casefold():
                self.pdf_links.append(href)
            else:
                self.links.append(href)


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: dict[str, str] = {}
        self.in_title = False
        self.title_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "meta":
            name = attrs_dict.get("name") or attrs_dict.get("property")
            content = attrs_dict.get("content")
            if name and content:
                self.meta[name] = content
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self) -> str:
        title = clean_text(" ".join(self.title_parts))
        return title.split(" | ", 1)[0].strip()


class ArticleMarkdownParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.capture = False
        self.article_depth = 0
        self.parts: list[str] = []
        self.heading_level: int | None = None
        self.heading_parts: list[str] = []
        self.in_code = False
        self.in_pre = False
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.table_header_written = False
        self.ignored_depth = 0
        self.cell_parts: list[str] = []
        self.row: list[str] = []

    def append(self, value: str) -> None:
        if self.in_cell:
            self.cell_parts.append(value)
        elif self.heading_level is not None:
            self.heading_parts.append(value)
        else:
            self.parts.append(value)

    def should_ignore(self, tag: str, attrs: dict[str, str | None]) -> bool:
        classes = set((attrs.get("class") or "").split())
        return tag in IGNORED_DOC_TAGS or bool(classes & IGNORED_DOC_CLASSES)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "article" and attrs_dict.get("role") == "article" and not self.capture:
            self.capture = True
            self.article_depth = 1
            return
        if not self.capture:
            return
        if self.ignored_depth:
            self.ignored_depth += 1
            return
        if self.should_ignore(tag, attrs_dict):
            self.ignored_depth = 1
            return
        if tag == "article":
            self.article_depth += 1
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_level = int(tag[1])
            self.heading_parts = []
        elif tag in {"p", "section", "div"}:
            self.parts.append("\n\n")
        elif tag == "br":
            self.append("\n")
        elif tag in {"ul", "ol"}:
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
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
        elif tag == "tr" and self.in_table:
            self.in_row = True
            self.row = []
        elif tag in {"th", "td"} and self.in_table:
            self.in_cell = True
            self.cell_parts = []

    def handle_endtag(self, tag: str) -> None:
        if not self.capture:
            return
        if self.ignored_depth:
            self.ignored_depth -= 1
            return
        if tag == "article":
            self.article_depth -= 1
            if self.article_depth <= 0:
                self.capture = False
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"} and self.heading_level is not None:
            text = clean_text(" ".join(self.heading_parts))
            if text:
                self.parts.append(f"\n\n{'#' * self.heading_level} {text}\n\n")
            self.heading_level = None
            self.heading_parts = []
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
        elif tag == "tr" and self.in_table and self.in_row:
            if self.row:
                escaped = [cell.replace("|", "\\|") for cell in self.row]
                self.parts.append("| " + " | ".join(escaped) + " |\n")
                if not self.table_header_written:
                    self.parts.append("| " + " | ".join("---" for _ in escaped) + " |\n")
                    self.table_header_written = True
            self.in_row = False
            self.row = []
        elif tag == "table" and self.in_table:
            self.in_table = False
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.capture or self.ignored_depth:
            return
        if self.in_pre:
            self.append(data)
            return
        text = clean_text(data)
        if not text:
            return
        self.append(text + " ")

    @property
    def markdown(self) -> str:
        return clean_markdown("".join(self.parts))


def normalize_doc_url(root_url: str, href: str) -> str:
    href, _ = urldefrag(href)
    if href.startswith("data-management/"):
        href = "/en/" + href
    return urljoin(root_url, href)


def is_core_cim_doc(url: str, docs_version: str) -> bool:
    parsed = urlparse(url)
    path = parsed.path
    if f"/common-information-model/{docs_version}/" not in path and not path.endswith(
        f"/common-information-model/{docs_version}"
    ):
        return False
    if "/overview-of-the-ocsf-cim-add-on" in path:
        return False
    if path.endswith(".pdf"):
        return False
    if not path.startswith("/en/"):
        return False
    return True


def fetch_docs(docs_url: str) -> tuple[list[DocsPage], str]:
    docs_version = docs_version_from_url(docs_url)
    with httpx.Client(headers=HTTP_HEADERS, follow_redirects=True, timeout=30.0) as client:
        response = client.get(docs_url)
        response.raise_for_status()
        docs_version = docs_version or docs_version_from_url(str(response.url))
        root_html = response.text
        toc = TocLinkParser(docs_version)
        toc.feed(root_html)
        urls = sorted(
            {
                normalize_doc_url(str(response.url), href)
                for href in toc.links
                if is_core_cim_doc(normalize_doc_url(str(response.url), href), docs_version)
            }
        )
        pdf_urls = sorted({normalize_doc_url(str(response.url), href) for href in toc.pdf_links})
        manual_pdf_url = pdf_urls[0] if pdf_urls else ""

        pages: list[DocsPage] = []
        seen_pages: set[str] = set()
        for url in urls:
            page_response = client.get(url)
            page_response.raise_for_status()
            page_html = page_response.text
            metadata = MetadataParser()
            metadata.feed(page_html)
            article = ArticleMarkdownParser()
            article.feed(page_html)
            title = metadata.title
            if not title:
                title_match = re.search(r"^#\s+(.+)$", article.markdown, flags=re.MULTILINE)
                title = title_match.group(1).strip() if title_match else url
            parsed = urlparse(str(page_response.url))
            path = parsed.path
            page_file = docs_page_path(path)
            if page_file in seen_pages:
                continue
            seen_pages.add(page_file)
            pages.append(
                DocsPage(
                    path=path,
                    url=str(page_response.url),
                    title=title,
                    version=metadata.meta.get("Version_Number", "") or docs_version,
                    version_id=metadata.meta.get("cisco_version_id", ""),
                    last_modified=metadata.meta.get("lastModifiedISO", ""),
                    markdown=article.markdown,
                    file=page_file,
                )
            )
    return pages, manual_pdf_url


def build_skill_markdown(app_version_value: str, docs_version: str) -> str:
    return f"""---
name: tenzir-splunk-cim
description: >-
  Answer questions and produce mappings for the Splunk Common Information Model
  (CIM), including CIM Add-on aliases such as Splunk_SA_CIM, SA-CIM,
  CommonInformationModel, and SA-CommonInformationModel. Use when the user
  mentions CIM data
  models/datamodels/DMs, datasets/data model objects, fields, field aliases,
  calculated/eval fields, tags, constraints, lookups/lookup tables, macros,
  normalization, mapping logs or events to CIM, CIM compliance,
  pytest-splunk-addon, technical add-ons/TAs, Splunk Enterprise Security/ES,
  data model acceleration, pivots, tstats, or datamodel searches.
---

# Splunk Common Information Model

Version: `{app_version_value}`.

The Splunk Common Information Model (CIM) is a normalization model for Splunk
data. CIM is organized around *data models*. Each data model contains
*datasets*, historically called data model objects. Datasets inherit fields and
constraints from parent datasets. Event datasets ultimately inherit from
`BaseEvent`; search datasets inherit from `BaseSearch`. All Splunk data model
datasets can use the base fields `_time`, `host`, `source`, and `sourcetype`.

- *Tags* and constraints decide which events belong in a dataset.
- *Fields* describe the effective normalized shape that searches, dashboards,
  pivots, and downstream apps expect. Each field entry states whether it is
  `base`, `declared`, `calculated`, or `inherited`.
- *Calculated field entries* include a `calculation` block because they create
  or normalize fields at search time.
- *Lookup files* document expected values, translations, and enrichments, such
  as actions, protocols, HTTP statuses, DNS reply codes, endpoint statuses, and
  severities.

## Data files

- Use [data/catalog.yaml](data/catalog.yaml) to choose a data model and find the generated files.
- Use `data/models/<model>.yaml` to inspect datasets, tags, constraints, and the effective `fields` map for one CIM data model.
- Use [data/fields.yaml](data/fields.yaml) to find field-specific files.
- Use `data/fields/<field>.yaml` to inspect lookup links and where a field is declared or calculated across models and datasets.
- Use [data/lookups.yaml](data/lookups.yaml) and `data/lookups/<lookup>.yaml` for lookup-backed values, translations, and enrichments.
- Use [docs/index.yaml](docs/index.yaml) and `docs/pages/*.md` for Splunk CIM {docs_version or "8.5"} prose guidance.
- Use [source.md](source.md) for provenance and generation counts.

## Mapping rules

- Start from the event semantics, choose the closest CIM data model in
  [data/catalog.yaml](data/catalog.yaml), then choose the dataset whose tags and
  constraints match the event.
- Apply all required tags and parent dataset tags implied by the dataset parent chain.
- Populate useful app-documented fields first, especially fields marked
  `recommended` or `required`.
- Treat fields with `source: calculated` or a `calculation` block as
  app-provided normalizations; when mapping a source, still populate the
  underlying source fields needed by those calculations when possible.
- Prefer specific fields such as `src_ip`, `dest_ip`, `user`, `signature`, or
  `vendor_product` over broad fields when the data source provides them.
- Use lookup files to normalize, translate, or enrich values when a lookup
  documents semantics for a field.
- Preserve source-specific details outside CIM fields when the app-derived
  reference has no normalized CIM field.

## Question routing

- Which CIM model should this log map to? [data/catalog.yaml](data/catalog.yaml), then the closest model file.
- What tags or constraints identify a dataset? `data/models/<model>.yaml`.
- What fields does a dataset include? `fields` in `data/models/<model>.yaml`.
- What does field X mean? [data/fields.yaml](data/fields.yaml), then `data/fields/<field>.yaml`.
- What values are expected for a field? Field `expected_values`, then [data/lookups.yaml](data/lookups.yaml).
- What does Splunk say about CIM workflows? [docs/index.yaml](docs/index.yaml).
- What source produced this skill? [source.md](source.md).
"""


def build_source_markdown(
    *,
    app_dir: Path,
    manifest: dict[str, Any],
    app_version_value: str,
    docs_url: str,
    docs_version: str,
    manual_pdf_url: str,
    counts: dict[str, int],
) -> str:
    info = manifest.get("info", {})
    app_id = info.get("id", {})
    return f"""# Source

This skill is generated from the Splunk Common Information Model app and current Splunk CIM docs.
The generated YAML files are the primary agent-facing reference.
Bundled docs are reference-only prose and do not override app-derived YAML.

- **App directory**: `{app_dir}`
- **App name**: `{app_id.get("name", "")}`
- **App version**: `{app_version_value}`
- **App title**: `{info.get("title", "")}`
- **App author**: `{", ".join(author.get("name", "") for author in info.get("author", []) if isinstance(author, dict))}`
- **Splunkbase listing**: {SPLUNKBASE_URL}
- **Docs root**: {docs_url}
- **Docs version**: `{docs_version or "unknown"}`
- **Docs manual PDF**: {manual_pdf_url or "not discovered"}
- **Data precedence**: app-derived YAML is authoritative; docs are bundled for workflow guidance only.

## Generated counts

- **Data model files**: `{counts["models"]}`
- **Datasets**: `{counts["datasets"]}`
- **Root datasets**: `{counts["root_datasets"]}`
- **Distinct fields**: `{counts["distinct_fields"]}`
- **Dataset field entries**: `{counts["field_records"]}`
- **Declared field definitions**: `{counts["declared_field_records"]}`
- **Calculated field definitions**: `{counts["calculated_field_records"]}`
- **Constraints**: `{counts["constraints"]}`
- **Lookup files**: `{counts["lookups"]}`
- **Docs pages**: `{counts["docs_pages"]}`

Raw app source files are not copied wholesale. The generated files preserve the app's data model, lookup, and documentation-relevant metadata in agent-friendly YAML.
"""


def generate(app_dir: Path, output_dir: Path, docs_url: str) -> None:
    manifest = read_json(app_dir / "app.manifest")
    app_conf = read_splunk_conf(app_dir / "default" / "app.conf")
    app_version_value = app_version(app_conf, manifest)

    docs_pages, manual_pdf_url = fetch_docs(docs_url)
    docs_version = next((page.version for page in docs_pages if page.version), "")

    lookup_records, field_to_lookups = parse_lookup_files(app_dir)

    model_records: list[dict[str, Any]] = []
    field_occurrences_by_name: dict[str, list[dict[str, Any]]] = defaultdict(list)
    model_paths = sorted((app_dir / "default" / "data" / "models").glob("*.json"), key=lambda item: item.name.casefold())
    for model_path in model_paths:
        model = read_json(model_path)
        record, occurrences = model_data(model, model_path.stem)
        model_records.append(record)
        for occurrence in occurrences:
            name = occurrence.get("name")
            if name:
                field_occurrences_by_name[str(name)].append(occurrence)

    distinct_fields = sorted(field_occurrences_by_name, key=stable_key)
    field_index = {name: data_field_path(name) for name in distinct_fields}
    docs_index = [
        compact_mapping(
            (
                ("title", page.title),
                ("file", page.file),
                ("url", page.url),
                ("last_modified", page.last_modified),
                ("version", page.version),
            )
        )
        for page in docs_pages
    ]

    counts = {
        "models": len(model_records),
        "datasets": sum(len(model.get("datasets", {})) for model in model_records),
        "root_datasets": sum(len(model.get("root_datasets", [])) for model in model_records),
        "distinct_fields": len(distinct_fields),
        "field_records": sum(
            len(dataset.get("fields", {}))
            for model in model_records
            for dataset in model.get("datasets", {}).values()
        ),
        "declared_field_records": sum(
            1
            for occurrences in field_occurrences_by_name.values()
            for occurrence in occurrences
            if occurrence.get("source") == "declared"
        ),
        "calculated_field_records": sum(
            1
            for occurrences in field_occurrences_by_name.values()
            for occurrence in occurrences
            if occurrence.get("source") == "calculated"
        ),
        "constraints": sum(
            len(dataset.get("constraints", []))
            for model in model_records
            for dataset in model.get("datasets", {}).values()
        ),
        "lookups": len(lookup_records),
        "docs_pages": len(docs_pages),
    }

    staging_dir = output_dir.with_name(f".{output_dir.name}.tmp")
    if staging_dir.exists():
        shutil.rmtree(staging_dir)
    staging_dir.mkdir(parents=True)

    write_file(staging_dir / "SKILL.md", build_skill_markdown(app_version_value, docs_version))
    write_file(
        staging_dir / "source.md",
        build_source_markdown(
            app_dir=app_dir,
            manifest=manifest,
            app_version_value=app_version_value,
            docs_url=docs_url,
            docs_version=docs_version,
            manual_pdf_url=manual_pdf_url,
            counts=counts,
        ),
    )

    catalog = {
        "models": {
            model["name"]: compact_mapping(
                (
                    ("file", data_model_path(model["name"])),
                    ("display_name", model.get("display_name")),
                    ("description", model.get("description")),
                    ("deprecated", True if model.get("deprecated") else None),
                    ("datasets", len(model.get("datasets", {}))),
                    ("root_datasets", model.get("root_datasets")),
                )
            )
            for model in sorted(model_records, key=lambda item: stable_key(item["name"]))
        },
        "base_fields": list(BASE_FIELDS),
        "indexes": {
            "fields": "data/fields.yaml",
            "lookups": "data/lookups.yaml",
            "docs": "docs/index.yaml",
        },
        "source": compact_mapping(
            (
                ("app_name", manifest.get("info", {}).get("id", {}).get("name")),
                ("app_version", app_version_value),
                ("app_title", manifest.get("info", {}).get("title")),
                ("splunkbase_url", SPLUNKBASE_URL),
                ("docs_url", docs_url),
                ("docs_version", docs_version),
                ("manual_pdf_url", manual_pdf_url),
            )
        ),
    }
    write_file(staging_dir / "data" / "catalog.yaml", dump_yaml(catalog))

    for model in model_records:
        write_file(staging_dir / data_model_path(model["name"]), dump_yaml(model))

    write_file(staging_dir / "data" / "fields.yaml", dump_yaml(field_index))
    for field_name in distinct_fields:
        occurrences = field_occurrences_by_name[field_name]
        field_data = compact_mapping(
            (
                ("name", field_name),
                ("lookups", field_to_lookups.get(field_name, [])),
                (
                    "used_by",
                    sorted(
                        [
                            {key: value for key, value in occurrence.items() if key != "name"}
                            for occurrence in occurrences
                        ],
                        key=lambda item: (
                            str(item.get("model", "")).casefold(),
                            str(item.get("dataset", "")).casefold(),
                            str(item.get("source", "")).casefold(),
                        ),
                    ),
                ),
            )
        )
        write_file(staging_dir / data_field_path(field_name), dump_yaml(field_data))

    write_file(
        staging_dir / "data" / "lookups.yaml",
        dump_yaml({record["name"]: record["file"] for record in lookup_records}),
    )
    for record in lookup_records:
        write_file(staging_dir / record["file"], dump_yaml(lookup_data(record)))

    write_file(
        staging_dir / "docs" / "index.yaml",
        dump_yaml(
            {
                "root_url": docs_url,
                "version": docs_version,
                "manual_pdf_url": manual_pdf_url,
                "pages": docs_index,
            }
        ),
    )
    for page in docs_pages:
        header = f"""---
title: {page.title}
url: {page.url}
last_modified: {page.last_modified}
version: {page.version}
---

"""
        write_file(staging_dir / page.file, header + page.markdown)

    if output_dir.exists():
        shutil.rmtree(output_dir)
    staging_dir.rename(output_dir)


def main() -> None:
    args = parse_args()
    generate(Path(args.app_dir).resolve(), Path(args.output_dir), args.docs_url)


if __name__ == "__main__":
    main()
