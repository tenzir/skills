#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "httpx>=0.28.0",
#   "PyYAML>=6.0.0",
# ]
# ///

from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx
import yaml


AZURE_SENTINEL_REPO = "Azure/Azure-Sentinel"
GITHUB_API = f"https://api.github.com/repos/{AZURE_SENTINEL_REPO}"
GITHUB_RAW = f"https://raw.githubusercontent.com/{AZURE_SENTINEL_REPO}"
GITHUB_BLOB = f"https://github.com/{AZURE_SENTINEL_REPO}/blob"
ASIM_SCHEMA_ROOT = "ASIM/schemas"
HTTP_HEADERS = {
    "User-Agent": "tenzir-microsoft-asim-generator",
    "Accept": "application/vnd.github+json",
}
LEARN_LINKS = {
    "content": "https://learn.microsoft.com/en-us/azure/sentinel/normalization-content",
    "schemas": "https://learn.microsoft.com/en-us/azure/sentinel/normalization-about-schemas",
    "common_fields": "https://learn.microsoft.com/en-us/azure/sentinel/normalization-common-fields",
}
SCHEMA_PURPOSES = {
    "AuditEvent": "Administrative, configuration, policy, and resource audit activity.",
    "Authentication": "Logon, logoff, elevation, and other authentication session activity.",
    "Dhcp": "DHCP lease, assignment, renewal, and address allocation activity.",
    "Dns": "DNS query and response activity.",
    "FileEvent": "File creation, deletion, modification, access, and inspection activity.",
    "Notification": "Notification and message delivery activity.",
    "ProcessEvent": "Process creation, termination, injection, and related process activity.",
    "RegistryEvent": "Windows registry key and value activity.",
    "User Management": "User and group creation, deletion, modification, and membership activity.",
}


@dataclass(frozen=True, slots=True)
class SourceRef:
    ref: str
    sha: str


@dataclass(frozen=True, slots=True)
class IncludeSpec:
    name: str
    file: str
    role: str | None = None


@dataclass(frozen=True, slots=True)
class FieldOrigin:
    source_path: str
    include_name: str | None = None
    role: str | None = None
    inherited: bool = False


@dataclass(frozen=True, slots=True)
class FieldRecord:
    name: str
    attrs: dict[str, Any]
    origin: FieldOrigin


@dataclass(slots=True)
class ResolvedField:
    name: str
    attrs: dict[str, Any]
    origins: list[FieldOrigin] = field(default_factory=list)


@dataclass(frozen=True, slots=True)
class EnumValue:
    value: str
    description: str = ""
    examples: tuple[str, ...] = ()
    link: str = ""


@dataclass(frozen=True, slots=True)
class Enumeration:
    name: str
    source_path: str
    values: tuple[EnumValue, ...]


@dataclass(frozen=True, slots=True)
class SourceFile:
    path: str
    kind: str
    data: dict[str, Any]
    fields: tuple[FieldRecord, ...]
    enumerations: tuple[Enumeration, ...]


@dataclass(slots=True)
class SchemaDoc:
    source: SourceFile
    name: str
    version: str
    last_updated: str
    references: tuple[Any, ...]
    includes: tuple[IncludeSpec, ...]
    fields: tuple[ResolvedField, ...]


