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


@dataclass(frozen=True, slots=True)
class VersionSpec:
    version: str
    ref: str
    is_stable: bool


def version_to_slug(version: str) -> str:
    return f"v{version}"


def name_to_slug(name: str) -> str:
    return name.replace("/", "_")


def clean_description(text: str) -> str:
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
            class_name = entry.stem
            if class_name == category_key:
                data = read_json(entry)
                data["category_key"] = category_key
                intermediates[class_name] = data
                continue
            data = read_json(entry)
            data["category_key"] = category_key
            classes[class_name] = data
    return classes, intermediates


def resolve_profiles(
    class_data: dict,
    all_classes: dict[str, dict],
    intermediates: dict[str, dict],
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
        current = all_classes.get(extends) or intermediates.get(extends)
    return profiles


def load_extensions(schema_dir: Path) -> dict[str, dict]:
    result: dict[str, dict] = {}
    extensions_dir = schema_dir / "extensions"
    if not extensions_dir.exists():
        return result

    for extension_dir in sorted(path for path in extensions_dir.iterdir() if path.is_dir()):
        meta_path = extension_dir / "extension.json"
        if not meta_path.exists():
            continue
        result[extension_dir.name] = {
            "meta": read_json(meta_path),
            "objects": load_directory_json(extension_dir / "objects"),
            "profiles": load_directory_json(extension_dir / "profiles"),
            "events": load_directory_json(extension_dir / "events"),
        }
    return result


def resolve_attribute(name: str, local_data: object, dictionary: dict) -> dict:
    base = dictionary.get("attributes", {}).get(name, {})
    if not isinstance(base, dict):
        base = {}
    if not isinstance(local_data, dict):
        local_data = {}
    return {**base, **local_data}


def format_attribute(name: str, data: dict) -> str:
    desc = clean_description(data.get("description") or data.get("caption") or "")
    lines = [f"### `{name}`", ""]
    meta = format_meta_list(
        [
            ("Type", f"`{data['object_type']}`" if data.get("object_type") else f"`{data['type']}`" if data.get("type") else ""),
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
            enum_desc = clean_description(value.get("description", ""))
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
    class_data: dict,
    all_classes: dict[str, dict],
    intermediates: dict[str, dict],
    dictionary: dict,
) -> list[tuple[str, list[tuple[str, str]]]]:
    """Walk the extends chain and collect required/recommended attributes
    from each ancestor.  Returns a list of (ancestor_name, [(attr, requirement), ...])."""
    result: list[tuple[str, list[tuple[str, str]]]] = []
    own_attrs = set((class_data.get("attributes") or {}).keys())
    extends = class_data.get("extends")
    while extends:
        parent = all_classes.get(extends) or intermediates.get(extends)
        if parent is None:
            break
        parent_caption = parent.get("caption") or extends
        parent_attrs = parent.get("attributes") or {}
        important: list[tuple[str, str]] = []
        for attr_name, attr_data in parent_attrs.items():
            if attr_name.startswith("$") or attr_name in own_attrs:
                continue
            resolved = resolve_attribute(attr_name, attr_data, dictionary)
            requirement = resolved.get("requirement", "")
            if requirement in ("required", "recommended"):
                important.append((attr_name, requirement))
                own_attrs.add(attr_name)
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
) -> str:
    lines = [f"# {title}", ""]
    if description:
        lines.extend([clean_description(description), ""])
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
            lines.append(format_attribute(attr_name, attr_data))
    return f"{re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip()}\n"


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
        category_classes = sorted(
            (
                (name, data)
                for name, data in version_data["classes"].items()
                if data.get("category_key") == category_key
            ),
            key=lambda item: (item[1].get("caption") or item[0]).casefold(),
        )
        if not category_classes:
            continue
        lines.extend([f"## {category['caption']}", "", clean_description(category.get("description", "")), ""])
        for name, data in category_classes:
            lines.append(f"- [{data.get('caption') or name}](classes/{name_to_slug(name)}.md)")
        lines.append("")
    if "base_event" in version_data["classes"]:
        lines.extend(["## Base Event", "", "- [Base Event](classes/base_event.md)", ""])
    return f"{re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip()}\n"


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

    return f"{re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip()}\n"


def generate_extensions_overview(version_data: dict) -> str:
    lines = [f"# Extensions ({version_data['version']})", ""]
    for name, data in sorted(
        version_data["extensions"].items(),
        key=lambda item: (item[1]["meta"].get("caption") or item[0]).casefold(),
    ):
        lines.append(f"- [{data['meta'].get('caption') or name}](extensions/{name_to_slug(name)}.md)")
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
    return f"{re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip()}\n"


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
                    "Look up OCSF reference documentation and answer from those sources. Only state facts from files you read. Never invent schema details. If the documentation does not cover the question, say so.",
                    "",
                    "## Reading the documentation",
                    "",
                    "Use the version links in this file to pick a schema release. Use the latest stable version unless the user requests a specific one. Stick to one version per answer.",
                    "",
                    "A development snapshot is available when the upstream `main` branch reports a `-dev` schema version. Treat that version as unreleased.",
                    "",
                    "The file tree follows this layout:",
                    "",
                    "```",
                    "introduction.md",
                    "introduction/{section}.md",
                    "faqs.md",
                    "faqs/{slug}.md",
                    "articles.md",
                    "articles/{slug}.md",
                    "{version}.md",
                    "{version}/classes.md",
                    "{version}/classes/{name}.md",
                    "{version}/objects.md",
                    "{version}/objects/{name}.md",
                    "{version}/profiles.md",
                    "{version}/profiles/{name}.md",
                    "{version}/extensions.md",
                    "{version}/extensions/{name}.md",
                    "{version}/types.md",
                    "```",
                    "",
                    "## Domain knowledge",
                    "",
                    "### Core concepts",
                    "",
                    "**Attributes** are named fields with a data type. Every OCSF field has a requirement level: required, recommended, or optional.",
                    "",
                    "**Objects** group related attributes into reusable structures. Objects can nest other objects.",
                    "",
                    "**Event classes** define schemas for specific security events. Each class belongs to a category and inherits from Base Event.",
                    "",
                    "**Base Event** provides universal attributes and serves as a catch-all when no more specific class fits.",
                    "",
                    "**Profiles** are mix-ins that add cross-cutting attributes. A class can apply multiple profiles.",
                    "",
                    "**Extensions** add vendor-specific attributes without modifying the core schema.",
                    "",
                    "### Event categories",
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
                    "- Suffixes carry meaning: `_id`, `_uid`, `_uuid`, `_name`, `_time`, `_dt`.",
                    "",
                    "## Answering principles",
                    "",
                    "- Read before answering. Every claim must trace back to a file you read.",
                    "- Use the category table to narrow scope before diving into class pages.",
                    "- Consult [faqs.md](faqs.md) when the question is about schema choices or ambiguity.",
                    "- Read multiple candidates for selection questions and explain trade-offs.",
                    "",
                    "## Versions",
                    "",
                    *[f"- [{data['version']}]({data['slug']}.md)" for data in version_docs],
                    "",
                    "## Documentation map",
                    "",
                    "### [Introduction](introduction.md)",
                    "",
                    f"### [Latest stable classes]({latest_reference['slug']}/classes.md)",
                    "",
                    f"### [Latest stable objects]({latest_reference['slug']}/objects.md)",
                    "",
                    f"### [Latest stable profiles]({latest_reference['slug']}/profiles.md)",
                    "",
                    f"### [Latest stable extensions]({latest_reference['slug']}/extensions.md)",
                    "",
                    f"### [Latest stable types]({latest_reference['slug']}/types.md)",
                    "",
                    *(
                        [
                            f"### [Latest dev snapshot]({latest_dev['slug']}.md)",
                        ]
                        if latest_dev
                        else []
                    ),
                    "",
                    "### [FAQs](faqs.md)",
                    "",
                    "### [Articles](articles.md)",
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
                        ("Extends", f"`{class_data['extends']}`" if class_data.get("extends") else ""),
                        (
                            "Profiles",
                            ", ".join(f"`{p}`" for p in class_profiles) if class_profiles else "",
                        ),
                    ],
                    constraints=constraints,
                    associations=associations,
                    inherited_attributes=collect_inherited_attributes(
                        class_data, data["classes"], data["intermediates"], data["dictionary"],
                    ),
                    attributes=[
                        (attr_name, resolve_attribute(attr_name, attr_data, data["dictionary"]))
                        for attr_name, attr_data in (class_data.get("attributes") or {}).items()
                        if not attr_name.startswith("$")
                    ],
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
                        ("Extends", f"`{intermediate_data['extends']}`" if intermediate_data.get("extends") else ""),
                        (
                            "Profiles",
                            ", ".join(f"`{p}`" for p in intermediate_profiles) if intermediate_profiles else "",
                        ),
                    ],
                    constraints=intermediate_data.get("constraints"),
                    associations=intermediate_data.get("associations"),
                    inherited_attributes=collect_inherited_attributes(
                        intermediate_data, data["classes"], data["intermediates"], data["dictionary"],
                    ),
                    attributes=[
                        (attr_name, resolve_attribute(attr_name, attr_data, data["dictionary"]))
                        for attr_name, attr_data in (intermediate_data.get("attributes") or {}).items()
                        if not attr_name.startswith("$")
                    ],
                )
                write_file(output_dir / data["slug"] / "classes" / f"{name_to_slug(name)}.md", page)

            for name, object_data in data["objects"].items():
                page = render_entity_page(
                    title=f"{object_data.get('caption') or name} ({name})",
                    description=object_data.get("description"),
                    meta_entries=[("Extends", f"`{object_data['extends']}`" if object_data.get("extends") else "")],
                    attributes=[
                        (attr_name, resolve_attribute(attr_name, attr_data, data["dictionary"]))
                        for attr_name, attr_data in (object_data.get("attributes") or {}).items()
                        if not attr_name.startswith("$")
                    ],
                )
                write_file(output_dir / data["slug"] / "objects" / f"{name_to_slug(name)}.md", page)

            # Build reverse mapping: profile name → list of classes that register for it.
            profile_to_classes: dict[str, list[str]] = {}
            for cname, cdata in {**data["classes"], **data["intermediates"]}.items():
                for pname in cdata.get("profiles") or []:
                    profile_to_classes.setdefault(pname, []).append(
                        cdata.get("caption") or cname
                    )
            for pname in profile_to_classes:
                profile_to_classes[pname].sort(key=str.casefold)

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
                )
                if extra_sections:
                    # Insert "Applies to" before ## Attributes (or at end if no attributes).
                    if "## Attributes" in page:
                        page = page.replace("## Attributes", f"{extra_sections.strip()}\n\n## Attributes")
                    else:
                        page = page.rstrip("\n") + "\n" + extra_sections
                write_file(output_dir / data["slug"] / "profiles" / f"{name_to_slug(name)}.md", page)

            for name, extension_data in data["extensions"].items():
                lines = [f"# {extension_data['meta'].get('caption') or name}", ""]
                desc = clean_description(extension_data["meta"].get("description", ""))
                if desc:
                    lines.extend([desc, ""])
                lines.append(f"- **Name**: `{extension_data['meta'].get('name') or name}`")
                if extension_data["meta"].get("uid") is not None:
                    lines.append(f"- **UID**: `{extension_data['meta']['uid']}`")
                lines.append("")

                if extension_data["events"]:
                    lines.extend(["## Events", ""])
                    for event_name, event_data in sorted(
                        extension_data["events"].items(),
                        key=lambda item: (item[1].get("caption") or item[0]).casefold(),
                    ):
                        suffix = f" - {event_data['caption']}" if event_data.get("caption") else ""
                        lines.append(f"- `{event_name}`{suffix}")
                    lines.append("")

                if extension_data["objects"]:
                    lines.extend(["## Objects", ""])
                    for object_name, object_data in sorted(
                        extension_data["objects"].items(),
                        key=lambda item: (item[1].get("caption") or item[0]).casefold(),
                    ):
                        suffix = f" - {object_data['caption']}" if object_data.get("caption") else ""
                        lines.append(f"- `{object_name}`{suffix}")
                    lines.append("")

                if extension_data["profiles"]:
                    lines.extend(["## Profiles", ""])
                    for profile_name, profile_data in sorted(
                        extension_data["profiles"].items(),
                        key=lambda item: (item[1].get("caption") or item[0]).casefold(),
                    ):
                        suffix = f" - {profile_data['caption']}" if profile_data.get("caption") else ""
                        lines.append(f"- `{profile_name}`{suffix}")
                    lines.append("")

                write_file(
                    output_dir / data["slug"] / "extensions" / f"{name_to_slug(name)}.md",
                    "\n".join(lines) + "\n",
                )

        print(f"Generated OCSF skill in {output_dir}")
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)


if __name__ == "__main__":
    main()
