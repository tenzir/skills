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
import hashlib
import posixpath
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx
import yaml


ECS_REPO = "elastic/ecs"
GITHUB_API = f"https://api.github.com/repos/{ECS_REPO}"
GITHUB_RAW = f"https://raw.githubusercontent.com/{ECS_REPO}"
GITHUB_BLOB = f"https://github.com/{ECS_REPO}/blob"
GITHUB_TREE = f"https://github.com/{ECS_REPO}/tree"
HTTP_HEADERS = {
    "User-Agent": "tenzir-ecs-generator",
    "Accept": "application/vnd.github+json",
}
STABLE_TAG_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
REFERENCE_PAGE_RE = re.compile(r"^/reference/ecs-([a-z0-9_]+)\.md$")
FIELD_ANCHOR_RE = re.compile(r"^#field-([A-Za-z0-9_-]+)$")


class NoAliasSafeDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:
        return True


@dataclass(frozen=True, slots=True)
class SourceRef:
    tag: str
    version: str
    sha: str
    release_name: str
    release_url: str
    published_at: str


@dataclass(frozen=True, slots=True)
class SourceDoc:
    source_path: str
    output_path: Path
    title: str


CURATED_DOCS = (
    SourceDoc("schemas/README.md", Path("docs/schema-format.md"), "Schema format"),
    SourceDoc("generated/README.md", Path("docs/artifacts.md"), "Generated artifacts"),
    SourceDoc("docs/reference/ecs-principles-design.md", Path("docs/design-principles.md"), "Design principles"),
    SourceDoc(
        "docs/reference/ecs-principles-implementation.md",
        Path("docs/implementation-patterns.md"),
        "Implementation patterns",
    ),
    SourceDoc("docs/reference/ecs-conventions.md", Path("docs/conventions.md"), "Conventions"),
    SourceDoc("docs/reference/ecs-custom-fields-in-ecs.md", Path("docs/custom-fields.md"), "Custom fields"),
    SourceDoc(
        "docs/reference/ecs-category-field-values-reference.md",
        Path("docs/categorization-fields.md"),
        "Categorization fields",
    ),
    SourceDoc(
        "docs/reference/ecs-using-categorization-fields.md",
        Path("docs/categorization-usage.md"),
        "Using categorization fields",
    ),
    SourceDoc(
        "docs/reference/ecs-mapping-network-events.md",
        Path("docs/mapping-network-events.md"),
        "Mapping network events",
    ),
    SourceDoc("docs/reference/ecs-opentelemetry.md", Path("docs/opentelemetry.md"), "ECS and OpenTelemetry"),
    SourceDoc("docs/reference/ecs-cloud-usage.md", Path("docs/usage/cloud.md"), "Cloud usage"),
    SourceDoc("docs/reference/ecs-service-usage.md", Path("docs/usage/service.md"), "Service usage"),
    SourceDoc("docs/reference/ecs-threat-usage.md", Path("docs/usage/threat.md"), "Threat usage"),
    SourceDoc("docs/reference/ecs-user-usage.md", Path("docs/usage/user.md"), "User usage"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--ref",
        default=None,
        help="Elastic ECS stable release tag to build from, for example v9.4.0 (default: latest stable release)",
    )
    return parser.parse_args()


def normalize_tag(ref: str) -> str:
    tag = ref if ref.startswith("v") else f"v{ref}"
    if not STABLE_TAG_RE.fullmatch(tag):
        raise ValueError(f"ECS ref must be a stable release tag like v9.4.0, got {ref!r}")
    return tag


def resolve_commit(client: httpx.Client, tag: str) -> str:
    response = client.get(f"{GITHUB_API}/commits/{tag}")
    response.raise_for_status()
    sha = response.json().get("sha")
    if not isinstance(sha, str) or not sha:
        raise RuntimeError(f"GitHub did not return a commit SHA for {tag}")
    return sha


def fetch_release_for_tag(client: httpx.Client, tag: str) -> dict[str, Any]:
    response = client.get(f"{GITHUB_API}/releases/tags/{tag}")
    response.raise_for_status()
    data = response.json()
    if data.get("draft") or data.get("prerelease"):
        raise ValueError(f"ECS ref must point to a published stable release, got {tag}")
    return data


def resolve_latest_release(client: httpx.Client) -> dict[str, Any]:
    response = client.get(f"{GITHUB_API}/releases", params={"per_page": 100})
    response.raise_for_status()
    for release in response.json():
        tag = release.get("tag_name")
        if (
            isinstance(tag, str)
            and STABLE_TAG_RE.fullmatch(tag)
            and not release.get("draft")
            and not release.get("prerelease")
        ):
            return release
    raise RuntimeError("Could not find a stable ECS release")


def resolve_source_ref(client: httpx.Client, requested_ref: str | None) -> SourceRef:
    release = fetch_release_for_tag(client, normalize_tag(requested_ref)) if requested_ref else resolve_latest_release(client)
    tag = release["tag_name"]
    version = tag.removeprefix("v")
    sha = resolve_commit(client, tag)
    return SourceRef(
        tag=tag,
        version=version,
        sha=sha,
        release_name=release.get("name") or tag,
        release_url=release.get("html_url") or f"https://github.com/{ECS_REPO}/releases/tag/{tag}",
        published_at=release.get("published_at") or "",
    )


def raw_url(source: SourceRef, path: str) -> str:
    return f"{GITHUB_RAW}/{source.sha}/{path}"


def blob_url(source: SourceRef, path: str) -> str:
    return f"{GITHUB_BLOB}/{source.sha}/{path}"


def tree_url(source: SourceRef, path: str) -> str:
    return f"{GITHUB_TREE}/{source.sha}/{path}"


def upstream_url(source: SourceRef, path: str) -> str:
    filename = posixpath.basename(path)
    return blob_url(source, path) if "." in filename else tree_url(source, path)


def fetch_text(client: httpx.Client, source: SourceRef, path: str) -> str:
    response = client.get(raw_url(source, path))
    response.raise_for_status()
    return response.text if response.text.endswith("\n") else f"{response.text}\n"


def fetch_yaml(client: httpx.Client, source: SourceRef, path: str) -> Any:
    return yaml.safe_load(fetch_text(client, source, path))


def clean_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    return text[end + len("\n---\n") :]


def slugify(value: str, *, prefix_at: bool = False) -> str:
    text = value.strip()
    if prefix_at:
        text = text.replace("@", "at_")
    text = re.sub(r"[^A-Za-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text.strip("_").lower() or "index"


def unique_slug(value: str, used: set[str]) -> str:
    slug = slugify(value, prefix_at=True)
    if slug not in used:
        used.add(slug)
        return slug
    suffix = hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]
    slug = f"{slug}_{suffix}"
    used.add(slug)
    return slug


def fieldset_name_for_field(field_name: str) -> str:
    if field_name.startswith("@") or "." not in field_name:
        return "base"
    return field_name.split(".", 1)[0]


def field_path(slug: str) -> str:
    return f"fields/{slug}.yaml"


def fieldset_path(name: str) -> str:
    return f"fieldsets/{name}.yaml"


def rel_link(from_path: Path, target_path: Path) -> str:
    start = from_path.parent.as_posix() or "."
    return posixpath.relpath(target_path.as_posix(), start=start)


def split_href(href: str) -> tuple[str, str]:
    for separator in ("#", "?"):
        if separator in href:
            base, suffix = href.split(separator, 1)
            return base, f"{separator}{suffix}"
    return href, ""


def source_relative_path(source_path: str, href_base: str) -> str:
    if href_base.startswith("/reference/"):
        return f"docs{href_base}"
    if href_base.startswith("/"):
        return href_base.lstrip("/")
    return posixpath.normpath(posixpath.join(posixpath.dirname(source_path), href_base))


def rewrite_markdown_links(
    text: str,
    *,
    source: SourceRef,
    source_path: str,
    output_path: Path,
    docs_by_source: dict[str, Path],
    field_slugs_by_dashed_name: dict[str, str],
    fieldset_names: set[str],
) -> str:
    def replace(match: re.Match[str]) -> str:
        label, href = match.groups()
        if href.startswith(("http://", "https://", "mailto:", "tel:", "elasticsearch://", "docs-content://", "#")):
            return match.group(0)

        href_base, suffix = split_href(href)

        if href_base.startswith("/reference/"):
            source_target = source_relative_path(source_path, href_base)
            target = docs_by_source.get(source_target)
            if target is not None:
                return f"[{label}]({rel_link(output_path, target)}{suffix})"

            if href_base.startswith("/reference/ecs-allowed-values-event-"):
                return f"[{label}]({rel_link(output_path, Path('categorization.yaml'))})"

            page_match = REFERENCE_PAGE_RE.fullmatch(href_base)
            if page_match:
                field_anchor = FIELD_ANCHOR_RE.fullmatch(suffix)
                if field_anchor:
                    field_slug = field_slugs_by_dashed_name.get(field_anchor.group(1))
                    if field_slug:
                        return f"[{label}]({rel_link(output_path, Path(field_path(field_slug)))})"

                fieldset_name = page_match.group(1)
                if fieldset_name in fieldset_names:
                    return f"[{label}]({rel_link(output_path, Path(fieldset_path(fieldset_name)))})"

        if href_base:
            source_target = source_relative_path(source_path, href_base)
            target = docs_by_source.get(source_target)
            if target is not None:
                return f"[{label}]({rel_link(output_path, target)}{suffix})"
            return f"[{label}]({upstream_url(source, source_target)}{suffix})"

        return match.group(0)

    return MARKDOWN_LINK_RE.sub(replace, text)


def dump_yaml(data: Any) -> str:
    return yaml.dump(data, Dumper=NoAliasSafeDumper, sort_keys=False, allow_unicode=True, width=1000)


def summary_description(record: dict[str, Any]) -> str | None:
    value = record.get("short") or record.get("description")
    if not isinstance(value, str):
        return None
    return re.sub(r"\s+", " ", value).strip()


def normalize_summary_value(value: Any) -> Any:
    if isinstance(value, list):
        return [normalize_summary_value(item) for item in value]
    if isinstance(value, dict):
        result: dict[str, Any] = {}
        for key, item in value.items():
            if key == "short":
                result["description"] = normalize_summary_value(item)
            elif key == "short_override":
                result["description_override"] = normalize_summary_value(item)
            else:
                result[key] = normalize_summary_value(item)
        return result
    return value


def normalize_generated_yaml_value(value: Any) -> Any:
    if isinstance(value, list):
        return [normalize_generated_yaml_value(item) for item in value]
    if isinstance(value, dict):
        result: dict[str, Any] = {}
        for key, item in value.items():
            if key == "version":
                continue
            if key == "normalize" and item == []:
                continue
            if key == "short":
                if "description" not in value:
                    result["description"] = normalize_generated_yaml_value(item)
            elif key == "short_override":
                result["description_override"] = normalize_generated_yaml_value(item)
            else:
                result[key] = normalize_generated_yaml_value(item)
        return result
    return value


def summarize_field(name: str, record: dict[str, Any], slug: str) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "name": name,
        "path": field_path(slug),
        "fieldset": fieldset_name_for_field(name),
        "type": record.get("type"),
        "description": summary_description(record),
    }
    for key in ("required", "original_fieldset", "normalize", "beta", "alpha"):
        if key in record:
            summary[key] = record[key]
    return {key: value for key, value in summary.items() if value not in (None, "", [])}


