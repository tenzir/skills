from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
import warnings
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "generate-google-udm-skill.py"
)
SPEC = importlib.util.spec_from_file_location("generate_google_udm_skill", SCRIPT_PATH)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GenerateGoogleUdmSkillTest(unittest.TestCase):
    def test_descriptor_rendering_preserves_proto_semantics(self) -> None:
        context = self._build_fixture_context()
        source = MODULE.SourceRef(ref="fixture", sha="abc123")
        docs = MODULE.build_docs(
            context,
            source,
            {
                "backstory/udm.proto",
                "backstory/entity.proto",
                "backstory/id.proto",
            },
        )

        skill_markdown = docs[Path("SKILL.md")]
        schema_markdown = docs[Path("schema.md")]
        udm_page = docs[Path("messages/udm.md")]
        metadata_page = docs[Path("messages/metadata.md")]
        variable_page = docs[Path("messages/finding_variable.md")]
        id_page = docs[Path("messages/id.md")]
        namespace_page = docs[Path("enums/id_namespace.md")]
        event_type_page = docs[Path("enums/metadata_event_type.md")]
        dedicated_event_types = docs[Path("event-types.md")]
        entity_page = docs[Path("messages/entity.md")]
        entity_metadata_page = docs[Path("messages/entity_metadata.md")]
        relation_page = docs[Path("messages/relation.md")]
        metric_page = docs[Path("messages/metric.md")]
        entity_type_page = docs[Path("enums/entity_metadata_entity_type.md")]
        relation_page_enum = docs[Path("enums/relation_relationship.md")]
        metric_page_enum = docs[Path("enums/metric_metric_name.md")]

        self.assertIn("name: tenzir-google-udm", skill_markdown)
        self.assertIn("`abc123`", schema_markdown)
        self.assertIn("backstory/entity.proto", schema_markdown)
        self.assertIn("## Top-level UDM event fields", schema_markdown)
        self.assertIn("## Top-level Entity graph fields", schema_markdown)
        self.assertIn("[`Metadata`](metadata.md)", udm_page)
        self.assertIn("map<`string`, [`FindingVariable`](finding_variable.md)>", udm_page)
        self.assertIn("[`Id`](id.md)", udm_page)
        self.assertIn("- **Cardinality**: `optional`", udm_page)
        self.assertIn("`google.protobuf.Timestamp`", metadata_page)
        self.assertNotIn("(imported)", metadata_page)
        self.assertIn("- `typed_value`: `string_value`, `int64_value`", variable_page)
        self.assertIn("### `NORMALIZED_TELEMETRY`", namespace_page)
        self.assertIn("[`Id.Namespace`](../enums/id_namespace.md)", id_page)
        self.assertIn("### `OLD_TEST_EVENT`", event_type_page)
        self.assertIn("- **Deprecated**: `true`", event_type_page)
        self.assertIn("# Event Types", dedicated_event_types)
        self.assertIn("Test event.", dedicated_event_types)
        self.assertIn("[`EntityMetadata`](entity_metadata.md)", entity_page)
        self.assertIn("[`Noun`](noun.md)", entity_page)
        self.assertIn("[`Relation`](relation.md)", entity_page)
        self.assertIn("[`Metric`](metric.md)", entity_page)
        self.assertIn("### `entity_type`", entity_metadata_page)
        self.assertIn("### `relations`", entity_page)
        self.assertIn("### `relationship`", relation_page)
        self.assertIn("### `metric_name`", metric_page)
        self.assertIn("### `IP_ADDRESS`", entity_type_page)
        self.assertIn("### `OWNS`", relation_page_enum)
        self.assertIn("### `NETWORK_BYTES_TOTAL`", metric_page_enum)

    def test_usage_and_field_list_guidance_render_deterministically(self) -> None:
        context = self._build_fixture_context()
        guidance = self._build_fixture_guidance()
        source = MODULE.SourceRef(ref="fixture", sha="abc123")

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            docs = MODULE.build_docs(
                context,
                source,
                {
                    "backstory/udm.proto",
                    "backstory/entity.proto",
                    "backstory/id.proto",
                },
                guidance,
            )

        warning_text = "\n".join(str(warning.message) for warning in caught)
        self.assertIn("idm.is_alert", warning_text)

        self.assertIn("Usage guide last updated", docs[Path("SKILL.md")])
        self.assertIn("schema and usage references", docs[Path("SKILL.md")])
        self.assertIn("Creative Commons Attribution 4.0", docs[Path("usage.md")])
        self.assertNotIn("Fetched:", docs[Path("usage.md")])
        self.assertIn("Google last updated: `2026-06-03 UTC`", docs[Path("usage.md")])

        field_paths = docs[Path("field-paths.md")]
        self.assertIn("For rules engine evaluation", field_paths)
        self.assertIn("`$event.metadata.event_type`", field_paths)
        self.assertIn("`event.idm.graph.entity.user.userid`", field_paths)
        self.assertIn("Field name values use lowercase", field_paths)

        datatypes = docs[Path("datatypes.md")]
        self.assertIn("`int32`", datatypes)
        self.assertIn("Uses variable-length encoding.", datatypes)
        self.assertIn("int32", datatypes)

        metadata_guidance = docs[Path("field-guidance/metadata.md")]
        self.assertIn("# Metadata Field Guidance", metadata_guidance)
        self.assertIn("`Metadata.event_type`", metadata_guidance)
        self.assertIn("- **Required**: Yes.", metadata_guidance)

        noun_guidance = docs[Path("field-guidance/noun.md")]
        self.assertIn("`Noun.ip`", noun_guidance)
        self.assertIn("192.0.2.1", noun_guidance)

        product_guidance = docs[Path("field-guidance/idm.md")]
        self.assertIn("`idm.is_alert`", product_guidance)
        self.assertIn("Identifies whether the event is an alert.", product_guidance)

        categories = docs[Path("event-type-categories.md")]
        self.assertIn("## Network telemetry events", categories)
        self.assertIn("[NETWORK_HTTP", categories)
        self.assertIn("TEST_EVENT", categories)

        event_index = docs[Path("event-guidance.md")]
        self.assertIn("[`NETWORK_HTTP`](event-guidance/network_http.md)", event_index)
        self.assertIn("[`TEST_EVENT`](event-guidance/test_event.md)", event_index)

        network_http = docs[Path("event-guidance/network_http.md")]
        self.assertIn("# NETWORK_HTTP Event Guidance", network_http)
        self.assertIn("- metadata: Include the required fields.", network_http)
        self.assertIn("metadata { event_type: NETWORK_HTTP }", network_http)

        test_event = docs[Path("event-guidance/test_event.md")]
        self.assertIn("- Usage-guide section: `NETWORK_HTTP, TEST_EVENT`", test_event)

        entity_guidance = docs[Path("entity-guidance/ip_address.md")]
        self.assertIn("# IP_ADDRESS Entity Guidance", entity_guidance)
        self.assertIn("entity.ip must contain at least one valid IP address.", entity_guidance)

    def test_event_and_entity_guidance_must_match_proto_enums(self) -> None:
        context = self._build_fixture_context()
        source = MODULE.DocSource(
            title="fixture",
            url="https://example.invalid",
            last_updated="2026-06-03 UTC",
        )
        bad_event_guidance = MODULE.DocsGuidance(
            usage_source=source,
            field_list_source=source,
            event_guidance=(
                MODULE.EventGuidance(
                    title="NOT_A_REAL_EVENT",
                    event_types=("NOT_A_REAL_EVENT",),
                    required=(),
                    optional=(),
                    notes=(),
                    examples=(),
                ),
            ),
        )
        with self.assertRaisesRegex(RuntimeError, "Metadata.EventType"):
            MODULE.render_guidance_docs(context, bad_event_guidance)

        bad_entity_guidance = MODULE.DocsGuidance(
            usage_source=source,
            field_list_source=source,
            entity_guidance=(
                MODULE.EntityGuidance(
                    entity_type="NOT_A_REAL_ENTITY",
                    requirements=("entity.foo must be present.",),
                ),
            ),
        )
        with self.assertRaisesRegex(RuntimeError, "EntityMetadata.EntityType"):
            MODULE.render_guidance_docs(context, bad_entity_guidance)

    def test_write_docs_replaces_output_tree(self) -> None:
        with tempfile.TemporaryDirectory() as output_dir_str:
            output_dir = Path(output_dir_str)
            self._write(output_dir / "stale.md", "stale\n")

            MODULE.write_docs(
                output_dir,
                {
                    Path("SKILL.md"): "---\nname: test\n---\n",
                    Path("messages/example.md"): "# Example\n",
                },
            )

            self.assertTrue((output_dir / "SKILL.md").exists())
            self.assertTrue((output_dir / "messages" / "example.md").exists())
            self.assertFalse((output_dir / "stale.md").exists())

    def _build_fixture_context(self):
        with tempfile.TemporaryDirectory() as proto_root_str:
            proto_root = Path(proto_root_str)
            self._write(
                proto_root / "backstory" / "udm.proto",
                "\n".join(
                    [
                        'syntax = "proto3";',
                        "",
                        "package google.backstory;",
                        "",
                        'import "google/protobuf/timestamp.proto";',
                        'import "backstory/id.proto";',
                        "",
                        "// A Unified Data Model event.",
                        "message UDM {",
                        "  // Event metadata.",
                        "  Metadata metadata = 1;",
                        "",
                        "  // Variables extracted from the event.",
                        "  map<string, FindingVariable> variables = 2;",
                        "",
                        "  // Related UDM fields that are grouped together.",
                        "  optional GroupedFields grouped = 3;",
                        "",
                        "  // Finding object reference.",
                        "  Id object_reference = 4;",
                        "",
                        "  // Principal entity.",
                        "  Noun principal = 5;",
                        "",
                        '  reserved "udm";',
                        "}",
                        "",
                        "// General information associated with a UDM event.",
                        "message Metadata {",
                        "  // An event type.",
                        "  enum EventType {",
                        "    // Default event type.",
                        "    EVENTTYPE_UNSPECIFIED = 0;",
                        "",
                        "    // Test event.",
                        "    TEST_EVENT = 1;",
                        "",
                        "    // Deprecated test event.",
                        "    OLD_TEST_EVENT = 2 [deprecated = true];",
                        "",
                        "    // HTTP network event.",
                        "    NETWORK_HTTP = 3;",
                        "",
                        "    // Mutex creation event.",
                        "    MUTEX_CREATION = 4;",
                        "  }",
                        "",
                        "  // The event type.",
                        "  EventType event_type = 1;",
                        "",
                        "  // Time when the event occurred.",
                        "  google.protobuf.Timestamp event_timestamp = 2;",
                        "}",
                        "",
                        "// Variable data.",
                        "message FindingVariable {",
                        "  oneof typed_value {",
                        "    // String value.",
                        "    string string_value = 1;",
                        "",
                        "    // Integer value.",
                        "    int64 int64_value = 2;",
                        "  }",
                        "}",
                        "",
                        "// Flattened grouped fields.",
                        "message GroupedFields {",
                        "  // Hostnames.",
                        "  repeated string hostname = 1;",
                        "}",
                        "",
                        "// A UDM noun.",
                        "message Noun {",
                        "  // IP addresses.",
                        "  repeated string ip = 1;",
                        "",
                        "  // Hostname.",
                        "  string hostname = 2;",
                        "",
                        "  // File details.",
                        "  File file = 3;",
                        "",
                        "  // User details.",
                        "  User user = 4;",
                        "",
                        "  // Resource details.",
                        "  Resource resource = 5;",
                        "}",
                        "",
                        "// File details.",
                        "message File {",
                        "  string full_path = 1;",
                        "}",
                        "",
                        "// User details.",
                        "message User {",
                        "  repeated string email_addresses = 1;",
                        "  string userid = 2;",
                        "}",
                        "",
                        "// Resource details.",
                        "message Resource {",
                        "  enum ResourceType {",
                        "    RESOURCE_TYPE_UNSPECIFIED = 0;",
                        "    MUTEX = 1;",
                        "  }",
                        "  ResourceType resource_type = 1;",
                        "  string name = 2;",
                        "}",
                        "",
                    ]
                ),
            )

            self._write(
                proto_root / "backstory" / "entity.proto",
                "\n".join(
                    [
                        'syntax = "proto3";',
                        "",
                        "package google.backstory;",
                        "",
                        'import "backstory/udm.proto";',
                        "",
                        "// Information about the Entity.",
                        "message EntityMetadata {",
                        "  // Describes the type of entity.",
                        "  enum EntityType {",
                        "    UNKNOWN_ENTITYTYPE = 0;",
                        "    ASSET = 1;",
                        "    RESOURCE = 2;",
                        "    IP_ADDRESS = 3;",
                        "    FILE = 4;",
                        "    DOMAIN_NAME = 5;",
                        "    URL = 6;",
                        "    MUTEX = 7;",
                        "    METRIC = 8;",
                        "    CIDR_BLOCK = 9;",
                        "    USER = 10000;",
                        "  }",
                        "",
                        "  // Entity type.",
                        "  EntityType entity_type = 1;",
                        "}",
                        "",
                        "// An Entity provides additional context.",
                        "message Entity {",
                        "  // Entity metadata.",
                        "  EntityMetadata metadata = 1;",
                        "",
                        "  // Noun represented by the entity.",
                        "  Noun entity = 2;",
                        "",
                        "  // Relationships.",
                        "  repeated Relation relations = 3;",
                        "",
                        "  // Metric payload.",
                        "  Metric metric = 4;",
                        "}",
                        "",
                        "// Defines a relationship.",
                        "message Relation {",
                        "  enum Relationship {",
                        "    RELATIONSHIP_UNSPECIFIED = 0;",
                        "    OWNS = 1;",
                        "  }",
                        "",
                        "  Noun entity = 1;",
                        "  EntityMetadata.EntityType entity_type = 2;",
                        "  Relationship relationship = 3;",
                        "}",
                        "",
                        "// Stores precomputed aggregated analytic data.",
                        "message Metric {",
                        "  enum MetricName {",
                        "    METRIC_NAME_UNSPECIFIED = 0;",
                        "    NETWORK_BYTES_TOTAL = 1;",
                        "  }",
                        "",
                        "  MetricName metric_name = 1;",
                        "}",
                        "",
                    ]
                ),
            )

            self._write(
                proto_root / "backstory" / "id.proto",
                "\n".join(
                    [
                        'syntax = "proto3";',
                        "",
                        "package google.backstory;",
                        "",
                        "// Identifier for a UDM object.",
                        "message Id {",
                        "  // Namespace component.",
                        "  enum Namespace {",
                        "    // Normalized telemetry.",
                        "    NORMALIZED_TELEMETRY = 0;",
                        "  }",
                        "",
                        "  // Namespace the id belongs to.",
                        "  Namespace namespace = 1;",
                        "",
                        "  // Full raw ID.",
                        "  bytes id = 2;",
                        "}",
                        "",
                    ]
                ),
            )

            descriptor_set = MODULE.compile_descriptor(proto_root)
            file_proto = next(
                proto for proto in descriptor_set.file if proto.name == "backstory/udm.proto"
            )
            extra_file_protos = [
                proto
                for proto in descriptor_set.file
                if proto.name in {
                    "backstory/entity.proto",
                    "backstory/id.proto",
                }
            ]
            return MODULE.collect_messages_and_enums(file_proto, extra_file_protos)

    def _build_fixture_guidance(self):
        usage_html = """
        <html><body>
        <article>
          <h1 data-text="UDM usage guide">UDM usage guide</h1>
          <p><strong>UDM field name formats</strong>:</p>
          <ul>
            <li>For rules engine evaluation, the prefix begins with <strong>udm</strong>.</li>
            <li>For configuration-based normalizer (CBN), the prefix begins with <strong>event.idm.read_only_udm</strong>.</li>
          </ul>
          <h2 id="event-metadata" data-text="Population of Event metadata">Population of Event metadata</h2>
          <h3 id="metadataevent_type" data-text="Metadata.event_type">Metadata.event_type</h3>
          <ul>
            <li><strong>Purpose</strong>: Specifies the type of the event.</li>
            <li><strong>Required</strong>: Yes.</li>
            <li><strong>Encoding</strong>: Must be one of the predefined event types.</li>
          </ul>
          <h4 data-text="Network telemetry events">Network telemetry events</h4>
          <p>Network telemetry events include protocol summaries.</p>
          <ul>
            <li>NETWORK_HTTP (for example, HTTP request details)</li>
            <li>TEST_EVENT</li>
          </ul>
          <h2 id="noun-metadata" data-text="Population of Noun metadata">Population of Noun metadata</h2>
          <h3 id="nounip" data-text="Noun.ip">Noun.ip</h3>
          <ul>
            <li><strong>Purpose</strong>: Stores IP addresses for the noun.</li>
            <li><strong>Examples</strong>:
              <ul><li>192.0.2.1</li></ul>
            </li>
          </ul>
          <h2 id="alert-metadata" data-text="Population of alert metadata">Population of alert metadata</h2>
          <h3 id="idmis_alert" data-text="idm.is_alert">idm.is_alert</h3>
          <ul>
            <li><strong>Purpose</strong>: Identifies whether the event is an alert.</li>
            <li><strong>Encoding</strong>: Boolean.</li>
          </ul>
          <h2 id="required_and_optional_entity_fields" data-text="Required and optional fields for entity types">Required and optional fields for entity types</h2>
          <table>
            <thead><tr><th>Entity type</th><th>Entity-specific requirements</th></tr></thead>
            <tbody>
              <tr>
                <td><code>IP_ADDRESS</code></td>
                <td><ul><li><code>entity.ip</code> must contain at least one valid IP address.</li></ul></td>
              </tr>
              <tr>
                <td><code>FILE</code></td>
                <td><ul><li><code>entity.file</code> must be present and contain at least one field.</li></ul></td>
              </tr>
            </tbody>
          </table>
          <h2 id="required_and_optional_fields" data-text="Required and optional fields for each event type">Required and optional fields for each event type</h2>
          <h3 id="network_http" data-text="NETWORK_HTTP, TEST_EVENT">NETWORK_HTTP, TEST_EVENT</h3>
          <p>Required fields:</p>
          <ul>
            <li><strong>metadata</strong>: Include the required fields.</li>
            <li><strong>target</strong>: Represents the web server.</li>
          </ul>
          <p>Optional fields:</p>
          <ul><li><strong>principal</strong>: Represents the client.</li></ul>
          <p>Notes:</p>
          <ul><li>Never populate principal.email.</li></ul>
          <h5 data-text="UDM example for NETWORK_HTTP">UDM example for NETWORK_HTTP</h5>
          <devsite-code><pre><code>metadata { event_type: NETWORK_HTTP }</code></pre></devsite-code>
        </article>
        <devsite-content-footer>
          <p>Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License.</p>
          <p>Last updated 2026-06-03 UTC.</p>
        </devsite-content-footer>
        </body></html>
        """
        field_list_html = """
        <html><body>
        <article>
          <h1 data-text="Unified Data Model field list">Unified Data Model field list</h1>
          <p>When specifying a field, use the following format: <code>&lt;prefix&gt;.&lt;field_name&gt;=&lt;value&gt;</code></p>
          <p>When writing rules for Detect Engine, use the &lt;prefix&gt; pattern <code>$event</code> for Event fields and <code>$entity</code> for Entity fields. For example:</p>
          <ul>
            <li><code>$event.metadata.event_type</code></li>
            <li><code>$entity.graph.entity.hostname</code></li>
          </ul>
          <p>When you write configuration-based normalizer (CBN) parsers, use the &lt;prefix&gt; pattern <code>event.idm.read_only_udm</code> for UDM Event fields and <code>event.idm.graph</code> for UDM Entity fields. For example:</p>
          <ul>
            <li><code>event.idm.read_only_udm.metadata.event_type</code></li>
            <li><code>event.idm.graph.entity.user.userid</code></li>
          </ul>
          <p>Field name and field type values can look similar.</p>
          <ul>
            <li>Field type values use camelCase characters.</li>
            <li>Field name values use lowercase characters.</li>
          </ul>
          <h2 id="standard_datatypes" data-text="Standard datatypes">Standard datatypes</h2>
          <table>
            <thead>
              <tr><th>Datatype</th><th>Notes</th><th>C++</th><th>Java</th></tr>
            </thead>
            <tbody>
              <tr><td>int32<a name="int32"></a></td><td>Uses variable-length encoding.</td><td>int32</td><td>int</td></tr>
              <tr><td>string<a name="string"></a></td><td>A string must contain UTF-8 text.</td><td>string</td><td>String</td></tr>
            </tbody>
          </table>
        </article>
        <devsite-content-footer>
          <p>Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License.</p>
          <p>Last updated 2026-06-03 UTC.</p>
        </devsite-content-footer>
        </body></html>
        """
        (
            usage_source,
            usage_field_path_notes,
            field_guidance,
            event_type_categories,
            entity_guidance,
            event_guidance,
        ) = MODULE.parse_usage_guide(usage_html)
        field_list_source, field_paths, datatypes = MODULE.parse_field_list_guide(
            field_list_html,
        )
        return MODULE.DocsGuidance(
            usage_source=usage_source,
            field_list_source=field_list_source,
            field_guidance=field_guidance,
            event_type_categories=event_type_categories,
            entity_guidance=entity_guidance,
            event_guidance=event_guidance,
            field_paths=MODULE.merge_field_path_guidance(
                usage_field_path_notes,
                field_paths,
            ),
            datatypes=datatypes,
        )

    def _write(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
