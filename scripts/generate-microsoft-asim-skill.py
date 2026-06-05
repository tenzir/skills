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
import html
import re
import shutil
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urldefrag

import httpx
import yaml


DEFENDER_DOCS_REPO = "MicrosoftDocs/defender-docs"
GITHUB_API = f"https://api.github.com/repos/{DEFENDER_DOCS_REPO}"
GITHUB_RAW = f"https://raw.githubusercontent.com/{DEFENDER_DOCS_REPO}"
GITHUB_BLOB = f"https://github.com/{DEFENDER_DOCS_REPO}/blob"
SCHEMA_CATALOG_PATH = "sentinel/normalization-about-schemas.md"
SUPPORTING_SOURCE_PATHS = (
    "sentinel/normalization-common-fields.md",
    "sentinel/normalization-content.md",
    "sentinel/normalization-entity-user.md",
    "sentinel/normalization-entity-device.md",
    "sentinel/normalization-entity-application.md",
)
HTTP_HEADERS = {
    "User-Agent": "tenzir-microsoft-asim-generator",
    "Accept": "application/vnd.github+json",
}
FIELD_CLASS_ORDER = {
    "mandatory": 0,
    "recommended": 1,
    "conditional": 2,
    "optional": 3,
    "alias": 4,
}


@dataclass(frozen=True, slots=True)
class SourceRef:
    ref: str
    sha: str


@dataclass(frozen=True, slots=True)
class RawDoc:
    path: str
    text: str


@dataclass(frozen=True, slots=True)
class SchemaCatalogEntry:
    kind: str
    title: str
    name: str
    version: str
    status: str
    path: str
    original_link: str


@dataclass(frozen=True, slots=True)
class FieldRecord:
    name: str
    field_class: str
    field_type: str
    description: str
    aliases: tuple[str, ...]
    examples: tuple[str, ...]
    notes: str
    source_section: str
    source_path: str


@dataclass(frozen=True, slots=True)
class SchemaDoc:
    catalog: SchemaCatalogEntry
    source: RawDoc
    fields: tuple[FieldRecord, ...]
    overview: str

    @property
    def name(self) -> str:
        return self.catalog.name

    @property
    def version(self) -> str:
        return self.catalog.version

    @property
    def status(self) -> str:
        return self.catalog.status

    @property
    def title(self) -> str:
        return self.catalog.title

    @property
    def kind(self) -> str:
        return self.catalog.kind


@dataclass(frozen=True, slots=True)
class AsimReference:
    source: SourceRef
    catalog: RawDoc
    schemas: tuple[SchemaDoc, ...]
    supporting_sources: tuple[RawDoc, ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--docs-ref",
        default=None,
        help="MicrosoftDocs/defender-docs ref to build from (default: public)",
    )
    parser.add_argument(
        "--ref",
        dest="legacy_ref",
        default=None,
        help="Deprecated alias for --docs-ref",
    )
    args = parser.parse_args()
    args.docs_ref = args.docs_ref or args.legacy_ref or "public"
    if args.legacy_ref:
        print("--ref is deprecated; use --docs-ref instead", file=sys.stderr)
    return args


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def resolve_ref(client: httpx.Client, ref: str) -> SourceRef:
    response = client.get(f"{GITHUB_API}/commits/{ref}")
    response.raise_for_status()
    data = response.json()
    sha = data.get("sha")
    if not isinstance(sha, str) or not sha:
        raise RuntimeError(f"GitHub did not return a commit SHA for {ref!r}")
    return SourceRef(ref=ref, sha=sha)


def raw_url(sha: str, path: str) -> str:
    return f"{GITHUB_RAW}/{sha}/{path}"


def blob_url(sha: str, path: str) -> str:
    return f"{GITHUB_BLOB}/{sha}/{path}"


def fetch_doc(client: httpx.Client, source: SourceRef, path: str) -> RawDoc:
    response = client.get(raw_url(source.sha, path))
    response.raise_for_status()
    text = response.text
    return RawDoc(path=path, text=text if text.endswith("\n") else text + "\n")


def source_copy_path(path: str) -> Path:
    return Path("sources") / "defender-docs" / path


def source_copy_link(path: str, *, prefix: str = "") -> str:
    return f"[`{path}`]({prefix}{source_copy_path(path).as_posix()})"


def to_slug(value: str) -> str:
    value = value.replace("ASim", "Asim")
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    return value.strip("_").lower() or "index"


def schema_slug(schema_name: str) -> str:
    return to_slug(schema_name)


def field_slug(field_name: str) -> str:
    return to_slug(field_name)


def schema_link(schema: SchemaDoc, *, prefix: str = "") -> str:
    return f"[{schema.name}]({prefix}schemas/{schema_slug(schema.name)}.md)"


def field_link(name: str, *, prefix: str = "") -> str:
    return f"[`{name}`]({prefix}fields/{field_slug(name)}.md)"


def clean_markdown(text: str) -> str:
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def escape_table(value: object) -> str:
    text = str(value).replace("\n", "<br>")
    return text.replace("|", "\\|")


def inline_code(value: object) -> str:
    text = str(value).strip()
    return f"`{text}`" if text else ""


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\xa0", " ")).strip()


def strip_markdown(value: str) -> str:
    text = value.replace("\xa0", " ")
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"</?a\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</?[^>]+>", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("__", "").replace("*", "")
    text = text.replace("`", "")
    return normalize_space(html.unescape(text))


def clean_cell_markdown(value: str) -> str:
    text = value.replace("\xa0", " ")
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</?a\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return html.unescape(text).strip()


def summarize_markdown(value: str, *, limit: int = 260) -> str:
    text = strip_markdown(value)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def split_table_row(row: str) -> list[str]:
    row = row.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in row:
        if char == "|" and not escaped:
            cells.append("".join(current).strip())
            current = []
            continue
        current.append(char)
        escaped = char == "\\" and not escaped
        if char != "\\":
            escaped = False
    cells.append("".join(current).strip())
    return cells