def build_fields(
    flat: dict[str, dict[str, Any]],
    field_slugs: dict[str, str],
    source: SourceRef,
) -> tuple[dict[Path, str], list[dict[str, Any]]]:
    docs: dict[Path, str] = {}
    summaries: list[dict[str, Any]] = []
    for name in sorted(flat, key=str.casefold):
        record = flat[name]
        slug = field_slugs[name]
        field_record: dict[str, Any] = {
            "field": name,
            "version": source.version,
            "fieldset": fieldset_name_for_field(name),
            **record,
        }
        docs[Path(field_path(slug))] = dump_yaml(normalize_generated_yaml_value(field_record))
        summaries.append(summarize_field(name, record, slug))

    docs[Path("fields.yaml")] = dump_yaml(
        {"fields": summaries}
    )
    return docs, summaries


def summarize_fieldset_field(name: str, record: dict[str, Any], field_slugs: dict[str, str]) -> dict[str, Any]:
    entry: dict[str, Any] = {
        "name": name,
        "type": record.get("type"),
        "description": summary_description(record),
    }
    if name not in field_slugs:
        entry["template_field"] = True
        for key in ("description", "example", "format", "pattern", "allowed_values", "multi_fields", "ignore_above"):
            if key in record:
                entry[key] = record[key]
    for key in ("required", "original_fieldset", "normalize", "beta", "alpha"):
        if key in record:
            entry[key] = record[key]
    return {key: value for key, value in entry.items() if value not in (None, "", [])}


