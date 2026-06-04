#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "beautifulsoup4>=4.12.0",
#   "grpcio-tools>=1.64.0",
#   "httpx>=0.28.0",
#   "protobuf>=5.27.0",
# ]
# ///

from __future__ import annotations

import argparse
import re
import shutil
import tempfile
import unicodedata
import warnings
from collections import defaultdict
from dataclasses import dataclass
from importlib import resources
from pathlib import Path

import httpx
from bs4 import BeautifulSoup, NavigableString, Tag
from google.protobuf import descriptor_pb2
from grpc_tools import protoc


GOOGLEAPIS_REPO = "googleapis/googleapis"
GITHUB_API = f"https://api.github.com/repos/{GOOGLEAPIS_REPO}"
GITHUB_RAW = f"https://raw.githubusercontent.com/{GOOGLEAPIS_REPO}"
GITHUB_BLOB = f"https://github.com/{GOOGLEAPIS_REPO}/blob"
UDM_PROTO_PATH = "backstory/udm.proto"
ENTITY_PROTO_PATH = "backstory/entity.proto"
ROOT_PROTO_PATHS = (UDM_PROTO_PATH, ENTITY_PROTO_PATH)
UDM_USAGE_URL = "https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en"
UDM_FIELD_LIST_URL = "https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list?hl=en"
HTTP_HEADERS = {
    "User-Agent": "tenzir-google-udm-generator",
    "Accept": "application/vnd.github+json",
}
IMPORT_RE = re.compile(
    r'^\s*import\s+(?:public\s+|weak\s+)?"([^"]+)";',
    flags=re.MULTILINE,
)

FIELD_TYPE_NAMES = descriptor_pb2.FieldDescriptorProto.Type
FIELD_LABELS = descriptor_pb2.FieldDescriptorProto.Label

SCALAR_TYPES = {
    descriptor_pb2.FieldDescriptorProto.TYPE_DOUBLE: "double",
    descriptor_pb2.FieldDescriptorProto.TYPE_FLOAT: "float",
    descriptor_pb2.FieldDescriptorProto.TYPE_INT64: "int64",
    descriptor_pb2.FieldDescriptorProto.TYPE_UINT64: "uint64",
    descriptor_pb2.FieldDescriptorProto.TYPE_INT32: "int32",
    descriptor_pb2.FieldDescriptorProto.TYPE_FIXED64: "fixed64",
    descriptor_pb2.FieldDescriptorProto.TYPE_FIXED32: "fixed32",
    descriptor_pb2.FieldDescriptorProto.TYPE_BOOL: "bool",
    descriptor_pb2.FieldDescriptorProto.TYPE_STRING: "string",
    descriptor_pb2.FieldDescriptorProto.TYPE_BYTES: "bytes",
    descriptor_pb2.FieldDescriptorProto.TYPE_UINT32: "uint32",
    descriptor_pb2.FieldDescriptorProto.TYPE_SFIXED32: "sfixed32",
    descriptor_pb2.FieldDescriptorProto.TYPE_SFIXED64: "sfixed64",
    descriptor_pb2.FieldDescriptorProto.TYPE_SINT32: "sint32",
    descriptor_pb2.FieldDescriptorProto.TYPE_SINT64: "sint64",
}
WELL_KNOWN_TYPES = {
    "google.protobuf.Duration": "duration",
    "google.protobuf.Struct": "object",
    "google.protobuf.Timestamp": "timestamp",
    "google.type.Interval": "interval",
    "google.type.LatLng": "latLng",
}
GUIDANCE_FIELD_PATH_ROOTS = {
    "about",
    "additional",
    "entity",
    "extensions",
    "idm",
    "intermediary",
    "metric",
    "metadata",
    "network",
    "observer",
    "principal",
    "relations",
    "security_result",
    "securityresult",
    "src",
    "target",
}
GUIDANCE_SIMPLE_FIELD_NAMES = GUIDANCE_FIELD_PATH_ROOTS | {
    "application",
    "category",
    "email",
    "event_timestamp",
    "event_type",
    "file",
    "ip",
    "mac",
    "name",
    "port",
    "process",
    "registry",
    "resource",
    "type",
    "url",
    "user",
}
MIN_GUIDANCE_COUNTS = {
    "field population guidance sections": 20,
    "event type category values": 20,
    "entity type guidance sections": 5,
    "entity type requirement bullets": 8,
    "event guidance sections": 10,
    "event guidance event type values": 20,
    "standard datatype rows": 5,
}
MIN_FIELD_PATH_COUNTS = {
    "rules engine prefix notes": 1,
    "Detect Engine notes": 1,
    "Detect Engine examples": 2,
    "CBN notes": 1,
    "CBN examples": 2,
    "field path style notes": 2,
}


@dataclass(frozen=True, slots=True)
class SourceRef:
    ref: str
    sha: str


@dataclass(frozen=True, slots=True)
class MessageDoc:
    file_name: str
    full_name: str
    qualified_name: str
    slug: str
    descriptor: descriptor_pb2.DescriptorProto
    path: tuple[int, ...]
    parent: str | None


@dataclass(frozen=True, slots=True)
class EnumDoc:
    file_name: str
    full_name: str
    qualified_name: str
    slug: str
    descriptor: descriptor_pb2.EnumDescriptorProto
    path: tuple[int, ...]
    parent: str | None


@dataclass(slots=True)
class FileContext:
    file_proto: descriptor_pb2.FileDescriptorProto
    file_protos: list[descriptor_pb2.FileDescriptorProto]
    comments: dict[tuple[str, tuple[int, ...]], descriptor_pb2.SourceCodeInfo.Location]
    messages: list[MessageDoc]
    enums: list[EnumDoc]
    message_by_full_name: dict[str, MessageDoc]
    enum_by_full_name: dict[str, EnumDoc]
    map_entry_by_full_name: dict[str, MessageDoc]


@dataclass(frozen=True, slots=True)
class DocSource:
    title: str
    url: str
    last_updated: str


@dataclass(frozen=True, slots=True)
class GuidanceBullet:
    label: str
    text: str
    values: tuple["GuidanceValue", ...] = ()


@dataclass(frozen=True, slots=True)
class GuidanceValue:
    value: str
    description: str


@dataclass(frozen=True, slots=True)
class FieldGuidance:
    field_path: str
    items: tuple[GuidanceBullet, ...]
    examples: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class EventTypeCategory:
    title: str
    description: tuple[str, ...]
    values: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class EntityGuidance:
    entity_type: str
    requirements: tuple["EntityRequirement", ...]


@dataclass(frozen=True, slots=True)
class EntityRequirement:
    text: str
    children: tuple["EntityRequirement", ...] = ()


@dataclass(frozen=True, slots=True)
class GuidanceExample:
    title: str
    code: str


@dataclass(frozen=True, slots=True)
class EventGuidance:
    title: str
    event_types: tuple[str, ...]
    required: tuple[str, ...]
    optional: tuple[str, ...]
    notes: tuple[str, ...]
    examples: tuple[GuidanceExample, ...]


@dataclass(frozen=True, slots=True)
class FieldPathGuidance:
    usage_notes: tuple[str, ...]
    detect_engine_notes: tuple[str, ...]
    detect_engine_examples: tuple[str, ...]
    cbn_notes: tuple[str, ...]
    cbn_examples: tuple[str, ...]
    style_notes: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class DatatypeGuidance:
    datatype: str
    notes: str
    language_types: tuple[tuple[str, str], ...]


@dataclass(frozen=True, slots=True)
class DocsGuidance:
    usage_source: DocSource
    field_list_source: DocSource
    field_guidance: tuple[FieldGuidance, ...] = ()
    event_type_categories: tuple[EventTypeCategory, ...] = ()
    entity_guidance: tuple[EntityGuidance, ...] = ()
    event_guidance: tuple[EventGuidance, ...] = ()
    field_paths: FieldPathGuidance | None = None
    datatypes: tuple[DatatypeGuidance, ...] = ()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--ref",
        default="master",
        help="googleapis/googleapis ref to build from (default: master)",
    )
    return parser.parse_args()


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


def fetch_text(client: httpx.Client, url: str) -> str:
    response = client.get(url)
    response.raise_for_status()
    return response.text


def is_bundled_google_protobuf_import(path: str) -> bool:
    return path.startswith("google/protobuf/")


