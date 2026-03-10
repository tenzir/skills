#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "httpx>=0.28.0",
#   "markdownify>=1.1.0",
#   "packaging>=24.0",
# ]
# ///

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

import httpx
from markdownify import markdownify
from packaging.version import Version


OCSF_SCHEMA_REPO = "https://github.com/ocsf/ocsf-schema.git"
OCSF_SCHEMA_RAW = "https://raw.githubusercontent.com/ocsf/ocsf-schema/main"
OCSF_DOCS_API = "https://api.github.com/repos/ocsf/ocsf-docs/contents"
OCSF_DOCS_RAW = "https://raw.githubusercontent.com/ocsf/ocsf-docs/main"
HTTP_HEADERS = {
    "User-Agent": "tenzir-skills-generator",
    "Accept": "application/json",
}
SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
DEV_VERSION_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)-dev$")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")


@dataclass(frozen=True, slots=True)
class VersionSpec:
    version: str
    ref: str
    is_stable: bool


def version_to_slug(version: str) -> str:
    return f"v{version}"


def name_to_slug(name: str) -> str:
    return name.replace("/", "_")


def rewrite_markdown_links(text: str, relative_link_prefix: str = "") -> str:
    def replace(match: re.Match[str]) -> str:
        label, href = match.groups()
        if href.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            return match.group(0)

        link_target = href
        anchor = ""
        if "#" in link_target:
            link_target, anchor = link_target.split("#", 1)
            anchor = f"#{anchor}"
        if "?" in link_target:
            return match.group(0)
        if not link_target.endswith(".md"):
            link_target = f"{link_target}.md"
        if relative_link_prefix and not link_target.startswith(("./", "../")):
            link_target = f"{relative_link_prefix}{link_target}"
        return f"[{label}]({link_target}{anchor})"

    return MARKDOWN_LINK_RE.sub(replace, text)


def clean_description(text: str, *, relative_link_prefix: str = "") -> str:
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
    rendered = rewrite_markdown_links(rendered, relative_link_prefix=relative_link_prefix)
    return rendered.strip()


def format_meta_list(entries: list[tuple[str, object]]) -> str:
    lines = [
        f"- **{label}**: {value}"
        for label, value in entries
        if value not in (None, "")
    ]
    return "\n".join(lines)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


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


def clone_schema(version: str, ref: str, temp_root: Path) -> Path:
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
            return repo_dir
        except subprocess.CalledProcessError:
            pass
    raise RuntimeError(f"Failed to clone OCSF schema for version {version} from ref {ref}")


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
    if not directory.exists():
        return {}
    return {
        path.stem: read_json(path)
        for path in sorted(directory.glob("*.json"))
        if path.is_file()
    }


def load_classes(schema_dir: Path) -> tuple[dict[str, dict], dict[str, dict]]:
    """Load event classes and intermediate (category-level) base classes.

    Returns (classes, intermediate_classes) where intermediate_classes
    are the abstract category base classes like ``network``, ``system``,
    ``iam`` etc. that concrete classes extend.
    """
    classes: dict[str, dict] = {}
    intermediates: dict[str, dict] = {}
    events_dir = schema_dir / "events"
    if not events_dir.exists():
        return classes, intermediates

    base_event_path = events_dir / "base_event.json"
    if base_event_path.exists():
        classes["base_event"] = read_json(base_event_path)

    for category_dir in sorted(path for path in events_dir.iterdir() if path.is_dir()):
        category_key = category_dir.name
        for entry in sorted(category_dir.glob("*.json")):
            data = read_json(entry)
            class_name = data.get("name") or entry.stem
            data["category_key"] = category_key
            if entry.stem == category_key:
                intermediates[class_name] = data
                continue
            classes[class_name] = data
    return classes, intermediates


def resolve_profiles(
    class_data: dict,
    *parent_mappings: dict[str, dict],
) -> list[str]:
    """Collect profile names registered on a class and its ancestors."""
    seen: set[str] = set()
    profiles: list[str] = []
    current: dict | None = class_data
    while current is not None:
        for name in current.get("profiles") or []:
            if name not in seen:
                seen.add(name)
                profiles.append(name)
        extends = current.get("extends")
        if not extends:
            break
        current = lookup_schema(extends, *parent_mappings)
    return profiles


def format_doc_link(
    name: str,
    data: dict,
    *,
    target: str,
    include_schema_name: bool = False,
) -> str:
    caption = data.get("caption") or name
    label = f"{caption} ({name})" if include_schema_name else caption
    return f"[{label}]({target})"


def format_class_doc_link(
    name: str,
    class_data: dict,
    *,
    link_prefix: str,
    include_schema_name: bool = False,
) -> str:
    return format_doc_link(
        name,
        class_data,
        target=f"{link_prefix}{name_to_slug(name)}.md",
        include_schema_name=include_schema_name,
    )


def format_named_links(
    names: list[str],
    *,
    data_by_name: dict[str, dict],
    link_by_name: dict[str, str],
    include_schema_name: bool = False,
) -> str:
    rendered: list[str] = []
    for name in names:
        target = link_by_name.get(name)
        if target is None:
            rendered.append(f"`{name}`")
            continue
        rendered.append(
            format_doc_link(
                name,
                data_by_name.get(name, {}),
                target=target,
                include_schema_name=include_schema_name,
            )
        )
    return ", ".join(rendered)


def load_extensions(schema_dir: Path) -> dict[str, dict]:
    result: dict[str, dict] = {}
    extensions_dir = schema_dir / "extensions"
    if not extensions_dir.exists():
        return result

    for extension_dir in sorted(path for path in extensions_dir.iterdir() if path.is_dir()):
        meta_path = extension_dir / "extension.json"
        if not meta_path.exists():
            continue
        dictionary_path = extension_dir / "dictionary.json"
        result[extension_dir.name] = {
            "meta": read_json(meta_path),
            "dictionary": read_json(dictionary_path) if dictionary_path.exists() else {},
            "objects": load_directory_json(extension_dir / "objects"),
            "profiles": load_directory_json(extension_dir / "profiles"),
            "events": load_directory_json(extension_dir / "events"),
        }
    return result