@dataclass(slots=True)
class AsimReference:
    source: SourceRef
    files: dict[str, SourceFile]
    schemas: tuple[SchemaDoc, ...]
    enumerations: tuple[Enumeration, ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--ref",
        default="master",
        help="Azure/Azure-Sentinel ref to build from (default: master)",
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


def blob_url(sha: str, path: str) -> str:
    return f"{GITHUB_BLOB}/{sha}/{path}"


def fetch_asim_yaml_paths(client: httpx.Client, source: SourceRef) -> list[str]:
    response = client.get(f"{GITHUB_API}/git/trees/{source.sha}", params={"recursive": "1"})
    response.raise_for_status()
    data = response.json()
    paths: list[str] = []
    for item in data.get("tree", []):
        path = item.get("path")
        if not isinstance(path, str):
            continue
        if not path.startswith(f"{ASIM_SCHEMA_ROOT}/"):
            continue
        if re.search(r"\.ya?ml$", path, flags=re.IGNORECASE):
            paths.append(path)
    return sorted(paths)


def fetch_yaml_files(client: httpx.Client, source: SourceRef) -> dict[str, dict[str, Any]]:
    files: dict[str, dict[str, Any]] = {}
    for path in fetch_asim_yaml_paths(client, source):
        response = client.get(raw_url(source.sha, path))
        response.raise_for_status()
        loaded = yaml.safe_load(response.text) or {}
        if not isinstance(loaded, dict):
            loaded = {}
        files[path] = loaded
    return files


def classify_path(path: str) -> str:
    if path.startswith(f"{ASIM_SCHEMA_ROOT}/common/"):
        return "common"
    if path.startswith(f"{ASIM_SCHEMA_ROOT}/entities/"):
        return "entity"
    if path.startswith(f"{ASIM_SCHEMA_ROOT}/"):
        return "schema"
    return "other"


def to_str(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def to_slug(value: str) -> str:
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    return value.strip("_").lower() or "index"


def schema_slug(schema_name: str) -> str:
    return to_slug(schema_name.replace("DHCP", "Dhcp"))


def field_slug(field_name: str) -> str:
    return to_slug(field_name)


def fragment_slug(path: str) -> str:
    stem = Path(path).stem
    return to_slug(stem.removeprefix("ASim"))


def normalize_include_path(path: str) -> str:
    if path.startswith(f"{ASIM_SCHEMA_ROOT}/"):
        return path
    return f"{ASIM_SCHEMA_ROOT}/{path}"


def clean_markdown(text: str) -> str:
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def escape_table(value: Any) -> str:
    text = to_str(value).replace("\n", "<br>")
    return text.replace("|", "\\|")


def inline_code(value: Any) -> str:
    return f"`{to_str(value)}`" if to_str(value) else ""


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def as_text_list(value: Any) -> list[str]:
    return [to_str(item) for item in as_list(value) if to_str(item)]


def first_present(mapping: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        if key in mapping:
            return mapping[key]
    return None


def substitute_role(value: Any, role: str | None) -> Any:
    role_prefix = role or ""
    if isinstance(value, str):
        return value.replace("<<Role>>", role_prefix).replace("<<role>>", role_prefix)
    if isinstance(value, list):
        return [substitute_role(item, role) for item in value]
    if isinstance(value, dict):
        return {
            substitute_role(key, role) if isinstance(key, str) else key: substitute_role(item, role)
            for key, item in value.items()
        }
    return value


def field_applies_to_role(attrs: dict[str, Any], role: str | None) -> bool:
    roles = as_text_list(attrs.get("For roles"))
    if not roles:
        return True
    return role in roles if role else False


def parse_field(data: Any, origin: FieldOrigin) -> FieldRecord | None:
    if not isinstance(data, dict):
        return None
    name = to_str(data.get("Name"))
    if not name:
        return None
    attrs = {key: value for key, value in data.items() if key != "Name"}
    return FieldRecord(name=name, attrs=attrs, origin=origin)


def normalize_enum_value(value: Any) -> EnumValue | None:
    if isinstance(value, str):
        return EnumValue(value=value)
    if not isinstance(value, dict):
        return None
    name = first_present(value, "Name", "Value")
    link = to_str(value.get("Link"))
    if name is None and link:
        name = link
    if name is None:
        return None
    examples = tuple(
        to_str(item)
        for item in as_list(first_present(value, "Examples", "Example", "example"))
        if to_str(item)
    )
    return EnumValue(
        value=to_str(name),
        description=to_str(value.get("Description")),
        examples=examples,
        link=link,
    )


def parse_enumerations(data: dict[str, Any], source_path: str) -> tuple[Enumeration, ...]:
    enumerations = data.get("Enumerations") or {}
    if not isinstance(enumerations, dict):
        return ()
    result: list[Enumeration] = []
    for name, values in sorted(enumerations.items(), key=lambda item: to_str(item[0]).casefold()):
        normalized = [
            enum_value
            for enum_value in (normalize_enum_value(item) for item in as_list(values))
            if enum_value is not None
        ]
        result.append(Enumeration(to_str(name), source_path, tuple(normalized)))
    return tuple(result)


def parse_source_files(raw_files: dict[str, dict[str, Any]], source: SourceRef) -> AsimReference:
    files: dict[str, SourceFile] = {}
    for path, data in sorted(raw_files.items()):
        origin = FieldOrigin(source_path=path)
        fields = tuple(
            field
            for field in (parse_field(item, origin) for item in as_list(data.get("Fields")))
            if field is not None
        )
        files[path] = SourceFile(
            path=path,
            kind=classify_path(path),
            data=data,
            fields=fields,
            enumerations=parse_enumerations(data, path),
        )

    schemas = tuple(
        build_schema_doc(source_file, files)
        for source_file in files.values()
        if source_file.kind == "schema"
    )
    enumerations = tuple(
        enumeration
        for source_file in files.values()
        for enumeration in source_file.enumerations
    )
    return AsimReference(source=source, files=files, schemas=schemas, enumerations=enumerations)


def parse_includes(data: dict[str, Any]) -> tuple[IncludeSpec, ...]:
    includes: list[IncludeSpec] = []
    for item in as_list(data.get("Include")):
        if not isinstance(item, dict):
            continue
        file_name = to_str(item.get("File"))
        if not file_name:
            continue
        includes.append(
            IncludeSpec(
                name=to_str(item.get("Name")) or file_name,
                file=normalize_include_path(file_name),
                role=to_str(item.get("Role")) or None,
            )
        )
    return tuple(includes)


def build_schema_doc(source_file: SourceFile, files: dict[str, SourceFile]) -> SchemaDoc:
    schema_meta = source_file.data.get("Schema") or {}
    if not isinstance(schema_meta, dict):
        schema_meta = {}
    includes = parse_includes(source_file.data)
    resolved: dict[str, ResolvedField] = {}

    def apply_field(record: FieldRecord, origin: FieldOrigin) -> None:
        attrs = substitute_role(record.attrs, origin.role)
        if not isinstance(attrs, dict):
            return
        if origin.inherited and not field_applies_to_role(attrs, origin.role):
            return
        name = to_str(substitute_role(record.name, origin.role))
        if not name:
            return
        if name in resolved:
            merged = dict(resolved[name].attrs)
            merged.update(attrs)
            resolved[name].attrs = merged
            resolved[name].origins.append(origin)
        else:
            resolved[name] = ResolvedField(name=name, attrs=dict(attrs), origins=[origin])

    for include in includes:
        included_file = files.get(include.file)
        if included_file is None:
            continue
        for record in included_file.fields:
            apply_field(
                record,
                FieldOrigin(
                    source_path=included_file.path,
                    include_name=include.name,
                    role=include.role,
                    inherited=True,
                ),
            )

    for record in source_file.fields:
        apply_field(record, FieldOrigin(source_path=source_file.path, inherited=False))

    return SchemaDoc(
        source=source_file,
        name=to_str(schema_meta.get("Schema")) or Path(source_file.path).stem,
        version=to_str(schema_meta.get("Version")),
        last_updated=to_str(schema_meta.get("Last Updated")),
        references=tuple(as_list(source_file.data.get("References"))),
        includes=includes,
        fields=tuple(sorted(resolved.values(), key=lambda item: item.name.casefold())),
    )


def schema_by_name(reference: AsimReference) -> dict[str, SchemaDoc]:
    return {schema.name: schema for schema in reference.schemas}


def enum_by_name(reference: AsimReference) -> dict[str, Enumeration]:
    return {enumeration.name: enumeration for enumeration in reference.enumerations}


def schema_link(schema: SchemaDoc, *, prefix: str = "") -> str:
    return f"[{schema.name}]({prefix}schemas/{schema_slug(schema.name)}.md)"


def field_link(name: str, *, prefix: str = "") -> str:
    return f"[`{name}`]({prefix}fields/{field_slug(name)}.md)"


def enum_link(name: str, *, prefix: str = "") -> str:
    return f"[{name}]({prefix}enumerations/{to_slug(name)}.md)"


def render_reference(value: Any) -> str:
    if isinstance(value, dict):
        title = to_str(value.get("Title")) or to_str(value.get("Link")) or "Reference"
        link = to_str(value.get("Link"))
        if link:
            return f"[{title}]({link})"
        return title
    text = to_str(value)
    if text.startswith(("http://", "https://")):
        return f"[{text}]({text})"
    return text


def format_meta(entries: list[tuple[str, Any]]) -> str:
    lines = [
        f"- **{label}**: {value}"
        for label, value in entries
        if value not in (None, "", [], ())
    ]
    return "\n".join(lines)


def list_values(value: Any) -> str:
    if isinstance(value, list):
        return ", ".join(f"`{to_str(item)}`" for item in value)
    if to_str(value):
        return inline_code(value)
    return ""


def format_list_of_values(value: Any, reference: AsimReference, *, prefix: str = "") -> str:
    if isinstance(value, list):
        return ", ".join(format_value_link(to_str(item), reference, prefix=prefix) for item in value)
    text = to_str(value)
    if not text:
        return ""
    if text in enum_by_name(reference):
        return enum_link(text, prefix=prefix)
    return inline_code(text)


def format_value_link(value: str, reference: AsimReference, *, prefix: str = "") -> str:
    schemas = schema_by_name(reference)
    if value in schemas:
        return schema_link(schemas[value], prefix=prefix)
    return f"`{value}`"


def aliases_for_field(attrs: dict[str, Any], reference: AsimReference, *, prefix: str = "") -> str:
    aliases = as_text_list(attrs.get("Aliases"))
    if not aliases:
        return ""
    field_names = collect_field_names(reference)
    rendered: list[str] = []
    for alias in aliases:
        rendered.append(field_link(alias, prefix=prefix) if alias in field_names else f"`{alias}`")
    return ", ".join(rendered)


def follows_for_field(attrs: dict[str, Any], reference: AsimReference, *, prefix: str = "") -> str:
    follows = to_str(attrs.get("Follows"))
    if not follows:
        return ""
    return field_link(follows, prefix=prefix) if follows in collect_field_names(reference) else inline_code(follows)


def collect_field_names(reference: AsimReference) -> set[str]:
    names: set[str] = set()
    for schema in reference.schemas:
        names.update(field.name for field in schema.fields)
    for source_file in reference.files.values():
        names.update(field.name for field in source_file.fields)
    return names


def provenance_summary(field: ResolvedField) -> str:
    latest = field.origins[-1] if field.origins else None
    if latest is None:
        return ""
    if latest.inherited:
        parts = ["inherited"]
        if latest.include_name:
            parts.append(f"from {latest.include_name}")
        if latest.role:
            parts.append(f"as {latest.role}")
        return " ".join(parts)
    if len(field.origins) > 1:
        return "local override"
    return "local"


def render_provenance(field: ResolvedField) -> str:
    lines = []
    for origin in field.origins:
        label = "Inherited" if origin.inherited else "Local"
        parts = [f"{label}: `{origin.source_path}`"]
        if origin.include_name:
            parts.append(f"include `{origin.include_name}`")
        if origin.role:
            parts.append(f"role `{origin.role}`")
        lines.append("- " + "; ".join(parts))
    return "\n".join(lines)


def render_field_detail(
    name: str,
    attrs: dict[str, Any],
    reference: AsimReference,
    *,
    prefix: str = "",
    heading_level: int = 3,
    provenance: str = "",
) -> str:
    lines = [f"{'#' * heading_level} `{name}`", ""]
    meta = format_meta(
        [
            ("Class", inline_code(attrs.get("Class"))),
            ("Type", inline_code(attrs.get("Type"))),
            ("Logical type", inline_code(attrs.get("Logical type"))),
            ("List of values", format_list_of_values(attrs.get("List of values"), reference, prefix=prefix)),
            ("Aliases", aliases_for_field(attrs, reference, prefix=prefix)),
            ("Follows", follows_for_field(attrs, reference, prefix=prefix)),
            ("Related to", inline_code(attrs.get("Related to"))),
            ("For roles", list_values(attrs.get("For roles"))),
        ]
    )
    if meta:
        lines.extend([meta, ""])
    if provenance:
        lines.extend(["#### Provenance", "", provenance, ""])
    description = to_str(attrs.get("Description") or attrs.get("DstDescription"))
    if description:
        lines.extend([description.strip(), ""])
    notes = to_str(attrs.get("Notes"))
    if notes:
        lines.extend(["#### Notes", "", notes.strip(), ""])
    examples = as_text_list(first_present(attrs, "Examples", "Example", "example"))
    if examples:
        lines.extend(["#### Examples", ""])
        for example in examples:
            lines.append(f"- `{example}`")
        lines.append("")
    references = as_list(attrs.get("References"))
    if references:
        lines.extend(["#### References", ""])
        for reference_value in references:
            lines.append(f"- {render_reference(reference_value)}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def render_skill_markdown(reference: AsimReference) -> str:
    return clean_markdown(
        "\n".join(
            [
                "---",
                "name: tenzir-microsoft-asim",
                "description: Answer questions about Microsoft Sentinel ASIM (Advanced Security Information Model). Use whenever the user asks about ASIM schemas, normalized Microsoft Sentinel fields, aliases, entities, enumerations, schema mapping, or mapping events into ASIM.",
                "---",
                "",
                "# Microsoft Sentinel ASIM",
                "",
                "Use this generated reference to answer Microsoft Sentinel ASIM schema and",
                "mapping questions. The schema pages are generated from Azure Sentinel ASIM",
                "YAML and are the local source of truth for field names, aliases, entities,",
                "and enumerations. The guidance pages summarize Microsoft Learn semantics.",
                "",
                "Read the relevant generated files before answering. Do not invent fields or",
                "schema behavior that is not present in these files. When Learn guidance and",
                "YAML disagree on field availability, treat the YAML-derived pages as the",
                "schema source of truth and mention the difference if it matters.",
                "",
                "## Source",
                "",
                "- [Source summary](source.md)",
                f"- Requested ref: `{reference.source.ref}`",
                f"- Resolved commit: `{reference.source.sha}`",
                "",
                "## File layout",
                "",
                "```",
                "source.md                         # Source refs, links, and counts",
                "schemas.md                        # Schema index",
                "schemas/{schema}.md               # Resolved schema fields",
                "fields.md                         # Field index",
                "fields/{field}.md                 # Field occurrences and aliases",
                "enumerations.md                   # Enumeration index",
                "enumerations/{enumeration}.md     # Enumeration values",
                "entities.md                       # Entity fragment index",
                "entities/{entity}.md              # Raw entity fragment fields",
                "common.md                         # Common fragment index",
                "common/{fragment}.md              # Raw common fragment fields",
                "guidance.md                       # ASIM mapping guidance index",
                "guidance/{topic}.md               # ASIM semantics and mapping guidance",
                "```",
                "",
                "## Question routing",
                "",
                "| Question pattern | Start here |",
                "| --- | --- |",
                "| Which ASIM schema should I map this event to? | [Schema semantics](guidance/schema-semantics.md) -> [Schemas](schemas.md) -> candidate schema pages |",
                "| What fields does schema X contain? | [Schemas](schemas.md) -> specific schema page |",
                "| What does field X mean? | [Fields](fields.md) -> specific field page |",
                "| Which field should an alias use? | [Fields](fields.md), then alias and target field pages |",
                "| How do user/device/process roles map? | [Schema semantics](guidance/schema-semantics.md) and [Entities](entities.md) |",
                "| Which enum values are allowed? | [Enumerations](enumerations.md) -> specific enumeration page |",
                "| What normalized content uses ASIM? | [Security content](guidance/security-content.md) |",
                "",
                "When advising on mappings, prefer the normalized field over an alias for",
                "reusable detections, rules, and workbooks. Use aliases mainly to explain",
                "interactive query convenience.",
                "",
            ]
        )
    )


def render_source_page(reference: AsimReference) -> str:
    common_files = [file for file in reference.files.values() if file.kind == "common"]
    entity_files = [file for file in reference.files.values() if file.kind == "entity"]
    resolved_field_count = sum(len(schema.fields) for schema in reference.schemas)
    alias_count = sum(
        1
        for schema in reference.schemas
        for field in schema.fields
        if to_str(field.attrs.get("Class")).casefold() == "alias"
    )
    distinct_fields = collect_field_names(reference)
    lines = [
        "# Source",
        "",
        "This skill is generated from the Azure Sentinel ASIM YAML files.",
        "",
        f"- **Requested ref**: `{reference.source.ref}`",
        f"- **Resolved commit**: `{reference.source.sha}`",
        f"- **Schema tree**: [{ASIM_SCHEMA_ROOT}]({blob_url(reference.source.sha, ASIM_SCHEMA_ROOT)})",
        f"- **Schemas**: `{len(reference.schemas)}`",
        f"- **Common fragments**: `{len(common_files)}`",
        f"- **Entity fragments**: `{len(entity_files)}`",
        f"- **Distinct fields**: `{len(distinct_fields)}`",
        f"- **Resolved schema field occurrences**: `{resolved_field_count}`",
        f"- **Aliases**: `{alias_count}`",
        f"- **Enumerations**: `{len(reference.enumerations)}`",
        "",
        "The YAML files are the local source of truth for generated schema, field,",
        "alias, entity, and enumeration pages. Microsoft Learn guidance pages in this",
        "skill explain ASIM semantics but do not create additional schema pages.",
        "",
        "## Source files",
        "",
    ]
    for source_file in sorted(reference.files.values(), key=lambda item: item.path):
        lines.append(f"- [{source_file.path}]({blob_url(reference.source.sha, source_file.path)})")
    return clean_markdown("\n".join(lines))


def render_schemas_index(reference: AsimReference) -> str:
    lines = ["# Schemas", ""]
    lines.append(
        "Use this page to choose candidate schemas before opening the full resolved"
        " schema pages."
    )
    lines.append("")
    lines.append("| Schema | Use for | Version | Last updated | Fields |")
    lines.append("| --- | --- | --- | --- | ---: |")
    for schema in sorted(reference.schemas, key=lambda item: item.name.casefold()):
        lines.append(
            "| "
            f"{schema_link(schema, prefix='')} | "
            f"{escape_table(SCHEMA_PURPOSES.get(schema.name, 'ASIM events for this schema.'))} | "
            f"`{escape_table(schema.version)}` | "
            f"{escape_table(schema.last_updated)} | "
            f"{len(schema.fields)} |"
        )
    lines.extend(
        [
            "",
            "Only schemas with upstream YAML files are listed here. Microsoft Learn may",
            "document additional ASIM schemas that are not generated in this skill.",
            "",
        ]
    )
    return clean_markdown("\n".join(lines))


def render_schema_page(schema: SchemaDoc, reference: AsimReference) -> str:
    lines = [f"# {schema.name}", ""]
    meta = format_meta(
        [
            ("Version", inline_code(schema.version)),
            ("Last updated", schema.last_updated),
            ("Source", f"[`{schema.source.path}`]({blob_url(reference.source.sha, schema.source.path)})"),
            ("Fields", inline_code(len(schema.fields))),
        ]
    )
    if meta:
        lines.extend([meta, ""])
    if schema.references:
        lines.extend(["## References", ""])
        for reference_value in schema.references:
            lines.append(f"- {render_reference(reference_value)}")
        lines.append("")
    if schema.includes:
        lines.extend(["## Includes", ""])
        lines.append("| Include | File | Role |")
        lines.append("| --- | --- | --- |")
        for include in schema.includes:
            lines.append(
                "| "
                f"{escape_table(include.name)} | "
                f"`{include.file}` | "
                f"{inline_code(include.role) if include.role else ''} |"
            )
        lines.append("")
    lines.extend(["## Resolved fields", ""])
    lines.append("| Field | Class | Type | Logical type | Values | Provenance |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for resolved in schema.fields:
        attrs = resolved.attrs
        lines.append(
            "| "
            f"{field_link(resolved.name, prefix='../')} | "
            f"{inline_code(attrs.get('Class'))} | "
            f"{inline_code(attrs.get('Type'))} | "
            f"{inline_code(attrs.get('Logical type'))} | "
            f"{escape_table(format_list_of_values(attrs.get('List of values'), reference, prefix='../'))} | "
            f"{escape_table(provenance_summary(resolved))} |"
        )
    lines.extend(["", "## Fields", ""])
    for resolved in schema.fields:
        lines.append(
            render_field_detail(
                resolved.name,
                resolved.attrs,
                reference,
                prefix="../",
                provenance=render_provenance(resolved),
            )
        )
    return clean_markdown("\n".join(lines))


def field_occurrences(reference: AsimReference) -> dict[str, list[tuple[SchemaDoc, ResolvedField]]]:
    occurrences: dict[str, list[tuple[SchemaDoc, ResolvedField]]] = {}
    for schema in reference.schemas:
        for resolved in schema.fields:
            occurrences.setdefault(resolved.name, []).append((schema, resolved))
    return occurrences


def raw_field_occurrences(reference: AsimReference) -> dict[str, list[tuple[SourceFile, FieldRecord]]]:
    occurrences: dict[str, list[tuple[SourceFile, FieldRecord]]] = {}
    for source_file in reference.files.values():
        for record in source_file.fields:
            occurrences.setdefault(record.name, []).append((source_file, record))
    return occurrences


def render_fields_index(reference: AsimReference) -> str:
    occurrences = field_occurrences(reference)
    lines = ["# Fields", ""]
    for name in sorted(occurrences, key=str.casefold):
        schema_list = ", ".join(schema_link(schema) for schema, _ in occurrences[name])
        lines.append(f"- {field_link(name)} ({len(occurrences[name])} schemas): {schema_list}")
    return clean_markdown("\n".join(lines))


def render_field_page(
    name: str,
    occurrences: list[tuple[SchemaDoc, ResolvedField]],
    raw_occurrences: list[tuple[SourceFile, FieldRecord]],
    reference: AsimReference,
) -> str:
    lines = [f"# `{name}`", ""]
    lines.append(f"- **Schema occurrences**: `{len(occurrences)}`")
    if raw_occurrences:
        lines.append(f"- **Raw fragment/source occurrences**: `{len(raw_occurrences)}`")
    lines.append("")
    if occurrences:
        lines.extend(["## Schema occurrences", ""])
        lines.append("| Schema | Class | Type | Logical type | Values | Provenance |")
        lines.append("| --- | --- | --- | --- | --- | --- |")
        for schema, resolved in sorted(occurrences, key=lambda item: item[0].name.casefold()):
            attrs = resolved.attrs
            lines.append(
                "| "
                f"{schema_link(schema, prefix='../')} | "
                f"{inline_code(attrs.get('Class'))} | "
                f"{inline_code(attrs.get('Type'))} | "
                f"{inline_code(attrs.get('Logical type'))} | "
                f"{escape_table(format_list_of_values(attrs.get('List of values'), reference, prefix='../'))} | "
                f"{escape_table(provenance_summary(resolved))} |"
            )
        lines.append("")
    if raw_occurrences:
        lines.extend(["## Raw sources", ""])
        for source_file, record in sorted(raw_occurrences, key=lambda item: item[0].path):
            lines.append(f"- `{source_file.path}`")
        lines.append("")
    lines.extend(["## Details by schema", ""])
    for schema, resolved in sorted(occurrences, key=lambda item: item[0].name.casefold()):
        lines.append(f"### {schema.name}")
        lines.append("")
        lines.append(
            render_field_detail(
                name,
                resolved.attrs,
                reference,
                prefix="../",
                heading_level=4,
                provenance=render_provenance(resolved),
            )
        )
    return clean_markdown("\n".join(lines))


def render_enumerations_index(reference: AsimReference) -> str:
    field_refs = fields_by_enumeration(reference)
    lines = ["# Enumerations", ""]
    lines.append("| Enumeration | Values | Referenced by fields | Source |")
    lines.append("| --- | ---: | --- | --- |")
    for enumeration in sorted(reference.enumerations, key=lambda item: item.name.casefold()):
        refs = field_refs.get(enumeration.name, set())
        rendered_refs = ", ".join(field_link(name) for name in sorted(refs, key=str.casefold))
        lines.append(
            "| "
            f"{enum_link(enumeration.name)} | "
            f"{len(enumeration.values)} | "
            f"{rendered_refs} | "
            f"`{enumeration.source_path}` |"
        )
    return clean_markdown("\n".join(lines))


def fields_by_enumeration(reference: AsimReference) -> dict[str, set[str]]:
    enum_names = set(enum_by_name(reference))
    result: dict[str, set[str]] = {}
    for schema in reference.schemas:
        for resolved in schema.fields:
            values = resolved.attrs.get("List of values")
            if isinstance(values, str) and values in enum_names:
                result.setdefault(values, set()).add(resolved.name)
    return result


def render_enumeration_page(enumeration: Enumeration, reference: AsimReference) -> str:
    field_refs = fields_by_enumeration(reference).get(enumeration.name, set())
    lines = [f"# {enumeration.name}", ""]
    lines.append(f"- **Source**: [`{enumeration.source_path}`]({blob_url(reference.source.sha, enumeration.source_path)})")
    lines.append(f"- **Values**: `{len(enumeration.values)}`")
    if field_refs:
        fields = ", ".join(field_link(name, prefix="../") for name in sorted(field_refs, key=str.casefold))
        lines.append(f"- **Referenced by fields**: {fields}")
    lines.append("")
    if enumeration.values:
        lines.extend(["## Values", ""])
        lines.append("| Value | Description | Examples | Link |")
        lines.append("| --- | --- | --- | --- |")
        for value in enumeration.values:
            rendered_value = format_value_link(value.value, reference, prefix="../")
            examples = ", ".join(f"`{example}`" for example in value.examples)
            link = f"[source]({value.link})" if value.link else ""
            lines.append(
                "| "
                f"{rendered_value} | "
                f"{escape_table(value.description)} | "
                f"{escape_table(examples)} | "
                f"{link} |"
            )
    return clean_markdown("\n".join(lines))


def source_files_by_kind(reference: AsimReference, kind: str) -> list[SourceFile]:
    return sorted(
        (source_file for source_file in reference.files.values() if source_file.kind == kind),
        key=lambda item: fragment_slug(item.path),
    )


def schemas_including(reference: AsimReference, source_path: str) -> list[tuple[SchemaDoc, IncludeSpec]]:
    result: list[tuple[SchemaDoc, IncludeSpec]] = []
    for schema in reference.schemas:
        for include in schema.includes:
            if include.file == source_path:
                result.append((schema, include))
    return result


def render_fragment_index(reference: AsimReference, kind: str) -> str:
    title = "Entities" if kind == "entity" else "Common Fragments"
    section = "entities" if kind == "entity" else "common"
    lines = [f"# {title}", ""]
    for source_file in source_files_by_kind(reference, kind):
        includes = schemas_including(reference, source_file.path)
        include_count = len(includes)
        lines.append(
            f"- [{Path(source_file.path).stem}]({section}/{fragment_slug(source_file.path)}.md)"
            f" ({len(source_file.fields)} fields, included by {include_count} schemas)"
        )
    return clean_markdown("\n".join(lines))


def render_fragment_page(source_file: SourceFile, reference: AsimReference) -> str:
    title = Path(source_file.path).stem
    lines = [f"# {title}", ""]
    lines.append(f"- **Source**: [`{source_file.path}`]({blob_url(reference.source.sha, source_file.path)})")
    lines.append(f"- **Fields**: `{len(source_file.fields)}`")
    lines.append("")
    references = as_list(source_file.data.get("References"))
    if references:
        lines.extend(["## References", ""])
        for reference_value in references:
            lines.append(f"- {render_reference(reference_value)}")
        lines.append("")
    includes = schemas_including(reference, source_file.path)
    if includes:
        lines.extend(["## Included by", ""])
        for schema, include in includes:
            role = f" as `{include.role}`" if include.role else ""
            lines.append(f"- {schema_link(schema, prefix='../')}{role}")
        lines.append("")
    lines.extend(["## Raw fields", ""])
    for record in sorted(source_file.fields, key=lambda item: item.name.casefold()):
        lines.append(
            render_field_detail(
                record.name,
                record.attrs,
                reference,
                prefix="../",
                heading_level=3,
            )
        )
    return clean_markdown("\n".join(lines))


def render_guidance_index() -> str:
    return clean_markdown(
        "\n".join(
            [
                "# Guidance",
                "",
                "These pages summarize ASIM concepts and best practices from Microsoft Learn.",
                "Use them for mapping semantics, while using the generated",
                "schema pages as the source of truth for fields and enumerations.",
                "",
                "- [Schema semantics](guidance/schema-semantics.md)",
                "- [Common fields](guidance/common-fields.md)",
                "- [Security content](guidance/security-content.md)",
                "",
            ]
        )
    )


def render_schema_semantics_guidance(reference: AsimReference) -> str:
    return clean_markdown(
        "\n".join(
            [
                "# Schema Semantics",
                "",
                f"Source: [Advanced Security Information Model schemas]({LEARN_LINKS['schemas']}).",
                "",
                "ASIM schemas model activities and entities with a consistent set of field",
                "names. Start a mapping by identifying the activity type, then inspect the",
                "candidate generated schema pages for mandatory and recommended fields.",
                "",
                "## Field classes",
                "",
                "- `Mandatory` fields are expected in normalized events for that schema.",
                "- `Recommended` fields should be normalized when the source provides them.",
                "- `Optional` fields can remain unnormalized when they are not needed.",
                "- `Conditional` fields become required when the field they follow is populated.",
                "- `Alias` fields are conditional convenience fields for analyst queries.",
                "",
                "## Entities and roles",
                "",
                "ASIM represents users, devices, processes, applications, and similar objects",
                "with repeatable entity field sets. When a record has multiple entities of the",
                "same type, role prefixes such as `Src`, `Dst`, `Actor`, `Acting`, `Target`,",
                "and `Parent` identify which entity the field describes.",
                "",
                "When a source has entity identifiers that do not map to normalized fields,",
                "keep the source value in its original form or place it in `AdditionalFields`.",
                "When a field stores an identifier with multiple possible formats, populate",
                "the matching `Type` field when the schema defines one.",
                "",
                "## Aliases",
                "",
                "Aliases make interactive queries friendlier, but reusable detections,",
                "analytics rules, and workbooks should prefer the aliased normalized field.",
                "",
                "## Logical types",
                "",
                "Logical types document value expectations that Log Analytics does not always",
                "enforce. Examples include enumerated strings, normalized date/time values,",
                "IP addresses, FQDNs, hostnames, hash strings, confidence levels, risk levels,",
                "and schema versions.",
                "",
            ]
        )
    )


def render_common_fields_guidance(reference: AsimReference) -> str:
    return clean_markdown(
        "\n".join(
            [
                "# Common Fields",
                "",
                f"Source: [ASIM common schema fields reference]({LEARN_LINKS['common_fields']}).",
                "",
                "Common fields appear across ASIM schemas. A schema page may override common",
                "field guidance for that schema, such as allowed `EventType` values or the",
                "`EventSchemaVersion` value.",
                "",
                "## Mapping notes",
                "",
                "- Preserve source-specific details that do not map cleanly in `AdditionalFields`.",
                "- Normalize `EventVendor` and `EventProduct` to ASIM's accepted designators",
                "  when possible instead of copying arbitrary source strings.",
                "- Treat common device fields as the shared vocabulary for source, target, and",
                "  reporting systems.",
                "- Use the generated field pages to check whether a common field is mandatory,",
                "  recommended, optional, conditional, or an alias in each schema.",
                "",
                "## Vendor and product values",
                "",
                "ASIM maintains normalized vendor and product names for `EventVendor` and",
                "`EventProduct`. If a mapping targets an unlisted vendor or product, keep the",
                "mapping explicit and expect that the upstream ASIM list may need expansion.",
                "",
                "## Schema updates",
                "",
                "Common fields can change over time and then affect every schema that includes",
                "the common fragments. The generated `source.md` page records the exact Azure",
                "Sentinel commit used for this skill.",
                "",
            ]
        )
    )


def render_security_content_guidance(reference: AsimReference) -> str:
    return clean_markdown(
        "\n".join(
            [
                "# Security Content",
                "",
                f"Source: [ASIM security content]({LEARN_LINKS['content']}).",
                "",
                "Microsoft Sentinel normalized security content includes analytics rules,",
                "hunting queries, and workbooks that use ASIM-normalized fields. This lets",
                "content work across multiple normalized sources instead of one source shape.",
                "",
                "When adapting or writing content, prefer canonical fields over aliases for",
                "reusable detections, analytics rules, and workbooks.",
                "",
                "The Microsoft Learn page lists built-in ASIM-aware content by schema and links",
                "to the current rule or hunting-query sources. This skill links to that page",
                "instead of mirroring its changing rule list.",
                "",
            ]
        )
    )


def build_docs(reference: AsimReference) -> dict[Path, str]:
    docs: dict[Path, str] = {
        Path("SKILL.md"): render_skill_markdown(reference),
        Path("source.md"): render_source_page(reference),
        Path("schemas.md"): render_schemas_index(reference),
        Path("fields.md"): render_fields_index(reference),
        Path("enumerations.md"): render_enumerations_index(reference),
        Path("entities.md"): render_fragment_index(reference, "entity"),
        Path("common.md"): render_fragment_index(reference, "common"),
        Path("guidance.md"): render_guidance_index(),
        Path("guidance/schema-semantics.md"): render_schema_semantics_guidance(reference),
        Path("guidance/common-fields.md"): render_common_fields_guidance(reference),
        Path("guidance/security-content.md"): render_security_content_guidance(reference),
    }

    for schema in reference.schemas:
        docs[Path("schemas") / f"{schema_slug(schema.name)}.md"] = render_schema_page(schema, reference)

    raw_occurrences = raw_field_occurrences(reference)
    for name, occurrences in field_occurrences(reference).items():
        docs[Path("fields") / f"{field_slug(name)}.md"] = render_field_page(
            name,
            occurrences,
            raw_occurrences.get(name, []),
            reference,
        )

    for enumeration in reference.enumerations:
        docs[Path("enumerations") / f"{to_slug(enumeration.name)}.md"] = render_enumeration_page(
            enumeration,
            reference,
        )

    for source_file in source_files_by_kind(reference, "entity"):
        docs[Path("entities") / f"{fragment_slug(source_file.path)}.md"] = render_fragment_page(
            source_file,
            reference,
        )

    for source_file in source_files_by_kind(reference, "common"):
        docs[Path("common") / f"{fragment_slug(source_file.path)}.md"] = render_fragment_page(
            source_file,
            reference,
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
    with httpx.Client(headers=HTTP_HEADERS, follow_redirects=True, timeout=30.0) as client:
        source = resolve_ref(client, args.ref)
        raw_files = fetch_yaml_files(client, source)
    reference = parse_source_files(raw_files, source)
    docs = build_docs(reference)
    write_docs(output_dir, docs)
    print(f"Generated Microsoft ASIM skill in {output_dir}")


if __name__ == "__main__":
    main()