def is_separator_row(row: str) -> bool:
    cells = split_table_row(row)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def iter_tables(text: str) -> Iterable[tuple[list[str], list[list[str]], str]]:
    lines = text.splitlines()
    headings: dict[int, str] = {}
    index = 0
    while index < len(lines):
        line = lines[index]
        heading_match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading_match:
            level = len(heading_match.group(1))
            title = strip_markdown(heading_match.group(2))
            headings = {key: value for key, value in headings.items() if key < level}
            headings[level] = title
            index += 1
            continue
        if (
            line.lstrip().startswith("|")
            and index + 1 < len(lines)
            and lines[index + 1].lstrip().startswith("|")
            and is_separator_row(lines[index + 1])
        ):
            header = split_table_row(line)
            rows: list[list[str]] = []
            index += 2
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                row = split_table_row(lines[index])
                if len(row) < len(header):
                    row.extend([""] * (len(header) - len(row)))
                rows.append(row[: len(header)])
                index += 1
            section = " > ".join(headings[level] for level in sorted(headings) if level >= 2)
            yield header, rows, section
            continue
        index += 1


def normalize_header(header: str) -> str:
    return strip_markdown(header).casefold().replace(" ", "_")


def extract_first_link(value: str) -> tuple[str, str] | None:
    match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", value)
    if not match:
        return None
    return strip_markdown(match.group(1)), match.group(2).strip()


def resolve_sentinel_path(href: str) -> str:
    href, _ = urldefrag(href)
    if href == "normalization-schema.md":
        href = "normalization-schema-network.md"
    if href.startswith("sentinel/"):
        return href
    return f"sentinel/{href}"


def parse_schema_catalog(catalog: RawDoc) -> tuple[SchemaCatalogEntry, ...]:
    entries: list[SchemaCatalogEntry] = []
    for header, rows, section in iter_tables(catalog.text):
        normalized = [normalize_header(cell) for cell in header]
        if normalized[:4] != ["schema", "schema_name_for_tests", "version", "status"]:
            continue
        kind = "entity" if "Entity Schemas" in section else "event"
        for row in rows:
            link = extract_first_link(row[0])
            if link is None:
                continue
            title, href = link
            name = strip_markdown(row[1])
            version = strip_markdown(row[2])
            status = strip_markdown(row[3])
            if not name:
                continue
            entries.append(
                SchemaCatalogEntry(
                    kind=kind,
                    title=title,
                    name=name,
                    version=version,
                    status=status,
                    path=resolve_sentinel_path(href),
                    original_link=href,
                )
            )
    if not entries:
        raise RuntimeError(f"No schema entries found in {catalog.path}")
    return tuple(entries)


def extract_field_names(cell: str) -> tuple[str, ...]:
    candidates = re.findall(r"\*\*([^*]+?)\*\*", cell)
    if not candidates:
        candidates = re.findall(r"`([A-Za-z][A-Za-z0-9]+)`", cell)
    if not candidates:
        candidates = re.findall(r"\[([A-Za-z][A-Za-z0-9]+)\]\([^)]+\)", cell)
    if not candidates:
        text = strip_markdown(cell)
        candidates = [text] if text else []
    names: list[str] = []
    for candidate in candidates:
        for part in re.split(r"\s*,\s*", strip_markdown(candidate)):
            part = re.sub(r"\s+fields?$", "", part, flags=re.IGNORECASE)
            part = part.strip(" .:")
            if re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", part) and part not in names:
                names.append(part)
    return tuple(names)


def extract_linked_field_names(cell: str) -> tuple[str, ...]:
    names: list[str] = []
    for match in re.finditer(r"\[([A-Za-z][A-Za-z0-9]+)\]\([^)]+\)", cell):
        name = strip_markdown(match.group(1))
        if name not in names:
            names.append(name)
    if not names:
        names.extend(extract_field_names(cell))
    return tuple(names)


def infer_alias_targets(description: str, own_name: str) -> tuple[str, ...]:
    text = description.replace("\n", " ")
    if "alias" not in text.casefold():
        return ()
    names: list[str] = []
    for match in re.finditer(
        r"(?:alias(?:es|ed)?|alias to|should alias|can alias|might alias)"
        r"(?:\s+(?:to|the|either))*\s+(.+?)"
        r"(?:\s+fields?|\s+field|, which|, depending|\s+when|\s+if|\s+where|\s+Supported|\s+Used|\.|;|\s+Example[s]?\s*:|$)",
        text,
        re.IGNORECASE,
    ):
        segment = match.group(1)
        segment_names: list[str] = []
        for pattern in (
            r"\[([A-Za-z][A-Za-z0-9]+)\]\([^)]+\)",
            r"`([A-Za-z][A-Za-z0-9]+)`",
        ):
            for candidate in re.findall(pattern, segment):
                name = strip_markdown(candidate)
                if name == own_name:
                    continue
                if name in {"Alias", "String", "ASIM", "KQL"}:
                    continue
                if name not in names and name not in segment_names:
                    segment_names.append(name)
        if not segment_names:
            candidates = re.findall(r"\b([A-Z][A-Za-z0-9]+)\b", strip_markdown(segment))
            has_list_separator = bool(re.search(r"[,/]|\s+or\s+|\s+and\s+|\s+either\s+", segment, re.IGNORECASE))
            if len(candidates) == 1 or has_list_separator:
                for candidate in candidates:
                    name = strip_markdown(candidate)
                    if name == own_name:
                        continue
                    if name in {"Alias", "String", "ASIM", "KQL"}:
                        continue
                    if name not in names and name not in segment_names:
                        segment_names.append(name)
        for name in segment_names:
            if name not in names:
                names.append(name)
    return tuple(names)


def extract_examples(description: str) -> tuple[str, ...]:
    examples: list[str] = []
    for match in re.finditer(r"Example[s]?\s*:\s*(.+?)(?:\n|$)", description, re.IGNORECASE):
        segment = match.group(1).strip()
        ticked = re.findall(r"`([^`]+)`", segment)
        if ticked:
            for value in ticked:
                if value not in examples:
                    examples.append(value)
        else:
            text = strip_markdown(segment).strip()
            if text and text not in examples:
                examples.append(text)
    return tuple(examples)


def extract_notes(description: str) -> str:
    note_match = re.search(r"\*\*Notes?\*\*:?\s*(.+)", description, re.IGNORECASE | re.DOTALL)
    if note_match:
        return note_match.group(1).strip()
    return ""