def build_fieldsets(
    nested: dict[str, dict[str, Any]],
    field_slugs: dict[str, str],
    source: SourceRef,
) -> tuple[dict[Path, str], list[dict[str, Any]]]:
    docs: dict[Path, str] = {}
    summaries: list[dict[str, Any]] = []
    for name in sorted(nested, key=str.casefold):
        fieldset = nested[name]
        fields = fieldset.get("fields") or {}
        fieldset_record: dict[str, Any] = {
            "fieldset": name,
            "version": source.version,
            **{key: value for key, value in fieldset.items() if key != "fields"},
            "fields": [
                summarize_fieldset_field(field_name, field_record, field_slugs)
                for field_name, field_record in sorted(fields.items(), key=lambda item: item[0].casefold())
            ],
        }
        docs[Path(fieldset_path(name))] = dump_yaml(normalize_generated_yaml_value(fieldset_record))
        summary: dict[str, Any] = {
            "name": name,
            "path": fieldset_path(name),
            "title": fieldset.get("title"),
            "type": fieldset.get("type"),
            "description": summary_description(fieldset),
        }
        for key in ("reusable", "reused_here", "nestings", "beta", "alpha"):
            if fieldset.get(key):
                summary[key] = normalize_summary_value(fieldset[key])
        summaries.append({key: value for key, value in summary.items() if value not in (None, "", [])})

    docs[Path("fieldsets.yaml")] = dump_yaml(
        {"fieldsets": summaries}
    )
    return docs, summaries