def merge_dictionaries(base: dict, extra: dict | None = None) -> dict:
    merged = dict(base)
    merged["attributes"] = dict(base.get("attributes", {}))
    merged["types"] = dict(base.get("types", {}))
    if not extra:
        return merged
    if isinstance(extra.get("attributes"), dict):
        merged["attributes"].update(extra["attributes"])
    if isinstance(extra.get("types"), dict):
        merged["types"].update(extra["types"])
    return merged


def lookup_schema(name: str, *mappings: dict[str, dict]) -> dict | None:
    for mapping in mappings:
        if name in mapping:
            return mapping[name]
    return None


def resolve_attribute(name: str, local_data: object, dictionary: dict) -> dict:
    base = dictionary.get("attributes", {}).get(name, {})
    if not isinstance(base, dict):
        base = {}
    if not isinstance(local_data, dict):
        local_data = {}
    return {**base, **local_data}


def format_attribute(
    name: str,
    data: dict,
    object_links: dict[str, str] | None = None,
    *,
    relative_link_prefix: str = "",
) -> str:
    desc = clean_description(
        data.get("description") or data.get("caption") or "",
        relative_link_prefix=relative_link_prefix,
    )
    lines = [f"### `{name}`", ""]
    # Build the type display, optionally linking to the object page.
    type_name = data.get("object_type") or data.get("type") or ""
    if type_name and object_links is not None and type_name in object_links:
        link_target = object_links[type_name]
        type_display = f"[`{type_name}`]({link_target})"
    elif type_name:
        type_display = f"`{type_name}`"
    else:
        type_display = ""
    meta = format_meta_list(
        [
            ("Type", type_display),
            ("Requirement", data.get("requirement")),
            ("Observable", data.get("observable")),
            ("Group", data.get("group")),
            ("Sibling", f"`{data['sibling']}`" if data.get("sibling") else ""),
        ]
    )
    if meta:
        lines.extend([meta, ""])
    if isinstance(data.get("range"), list):
        lines.extend([f"- **Range**: `{data['range'][0]}` to `{data['range'][1]}`", ""])
    if data.get("regex"):
        lines.extend([f"- **Regex**: `{data['regex']}`", ""])
    if isinstance(data.get("values"), list) and data["values"]:
        values = ", ".join(f"`{value}`" for value in data["values"])
        lines.extend([f"- **Values**: {values}", ""])
    if isinstance(data.get("enum"), dict) and data["enum"]:
        lines.extend(["#### Enum values", ""])
        for key, value in data["enum"].items():
            enum_desc = clean_description(
                value.get("description", ""),
                relative_link_prefix=relative_link_prefix,
            )
            label = value.get("caption") or key
            suffix = f" - {enum_desc}" if enum_desc else ""
            lines.append(f"- `{key}`: `{label}`{suffix}")
        lines.append("")
    if desc:
        lines.extend([desc, ""])
    return "\n".join(lines)


def format_constraints(constraints: dict) -> str:
    """Render an OCSF constraints dict as Markdown."""
    lines: list[str] = []
    for kind in ("at_least_one", "just_one"):
        attrs = constraints.get(kind)
        if not attrs:
            continue
        label = "At least one of" if kind == "at_least_one" else "Exactly one of"
        attrs_str = ", ".join(f"`{a}`" for a in attrs)
        lines.append(f"- **{label}**: {attrs_str}")
    return "\n".join(lines)


def format_associations(associations: dict) -> str:
    """Render an OCSF associations dict as Markdown."""
    lines: list[str] = []
    for source, targets in associations.items():
        targets_str = ", ".join(f"`{t}`" for t in targets)
        lines.append(f"- `{source}` ↔ {targets_str}")
    return "\n".join(lines)


def collect_inherited_attributes(
    entity_data: dict,
    dictionary: dict,
    *parent_mappings: dict[str, dict],
) -> list[tuple[str, list[tuple[str, str]]]]:
    """Walk the extends chain and collect required/recommended attributes
    from each ancestor.  Returns a list of (ancestor_name, [(attr, requirement), ...])."""
    result: list[tuple[str, list[tuple[str, str]]]] = []
    own_attrs = set((entity_data.get("attributes") or {}).keys())
    extends = entity_data.get("extends")
    seen_parents: set[str] = set()
    while extends:
        if extends in seen_parents:
            break
        seen_parents.add(extends)
        parent = lookup_schema(extends, *parent_mappings)
        if parent is None:
            break
        parent_caption = parent.get("caption") or extends
        parent_attrs = parent.get("attributes") or {}
        important: list[tuple[str, str]] = []
        for attr_name, attr_data in parent_attrs.items():
            if attr_name.startswith("$") or attr_name in own_attrs:
                continue
            resolved = resolve_attribute(attr_name, attr_data, dictionary)
            # Any nearer ancestor shadows the same attribute higher in the chain,
            # even if the nearer definition downgrades it to optional.
            own_attrs.add(attr_name)
            requirement = resolved.get("requirement", "")
            if requirement in ("required", "recommended"):
                important.append((attr_name, requirement))
        if important:
            important.sort(key=lambda pair: (0 if pair[1] == "required" else 1, pair[0]))
            result.append((parent_caption, important))
        extends = parent.get("extends")
    return result


