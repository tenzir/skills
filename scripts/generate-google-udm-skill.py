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
    requirements: tuple[str, ...]


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


def parse_labeled_list_item(li: Tag) -> tuple[GuidanceBullet, tuple[str, ...]]:
    strong = li.find(["strong", "b"])
    full_text = markdown_text(li)
    if isinstance(strong, Tag):
        label = tag_text(strong).rstrip(":")
        text = re.sub(rf"^{re.escape(label)}\s*:?\s*", "", full_text).strip()
    else:
        label = "Note"
        text = full_text
    examples: tuple[str, ...] = ()
    if label.lower() in {"example", "examples"}:
        nested = li.find("ul")
        if isinstance(nested, Tag):
            examples = immediate_li_texts(nested, markdown=True)
        elif text:
            examples = (text,)
    return GuidanceBullet(label=label, text=text), examples


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
                if bullet.text:
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
        requirements = tuple(
            markdown_text(li)
            for li in cells[1].find_all("li")
            if markdown_text(li)
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
                current_kind = None
            continue
        if block.name == "p":
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
            text = markdown_text(block)
            if text:
                notes.append(text)
            continue
        pre = block.find("pre") if block.name != "pre" else block
        if isinstance(pre, Tag):
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
    return DocsGuidance(
        usage_source=usage_source,
        field_list_source=field_list_source,
        field_guidance=field_guidance,
        event_type_categories=event_type_categories,
        entity_guidance=entity_guidance,
        event_guidance=event_guidance,
        field_paths=merge_field_path_guidance(usage_field_path_notes, field_paths),
        datatypes=datatypes,
    )


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


def markdown_table_cell(text: str) -> str:
    return text.replace("|", "\\|")


def render_source_section(sources: tuple[DocSource, ...]) -> list[str]:
    lines = ["## Source", ""]
    for source in sources:
        lines.extend(
            [
                f"- **{source.title}**: {source.url}",
                f"  - Google last updated: `{source.last_updated}`",
            ]
        )
    lines.append("")
    return lines


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
                "it is not a proto message field.",
                stacklevel=2,
            )
        elif family not in known_messages:
            warnings.warn(
                f"Preserving usage guidance for {field.field_path}; "
                f"{family} is not a top-level or nested proto message name.",
                stacklevel=2,
            )


def render_usage_page(guidance: DocsGuidance) -> str:
    lines = [
        "# Google UDM Usage Guidance",
        "",
        "Generated from targeted sections of the Google UDM usage guide and field list.",
        "Use these pages for field population policy, required fields, field-path",
        "prefixes, datatype notes, and examples. Use the proto-derived schema pages",
        "for field existence, types, numbers, JSON names, oneofs, and deprecation.",
        "",
    ]
    lines.extend(render_source_section((guidance.usage_source, guidance.field_list_source)))
    lines.extend(
        [
            "## Generated Guidance",
            "",
            f"- Field guidance families: `{len({field.field_path.split('.', 1)[0] for field in guidance.field_guidance})}`",
            f"- Field guidance entries: `{len(guidance.field_guidance)}`",
            f"- Event type categories: `{len(guidance.event_type_categories)}`",
            f"- Event guidance sections: `{len(guidance.event_guidance)}`",
            f"- Entity requirement pages: `{len(guidance.entity_guidance)}`",
            f"- Datatype rows: `{len(guidance.datatypes)}`",
            "",
            "## Indexes",
            "",
            "- [Field paths](field-paths.md)",
            "- [Datatypes](datatypes.md)",
            "- [Field guidance](field-guidance.md)",
            "- [Event type categories](event-type-categories.md)",
            "- [Event guidance](event-guidance.md)",
            "- [Entity guidance](entity-guidance.md)",
            "",
        ]
    )
    return clean_markdown("\n".join(lines))