def build_categorization(flat: dict[str, dict[str, Any]], field_slugs: dict[str, str], source: SourceRef) -> dict[Path, str]:
    categorization_fields = ("event.kind", "event.category", "event.type", "event.outcome")
    fields: dict[str, dict[str, Any]] = {}
    expected_category_type_combinations: list[dict[str, Any]] = []
    for field_name in categorization_fields:
        record = flat.get(field_name)
        if not record:
            continue
        fields[field_name] = {
            "path": field_path(field_slugs[field_name]),
            "type": record.get("type"),
            "normalize": record.get("normalize", []),
            "description": record.get("description"),
            "allowed_values": record.get("allowed_values", []),
        }
        if field_name == "event.category":
            for value in record.get("allowed_values", []):
                expected_event_types = value.get("expected_event_types")
                if expected_event_types:
                    expected_category_type_combinations.append(
                        {
                            "category": value.get("name"),
                            "event_types": expected_event_types,
                        }
                    )
    return {
        Path("categorization.yaml"): dump_yaml(
            normalize_generated_yaml_value(
                {
                    "fields": fields,
                    "expected_category_type_combinations": expected_category_type_combinations,
                }
            )
        )
    }


def build_otel(flat: dict[str, dict[str, Any]], field_slugs: dict[str, str], source: SourceRef) -> dict[Path, str]:
    fields: list[dict[str, Any]] = []
    for field_name in sorted(flat, key=str.casefold):
        relations = flat[field_name].get("otel") or []
        if not relations:
            continue
        fields.append(
            {
                "field": field_name,
                "path": field_path(field_slugs[field_name]),
                "relations": relations,
            }
        )
    return {
        Path("otel.yaml"): dump_yaml(
            {"fields": fields}
        )
    }


