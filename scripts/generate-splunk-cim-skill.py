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
import csv
import html
import json
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urldefrag, urljoin, urlparse

import httpx
import yaml


BASE_FIELDS = ("_time", "host", "source", "sourcetype")
SPLUNKBASE_URL = "https://splunkbase.splunk.com/app/1621"
HTTP_HEADERS = {
    "User-Agent": "tenzir-cim-generator",
}
DOCS_VERSION_RE = re.compile(r"common-information-model/([0-9]+(?:\.[0-9]+)*)(?:/|$)")
IGNORED_DOC_TAGS = {"script", "style", "svg", "button", "details", "textarea"}
IGNORED_DOC_CLASSES = {"code-language-label"}
DOC_SECTION_ORDER = (
    "Start",
    "Introduction and setup",
    "Workflows",
    "Data model prose",
    "Field mapping examples",
    "Worked examples",
    "Additional normalizations",
    "Other pages",
)


@dataclass(frozen=True, slots=True)
class DocsPage:
    path: str
    url: str
    title: str
    version: str
    version_id: str
    last_modified: str
    markdown: str
    file: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app-dir", required=True, help="Path to an unpacked Splunk_SA_CIM app directory")
    parser.add_argument("--output-dir", required=True, help="Generated skill output directory")
    parser.add_argument(
        "--docs-url",
        required=True,
        help="Splunk CIM docs page to use as the 8.5 TOC/documentation root",
    )
    return parser.parse_args()


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def to_slug(value: str) -> str:
    value = value.replace("DLP", "Dlp").replace("JVM", "Jvm").replace("DNS", "Dns")
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    return value.strip("_").lower() or "index"


def to_field_slug(value: str) -> str:
    leading_underscores = re.match(r"_+", value)
    prefix = leading_underscores.group(0) if leading_underscores else ""
    return f"{prefix}{to_slug(value)}"


def stable_key(value: str) -> tuple[str, str]:
    return value.casefold(), value


def unique_sorted(values: list[str] | tuple[str, ...]) -> list[str]:
    return sorted({value for value in values if value}, key=stable_key)


def unique_ordered(values: list[str] | tuple[str, ...]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def clean_text(value: object) -> str:
    text = "" if value is None else str(value)
    text = html.unescape(text.replace("\xa0", " "))
    return re.sub(r"\s+", " ", text).strip()


def clean_markdown(text: str) -> str:
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def convert_conf_value(value: str) -> object:
    value = value.strip()
    if value.casefold() == "true":
        return True
    if value.casefold() == "false":
        return False
    if re.fullmatch(r"-?[0-9]+", value):
        return int(value)
    return value


def read_splunk_conf(path: Path) -> dict[str, dict[str, object]]:
    stanzas: dict[str, dict[str, object]] = {}
    current: str | None = None
    if not path.exists():
        return stanzas
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"\[([^\]]+)\]", line)
        if match:
            current = match.group(1).strip()
            stanzas.setdefault(current, {})
            continue
        if current is None or "=" not in line:
            continue
        key, value = line.split("=", 1)
        stanzas[current][key.strip()] = convert_conf_value(value)
    return stanzas


def data_model_path(name: str) -> str:
    return f"data/models/{to_slug(name)}.yaml"


def data_field_path(name: str) -> str:
    return f"data/fields/{to_field_slug(name)}.yaml"


def data_lookup_path(name: str) -> str:
    return f"data/lookups/{to_slug(name)}.yaml"


def docs_page_path(path: str) -> str:
    rel = path.strip("/")
    rel = re.sub(r"^en/", "", rel)
    rel = re.sub(r"^data-management/common-information-model/[0-9.]+/?", "", rel)
    return f"docs/pages/{to_slug(rel or 'index')}.md"


def docs_relative_path(path: str) -> str:
    return re.sub(r"^docs/", "", path)


def docs_version_from_url(url: str) -> str:
    match = DOCS_VERSION_RE.search(urlparse(url).path)
    return match.group(1) if match else ""


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


def compact_mapping(items: list[tuple[str, Any]] | tuple[tuple[str, Any], ...]) -> dict[str, Any]:
    return {
        key: value
        for key, value in items
        if value not in (None, "", [], (), {})
    }


def markdown_link_text(value: str) -> str:
    return value.replace("[", "\\[").replace("]", "\\]")


def markdown_table_cell(value: str) -> str:
    return clean_text(value).replace("|", "\\|")