def render_field_paths_page(guidance: DocsGuidance) -> str:
    field_paths = guidance.field_paths
    lines = [
        "# Field Path Prefixes",
        "",
        "Use this page to choose the right field-path prefix for rules, Detect Engine,",
        "and configuration-based normalizer contexts.",
        "",
    ]
    lines.extend(render_source_section((guidance.usage_source, guidance.field_list_source)))
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
                lines.append(f"- {note}")
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
        "# Standard Datatypes",
        "",
        "Standard datatype notes from the Google UDM field list.",
        "",
    ]
    lines.extend(render_source_section((guidance.field_list_source,)))
    if not guidance.datatypes:
        lines.extend(["No datatype guidance was extracted.", ""])
        return clean_markdown("\n".join(lines))

    languages = sorted(
        {
            language
            for datatype in guidance.datatypes
            for language, _value in datatype.language_types
        }
    )
    lines.append("| Datatype | Notes | " + " | ".join(languages) + " |")
    lines.append("| --- | --- | " + " | ".join("---" for _ in languages) + " |")
    for datatype in guidance.datatypes:
        language_map = dict(datatype.language_types)
        cells = [
            f"`{datatype.datatype}`",
            markdown_table_cell(datatype.notes),
            *[
                markdown_table_cell(language_map.get(language, ""))
                for language in languages
            ],
        ]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    return clean_markdown("\n".join(lines))


def render_field_guidance_index(
    context: FileContext,
    guidance: DocsGuidance,
) -> tuple[str, dict[str, list[FieldGuidance]]]:
    groups: dict[str, list[FieldGuidance]] = defaultdict(list)
    for field in guidance.field_guidance:
        groups[field.field_path.split(".", 1)[0]].append(field)

    lines = [
        "# Field Guidance",
        "",
        "Field population guidance from the Google UDM usage guide. These pages",
        "describe how fields should be populated; use schema pages for exact field",
        "existence and types.",
        "",
    ]
    lines.extend(render_source_section((guidance.usage_source,)))
    lines.extend(["## Families", ""])
    for family in sorted(groups, key=str.lower):
        message = find_message_by_simple_name(context, family)
        schema_link = (
            f" ([schema](messages/{message.slug}.md))"
            if message is not None
            else ""
        )
        lines.append(
            f"- [{family}](field-guidance/{to_snake_case(family)}.md)"
            f" ({len(groups[family])} fields){schema_link}"
        )
    lines.append("")
    return clean_markdown("\n".join(lines)), groups


def render_field_guidance_page(
    context: FileContext,
    guidance: DocsGuidance,
    family: str,
    fields: list[FieldGuidance],
) -> str:
    message = find_message_by_simple_name(context, family)
    lines = [
        f"# {family} Field Guidance",
        "",
    ]
    lines.extend(render_source_section((guidance.usage_source,)))
    if message is not None:
        lines.extend(
            [
                "## Schema",
                "",
                f"- [{message.qualified_name}](../messages/{message.slug}.md)",
                "",
            ]
        )
    lines.extend(["## Fields", ""])
    for field in sorted(fields, key=lambda item: item.field_path.lower()):
        lines.extend([f"### `{field.field_path}`", ""])
        for item in field.items:
            if item.text:
                lines.append(f"- **{item.label}**: {item.text}")
        if field.examples:
            lines.extend(["", "#### Examples", ""])
            for example in field.examples:
                lines.append(f"- {example}")
        lines.append("")
    return clean_markdown("\n".join(lines))


def render_event_type_categories_page(
    guidance: DocsGuidance,
) -> str:
    event_guidance_values = {
        event_type
        for section in guidance.event_guidance
        for event_type in section.event_types
    }
    lines = [
        "# Event Type Categories",
        "",
        "Usage-guide grouping for choosing `metadata.event_type`.",
        "",
    ]
    lines.extend(render_source_section((guidance.usage_source,)))
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
                if event_type in event_guidance_values:
                    lines.append(
                        f"- [{value}](event-guidance/{to_snake_case(event_type)}.md)"
                    )
                else:
                    lines.append(f"- {value}")
        lines.append("")
    return clean_markdown("\n".join(lines))