def render_entity_page(
    *,
    title: str,
    description: str | None,
    meta_entries: list[tuple[str, object]],
    attributes: list[tuple[str, dict]],
    constraints: dict | None = None,
    associations: dict | None = None,
    inherited_attributes: list[tuple[str, list[tuple[str, str]]]] | None = None,
    object_links: dict[str, str] | None = None,
    relative_link_prefix: str = "",
) -> str:
    lines = [f"# {title}", ""]
    if description:
        lines.extend([clean_description(description, relative_link_prefix=relative_link_prefix), ""])
    meta = format_meta_list(meta_entries)
    if meta:
        lines.extend([meta, ""])
    if constraints:
        rendered = format_constraints(constraints)
        if rendered:
            lines.extend(["## Constraints", "", rendered, ""])
    if associations:
        rendered = format_associations(associations)
        if rendered:
            lines.extend(["## Associations", "", rendered, ""])
    if inherited_attributes:
        lines.extend(["## Inherited attributes", ""])
        for ancestor_name, attrs in inherited_attributes:
            lines.append(f"**From {ancestor_name}:**")
            for attr_name, requirement in attrs:
                lines.append(f"- `{attr_name}` ({requirement})")
            lines.append("")
    if attributes:
        lines.extend(["## Attributes", ""])
        for attr_name, attr_data in attributes:
            lines.append(format_attribute(
                attr_name, attr_data,
                object_links=object_links,
                relative_link_prefix=relative_link_prefix,
            ))
    content = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    return content + "\n"


def build_version_docs(version: str, schema_dir: Path) -> dict:
    slug = version_to_slug(version)
    categories = read_json(schema_dir / "categories.json").get("attributes", {})
    dictionary = read_json(schema_dir / "dictionary.json")
    classes, intermediates = load_classes(schema_dir)
    objects = load_directory_json(schema_dir / "objects")
    profiles = load_directory_json(schema_dir / "profiles")
    extensions = load_extensions(schema_dir)
    types = dictionary.get("types", {}).get("attributes", {})

    return {
        "version": version,
        "slug": slug,
        "categories": categories,
        "dictionary": dictionary,
        "classes": classes,
        "intermediates": intermediates,
        "objects": objects,
        "profiles": profiles,
        "extensions": extensions,
        "types": types,
    }


def generate_classes_overview(version_data: dict) -> str:
    lines = [f"# Classes ({version_data['version']})", ""]
    for category_key, category in version_data["categories"].items():
        category_bases = sorted(
            (
                (name, data)
                for name, data in version_data["intermediates"].items()
                if data.get("category_key") == category_key
            ),
            key=lambda item: (item[1].get("caption") or item[0]).casefold(),
        )
        category_classes = sorted(
            (
                (name, data)
                for name, data in version_data["classes"].items()
                if data.get("category_key") == category_key
            ),
            key=lambda item: (item[1].get("caption") or item[0]).casefold(),
        )
        if not category_bases and not category_classes:
            continue
        lines.extend([f"## {category['caption']}", "", clean_description(category.get("description", "")), ""])
        for name, data in category_bases:
            lines.append(
                f"- {format_class_doc_link(name, data, link_prefix='classes/', include_schema_name=True)}"
                " [base class]"
            )
        for name, data in category_classes:
            lines.append(f"- {format_class_doc_link(name, data, link_prefix='classes/')}")
        lines.append("")
    if "base_event" in version_data["classes"]:
        lines.extend([
            "## Base Event",
            "",
            f"- {format_class_doc_link('base_event', version_data['classes']['base_event'], link_prefix='classes/')}",
            "",
        ])
    content = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    return content + "\n"


def generate_named_overview(version_data: dict, title: str, section: str) -> str:
    items = version_data[section]
    lines = [f"# {title} ({version_data['version']})", ""]
    for name, data in sorted(items.items(), key=lambda item: (item[1].get("caption") or item[0]).casefold()):
        lines.append(f"- [{data.get('caption') or name}]({section}/{name_to_slug(name)}.md)")
    return "\n".join(lines) + "\n"


# Semantic grouping for objects overview.  Each entry maps a group
# heading to a set of object names.  Objects not listed land in the
# catch-all group at the end.
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


def generate_objects_overview(version_data: dict) -> str:
    objects = version_data["objects"]
    assigned: set[str] = set()
    lines = [f"# Objects ({version_data['version']})", ""]

    for group_title, group_names in _OBJECT_GROUPS:
        group_items = sorted(
            ((name, data) for name, data in objects.items() if name in group_names),
            key=lambda item: (item[1].get("caption") or item[0]).casefold(),
        )
        if not group_items:
            continue
        lines.extend([f"## {group_title}", ""])
        for name, data in group_items:
            lines.append(f"- [{data.get('caption') or name}](objects/{name_to_slug(name)}.md)")
            assigned.add(name)
        lines.append("")

    # Catch-all for objects not assigned to any group.
    remaining = sorted(
        ((name, data) for name, data in objects.items() if name not in assigned),
        key=lambda item: (item[1].get("caption") or item[0]).casefold(),
    )
    if remaining:
        lines.extend(["## Other", ""])
        for name, data in remaining:
            lines.append(f"- [{data.get('caption') or name}](objects/{name_to_slug(name)}.md)")
        lines.append("")

    content = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    return content + "\n"


def generate_extensions_overview(version_data: dict) -> str:
    lines = [f"# Extensions ({version_data['version']})", ""]
    for name, data in sorted(
        version_data["extensions"].items(),
        key=lambda item: (item[1]["meta"].get("caption") or item[0]).casefold(),
    ):
        lines.append(
            f"- [{data['meta'].get('caption') or name}](extensions/{name_to_slug(name)}/index.md)"
        )
    return "\n".join(lines) + "\n"


def build_name_link_map(names: list[str] | set[str], *, prefix: str) -> dict[str, str]:
    return {
        name: f"{prefix}{name_to_slug(name)}.md"
        for name in sorted(names)
    }