DOC_PAGE_SUMMARIES = {
    "index.md": (
        "Open this when an agent needs the root landing metadata for the bundled "
        "CIM docs version. It only provides version and URL context, not "
        "substantive CIM guidance."
    ),
    "introduction_overview_of_the_splunk_common_information_model.md": (
        "Open this for high-level questions about what Splunk CIM is, why it "
        "exists, and how the manual is organized. It gives conceptual context "
        "for search-time normalization, CIM tooling, and where reference "
        "material lives; use `../data/` for exact model, field, and tag facts."
    ),
    "introduction_install_the_splunk_common_information_model_add_on.md": (
        "Open this for installation-oriented tasks around the CIM add-on, "
        "especially where to install it and what index-related checks matter "
        "before setup. It provides deployment-scope guidance and points onward "
        "to setup and performance configuration."
    ),
    "introduction_release_notes_for_the_splunk_common_information_model_add_on.md": (
        "Open this when an agent needs release-specific context, compatibility "
        "notes, upgrade cautions, fixed issues, limitations, or deprecation "
        "history for the bundled CIM version. It is useful for explaining "
        "version behavior, not for deriving exact CIM model contents."
    ),
    "introduction_set_up_the_splunk_common_information_model_add_on.md": (
        "Open this for tasks about configuring CIM after installation: setup "
        "page access, index constraints, tag allowlists, data model acceleration, "
        "acceleration status, and field-filter impacts. It provides operational "
        "Splunk setup context and performance tradeoffs; use `../data/` for "
        "exact model, tag, and field reference facts."
    ),
    "introduction_support_and_resource_links_for_the_splunk_common_information_model_add_on.md": (
        "Open this when an agent needs support, download, Q&A, or broader "
        "Splunk documentation links for the CIM add-on. It is a resource-routing "
        "page rather than a technical normalization reference."
    ),
    "introduction_troubleshooting_adaptive_response_actions.md": (
        "Open this for troubleshooting adaptive response relay or action errors, "
        "especially Splunk Cloud Platform search head cluster deployments or "
        "environments without Splunk Enterprise Security. It provides "
        "cause-and-solution context for CAM/ARR setup and required related apps."
    ),
    "additional_normalizations_itsi_normalization.md": (
        "Open this when an agent needs ITSI Universal Alerting normalization "
        "context or wants to understand what kind of alert fields the "
        "ITSI-oriented normalization discusses. It contains a field-oriented "
        "table, but use `../data/` for exact structured facts when needed."
    ),
    "using_the_common_information_model_approaches_to_using_the_cim.md": (
        "Open this when an agent needs to choose the right CIM workflow for a "
        "broad task like normalization, validation, reporting, or custom alert "
        "actions. It provides routing context rather than implementation detail."
    ),
    "using_the_common_information_model_accelerate_cim_data_models.md": (
        "Open this when the task is about enabling, disabling, tuning, or "
        "auditing CIM data model acceleration. It gives operational workflow "
        "context for CIM Setup, summary ranges, acceleration enforcement, and "
        "the Data Model Audit dashboard."
    ),
    "using_the_common_information_model_match_ta_event_types_with_cim_data_models_to_accelerate_searches.md": (
        "Open this when explaining how Technology Add-ons, event types, tags, "
        "data models, and accelerated searches fit together in Splunk Enterprise "
        "Security. It provides conceptual workflow context; use `../data/` for "
        "exact CIM model, tag, field, or dataset facts."
    ),
    "using_the_common_information_model_use_the_cim_filters_to_exclude_data.md": (
        "Open this when the task is to reduce CIM-backed search noise or false "
        "positives by excluding known categories of data. It explains the CIM "
        "filter macro workflow and where those macros fit into searches, "
        "especially with Enterprise Security asset and identity categories."
    ),
    "using_the_common_information_model_use_the_cim_to_create_reports_and_dashboards.md": (
        "Open this when a user wants to build reports, dashboard panels, or "
        "Pivot visualizations from data already normalized to CIM. It provides "
        "reporting workflow context, including Pivot/Datasets entry points and "
        "the relationship between normalized data, dashboards, and acceleration "
        "monitoring."
    ),
    "using_the_common_information_model_use_the_cim_to_normalize_data_at_search_time.md": (
        "Open this when the task is to normalize a new Splunk data source to CIM "
        "at search time. It provides the end-to-end workflow for choosing "
        "relevant models, tagging events, mapping fields, validating output, "
        "optionally extending models, and packaging the result; use `../data/` "
        "for exact model, field, and tag facts."
    ),
    "using_the_common_information_model_use_the_cim_to_validate_your_data.md": (
        "Open this when checking whether indexed data is actually mapping to CIM "
        "as expected. It gives validation workflow context using `datamodelsimple`, "
        "Pivot, validation datasets, missing extraction checks, and untagged "
        "event checks; use `../data/` for exact CIM structures."
    ),
    "using_the_common_information_model_use_the_common_action_model_to_build_custom_alert_actions.md": (
        "Open this when building or refactoring Splunk custom alert actions or "
        "adaptive response actions to follow the common action model. It "
        "provides developer workflow context for the helper library, alert "
        "action metadata spec, and introspection data emitted by compliant "
        "actions."
    ),
    "data_models_how_to_use_the_cim_data_model_reference_tables.md": (
        "Open this when an agent needs to understand how Splunk's CIM reference "
        "prose should be interpreted, especially tags as constraints, inherited "
        "fields, expected values, and the limits of rendered tables. Use it for "
        "narrative guidance on reading the docs; defer exact field, tag, "
        "hierarchy, and constraint facts to `../data/models/*.yaml` or "
        "`../data/fields.yaml`."
    ),
    "data_models_alerts.md": (
        "Open this when deciding whether an event belongs in the Alerts model, "
        "especially for vendor-agnostic security alerts produced by alerting "
        "systems rather than Splunk alerts, notable events, raw packet counts, "
        "or non-security IT alerts. It provides scope boundaries and examples "
        "of what should not be modeled as Alerts; use `../data/` for exact "
        "schema facts."
    ),
    "data_models_application_state_deprecated.md": (
        "Open this for legacy references to Application State or when migrating "
        "older process, service, or listening-port inventory mappings. The "
        "narrative context is mainly historical: this model is deprecated and "
        "replaced by Endpoint, so current work should prefer the Endpoint model."
    ),
    "data_models_authentication.md": (
        "Open this for questions about modeling login activity from any source, "
        "including authentication outcomes, involved applications, source and "
        "destination systems, and privilege-escalation context. It explains the "
        "semantic roles of users and systems in authentication events; defer "
        "exact fields, prescribed values, and dataset constraints to `../data/`."
    ),
    "data_models_certificates.md": (
        "Open this for key and certificate management events from secure servers "
        "or IAM systems, especially SSL/TLS certificate observations. It "
        "provides narrative context for issuer/subject identity, validity "
        "timing, and a worked certificate-event example; exact field "
        "requirements and dataset facts belong in `../data/`."
    ),
    "data_models_change_analysis_deprecated.md": (
        "Open this only when handling old Change Analysis references or "
        "migration from pre-4.12 CIM content. It frames the deprecated "
        "CRUD-change model and its historical scope; use the current Change "
        "page for active guidance and YAML files for exact facts."
    ),
    "data_models_change.md": (
        "Open this for administrative or policy changes to infrastructure "
        "devices, servers, cloud environments, accounts, network controls, or "
        "EDR systems. Its most useful prose explains the boundary between "
        "Change and Endpoint, especially administrative changes versus "
        "endpoint-client activity; exact facts should come from `../data/`."
    ),
    "data_models_cim_fields_per_associated_data_model.md": (
        "Open this when an agent needs a prose index for field overlap across "
        "CIM models or wants context for joining or searching across datasets "
        "that share field names. Treat it as a cross-reference aid, not the "
        "source of truth; use `../data/fields.yaml` and model YAML files for "
        "exact associations."
    ),
    "data_models_data_access.md": (
        "Open this for user-driven access to shared, collaborative data such as "
        "documents, repositories, comments, tasks, invites, and similar "
        "user-managed objects. The key narrative value is boundary guidance "
        "against Change and Web: regular-user content collaboration maps here, "
        "while admin configuration and web-server client delivery generally do "
        "not."
    ),
    "data_models_data_loss_prevention.md": (
        "Open this for events generated by DLP tools that identify, monitor, or "
        "protect sensitive data. It frames DLP as incident-oriented tool output "
        "involving affected objects, users, sources, destinations, and severity "
        "context; defer exact field and tag requirements to `../data/`."
    ),
    "data_models_databases.md": (
        "Open this for events about structured or semi-structured data storage "
        "systems, including database activity, health, sessions, locks, queries, "
        "capacity, and performance context. The page provides narrative scope "
        "for database observability; use YAML sources for exact dataset and "
        "field details."
    ),
    "data_models_email.md": (
        "Open this for email traffic normalization, whether server-to-server or "
        "client-to-server. It gives narrative context for message delivery, "
        "content, filtering, senders, recipients, attachments, and mail "
        "infrastructure roles; exact protocol values, fields, and dataset facts "
        "belong in `../data/`."
    ),
    "data_models_endpoint.md": (
        "Open this for endpoint-client monitoring such as process launches, "
        "service launches, listening ports, filesystem activity, and registry "
        "activity on user machines, laptops, virtual desktops, or BYOD "
        "endpoints. Its key narrative guidance is the distinction from Change: "
        "endpoint activity belongs here, while administrative or policy changes "
        "belong under Change."
    ),
    "data_models_event_signatures.md": (
        "Open this when a task asks where Windows Event IDs and their "
        "human-readable descriptions belong in CIM. It explains that this model "
        "is specifically for Microsoft Windows event signature context, not a "
        "general event taxonomy."
    ),
    "data_models_interprocess_messaging.md": (
        "Open this for questions about modeling RPC, WMI, REST/SOAP calls, "
        "queues, or message-oriented middleware transactions. It gives narrative "
        "scope for request/response messaging, timing, payloads, and endpoints; "
        "use YAML for exact field requirements."
    ),
    "data_models_intrusion_detection.md": (
        "Open this when deciding how to model IDS/IPS attack detections or "
        "signature-based traffic blocks. It explains the boundary between "
        "simple network allow/deny traffic and intrusion detection based on "
        "deeper traffic patterns or signatures."
    ),
    "data_models_inventory.md": (
        "Open this for asset inventory, compute inventory, infrastructure "
        "topology, OS, local accounts, virtual systems, snapshots, and "
        "hardware/resource descriptions. It provides the model's broad "
        "inventory intent and notes the legacy Compute Inventory naming context."
    ),
    "data_models_java_virtual_machines_jvm.md": (
        "Open this for JVM monitoring questions covering Java runtime, "
        "threading, class loading, compilation, OS, and memory observations. It "
        "frames the model as generic Java server platform telemetry; exact "
        "metric names belong in YAML."
    ),
    "data_models_malware.md": (
        "Open this for antivirus, anti-malware, endpoint protection, infection "
        "detections, and malware product operations. It explains the distinction "
        "between malware attack alerting and operational health/status "
        "monitoring for protection systems."
    ),
    "data_models_network_resolution_dns.md": (
        "Open this for DNS resolution telemetry, including client/server and "
        "server/server DNS activity. It provides the narrative scope for DNS "
        "queries, responses, timing, and resolution outcomes; defer exact "
        "record and response details to YAML."
    ),
    "data_models_network_sessions.md": (
        "Open this for DHCP and VPN session modeling, especially lease "
        "starts/ends, VPN start/teardown attempts, and session user/client "
        "context. It explains that the model is about network session lifecycle "
        "rather than raw packet or flow traffic."
    ),
    "data_models_network_traffic.md": (
        "Open this for firewall, flow, proxy-adjacent, NAT, packet/byte, port, "
        "transport, and connection allow/deny modeling. It provides the key "
        "distinction from Intrusion Detection: rule-based connection handling "
        "versus signature/pattern-based attack detection."
    ),
    "data_models_performance.md": (
        "Open this for performance telemetry across systems, facilities, CPU, "
        "memory, storage, network throughput, uptime, and time synchronization. "
        "It gives scope for operational health and resource tracking; use YAML "
        "for exact metric fields."
    ),
    "data_models_splunk_audit_logs.md": (
        "Open this for Splunk-internal audit, search activity, scheduler "
        "activity, data model acceleration, view activity, web service errors, "
        "and modular alert actions. It provides narrative context for Splunk "
        "platform observability and custom alert action results."
    ),
    "data_models_ticket_management.md": (
        "Open this for service desk, ITIL-style requests, incidents, problems, "
        "changes, GRC tickets, or bug/ticket workflow normalization. It explains "
        "the lifecycle and ownership context for service requests without "
        "replacing exact model facts in YAML."
    ),
    "data_models_updates.md": (
        "Open this for patch management, update status, patch errors, and "
        "central or endpoint update tooling events. It frames update telemetry "
        "around affected systems, patch requirements, installation outcomes, "
        "and update product context."
    ),
    "data_models_vulnerabilities.md": (
        "Open this for vulnerability scanner findings, CVE-style references, "
        "severity, affected hosts, and scanner/reporting system context. It "
        "explains vulnerability detection scope and cross-reference intent; use "
        "YAML for exact identifiers and fields."
    ),
    "data_models_web.md": (
        "Open this for web server, proxy, HTTP request/response, URL, user "
        "agent, response code, and cloud storage access events in security or "
        "operational contexts. It provides the narrative boundary for web/proxy "
        "telemetry, while exact HTTP and storage fields belong in YAML."
    ),
    "field_mappings_authentication_field_mapping.md": (
        "Open this when the task involves reasoning about CIM-style "
        "normalization for cloud authentication events, especially login "
        "success, login failure, or privilege escalation. It compares GCP, "
        "Microsoft 365, AWS, and short-lived credential flows; use it for "
        "mapping intuition only and defer exact fields to `../data/`."
    ),
    "field_mappings_change_field_mapping.md": (
        "Open this when the task is about cloud administrative change events, "
        "such as user updates or compute reboot actions. It gives AWS and Azure "
        "examples and useful reasoning about identifying the changed object from "
        "provider payloads, while exact CIM field expectations should still come "
        "from `../data/`."
    ),
    "field_mappings_data_access_field_mapping.md": (
        "Open this when the task involves data-access normalization for file "
        "activity, especially upload events in SaaS storage logs. It compares "
        "Google Drive and Box examples to show how actor, object, owner, and "
        "source context can appear differently across providers."
    ),
    "field_mappings_network_traffic_field_mapping.md": (
        "Open this when the task involves cloud flow-log normalization or "
        "comparing network traffic records from different providers. It uses "
        "GCP and AWS source-flow examples to illustrate provider-specific "
        "context such as endpoints, direction/reporting perspective, counters, "
        "and timing without serving as the authoritative field source."
    ),
    "examples_use_the_cim_to_normalize_ossec_data.md": (
        "Open this when the task needs a full worked example of turning a "
        "proprietary IDS/syslog source into a Splunk add-on aligned with CIM "
        "expectations. It walks through sourcetyping, tags, regex extractions, "
        "aliases, lookups, validation, and optional packaging for OSSEC data."
    ),
    "examples_use_the_cim_to_normalize_cpu_performance_metrics.md": (
        "Open this when the task is about a procedural CIM-normalization "
        "workflow for performance metrics, especially CPU metrics for ITSI-style "
        "use cases. It provides both Splunk Web and config-file approaches for "
        "tags, event types, field aliases, extraction, and validation."
    ),
}