def remove_notes(description: str) -> str:
    return re.split(r"\*\*Notes?\*\*:?", description, maxsplit=1, flags=re.IGNORECASE)[0].strip()


def truncate_at_sentence(value: str, *, limit: int) -> str:
    if len(value) <= limit:
        return value
    candidate = value[:limit].rstrip()
    sentence_end = max(candidate.rfind("."), candidate.rfind("!"), candidate.rfind("?"))
    if sentence_end >= limit // 2:
        return candidate[: sentence_end + 1]
    word_end = candidate.rfind(" ")
    if word_end >= limit // 2:
        return candidate[:word_end].rstrip() + "..."
    return candidate + "..."


def parse_field_table(header: list[str], rows: list[list[str]], section: str, source_path: str) -> list[FieldRecord]:
    normalized = [normalize_header(cell) for cell in header]
    column = {name: index for index, name in enumerate(normalized)}
    if "field" not in column or "class" not in column:
        return []
    description_column = column.get("description", column.get("notes"))
    if description_column is None and "type" not in column:
        return []
    records: list[FieldRecord] = []
    for row in rows:
        names = extract_field_names(row[column["field"]])
        field_class = strip_markdown(row[column["class"]])
        field_type = strip_markdown(row[column["type"]]) if "type" in column else ""
        description = clean_cell_markdown(row[description_column]) if description_column is not None else ""
        notes = extract_notes(description)
        display_description = remove_notes(description) if notes else description
        for name in names:
            records.append(
                FieldRecord(
                    name=name,
                    field_class=field_class,
                    field_type=field_type,
                    description=display_description,
                    aliases=infer_alias_targets(description, name),
                    examples=extract_examples(description),
                    notes=notes,
                    source_section=section,
                    source_path=source_path,
                )
            )
    return records


def parse_common_field_table(header: list[str], rows: list[list[str]], section: str, source_path: str) -> list[FieldRecord]:
    normalized = [normalize_header(cell) for cell in header]
    column = {name: index for index, name in enumerate(normalized)}
    if "class" not in column or "fields" not in column:
        return []
    records: list[FieldRecord] = []
    for row in rows:
        field_class = strip_markdown(row[column["class"]])
        article = "an" if field_class[:1].casefold() in {"a", "e", "i", "o", "u"} else "a"
        for name in extract_linked_field_names(row[column["fields"]]):
            records.append(
                FieldRecord(
                    name=name,
                    field_class=field_class,
                    field_type="",
                    description=f"Listed as {article} {field_class.lower()} common ASIM field for this schema.",
                    aliases=(),
                    examples=(),
                    notes="",
                    source_section=section,
                    source_path=source_path,
                )
            )
    return records


def parse_fields(source: RawDoc) -> tuple[FieldRecord, ...]:
    records: list[FieldRecord] = []
    for header, rows, section in iter_tables(source.text):
        normalized = [normalize_header(cell) for cell in header]
        if "field" in normalized and "class" in normalized:
            records.extend(parse_field_table(header, rows, section, source.path))
        elif "class" in normalized and "fields" in normalized:
            records.extend(parse_common_field_table(header, rows, section, source.path))
    return tuple(sorted(records, key=lambda item: (item.name.casefold(), item.source_section.casefold())))


def extract_overview(source: RawDoc) -> str:
    lines = source.text.splitlines()
    if lines and lines[0].strip() == "---":
        try:
            lines = lines[lines.index("---", 1) + 1 :]
        except ValueError:
            pass
    paragraphs: list[str] = []
    current: list[str] = []
    for line in lines:
        if line.strip() == "---":
            continue
        if line.startswith("#Customer intent:"):
            continue
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            break
        if not line.strip():
            if current:
                paragraphs.append(normalize_space(" ".join(current)))
                current = []
            continue
        if line.startswith((">", "|", ":::")):
            continue
        current.append(strip_markdown(line))
    if current:
        paragraphs.append(normalize_space(" ".join(current)))
    return truncate_at_sentence("\n\n".join(paragraph for paragraph in paragraphs if paragraph), limit=1200)


def build_reference(
    source: SourceRef,
    catalog: RawDoc,
    schema_sources: dict[str, RawDoc],
    supporting_sources: tuple[RawDoc, ...],
) -> AsimReference:
    catalog_entries = parse_schema_catalog(catalog)
    schemas = tuple(
        SchemaDoc(
            catalog=entry,
            source=schema_sources[entry.path],
            fields=parse_fields(schema_sources[entry.path]),
            overview=extract_overview(schema_sources[entry.path]),
        )
        for entry in catalog_entries
    )
    return AsimReference(
        source=source,
        catalog=catalog,
        schemas=schemas,
        supporting_sources=supporting_sources,
    )


def field_occurrences(reference: AsimReference) -> dict[str, list[tuple[SchemaDoc, FieldRecord]]]:
    occurrences: dict[str, list[tuple[SchemaDoc, FieldRecord]]] = defaultdict(list)
    for schema in reference.schemas:
        for record in schema_field_records(schema):
            occurrences[record.name].append((schema, record))
    return dict(occurrences)


def distinct_schema_fields(schema: SchemaDoc) -> set[str]:
    return {field.name for field in schema_field_records(schema)}


def distinct_field_names(reference: AsimReference) -> set[str]:
    return {field.name for schema in reference.schemas for field in schema_field_records(schema)}


def alias_count(reference: AsimReference) -> int:
    return schema_alias_count(reference)


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


def data_schema_path(schema_name: str) -> str:
    return f"data/schemas/{schema_slug(schema_name)}.yaml"


def data_field_path(field_name: str) -> str:
    return f"data/fields/{field_slug(field_name)}.yaml"


def data_schema_link(schema: SchemaDoc) -> str:
    return f"[{schema.name}]({data_schema_path(schema.name)})"


def clean_data_text(value: str) -> str:
    return strip_markdown(value)


def clean_description_text(record: FieldRecord) -> str:
    description = record.description
    if record.examples:
        description = re.sub(r"\s*Example[s]?\s*:\s*.+?(?=\n|$)", "", description, flags=re.IGNORECASE)
    description = clean_data_text(description)
    if is_generic_common_description(description):
        return ""
    return description


