#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
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
from dataclasses import dataclass
from importlib import resources
from pathlib import Path

import httpx
from google.protobuf import descriptor_pb2
from grpc_tools import protoc


GOOGLEAPIS_REPO = "googleapis/googleapis"
GITHUB_API = f"https://api.github.com/repos/{GOOGLEAPIS_REPO}"
GITHUB_RAW = f"https://raw.githubusercontent.com/{GOOGLEAPIS_REPO}"
GITHUB_BLOB = f"https://github.com/{GOOGLEAPIS_REPO}/blob"
UDM_PROTO_PATH = "backstory/udm.proto"
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
    pending = [UDM_PROTO_PATH]
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
    proto_path: str = UDM_PROTO_PATH,
) -> descriptor_pb2.FileDescriptorSet:
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
            proto_path,
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


def type_label(context: FileContext, full_name: str) -> str:
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


def oneof_name(
    message: descriptor_pb2.DescriptorProto,
    field: descriptor_pb2.FieldDescriptorProto,
) -> str | None:
    if not field.HasField("oneof_index") or field.proto3_optional:
        return None
    return message.oneof_decl[field.oneof_index].name


def active_oneofs(message: descriptor_pb2.DescriptorProto) -> list[tuple[str, list[str]]]:
    result: list[tuple[str, list[str]]] = []
    for idx, oneof in enumerate(message.oneof_decl):
        fields = [
            field.name
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


def render_field(
    context: FileContext,
    message_doc: MessageDoc,
    field_idx: int,
) -> str:
    message = message_doc.descriptor
    field = message.field[field_idx]
    comment = source_comment(context, message_doc.file_name, (*message_doc.path, 2, field_idx))
    meta = format_meta(
        [
            ("Number", f"`{field.number}`"),
            ("Cardinality", f"`{field_cardinality(context, field)}`"),
            ("Type", format_type(context, field, section="messages")),
            ("JSON name", f"`{field.json_name}`" if field.json_name else ""),
            ("Oneof", f"`{oneof_name(message, field)}`" if oneof_name(message, field) else ""),
            ("Deprecated", "`true`" if field.options.deprecated else ""),
        ]
    )
    lines = [f"### `{field.name}`", ""]
    if meta:
        lines.extend([meta, ""])
    if comment:
        lines.extend([comment, ""])
    return "\n".join(lines).strip() + "\n"


def render_message_page(context: FileContext, message_doc: MessageDoc) -> str:
    message = message_doc.descriptor
    comment = source_comment(context, message_doc.file_name, message_doc.path)
    nested_messages = [
        candidate
        for candidate in generated_messages(context)
        if candidate.parent == message_doc.qualified_name
    ]
    nested_enums = [
        enum
        for enum in context.enums
        if enum.parent == message_doc.qualified_name
    ]
    meta = format_meta(
        [
            ("Full name", f"`{message_doc.full_name}`"),
            ("Fields", f"`{len(message.field)}`"),
            ("Nested messages", f"`{len(nested_messages)}`" if nested_messages else ""),
            ("Nested enums", f"`{len(nested_enums)}`" if nested_enums else ""),
        ]
    )

    lines = [f"# {message_doc.qualified_name}", ""]
    if comment:
        lines.extend([comment, ""])
    if meta:
        lines.extend([meta, ""])
    if nested_messages:
        lines.extend(["## Nested messages", ""])
        for nested in nested_messages:
            lines.append(f"- [{nested.qualified_name}]({nested.slug}.md)")
        lines.append("")
    if nested_enums:
        lines.extend(["## Nested enums", ""])
        for nested in nested_enums:
            lines.append(f"- [{nested.qualified_name}](../enums/{nested.slug}.md)")
        lines.append("")
    oneofs = active_oneofs(message)
    if oneofs:
        lines.extend(["## Oneofs", ""])
        for name, fields in oneofs:
            field_list = ", ".join(f"`{field}`" for field in fields)
            lines.append(f"- `{name}`: {field_list}")
        lines.append("")
    if message.field:
        lines.extend(["## Fields", ""])
        for field_idx, _field in enumerate(message.field):
            lines.append(render_field(context, message_doc, field_idx))
    else:
        lines.extend(["## Fields", "", "No fields.", ""])

    return clean_markdown("\n".join(lines))


def render_enum_value(
    context: FileContext,
    enum_doc: EnumDoc,
    value_idx: int,
    value: descriptor_pb2.EnumValueDescriptorProto,
) -> str:
    comment = source_comment(context, enum_doc.file_name, (*enum_doc.path, 2, value_idx))
    meta = format_meta(
        [
            ("Number", f"`{value.number}`"),
            ("Deprecated", "`true`" if value.options.deprecated else ""),
        ]
    )
    lines = [f"### `{value.name}`", ""]
    if meta:
        lines.extend([meta, ""])
    if comment:
        lines.extend([comment, ""])
    return "\n".join(lines).strip() + "\n"


def render_enum_page(
    context: FileContext,
    enum_doc: EnumDoc,
    *,
    title: str | None = None,
) -> str:
    enum = enum_doc.descriptor
    comment = source_comment(context, enum_doc.file_name, enum_doc.path)
    meta = format_meta(
        [
            ("Full name", f"`{enum_doc.full_name}`"),
            ("Values", f"`{len(enum.value)}`"),
        ]
    )
    lines = [f"# {title or enum_doc.qualified_name}", ""]
    if comment:
        lines.extend([comment, ""])
    if meta:
        lines.extend([meta, ""])
    if enum.value:
        lines.extend(["## Values", ""])
        for value_idx, value in enumerate(enum.value):
            lines.append(render_enum_value(context, enum_doc, value_idx, value))
    return clean_markdown("\n".join(lines))


def clean_markdown(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def brief_comment(comment: str, limit: int = 140) -> str:
    first_paragraph = comment.split("\n\n", 1)[0].replace("\n", " ").strip()
    if len(first_paragraph) <= limit:
        return first_paragraph
    return first_paragraph[: limit - 1].rstrip() + "..."


def render_messages_overview(context: FileContext) -> str:
    lines = ["# Messages", ""]
    for message in generated_messages(context):
        comment = source_comment(context, message.file_name, message.path)
        suffix = f" - {brief_comment(comment)}" if comment else ""
        lines.append(
            f"- [{message.qualified_name}](messages/{message.slug}.md)"
            f" ({len(message.descriptor.field)} fields){suffix}"
        )
    return clean_markdown("\n".join(lines))


def render_enums_overview(context: FileContext) -> str:
    lines = ["# Enums", ""]
    for enum in context.enums:
        comment = source_comment(context, enum.file_name, enum.path)
        suffix = f" - {brief_comment(comment)}" if comment else ""
        lines.append(
            f"- [{enum.qualified_name}](enums/{enum.slug}.md)"
            f" ({len(enum.descriptor.value)} values){suffix}"
        )
    return clean_markdown("\n".join(lines))


def render_schema_page(context: FileContext, source: SourceRef, fetched_files: set[str]) -> str:
    messages = generated_messages(context)
    fields = sum(len(message.descriptor.field) for message in messages)
    enum_values = sum(len(enum.descriptor.value) for enum in context.enums)
    udm = context.message_by_full_name.get(f"{context.file_proto.package}.UDM")

    lines = [
        "# Google UDM schema",
        "",
        "Generated from the canonical Google UDM protocol buffer definition.",
        "",
        f"- **Source**: [{UDM_PROTO_PATH}]({GITHUB_BLOB}/{source.sha}/{UDM_PROTO_PATH})",
        f"- **Requested ref**: `{source.ref}`",
        f"- **Resolved commit**: `{source.sha}`",
        f"- **Package**: `{context.file_proto.package}`",
        f"- **Messages**: `{len(messages)}`",
        f"- **Enums**: `{len(context.enums)}`",
        f"- **Fields**: `{fields}`",
        f"- **Enum values**: `{enum_values}`",
        "",
        "## Imports",
        "",
    ]
    for path in sorted(fetched_files):
        if path != UDM_PROTO_PATH:
            lines.append(f"- `{path}`")
    lines.extend(
        [
            "",
            "## Indexes",
            "",
            "- [Messages](messages.md)",
            "- [Enums](enums.md)",
            "- [Event types](event-types.md)",
            "",
        ]
    )
    if udm is not None:
        lines.extend(["## Top-level UDM fields", ""])
        lines.append("| Field | No. | Cardinality | Type | Description |")
        lines.append("| --- | ---: | --- | --- | --- |")
        for field_idx, field in enumerate(udm.descriptor.field):
            comment = source_comment(context, udm.file_name, (*udm.path, 2, field_idx))
            lines.append(
                "| "
                f"`{field.name}` | "
                f"`{field.number}` | "
                f"`{field_cardinality(context, field)}` | "
                f"{format_type(context, field, section='schema')} | "
                f"{brief_comment(comment, 100)} |"
            )
        lines.append("")
    return clean_markdown("\n".join(lines))


def render_skill_markdown(context: FileContext, source: SourceRef) -> str:
    return clean_markdown(
        "\n".join(
            [
                "---",
                "name: tenzir-google-udm",
                "description: Answer questions about Google SecOps / Chronicle UDM (Unified Data Model) schema. Use whenever the user asks about UDM fields, event types, messages, enums, entity nouns, metadata, security_result, network, Chronicle normalization, or Google SecOps event schema.",
                "---",
                "",
                "# Google UDM",
                "",
                "Look up the generated Google UDM schema reference and answer from those",
                "files. The reference is generated from `backstory/udm.proto`, which is",
                "the ground truth for this skill. Only state schema facts from files you",
                "read. If the generated files do not cover the question, say so.",
                "",
                "## Source",
                "",
                f"- [Schema summary](schema.md)",
                f"- Source ref: `{source.ref}`",
                f"- Resolved commit: `{source.sha}`",
                "",
                "## File layout",
                "",
                "```",
                "schema.md                  # Source, counts, imports, top-level UDM fields",
                "messages.md                # Message index",
                "messages/{message}.md      # Message fields and nested types",
                "enums.md                   # Enum index",
                "enums/{enum}.md            # Enum values",
                "event-types.md             # Dedicated Metadata.EventType reference",
                "```",
                "",
                "## Question routing",
                "",
                "| Question pattern | Start here |",
                "| --- | --- |",
                "| What fields does UDM/message X have? | [Messages](messages.md) -> specific message page |",
                "| What values can enum X take? | [Enums](enums.md) -> specific enum page |",
                "| Which `metadata.event_type` should I use? | [Event types](event-types.md), then candidate message pages |",
                "| What are `principal`, `src`, `target`, `observer`, `intermediary`, or `about`? | [UDM message](messages/udm.md) and [Noun](messages/noun.md) |",
                "| What fields exist for network/protocol details? | [Network](messages/network.md), then protocol messages such as DNS, HTTP, TLS, DHCP |",
                "| What fields exist for detections or alerts? | [SecurityResult](messages/security_result.md) and related nested enums |",
                "| What is the top-level event shape? | [Schema summary](schema.md) and [UDM](messages/udm.md) |",
                "",
                "When a question asks for modeling guidance, read the relevant event type,",
                "top-level UDM noun fields, and candidate message pages. Explain what the",
                "proto comments say and call out any requirement that is not represented in",
                "the generated reference.",
                "",
                "## Domain knowledge",
                "",
                "- UDM events center on `metadata`, participant nouns (`principal`, `src`,",
                "  `target`, `intermediary`, `observer`, `about`), `security_result`,",
                "  `network`, and `extensions`.",
                "- `metadata.event_type` classifies the event. It is the first place to look",
                "  when deciding how an event should be represented.",
                "- `Noun` carries entity details such as users, assets, processes, files,",
                "  resources, cloud context, and labels.",
                "- The generated Google UDM field list is derived from the proto. Use this",
                "  skill's proto-derived files as the local source of truth.",
                "",
                "## Answering principles",
                "",
                "- Read before answering. Every schema claim must trace back to a generated",
                "  file in this skill.",
                "- Prefer exact field names, enum names, and message names from the reference.",
                "- Distinguish proto structure from mapping policy. If a required-field or",
                "  validation rule is not in the generated files, say it is not covered here.",
                "- Do not invent UDM semantics from memory.",
                "",
            ]
        )
    )


def build_docs(
    context: FileContext,
    source: SourceRef,
    fetched_files: set[str],
) -> dict[Path, str]:
    docs: dict[Path, str] = {
        Path("SKILL.md"): render_skill_markdown(context, source),
        Path("schema.md"): render_schema_page(context, source, fetched_files),
        Path("messages.md"): render_messages_overview(context),
        Path("enums.md"): render_enums_overview(context),
    }

    for message in generated_messages(context):
        docs[Path("messages") / f"{message.slug}.md"] = render_message_page(context, message)

    for enum in context.enums:
        docs[Path("enums") / f"{enum.slug}.md"] = render_enum_page(context, enum)

    event_type = context.enum_by_full_name.get(f"{context.file_proto.package}.Metadata.EventType")
    if event_type is not None:
        docs[Path("event-types.md")] = render_enum_page(
            context,
            event_type,
            title="Event Types",
        )

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
        docs = build_docs(context, source, fetched_files)
        write_docs(output_dir, docs)
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    print(f"Generated Google UDM skill in {output_dir}")


if __name__ == "__main__":
    main()