def render_skill_markdown(source: SourceRef) -> str:
    return clean_markdown(
        "\n".join(
            [
                "---",
                "name: tenzir-ecs",
                "description: Answer questions about Elastic Common Schema (ECS), Elastic field names, fieldsets, field types, categorization fields such as event.kind/event.category/event.type/event.outcome, ECS mapping decisions, custom fields, field reuse, and ECS/OpenTelemetry relations. Use whenever the user maps logs, events, security telemetry, network data, IAM activity, threat indicators, cloud/service context, or observability data into ECS, even if they only mention Elastic fields or event categorization.",
                "---",
                "",
                "# Elastic Common Schema",
                "",
                "Elastic Common Schema (ECS) defines common fields for logs, metrics, security telemetry, and observability data so events from different sources can be queried and correlated consistently.",
                "",
                f"This skill is generated from the latest supported ECS release in this repository: `{source.tag}` / `{source.version}`.",
                "Use the YAML files as the authoritative reference for exact field names, fieldsets, types, levels, allowed values, normalization hints, reuse metadata, and OpenTelemetry relations.",
                "Use the Markdown docs only for conceptual guidance, mapping examples, and implementation conventions.",
                "If a field, fieldset, allowed value, or relation is not present in the YAML data, say that it is not documented here.",
                "",
                "## Data files",
                "",
                "- Use [fields.yaml](fields.yaml) to find a dotted ECS field and then load the referenced `fields/<field>.yaml` file.",
                "- Use [fieldsets.yaml](fieldsets.yaml) to choose a fieldset and then load the referenced `fieldsets/<fieldset>.yaml` file.",
                "- Use [categorization.yaml](categorization.yaml) for `event.kind`, `event.category`, `event.type`, `event.outcome`, allowed values, and expected category/type combinations.",
                "- Use [otel.yaml](otel.yaml) for ECS-to-OpenTelemetry relation records.",
                "- Use [source.md](source.md) for release provenance, source artifacts, copied docs, and counts.",
                "",
                "## Complementary docs",
                "",
                "- Start with [Implementation patterns](docs/implementation-patterns.md), [Design principles](docs/design-principles.md), and [Conventions](docs/conventions.md) for general modeling questions.",
                "- Use [Categorization fields](docs/categorization-fields.md) and [Using categorization fields](docs/categorization-usage.md) when assigning `event.*` categorization values.",
                "- Use [Mapping network events](docs/mapping-network-events.md) for `source`/`destination` versus `client`/`server` decisions.",
                "- Use [Custom fields](docs/custom-fields.md) when ECS has no suitable field.",
                "- Use [ECS and OpenTelemetry](docs/opentelemetry.md) together with [otel.yaml](otel.yaml) for OTel alignment questions.",
                "- Use focused usage docs for [cloud](docs/usage/cloud.md), [service](docs/usage/service.md), [threat](docs/usage/threat.md), and [user](docs/usage/user.md) mapping scenarios.",
                "",
                "## Mapping rules",
                "",
                "- Populate required fields first: `@timestamp` and `ecs.version`.",
                "- Prefer documented ECS fields over custom fields when the field semantics match.",
                "- Preserve source-specific detail in custom fields when ECS has no matching field; use `labels` for small keyword metadata when appropriate.",
                "- For categorization, use only allowed values from [categorization.yaml](categorization.yaml); leave categorization fields empty when no allowed value fits.",
                "- Treat `event.category` and `event.type` as arrays and use multiple values only when the event reasonably belongs to multiple categories or types.",
                "- Use fieldset reuse metadata in [fieldsets.yaml](fieldsets.yaml) to distinguish role-specific locations such as `user.target`, `process.parent`, `cloud.origin`, and `service.target`.",
                "- For network events, use `source`/`destination` for packet or flow direction and also populate `client`/`server` when the endpoint roles are known.",
                "- Copy pivot values into `related.*` when the docs or field semantics call for cross-field searching.",
                "",
                "## Question routing",
                "",
                "- **What does field X mean?** Start with [fields.yaml](fields.yaml), then load the selected field YAML.",
                "- **What fields exist under fieldset X?** Start with [fieldsets.yaml](fieldsets.yaml), then load the selected fieldset YAML.",
                "- **Which `event.category` or `event.type` should I use?** Start with [categorization.yaml](categorization.yaml), then read [Using categorization fields](docs/categorization-usage.md) for examples.",
                "- **How should I map a network event?** Read [Mapping network events](docs/mapping-network-events.md), then inspect the relevant fieldsets.",
                "- **How do I model users, cloud resources, services, or threat indicators?** Read the matching usage doc under `docs/usage/`, then inspect the relevant fieldset YAML.",
                "- **How does ECS relate to OpenTelemetry?** Use [otel.yaml](otel.yaml) for relation records and [ECS and OpenTelemetry](docs/opentelemetry.md) for conceptual guidance.",
                "- **What if ECS has no matching field?** Read [Custom fields](docs/custom-fields.md).",
                "- **What raw upstream source backs this skill?** Use [source.md](source.md).",
                "",
            ]
        )
    )