def build_extension_index_page(name: str, extension_data: dict) -> str:
    lines = [f"# {extension_data['meta'].get('caption') or name}", ""]
    desc = clean_description(extension_data["meta"].get("description", ""))
    if desc:
        lines.extend([desc, ""])
    lines.append(f"- **Name**: `{extension_data['meta'].get('name') or name}`")
    if extension_data["meta"].get("version"):
        lines.append(f"- **Version**: `{extension_data['meta']['version']}`")
    if extension_data["meta"].get("uid") is not None:
        lines.append(f"- **UID**: `{extension_data['meta']['uid']}`")
    lines.append("")

    for section_title, key in (
        ("Events", "events"),
        ("Objects", "objects"),
        ("Profiles", "profiles"),
    ):
        section_items = extension_data[key]
        if not section_items:
            continue
        lines.extend([f"## {section_title}", ""])
        for item_name, item_data in sorted(
            section_items.items(),
            key=lambda item: (item[1].get("caption") or item[0]).casefold(),
        ):
            lines.append(
                f"- [{item_data.get('caption') or item_name}]({key}/{name_to_slug(item_name)}.md)"
            )
        lines.append("")

    return "\n".join(lines) + "\n"


def generate_types_overview(version_data: dict) -> str:
    lines = [f"# Types ({version_data['version']})", ""]
    for name, data in sorted(
        version_data["types"].items(),
        key=lambda item: (item[1].get("caption") or item[0]).casefold(),
    ):
        lines.extend([f"## `{name}`", "", f"- **Caption**: {data.get('caption') or name}"])
        if data.get("type_name"):
            lines.append(f"- **Base type**: `{data['type_name']}`")
        if data.get("regex"):
            lines.append(f"- **Regex**: `{data['regex']}`")
        if isinstance(data.get("range"), list):
            lines.append(f"- **Range**: `{data['range'][0]}` to `{data['range'][1]}`")
        if isinstance(data.get("values"), list) and data["values"]:
            values = ", ".join(f"`{value}`" for value in data["values"])
            lines.append(f"- **Values**: {values}")
        desc = clean_description(data.get("description", ""))
        if desc:
            lines.extend(["", desc])
        lines.append("")
    content = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    return content + "\n"


def generate_changelog(current: dict, previous: dict | None) -> str:
    """Generate a compact 'What's new' section comparing two version dicts."""
    if previous is None:
        return ""

    def _caption_set(section: dict) -> dict[str, str]:
        return {name: data.get("caption") or name for name, data in section.items()}

    lines: list[str] = []
    for label, key in [("Classes", "classes"), ("Objects", "objects"), ("Profiles", "profiles")]:
        cur_names = _caption_set(current[key])
        prev_names = _caption_set(previous[key])
        added = sorted(set(cur_names) - set(prev_names))
        removed = sorted(set(prev_names) - set(cur_names))
        if added:
            lines.append(f"**New {label.lower()}:** {', '.join(cur_names[n] for n in added)}")
        if removed:
            lines.append(f"**Removed {label.lower()}:** {', '.join(prev_names[n] for n in removed)}")

    if not lines:
        return ""
    return "## What's new\n\n" + "\n\n".join(lines) + "\n"


