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
from pathlib import Path

import httpx
from markdownify import markdownify
from packaging.version import Version


OCSF_SCHEMA_REPO = "https://github.com/ocsf/ocsf-schema.git"
OCSF_DOCS_API = "https://api.github.com/repos/ocsf/ocsf-docs/contents"
OCSF_DOCS_RAW = "https://raw.githubusercontent.com/ocsf/ocsf-docs/main"
HTTP_HEADERS = {
    "User-Agent": "tenzir-skills-generator",
    "Accept": "application/json",
}


def version_to_slug(version: str) -> str:
    return version.replace(".", "-")


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


def clone_schema(version: str, temp_root: Path) -> Path:
    repo_dir = temp_root / f"ocsf-schema-{version}"
    for ref in (f"v{version}", version):
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", "--branch", ref, OCSF_SCHEMA_REPO, str(repo_dir)],
                check=True,
                capture_output=True,
                text=True,
            )
            return repo_dir
        except subprocess.CalledProcessError:
            pass
    raise RuntimeError(f"Failed to clone OCSF schema for version {version}")


def load_directory_json(directory: Path) -> dict[str, dict]:
    if not directory.exists():
        return {}
    return {
        path.stem: read_json(path)
        for path in sorted(directory.glob("*.json"))
        if path.is_file()
    }


def load_classes(schema_dir: Path) -> dict[str, dict]:
    classes: dict[str, dict] = {}
    events_dir = schema_dir / "events"
    if not events_dir.exists():
        return classes

    base_event_path = events_dir / "base_event.json"
    if base_event_path.exists():
        classes["base_event"] = read_json(base_event_path)

    for category_dir in sorted(path for path in events_dir.iterdir() if path.is_dir()):
        category_key = category_dir.name
        for entry in sorted(category_dir.glob("*.json")):
            class_name = entry.stem
            if class_name == category_key:
                continue
            data = read_json(entry)
            data["category_key"] = category_key
            classes[class_name] = data
    return classes


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


def render_entity_page(
    *,
    title: str,
    description: str | None,
    meta_entries: list[tuple[str, object]],
    attributes: list[tuple[str, dict]],
) -> str:
    lines = [f"# {title}", ""]
    if description:
        lines.extend([clean_description(description), ""])
    meta = format_meta_list(meta_entries)
    if meta:
        lines.extend([meta, ""])
    if attributes:
        lines.extend(["## Attributes", ""])
        for attr_name, attr_data in attributes:
            lines.append(format_attribute(attr_name, attr_data))
    return f"{re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip()}\n"


def build_version_docs(version: str, schema_dir: Path) -> dict:
    slug = version_to_slug(version)
    categories = read_json(schema_dir / "categories.json").get("attributes", {})
    dictionary = read_json(schema_dir / "dictionary.json")
    classes = load_classes(schema_dir)
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


def generate_version_overview(version_data: dict) -> str:
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
    return "\n".join(lines) + "\n"


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
    versions = [args.version] if args.version else list_stable_versions()
    if args.latest_only:
        versions = [versions[-1]]

    output_dir = Path(args.output_dir).resolve()
    temp_root = Path(tempfile.mkdtemp(prefix="ocsf-skill-"))
    version_docs: list[dict] = []

    try:
        for version in versions:
            schema_dir = clone_schema(version, temp_root)
            version_docs.append(build_version_docs(version, schema_dir))

        latest = version_docs[-1]
        with httpx.Client(headers=HTTP_HEADERS, follow_redirects=True, timeout=30.0) as client:
            faqs = fetch_pages(client, "faqs")
            articles = fetch_pages(client, "articles")
            overview = fetch_text(client, f"{OCSF_DOCS_RAW}/overview/understanding-ocsf.md")

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
                    "Start with [index.md](index.md) to discover available versions. Use the latest stable version unless the user requests a specific one. Stick to one version per answer.",
                    "",
                    "The file tree follows this layout:",
                    "",
                    "```",
                    "index.md",
                    "introduction.md",
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
                    "## Documentation map",
                    "",
                    "### [Introduction](introduction.md)",
                    "",
                    f"### [Latest classes]({latest['slug']}/classes.md)",
                    "",
                    f"### [Latest objects]({latest['slug']}/objects.md)",
                    "",
                    f"### [Latest profiles]({latest['slug']}/profiles.md)",
                    "",
                    f"### [Latest extensions]({latest['slug']}/extensions.md)",
                    "",
                    f"### [Latest types]({latest['slug']}/types.md)",
                    "",
                    "### [FAQs](faqs.md)",
                    "",
                    "### [Articles](articles.md)",
                    "",
                ]
            ),
        )

        write_file(
            output_dir / "index.md",
            "\n".join(
                [
                    "# OCSF",
                    "",
                    "Generated from the official [`ocsf-schema`](https://github.com/ocsf/ocsf-schema) and [`ocsf-docs`](https://github.com/ocsf/ocsf-docs) repositories.",
                    "",
                    "## Versions",
                    "",
                    *[f"- [{data['version']}]({data['slug']}.md)" for data in version_docs],
                    "",
                ]
            ),
        )

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

        for data in version_docs:
            write_file(output_dir / f"{data['slug']}.md", generate_version_overview(data))
            write_file(output_dir / data["slug"] / "classes.md", generate_classes_overview(data))
            write_file(output_dir / data["slug"] / "objects.md", generate_named_overview(data, "Objects", "objects"))
            write_file(output_dir / data["slug"] / "profiles.md", generate_named_overview(data, "Profiles", "profiles"))
            write_file(output_dir / data["slug"] / "extensions.md", generate_extensions_overview(data))
            write_file(output_dir / data["slug"] / "types.md", generate_types_overview(data))

            for name, class_data in data["classes"].items():
                page = render_entity_page(
                    title=f"{class_data.get('caption') or name} ({name})",
                    description=class_data.get("description"),
                    meta_entries=[
                        ("UID", f"`{class_data['uid']}`" if class_data.get("uid") else ""),
                        (
                            "Category",
                            data["categories"].get(class_data.get("category_key"), {}).get("caption")
                            or class_data.get("category_key")
                            or "",
                        ),
                        ("Extends", f"`{class_data['extends']}`" if class_data.get("extends") else ""),
                    ],
                    attributes=[
                        (attr_name, resolve_attribute(attr_name, attr_data, data["dictionary"]))
                        for attr_name, attr_data in (class_data.get("attributes") or {}).items()
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
                    ],
                )
                write_file(output_dir / data["slug"] / "objects" / f"{name_to_slug(name)}.md", page)

            for name, profile_data in data["profiles"].items():
                page = render_entity_page(
                    title=f"{profile_data.get('caption') or name} ({name})",
                    description=profile_data.get("description"),
                    meta_entries=[],
                    attributes=[
                        (attr_name, resolve_attribute(attr_name, attr_data, data["dictionary"]))
                        for attr_name, attr_data in (profile_data.get("attributes") or {}).items()
                    ],
                )
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