def render_event_guidance_index(
    guidance: DocsGuidance,
) -> str:
    lines = [
        "# Event Guidance",
        "",
        "Required fields, optional fields, notes, and examples by",
        "`Metadata.EventType`. Grouped Google usage-guide sections are rendered as",
        "one alias page for each event type.",
        "",
    ]
    lines.extend(render_source_section((guidance.usage_source,)))
    lines.extend(["## Event Types", ""])
    entries = sorted(
        (
            (event_type, section.title)
            for section in guidance.event_guidance
            for event_type in section.event_types
        ),
        key=lambda item: item[0],
    )
    for event_type, title in entries:
        suffix = f" - section: {title}" if title != event_type else ""
        lines.append(
            f"- [`{event_type}`](event-guidance/{to_snake_case(event_type)}.md){suffix}"
        )
    lines.append("")
    return clean_markdown("\n".join(lines))


def render_event_guidance_page(
    guidance: DocsGuidance,
    event_type: str,
    section: EventGuidance,
) -> str:
    lines = [
        f"# {event_type} Event Guidance",
        "",
    ]
    lines.extend(render_source_section((guidance.usage_source,)))
    lines.extend(
        [
            "## Applies To",
            "",
            "- " + ", ".join(f"`{value}`" for value in section.event_types),
            f"- Usage-guide section: `{section.title}`",
            "- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)",
            "",
        ]
    )
    sections = [
        ("## Required Fields", section.required),
        ("## Optional Fields", section.optional),
        ("## Notes", section.notes),
    ]
    for title, values in sections:
        lines.extend([title, ""])
        if values:
            for value in values:
                lines.append(f"- {value}")
        else:
            lines.append("No entries extracted.")
        lines.append("")
    if section.examples:
        lines.extend(["## Examples", ""])
        for example_idx, example in enumerate(section.examples, start=1):
            title = example.title
            if len(section.examples) > 1:
                title = f"{title} ({example_idx})"
            lines.extend(
                [
                    f"### {title}",
                    "",
                    "```text",
                    example.code,
                    "```",
                    "",
                ]
            )
    return clean_markdown("\n".join(lines))


def render_entity_guidance_index(guidance: DocsGuidance) -> str:
    lines = [
        "# Entity Guidance",
        "",
        "Required fields for Google UDM entity types.",
        "",
    ]
    lines.extend(render_source_section((guidance.usage_source,)))
    lines.extend(["## Entity Types", ""])
    for entity in sorted(guidance.entity_guidance, key=lambda item: item.entity_type):
        lines.append(
            f"- [`{entity.entity_type}`](entity-guidance/{to_snake_case(entity.entity_type)}.md)"
        )
    lines.append("")
    return clean_markdown("\n".join(lines))


def render_entity_guidance_page(
    guidance: DocsGuidance,
    entity: EntityGuidance,
) -> str:
    lines = [
        f"# {entity.entity_type} Entity Guidance",
        "",
    ]
    lines.extend(render_source_section((guidance.usage_source,)))
    lines.extend(
        [
            "## Schema",
            "",
            "- Proto enum: [EntityMetadata.EntityType](../enums/entity_metadata_entity_type.md)",
            "- Entity root: [Entity](../messages/entity.md)",
            "",
            "## Requirements",
            "",
        ]
    )
    for requirement in entity.requirements:
        lines.append(f"- {requirement}")
    lines.append("")
    return clean_markdown("\n".join(lines))