def fetch_proto_tree(client: httpx.Client, source: SourceRef, output_dir: Path) -> set[str]:
    pending = list(ROOT_PROTO_PATHS)
    fetched: set[str] = set()

    while pending:
        path = pending.pop()
        if path in fetched or is_bundled_google_protobuf_import(path):
            continue
        text = fetch_text(client, raw_url(source.sha, path))
        write_file(output_dir / path, text)
        fetched.add(path)
        for imported_path in IMPORT_RE.findall(text):
            if imported_path not in fetched:
                pending.append(imported_path)

    return fetched


def compile_descriptor(
    proto_root: Path,
    proto_paths: str | tuple[str, ...] | list[str] = ROOT_PROTO_PATHS,
) -> descriptor_pb2.FileDescriptorSet:
    if isinstance(proto_paths, str):
        proto_paths = (proto_paths,)
    output_path = proto_root / "udm.desc"
    protobuf_include = resources.files("grpc_tools") / "_proto"
    code = protoc.main(
        [
            "protoc",
            f"-I{proto_root}",
            f"-I{protobuf_include}",
            "--include_imports",
            "--include_source_info",
            f"--descriptor_set_out={output_path}",
            *proto_paths,
        ]
    )
    if code != 0:
        raise RuntimeError(f"protoc failed with exit code {code}")

    descriptor_set = descriptor_pb2.FileDescriptorSet()
    descriptor_set.ParseFromString(output_path.read_bytes())
    return descriptor_set


def source_comment(
    context: FileContext,
    file_name: str,
    path: tuple[int, ...],
) -> str:
    location = context.comments.get((file_name, path))
    if location is None:
        return ""
    return clean_comment(location.leading_comments or location.trailing_comments)


def clean_comment(comment: str) -> str:
    paragraphs: list[str] = []
    current: list[str] = []
    for raw_line in comment.strip().splitlines():
        line = re.sub(r"\s+", " ", raw_line.strip())
        if not line:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(line)
    if current:
        paragraphs.append(" ".join(current))
    return "\n\n".join(paragraphs)


def to_snake_case(name: str) -> str:
    name = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"[^A-Za-z0-9]+", "_", name)
    return name.strip("_").lower()


def entity_slug(qualified_name: str) -> str:
    return "_".join(to_snake_case(part) for part in qualified_name.split("."))


def relative_name(package: str, full_name: str) -> str:
    prefix = f"{package}."
    return full_name.removeprefix(prefix)


def collect_messages_and_enums(
    file_proto: descriptor_pb2.FileDescriptorProto,
    extra_file_protos: list[descriptor_pb2.FileDescriptorProto] | None = None,
) -> FileContext:
    package = file_proto.package
    file_protos = [file_proto, *(extra_file_protos or [])]
    comments = {
        (proto.name, tuple(location.path)): location
        for proto in file_protos
        for location in proto.source_code_info.location
    }
    messages: list[MessageDoc] = []
    enums: list[EnumDoc] = []

    def walk_enum(
        proto: descriptor_pb2.FileDescriptorProto,
        enum: descriptor_pb2.EnumDescriptorProto,
        qualified_name: str,
        path: tuple[int, ...],
        parent: str | None,
    ) -> None:
        full_name = f"{proto.package}.{qualified_name}" if proto.package else qualified_name
        enums.append(
            EnumDoc(
                file_name=proto.name,
                full_name=full_name,
                qualified_name=qualified_name,
                slug=entity_slug(qualified_name),
                descriptor=enum,
                path=path,
                parent=parent,
            )
        )

    def walk_message(
        proto: descriptor_pb2.FileDescriptorProto,
        message: descriptor_pb2.DescriptorProto,
        qualified_name: str,
        path: tuple[int, ...],
        parent: str | None,
    ) -> None:
        full_name = f"{proto.package}.{qualified_name}" if proto.package else qualified_name
        message_doc = MessageDoc(
            file_name=proto.name,
            full_name=full_name,
            qualified_name=qualified_name,
            slug=entity_slug(qualified_name),
            descriptor=message,
            path=path,
            parent=parent,
        )
        messages.append(message_doc)
        for enum_idx, enum in enumerate(message.enum_type):
            walk_enum(
                proto,
                enum,
                f"{qualified_name}.{enum.name}",
                (*path, 4, enum_idx),
                qualified_name,
            )
        for nested_idx, nested in enumerate(message.nested_type):
            walk_message(
                proto,
                nested,
                f"{qualified_name}.{nested.name}",
                (*path, 3, nested_idx),
                qualified_name,
            )

    for proto in file_protos:
        if proto.package != package:
            continue
        for idx, message in enumerate(proto.message_type):
            walk_message(proto, message, message.name, (4, idx), None)
        for idx, enum in enumerate(proto.enum_type):
            walk_enum(proto, enum, enum.name, (5, idx), None)

    message_by_full_name = {
        message.full_name: message
        for message in messages
    }
    enum_by_full_name = {
        enum.full_name: enum
        for enum in enums
    }
    map_entry_by_full_name = {
        message.full_name: message
        for message in messages
        if message.descriptor.options.map_entry
    }
    return FileContext(
        file_proto=file_proto,
        file_protos=file_protos,
        comments=comments,
        messages=messages,
        enums=enums,
        message_by_full_name=message_by_full_name,
        enum_by_full_name=enum_by_full_name,
        map_entry_by_full_name=map_entry_by_full_name,
    )


def generated_messages(context: FileContext) -> list[MessageDoc]:
    return [
        message
        for message in context.messages
        if not message.descriptor.options.map_entry
    ]


def simple_type_label(context: FileContext, full_name: str) -> str:
    return relative_name(context.file_proto.package, full_name).rsplit(".", 1)[-1]


def type_label(context: FileContext, full_name: str) -> str:
    simple = simple_type_label(context, full_name)
    type_names = [
        *(message.full_name for message in generated_messages(context)),
        *(enum.full_name for enum in context.enums),
    ]
    if sum(simple_type_label(context, name) == simple for name in type_names) == 1:
        return simple
    return relative_name(context.file_proto.package, full_name)


def link_for_message(message: MessageDoc, section: str) -> str:
    if section == "messages":
        return f"{message.slug}.md"
    return f"messages/{message.slug}.md"


def link_for_enum(enum: EnumDoc, section: str) -> str:
    if section == "messages":
        return f"../enums/{enum.slug}.md"
    if section == "enums":
        return f"{enum.slug}.md"
    return f"enums/{enum.slug}.md"


def format_type(
    context: FileContext,
    field: descriptor_pb2.FieldDescriptorProto,
    *,
    section: str,
) -> str:
    if (
        field.type == descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE
        and field.type_name.lstrip(".") in context.map_entry_by_full_name
    ):
        entry = context.map_entry_by_full_name[field.type_name.lstrip(".")]
        key, value = entry.descriptor.field
        return (
            "map<"
            f"{format_type(context, key, section=section)}, "
            f"{format_type(context, value, section=section)}"
            ">"
        )

    if field.type in SCALAR_TYPES:
        return f"`{SCALAR_TYPES[field.type]}`"

    if field.type in (
        descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE,
        descriptor_pb2.FieldDescriptorProto.TYPE_ENUM,
    ):
        full_name = field.type_name.lstrip(".")
        if full_name in WELL_KNOWN_TYPES:
            return f"`{WELL_KNOWN_TYPES[full_name]}`"
        message = context.message_by_full_name.get(full_name)
        if message is not None and not message.descriptor.options.map_entry:
            return f"[`{type_label(context, full_name)}`]({link_for_message(message, section)})"
        enum = context.enum_by_full_name.get(full_name)
        if enum is not None:
            return f"[`{type_label(context, full_name)}`]({link_for_enum(enum, section)})"
        return f"`{full_name}`"

    type_name = FIELD_TYPE_NAMES.Name(field.type).removeprefix("TYPE_").lower()
    return f"`{type_name}`"


def field_cardinality(
    context: FileContext,
    field: descriptor_pb2.FieldDescriptorProto,
) -> str:
    if (
        field.type == descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE
        and field.type_name.lstrip(".") in context.map_entry_by_full_name
    ):
        return "map"
    if field.label == descriptor_pb2.FieldDescriptorProto.LABEL_REPEATED:
        return "repeated"
    if field.proto3_optional:
        return "optional"
    return "singular"


def field_display_name(field: descriptor_pb2.FieldDescriptorProto) -> str:
    return field.json_name or field.name