def generate_version_overview(version_data: dict, previous: dict | None = None) -> str:
    lines = [f"# OCSF {version_data['version']}", ""]
    lines.append(f"- **Classes**: {len(version_data['classes'])}")
    lines.append(f"- **Objects**: {len(version_data['objects'])}")
    lines.append(f"- **Profiles**: {len(version_data['profiles'])}")
    lines.append(f"- **Extensions**: {len(version_data['extensions'])}")
    lines.extend(
        [
            f"- **Types**: {len(version_data['types'])}",
            "",
            f"- [Classes]({version_data['slug']}/classes.md)",
            f"- [Objects]({version_data['slug']}/objects.md)",
            f"- [Profiles]({version_data['slug']}/profiles.md)",
            f"- [Extensions]({version_data['slug']}/extensions.md)",
            f"- [Types]({version_data['slug']}/types.md)",
            "",
        ]
    )

    changelog = generate_changelog(version_data, previous)
    if changelog:
        lines.extend([changelog, ""])
    return "\n".join(lines) + "\n"


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
                schema_dir = clone_schema(spec.version, spec.ref, temp_root)
                version_docs.append(build_version_docs(spec.version, schema_dir))

            faqs = fetch_pages(client, "faqs")
            articles = fetch_pages(client, "articles")
            overview = fetch_text(client, f"{OCSF_DOCS_RAW}/overview/understanding-ocsf.md")

        latest_stable = next((data for data in reversed(version_docs) if not data["version"].endswith("-dev")), None)
        latest_dev = next((data for data in reversed(version_docs) if data["version"].endswith("-dev")), None)
        latest_reference = latest_stable or version_docs[-1]

        shutil.rmtree(output_dir, ignore_errors=True)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Build annotated version list.
        version_lines: list[str] = []
        for data in version_docs:
            link = f"[{data['version']}]({data['slug']}.md)"
            if data == latest_stable:
                version_lines.append(f"- **{link}** ← latest stable")
            elif data == latest_dev:
                version_lines.append(f"- {link} ← unreleased development snapshot")
            else:
                version_lines.append(f"- {link}")

        write_file(
            output_dir / "SKILL.md",
            "\n".join(
                [
                    "---",
                    "name: ocsf",
                    "description: Answer questions about OCSF (Open Cybersecurity Schema Framework). Use when the user asks about OCSF classes, objects, attributes, profiles, extensions, or event normalization.",
                    "---",
                    "",
                    "# OCSF",
                    "",
                    "Look up OCSF reference documentation and answer from those sources. Only state",
                    "facts from files you read. Never invent schema details. If the documentation",
                    "does not cover the question, say so.",
                    "",
                    "## Versions",
                    "",
                    "Use the latest stable version unless the user requests a specific one. Stick to",
                    "one version per answer.",
                    "",
                    *version_lines,
                    "",
                    "Each version page links to its classes, objects, profiles, extensions, and",
                    "types.",
                    "",
                    "## File layout",
                    "",
                    "```",
                    "introduction.md          # OCSF overview and conceptual sections",
                    "introduction/{section}.md",
                    "faqs.md                  # Schema design rationale",
                    "faqs/{slug}.md",
                    "articles.md              # Deep-dive guides on specific topics",
                    "articles/{slug}.md",
                    "{version}.md             # Version summary (what's new, counts)",
                    "{version}/classes.md     # Class index grouped by category",
                    "{version}/classes/{name}.md",
                    "{version}/objects.md",
                    "{version}/objects/{name}.md",
                    "{version}/profiles.md",
                    "{version}/profiles/{name}.md",
                    "{version}/extensions.md",
                    "{version}/extensions/{name}/index.md",
                    "{version}/extensions/{name}/events/{event}.md",
                    "{version}/extensions/{name}/objects/{object}.md",
                    "{version}/extensions/{name}/profiles/{profile}.md",
                    "{version}/types.md",
                    "```",
                    "",
                    "## Question routing",
                    "",
                    "Pick the shortest reading path for the question type.",
                    "",
                    "| Question pattern | Start here |",
                    "| --- | --- |",
                    "| Which class fits event X? | Category table below → version classes index → candidate class pages |",
                    "| What attributes does class/object Y have? | Version classes or objects index → the specific page |",
                    "| How do profiles work? / Which profile for X? | [Introduction: Profiles](introduction/profiles.md) → version profiles index |",
                    "| How do I extend the schema? | [Introduction: Extensions](introduction/extensions.md) or [Patching the Core Schema](articles/patching-core-using-extensions.md) |",
                    "| How do I populate observables / model alerts? | [FAQs](faqs.md) and [Articles](articles.md) |",
                    "| What changed between versions? | Compare the two version pages |",
                    "| Conceptual / design question | [Introduction](introduction.md) → [FAQs](faqs.md) |",
                    "",
                    "When the question asks you to pick a class, read multiple candidates and explain",
                    "trade-offs.",
                    "",
                    "## Domain knowledge",
                    "",
                    "### Core concepts",
                    "",
                    "**Attributes** are named fields with a data type. Every OCSF field has a",
                    "requirement level: required, recommended, or optional.",
                    "",
                    "**Objects** group related attributes into reusable structures. Objects can nest",
                    "other objects.",
                    "",
                    "**Event classes** define schemas for specific security events. Each class belongs",
                    "to a category and inherits from Base Event.",
                    "",
                    "**Base Event** provides universal attributes and serves as a catch-all when no",
                    "more specific class fits.",
                    "",
                    "**Profiles** are mix-ins that add cross-cutting attributes. A class can apply",
                    "multiple profiles.",
                    "",
                    "**Extensions** add vendor-specific attributes without modifying the core schema.",
                    "",
                    "### Event categories",
                    "",
                    "Use the category range to narrow scope before diving into individual class",
                    "pages.",
                    "",
                    "| Range | Category | Focus |",
                    "| ----- | -------- | ----- |",
                    "| 1xxx | System Activity | OS-level: process, file, module, memory, kernel, registry |",
                    "| 2xxx | Findings | Detections, vulnerabilities, incidents, compliance |",
                    "| 3xxx | IAM | Authentication, authorization, account and group changes |",
                    "| 4xxx | Network Activity | General traffic and protocol-specific activity |",
                    "| 5xxx | Discovery | Device, user, service, and resource enumeration |",
                    "| 6xxx | Application Activity | Web resources, API calls, file hosting, datastore operations |",
                    "| 7xxx | Remediation | File, process, network, and entity remediation actions |",
                    "| 8xxx | Unmanned | Drones, vehicles, and robots |",
                    "",
                    "### Naming conventions",
                    "",
                    "- `snake_case` everywhere: `process_activity`, `network_endpoint`.",
                    "- Arrays use plural names: `answers`, `enrichments`, `attacks`.",
                    "- When `_id` is `Other` (`99`), the sibling string **must** be populated with",
                    "  the source value.",
                    "",
                    "Key suffixes:",
                    "",
                    "| Suffix | Meaning |",
                    "| ------ | ------- |",
                    "| `_id` | Enum integer identifier with a sibling string (same name minus `_id`). `0` = Unknown, `99` = Other. |",
                    "| `_uid` | Schema-unique or external unique identifier (integer for classification attrs, string otherwise). Sibling uses `_name`. |",
                    "| `_uuid` | Globally unique 128-bit identifier (string). No sibling. |",
                    "| `_name` | Friendly name / caption sibling for `_uid` or `_id` attributes. |",
                    "| `_time` | Timestamp (`timestamp_t`, milliseconds since epoch). |",
                    "| `_dt` | Datetime (`datetime_t`, RFC 3339 string). Added by the Date/Time profile alongside `_time` attributes. |",
                    "| `_info` / `_detail` | Object carrying supplementary information. |",
                    "| `_process` | Reference to a Process object. |",
                    "| `_ver` | Version string. |",
                    "| `_list` | Array of values. |",
                    "",
                    "## Answering principles",
                    "",
                    "- Read before answering. Every claim must trace back to a file you read.",
                    "- Use the question routing table and category table to narrow scope before",
                    "  reading class or object pages.",
                    "- Consult [FAQs](faqs.md) for schema design rationale and ambiguous mappings.",
                    "- Consult [Articles](articles.md) for deep-dive topics like observables, alerts,",
                    "  process parentage, and extensions.",
                    "- Read [Introduction](introduction.md) sections for conceptual questions about",
                    "  the framework itself.",
                    "",
                ]
            ),
        )

        intro_sections = split_introduction(overview)
        if intro_sections:
            toc_lines = ["# Introduction", "", "OCSF overview split into focused sections.", ""]
            for section in intro_sections:
                toc_lines.append(f"- [{section['title']}](introduction/{section['slug']}.md)")
                section_content = section["content"]
                if not section_content.endswith("\n"):
                    section_content += "\n"
                write_file(output_dir / "introduction" / f"{section['slug']}.md", section_content)
            write_file(output_dir / "introduction.md", "\n".join(toc_lines) + "\n")
        else:
            write_file(
                output_dir / "introduction.md",
                overview if overview.endswith("\n") else f"{overview}\n",
            )

        write_file(
            output_dir / "faqs.md",
            "\n".join(["# FAQs", "", *[f"- [{page['title']}](faqs/{page['slug']}.md)" for page in faqs], ""]),
        )
        for faq in faqs:
            write_file(
                output_dir / "faqs" / f"{faq['slug']}.md",
                faq["content"] if faq["content"].endswith("\n") else f"{faq['content']}\n",
            )

        write_file(
            output_dir / "articles.md",
            "\n".join(
                ["# Articles", "", *[f"- [{page['title']}](articles/{page['slug']}.md)" for page in articles], ""]
            ),
        )
        for article in articles:
            write_file(
                output_dir / "articles" / f"{article['slug']}.md",
                article["content"] if article["content"].endswith("\n") else f"{article['content']}\n",
            )

        for idx, data in enumerate(version_docs):
            prev = version_docs[idx - 1] if idx > 0 else None
            class_names = set(data["classes"].keys()) | set(data["intermediates"].keys())
            obj_names = set(data["objects"].keys())
            profile_names = set(data["profiles"].keys())
            object_links = build_name_link_map(obj_names, prefix="")
            profile_links = build_name_link_map(profile_names, prefix="../profiles/")
            object_links_from_class_pages = build_name_link_map(obj_names, prefix="../objects/")
            write_file(output_dir / f"{data['slug']}.md", generate_version_overview(data, prev))
            write_file(output_dir / data["slug"] / "classes.md", generate_classes_overview(data))
            write_file(output_dir / data["slug"] / "objects.md", generate_objects_overview(data))
            write_file(output_dir / data["slug"] / "profiles.md", generate_named_overview(data, "Profiles", "profiles"))
            write_file(output_dir / data["slug"] / "extensions.md", generate_extensions_overview(data))
            write_file(output_dir / data["slug"] / "types.md", generate_types_overview(data))

            for name, class_data in data["classes"].items():
                category_info = data["categories"].get(class_data.get("category_key"), {})
                category_uid = category_info.get("uid")
                relative_uid = class_data.get("uid")
                class_uid = (
                    category_uid * 1000 + relative_uid
                    if category_uid is not None and relative_uid is not None
                    else None
                )
                class_profiles = resolve_profiles(
                    class_data, data["classes"], data["intermediates"],
                )
                # Collect constraints: prefer class-level, fall back to parent.
                constraints = class_data.get("constraints")
                if not constraints:
                    parent = data["intermediates"].get(class_data.get("extends", ""))
                    if parent:
                        constraints = parent.get("constraints")
                associations = class_data.get("associations")
                if not associations:
                    parent = data["intermediates"].get(class_data.get("extends", ""))
                    if parent:
                        associations = parent.get("associations")
                page = render_entity_page(
                    title=f"{class_data.get('caption') or name} ({name})",
                    description=class_data.get("description"),
                    meta_entries=[
                        ("Class UID", f"`{class_uid}`" if class_uid is not None else ""),
                        (
                            "Category",
                            category_info.get("caption")
                            or class_data.get("category_key")
                            or "",
                        ),
                        (
                            "Extends",
                            format_class_doc_link(
                                class_data["extends"],
                                data["classes"].get(class_data["extends"])
                                or data["intermediates"].get(class_data["extends"], {}),
                                link_prefix="",
                                include_schema_name=True,
                            )
                            if class_data.get("extends")
                            else "",
                        ),
                        (
                            "Profiles",
                            format_named_links(
                                class_profiles,
                                data_by_name=data["profiles"],
                                link_by_name=profile_links,
                            )
                            if class_profiles
                            else "",
                        ),
                    ],
                    constraints=constraints,
                    associations=associations,
                    inherited_attributes=collect_inherited_attributes(
                        class_data, data["dictionary"], data["classes"], data["intermediates"],
                    ),
                    attributes=[
                        (attr_name, resolve_attribute(attr_name, attr_data, data["dictionary"]))
                        for attr_name, attr_data in (class_data.get("attributes") or {}).items()
                        if not attr_name.startswith("$")
                    ],
                    object_links=object_links_from_class_pages,
                )
                write_file(output_dir / data["slug"] / "classes" / f"{name_to_slug(name)}.md", page)

            for name, intermediate_data in data["intermediates"].items():
                category_info = data["categories"].get(intermediate_data.get("category_key"), {})
                intermediate_profiles = resolve_profiles(
                    intermediate_data, data["classes"], data["intermediates"],
                )
                page = render_entity_page(
                    title=f"{intermediate_data.get('caption') or name} ({name})",
                    description=(
                        f"Abstract base class for {category_info.get('caption', name)} event classes. "
                        "Concrete classes in this category extend this class and inherit its attributes."
                    ),
                    meta_entries=[
                        (
                            "Category",
                            category_info.get("caption")
                            or intermediate_data.get("category_key")
                            or "",
                        ),
                        (
                            "Extends",
                            format_class_doc_link(
                                intermediate_data["extends"],
                                data["classes"].get(intermediate_data["extends"])
                                or data["intermediates"].get(intermediate_data["extends"], {}),
                                link_prefix="",
                                include_schema_name=True,
                            )
                            if intermediate_data.get("extends")
                            else "",
                        ),
                        (
                            "Profiles",
                            format_named_links(
                                intermediate_profiles,
                                data_by_name=data["profiles"],
                                link_by_name=profile_links,
                            )
                            if intermediate_profiles
                            else "",
                        ),
                    ],
                    constraints=intermediate_data.get("constraints"),
                    associations=intermediate_data.get("associations"),
                    inherited_attributes=collect_inherited_attributes(
                        intermediate_data, data["dictionary"], data["classes"], data["intermediates"],
                    ),
                    attributes=[
                        (attr_name, resolve_attribute(attr_name, attr_data, data["dictionary"]))
                        for attr_name, attr_data in (intermediate_data.get("attributes") or {}).items()
                        if not attr_name.startswith("$")
                    ],
                    object_links=object_links_from_class_pages,
                )
                write_file(output_dir / data["slug"] / "classes" / f"{name_to_slug(name)}.md", page)

            for name, object_data in data["objects"].items():
                extends = object_data.get("extends")
                page = render_entity_page(
                    title=f"{object_data.get('caption') or name} ({name})",
                    description=object_data.get("description"),
                    meta_entries=[
                        (
                            "Extends",
                            format_doc_link(
                                extends,
                                data["objects"].get(extends, {}),
                                target=object_links.get(extends, f"{name_to_slug(extends)}.md"),
                                include_schema_name=True,
                            )
                            if extends
                            else "",
                        ),
                    ],
                    attributes=[
                        (attr_name, resolve_attribute(attr_name, attr_data, data["dictionary"]))
                        for attr_name, attr_data in (object_data.get("attributes") or {}).items()
                        if not attr_name.startswith("$")
                    ],
                    object_links=object_links,
                )
                write_file(output_dir / data["slug"] / "objects" / f"{name_to_slug(name)}.md", page)

            # Build reverse mapping: profile name → list of classes that register for it.
            profile_to_classes: dict[str, list[str]] = {}
            for cname, cdata in {**data["classes"], **data["intermediates"]}.items():
                for pname in resolve_profiles(cdata, data["classes"], data["intermediates"]):
                    profile_to_classes.setdefault(pname, []).append(cdata.get("caption") or cname)
            for pname, consumers in profile_to_classes.items():
                profile_to_classes[pname] = sorted(set(consumers), key=str.casefold)

            for name, profile_data in data["profiles"].items():
                applies_to = profile_to_classes.get(name, [])
                applies_section = (
                    "\n".join(f"- {cls}" for cls in applies_to)
                    if applies_to
                    else ""
                )
                extra_sections = ""
                if applies_section:
                    extra_sections = f"\n\n## Applies to\n\n{applies_section}\n"
                page = render_entity_page(
                    title=f"{profile_data.get('caption') or name} ({name})",
                    description=profile_data.get("description"),
                    meta_entries=[],
                    attributes=[
                        (attr_name, resolve_attribute(attr_name, attr_data, data["dictionary"]))
                        for attr_name, attr_data in (profile_data.get("attributes") or {}).items()
                        if not attr_name.startswith("$")
                    ],
                    object_links=object_links_from_class_pages,
                )
                if extra_sections:
                    # Insert "Applies to" before ## Attributes (or at end if no attributes).
                    if "## Attributes" in page:
                        page = page.replace("## Attributes", f"{extra_sections.strip()}\n\n## Attributes")
                    else:
                        page = page.rstrip("\n") + "\n" + extra_sections
                write_file(output_dir / data["slug"] / "profiles" / f"{name_to_slug(name)}.md", page)

            for name, extension_data in data["extensions"].items():
                extension_slug = name_to_slug(name)
                extension_output_dir = output_dir / data["slug"] / "extensions" / extension_slug
                extension_dictionary = merge_dictionaries(
                    data["dictionary"],
                    extension_data.get("dictionary"),
                )
                extension_events = extension_data["events"]
                extension_objects = extension_data["objects"]
                extension_profiles = extension_data["profiles"]
                extension_object_links = build_name_link_map(
                    data["objects"].keys(),
                    prefix="../../../objects/",
                )
                extension_object_links.update(
                    build_name_link_map(extension_objects.keys(), prefix="../objects/")
                )
                extension_class_links = build_name_link_map(
                    class_names,
                    prefix="../../../classes/",
                )
                extension_class_links.update(
                    build_name_link_map(extension_events.keys(), prefix="../events/")
                )
                qualified_extension_profiles = {
                    f"{name}/{profile_name}": profile_data
                    for profile_name, profile_data in extension_profiles.items()
                }
                extension_profile_links = build_name_link_map(
                    data["profiles"].keys(),
                    prefix="../../../profiles/",
                )
                extension_profile_links.update(
                    build_name_link_map(extension_profiles.keys(), prefix="../profiles/")
                )
                extension_profile_links.update(
                    {
                        qualified_name: f"../profiles/{name_to_slug(profile_name)}.md"
                        for qualified_name, profile_name in (
                            (f"{name}/{profile_name}", profile_name)
                            for profile_name in extension_profiles
                        )
                    }
                )
                extension_profile_data = {
                    **data["profiles"],
                    **extension_profiles,
                    **qualified_extension_profiles,
                }

                write_file(
                    extension_output_dir / "index.md",
                    build_extension_index_page(name, extension_data),
                )

                for event_name, event_data in extension_events.items():
                    extends = event_data.get("extends")
                    parent = lookup_schema(
                        extends or "",
                        data["classes"],
                        data["intermediates"],
                        extension_events,
                    )
                    parent_category_key = (
                        parent.get("category_key")
                        if parent is not None
                        else ""
                    )
                    category_info = data["categories"].get(parent_category_key, {})
                    event_profiles = resolve_profiles(
                        event_data,
                        extension_events,
                        data["classes"],
                        data["intermediates"],
                    )
                    constraints = event_data.get("constraints")
                    if not constraints and parent is not None:
                        constraints = parent.get("constraints")
                    associations = event_data.get("associations")
                    if not associations and parent is not None:
                        associations = parent.get("associations")
                    page = render_entity_page(
                        title=f"{event_data.get('caption') or event_name} ({event_name})",
                        description=event_data.get("description"),
                        meta_entries=[
                            ("Event UID", f"`{event_data['uid']}`" if event_data.get("uid") is not None else ""),
                            (
                                "Category",
                                category_info.get("caption") or parent_category_key or "",
                            ),
                            (
                                "Extends",
                                format_doc_link(
                                    extends,
                                    parent or {},
                                    target=extension_class_links.get(
                                        extends,
                                        f"../../../classes/{name_to_slug(extends)}.md",
                                    ),
                                    include_schema_name=True,
                                )
                                if extends
                                else "",
                            ),
                            (
                                "Profiles",
                                format_named_links(
                                    event_profiles,
                                    data_by_name=extension_profile_data,
                                    link_by_name=extension_profile_links,
                                )
                                if event_profiles
                                else "",
                            ),
                        ],
                        constraints=constraints,
                        associations=associations,
                        inherited_attributes=collect_inherited_attributes(
                            event_data,
                            extension_dictionary,
                            extension_events,
                            data["classes"],
                            data["intermediates"],
                        ),
                        attributes=[
                            (
                                attr_name,
                                resolve_attribute(attr_name, attr_data, extension_dictionary),
                            )
                            for attr_name, attr_data in (event_data.get("attributes") or {}).items()
                            if not attr_name.startswith("$")
                        ],
                        object_links=extension_object_links,
                    )
                    write_file(
                        extension_output_dir / "events" / f"{name_to_slug(event_name)}.md",
                        page,
                    )

                for object_name, object_data in extension_objects.items():
                    extends = object_data.get("extends")
                    object_profiles = list(object_data.get("profiles") or [])
                    parent = lookup_schema(extends or "", data["objects"], extension_objects)
                    page = render_entity_page(
                        title=f"{object_data.get('caption') or object_name} ({object_name})",
                        description=object_data.get("description"),
                        meta_entries=[
                            (
                                "Extends",
                                format_doc_link(
                                    extends,
                                    parent or {},
                                    target=(
                                        f"../../../objects/{name_to_slug(extends)}.md"
                                        if extends in data["objects"]
                                        else f"../objects/{name_to_slug(extends)}.md"
                                    ),
                                    include_schema_name=True,
                                )
                                if extends
                                else "",
                            ),
                            (
                                "Profiles",
                                format_named_links(
                                    object_profiles,
                                    data_by_name=extension_profile_data,
                                    link_by_name=extension_profile_links,
                                )
                                if object_profiles
                                else "",
                            ),
                        ],
                        inherited_attributes=collect_inherited_attributes(
                            object_data,
                            extension_dictionary,
                            data["objects"],
                            extension_objects,
                        ),
                        attributes=[
                            (
                                attr_name,
                                resolve_attribute(attr_name, attr_data, extension_dictionary),
                            )
                            for attr_name, attr_data in (object_data.get("attributes") or {}).items()
                            if not attr_name.startswith("$")
                        ],
                        object_links=extension_object_links,
                    )
                    write_file(
                        extension_output_dir / "objects" / f"{name_to_slug(object_name)}.md",
                        page,
                    )

                extension_profile_to_entities: dict[str, list[str]] = {}
                for entity_name, entity_data in {**extension_events, **extension_objects}.items():
                    for profile_name in entity_data.get("profiles") or []:
                        extension_profile_to_entities.setdefault(profile_name, []).append(
                            entity_data.get("caption") or entity_name
                        )
                for profile_name, consumers in extension_profile_to_entities.items():
                    extension_profile_to_entities[profile_name] = sorted(
                        set(consumers),
                        key=str.casefold,
                    )

                for profile_name, profile_data in extension_profiles.items():
                    applies_to = sorted(
                        {
                            *extension_profile_to_entities.get(profile_name, []),
                            *extension_profile_to_entities.get(f"{name}/{profile_name}", []),
                        },
                        key=str.casefold,
                    )
                    applies_section = (
                        "\n".join(f"- {item}" for item in applies_to)
                        if applies_to
                        else ""
                    )
                    extra_sections = ""
                    if applies_section:
                        extra_sections = f"\n\n## Applies to\n\n{applies_section}\n"
                    page = render_entity_page(
                        title=f"{profile_data.get('caption') or profile_name} ({profile_name})",
                        description=profile_data.get("description"),
                        meta_entries=[],
                        attributes=[
                            (
                                attr_name,
                                resolve_attribute(attr_name, attr_data, extension_dictionary),
                            )
                            for attr_name, attr_data in (profile_data.get("attributes") or {}).items()
                            if not attr_name.startswith("$")
                        ],
                        object_links=extension_object_links,
                    )
                    if extra_sections:
                        if "## Attributes" in page:
                            page = page.replace("## Attributes", f"{extra_sections.strip()}\n\n## Attributes")
                        else:
                            page = page.rstrip("\n") + "\n" + extra_sections
                    write_file(
                        extension_output_dir / "profiles" / f"{name_to_slug(profile_name)}.md",
                        page,
                    )

        print(f"Generated OCSF skill in {output_dir}")
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)


if __name__ == "__main__":
    main()
