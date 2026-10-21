#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "httpx>=0.28.0",
#   "markdownify>=1.1.0",
#   "ocsf-schema-compiler==1.1.1",
#   "packaging>=24.0",
#   "pyyaml>=6.0.0",
# ]
# ///

from __future__ import annotations

import argparse
import json
import logging
import re
import shutil
import string
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx
import yaml
from markdownify import markdownify
from ocsf_schema_compiler.compiler import SchemaCompiler
from ocsf_schema_compiler.ocsf_utils import is_hidden_class, is_hidden_object
from packaging.version import Version


OCSF_SCHEMA_REPO = "https://github.com/ocsf/ocsf-schema.git"
OCSF_SCHEMA_RAW = "https://raw.githubusercontent.com/ocsf/ocsf-schema/main"
OCSF_DOCS_API = "https://api.github.com/repos/ocsf/ocsf-docs/contents"
OCSF_DOCS_RAW = "https://raw.githubusercontent.com/ocsf/ocsf-docs/main"
OCSF_COMPILER = "ocsf-schema-compiler 1.1.1"
HTTP_HEADERS = {
    "User-Agent": "tenzir-skills-generator",
    "Accept": "application/json",
}
SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
DEV_VERSION_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)-dev$")
SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z`(\"])")


@dataclass(frozen=True, slots=True)
class VersionSpec:
    version: str
    ref: str
    is_stable: bool


def version_to_slug(version: str) -> str:
    return f"v{version}"


def clean_description(text: str) -> str:
    """Convert the HTML fragments in OCSF descriptions to Markdown."""
    if not text:
        return ""
    if re.search(r"</?[A-Za-z][^>]*>", text):
        rendered = markdownify(
            text,
            bullets="-",
            escape_asterisks=False,
            escape_underscores=False,
            strip=["b", "em", "i", "strong"],
        )
    else:
        rendered = text
    rendered = rendered.replace("\r\n", "\n")
    rendered = re.sub(r"\n{3,}", "\n\n", rendered)
    rendered = re.sub(r"[ \t]+$", "", rendered, flags=re.MULTILINE)
    return rendered.strip()


def summarize(text: str) -> str:
    """Return the first sentence of a description on a single line."""
    flat = " ".join(clean_description(text).split())
    match = SENTENCE_END_RE.search(flat)
    return flat[: match.start()] if match else flat


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class _NoAliasSafeDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:
        return True


def _represent_str(dumper: yaml.Dumper, data: str) -> yaml.Node:
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


def _represent_list(dumper: yaml.Dumper, data: list) -> yaml.Node:
    # Lists of names stay on one line so that a grep hit shows all of them.
    flow = bool(data) and all(
        isinstance(item, (int, str)) and "\n" not in str(item) for item in data
    )
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=flow)


class Flow(dict):
    """A mapping written on one line, so that a grep hit shows all of it."""


def _represent_flow(dumper: yaml.Dumper, data: Flow) -> yaml.Node:
    return dumper.represent_mapping("tag:yaml.org,2002:map", data, flow_style=True)


_NoAliasSafeDumper.add_representer(str, _represent_str)
_NoAliasSafeDumper.add_representer(Flow, _represent_flow)
_NoAliasSafeDumper.add_representer(list, _represent_list)


def dump_yaml(data: Any) -> str:
    text = yaml.dump(
        data,
        Dumper=_NoAliasSafeDumper,
        allow_unicode=True,
        sort_keys=False,
        width=1_000_000,
    )
    if yaml.safe_load(text) != data:
        raise ValueError("YAML output does not round-trip to the source data")
    return text


def list_stable_versions() -> list[str]:
    result = subprocess.run(
        ["git", "ls-remote", "--tags", OCSF_SCHEMA_REPO],
        check=True,
        capture_output=True,
        text=True,
    )
    versions: set[str] = set()
    for line in result.stdout.splitlines():
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        ref = parts[1]
        if ref.endswith("^{}"):
            continue
        match = re.match(r"^refs/tags/v?(\d+\.\d+\.\d+)$", ref)
        if match and Version(match.group(1)).major >= 1:
            versions.add(match.group(1))
    return [str(version) for version in sorted((Version(version) for version in versions))]


def clone_schema(version: str, ref: str, temp_root: Path) -> tuple[Path, str]:
    """Clone the schema at `ref` and return the checkout and the ref used."""
    repo_dir = temp_root / f"ocsf-schema-{version}"
    refs = [ref]
    if ref == version:
        refs.insert(0, f"v{version}")
    for candidate in refs:
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", "--branch", candidate, OCSF_SCHEMA_REPO, str(repo_dir)],
                check=True,
                capture_output=True,
                text=True,
            )
            return repo_dir, candidate
        except subprocess.CalledProcessError:
            pass
    raise RuntimeError(f"Failed to clone OCSF schema for version {version} from ref {ref}")


def resolve_commit(repo_dir: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo_dir), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def parse_semver_triplet(version: str) -> tuple[int, int, int]:
    match = SEMVER_RE.fullmatch(version)
    if not match:
        raise ValueError(f"Unsupported stable version format: {version}")
    return tuple(int(part) for part in match.groups())


def fetch_latest_dev_version(client: httpx.Client) -> str | None:
    response = client.get(f"{OCSF_SCHEMA_RAW}/version.json")
    response.raise_for_status()
    version = response.json().get("version")
    if not isinstance(version, str):
        return None
    return version if DEV_VERSION_RE.fullmatch(version) else None


def collect_version_specs(client: httpx.Client, requested_version: str | None) -> list[VersionSpec]:
    if requested_version:
        if requested_version.endswith("-dev"):
            if not DEV_VERSION_RE.fullmatch(requested_version):
                raise ValueError(f"Unsupported development version format: {requested_version}")
            current_dev_version = fetch_latest_dev_version(client)
            if current_dev_version != requested_version:
                current_label = current_dev_version or "no development snapshot"
                raise ValueError(
                    "Requested development version "
                    f"{requested_version} does not match the version published from main "
                    f"({current_label})"
                )
            return [VersionSpec(version=requested_version, ref="main", is_stable=False)]
        return [VersionSpec(version=requested_version, ref=requested_version, is_stable=True)]

    stable_versions = list_stable_versions()
    specs = [
        VersionSpec(version=version, ref=version, is_stable=True)
        for version in stable_versions
    ]

    dev_version = fetch_latest_dev_version(client)
    if dev_version:
        dev_triplet = tuple(int(part) for part in DEV_VERSION_RE.fullmatch(dev_version).groups())
        latest_stable_triplet = parse_semver_triplet(stable_versions[-1])
        if dev_triplet >= latest_stable_triplet:
            specs.append(VersionSpec(version=dev_version, ref="main", is_stable=False))

    return specs


def load_directory_json(directory: Path) -> dict[str, dict]:
    """Load all JSON files in a directory, keyed by the item's schema name.
    Extension patches have no `name` and are keyed by the item they extend."""
    if not directory.exists():
        return {}
    result: dict[str, dict] = {}
    for path in sorted(directory.glob("*.json")):
        if not path.is_file():
            continue
        data = read_json(path)
        result[data.get("name") or data.get("extends") or path.stem] = data
    return result


def load_extensions(schema_dir: Path) -> dict[str, dict]:
    """Load the raw extension definitions, keyed by the extension's scope name
    (e.g. `win`), which prefixes the names of its classes and objects."""
    result: dict[str, dict] = {}
    extensions_dir = schema_dir / "extensions"
    if not extensions_dir.exists():
        return result

    for extension_dir in sorted(path for path in extensions_dir.iterdir() if path.is_dir()):
        meta_path = extension_dir / "extension.json"
        if not meta_path.exists():
            continue
        meta = read_json(meta_path)
        result[meta.get("name") or extension_dir.name] = {
            "meta": meta,
            "classes": load_directory_json(extension_dir / "events"),
            "objects": load_directory_json(extension_dir / "objects"),
            "profiles": load_directory_json(extension_dir / "profiles"),
        }
    return result


class _SkillSchemaCompiler(SchemaCompiler):
    """Schema compiler that also keeps the hidden (abstract) classes and
    objects, such as `system` or `_entity`, which the compiler resolves but
    drops from its output. The skill documents them as abstract items."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._hidden_classes: dict = {}
        self._hidden_objects: dict = {}

    def _resolve_extends(self, items: dict, kind: str) -> None:
        super()._resolve_extends(items, kind)
        for name, item in items.items():
            if kind == "Class" and is_hidden_class(name, item):
                self._hidden_classes[name] = item
            elif kind == "Object" and is_hidden_object(name):
                self._hidden_objects[name] = item

    def compile(self) -> dict:
        output = super().compile()
        for hidden, kind, key in (
            (self._hidden_classes, "class", "classes"),
            (self._hidden_objects, "object", "objects"),
        ):
            self._ensure_item_attributes_have_requirement(hidden, kind, [])
            self._finish_item_attributes(hidden, kind)
            output[key].update(hidden)
        return output


def compile_schema(schema_dir: Path, *, ignore_platform_extensions: bool) -> dict:
    """Compile a raw OCSF schema checkout with the official OCSF schema
    compiler in browser mode, which records each attribute's `_source` and
    the back-references between items in `_links`."""
    logging.getLogger("ocsf_schema_compiler").setLevel(logging.ERROR)
    return _SkillSchemaCompiler(
        schema_dir,
        ignore_platform_extensions=ignore_platform_extensions,
        browser_mode=True,
    ).compile()


# Semantic grouping for the objects index.  Each entry maps a group
# name to a set of object names.  Objects not listed land in "Other".
_OBJECT_GROUPS: list[tuple[str, set[str]]] = [
    ("Base", {
        "object", "_entity", "_resource",
    }),
    ("Network", {
        "_dns", "dns_answer", "dns_query", "endpoint", "endpoint_connection",
        "network_endpoint", "network_proxy", "network_connection_info",
        "network_interface", "network_traffic", "autonomous_system", "hassh",
        "http_cookie", "http_header", "http_request", "http_response",
        "ja4_fingerprint", "load_balancer", "tls", "tls_extension", "url",
        "dce_rpc", "rpc_interface", "port_info",
    }),
    ("Identity & Access", {
        "account", "actor", "auth_factor", "authentication_token",
        "authorization", "group", "idp", "ldap_person", "scim", "session",
        "sso", "user", "identity_activity_metrics", "programmatic_credential",
    }),
    ("Device & Host", {
        "agent", "device", "device_hw_info", "display", "keyboard_info",
        "os", "peripheral_device", "container", "image", "kernel",
        "kernel_driver",
    }),
    ("Process & Module", {
        "process", "process_entity", "module", "script", "service",
        "startup_item", "environment_variable", "function_invocation",
        "parameter",
    }),
    ("File & Data", {
        "file", "fingerprint", "digital_signature", "database", "databucket",
        "table", "web_resource", "data_classification", "data_security",
        "encryption_details", "sbom", "software_component", "package",
        "affected_code", "affected_package",
    }),
    ("Threat Intelligence", {
        "attack", "campaign", "cve", "cvss", "cwe", "epss", "kill_chain_phase",
        "malware", "malware_scan_info", "osint", "reputation", "sub_technique",
        "tactic", "technique", "threat_actor", "vulnerability", "d3fend",
        "d3f_tactic", "d3f_technique", "mitigation",
    }),
    ("Findings & Compliance", {
        "analytic", "anomaly", "anomaly_analysis", "assessment", "baseline",
        "check", "cis_benchmark", "cis_benchmark_result", "cis_control",
        "cis_csc", "compliance", "evidences", "finding", "finding_info",
        "observation", "remediation", "rule", "firewall_rule", "policy",
        "security_state", "access_analysis_result", "permission_analysis_result",
    }),
    ("Email", {
        "email", "email_auth",
    }),
    ("Cloud & Resources", {
        "cloud", "resource_details", "managed_entity",
    }),
    ("Metadata & Context", {
        "api", "application", "classifier_details", "enrichment", "extension",
        "feature", "key_value_object", "logger", "long_string", "metadata",
        "metric", "observable", "occurrence_details", "organization",
        "product", "query_info", "query_evidence", "related_event", "request",
        "response", "span", "trace", "ticket", "vendor_attributes",
        "transformation_info", "reporter",
    }),
    ("Location & Geography", {
        "location", "domain_contact", "whois", "san", "certificate",
    }),
    ("Unmanned Systems", {
        "aircraft", "unmanned_aerial_system", "unmanned_system_operating_area",
    }),
    ("Discovery", {
        "analysis_target", "discovery_details", "graph", "edge", "node",
        "trait", "kb_article", "job",
    }),
]


def object_group(name: str) -> str:
    base = name.split("/", 1)[-1]
    return next((title for title, names in _OBJECT_GROUPS if base in names), "Other")


def entity_path(slug: str, section: str, name: str, *, patch_of: str | None = None) -> str:
    """Path of a class or object file relative to the skill root. Scoped
    names (`win/reg_key`) and extension patches live below the extension."""
    if patch_of is not None:
        return f"{slug}/extensions/{patch_of}/{section}/{name}.yaml"
    if "/" in name:
        scope, base = name.split("/", 1)
        return f"{slug}/extensions/{scope}/{section}/{base}.yaml"
    return f"{slug}/{section}/{name}.yaml"


def set_if(out: dict, key: str, value: Any) -> None:
    if value not in (None, "", [], {}):
        out[key] = value


def render_deprecation(deprecation: object) -> dict | None:
    if not isinstance(deprecation, dict):
        return None
    out: dict[str, Any] = {}
    set_if(out, "since", deprecation.get("since"))
    set_if(out, "message", clean_description(deprecation.get("message", "")))
    set_if(out, "superseded_by", list(deprecation.get("superseded_by") or []))
    return out or {"since": None}


def render_references(references: object) -> list[dict]:
    rendered: list[dict] = []
    for reference in references or []:
        entry: dict[str, Any] = {}
        set_if(entry, "description", clean_description(reference.get("description", "")))
        set_if(entry, "url", reference.get("url"))
        if entry:
            rendered.append(entry)
    return rendered


def render_enum(enum: dict) -> dict:
    """Render enum values keyed by value. Numeric values become integer keys,
    as TQL compares them, e.g. `activity_id == 1`."""
    items = list(enum.items())
    if all(re.fullmatch(r"-?\d+", key) for key, _ in items):
        items = sorted(((int(key), value) for key, value in items), key=lambda item: item[0])
    rendered: dict[int | str, dict] = {}
    for key, value in items:
        entry: dict[str, Any] = {"caption": value.get("caption") or str(key)}
        set_if(entry, "description", clean_description(value.get("description", "")))
        set_if(entry, "deprecated", render_deprecation(value.get("@deprecated")))
        set_if(entry, "references", render_references(value.get("references")))
        rendered[key] = entry
    return rendered


def effective_observable(attribute: dict, types: dict, objects: dict) -> int | None:
    """The observable type ID of an attribute: defined on the attribute itself
    (dictionary or class level), or else by its data type or object."""
    if attribute.get("observable") is not None:
        return attribute["observable"]
    observable = (types.get(attribute.get("type") or "") or {}).get("observable")
    if observable is not None:
        return observable
    return (objects.get(attribute.get("object_type") or "") or {}).get("observable")


def render_attribute(attribute: dict, *, owner: str, types: dict, objects: dict) -> dict:
    out: dict[str, Any] = {}
    set_if(out, "caption", attribute.get("caption"))
    set_if(out, "type", attribute.get("type"))
    set_if(out, "object", attribute.get("object_type"))
    if attribute.get("is_array"):
        out["array"] = True
    set_if(out, "requirement", attribute.get("requirement"))
    set_if(out, "group", attribute.get("group"))
    profiles = attribute.get("profiles") or []
    if len(profiles) == 1:
        out["profile"] = profiles[0]
    else:
        set_if(out, "profiles", list(profiles))
    source = attribute.get("_source")
    if source and source != owner:
        out["from"] = source
    set_if(out, "sibling", attribute.get("sibling"))
    set_if(out, "observable", effective_observable(attribute, types, objects))
    set_if(out, "deprecated", render_deprecation(attribute.get("@deprecated")))
    set_if(out, "description", clean_description(attribute.get("description", "")))
    if isinstance(attribute.get("enum"), dict) and attribute["enum"]:
        out["enum"] = render_enum(attribute["enum"])
    set_if(out, "references", render_references(attribute.get("references")))
    return out


def render_links(links: object, *, with_attributes: bool) -> dict:
    """Group compiler back-references (`_links`) by class and object."""
    classes: dict[str, list[str]] = {}
    objects: dict[str, list[str]] = {}
    for link in links or []:
        target = {"class": classes, "object": objects}.get(link.get("group"))
        if target is None:
            continue
        keys = target.setdefault(link["type"], [])
        for key in link.get("attribute_keys") or []:
            if key not in keys:
                keys.append(key)
    out: dict[str, Any] = {}
    for key, entries in (("classes", classes), ("objects", objects)):
        if not entries:
            continue
        names = sorted(entries)
        out[key] = {name: sorted(entries[name]) for name in names} if with_attributes else names
    return out


def item_profiles(item: dict) -> list[str]:
    """Profiles that apply to an item: those registered on it and its
    ancestors, plus those whose attributes the compiler merged in."""
    profiles = list(item.get("profiles") or [])
    for attribute in (item.get("attributes") or {}).values():
        for name in attribute.get("profiles") or []:
            if name not in profiles:
                profiles.append(name)
    return profiles


# Attributes are listed by requirement, so the top of a file is the list of
# attributes every event must set.
REQUIREMENT_ORDER = {"required": 0, "recommended": 1, "optional": 2}


def render_item(
    item: dict,
    *,
    name: str,
    kind: str,
    types: dict,
    objects: dict,
    categories: dict,
    extension: str | None = None,
    patches: str | None = None,
    patched_by: list[str] | None = None,
    attribute_names: list[str] | None = None,
) -> dict:
    """Render a compiled class or object as a self-contained document."""
    out: dict[str, Any] = {"name": name}
    set_if(out, "caption", item.get("caption"))
    abstract = (
        is_hidden_class(name, item) if kind == "class" else is_hidden_object(name)
    ) and patches is None
    if kind == "class" and patches is None:
        set_if(out, "uid", item.get("uid"))
        category = item.get("category")
        if category in categories:
            out["category"] = category
        set_if(out, "category_uid", item.get("category_uid"))
    if abstract:
        out["abstract"] = True
    set_if(out, "extension", extension)
    if patches is not None:
        out["patches"] = patches
    else:
        set_if(out, "extends", item.get("extends"))
    if kind == "object":
        set_if(out, "observable", item.get("observable"))
    set_if(out, "deprecated", render_deprecation(item.get("@deprecated")))
    set_if(
        out,
        "supersedes",
        [
            {key: value for key, value in (("name", entry.get("type")), ("since", entry.get("since"))) if value}
            for entry in item.get("_supersedes") or []
        ],
    )
    set_if(out, "description", clean_description(item.get("description", "")))
    if patches is None:
        set_if(out, "profiles", item_profiles(item))
    set_if(out, "constraints", item.get("constraints"))
    set_if(out, "associations", item.get("associations"))
    set_if(out, "references", render_references(item.get("references")))
    set_if(out, "patched_by", patched_by)
    if kind == "object" and patches is None:
        set_if(out, "referenced_by", render_links(item.get("_links"), with_attributes=True))
    compiled_attributes = item.get("attributes") or {}
    names = attribute_names if attribute_names is not None else list(compiled_attributes)
    names = sorted(
        (attribute_name for attribute_name in names if attribute_name in compiled_attributes),
        key=lambda attribute_name: (
            REQUIREMENT_ORDER.get(compiled_attributes[attribute_name].get("requirement"), len(REQUIREMENT_ORDER)),
            attribute_name,
        ),
    )
    out["attributes"] = {
        attribute_name: render_attribute(
            compiled_attributes[attribute_name],
            owner=name,
            types=types,
            objects=objects,
        )
        for attribute_name in names
    }
    # `type_uid` is `class_uid * 100 + activity_id`; SKILL.md states the rule
    # instead of listing every combination.
    out["attributes"].get("type_uid", {}).pop("enum", None)
    return out


def render_patch(
    raw_patch: dict,
    compiled_item: dict,
    *,
    name: str,
    kind: str,
    scope: str,
    types: dict,
    objects: dict,
    categories: dict,
) -> dict:
    """Render an extension patch: the attributes, profiles, and constraints it
    adds to a core item, resolved against the patched item."""
    profiles = list(raw_patch.get("profiles") or [])
    attribute_names = sorted(
        attribute_name
        for attribute_name, attribute in (compiled_item.get("attributes") or {}).items()
        if attribute_name in (raw_patch.get("attributes") or {})
        or set(attribute.get("profiles") or []) & set(profiles)
    )
    full = render_item(
        compiled_item,
        name=name,
        kind=kind,
        types=types,
        objects=objects,
        categories=categories,
        patches=name,
        attribute_names=attribute_names,
    )
    out: dict[str, Any] = {"name": name}
    set_if(out, "caption", raw_patch.get("caption"))
    out["extension"] = scope
    out["patches"] = name
    set_if(out, "description", clean_description(raw_patch.get("description", "")))
    set_if(out, "profiles", profiles)
    if "constraints" in raw_patch:
        set_if(out, "constraints", compiled_item.get("constraints"))
    out["attributes"] = full["attributes"]
    return out


# Fields in which an inherited attribute may differ from its definition and
# still count as unchanged.
INHERITED_ATTRIBUTE_FIELDS = ("caption", "requirement", "profile", "profiles")
# Larger enums keep one value per line instead of one long flow line.
MAX_FLOW_ENUM_VALUES = 12
INHERITED_ATTRIBUTE_NOTE = (
    "# Attributes with `from` but no description are inherited unchanged. Their\n"
    "# descriptions are in the file of the item that `from` names.\n"
)


def compact_inherited_attributes(documents: dict, slug: str) -> None:
    """Write inherited attributes on one line without their descriptions,
    which the defining item's file holds. An attribute stays complete when
    anything other than its requirement differs from that definition, e.g.
    a narrowed enum."""
    for path, document in documents.items():
        section = "classes" if "/classes/" in path else "objects" if "/objects/" in path else None
        if section is None or "patches" in document:
            continue
        for name, attribute in document["attributes"].items():
            source = attribute.get("from")
            if source is None:
                continue
            defined = documents.get(entity_path(slug, section, source), {}).get("attributes", {}).get(name)
            if defined is None or "from" in defined:
                continue
            rest = {key: value for key, value in attribute.items() if key not in INHERITED_ATTRIBUTE_FIELDS}
            rest.pop("from")
            if rest != {key: value for key, value in defined.items() if key not in INHERITED_ATTRIBUTE_FIELDS}:
                continue
            compact = {
                key: value
                for key, value in attribute.items()
                if key not in ("description", "references", "enum", "from")
            }
            enum = attribute.get("enum")
            if enum:
                captions = {key: value["caption"] for key, value in enum.items()}
                compact["enum"] = Flow(captions) if len(captions) <= MAX_FLOW_ENUM_VALUES else captions
            compact["from"] = source
            if enum and len(enum) > MAX_FLOW_ENUM_VALUES:
                document["attributes"][name] = compact
            else:
                document["attributes"][name] = Flow(compact)


def render_types(compiled_types: dict, *, extension_types: dict) -> dict:
    rendered: dict[str, dict] = {}
    for name, data in sorted({**compiled_types, **extension_types}.items()):
        entry: dict[str, Any] = {}
        set_if(entry, "caption", data.get("caption"))
        set_if(entry, "base", data.get("type"))
        set_if(entry, "extension", data.get("extension"))
        set_if(entry, "max_len", data.get("max_len"))
        set_if(entry, "range", data.get("range"))
        set_if(entry, "regex", data.get("regex"))
        if isinstance(data.get("values"), list):
            entry["values"] = data["values"]
        set_if(entry, "observable", data.get("observable"))
        set_if(entry, "deprecated", render_deprecation(data.get("@deprecated")))
        set_if(entry, "description", clean_description(data.get("description", "")))
        set_if(entry, "references", render_references(data.get("references")))
        rendered[name] = entry
    return rendered


def render_dictionary(attributes: dict, *, types: dict, objects: dict) -> dict:
    rendered: dict[str, dict] = {}
    for name, data in sorted(attributes.items()):
        entry: dict[str, Any] = {}
        set_if(entry, "caption", data.get("caption"))
        set_if(entry, "type", data.get("type"))
        set_if(entry, "object", data.get("object_type"))
        if data.get("is_array"):
            entry["array"] = True
        set_if(entry, "extension", data.get("extension"))
        set_if(entry, "sibling", data.get("sibling"))
        set_if(entry, "observable", effective_observable(data, types, objects))
        set_if(entry, "deprecated", render_deprecation(data.get("@deprecated")))
        set_if(entry, "description", clean_description(data.get("description", "")))
        set_if(entry, "used_by", render_links(data.get("_links"), with_attributes=False))
        rendered[name] = entry
    return rendered


def render_profile(profile: dict, *, name: str, types: dict, objects: dict, extension: str | None) -> dict:
    out: dict[str, Any] = {}
    set_if(out, "caption", profile.get("caption"))
    set_if(out, "extension", extension)
    set_if(out, "deprecated", render_deprecation(profile.get("@deprecated")))
    set_if(out, "description", clean_description(profile.get("description", "")))
    set_if(out, "applies_to", render_links(profile.get("_links"), with_attributes=False))
    out["attributes"] = {
        attribute_name: render_attribute(attribute, owner=name, types=types, objects=objects)
        for attribute_name, attribute in sorted((profile.get("attributes") or {}).items())
    }
    return out


def index_entry(document: dict, *, path: str, extra: dict | None = None) -> dict:
    entry: dict[str, Any] = {"name": document["name"]}
    for key in ("caption", "uid", "category", "abstract", "extension", "extends", "observable"):
        set_if(entry, key, document.get(key))
    entry.update(extra or {})
    if "deprecated" in document:
        entry["deprecated"] = True
    set_if(entry, "summary", summarize(document.get("description", "")))
    if "uid" in document and not document.get("abstract"):
        # Unknown (0) and Other (99) exist in every class.
        enum = document["attributes"].get("activity_id", {}).get("enum", {})
        set_if(
            entry,
            "activities",
            Flow({key: value["caption"] for key, value in enum.items() if key not in (0, 99)}),
        )
    entry["path"] = path
    return entry


def build_version(version: str, schema_dir: Path, *, ref: str, is_stable: bool) -> dict:
    """Render all documents of one schema version, keyed by output path."""
    slug = version_to_slug(version)
    core = compile_schema(schema_dir, ignore_platform_extensions=True)
    full = compile_schema(schema_dir, ignore_platform_extensions=False)
    raw_extensions = load_extensions(schema_dir)
    categories = core["categories"].get("attributes", core["categories"])
    core_types = core["dictionary"]["types"]["attributes"]
    full_types = full["dictionary"]["types"]["attributes"]
    extension_types = {name: data for name, data in full_types.items() if name not in core_types}
    types = {**core_types, **extension_types}

    documents: dict[str, Any] = {}
    class_index: list[dict] = []
    object_index: list[dict] = []
    patched_by: dict[tuple[str, str], list[str]] = {}
    extension_summaries: dict[str, dict] = {}

    # Extension patches modify core items in place, so find them first to
    # mark the patched core items.
    for scope, extension in raw_extensions.items():
        for section in ("classes", "objects"):
            for name, item in extension[section].items():
                if item.get("extends") == name:
                    patched_by.setdefault((section, name), []).append(scope)

    core_objects = core["objects"]
    for section, kind, items, index in (
        ("classes", "class", core["classes"], class_index),
        ("objects", "object", core_objects, object_index),
    ):
        for name, item in items.items():
            document = render_item(
                item,
                name=name,
                kind=kind,
                types=types,
                objects=core_objects,
                categories=categories,
                patched_by=patched_by.get((section, name)),
            )
            path = entity_path(slug, section, name)
            documents[path] = document
            extra = {"group": object_group(name)} if kind == "object" else None
            index.append(index_entry(document, path=path, extra=extra))

    full_objects = full["objects"]
    for scope, extension in raw_extensions.items():
        summary: dict[str, Any] = {}
        meta = extension["meta"]
        set_if(summary, "uid", meta.get("uid"))
        set_if(summary, "caption", meta.get("caption"))
        set_if(summary, "version", meta.get("version"))
        set_if(summary, "description", clean_description(meta.get("description", "")))
        patches: dict[str, list[str]] = {}
        for section, kind, compiled_items, index in (
            ("classes", "class", full["classes"], class_index),
            ("objects", "object", full_objects, object_index),
        ):
            own: list[str] = []
            for name, raw_item in extension[section].items():
                if raw_item.get("extends") == name:
                    documents[entity_path(slug, section, name, patch_of=scope)] = render_patch(
                        raw_item,
                        compiled_items[name],
                        name=name,
                        kind=kind,
                        scope=scope,
                        types=types,
                        objects=full_objects,
                        categories=categories,
                    )
                    patches.setdefault(section, []).append(name)
                    continue
                scoped = f"{scope}/{name}"
                document = render_item(
                    compiled_items[scoped],
                    name=scoped,
                    kind=kind,
                    types=types,
                    objects=full_objects,
                    categories=categories,
                    extension=scope,
                )
                path = entity_path(slug, section, scoped)
                documents[path] = document
                extra = {"group": object_group(scoped)} if kind == "object" else None
                index.append(index_entry(document, path=path, extra=extra))
                own.append(scoped)
            set_if(summary, section, sorted(own))
        set_if(
            summary,
            "profiles",
            sorted(f"{scope}/{name}" for name in extension["profiles"]),
        )
        set_if(summary, "patches", {key: sorted(value) for key, value in patches.items()})
        extension_summaries[scope] = summary

    profiles: dict[str, dict] = {}
    for name, profile in sorted(core["profiles"].items()):
        profiles[name] = render_profile(profile, name=name, types=types, objects=core_objects, extension=None)
    for name, profile in sorted(full["profiles"].items()):
        if "/" in name:
            profiles[name] = render_profile(
                profile, name=name, types=types, objects=full_objects, extension=name.split("/", 1)[0],
            )

    category_classes: dict[str, list[str]] = {}
    for entry in class_index:
        if entry.get("category") and not entry.get("abstract"):
            category_classes.setdefault(entry["category"], []).append(entry["name"])
    rendered_categories: dict[str, dict] = {}
    for name, category in sorted(categories.items(), key=lambda item: item[1].get("uid", 0)):
        entry: dict[str, Any] = {}
        set_if(entry, "uid", category.get("uid"))
        set_if(entry, "caption", category.get("caption"))
        set_if(entry, "description", clean_description(category.get("description", "")))
        set_if(entry, "classes", sorted(category_classes.get(name, [])))
        rendered_categories[name] = entry

    dictionary = {
        **core["dictionary"]["attributes"],
        **{
            name: data
            for name, data in full["dictionary"]["attributes"].items()
            if name not in core["dictionary"]["attributes"]
        },
    }

    class_index.sort(
        key=lambda entry: (
            categories.get(entry.get("category", ""), {}).get("uid", 0),
            "/" in entry["name"],
            not entry.get("abstract", False),
            entry["name"],
        )
    )
    object_index.sort(key=lambda entry: ("/" in entry["name"], entry["name"]))
    compact_inherited_attributes(documents, slug)

    documents[f"{slug}/categories.yaml"] = rendered_categories
    documents[f"{slug}/classes.yaml"] = {"classes": class_index}
    documents[f"{slug}/objects.yaml"] = {"objects": object_index}
    documents[f"{slug}/profiles.yaml"] = profiles
    documents[f"{slug}/attributes.yaml"] = render_dictionary(dictionary, types=types, objects=full_objects)
    documents[f"{slug}/types.yaml"] = render_types(core_types, extension_types=extension_types)

    version_document: dict[str, Any] = {
        "version": version,
        "status": "stable" if is_stable else "development",
        "source": {
            "repository": OCSF_SCHEMA_REPO,
            "ref": ref,
            "commit": resolve_commit(schema_dir),
            "compiler": OCSF_COMPILER,
        },
    }
    set_if(version_document, "extensions", extension_summaries)
    documents[f"{slug}/version.yaml"] = version_document

    return {
        "version": version,
        "slug": slug,
        "is_stable": is_stable,
        "documents": documents,
        "names": {
            "classes": sorted(entry["name"] for entry in class_index if "/" not in entry["name"] and not entry.get("abstract")),
            "objects": sorted(entry["name"] for entry in object_index if "/" not in entry["name"]),
            "profiles": sorted(name for name in profiles if "/" not in name),
        },
    }


def add_version_changes(current: dict, previous: dict | None) -> None:
    """Record the core classes, objects, and profiles added or removed since
    the previous version in the version document."""
    if previous is None:
        return
    version_document = current["documents"][f"{current['slug']}/version.yaml"]
    version_document["previous"] = previous["version"]
    changes: dict[str, dict] = {}
    for key in ("classes", "objects", "profiles"):
        cur = set(current["names"][key])
        prev = set(previous["names"][key])
        set_if(changes.setdefault("added", {}), key, sorted(cur - prev))
        set_if(changes.setdefault("removed", {}), key, sorted(prev - cur))
    set_if(version_document, "changes", {key: value for key, value in changes.items() if value})


def check_references(version_data: dict) -> None:
    """Fail when a name in a generated document does not resolve, since the
    YAML files refer to each other by name only."""
    slug = version_data["slug"]
    documents = version_data["documents"]
    classes = {entry["name"] for entry in documents[f"{slug}/classes.yaml"]["classes"]}
    objects = {entry["name"] for entry in documents[f"{slug}/objects.yaml"]["objects"]}
    profiles = set(documents[f"{slug}/profiles.yaml"])
    types = set(documents[f"{slug}/types.yaml"])
    categories = set(documents[f"{slug}/categories.yaml"])
    extensions = set(documents[f"{slug}/version.yaml"].get("extensions", {}))
    errors: list[str] = []

    def expect(path: str, what: str, name: object, known: set[str]) -> None:
        if name not in known:
            errors.append(f"{path}: unknown {what} `{name}`")

    def check_attributes(path: str, attributes: dict) -> None:
        for attribute_name, attribute in attributes.items():
            if "object" in attribute:
                expect(path, "object", attribute["object"], objects)
            for profile in attribute.get("profiles", [attribute.get("profile")]):
                if profile is not None:
                    expect(path, "profile", profile, profiles)
            if attribute.get("type") != "object_t":
                expect(path, "type", attribute.get("type"), types)

    def check_links(path: str, links: dict) -> None:
        for name in links.get("classes", []):
            expect(path, "class", name, classes)
        for name in links.get("objects", []):
            expect(path, "object", name, objects)

    for path, document in documents.items():
        if "/classes/" in path or "/objects/" in path:
            known = classes if "/classes/" in path else objects
            if "extends" in document:
                expect(path, "parent", document["extends"], known)
            if "patches" in document:
                expect(path, "patched item", document["patches"], known)
            if "category" in document:
                expect(path, "category", document["category"], categories)
            for profile in document.get("profiles", []):
                expect(path, "profile", profile, profiles)
            for extension in document.get("patched_by", []):
                expect(path, "extension", extension, extensions)
            check_links(path, document.get("referenced_by", {}))
            check_attributes(path, document["attributes"])
    for name, profile in documents[f"{slug}/profiles.yaml"].items():
        path = f"{slug}/profiles.yaml#{name}"
        check_links(path, profile.get("applies_to", {}))
        check_attributes(path, profile["attributes"])
    for name, attribute in documents[f"{slug}/attributes.yaml"].items():
        path = f"{slug}/attributes.yaml#{name}"
        if "object" in attribute:
            expect(path, "object", attribute["object"], objects)
        check_links(path, attribute.get("used_by", {}))
    for name, category in documents[f"{slug}/categories.yaml"].items():
        for class_name in category.get("classes", []):
            expect(f"{slug}/categories.yaml#{name}", "class", class_name, classes)
    for entry in documents[f"{slug}/classes.yaml"]["classes"] + documents[f"{slug}/objects.yaml"]["objects"]:
        if entry["path"] not in documents:
            errors.append(f"{slug}: index entry `{entry['name']}` points to missing {entry['path']}")
    if errors:
        raise ValueError("Unresolved references:\n" + "\n".join(errors[:50]))


def split_introduction(text: str) -> list[dict[str, str]]:
    """Split a long Markdown document at ``## `` headings.

    Returns a list of dicts with keys *slug*, *title*, and *content*.
    The first chunk uses the document's ``# `` heading (or falls back
    to "Introduction").
    """
    sections: list[dict[str, str]] = []
    # Split on lines starting with "## ".
    parts = re.split(r"(?m)^(?=## )", text)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        heading_match = re.match(r"^(#{1,2})\s+(.+)$", part, flags=re.MULTILINE)
        if heading_match:
            title = heading_match.group(2).strip()
        else:
            title = "Introduction"
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        sections.append({"slug": slug, "title": title, "content": part})
    return sections


def fetch_json(client: httpx.Client, url: str) -> object:
    response = client.get(url)
    response.raise_for_status()
    return response.json()


def fetch_text(client: httpx.Client, url: str) -> str:
    response = client.get(url)
    response.raise_for_status()
    return response.text


def parse_heading(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, flags=re.MULTILINE)
    return match.group(1).strip() if match else fallback


def fetch_pages(client: httpx.Client, section: str) -> list[dict[str, str]]:
    items = fetch_json(client, f"{OCSF_DOCS_API}/{section}")
    assert isinstance(items, list)
    pages: list[dict[str, str]] = []
    for item in items:
        name = item["name"]
        if not name.endswith(".md") or name.lower() == "readme.md":
            continue
        content = fetch_text(client, f"{OCSF_DOCS_RAW}/{section}/{name}")
        slug = name.removesuffix(".md")
        pages.append({"slug": slug, "title": parse_heading(content, slug), "content": content})
    return pages


SKILL_TEMPLATE = string.Template(
    """---
name: tenzir-ocsf
description: Answer questions about OCSF (Open Cybersecurity Schema Framework). Use when the user asks about OCSF classes, objects, attributes, profiles, extensions, or event normalization.
metadata:
  uses:
    skills:
      - name: tenzir
        when: writing TQL that maps events to OCSF
---

# OCSF

Answer OCSF questions and make OCSF mapping decisions from the files in this
skill. The YAML schema files are authoritative for names, types, requirements,
enum values, and constraints. The Markdown docs under `docs/` explain concepts
and mapping practice. State only facts from files you read, and say when the
files do not cover a question.

## Versions

Use ${latest}${latest_note} unless the user asks for another one. Stay
within one version per answer.

Available: ${available}.

Paths below use `${latest}/`; swap in the version you need.

## Data files

All paths are relative to this skill's directory. Run searches from there.

| File | Contents |
| --- | --- |
| `${latest}/version.yaml` | Status, source commit, extensions, and changes since the previous version |
| `${latest}/categories.yaml` | Categories with UID and classes |
| `${latest}/classes.yaml` | Class index: UID, category, summary, `activities`, path |
| `${latest}/classes/{name}.yaml` | One class, fully resolved |
| `${latest}/objects.yaml` | Object index: group, summary, path |
| `${latest}/objects/{name}.yaml` | One object, fully resolved |
| `${latest}/profiles.yaml` | Profiles with their attributes and `applies_to` |
| `${latest}/attributes.yaml` | Attribute dictionary with `used_by` |
| `${latest}/types.yaml` | Data types with base type, constraints, and observable type ID |
| `${latest}/extensions/{ext}/{classes,objects}/{name}.yaml` | Extension classes and objects, and patches of core items |

Names resolve within the same version: `object: actor` →
`objects/actor.yaml`; `object: win/reg_key` →
`extensions/win/objects/reg_key.yaml`; `extends` → the parent class or object
file; `type`, `profile`, and `category` → the key in `types.yaml`,
`profiles.yaml`, or `categories.yaml`; `patched_by: [linux]` →
`extensions/linux/{classes,objects}/{same name}.yaml`.

Searches that avoid opening many files:

- Find a class: `grep -n -i "keyword" ${latest}/classes.yaml`
- Find an attribute and where it is used: `grep -n -A 12 "^src_endpoint:" ${latest}/attributes.yaml`
- Jump to an attribute in a class: `grep -n -A 20 "^  actor:" ${latest}/classes/process_activity.yaml`
- Find what holds an object: `referenced_by` in `${latest}/objects/{name}.yaml`

## Reading class and object files

`attributes` lists every attribute, including inherited and profile
attributes, ordered required, recommended, then optional. Attributes that
`patched_by` extensions add live only in the extension patch files.

Attributes with `from` but no description are inherited unchanged and fit on
one line; the description is in the file that `from` names:

```yaml
severity_id: {caption: Severity ID, type: integer_t, requirement: required, group: classification, sibling: severity, enum: {0: Unknown, 1: Informational, 2: Low, 3: Medium, 4: High, 5: Critical, 6: Fatal, 99: Other}, from: base_event}
```

Fields that need explanation:

- `uid`, `category_uid`: the class's `class_uid` and `category_uid` values.
- `abstract: true`: a parent that events never use directly.
- `profile` / `profiles` on an attribute: present only when that profile is
  applied.
- `sibling`: the string attribute that takes the enum caption, e.g.
  `activity_name` for `activity_id`.
- `enum`: integer keys mapped to captions, or to `caption` and `description`.
- `observable`: the observable `type_id` of the attribute or object.
- `constraints`: `at_least_one` (one or more listed attributes set) or
  `just_one` (exactly one set).
- `associations`: attributes that describe the same entity.
- `referenced_by` (objects): classes and objects that hold this object, with
  the attribute names.
- `extension`, `patches`: the defining extension and, for a patch, the core
  item it extends. A patch lists only what it adds or changes.
- `deprecated`, `supersedes`: deprecation details and the items this one
  replaces.

## Mapping events

Write the TQL with the `tenzir` skill. Use this skill for the schema
decisions:

1. Pick the class by its category and the `activities` in `classes.yaml`;
   read the candidate class files and compare them. `activities` omits `0`
   (Unknown) and `99` (Other), which every class allows.
2. Set `class_uid`, `category_uid`, `activity_id`, `type_uid`
   (`class_uid * 100 + activity_id`), `severity_id`, `time`,
   `metadata.version`, and `metadata.product`.
3. Apply the profiles the source supports: list them in `metadata.profiles`
   and fill the attributes they add.
4. Fill required attributes, then recommended ones. A nested object's own
   requirement levels apply once you set it. Satisfy `constraints`.
5. Set `_id` attributes and let `ocsf_derive` fill their string siblings. For
   `99` (Other), set the sibling to the source value.
6. Keep source fields without an OCSF target in `unmapped`.
7. Run `ocsf_derive`, then `ocsf_cast`. The mapping is complete when
   `ocsf_cast` emits no warnings.

## Docs

| Topic | Start here |
| --- | --- |
| Framework concepts and design | [Introduction](docs/introduction.md), [FAQs](docs/faqs.md) |
| Profiles | [Profiles](docs/introduction/profiles.md), then `profiles.yaml` |
| Extending the schema | [Extensions](docs/introduction/extensions.md), [Patching the Core Schema](docs/articles/patching-core-using-extensions.md) |
| Observables, alerts, process parentage | [Articles](docs/articles.md) |
| Changes between versions | `changes` in `version.yaml`, then diff the item files |
"""
)


def render_skill(*, latest: str, latest_note: str, available: str) -> str:
    return SKILL_TEMPLATE.substitute(latest=latest, latest_note=latest_note, available=available)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--version")
    parser.add_argument("--latest-only", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    temp_root = Path(tempfile.mkdtemp(prefix="ocsf-skill-"))
    version_docs: list[dict] = []

    try:
        with httpx.Client(headers=HTTP_HEADERS, follow_redirects=True, timeout=30.0) as client:
            version_specs = collect_version_specs(client, args.version)
            if args.latest_only:
                version_specs = [version_specs[-1]]

            for spec in version_specs:
                schema_dir, ref = clone_schema(spec.version, spec.ref, temp_root)
                version_docs.append(
                    build_version(spec.version, schema_dir, ref=ref, is_stable=spec.is_stable)
                )

            faqs = fetch_pages(client, "faqs")
            articles = fetch_pages(client, "articles")
            overview = fetch_text(client, f"{OCSF_DOCS_RAW}/overview/understanding-ocsf.md")

        for idx, data in enumerate(version_docs):
            add_version_changes(data, version_docs[idx - 1] if idx > 0 else None)
            check_references(data)

        latest_stable = next((data for data in reversed(version_docs) if data["is_stable"]), None)
        latest_dev = next((data for data in reversed(version_docs) if not data["is_stable"]), None)
        latest_reference = latest_stable or version_docs[-1]

        shutil.rmtree(output_dir, ignore_errors=True)
        output_dir.mkdir(parents=True, exist_ok=True)

        slugs = [data["slug"] for data in version_docs if data["is_stable"]]
        available = f"{slugs[0]} through {slugs[-1]}" if len(slugs) > 1 else ", ".join(slugs)
        if latest_dev is not None:
            dev = f"{latest_dev['slug']} (unreleased)"
            available = f"{available} and {dev}" if available else dev
        write_file(
            output_dir / "SKILL.md",
            render_skill(
                latest=latest_reference["slug"],
                latest_note=", the latest stable version," if latest_stable is not None else "",
                available=available,
            ),
        )

        docs_dir = output_dir / "docs"
        intro_sections = split_introduction(overview)
        if intro_sections:
            toc_lines = ["# Introduction", "", "OCSF overview split into focused sections.", ""]
            for section in intro_sections:
                toc_lines.append(f"- [{section['title']}](introduction/{section['slug']}.md)")
                section_content = section["content"]
                if not section_content.endswith("\n"):
                    section_content += "\n"
                write_file(docs_dir / "introduction" / f"{section['slug']}.md", section_content)
            write_file(docs_dir / "introduction.md", "\n".join(toc_lines) + "\n")
        else:
            write_file(
                docs_dir / "introduction.md",
                overview if overview.endswith("\n") else f"{overview}\n",
            )

        write_file(
            docs_dir / "faqs.md",
            "\n".join(["# FAQs", "", *[f"- [{page['title']}](faqs/{page['slug']}.md)" for page in faqs], ""]),
        )
        for faq in faqs:
            write_file(
                docs_dir / "faqs" / f"{faq['slug']}.md",
                faq["content"] if faq["content"].endswith("\n") else f"{faq['content']}\n",
            )

        write_file(
            docs_dir / "articles.md",
            "\n".join(
                ["# Articles", "", *[f"- [{page['title']}](articles/{page['slug']}.md)" for page in articles], ""]
            ),
        )
        for article in articles:
            write_file(
                docs_dir / "articles" / f"{article['slug']}.md",
                article["content"] if article["content"].endswith("\n") else f"{article['content']}\n",
            )

        for data in version_docs:
            for path, document in data["documents"].items():
                text = dump_yaml(document)
                if any(
                    "from" in attribute and "description" not in attribute
                    for attribute in document.get("attributes", {}).values()
                ):
                    text = INHERITED_ATTRIBUTE_NOTE + text
                write_file(output_dir / path, text)

        print(f"Generated OCSF skill in {output_dir}")
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)


if __name__ == "__main__":
    main()