def rest_field_name_map(context: FileContext) -> dict[str, str]:
    return {
        field.name: field_display_name(field)
        for message in generated_messages(context)
        for field in message.descriptor.field
        if field.name != field_display_name(field)
    }


def apply_endpoint_language(text: str) -> str:
    replacements = {
        "RFC 3339, as appropriate for JSON or Proto3 timestamp format.": "RFC 3339 timestamp.",
        "as appropriate for JSON or Proto3 timestamp format": "as RFC 3339 timestamp values",
        " in Proto3 using": " using",
        " in Proto3": "",
        "Proto3 format": "timestamp",
        "Proto3 timestamp format": "timestamp",
        "proto3 format": "timestamp",
        "single File proto": "single File message",
        "Unified Data Model schema": "Unified Data Model",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def apply_rest_field_names(context: FileContext, text: str) -> str:
    text = apply_endpoint_language(text)
    replacements = rest_field_name_map(context)
    if not replacements:
        return text
    pattern = re.compile(
        r"(?<![?&/])\b("
        + "|".join(re.escape(name) for name in sorted(replacements, key=len, reverse=True))
        + r")\b(?!\s*=)"
    )
    return pattern.sub(lambda match: replacements[match.group(0)], text)


def code_rest_field_names(context: FileContext, text: str) -> str:
    field_names = sorted(
        {
            value
            for value in rest_field_name_map(context).values()
            if re.search(r"[A-Z]", value)
        },
        key=len,
        reverse=True,
    )
    if not field_names:
        return text
    pattern = re.compile(
        r"\b(" + "|".join(re.escape(name) for name in field_names) + r")\b"
    )
    return "".join(
        part
        if part.startswith("`") and part.endswith("`")
        else pattern.sub(lambda match: code_span(match.group(0)), part)
        for part in re.split(r"(`[^`]*`)", text)
    )


def find_field_by_name(
    message: MessageDoc,
    name: str,
) -> descriptor_pb2.FieldDescriptorProto | None:
    for field in message.descriptor.field:
        if field.name == name or field_display_name(field) == name:
            return field
    return None


def display_field_path(context: FileContext, field_path: str) -> str:
    parts = field_path.split(".")
    if not parts:
        return field_path
    message = find_message_by_simple_name(context, parts[0])
    if message is None:
        return field_path

    display_parts = [message.qualified_name.rsplit(".", 1)[-1]]
    current_message: MessageDoc | None = message
    for part in parts[1:]:
        if current_message is None:
            display_parts.append(part)
            continue
        field = find_field_by_name(current_message, part)
        if field is None:
            display_parts.append(part)
            current_message = None
            continue
        display_parts.append(field_display_name(field))
        nested_message = context.message_by_full_name.get(field.type_name.lstrip("."))
        current_message = (
            nested_message
            if field.type == descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE
            and nested_message is not None
            else None
        )
    return ".".join(display_parts)


def oneof_name(
    message: descriptor_pb2.DescriptorProto,
    field: descriptor_pb2.FieldDescriptorProto,
) -> str | None:
    if not field.HasField("oneof_index") or field.proto3_optional:
        return None
    return message.oneof_decl[field.oneof_index].name


def active_oneofs(
    message: descriptor_pb2.DescriptorProto,
) -> list[tuple[str, list[descriptor_pb2.FieldDescriptorProto]]]:
    result: list[tuple[str, list[descriptor_pb2.FieldDescriptorProto]]] = []
    for idx, oneof in enumerate(message.oneof_decl):
        fields = [
            field
            for field in message.field
            if field.HasField("oneof_index")
            and field.oneof_index == idx
            and not field.proto3_optional
        ]
        if fields:
            result.append((oneof.name, fields))
    return result


def format_meta(entries: list[tuple[str, object]]) -> str:
    return "\n".join(
        f"- **{label}**: {value}"
        for label, value in entries
        if value not in (None, "")
    )


def format_field_meta(entries: list[tuple[str, object]]) -> str:
    return "\n".join(
        f"- {label}: {value}"
        for label, value in entries
        if value not in (None, "")
    )


def render_field(
    context: FileContext,
    message_doc: MessageDoc,
    field_idx: int,
) -> str:
    message = message_doc.descriptor
    field = message.field[field_idx]
    comment = apply_rest_field_names(
        context,
        source_comment(context, message_doc.file_name, (*message_doc.path, 2, field_idx)),
    )
    meta = format_field_meta(
        [
            (
                "Type",
                f"{format_type(context, field, section='messages')} "
                f"({field_cardinality(context, field)})",
            ),
            ("Oneof", f"`{oneof_name(message, field)}`" if oneof_name(message, field) else ""),
            ("Deprecated", "`true`" if field.options.deprecated else ""),
        ]
    )
    lines = [f"### `{field_display_name(field)}`", ""]
    if meta:
        lines.extend([meta, ""])
    if comment:
        lines.extend([comment, ""])
    return "\n".join(lines).strip() + "\n"


def render_guidance_bullet(
    item: GuidanceBullet,
    context: FileContext | None = None,
) -> list[str]:
    def format_text(text: str) -> str:
        if context is not None:
            text = apply_rest_field_names(context, text)
            return code_rest_field_names(context, format_guidance_text(text))
        return format_guidance_text(text)

    if item.values:
        header = f"- **{item.label}**:"
        if item.text:
            header += f" {format_text(item.text)}"
        lines = [header]
        for value in item.values:
            value_line = f"  - {code_span(value.value)}"
            if value.description:
                value_line += f": {format_text(value.description)}"
            lines.append(value_line)
        return lines
    if item.text:
        return [f"- **{item.label}**: {format_text(item.text)}"]
    return [f"- **{item.label}**"]


def render_message_guidance(
    context: FileContext,
    fields: tuple[FieldGuidance, ...],
) -> list[str]:
    if not fields:
        return []
    lines = [
        "## Guidance",
        "",
        "Population guidance from the Google UDM usage guide.",
        "",
    ]
    for field in sorted(fields, key=lambda item: item.field_path.lower()):
        lines.extend([f"### `{display_field_path(context, field.field_path)}`", ""])
        for item in field.items:
            lines.extend(render_guidance_bullet(item, context))
        if field.examples:
            lines.extend(["", "#### Examples", ""])
            for example in field.examples:
                lines.append(f"- {apply_rest_field_names(context, example)}")
        lines.append("")
    return lines


def render_entity_requirement(
    context: FileContext,
    requirement: EntityRequirement,
    *,
    depth: int = 0,
) -> list[str]:
    indent = "  " * depth
    text = apply_rest_field_names(context, requirement.text)
    lines = [f"{indent}- {code_rest_field_names(context, format_guidance_text(text))}"]
    for child in requirement.children:
        lines.extend(render_entity_requirement(context, child, depth=depth + 1))
    return lines


def render_entity_type_guidance(
    context: FileContext,
    entity_guidance: tuple[EntityGuidance, ...],
) -> list[str]:
    if not entity_guidance:
        return []
    lines = [
        "## Entity Type Guidance",
        "",
        "Required fields from the Google UDM usage guide. Set",
        "`metadata.entityType` to the matching `EntityMetadata.EntityType` value.",
        "",
    ]
    for entity in sorted(entity_guidance, key=lambda item: item.entity_type):
        lines.extend([f"### `{entity.entity_type}`", ""])
        for requirement in entity.requirements:
            lines.extend(render_entity_requirement(context, requirement))
        lines.append("")
    return lines


def markdown_heading_anchor(text: str) -> str:
    anchor = normalize_text(text).lower()
    anchor = re.sub(r"[^\w\s-]", "", anchor)
    return anchor.replace(" ", "-")


def event_token_prefix(event_types: tuple[str, ...]) -> tuple[str, ...]:
    tokenized = [event_type.split("_") for event_type in event_types]
    if not tokenized:
        return ()
    prefix: list[str] = []
    for idx in range(min(len(tokens) for tokens in tokenized)):
        token = tokenized[0][idx]
        if all(tokens[idx] == token for tokens in tokenized):
            prefix.append(token)
        else:
            break
    return tuple(prefix)


def humanize_event_tokens(tokens: tuple[str, ...] | list[str]) -> str:
    return " ".join(token.capitalize() for token in tokens)


def event_guidance_heading(section: EventGuidance) -> str:
    if len(section.event_types) == 1:
        return section.event_types[0]

    prefix = event_token_prefix(section.event_types)
    if not prefix:
        return section.title

    suffixes = []
    for event_type in section.event_types:
        tokens = event_type.split("_")
        suffix_tokens = tokens[len(prefix):] or tokens
        suffixes.append(humanize_event_tokens(suffix_tokens))
    return f"{humanize_event_tokens(prefix)} {' / '.join(suffixes)} Events"


def format_event_guidance_text(context: FileContext, text: str) -> str:
    text = apply_rest_field_names(context, text)

    def format_fragment(fragment: str) -> str:
        formatted = format_guidance_text(fragment)
        formatted = code_rest_field_names(context, formatted)
        field_name_alternation = "|".join(
            re.escape(name)
            for name in sorted(GUIDANCE_SIMPLE_FIELD_NAMES, key=len, reverse=True)
        )
        simple_field_pattern = re.compile(
            rf"\b({field_name_alternation})\b"
            rf"(?=(?:\s+(?:and|or)\s+(?:{field_name_alternation}))*\s+fields?\b)",
            flags=re.IGNORECASE,
        )
        return "".join(
            part
            if part.startswith("`") and part.endswith("`")
            else simple_field_pattern.sub(lambda match: code_span(match.group(0)), part)
            for part in re.split(r"(`[^`]*`)", formatted)
        )

    compound_match = re.match(
        r"^([a-z][A-Za-z0-9_]*)(\s+and\s+)(`?[^`:]+`?)(:\s*)(.*)$",
        text,
    )
    if compound_match and compound_match.group(1).lower() in GUIDANCE_FIELD_PATH_ROOTS:
        return (
            f"{code_span(compound_match.group(1))}"
            f"{compound_match.group(2)}"
            f"{format_fragment(compound_match.group(3))}"
            f"{compound_match.group(4)}"
            f"{format_fragment(compound_match.group(5))}"
        )
    match = re.match(
        r"^([a-z][A-Za-z0-9_]*(?:\.[A-Za-z][A-Za-z0-9_]*)*)(:\s*)(.*)$",
        text,
    )
    if match:
        return f"{code_span(match.group(1))}: {format_fragment(match.group(3))}"
    return format_fragment(text)


def render_event_guidance_items(
    context: FileContext,
    title: str,
    values: tuple[str, ...],
) -> list[str]:
    if not values:
        return []
    lines = [f"#### {title}", ""]
    for value in values:
        lines.append(f"- {format_event_guidance_text(context, value)}")
    lines.append("")
    return lines


def render_event_type_guidance(context: FileContext, guidance: DocsGuidance) -> list[str]:
    if not guidance.event_guidance:
        return []
    lines = [
        "## Guidance",
        "",
        "Population guidance for choosing event types and required fields.",
        "",
    ]
    for section in guidance.event_guidance:
        lines.extend([f"### {event_guidance_heading(section)}", ""])
        if len(section.event_types) > 1:
            event_types = ", ".join(code_span(value) for value in section.event_types)
            lines.extend([f"Applies to: {event_types}", ""])
        lines.extend(
            render_event_guidance_items(context, "Required Fields", section.required)
        )
        lines.extend(
            render_event_guidance_items(context, "Optional Fields", section.optional)
        )
        lines.extend(render_event_guidance_items(context, "Notes", section.notes))
        if section.examples:
            lines.extend(["#### Examples", ""])
            for example_idx, example in enumerate(section.examples, start=1):
                title = example.title
                if len(section.examples) > 1:
                    title = f"{title} ({example_idx})"
                lines.extend(
                    [
                        f"##### {title}",
                        "",
                        "```text",
                        example.code,
                        "```",
                        "",
                    ]
                )
    return lines


def render_message_page(
    context: FileContext,
    message_doc: MessageDoc,
    guidance_fields: tuple[FieldGuidance, ...] = (),
    entity_guidance: tuple[EntityGuidance, ...] = (),
) -> str:
    message = message_doc.descriptor
    comment = apply_rest_field_names(
        context,
        source_comment(context, message_doc.file_name, message_doc.path),
    )

    lines = [f"# {type_label(context, message_doc.full_name)}", ""]
    if comment:
        lines.extend([comment, ""])
    oneofs = active_oneofs(message)
    if oneofs:
        lines.extend(["## Oneofs", ""])
        for name, fields in oneofs:
            field_list = ", ".join(f"`{field_display_name(field)}`" for field in fields)
            lines.append(f"- `{name}`: {field_list}")
        lines.append("")
    if message.field:
        lines.extend(["## Fields", ""])
        for field_idx, _field in enumerate(message.field):
            lines.append(render_field(context, message_doc, field_idx))
    else:
        lines.extend(["## Fields", "", "No fields.", ""])
    lines.extend(render_message_guidance(context, guidance_fields))
    if message_doc.qualified_name == "Entity":
        lines.extend(render_entity_type_guidance(context, entity_guidance))

    return clean_markdown("\n".join(lines))


def render_enum_value(
    context: FileContext,
    enum_doc: EnumDoc,
    value_idx: int,
    value: descriptor_pb2.EnumValueDescriptorProto,
) -> str:
    comment = apply_rest_field_names(
        context,
        source_comment(context, enum_doc.file_name, (*enum_doc.path, 2, value_idx)),
    )
    value_meta = str(value.number)
    if value.options.deprecated:
        value_meta += ", deprecated"
    if comment:
        return f"- `{value.name}` ({value_meta}): {comment}"
    return f"- `{value.name}` ({value_meta})"


def render_enum_page(
    context: FileContext,
    enum_doc: EnumDoc,
    *,
    title: str | None = None,
    guidance: DocsGuidance | None = None,
) -> str:
    enum = enum_doc.descriptor
    comment = apply_rest_field_names(
        context,
        source_comment(context, enum_doc.file_name, enum_doc.path),
    )
    lines = [f"# {title or type_label(context, enum_doc.full_name)}", ""]
    if comment:
        lines.extend([comment, ""])
    if enum.value:
        lines.extend(["## Values", ""])
        for value_idx, value in enumerate(enum.value):
            lines.append(render_enum_value(context, enum_doc, value_idx, value))
    if guidance is not None:
        lines.append("")
        lines.extend(render_event_type_guidance(context, guidance))
    return clean_markdown("\n".join(lines))


def clean_markdown(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def normalize_text(text: str) -> str:
    replacements = {
        "\xa0": " ",
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"\s+([:;,.])", r"\1", text)


def normalize_code(text: str) -> str:
    replacements = {
        "\xa0": " ",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return text.strip()


def tag_text(tag: Tag) -> str:
    return normalize_text(tag.get_text(" ", strip=True))


def code_span(text: str) -> str:
    text = normalize_code(text)
    if "`" not in text:
        return f"`{text}`"
    longest_tick_run = max(len(match.group(0)) for match in re.finditer(r"`+", text))
    delimiter = "`" * (longest_tick_run + 1)
    return f"{delimiter} {text} {delimiter}"


def format_guidance_text(text: str) -> str:
    parts = re.split(r"(`[^`]*`)", text)
    pattern = re.compile(r"\b[A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z][A-Za-z0-9_]*)+\b")
    standalone_name_alternation = "|".join(
        re.escape(name)
        for name in sorted(
            (name for name in GUIDANCE_SIMPLE_FIELD_NAMES if "_" in name),
            key=len,
            reverse=True,
        )
    )
    standalone_field_pattern = re.compile(
        rf"\b({standalone_name_alternation})\b",
        flags=re.IGNORECASE,
    )

    def replace(match: re.Match[str]) -> str:
        value = match.group(0)
        root = value.split(".", 1)[0]
        if (
            "_" in value
            or value[0].isupper()
            or root.lower() in GUIDANCE_FIELD_PATH_ROOTS
        ):
            return code_span(value)
        return value

    formatted = "".join(
        part if part.startswith("`") and part.endswith("`") else pattern.sub(replace, part)
        for part in parts
    )
    return "".join(
        part
        if part.startswith("`") and part.endswith("`")
        else standalone_field_pattern.sub(lambda match: code_span(match.group(0)), part)
        for part in re.split(r"(`[^`]*`)", formatted)
    )


def markdown_text(tag: Tag) -> str:
    def render_node(node: object) -> str:
        if isinstance(node, NavigableString):
            return str(node)
        if not isinstance(node, Tag):
            return ""
        if node.name == "code":
            text = normalize_code(node.get_text(" ", strip=True))
            return code_span(text) if text else ""
        if node.name == "br":
            return " "
        return "".join(render_node(child) for child in node.children)

    return normalize_text("".join(render_node(child) for child in tag.children))


def markdown_text_without_children(tag: Tag, excluded: tuple[Tag, ...]) -> str:
    excluded_ids = {id(item) for item in excluded}

    def render_node(node: object) -> str:
        if id(node) in excluded_ids:
            return ""
        if isinstance(node, NavigableString):
            return str(node)
        if not isinstance(node, Tag):
            return ""
        if node.name == "code":
            text = normalize_code(node.get_text(" ", strip=True))
            return code_span(text) if text else ""
        if node.name == "br":
            return " "
        return "".join(render_node(child) for child in node.children)

    return normalize_text("".join(render_node(child) for child in tag.children))


def heading_text(tag: Tag) -> str:
    value = tag.get("data-text")
    if isinstance(value, str) and value.strip():
        return normalize_text(value)
    return tag_text(tag)


def heading_level(tag: Tag) -> int | None:
    if tag.name and re.fullmatch(r"h[1-6]", tag.name):
        return int(tag.name[1])
    return None


def iter_section_siblings(
    heading: Tag,
    *,
    stop_levels: set[int],
) -> list[Tag]:
    result: list[Tag] = []
    for sibling in heading.next_siblings:
        if not isinstance(sibling, Tag):
            continue
        level = heading_level(sibling)
        if level in stop_levels:
            break
        result.append(sibling)
    return result


def article_from_html(html: str) -> tuple[BeautifulSoup, Tag]:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")
    if not isinstance(article, Tag):
        raise RuntimeError("Google documentation page does not contain an <article>")
    return soup, article


def source_from_soup(
    soup: BeautifulSoup,
    article: Tag,
    *,
    url: str,
) -> DocSource:
    title_tag = article.find("h1")
    title = heading_text(title_tag) if isinstance(title_tag, Tag) else url
    footer = soup.find("devsite-content-footer")
    footer_text = tag_text(footer) if isinstance(footer, Tag) else ""
    match = re.search(r"Last updated\s+([^\.]+UTC)", footer_text)
    last_updated = match.group(1) if match else "unknown"
    return DocSource(
        title=title,
        url=url,
        last_updated=last_updated,
    )


def immediate_li_texts(ul: Tag, *, markdown: bool = False) -> tuple[str, ...]:
    extractor = markdown_text if markdown else tag_text
    items: list[str] = []
    for li in ul.find_all("li", recursive=False):
        text = extractor(li)
        if text:
            items.append(text)
    return tuple(items)


def parse_guidance_value(li: Tag) -> GuidanceValue:
    text = normalize_text(li.get_text(" ", strip=True))
    match = re.fullmatch(r"([A-Z][A-Z0-9_]*)(?:\s*-\s*(.+))?", text)
    if match:
        return GuidanceValue(
            value=match.group(1),
            description=match.group(2) or "",
        )
    return GuidanceValue(value=text, description="")


def parse_labeled_list_item(li: Tag) -> tuple[GuidanceBullet, tuple[str, ...]]:
    strong = li.find(["strong", "b"])
    nested = li.find("ul")
    full_text = (
        markdown_text_without_children(li, (nested,))
        if isinstance(nested, Tag)
        else markdown_text(li)
    )
    if isinstance(strong, Tag):
        label = tag_text(strong).rstrip(":")
        text = re.sub(rf"^{re.escape(label)}\s*:?\s*", "", full_text).strip()
    else:
        label = "Note"
        text = full_text
    values: tuple[GuidanceValue, ...] = ()
    examples: tuple[str, ...] = ()
    if isinstance(nested, Tag):
        if label.lower() == "possible values":
            values = tuple(
                parse_guidance_value(nested_li)
                for nested_li in nested.find_all("li", recursive=False)
            )
        elif label.lower() in {"example", "examples"}:
            examples = immediate_li_texts(nested, markdown=True)
    elif label.lower() in {"example", "examples"} and text:
        examples = (text,)
    return GuidanceBullet(label=label, text=text, values=values), examples


def parse_field_guidance(article: Tag) -> tuple[FieldGuidance, ...]:
    result: list[FieldGuidance] = []
    in_population_section = False
    for heading in article.find_all(["h2", "h3"]):
        if not isinstance(heading, Tag):
            continue
        level = heading_level(heading)
        title = heading_text(heading)
        heading_id = heading.get("id")
        if level == 2:
            if heading_id in {
                "required_and_optional_entity_fields",
                "required_and_optional_fields",
            }:
                break
            in_population_section = title.startswith("Population of ")
            continue
        if level != 3 or not in_population_section or "." not in title:
            continue
        items: list[GuidanceBullet] = []
        examples: list[str] = []
        for block in iter_section_siblings(heading, stop_levels={2, 3, 4}):
            if block.name != "ul":
                continue
            for li in block.find_all("li", recursive=False):
                bullet, bullet_examples = parse_labeled_list_item(li)
                if bullet.text or bullet.values:
                    items.append(bullet)
                examples.extend(bullet_examples)
        if items or examples:
            result.append(
                FieldGuidance(
                    field_path=title,
                    items=tuple(items),
                    examples=tuple(examples),
                )
            )
    return tuple(result)


def extract_event_value(text: str) -> str | None:
    match = re.search(r"\b[A-Z][A-Z0-9]+(?:_[A-Z0-9]+)+\b", text)
    return match.group(0) if match else None


def code_event_type_value(text: str) -> str:
    event_type = extract_event_value(text)
    if not event_type:
        return text
    return text.replace(event_type, f"`{event_type}`", 1)


def extract_event_values(text: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys(re.findall(r"\b[A-Z][A-Z0-9]+(?:_[A-Z0-9]+)+\b", text)))


def parse_event_type_categories(article: Tag) -> tuple[EventTypeCategory, ...]:
    heading = article.find("h3", id="metadataevent_type")
    if not isinstance(heading, Tag):
        return ()

    categories: list[EventTypeCategory] = []
    current_title: str | None = None
    description: list[str] = []
    values: list[str] = []

    def flush() -> None:
        nonlocal current_title, description, values
        if current_title is not None:
            categories.append(
                EventTypeCategory(
                    title=current_title,
                    description=tuple(description),
                    values=tuple(values),
                )
            )
        current_title = None
        description = []
        values = []

    for block in iter_section_siblings(heading, stop_levels={2, 3}):
        if block.name == "h4":
            flush()
            current_title = heading_text(block)
            continue
        if current_title is None:
            continue
        if block.name == "p":
            text = markdown_text(block)
            if text:
                description.append(text)
        elif block.name == "ul":
            values.extend(immediate_li_texts(block))
    flush()
    return tuple(categories)


def parse_usage_field_path_notes(article: Tag) -> tuple[str, ...]:
    h1 = article.find("h1")
    if not isinstance(h1, Tag):
        return ()
    notes: list[str] = []
    capture_next_list = False
    for block in iter_section_siblings(h1, stop_levels={2}):
        text = tag_text(block)
        if capture_next_list and block.name == "ul":
            notes.extend(immediate_li_texts(block, markdown=True))
            break
        elif "UDM field name formats" in text:
            notes.append(markdown_text(block))
            capture_next_list = True
    return tuple(notes)


def parse_entity_requirement(li: Tag) -> EntityRequirement:
    child_lists = tuple(li.find_all("ul", recursive=False))
    text = (
        markdown_text_without_children(li, child_lists)
        if child_lists
        else markdown_text(li)
    )
    children: list[EntityRequirement] = []
    for child_list in child_lists:
        children.extend(
            parse_entity_requirement(child_li)
            for child_li in child_list.find_all("li", recursive=False)
        )
    return EntityRequirement(text=text, children=tuple(children))


def parse_entity_guidance(article: Tag) -> tuple[EntityGuidance, ...]:
    heading = article.find("h2", id="required_and_optional_entity_fields")
    if not isinstance(heading, Tag):
        return ()
    table = heading.find_next("table")
    if not isinstance(table, Tag):
        return ()
    result: list[EntityGuidance] = []
    for row in table.find_all("tr"):
        cells = row.find_all(["td", "th"], recursive=False)
        if len(cells) != 2 or cells[0].name == "th":
            continue
        entity_type = tag_text(cells[0])
        ul = cells[1].find("ul")
        requirements = (
            tuple(
                parse_entity_requirement(li)
                for li in ul.find_all("li", recursive=False)
                if markdown_text(li)
            )
            if isinstance(ul, Tag)
            else ()
        )
        if entity_type and requirements:
            result.append(
                EntityGuidance(
                    entity_type=entity_type,
                    requirements=requirements,
                )
            )
    return tuple(result)


def parse_event_guidance_section(heading: Tag, blocks: list[Tag]) -> EventGuidance | None:
    title = heading_text(heading)
    event_types = extract_event_values(title)
    if not event_types:
        return None

    required: list[str] = []
    optional: list[str] = []
    notes: list[str] = []
    examples: list[GuidanceExample] = []
    current_kind: str | None = None
    current_example_title: str | None = None

    for block in blocks:
        level = heading_level(block)
        if level in {4, 5}:
            text = heading_text(block)
            if "example" in text.lower():
                current_example_title = text
                # The usage guide examples are UDM text format, not endpoint
                # request bodies. Skip them until we can render valid endpoint
                # examples.
                current_kind = "example"
            continue
        if block.name == "p":
            if current_kind == "example":
                continue
            text = markdown_text(block)
            lowered = text.lower()
            if lowered.startswith("required fields"):
                current_kind = "required"
            elif lowered.startswith("optional fields"):
                current_kind = "optional"
            elif lowered.startswith("notes"):
                current_kind = "notes"
            elif text and current_kind in {None, "notes"}:
                notes.append(text)
            continue
        if block.name == "aside":
            if current_kind == "example":
                continue
            text = markdown_text(block)
            if text:
                notes.append(text)
            continue
        pre = block.find("pre") if block.name != "pre" else block
        if isinstance(pre, Tag):
            if current_kind == "example":
                continue
            code = normalize_code(pre.get_text("", strip=False))
            if code:
                examples.append(
                    GuidanceExample(
                        title=current_example_title or "Example",
                        code=code,
                    )
                )
            continue
        if block.name != "ul":
            continue
        if current_kind == "example":
            continue
        items = immediate_li_texts(block, markdown=True)
        if current_kind == "required":
            required.extend(items)
        elif current_kind == "optional":
            optional.extend(items)
        else:
            notes.extend(items)

    return EventGuidance(
        title=title,
        event_types=event_types,
        required=tuple(required),
        optional=tuple(optional),
        notes=tuple(notes),
        examples=tuple(examples),
    )


def parse_event_guidance(article: Tag) -> tuple[EventGuidance, ...]:
    heading = article.find("h2", id="required_and_optional_fields")
    if not isinstance(heading, Tag):
        return ()

    sections: list[EventGuidance] = []
    current_heading: Tag | None = None
    current_blocks: list[Tag] = []

    def flush() -> None:
        nonlocal current_heading, current_blocks
        if current_heading is not None:
            section = parse_event_guidance_section(current_heading, current_blocks)
            if section is not None:
                sections.append(section)
        current_heading = None
        current_blocks = []

    for sibling in heading.next_siblings:
        if not isinstance(sibling, Tag):
            continue
        level = heading_level(sibling)
        if level == 2:
            break
        if level == 3:
            flush()
            current_heading = sibling
            continue
        if current_heading is not None:
            current_blocks.append(sibling)
    flush()
    return tuple(sections)


def parse_usage_guide(
    html: str,
) -> tuple[
    DocSource,
    tuple[str, ...],
    tuple[FieldGuidance, ...],
    tuple[EventTypeCategory, ...],
    tuple[EntityGuidance, ...],
    tuple[EventGuidance, ...],
]:
    soup, article = article_from_html(html)
    source = source_from_soup(
        soup,
        article,
        url=UDM_USAGE_URL,
    )
    return (
        source,
        parse_usage_field_path_notes(article),
        parse_field_guidance(article),
        parse_event_type_categories(article),
        parse_entity_guidance(article),
        parse_event_guidance(article),
    )


def parse_field_path_guidance(article: Tag) -> FieldPathGuidance:
    h1 = article.find("h1")
    if not isinstance(h1, Tag):
        return FieldPathGuidance((), (), (), (), (), ())

    usage_notes: list[str] = []
    detect_notes: list[str] = []
    detect_examples: list[str] = []
    cbn_notes: list[str] = []
    cbn_examples: list[str] = []
    style_notes: list[str] = []
    current_mode: str | None = None

    for block in iter_section_siblings(h1, stop_levels={2}):
        if block.name == "p":
            text = markdown_text(block)
            if not text:
                continue
            if "Detect Engine" in text:
                current_mode = "detect"
                detect_notes.append(text)
            elif "configuration-based normalizer" in text:
                current_mode = "cbn"
                cbn_notes.append(text)
            elif "Field name and field type values" in text:
                current_mode = "style"
                style_notes.append(text)
            else:
                current_mode = None
                usage_notes.append(text)
            continue
        if block.name != "ul":
            continue
        examples_are_plain = current_mode in {"detect", "cbn"}
        items = immediate_li_texts(block, markdown=not examples_are_plain)
        if current_mode == "detect":
            detect_examples.extend(items)
        elif current_mode == "cbn":
            cbn_examples.extend(items)
        elif current_mode == "style":
            style_notes.extend(items)
        else:
            usage_notes.extend(items)

    return FieldPathGuidance(
        usage_notes=tuple(usage_notes),
        detect_engine_notes=tuple(detect_notes),
        detect_engine_examples=tuple(detect_examples),
        cbn_notes=tuple(cbn_notes),
        cbn_examples=tuple(cbn_examples),
        style_notes=tuple(style_notes),
    )


def merge_field_path_guidance(
    usage_notes: tuple[str, ...],
    field_list_guidance: FieldPathGuidance,
) -> FieldPathGuidance:
    return FieldPathGuidance(
        usage_notes=tuple(dict.fromkeys((*usage_notes, *field_list_guidance.usage_notes))),
        detect_engine_notes=field_list_guidance.detect_engine_notes,
        detect_engine_examples=field_list_guidance.detect_engine_examples,
        cbn_notes=field_list_guidance.cbn_notes,
        cbn_examples=field_list_guidance.cbn_examples,
        style_notes=field_list_guidance.style_notes,
    )


def parse_datatypes(article: Tag) -> tuple[DatatypeGuidance, ...]:
    heading = article.find("h2", id="standard_datatypes")
    if not isinstance(heading, Tag):
        return ()
    table = heading.find_next("table")
    if not isinstance(table, Tag):
        return ()
    header_row = table.find("tr")
    if not isinstance(header_row, Tag):
        return ()
    headers = [tag_text(cell) for cell in header_row.find_all("th")]
    result: list[DatatypeGuidance] = []
    for row in table.find_all("tr")[1:]:
        cells = [tag_text(cell) for cell in row.find_all("td", recursive=False)]
        if len(cells) < 2:
            continue
        language_types = tuple(
            (header, value)
            for header, value in zip(headers[2:], cells[2:], strict=False)
            if value
        )
        result.append(
            DatatypeGuidance(
                datatype=cells[0],
                notes=cells[1],
                language_types=language_types,
            )
        )
    return tuple(result)


def parse_field_list_guide(
    html: str,
) -> tuple[DocSource, FieldPathGuidance, tuple[DatatypeGuidance, ...]]:
    soup, article = article_from_html(html)
    source = source_from_soup(
        soup,
        article,
        url=UDM_FIELD_LIST_URL,
    )
    return source, parse_field_path_guidance(article), parse_datatypes(article)


def count_entity_requirements(requirements: tuple[EntityRequirement, ...]) -> int:
    return sum(
        1 + count_entity_requirements(requirement.children)
        for requirement in requirements
    )


def validate_docs_guidance_extraction(guidance: DocsGuidance) -> None:
    counts = {
        "field population guidance sections": len(guidance.field_guidance),
        "event type category values": sum(
            len(category.values) for category in guidance.event_type_categories
        ),
        "entity type guidance sections": len(guidance.entity_guidance),
        "entity type requirement bullets": sum(
            count_entity_requirements(entity.requirements)
            for entity in guidance.entity_guidance
        ),
        "event guidance sections": len(guidance.event_guidance),
        "event guidance event type values": sum(
            len(section.event_types) for section in guidance.event_guidance
        ),
        "standard datatype rows": len(guidance.datatypes),
    }
    failures = [
        f"{label}: expected at least {minimum}, found {counts[label]}"
        for label, minimum in MIN_GUIDANCE_COUNTS.items()
        if counts[label] < minimum
    ]

    if guidance.field_paths is None:
        failures.append("field path guidance: expected extracted guidance, found none")
    else:
        field_path_counts = {
            "rules engine prefix notes": len(guidance.field_paths.usage_notes),
            "Detect Engine notes": len(guidance.field_paths.detect_engine_notes),
            "Detect Engine examples": len(guidance.field_paths.detect_engine_examples),
            "CBN notes": len(guidance.field_paths.cbn_notes),
            "CBN examples": len(guidance.field_paths.cbn_examples),
            "field path style notes": len(guidance.field_paths.style_notes),
        }
        failures.extend(
            f"{label}: expected at least {minimum}, found {field_path_counts[label]}"
            for label, minimum in MIN_FIELD_PATH_COUNTS.items()
            if field_path_counts[label] < minimum
        )

    if failures:
        raise RuntimeError(
            "Google UDM docs guidance extraction failed sanity checks:\n"
            + "\n".join(f"- {failure}" for failure in failures)
        )


def fetch_docs_guidance(client: httpx.Client) -> DocsGuidance:
    usage_html = fetch_text(client, UDM_USAGE_URL)
    field_list_html = fetch_text(client, UDM_FIELD_LIST_URL)
    (
        usage_source,
        usage_field_path_notes,
        field_guidance,
        event_type_categories,
        entity_guidance,
        event_guidance,
    ) = parse_usage_guide(usage_html)
    field_list_source, field_paths, datatypes = parse_field_list_guide(field_list_html)
    guidance = DocsGuidance(
        usage_source=usage_source,
        field_list_source=field_list_source,
        field_guidance=field_guidance,
        event_type_categories=event_type_categories,
        entity_guidance=entity_guidance,
        event_guidance=event_guidance,
        field_paths=merge_field_path_guidance(usage_field_path_notes, field_paths),
        datatypes=datatypes,
    )
    validate_docs_guidance_extraction(guidance)
    return guidance


def brief_comment(comment: str, limit: int = 140) -> str:
    first_paragraph = comment.split("\n\n", 1)[0].replace("\n", " ").strip()
    if len(first_paragraph) <= limit:
        return first_paragraph
    return first_paragraph[: limit - 1].rstrip() + "..."


def render_messages_overview(context: FileContext) -> str:
    lines = ["# Messages", ""]
    for message in generated_messages(context):
        comment = apply_rest_field_names(
            context,
            source_comment(context, message.file_name, message.path),
        )
        suffix = f" - {brief_comment(comment)}" if comment else ""
        lines.append(
            f"- [{type_label(context, message.full_name)}](messages/{message.slug}.md)"
            f"{suffix}"
        )
    return clean_markdown("\n".join(lines))


def render_enums_overview(context: FileContext) -> str:
    lines = ["# Enums", ""]
    for enum in context.enums:
        comment = apply_rest_field_names(
            context,
            source_comment(context, enum.file_name, enum.path),
        )
        suffix = f" - {brief_comment(comment)}" if comment else ""
        lines.append(
            f"- [{type_label(context, enum.full_name)}](enums/{enum.slug}.md)"
            f"{suffix}"
        )
    return clean_markdown("\n".join(lines))


def markdown_table_cell(text: str) -> str:
    return text.replace("|", "\\|")


def enum_value_names(context: FileContext, qualified_name: str) -> set[str]:
    enum = context.enum_by_full_name.get(f"{context.file_proto.package}.{qualified_name}")
    if enum is None:
        return set()
    return {value.name for value in enum.descriptor.value}


def message_simple_names(context: FileContext) -> set[str]:
    return {
        message.qualified_name.rsplit(".", 1)[-1]
        for message in generated_messages(context)
    }


def find_message_by_simple_name(context: FileContext, name: str) -> MessageDoc | None:
    for message in generated_messages(context):
        if message.qualified_name.rsplit(".", 1)[-1].lower() == name.lower():
            return message
    return None


def group_field_guidance_by_message(
    context: FileContext,
    guidance: DocsGuidance,
) -> tuple[dict[str, tuple[FieldGuidance, ...]], tuple[FieldGuidance, ...]]:
    groups: dict[str, list[FieldGuidance]] = defaultdict(list)
    unmatched: list[FieldGuidance] = []
    for field in guidance.field_guidance:
        family = field.field_path.split(".", 1)[0]
        message = find_message_by_simple_name(context, family)
        if message is None:
            unmatched.append(field)
        else:
            groups[message.slug].append(field)
    return (
        {slug: tuple(fields) for slug, fields in groups.items()},
        tuple(unmatched),
    )


def validate_guidance_against_schema(context: FileContext, guidance: DocsGuidance) -> None:
    known_event_types = enum_value_names(context, "Metadata.EventType")
    known_entity_types = enum_value_names(context, "EntityMetadata.EntityType")

    if known_event_types:
        unknown_events = sorted(
            {
                event_type
                for section in guidance.event_guidance
                for event_type in section.event_types
                if event_type not in known_event_types
            }
        )
        if unknown_events:
            raise RuntimeError(
                "Usage guide event requirements reference unknown Metadata.EventType "
                f"values: {', '.join(unknown_events)}"
            )

    if known_entity_types:
        unknown_entities = sorted(
            entity.entity_type
            for entity in guidance.entity_guidance
            if entity.entity_type not in known_entity_types
        )
        if unknown_entities:
            raise RuntimeError(
                "Usage guide entity requirements reference unknown "
                "EntityMetadata.EntityType values: "
                f"{', '.join(unknown_entities)}"
            )

    known_messages = message_simple_names(context)
    for field in guidance.field_guidance:
        family = field.field_path.split(".", 1)[0]
        if family == "idm":
            warnings.warn(
                f"Preserving product-only usage guidance for {field.field_path}; "
                "it is not a UDM message field.",
                stacklevel=2,
            )
        elif family not in known_messages:
            warnings.warn(
                f"Preserving usage guidance for {field.field_path}; "
                f"{family} is not a top-level or nested UDM message name.",
                stacklevel=2,
            )


def render_field_paths_page(guidance: DocsGuidance) -> str:
    field_paths = guidance.field_paths
    lines = [
        "# Field Path Prefixes",
        "",
        "Use this page to choose the right field-path prefix for rules, Detect Engine,",
        "and configuration-based normalizer contexts.",
        "",
    ]
    if field_paths is None:
        lines.extend(["No field path guidance was extracted.", ""])
        return clean_markdown("\n".join(lines))

    sections = [
        ("## Rules Engine Prefix Notes", field_paths.usage_notes, ()),
        ("## Detect Engine", field_paths.detect_engine_notes, field_paths.detect_engine_examples),
        ("## Configuration-Based Normalizer", field_paths.cbn_notes, field_paths.cbn_examples),
        ("## Style Notes", field_paths.style_notes, ()),
    ]
    for title, notes, examples in sections:
        lines.extend([title, ""])
        if notes:
            for note in notes:
                lines.append(f"- {apply_endpoint_language(note)}")
        else:
            lines.append("No notes extracted.")
        if examples:
            lines.extend(["", "### Examples", ""])
            for example in examples:
                lines.append(f"- `{example}`")
        lines.append("")
    return clean_markdown("\n".join(lines))


def render_datatypes_page(guidance: DocsGuidance) -> str:
    lines = [
        "# Datatypes",
        "",
        "Common type labels used in the message field reference.",
        "",
        "| Type | Meaning |",
        "| --- | --- |",
        "| `string` | Text value. |",
        "| `bool` | Boolean value. |",
        "| `bytes` | Binary value. |",
        "| `int32`, `int64`, `uint32`, `uint64` | Integer value. |",
        "| `float`, `double` | Floating-point numeric value. |",
        "| `timestamp` | Timestamp value. Check field guidance for the expected format. |",
        "| `duration` | Duration value. Check field guidance for the expected format. |",
        "| `object` | Structured object for values that do not fit a specific UDM message. |",
        "| `interval` | Time interval value. |",
        "| `latLng` | Geographic latitude and longitude value. |",
        "| `map<K, V>` | Keyed collection whose keys and values use the listed types. |",
        "",
    ]
    return clean_markdown("\n".join(lines))


def render_event_type_categories_page(
    guidance: DocsGuidance,
) -> str:
    event_guidance_anchors = {
        event_type: markdown_heading_anchor(event_guidance_heading(section))
        for section in guidance.event_guidance
        for event_type in section.event_types
    }
    lines = [
        "# Event Type Categories",
        "",
        "Usage-guide grouping for choosing `metadata.eventType`.",
        "",
    ]
    if not guidance.event_type_categories:
        lines.extend(["No event type categories were extracted.", ""])
        return clean_markdown("\n".join(lines))
    for category in guidance.event_type_categories:
        lines.extend([f"## {category.title}", ""])
        for paragraph in category.description:
            lines.extend([paragraph, ""])
        if category.values:
            for value in category.values:
                event_type = extract_event_value(value)
                label = code_event_type_value(value)
                if event_type in event_guidance_anchors:
                    lines.append(
                        f"- [{label}](event-types.md#{event_guidance_anchors[event_type]})"
                    )
                else:
                    lines.append(f"- {label}")
        lines.append("")
    return clean_markdown("\n".join(lines))


def render_guidance_docs(
    context: FileContext,
    guidance: DocsGuidance,
) -> dict[Path, str]:
    validate_guidance_against_schema(context, guidance)
    docs: dict[Path, str] = {
        Path("field-paths.md"): render_field_paths_page(guidance),
        Path("datatypes.md"): render_datatypes_page(guidance),
        Path("event-type-categories.md"): render_event_type_categories_page(guidance),
    }

    return docs


def render_top_level_structure(context: FileContext) -> list[str]:
    roots = [
        ("Event", context.message_by_full_name.get(f"{context.file_proto.package}.UDM")),
        ("Entity", context.message_by_full_name.get(f"{context.file_proto.package}.Entity")),
    ]
    lines = [
        "## Top-level structure",
        "",
        "UDM uses two top-level data shapes: event records for telemetry and",
        "entity records for contextual objects such as users, assets, domains,",
        "files, URLs, and IP addresses.",
        "",
        "The event ingestion path imports UDM events. Entity records are",
        "ingested as entity context through the entity ingestion path.",
        "",
    ]
    for label, root in roots:
        if root is None:
            continue
        lines.extend([f"### {label}", ""])
        lines.append("| Field | Cardinality | Type | Description |")
        lines.append("| --- | --- | --- | --- |")
        for field_idx, field in enumerate(root.descriptor.field):
            comment = apply_rest_field_names(
                context,
                source_comment(context, root.file_name, (*root.path, 2, field_idx)),
            )
            lines.append(
                "| "
                f"`{field_display_name(field)}` | "
                f"`{field_cardinality(context, field)}` | "
                f"{format_type(context, field, section='schema')} | "
                f"{markdown_table_cell(brief_comment(comment, 100))} |"
            )
        lines.append("")
    return lines


def render_skill_markdown(
    context: FileContext,
    guidance: DocsGuidance | None = None,
) -> str:
    return clean_markdown(
        "\n".join(
            [
                "---",
                "name: tenzir-google-udm",
                "description: Answer questions about Google SecOps / Chronicle UDM (Unified Data Model) field structure and normalization guidance. Use whenever the user asks about UDM fields, event types, entity types, required fields, field formats, field-path prefixes for rules, Detect Engine, or CBN, messages, enums, entity nouns, metadata, securityResult, network, Chronicle normalization, or Google SecOps ingestion endpoints.",
                "---",
                "",
                "# Google UDM",
                "",
                "Google UDM (Unified Data Model) is the Google SecOps data model",
                "for normalized security telemetry. It represents events and",
                "entities in a common structure so logs from different products",
                "can describe actors, assets, resources, network activity,",
                "security outcomes, and product context with consistent field",
                "names and enum values.",
                "",
                "Use this skill to answer how a log should map to UDM, which",
                "event or entity type to choose, which UDM fields to populate,",
                "and how Google expects values and field paths to be formatted.",
                "",
                *render_top_level_structure(context),
                "## Question routing",
                "",
                "| Question pattern | Start here |",
                "| --- | --- |",
                "| What fields exist? | [Messages](messages.md) and the specific message page |",
                "| What values can enum X take? | [Enums](enums.md) -> specific enum page |",
                "| How should I map this event? | [Event types](event-types.md), then relevant message pages |",
                "| Which `metadata.eventType` should I use? | [Event type categories](event-type-categories.md), then [Event types](event-types.md) |",
                "| Required or forbidden fields? | [Event types](event-types.md), [Entity](messages/entity.md), or relevant message page |",
                "| Field formats or examples? | Relevant message page guidance and [Datatypes](datatypes.md) |",
                "| How do I reference UDM fields in rules, Detect Engine, or CBN? | [Field paths](field-paths.md) |",
                "| What are `principal`, `src`, `target`, `observer`, `intermediary`, or `about`? | [UDM message](messages/udm.md) and [Noun](messages/noun.md) |",
                "| What fields exist for network/protocol details? | [Network](messages/network.md) and protocol messages such as DNS/HTTP/TLS/DHCP |",
                "| What fields exist for entities? | [Entity](messages/entity.md) and [EntityMetadata](messages/entity_metadata.md) |",
                "| What is the top-level event shape? | This file, then [UDM](messages/udm.md) |",
                "",
                "When a question asks for modeling guidance, read both layers.",
                "Message, event, or entity guidance explains how Google says to",
                "populate the data; message pages show the exact field structure.",
                "If they differ, state both facts instead of silently",
                "reconciling them.",
                "",
                "## Domain knowledge",
                "",
                "- UDM events center on `metadata`, participant nouns (`principal`, `src`,",
                "  `target`, `intermediary`, `observer`, `about`), `securityResult`,",
                "  `network`, and `extensions`.",
                "- UDM entities center on `metadata`, an `entity` noun, `relations`,",
                "  optional `riskScore`, and optional `metric` data.",
                "- `metadata.eventType` classifies the event. It is the first place to look",
                "  when deciding how an event should be represented.",
                "- `metadata.entityType` classifies entity records and drives entity-specific",
                "  requirements.",
                "- `Noun` carries entity details such as users, assets, processes, files,",
                "  resources, cloud context, and labels.",
                "",
            ]
        )
    )


def build_docs(
    context: FileContext,
    guidance: DocsGuidance | None = None,
) -> dict[Path, str]:
    field_guidance_groups: dict[str, tuple[FieldGuidance, ...]] = {}
    if guidance is not None:
        field_guidance_groups, _unmatched_field_guidance = group_field_guidance_by_message(
            context,
            guidance,
        )

    docs: dict[Path, str] = {
        Path("SKILL.md"): render_skill_markdown(context, guidance),
        Path("messages.md"): render_messages_overview(context),
        Path("enums.md"): render_enums_overview(context),
    }

    for message in generated_messages(context):
        docs[Path("messages") / f"{message.slug}.md"] = render_message_page(
            context,
            message,
            field_guidance_groups.get(message.slug, ()),
            guidance.entity_guidance
            if guidance is not None and message.qualified_name == "Entity"
            else (),
        )

    for enum in context.enums:
        docs[Path("enums") / f"{enum.slug}.md"] = render_enum_page(context, enum)

    event_type = context.enum_by_full_name.get(f"{context.file_proto.package}.Metadata.EventType")
    if event_type is not None:
        docs[Path("event-types.md")] = render_enum_page(
            context,
            event_type,
            title="Event Types",
            guidance=guidance,
        )

    if guidance is not None:
        docs.update(render_guidance_docs(context, guidance))

    return docs


def write_docs(output_dir: Path, docs: dict[Path, str]) -> None:
    shutil.rmtree(output_dir, ignore_errors=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    for relative_path, content in sorted(docs.items()):
        write_file(output_dir / relative_path, content)


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    temp_root = Path(tempfile.mkdtemp(prefix="google-udm-skill-"))

    try:
        with httpx.Client(headers=HTTP_HEADERS, follow_redirects=True, timeout=30.0) as client:
            source = resolve_ref(client, args.ref)
            fetched_files = fetch_proto_tree(client, source, temp_root)
            guidance = fetch_docs_guidance(client)

        descriptor_set = compile_descriptor(temp_root)
        file_proto = next(
            (proto for proto in descriptor_set.file if proto.name == UDM_PROTO_PATH),
            None,
        )
        if file_proto is None:
            raise RuntimeError(f"Descriptor set does not contain {UDM_PROTO_PATH}")

        extra_file_protos = [
            proto
            for proto in descriptor_set.file
            if proto.name in fetched_files and proto.name != UDM_PROTO_PATH
        ]
        context = collect_messages_and_enums(file_proto, extra_file_protos)
        docs = build_docs(context, guidance)
        write_docs(output_dir, docs)
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    print(f"Generated Google UDM skill in {output_dir}")


if __name__ == "__main__":
    main()