def app_version(app_conf: dict[str, dict[str, object]], manifest: dict[str, Any]) -> str:
    launcher = app_conf.get("launcher", {})
    version = launcher.get("version")
    if version:
        return str(version)
    return str(manifest.get("info", {}).get("id", {}).get("version", ""))


def lookup_value(value: object) -> object:
    if value is None:
        return ""
    value = str(value).strip()
    if value.casefold() == "true":
        return True
    if value.casefold() == "false":
        return False
    if value.startswith(("[", "{")):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    return value


def lookup_row(row: dict[str, str]) -> dict[str, object]:
    return {key: lookup_value(value) for key, value in row.items()}


def lookup_values(rows: list[dict[str, str]], field: str) -> list[object]:
    values: list[object] = []
    seen: set[tuple[str, str]] = set()
    for row in rows:
        normalized = lookup_value(row.get(field, ""))
        if normalized == "":
            continue
        key = (type(normalized).__name__, json.dumps(normalized, sort_keys=True))
        if key in seen:
            continue
        seen.add(key)
        values.append(normalized)
    return values


def lookup_data(record: dict[str, Any]) -> dict[str, Any]:
    columns = record["columns"]
    rows = record["rows"]
    if not columns:
        return {
            "name": record["name"],
        }

    if len(columns) == 1 or (len(columns) == 2 and columns[1] == "is_visible"):
        field = columns[0]
        return compact_mapping(
            (
                ("name", record["name"]),
                ("field", field),
                ("values", lookup_values(rows, field)),
            )
        )

    key = columns[0]
    if len(columns) == 2:
        target = columns[1]
        mappings = []
        for row in rows:
            source_value = lookup_value(row.get(key, ""))
            if source_value == "":
                continue
            mappings.append(
                {
                    "from": source_value,
                    "to": lookup_value(row.get(target, "")),
                }
            )
        return compact_mapping(
            (
                ("name", record["name"]),
                ("key", key),
                ("maps_to", target),
                ("mappings", mappings),
            )
        )

    return compact_mapping(
        (
            ("name", record["name"]),
            ("key", key),
            ("fields", columns if not rows else []),
            ("entries", [lookup_row(row) for row in rows if lookup_value(row.get(key, "")) != ""]),
        )
    )