def clean_notes_text(value: str) -> str:
    value = re.sub(r"\s*Example[s]?\s*:\s*.+?(?=\n|$)", "", value, flags=re.IGNORECASE)
    return clean_data_text(value)


def is_generic_common_description(description: str) -> bool:
    return bool(re.match(r"listed as an? .+ common asim field for this schema\.?$", description, re.IGNORECASE))


def first_unique(values: Iterable[str]) -> list[str]:
    unique: list[str] = []
    for value in values:
        value = value.strip()
        if value and value not in unique:
            unique.append(value)
    return unique


def strongest_field_class(records: Iterable[FieldRecord]) -> str:
    classes = [record.field_class for record in records if record.field_class]
    if not classes:
        return ""
    return min(classes, key=lambda item: (FIELD_CLASS_ORDER.get(item.casefold(), 99), item.casefold()))


def field_quality_key(record: FieldRecord) -> tuple[int, int, int, int, int]:
    description = clean_description_text(record)
    return (
        0 if description else 1,
        0 if record.field_type else 1,
        -len(record.aliases),
        -len(record.examples),
        -len(description),
    )


def merge_field_records(records: Iterable[FieldRecord]) -> FieldRecord:
    records = tuple(records)
    if not records:
        raise ValueError("cannot merge an empty field record set")
    preferred = min(records, key=field_quality_key)
    description_record = next((record for record in records if clean_description_text(record)), preferred)
    description = description_record.description if clean_description_text(description_record) else ""
    notes = "\n\n".join(first_unique(clean_notes_text(record.notes) for record in records if record.notes))
    aliases = tuple(sorted({alias for record in records for alias in record.aliases}, key=str.casefold))
    examples = tuple(first_unique(example for record in records for example in record.examples))
    field_type = description_record.field_type or next((record.field_type for record in records if record.field_type), preferred.field_type)
    return FieldRecord(
        name=preferred.name,
        field_class=strongest_field_class(records),
        field_type=field_type,
        description=description,
        aliases=aliases,
        examples=examples,
        notes=notes,
        source_section="",
        source_path=preferred.source_path,
    )


def schema_field_records(schema: SchemaDoc) -> tuple[FieldRecord, ...]:
    grouped: dict[str, list[FieldRecord]] = defaultdict(list)
    for record in schema.fields:
        grouped[record.name].append(record)
    return tuple(
        sorted(
            (merge_field_records(records) for records in grouped.values()),
            key=class_sort_key,
        )
    )


def generated_schema_field_count(reference: AsimReference) -> int:
    return sum(len(schema_field_records(schema)) for schema in reference.schemas)


def schema_alias_count(reference: AsimReference) -> int:
    return sum(
        1
        for schema in reference.schemas
        for record in schema_field_records(schema)
        if record.field_class.casefold() == "alias"
    )


def infer_field_role(name: str) -> str:
    role_prefixes = (
        ("Actor", "actor"),
        ("Acting", "acting"),
        ("Target", "target"),
        ("Src", "source"),
        ("Dst", "destination"),
        ("Dvc", "device"),
        ("Dns", "dns"),
        ("Dhcp", "dhcp"),
        ("Http", "http"),
        ("Url", "web"),
        ("Network", "network"),
        ("Tcp", "network"),
        ("Registry", "registry"),
        ("Threat", "threat"),
        ("Attack", "threat"),
        ("Alert", "alert"),
        ("Asset", "asset"),
        ("Entity", "entity"),
        ("Event", "common"),
        ("ASim", "common"),
        ("AAD", "entity"),
        ("Identity", "entity"),
        ("User", "user"),
        ("Group", "group"),
        ("Rule", "rule"),
        ("Tool", "tool"),
        ("Platform", "platform"),
        ("Model", "model"),
        ("Input", "model"),
        ("Output", "model"),
    )
    special_roles = {
        "AdditionalFields": "common",
        "Application": "application",
        "CommandLine": "process",
        "Domain": "dns",
        "DomainCategory": "dns",
        "Duration": "network",
        "FileName": "file",
        "FilePath": "file",
        "Hash": "file",
        "Hostname": "device",
        "InnerVlanId": "network",
        "IpAddr": "network",
        "LogonTarget": "target",
        "Object": "object",
        "ObjectType": "object",
        "OuterVlanId": "network",
        "Process": "process",
        "SessionId": "session",
        "UpdatedPropertyName": "object",
        "Username": "user",
        "ValueType": "object",
    }
    if name in special_roles:
        return special_roles[name]
    for prefix, role in role_prefixes:
        if name.startswith(prefix):
            return role
    if "File" in name or name.endswith(("MD5", "SHA1", "SHA256", "SHA512", "IMPHASH")):
        return "file"
    if "Process" in name:
        return "process"
    return ""


