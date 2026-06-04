from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
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
            id_proto = next(
                proto for proto in descriptor_set.file if proto.name == "backstory/id.proto"
            )
            context = MODULE.collect_messages_and_enums(file_proto, [id_proto])
            source = MODULE.SourceRef(ref="fixture", sha="abc123")
            docs = MODULE.build_docs(
                context,
                source,
                {"backstory/udm.proto", "backstory/id.proto"},
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

        self.assertIn("name: tenzir-google-udm", skill_markdown)
        self.assertIn("`abc123`", schema_markdown)
        self.assertIn("[`Metadata`](metadata.md)", udm_page)
        self.assertIn("map<`string`, [`FindingVariable`](finding_variable.md)>", udm_page)
        self.assertIn("[`Id`](id.md)", udm_page)
        self.assertIn("- **Cardinality**: `optional`", udm_page)
        self.assertIn("`google.protobuf.Timestamp` (imported)", metadata_page)
        self.assertIn("- `typed_value`: `string_value`, `int64_value`", variable_page)
        self.assertIn("### `NORMALIZED_TELEMETRY`", namespace_page)
        self.assertIn("[`Id.Namespace`](../enums/id_namespace.md)", id_page)
        self.assertIn("### `OLD_TEST_EVENT`", event_type_page)
        self.assertIn("- **Deprecated**: `true`", event_type_page)
        self.assertIn("# Event Types", dedicated_event_types)
        self.assertIn("Test event.", dedicated_event_types)

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

    def _write(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