def parse_lookup_files(app_dir: Path) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, str]]]]:
    lookup_records: list[dict[str, Any]] = []
    field_to_lookups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for path in sorted((app_dir / "lookups").glob("*"), key=lambda item: item.name.casefold()):
        if not path.is_file():
            continue
        if not (path.name.endswith(".csv") or path.name.endswith(".csv.default")):
            continue
        lookup_name = path.name
        if lookup_name.endswith(".csv.default"):
            lookup_name = lookup_name[: -len(".csv.default")]
        elif lookup_name.endswith(".csv"):
            lookup_name = lookup_name[: -len(".csv")]
        text = path.read_text(encoding="utf-8")
        rows = list(csv.DictReader(text.splitlines())) if text.strip() else []
        columns = list(rows[0].keys()) if rows else []
        if not columns and text.strip():
            reader = csv.reader(text.splitlines())
            columns = next(reader, [])
        record = {
            "name": lookup_name,
            "file": data_lookup_path(lookup_name),
            "columns": columns,
            "rows": rows,
        }
        lookup_records.append(record)
        for column in columns:
            field_to_lookups[column].append(
                {
                    "name": lookup_name,
                    "file": data_lookup_path(lookup_name),
                }
            )
    return lookup_records, dict(field_to_lookups)


def field_from_json(
    field: dict[str, Any],
    *,
    source: str | None = None,
    calculation: dict[str, Any] | None = None,
    include_name: bool = True,
) -> dict[str, Any]:
    comment = field.get("comment") if isinstance(field.get("comment"), dict) else {}
    name = str(field.get("fieldName") or "")
    display_name = field.get("displayName")
    record = compact_mapping(
        (
            ("name", name if include_name else ""),
            ("display_name", display_name if display_name and display_name != name else ""),
            ("source", source),
            ("type", field.get("type")),
            ("description", clean_text(comment.get("description"))),
            ("expected_values", comment.get("expected_values")),
            ("field_search", field.get("fieldSearch")),
        )
    )
    for key, value in (
        ("required", field.get("required")),
        ("recommended", comment.get("recommended")),
        ("ta_relevant", comment.get("ta_relevant")),
        ("multivalue", field.get("multivalue")),
        ("hidden", field.get("hidden")),
    ):
        if value:
            record[key] = value
    if calculation:
        record["calculation"] = compact_mapping(
            (
                ("id", calculation.get("calculationID")),
                ("type", calculation.get("calculationType")),
                ("expression", calculation.get("expression")),
                ("input_field", calculation.get("inputField")),
            )
        )
    return record


def field_occurrence(
    field: dict[str, Any],
    *,
    model: str,
    dataset: str,
    source: str,
    calculation: dict[str, Any] | None = None,
) -> dict[str, Any]:
    details = field_from_json(field, calculation=calculation)
    name = details.pop("name", "")
    return compact_mapping(
        (
            ("name", name),
            ("model", model),
            ("dataset", dataset),
            ("source", source),
            *details.items(),
        )
    )


def dataset_tags(obj: dict[str, Any]) -> list[str]:
    comment = obj.get("comment") if isinstance(obj.get("comment"), dict) else {}
    tags = comment.get("tags") if isinstance(comment, dict) else None
    return list(tags) if isinstance(tags, list) else []


def dataset_description(obj: dict[str, Any]) -> str:
    comment = obj.get("comment") if isinstance(obj.get("comment"), dict) else {}
    return clean_text(comment.get("description"))


def dataset_kind(name: str, object_by_name: dict[str, dict[str, Any]]) -> str:
    current = object_by_name.get(name)
    seen: set[str] = set()
    while current:
        parent = str(current.get("parentName") or "")
        if parent == "BaseSearch":
            return "search"
        if parent == "BaseEvent":
            return "event"
        if parent in seen:
            break
        seen.add(parent)
        current = object_by_name.get(parent)
    return "dataset"


def parent_chain(name: str, object_by_name: dict[str, dict[str, Any]]) -> list[str]:
    chain: list[str] = []
    current = object_by_name.get(name)
    seen: set[str] = set()
    while current:
        parent = str(current.get("parentName") or "")
        if not parent:
            break
        chain.append(parent)
        if parent in {"BaseEvent", "BaseSearch"}:
            break
        if parent in seen:
            break
        seen.add(parent)
        current = object_by_name.get(parent)
    return list(reversed(chain))


def infer_deprecated(model_name: str, model: dict[str, Any]) -> bool:
    text = " ".join(
        clean_text(value)
        for value in (
            model_name,
            model.get("displayName"),
            model.get("description"),
        )
    )
    return "deprecated" in text.casefold()