def extract_documented_value(record: FieldRecord, schema: SchemaDoc) -> str:
    if record.name in {"EventSchema", "EntitySchema"}:
        text = clean_description_text(record)
        match = re.search(r"schema documented here is\s+[`'\"]?([A-Za-z][A-Za-z0-9]*)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip(" .")
        return schema.name
    if record.name in {"EventSchemaVersion", "EntitySchemaVersion"}:
        text = clean_description_text(record)
        match = re.search(r"schema documented here is\s+[`'\"]?([0-9][0-9A-Za-z_.-]*)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip(" .")
        return schema.version
    return ""


def extract_required_if(description: str) -> list[str]:
    text = clean_data_text(description)
    conditions: list[str] = []
    for match in re.finditer(
        r"(?:this\s+(?:field|value)\s+is\s+)?(?:required|mandatory)\s+if\s+(.+?)(?:\.|$)",
        text,
        re.IGNORECASE,
    ):
        condition = normalize_space(match.group(1))
        condition = condition.strip(" .")
        if condition and condition not in conditions:
            conditions.append(condition)
    return conditions


def extract_bullet_value(line: str) -> str:
    value = re.sub(r"^\s*[-*]\s*", "", line).strip()
    value = strip_markdown(value).strip(" .")
    if not value:
        return ""
    if " - " in value:
        left, right = value.split(" - ", 1)
        if left and right:
            return f"{left.strip()}: {right.strip()}"
    if ":" in value:
        left, _ = value.split(":", 1)
        return left.strip()
    return value


def extract_inline_values(segment: str) -> list[str]:
    ticked = first_unique(re.findall(r"`([^`]+)`", segment))
    if ticked:
        return ticked
    text = strip_markdown(segment)
    text = re.sub(r"^(?:are|include|includes|:)\s*", "", text, flags=re.IGNORECASE).strip(" .")
    text = re.sub(r"\s+(?:or|and)\s+", ", ", text, flags=re.IGNORECASE)
    values = [value.strip(" .") for value in text.split(",")]
    return [value for value in values if value and len(value) <= 80]


def extract_allowed_values(description: str) -> list[str]:
    if not description:
        return []
    trigger = re.compile(
        r"(?:"
        r"(?:allowed|supported|possible)(?:\s+and\s+supported)?\s+values?\s+(?:are|include|includes)"
        r"|support(?:ed)?\s+sources\s+include"
        r"|the\s+value\s+is\s+either"
        r")",
        re.IGNORECASE,
    )
    values: list[str] = []
    lines = description.splitlines()
    for index, line in enumerate(lines):
        match = trigger.search(line)
        if not match:
            continue
        tail = line[match.end() :].strip()
        if tail and tail not in {":", "."}:
            values.extend(extract_inline_values(tail))
        started = False
        for candidate in lines[index + 1 :]:
            stripped = candidate.strip()
            if not stripped:
                if started:
                    break
                continue
            if not stripped.startswith(("-", "*")):
                if started:
                    break
                continue
            started = True
            bullet = extract_bullet_value(stripped)
            if bullet:
                values.append(bullet)
    if not values:
        text = description.replace("\n", " ")
        match = trigger.search(text)
        if match:
            values.extend(extract_inline_values(text[match.end() :].split(".", 1)[0]))
    return first_unique(values)


def simple_alias_description(description: str, targets: Iterable[str]) -> bool:
    targets = list(targets)
    if not description or not targets:
        return False
    description_lower = description.casefold()
    if any(word in description_lower for word in (" if ", " depending ", " might ", " either the value ", " in many cases ")):
        return False
    if not all(target.casefold() in description_lower for target in targets):
        return False
    return bool(
        re.match(
            r"^(?:the\s+)?alias(?:es)?\s+(?:to|for)\b|^alias\s+or\s+friendly\s+name\s+for\b",
            description,
            re.IGNORECASE,
        )
    )


def record_semantic_text(record: FieldRecord) -> str:
    return "\n\n".join(part for part in (record.description, record.notes) if part)


def field_record_data(record: FieldRecord, *, schema: SchemaDoc | None, include_name: bool) -> dict[str, Any]:
    description = clean_description_text(record)
    aliases = list(record.aliases)
    is_alias = record.field_class.casefold() == "alias"
    role = infer_field_role(record.name)
    documented_value = extract_documented_value(record, schema) if schema else ""
    semantic_text = record_semantic_text(record)
    required_if = extract_required_if(semantic_text)
    allowed_values = extract_allowed_values(semantic_text)
    if is_alias:
        description_field = ""
        resolution = description if not simple_alias_description(description, aliases) else ""
    else:
        description_field = description
        resolution = ""
    return compact_mapping(
        (
            ("name", record.name if include_name else ""),
            ("role", role),
            ("class", record.field_class),
            ("type", record.field_type),
            ("value", documented_value),
            ("to", aliases),
            ("required_if", required_if),
            ("allowed_values", allowed_values),
            ("resolution", resolution),
            ("description", description_field),
            ("examples", list(record.examples)),
            ("notes", clean_notes_text(record.notes)),
        )
    )


def field_summary(name: str, occurrences: list[tuple[SchemaDoc, FieldRecord]]) -> str:
    aliases = sorted({alias for _, record in occurrences for alias in record.aliases}, key=str.casefold)
    if aliases and all(record.field_class.casefold() == "alias" for _, record in occurrences):
        return f"{name} is an alias for {', '.join(aliases)}."
    for _, record in occurrences:
        description = clean_description_text(record)
        if not description:
            continue
        if re.match(r"listed as an? .+ common asim field", description, re.IGNORECASE):
            continue
        return description
    return ""


def render_catalog_yaml(reference: AsimReference) -> str:
    data = {
        "schemas": {
            schema.name: {
                "file": data_schema_path(schema.name),
                "kind": schema.kind,
                "title": schema.title,
                "version": schema.version,
                "status": schema.status,
            }
            for schema in sorted(reference.schemas, key=lambda item: (item.kind, item.name.casefold()))
        },
        "indexes": {
            "fields": "data/fields.yaml",
            "aliases": "data/aliases.yaml",
        },
    }
    return dump_yaml(data)


def render_schema_yaml(schema: SchemaDoc) -> str:
    data = compact_mapping(
        (
            ("name", schema.name),
            ("title", schema.title),
            ("kind", schema.kind),
            ("version", schema.version),
            ("status", schema.status),
            ("summary", clean_data_text(schema.overview)),
            ("fields", [field_record_data(record, schema=schema, include_name=True) for record in schema_field_records(schema)]),
        )
    )
    return dump_yaml(data)


def render_fields_index_yaml(reference: AsimReference) -> str:
    occurrences = field_occurrences(reference)
    return dump_yaml({name: data_field_path(name) for name in sorted(occurrences, key=str.casefold)})


def render_field_yaml(name: str, occurrences: list[tuple[SchemaDoc, FieldRecord]]) -> str:
    aliases = sorted({alias for _, record in occurrences for alias in record.aliases}, key=str.casefold)
    data = compact_mapping(
        (
            ("name", name),
            ("summary", field_summary(name, occurrences)),
            ("to", aliases),
            (
                "schemas",
                [
                    {"name": schema.name} | field_record_data(record, schema=schema, include_name=False)
                    for schema, record in sorted(
                        occurrences,
                        key=lambda item: (
                            item[0].name.casefold(),
                            FIELD_CLASS_ORDER.get(item[1].field_class.casefold(), 99),
                        ),
                    )
                ],
            ),
        )
    )
    return dump_yaml(data)


def render_aliases_yaml(reference: AsimReference) -> str:
    grouped: dict[str, list[tuple[SchemaDoc, FieldRecord]]] = defaultdict(list)
    for schema in reference.schemas:
        for record in schema_field_records(schema):
            if record.field_class.casefold() == "alias":
                grouped[record.name].append((schema, record))
    aliases: dict[str, Any] = {}
    for name in sorted(grouped, key=str.casefold):
        records = grouped[name]
        aliases_to = sorted({alias for _, record in records for alias in record.aliases}, key=str.casefold)
        resolution = []
        for schema, record in records:
            description = clean_description_text(record)
            if description and not simple_alias_description(description, record.aliases):
                resolution.append(
                    compact_mapping(
                        (
                            ("schema", schema.name),
                            ("rule", description),
                        )
                    )
                )
        aliases[name] = compact_mapping(
            (
                ("to", aliases_to),
                ("schemas", sorted({schema.name for schema, _ in records}, key=str.casefold)),
                ("resolution", resolution),
            )
        )
    return dump_yaml({"aliases": aliases})


def render_skill_markdown(reference: AsimReference) -> str:
    return clean_markdown(
        "\n".join(
            [
                "---",
                "name: tenzir-microsoft-asim",
                "description: Answer questions about Microsoft Sentinel ASIM (Advanced Security Information Model). Use whenever the user asks about ASIM schemas, normalized Microsoft Sentinel fields, field classes, aliases, schema mapping, or mapping events and entities into ASIM.",
                "---",
                "",
                "# Microsoft Sentinel ASIM",
                "",
                "Use this generated reference to answer Microsoft Sentinel ASIM schema and mapping questions.",
                "The data files are optimized for agent context: load the smallest YAML file that answers the question, then follow cross-references only when needed.",
                "",
                "Do not invent fields, aliases, enum values, schema versions, or schema behavior that is not present in the generated YAML data.",
                "",
                "## Data files",
                "",
                "- Use [data/catalog.yaml](data/catalog.yaml) to choose a schema and find the schema data file.",
                "- Use `data/schemas/<schema>.yaml` to map telemetry into one ASIM schema.",
                "- Use [data/fields.yaml](data/fields.yaml) directly as the field-name to field-file manifest.",
                "- Use `data/fields/<field>.yaml` for field meaning across schemas.",
                "- Use [data/aliases.yaml](data/aliases.yaml) to resolve alias fields and conditional alias rules.",
                "",
                "## Mapping rules",
                "",
                "- Start from activity or entity semantics, choose the ASIM schema in [data/catalog.yaml](data/catalog.yaml), then load the schema file.",
                "- Populate `Mandatory` and useful `Recommended` fields first, then add `Optional` fields when the source provides useful context.",
                "- Populate `Conditional` fields when the field record's `required_if` condition applies.",
                "- Prefer canonical normalized fields over aliases for reusable detections, analytics rules, workbooks, and mappings.",
                "- Use aliases to explain Microsoft-documented query convenience, but resolve them through [data/aliases.yaml](data/aliases.yaml) before mapping.",
                "- Preserve source-specific values in original fields or `AdditionalFields` when ASIM has no direct normalized field.",
                "- When a schema defines both a value field and a type field, populate the type field when the identifier format is known.",
                "- Treat fields with `role: common` as shared event/entity metadata, but obey schema-specific `value`, `allowed_values`, and `required_if` records.",
                "",
                "## Field classes",
                "",
                "| Class | Meaning |",
                "| --- | --- |",
                "| `Mandatory` | Populate for normalized records of that schema. |",
                "| `Recommended` | Populate when the source provides enough information because it improves analytic value. |",
                "| `Conditional` | Populate when the field record's condition applies. |",
                "| `Optional` | Populate for useful context when the source provides it. |",
                "| `Alias` | Query convenience field; prefer canonical target fields for reusable content. |",
                "",
                "## Role prefixes",
                "",
                "| Prefix | Role |",
                "| --- | --- |",
                "| `Src` | Source system, identity, or application initiating the activity. |",
                "| `Dst` | Destination system, identity, or application targeted by the activity. |",
                "| `Actor` | User or identity performing the operation. |",
                "| `Target` | User, system, object, or application affected by the operation. |",
                "| `Acting` | Process or application acting on behalf of an actor. |",
                "| `Dvc` | Reporting device or collector unless the selected schema defines a more specific role. |",
                "",
                "## Question routing",
                "",
                "| Question pattern | Start here |",
                "| --- | --- |",
                "| Which ASIM schema should I map this event or entity to? | [data/catalog.yaml](data/catalog.yaml), then the selected schema file |",
                "| What fields does schema X contain? | `data/schemas/<schema>.yaml` |",
                "| What does field X mean? | [data/fields.yaml](data/fields.yaml), then `data/fields/<field>.yaml` |",
                "| Which field should an alias use? | [data/aliases.yaml](data/aliases.yaml), then target field files |",
                "| How do user/device/application roles map? | Role-prefix table above, then the selected schema file |",
                "| What raw Microsoft source backs this data? | [source.md](source.md) |",
                "",
                "For provenance, the pinned Microsoft Defender Docs commit, and raw source copies, use [source.md](source.md) as the last anchor.",
                "",
            ]
        )
    )


def render_source_page(reference: AsimReference) -> str:
    event_schema_count = sum(1 for schema in reference.schemas if schema.kind == "event")
    entity_schema_count = sum(1 for schema in reference.schemas if schema.kind == "entity")
    field_count = generated_schema_field_count(reference)
    distinct_count = len(distinct_field_names(reference))
    lines = [
        "# Source",
        "",
        "This skill is generated from Microsoft Defender Docs Markdown. The generated YAML files are the primary agent-facing reference; use this page only when provenance or raw source lookup is needed.",
        "",
        f"- **Requested docs ref**: `{reference.source.ref}`",
        f"- **Resolved Defender Docs commit**: `{reference.source.sha}`",
        f"- **Schema catalog source path**: {source_copy_link(reference.catalog.path)} ([upstream]({blob_url(reference.source.sha, reference.catalog.path)}))",
        f"- **Event schemas**: `{event_schema_count}`",
        f"- **Entity schemas**: `{entity_schema_count}`",
        f"- **Generated schemas**: `{len(reference.schemas)}`",
        f"- **Generated distinct fields**: `{distinct_count}`",
        f"- **Generated schema field records**: `{field_count}`",
        f"- **Alias field records**: `{alias_count(reference)}`",
        "",
        "Raw Markdown source files are copied under `sources/defender-docs/sentinel/` for audit and parser debugging.",
        "",
        "## Schema source paths",
        "",
    ]
    for schema in sorted(reference.schemas, key=lambda item: (item.kind, item.name.casefold())):
        lines.append(
            f"- {data_schema_link(schema)}: {source_copy_link(schema.source.path)} "
            f"([upstream]({blob_url(reference.source.sha, schema.source.path)}))"
        )
    lines.extend(["", "## Supporting source paths", ""])
    lines.append(f"- {source_copy_link(reference.catalog.path)} ([upstream]({blob_url(reference.source.sha, reference.catalog.path)}))")
    for source in sorted(reference.supporting_sources, key=lambda item: item.path):
        lines.append(f"- {source_copy_link(source.path)} ([upstream]({blob_url(reference.source.sha, source.path)}))")
    return clean_markdown("\n".join(lines))


def render_schemas_index(reference: AsimReference) -> str:
    lines = [
        "# Schemas",
        "",
        "Schemas are generated from the event and entity schema tables in the Microsoft Defender Docs ASIM schema catalog.",
        "",
    ]
    for kind, title in (("event", "Event Schemas"), ("entity", "Entity Schemas")):
        schemas = [schema for schema in reference.schemas if schema.kind == kind]
        if not schemas:
            continue
        lines.extend([f"## {title}", ""])
        lines.append("| Schema | Catalog title | Version | Status | Fields | Source |")
        lines.append("| --- | --- | --- | --- | ---: | --- |")
        for schema in sorted(schemas, key=lambda item: item.name.casefold()):
            lines.append(
                "| "
                f"{schema_link(schema)} | "
                f"{escape_table(schema.title)} | "
                f"`{escape_table(schema.version)}` | "
                f"{escape_table(schema.status)} | "
                f"{len(distinct_schema_fields(schema))} | "
                f"{source_copy_link(schema.source.path)} |"
            )
        lines.append("")
    return clean_markdown("\n".join(lines))


def class_sort_key(record: FieldRecord) -> tuple[int, str]:
    return (
        FIELD_CLASS_ORDER.get(record.field_class.casefold(), 99),
        record.name.casefold(),
    )


def render_aliases(
    record: FieldRecord,
    *,
    prefix: str = "",
    field_names: set[str] | None = None,
) -> str:
    if not record.aliases:
        return ""
    return ", ".join(
        field_link(alias, prefix=prefix) if field_names is None or alias in field_names else inline_code(alias)
        for alias in record.aliases
    )


def render_field_summary(
    record: FieldRecord,
    *,
    prefix: str = "",
    field_names: set[str] | None = None,
) -> str:
    parts: list[str] = []
    if record.field_class:
        parts.append(f"class {inline_code(record.field_class)}")
    if record.field_type:
        parts.append(f"type {inline_code(record.field_type)}")
    if record.aliases:
        parts.append(f"aliases {render_aliases(record, prefix=prefix, field_names=field_names)}")
    return "; ".join(parts) or "no field metadata"


def render_schema_page(schema: SchemaDoc, reference: AsimReference) -> str:
    field_names = distinct_field_names(reference)
    grouped: dict[str, list[FieldRecord]] = defaultdict(list)
    for record in schema.fields:
        grouped[record.source_section or "Fields"].append(record)
    alias_records = [record for record in schema.fields if record.field_class.casefold() == "alias"]
    priority_records = [
        record
        for record in schema.fields
        if record.field_class.casefold() in {"mandatory", "recommended"}
    ]
    lines = [
        f"# {schema.name}",
        "",
        f"- **Catalog title**: {schema.title}",
        f"- **Kind**: `{schema.kind}`",
        f"- **Version**: `{schema.version}`",
        f"- **Status**: `{schema.status}`",
        f"- **Source file**: {source_copy_link(schema.source.path, prefix='../')}",
        f"- **Distinct fields**: `{len(distinct_schema_fields(schema))}`",
        f"- **Field records**: `{len(schema.fields)}`",
        "",
    ]
    if schema.overview:
        lines.extend(["## Overview", "", schema.overview, ""])
    if priority_records:
        lines.extend(["## Mapping priorities", ""])
        for field_class in ("Mandatory", "Recommended"):
            matching = [
                record
                for record in priority_records
                if record.field_class.casefold() == field_class.casefold()
            ]
            if not matching:
                continue
            lines.extend([f"### {field_class}", ""])
            for record in sorted(matching, key=class_sort_key):
                lines.append(
                    f"- {field_link(record.name, prefix='../')}: "
                    f"{render_field_summary(record, prefix='../', field_names=field_names)} "
                    f"({record.source_section})"
                )
            lines.append("")
    if alias_records:
        lines.extend(["## Aliases", ""])
        lines.append("| Alias | Aliases to | Source section |")
        lines.append("| --- | --- | --- |")
        for record in sorted(alias_records, key=lambda item: item.name.casefold()):
            lines.append(
                "| "
                f"{field_link(record.name, prefix='../')} | "
                f"{escape_table(render_aliases(record, prefix='../', field_names=field_names) or summarize_markdown(record.description, limit=120))} | "
                f"{escape_table(record.source_section)} |"
            )
        lines.append("")
    lines.extend(["## Field sections", ""])
    for section in sorted(grouped, key=str.casefold):
        lines.extend([f"### {section}", ""])
        lines.append("| Field | Class | Type | Aliases to | Description |")
        lines.append("| --- | --- | --- | --- | --- |")
        for record in sorted(grouped[section], key=class_sort_key):
            lines.append(
                "| "
                f"{field_link(record.name, prefix='../')} | "
                f"{inline_code(record.field_class)} | "
                f"{inline_code(record.field_type)} | "
                f"{escape_table(render_aliases(record, prefix='../', field_names=field_names))} | "
                f"{escape_table(summarize_markdown(record.description))} |"
            )
        lines.append("")
    return clean_markdown("\n".join(lines))


def render_fields_index(reference: AsimReference) -> str:
    occurrences = field_occurrences(reference)
    lines = [
        "# Fields",
        "",
        "This index groups field records from all generated ASIM schema pages.",
        "",
        "| Field | Schema records | Schemas | Classes |",
        "| --- | ---: | --- | --- |",
    ]
    for name in sorted(occurrences, key=str.casefold):
        schema_names = sorted({schema.name for schema, _ in occurrences[name]}, key=str.casefold)
        classes = sorted(
            {record.field_class for _, record in occurrences[name] if record.field_class},
            key=lambda item: (FIELD_CLASS_ORDER.get(item.casefold(), 99), item.casefold()),
        )
        schema_links = ", ".join(
            schema_link(next(schema for schema in reference.schemas if schema.name == schema_name))
            for schema_name in schema_names
        )
        lines.append(
            "| "
            f"{field_link(name)} | "
            f"{len(occurrences[name])} | "
            f"{escape_table(schema_links)} | "
            f"{escape_table(', '.join(inline_code(value) for value in classes))} |"
        )
    return clean_markdown("\n".join(lines))


def render_field_detail(
    record: FieldRecord,
    schema: SchemaDoc,
    *,
    prefix: str = "",
    field_names: set[str] | None = None,
) -> str:
    lines = [
        f"### {schema.name}: {record.source_section}",
        "",
        f"- **Schema**: {schema_link(schema, prefix=prefix)}",
        f"- **Source file**: {source_copy_link(record.source_path, prefix=prefix)}",
    ]
    if record.field_class:
        lines.append(f"- **Class**: `{record.field_class}`")
    if record.field_type:
        lines.append(f"- **Type**: `{record.field_type}`")
    if record.aliases:
        lines.append(f"- **Aliases to**: {render_aliases(record, prefix=prefix, field_names=field_names)}")
    if record.examples:
        lines.append(f"- **Examples**: {', '.join(inline_code(example) for example in record.examples)}")
    lines.append("")
    if record.description:
        lines.extend([record.description, ""])
    if record.notes:
        lines.extend(["#### Notes", "", record.notes, ""])
    return "\n".join(lines).strip() + "\n"


def render_field_page(
    name: str,
    occurrences: list[tuple[SchemaDoc, FieldRecord]],
    reference: AsimReference,
) -> str:
    field_names = distinct_field_names(reference)
    schema_names = sorted({schema.name for schema, _ in occurrences}, key=str.casefold)
    aliases = sorted({alias for _, record in occurrences for alias in record.aliases}, key=str.casefold)
    lines = [
        f"# `{name}`",
        "",
        f"- **Source schema records**: `{len(occurrences)}`",
        f"- **Source schemas**: {', '.join(schema_link(schema, prefix='../') for schema in reference.schemas if schema.name in schema_names)}",
    ]
    if aliases:
        lines.append(
            "- **Aliases to**: "
            + ", ".join(
                field_link(alias, prefix="../") if alias in field_names else inline_code(alias)
                for alias in aliases
            )
        )
    lines.extend(["", "## Source schema occurrences", ""])
    lines.append("| Schema | Class | Type | Source section | Aliases to |")
    lines.append("| --- | --- | --- | --- | --- |")
    for schema, record in sorted(occurrences, key=lambda item: (item[0].name.casefold(), item[1].source_section.casefold())):
        lines.append(
            "| "
            f"{schema_link(schema, prefix='../')} | "
            f"{inline_code(record.field_class)} | "
            f"{inline_code(record.field_type)} | "
            f"{escape_table(record.source_section)} | "
            f"{escape_table(render_aliases(record, prefix='../', field_names=field_names))} |"
        )
    lines.extend(["", "## Details by schema", ""])
    for schema, record in sorted(occurrences, key=lambda item: (item[0].name.casefold(), item[1].source_section.casefold())):
        lines.append(render_field_detail(record, schema, prefix="../", field_names=field_names))
    return clean_markdown("\n".join(lines))


def build_docs(reference: AsimReference) -> dict[Path, str]:
    docs: dict[Path, str] = {
        Path("SKILL.md"): render_skill_markdown(reference),
        Path("source.md"): render_source_page(reference),
        Path("data/catalog.yaml"): render_catalog_yaml(reference),
        Path("data/fields.yaml"): render_fields_index_yaml(reference),
        Path("data/aliases.yaml"): render_aliases_yaml(reference),
    }
    for schema in reference.schemas:
        docs[Path(data_schema_path(schema.name))] = render_schema_yaml(schema)
    for name, occurrences in field_occurrences(reference).items():
        docs[Path(data_field_path(name))] = render_field_yaml(name, occurrences)
    copied_sources = {
        reference.catalog.path: reference.catalog.text,
        **{schema.source.path: schema.source.text for schema in reference.schemas},
        **{source.path: source.text for source in reference.supporting_sources},
    }
    for path, text in copied_sources.items():
        docs[source_copy_path(path)] = text
    return docs


def write_docs(output_dir: Path, docs: dict[Path, str]) -> None:
    shutil.rmtree(output_dir, ignore_errors=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    for relative_path, content in sorted(docs.items()):
        write_file(output_dir / relative_path, content)


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    with httpx.Client(headers=HTTP_HEADERS, follow_redirects=True, timeout=30.0) as client:
        source = resolve_ref(client, args.docs_ref)
        catalog = fetch_doc(client, source, SCHEMA_CATALOG_PATH)
        catalog_entries = parse_schema_catalog(catalog)
        schema_sources = {
            path: fetch_doc(client, source, path)
            for path in sorted({entry.path for entry in catalog_entries})
        }
        supporting_sources = tuple(fetch_doc(client, source, path) for path in SUPPORTING_SOURCE_PATHS)
    reference = build_reference(source, catalog, schema_sources, supporting_sources)
    docs = build_docs(reference)
    write_docs(output_dir, docs)
    print(f"Generated Microsoft ASIM skill in {output_dir}")


if __name__ == "__main__":
    main()