def render_source_page(
    source: SourceRef,
    *,
    field_count: int,
    fieldset_count: int,
    categorization_field_count: int,
    otel_field_count: int,
) -> str:
    lines = [
        "# Source",
        "",
        "This skill is generated from the official Elastic ECS GitHub release artifacts. The generated YAML files are the primary agent-facing reference; copied Markdown files provide mapping guidance and examples.",
        "",
        f"- **Release**: [{source.release_name}]({source.release_url})",
        f"- **Tag**: `{source.tag}`",
        f"- **Version**: `{source.version}`",
        f"- **Resolved commit**: `{source.sha}`",
    ]
    if source.published_at:
        lines.append(f"- **Published at**: `{source.published_at}`")
    lines.extend(
        [
            f"- **Generated ECS fields**: `{field_count}`",
            f"- **Generated fieldsets**: `{fieldset_count}`",
            f"- **Categorization fields**: `{categorization_field_count}`",
            f"- **Fields with OpenTelemetry relations**: `{otel_field_count}`",
            "",
            "## Source artifacts",
            "",
            f"- [`generated/ecs/ecs_flat.yml`]({blob_url(source, 'generated/ecs/ecs_flat.yml')}) -> [fields.yaml](fields.yaml), `fields/*.yaml`, [categorization.yaml](categorization.yaml), [otel.yaml](otel.yaml)",
            f"- [`generated/ecs/ecs_nested.yml`]({blob_url(source, 'generated/ecs/ecs_nested.yml')}) -> [fieldsets.yaml](fieldsets.yaml), `fieldsets/*.yaml`",
            f"- [`version`]({blob_url(source, 'version')})",
            "",
            "## Copied Markdown docs",
            "",
        ]
    )
    for doc in CURATED_DOCS:
        lines.append(f"- {doc.title}: [`{doc.source_path}`]({blob_url(source, doc.source_path)}) -> [{doc.output_path.as_posix()}]({doc.output_path.as_posix()})")
    return clean_markdown("\n".join(lines))


def build_docs(
    source: SourceRef,
    flat: dict[str, dict[str, Any]],
    nested: dict[str, dict[str, Any]],
    markdown_sources: dict[str, str],
) -> dict[Path, str]:
    used_slugs: set[str] = set()
    field_slugs = {name: unique_slug(name, used_slugs) for name in sorted(flat, key=str.casefold)}
    field_slugs_by_dashed_name = {
        record["dashed_name"]: field_slugs[name]
        for name, record in flat.items()
        if isinstance(record.get("dashed_name"), str)
    }
    docs_by_source = {doc.source_path: doc.output_path for doc in CURATED_DOCS}
    fieldset_names = set(nested)

    docs: dict[Path, str] = {
        Path("SKILL.md"): render_skill_markdown(source),
    }
    field_docs, _field_summaries = build_fields(flat, field_slugs, source)
    fieldset_docs, _fieldset_summaries = build_fieldsets(nested, field_slugs, source)
    docs.update(field_docs)
    docs.update(fieldset_docs)
    docs.update(build_categorization(flat, field_slugs, source))
    docs.update(build_otel(flat, field_slugs, source))

    for doc in CURATED_DOCS:
        text = strip_frontmatter(markdown_sources[doc.source_path])
        text = rewrite_markdown_links(
            text,
            source=source,
            source_path=doc.source_path,
            output_path=doc.output_path,
            docs_by_source=docs_by_source,
            field_slugs_by_dashed_name=field_slugs_by_dashed_name,
            fieldset_names=fieldset_names,
        )
        docs[doc.output_path] = clean_markdown(text)

    docs[Path("source.md")] = render_source_page(
        source,
        field_count=len(flat),
        fieldset_count=len(nested),
        categorization_field_count=sum(1 for name in ("event.kind", "event.category", "event.type", "event.outcome") if name in flat),
        otel_field_count=sum(1 for record in flat.values() if record.get("otel")),
    )
    return docs


def write_docs(output_dir: Path, docs: dict[Path, str]) -> None:
    shutil.rmtree(output_dir, ignore_errors=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    for relative_path, content in sorted(docs.items()):
        path = output_dir / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    with httpx.Client(headers=HTTP_HEADERS, follow_redirects=True, timeout=30.0) as client:
        source = resolve_source_ref(client, args.ref)
        version_text = fetch_text(client, source, "version").strip()
        if version_text != source.version:
            raise RuntimeError(f"ECS version file reports {version_text!r}, expected {source.version!r}")

        flat = fetch_yaml(client, source, "generated/ecs/ecs_flat.yml")
        nested = fetch_yaml(client, source, "generated/ecs/ecs_nested.yml")
        if not isinstance(flat, dict) or not isinstance(nested, dict):
            raise RuntimeError("ECS generated artifacts did not contain the expected YAML mappings")

        markdown_sources = {
            doc.source_path: fetch_text(client, source, doc.source_path)
            for doc in CURATED_DOCS
        }

    docs = build_docs(source, flat, nested, markdown_sources)
    write_docs(output_dir, docs)
    print(f"Generated Elastic ECS skill {source.tag} in {output_dir}")


if __name__ == "__main__":
    main()