def model_data(
    model: dict[str, Any],
    fallback_name: str,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    model_name = str(model.get("modelName") or fallback_name)
    objects = model.get("objects") or []
    object_by_name = {str(obj.get("objectName")): obj for obj in objects}
    children_by_parent: dict[str, list[str]] = defaultdict(list)
    for obj in objects:
        parent = str(obj.get("parentName") or "")
        if parent:
            children_by_parent[parent].append(str(obj.get("objectName")))

    effective_cache: dict[str, dict[str, dict[str, Any]]] = {}
    constraints_cache: dict[str, list[str]] = {}

    def field_record(
        field: dict[str, Any],
        *,
        source: str,
        calculation: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        details = field_from_json(field, calculation=calculation, include_name=False)
        return compact_mapping(
            (
                ("source", source),
                *details.items(),
            )
        )

    def base_fields() -> dict[str, dict[str, Any]]:
        return {
            field_name: {
                "source": "base",
            }
            for field_name in BASE_FIELDS
        }

    def inherited_field(record: dict[str, Any], *, inherited_from: str) -> dict[str, Any]:
        return compact_mapping(
            (
                ("source", "inherited"),
                ("inherited_from", inherited_from),
                *(
                    (key, value)
                    for key, value in record.items()
                    if key not in {"source", "inherited_from"}
                ),
            )
        )

    def effective_fields(object_name: str) -> dict[str, dict[str, Any]]:
        if object_name in effective_cache:
            return effective_cache[object_name]
        obj = object_by_name[object_name]
        parent = str(obj.get("parentName") or "")
        fields: dict[str, dict[str, Any]] = {}
        if parent in object_by_name:
            fields.update(
                {
                    field_name: inherited_field(record, inherited_from=parent)
                    for field_name, record in effective_fields(parent).items()
                }
            )
        elif parent in {"BaseEvent", "BaseSearch"}:
            fields.update(base_fields())
        for field in obj.get("fields") or []:
            field_name = str(field.get("fieldName") or "")
            if not field_name:
                continue
            fields[field_name] = field_record(field, source="declared")
        for calculation in obj.get("calculations") or []:
            for field in calculation.get("outputFields") or []:
                field_name = str(field.get("fieldName") or "")
                if not field_name:
                    continue
                fields[field_name] = field_record(
                    field,
                    source="calculated",
                    calculation=calculation,
                )
        effective_cache[object_name] = {
            field_name: fields[field_name]
            for field_name in sorted(fields, key=stable_key)
        }
        return effective_cache[object_name]

    def local_constraints(object_name: str) -> list[str]:
        obj = object_by_name[object_name]
        return [
            str(item.get("search"))
            for item in obj.get("constraints") or []
            if item.get("search")
        ]

    def effective_constraints(object_name: str) -> list[str]:
        if object_name in constraints_cache:
            return constraints_cache[object_name]
        obj = object_by_name[object_name]
        parent = str(obj.get("parentName") or "")
        constraints: list[str] = []
        if parent in object_by_name:
            constraints.extend(effective_constraints(parent))
        constraints.extend(local_constraints(object_name))
        constraints_cache[object_name] = unique_ordered(constraints)
        return constraints_cache[object_name]

    datasets: dict[str, dict[str, Any]] = {}
    field_occurrences: list[dict[str, Any]] = []
    for obj in objects:
        name = str(obj.get("objectName"))
        kind = dataset_kind(name, object_by_name)
        for field in obj.get("fields") or []:
            field_name = str(field.get("fieldName") or "")
            if not field_name:
                continue
            field_occurrences.append(
                field_occurrence(
                    field,
                    model=model_name,
                    dataset=name,
                    source="declared",
                )
            )

        for calculation in obj.get("calculations") or []:
            for field in calculation.get("outputFields") or []:
                field_name = str(field.get("fieldName") or "")
                if not field_name:
                    continue
                field_occurrences.append(
                    field_occurrence(
                        field,
                        model=model_name,
                        dataset=name,
                        source="calculated",
                        calculation=calculation,
                    )
                )

        display_name = obj.get("displayName")
        datasets[name] = compact_mapping(
            (
                ("display_name", display_name if display_name and display_name != name else ""),
                ("kind", kind),
                ("description", dataset_description(obj)),
                ("tags", dataset_tags(obj)),
                ("constraints", effective_constraints(name)),
                ("fields", effective_fields(name)),
                ("inherits", parent_chain(name, object_by_name)),
                ("children", unique_sorted(children_by_parent.get(name, []))),
                ("search", obj.get("baseSearch")),
            )
        )

    data = compact_mapping(
        (
            ("name", model_name),
            (
                "display_name",
                model.get("displayName") if model.get("displayName") and model.get("displayName") != model_name else "",
            ),
            ("description", clean_text(model.get("description"))),
            ("deprecated", True if infer_deprecated(model_name, model) else None),
            ("root_datasets", [name for name, dataset in datasets.items() if dataset.get("inherits", [None])[-1] in {"BaseEvent", "BaseSearch"}]),
            ("datasets", datasets),
        )
    )
    return data, field_occurrences


class TocLinkParser(HTMLParser):
    def __init__(self, docs_version: str) -> None:
        super().__init__()
        self.docs_version = docs_version
        self.links: list[str] = []
        self.pdf_links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        for attr in ("href", "data-href", "data-nav-href"):
            href = attrs_dict.get(attr)
            if not href:
                continue
            if f"common-information-model/{self.docs_version}" not in href:
                continue
            if href.casefold().endswith(".pdf") or ".pdf?" in href.casefold():
                self.pdf_links.append(href)
            else:
                self.links.append(href)


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: dict[str, str] = {}
        self.in_title = False
        self.title_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "meta":
            name = attrs_dict.get("name") or attrs_dict.get("property")
            content = attrs_dict.get("content")
            if name and content:
                self.meta[name] = content
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self) -> str:
        title = clean_text(" ".join(self.title_parts))
        return title.split(" | ", 1)[0].strip()


class ArticleMarkdownParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.capture = False
        self.article_depth = 0
        self.parts: list[str] = []
        self.heading_level: int | None = None
        self.heading_parts: list[str] = []
        self.in_code = False
        self.in_pre = False
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.table_header_written = False
        self.ignored_depth = 0
        self.cell_parts: list[str] = []
        self.row: list[str] = []

    def append(self, value: str) -> None:
        if self.in_cell:
            self.cell_parts.append(value)
        elif self.heading_level is not None:
            self.heading_parts.append(value)
        else:
            self.parts.append(value)

    def should_ignore(self, tag: str, attrs: dict[str, str | None]) -> bool:
        classes = set((attrs.get("class") or "").split())
        return tag in IGNORED_DOC_TAGS or bool(classes & IGNORED_DOC_CLASSES)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "article" and attrs_dict.get("role") == "article" and not self.capture:
            self.capture = True
            self.article_depth = 1
            return
        if not self.capture:
            return
        if self.ignored_depth:
            self.ignored_depth += 1
            return
        if self.should_ignore(tag, attrs_dict):
            self.ignored_depth = 1
            return
        if tag == "article":
            self.article_depth += 1
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_level = int(tag[1])
            self.heading_parts = []
        elif tag in {"p", "section", "div"}:
            self.parts.append("\n\n")
        elif tag == "br":
            self.append("\n")
        elif tag in {"ul", "ol"}:
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "code":
            if self.in_pre:
                return
            self.in_code = True
            self.append("`")
        elif tag == "pre":
            self.in_pre = True
            self.parts.append("\n\n```text\n")
        elif tag == "table":
            self.in_table = True
            self.table_header_written = False
            self.parts.append("\n\n")
        elif tag == "tr" and self.in_table:
            self.in_row = True
            self.row = []
        elif tag in {"th", "td"} and self.in_table:
            self.in_cell = True
            self.cell_parts = []

    def handle_endtag(self, tag: str) -> None:
        if not self.capture:
            return
        if self.ignored_depth:
            self.ignored_depth -= 1
            return
        if tag == "article":
            self.article_depth -= 1
            if self.article_depth <= 0:
                self.capture = False
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"} and self.heading_level is not None:
            text = clean_text(" ".join(self.heading_parts))
            if text:
                self.parts.append(f"\n\n{'#' * self.heading_level} {text}\n\n")
            self.heading_level = None
            self.heading_parts = []
        elif tag == "code" and self.in_code:
            self.append("`")
            self.in_code = False
        elif tag == "pre" and self.in_pre:
            self.parts.append("\n```\n\n")
            self.in_pre = False
        elif tag in {"th", "td"} and self.in_table and self.in_cell:
            self.row.append(clean_text(" ".join(self.cell_parts)))
            self.cell_parts = []
            self.in_cell = False
        elif tag == "tr" and self.in_table and self.in_row:
            if self.row:
                escaped = [cell.replace("|", "\\|") for cell in self.row]
                self.parts.append("| " + " | ".join(escaped) + " |\n")
                if not self.table_header_written:
                    self.parts.append("| " + " | ".join("---" for _ in escaped) + " |\n")
                    self.table_header_written = True
            self.in_row = False
            self.row = []
        elif tag == "table" and self.in_table:
            self.in_table = False
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.capture or self.ignored_depth:
            return
        if self.in_pre:
            self.append(data)
            return
        text = clean_text(data)
        if not text:
            return
        self.append(text + " ")

    @property
    def markdown(self) -> str:
        return clean_markdown("".join(self.parts))


def normalize_doc_url(root_url: str, href: str) -> str:
    href, _ = urldefrag(href)
    if href.startswith("data-management/"):
        href = "/en/" + href
    return urljoin(root_url, href)


def is_core_cim_doc(url: str, docs_version: str) -> bool:
    parsed = urlparse(url)
    path = parsed.path
    if f"/common-information-model/{docs_version}/" not in path and not path.endswith(
        f"/common-information-model/{docs_version}"
    ):
        return False
    if "/overview-of-the-ocsf-cim-add-on" in path:
        return False
    if path.endswith(".pdf"):
        return False
    if not path.startswith("/en/"):
        return False
    return True


def fetch_docs(docs_url: str) -> tuple[list[DocsPage], str]:
    docs_version = docs_version_from_url(docs_url)
    with httpx.Client(headers=HTTP_HEADERS, follow_redirects=True, timeout=30.0) as client:
        response = client.get(docs_url)
        response.raise_for_status()
        docs_version = docs_version or docs_version_from_url(str(response.url))
        root_html = response.text
        toc = TocLinkParser(docs_version)
        toc.feed(root_html)
        urls = sorted(
            {
                normalize_doc_url(str(response.url), href)
                for href in toc.links
                if is_core_cim_doc(normalize_doc_url(str(response.url), href), docs_version)
            }
        )
        pdf_urls = sorted({normalize_doc_url(str(response.url), href) for href in toc.pdf_links})
        manual_pdf_url = pdf_urls[0] if pdf_urls else ""

        pages: list[DocsPage] = []
        seen_pages: set[str] = set()
        for url in urls:
            page_response = client.get(url)
            page_response.raise_for_status()
            page_html = page_response.text
            metadata = MetadataParser()
            metadata.feed(page_html)
            article = ArticleMarkdownParser()
            article.feed(page_html)
            title = metadata.title
            if not title:
                title_match = re.search(r"^#\s+(.+)$", article.markdown, flags=re.MULTILINE)
                title = title_match.group(1).strip() if title_match else url
            parsed = urlparse(str(page_response.url))
            path = parsed.path
            page_file = docs_page_path(path)
            if page_file in seen_pages:
                continue
            seen_pages.add(page_file)
            pages.append(
                DocsPage(
                    path=path,
                    url=str(page_response.url),
                    title=title,
                    version=metadata.meta.get("Version_Number", "") or docs_version,
                    version_id=metadata.meta.get("cisco_version_id", ""),
                    last_modified=metadata.meta.get("lastModifiedISO", ""),
                    markdown=article.markdown,
                    file=page_file,
                )
            )
    return pages, manual_pdf_url


def docs_section(page: DocsPage) -> str:
    name = Path(page.file).name
    if name == "index.md":
        return "Start"
    if name.startswith("introduction_"):
        return "Introduction and setup"
    if name.startswith("using_the_common_information_model_"):
        return "Workflows"
    if name.startswith("data_models_"):
        return "Data model prose"
    if name.startswith("field_mappings_"):
        return "Field mapping examples"
    if name.startswith("examples_"):
        return "Worked examples"
    if name.startswith("additional_normalizations_"):
        return "Additional normalizations"
    return "Other pages"


def docs_page_link(page: DocsPage) -> str:
    return f"[{markdown_link_text(page.title)}]({docs_relative_path(page.file)})"


def docs_page_link_by_file(pages_by_file: dict[str, DocsPage], file: str) -> str:
    page = pages_by_file.get(file)
    if not page:
        return "`not bundled`"
    return docs_page_link(page)


def docs_page_summary(page: DocsPage) -> str:
    return DOC_PAGE_SUMMARIES[Path(page.file).name]


def build_docs_index_markdown(
    *,
    docs_url: str,
    docs_version: str,
    manual_pdf_url: str,
    pages: list[DocsPage],
) -> str:
    pages_by_file = {page.file: page for page in pages}
    page_names = {Path(page.file).name for page in pages}
    missing_summaries = sorted(page_names - set(DOC_PAGE_SUMMARIES), key=stable_key)
    if missing_summaries:
        raise ValueError(f"Missing curated docs summaries for: {', '.join(missing_summaries)}")
    grouped_pages: dict[str, list[DocsPage]] = defaultdict(list)
    for page in pages:
        grouped_pages[docs_section(page)].append(page)

    task_rows = [
        (
            "Understand CIM at a high level",
            docs_page_link_by_file(
                pages_by_file,
                "docs/pages/introduction_overview_of_the_splunk_common_information_model.md",
            ),
            "Use docs for concepts and scope; use `../data/catalog.yaml` for the generated model inventory.",
        ),
        (
            "Normalize a new source",
            docs_page_link_by_file(
                pages_by_file,
                "docs/pages/using_the_common_information_model_use_the_cim_to_normalize_data_at_search_time.md",
            ),
            "Use docs for the workflow; use `../data/catalog.yaml` and `../data/models/*.yaml` for exact mapping facts.",
        ),
        (
            "Interpret reference tables",
            docs_page_link_by_file(
                pages_by_file,
                "docs/pages/data_models_how_to_use_the_cim_data_model_reference_tables.md",
            ),
            "Use docs for how to read Splunk prose tables; use `../data/` files for authoritative fields and constraints.",
        ),
        (
            "Validate CIM compliance",
            docs_page_link_by_file(
                pages_by_file,
                "docs/pages/using_the_common_information_model_use_the_cim_to_validate_your_data.md",
            ),
            "Use docs for the validation workflow; use `../data/models/splunk_cim_validation.yaml` for generated reference data.",
        ),
        (
            "Review provider field mapping examples",
            "[Field mapping examples](#field-mapping-examples)",
            "Use examples for reasoning patterns only; use `../data/fields.yaml` for exact CIM field usage.",
        ),
        (
            "Build reports, dashboards, or accelerated searches",
            "[Workflows](#workflows)",
            "Use docs for Splunk workflow guidance; use generated YAML for the model and dataset details.",
        ),
        (
            "Check release, setup, or support guidance",
            "[Introduction and setup](#introduction-and-setup)",
            "Use docs for Splunk operational guidance; use `../source.md` for generator provenance.",
        ),
    ]

    lines = [
        "# Splunk CIM Docs",
        "",
        "These Markdown files provide additional Splunk CIM prose context for workflows, examples, interpretation guidance, setup, and release notes.",
        "",
        "Use `../data/` as the authoritative reference for generated CIM facts: models, datasets, fields, tags, constraints, calculated fields, and lookups. Use this docs tree only to decide how to think about or apply those facts.",
        "",
        f"- **Docs root**: {docs_url}",
        f"- **Docs version**: `{docs_version or 'unknown'}`",
        f"- **Manual PDF**: {manual_pdf_url or 'not discovered'}",
        "",
        "## Start By Task",
        "",
        "| Task | Read first | Boundary |",
        "| --- | --- | --- |",
    ]
    for task, read_first, boundary in task_rows:
        lines.append(
            f"| {markdown_table_cell(task)} | {read_first} | {markdown_table_cell(boundary)} |"
        )

    lines.extend(
        [
            "",
            "## Imported Pages",
            "",
            "Each page entry has a curated trigger summary to help decide whether to open the linked article. These summaries are navigation context only and intentionally do not restate generated CIM data.",
            "",
        ]
    )

    for section in DOC_SECTION_ORDER:
        section_pages = grouped_pages.get(section, [])
        if not section_pages:
            continue
        lines.extend([f"### {section}", ""])
        for page in section_pages:
            lines.extend(
                [
                    f"#### {docs_page_link(page)}",
                    "",
                    docs_page_summary(page),
                    "",
                ]
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_skill_markdown(app_version_value: str, docs_version: str) -> str:
    return f"""---
name: tenzir-cim
description: >-
  Answer questions and produce mappings for the Splunk Common Information Model
  (CIM), including CIM Add-on aliases such as SA-CIM, CommonInformationModel,
  and SA-CommonInformationModel. Use when the user mentions CIM data
  models/datamodels/DMs, datasets/data model objects, fields, field aliases,
  calculated/eval fields, tags, constraints, lookups/lookup tables, macros,
  normalization, mapping logs or events to CIM, CIM compliance,
  pytest-splunk-addon, technical add-ons/TAs, Splunk Enterprise Security/ES,
  data model acceleration, pivots, tstats, or datamodel searches.
---

# Splunk Common Information Model

Version: {app_version_value}

CIM is organized around *data models*. Each data model contains *datasets*,
historically called data model objects. Datasets inherit fields and constraints
from parent datasets. Event datasets ultimately inherit from `BaseEvent`; search
datasets inherit from `BaseSearch`. All Splunk data model datasets can use the
base fields `_time`, `host`, `source`, and `sourcetype`.

- *Tags* and constraints decide which events belong in a dataset.
- *Fields* describe the effective normalized shape that searches, dashboards,
  pivots, and downstream apps expect. Each field entry states whether it is
  `base`, `declared`, `calculated`, or `inherited`.
- *Calculated field entries* include a `calculation` block because they create
  or normalize fields at search time.
- *Lookup files* document expected values, translations, and enrichments, such
  as actions, protocols, HTTP statuses, DNS reply codes, endpoint statuses, and
  severities.

## Data files

- Use [data/catalog.yaml](data/catalog.yaml) to choose a data model and find the generated files.
- Use `data/models/<model>.yaml` to inspect datasets, tags, constraints, and the effective `fields` map for one CIM data model.
- Use [data/fields.yaml](data/fields.yaml) to find field-specific files.
- Use `data/fields/<field>.yaml` to inspect lookup links and where a field is declared or calculated across models and datasets.
- Use [data/lookups.yaml](data/lookups.yaml) and `data/lookups/<lookup>.yaml` for lookup-backed values, translations, and enrichments.
- Use [docs/index.md](docs/index.md) and `docs/pages/*.md` for Splunk CIM {docs_version or "8.5"} workflow guidance, examples, and explanatory prose.
- Use [source.md](source.md) for provenance and generation counts.

Treat `docs/` as additional context only. Do not use docs pages as the
authority for fields, tags, constraints, datasets, or lookup values when a
generated `data/` file exists.

## Mapping rules

- Start from the event semantics, choose the closest CIM data model in
  [data/catalog.yaml](data/catalog.yaml), then choose the dataset whose tags and
  constraints match the event.
- Apply all required tags and parent dataset tags implied by the dataset parent chain.
- Populate useful app-documented fields first, especially fields marked
  `recommended` or `required`.
- Treat fields with `source: calculated` or a `calculation` block as
  app-provided normalizations; when mapping a source, still populate the
  underlying source fields needed by those calculations when possible.
- Prefer specific fields such as `src_ip`, `dest_ip`, `user`, `signature`, or
  `vendor_product` over broad fields when the data source provides them.
- Use lookup files to normalize, translate, or enrich values when a lookup
  documents semantics for a field.
- Preserve source-specific details outside CIM fields when the app-derived
  reference has no normalized CIM field.

## Question routing

- Which CIM model should this log map to? [data/catalog.yaml](data/catalog.yaml), then the closest model file.
- What tags or constraints identify a dataset? `data/models/<model>.yaml`.
- What fields does a dataset include? `fields` in `data/models/<model>.yaml`.
- What does field X mean? [data/fields.yaml](data/fields.yaml), then `data/fields/<field>.yaml`.
- What values are expected for a field? Field `expected_values`, then [data/lookups.yaml](data/lookups.yaml).
- What does Splunk say about CIM workflows? [docs/index.md](docs/index.md).
- What source produced this skill? [source.md](source.md).
"""


def build_source_markdown(
    *,
    manifest: dict[str, Any],
    app_version_value: str,
    docs_url: str,
    docs_version: str,
    manual_pdf_url: str,
    counts: dict[str, int],
) -> str:
    info = manifest.get("info", {})
    app_id = info.get("id", {})
    app_name = str(app_id.get("name", "") or "Splunk_SA_CIM")
    return f"""# Source

This skill is generated from the Splunk Common Information Model app and current Splunk CIM docs.
The generated YAML files are the primary agent-facing reference.
Bundled Markdown docs provide additional workflow and interpretation context and do not override app-derived YAML.

- **App source**: Splunkbase app `{app_name}`
- **App version**: `{app_version_value}`
- **App title**: `{info.get("title", "")}`
- **App author**: `{", ".join(author.get("name", "") for author in info.get("author", []) if isinstance(author, dict))}`
- **Splunkbase listing**: {SPLUNKBASE_URL}
- **Docs root**: {docs_url}
- **Docs version**: `{docs_version or "unknown"}`
- **Docs manual PDF**: {manual_pdf_url or "not discovered"}
- **Data precedence**: app-derived YAML is authoritative; docs are bundled as additional context for workflow guidance only.

## Generated counts

- **Data model files**: `{counts["models"]}`
- **Datasets**: `{counts["datasets"]}`
- **Root datasets**: `{counts["root_datasets"]}`
- **Distinct fields**: `{counts["distinct_fields"]}`
- **Dataset field entries**: `{counts["field_records"]}`
- **Declared field definitions**: `{counts["declared_field_records"]}`
- **Calculated field definitions**: `{counts["calculated_field_records"]}`
- **Constraints**: `{counts["constraints"]}`
- **Lookup files**: `{counts["lookups"]}`
- **Docs pages**: `{counts["docs_pages"]}`

Raw app source files are not copied wholesale. The generated files preserve the app's data model, lookup, and documentation-relevant metadata in agent-friendly YAML.
"""


def generate(app_dir: Path, output_dir: Path, docs_url: str) -> None:
    manifest = read_json(app_dir / "app.manifest")
    app_conf = read_splunk_conf(app_dir / "default" / "app.conf")
    app_version_value = app_version(app_conf, manifest)

    docs_pages, manual_pdf_url = fetch_docs(docs_url)
    docs_version = next((page.version for page in docs_pages if page.version), "")

    lookup_records, field_to_lookups = parse_lookup_files(app_dir)

    model_records: list[dict[str, Any]] = []
    field_occurrences_by_name: dict[str, list[dict[str, Any]]] = defaultdict(list)
    model_paths = sorted((app_dir / "default" / "data" / "models").glob("*.json"), key=lambda item: item.name.casefold())
    for model_path in model_paths:
        model = read_json(model_path)
        record, occurrences = model_data(model, model_path.stem)
        model_records.append(record)
        for occurrence in occurrences:
            name = occurrence.get("name")
            if name:
                field_occurrences_by_name[str(name)].append(occurrence)

    distinct_fields = sorted(field_occurrences_by_name, key=stable_key)
    field_index = {name: data_field_path(name) for name in distinct_fields}

    counts = {
        "models": len(model_records),
        "datasets": sum(len(model.get("datasets", {})) for model in model_records),
        "root_datasets": sum(len(model.get("root_datasets", [])) for model in model_records),
        "distinct_fields": len(distinct_fields),
        "field_records": sum(
            len(dataset.get("fields", {}))
            for model in model_records
            for dataset in model.get("datasets", {}).values()
        ),
        "declared_field_records": sum(
            1
            for occurrences in field_occurrences_by_name.values()
            for occurrence in occurrences
            if occurrence.get("source") == "declared"
        ),
        "calculated_field_records": sum(
            1
            for occurrences in field_occurrences_by_name.values()
            for occurrence in occurrences
            if occurrence.get("source") == "calculated"
        ),
        "constraints": sum(
            len(dataset.get("constraints", []))
            for model in model_records
            for dataset in model.get("datasets", {}).values()
        ),
        "lookups": len(lookup_records),
        "docs_pages": len(docs_pages),
    }

    staging_dir = output_dir.with_name(f".{output_dir.name}.tmp")
    if staging_dir.exists():
        shutil.rmtree(staging_dir)
    staging_dir.mkdir(parents=True)

    write_file(staging_dir / "SKILL.md", build_skill_markdown(app_version_value, docs_version))
    write_file(
        staging_dir / "source.md",
        build_source_markdown(
            manifest=manifest,
            app_version_value=app_version_value,
            docs_url=docs_url,
            docs_version=docs_version,
            manual_pdf_url=manual_pdf_url,
            counts=counts,
        ),
    )

    catalog = {
        "models": {
            model["name"]: compact_mapping(
                (
                    ("file", data_model_path(model["name"])),
                    ("display_name", model.get("display_name")),
                    ("description", model.get("description")),
                    ("deprecated", True if model.get("deprecated") else None),
                    ("datasets", len(model.get("datasets", {}))),
                    ("root_datasets", model.get("root_datasets")),
                )
            )
            for model in sorted(model_records, key=lambda item: stable_key(item["name"]))
        },
        "base_fields": list(BASE_FIELDS),
        "indexes": {
            "fields": "data/fields.yaml",
            "lookups": "data/lookups.yaml",
            "docs": "docs/index.md",
        },
        "source": compact_mapping(
            (
                ("app_name", manifest.get("info", {}).get("id", {}).get("name")),
                ("app_version", app_version_value),
                ("app_title", manifest.get("info", {}).get("title")),
                ("splunkbase_url", SPLUNKBASE_URL),
                ("docs_url", docs_url),
                ("docs_version", docs_version),
                ("manual_pdf_url", manual_pdf_url),
            )
        ),
    }
    write_file(staging_dir / "data" / "catalog.yaml", dump_yaml(catalog))

    for model in model_records:
        write_file(staging_dir / data_model_path(model["name"]), dump_yaml(model))

    write_file(staging_dir / "data" / "fields.yaml", dump_yaml(field_index))
    for field_name in distinct_fields:
        occurrences = field_occurrences_by_name[field_name]
        field_data = compact_mapping(
            (
                ("name", field_name),
                ("lookups", field_to_lookups.get(field_name, [])),
                (
                    "used_by",
                    sorted(
                        [
                            {key: value for key, value in occurrence.items() if key != "name"}
                            for occurrence in occurrences
                        ],
                        key=lambda item: (
                            str(item.get("model", "")).casefold(),
                            str(item.get("dataset", "")).casefold(),
                            str(item.get("source", "")).casefold(),
                        ),
                    ),
                ),
            )
        )
        write_file(staging_dir / data_field_path(field_name), dump_yaml(field_data))

    write_file(
        staging_dir / "data" / "lookups.yaml",
        dump_yaml({record["name"]: record["file"] for record in lookup_records}),
    )
    for record in lookup_records:
        write_file(staging_dir / record["file"], dump_yaml(lookup_data(record)))

    write_file(
        staging_dir / "docs" / "index.md",
        build_docs_index_markdown(
            docs_url=docs_url,
            docs_version=docs_version,
            manual_pdf_url=manual_pdf_url,
            pages=docs_pages,
        ),
    )
    for page in docs_pages:
        header = f"""---
title: {page.title}
url: {page.url}
last_modified: {page.last_modified}
version: {page.version}
---

"""
        write_file(staging_dir / page.file, header + page.markdown)

    if output_dir.exists():
        shutil.rmtree(output_dir)
    staging_dir.rename(output_dir)


def main() -> None:
    args = parse_args()
    generate(Path(args.app_dir).resolve(), Path(args.output_dir), args.docs_url)


if __name__ == "__main__":
    main()