def render_guidance_docs(
    context: FileContext,
    guidance: DocsGuidance,
) -> dict[Path, str]:
    validate_guidance_against_schema(context, guidance)
    docs: dict[Path, str] = {
        Path("usage.md"): render_usage_page(guidance),
        Path("field-paths.md"): render_field_paths_page(guidance),
        Path("datatypes.md"): render_datatypes_page(guidance),
        Path("event-type-categories.md"): render_event_type_categories_page(guidance),
        Path("event-guidance.md"): render_event_guidance_index(guidance),
        Path("entity-guidance.md"): render_entity_guidance_index(guidance),
    }

    field_index, field_groups = render_field_guidance_index(context, guidance)
    docs[Path("field-guidance.md")] = field_index
    for family, fields in field_groups.items():
        docs[Path("field-guidance") / f"{to_snake_case(family)}.md"] = (
            render_field_guidance_page(context, guidance, family, fields)
        )

    for section in guidance.event_guidance:
        for event_type in section.event_types:
            docs[Path("event-guidance") / f"{to_snake_case(event_type)}.md"] = (
                render_event_guidance_page(guidance, event_type, section)
            )

    for entity in guidance.entity_guidance:
        docs[Path("entity-guidance") / f"{to_snake_case(entity.entity_type)}.md"] = (
            render_entity_guidance_page(guidance, entity)
        )

    return docs


def render_schema_page(context: FileContext, source: SourceRef, fetched_files: set[str]) -> str:
    messages = generated_messages(context)
    fields = sum(len(message.descriptor.field) for message in messages)
    enum_values = sum(len(enum.descriptor.value) for enum in context.enums)
    roots = [
        ("UDM event", context.message_by_full_name.get(f"{context.file_proto.package}.UDM")),
        ("Entity graph", context.message_by_full_name.get(f"{context.file_proto.package}.Entity")),
    ]

    lines = [
        "# Google UDM schema",
        "",
        "Generated from the canonical Google UDM protocol buffer definitions.",
        "",
        "- **Sources**:",
        *[
            f"  - [{path}]({GITHUB_BLOB}/{source.sha}/{path})"
            for path in ROOT_PROTO_PATHS
            if path in fetched_files or path == UDM_PROTO_PATH
        ],
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
            "- [Usage guidance](usage.md)",
            "",
        ]
    )
    for label, root in roots:
        if root is None:
            continue
        lines.extend([f"## Top-level {label} fields", ""])
        lines.append("| Field | No. | Cardinality | Type | Description |")
        lines.append("| --- | ---: | --- | --- | --- |")
        for field_idx, field in enumerate(root.descriptor.field):
            comment = source_comment(context, root.file_name, (*root.path, 2, field_idx))
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


def render_skill_markdown(
    context: FileContext,
    source: SourceRef,
    guidance: DocsGuidance | None = None,
) -> str:
    guidance_sources = []
    if guidance is not None:
        guidance_sources = [
            f"- Usage guide last updated: `{guidance.usage_source.last_updated}`",
            f"- Field list last updated: `{guidance.field_list_source.last_updated}`",
        ]
    return clean_markdown(
        "\n".join(
            [
                "---",
                "name: tenzir-google-udm",
                "description: Answer questions about Google SecOps / Chronicle UDM (Unified Data Model) schema and normalization guidance. Use whenever the user asks about UDM fields, event types, entity types, required fields, field formats, field-path prefixes, messages, enums, entity nouns, metadata, security_result, network, Chronicle normalization, or Google SecOps event schema.",
                "---",
                "",
                "# Google UDM",
                "",
                "Look up the generated Google UDM schema and usage references before",
                "answering. The schema pages are generated from `backstory/udm.proto`",
                "and `backstory/entity.proto`; they are the ground truth for field",
                "existence, field numbers, types, JSON names, oneofs, and deprecation.",
                "The guidance pages are generated from targeted Google documentation",
                "sections; they are the source for population policy, required fields,",
                "field-path prefixes, datatype notes, and examples.",
                "",
                "## Source",
                "",
                "- [Schema summary](schema.md)",
                "- [Usage guidance](usage.md)",
                f"- Source ref: `{source.ref}`",
                f"- Resolved commit: `{source.sha}`",
                *guidance_sources,
                "",
                "## File layout",
                "",
                "```",
                "schema.md                  # Proto sources, counts, top-level UDM and Entity fields",
                "messages.md                # Message index",
                "messages/{message}.md      # Message fields and nested types",
                "enums.md                   # Enum index",
                "enums/{enum}.md            # Enum values",
                "event-types.md             # Dedicated Metadata.EventType reference",
                "usage.md                   # Guidance source summary and routing",
                "field-paths.md             # Rules, Detect Engine, and CBN prefixes",
                "datatypes.md               # Standard datatype notes",
                "field-guidance/{family}.md # Field population policy by message family",
                "event-guidance/{type}.md   # Required/optional event guidance by event type",
                "entity-guidance/{type}.md  # Required entity fields by entity type",
                "```",
                "",
                "## Question routing",
                "",
                "| Question pattern | Start here |",
                "| --- | --- |",
                "| What fields exist? | [Schema](schema.md), [Messages](messages.md), and specific message page |",
                "| What values can enum X take? | [Enums](enums.md) -> specific enum page |",
                "| How should I map this event? | [Event guidance](event-guidance.md), relevant [field guidance](field-guidance.md), then schema pages |",
                "| Which `metadata.event_type` should I use? | [Event type categories](event-type-categories.md), [Event types](event-types.md), then event guidance |",
                "| Required or forbidden fields? | [Event guidance](event-guidance.md) or [Entity guidance](entity-guidance.md) |",
                "| Field formats or examples? | [Field guidance](field-guidance.md) and [Datatypes](datatypes.md) |",
                "| Which field path prefix? | [Field paths](field-paths.md) |",
                "| What are `principal`, `src`, `target`, `observer`, `intermediary`, or `about`? | [UDM message](messages/udm.md), [Noun](messages/noun.md), and Noun field guidance |",
                "| What fields exist for network/protocol details? | [Network](messages/network.md), protocol messages such as DNS/HTTP/TLS/DHCP, and field guidance |",
                "| What fields exist for entities? | [Entity](messages/entity.md), [EntityMetadata](messages/entity_metadata.md), and [Entity guidance](entity-guidance.md) |",
                "| What is the top-level event shape? | [Schema summary](schema.md) and [UDM](messages/udm.md) |",
                "",
                "When a question asks for modeling guidance, read both layers: the",
                "guidance page for how Google says to populate the data and the schema",
                "page for the exact field structure. If the two layers appear to differ,",
                "state both facts and identify which source each fact comes from.",
                "",
                "## Domain knowledge",
                "",
                "- UDM events center on `metadata`, participant nouns (`principal`, `src`,",
                "  `target`, `intermediary`, `observer`, `about`), `security_result`,",
                "  `network`, and `extensions`.",
                "- UDM entities center on `metadata`, an `entity` noun, `relations`,",
                "  optional `risk_score`, and optional `metric` data.",
                "- `metadata.event_type` classifies the event. It is the first place to look",
                "  when deciding how an event should be represented.",
                "- `metadata.entity_type` classifies entity records and drives entity-specific",
                "  requirements.",
                "- `Noun` carries entity details such as users, assets, processes, files,",
                "  resources, cloud context, and labels.",
                "",
                "## Answering principles",
                "",
                "- Read before answering. Every schema or guidance claim must trace back to",
                "  a generated file in this skill.",
                "- Prefer exact field names, enum names, and message names from the reference.",
                "- Distinguish proto structure from mapping policy. Required-field and",
                "  population rules come from guidance pages, not from proto field presence.",
                "- Do not invent UDM semantics from memory.",
                "",
            ]
        )
    )


def build_docs(
    context: FileContext,
    source: SourceRef,
    fetched_files: set[str],
    guidance: DocsGuidance | None = None,
) -> dict[Path, str]:
    docs: dict[Path, str] = {
        Path("SKILL.md"): render_skill_markdown(context, source, guidance),
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
        docs = build_docs(context, source, fetched_files, guidance)
        write_docs(output_dir, docs)
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    print(f"Generated Google UDM skill in {output_dir}")


if __name__ == "__main__":
    main()
