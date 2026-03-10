from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "generate-ocsf-skill.py"
)
SPEC = importlib.util.spec_from_file_location("generate_ocsf_skill", SCRIPT_PATH)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GenerateOcsfSkillTest(unittest.TestCase):
    def test_load_classes_keys_category_bases_by_schema_name(self) -> None:
        with tempfile.TemporaryDirectory() as schema_dir_str:
            schema_dir = Path(schema_dir_str)
            self._write_json(
                schema_dir / "events" / "base_event.json",
                {
                    "name": "base_event",
                    "caption": "Base Event",
                    "attributes": {
                        "time": {"requirement": "required"},
                    },
                },
            )
            self._write_json(
                schema_dir / "events" / "network" / "network.json",
                {
                    "name": "network_activity",
                    "caption": "Network Activity",
                    "extends": "base_event",
                    "profiles": ["base_profile"],
                    "attributes": {
                        "src_endpoint": {"requirement": "recommended"},
                    },
                },
            )
            self._write_json(
                schema_dir / "events" / "network" / "http.json",
                {
                    "name": "http",
                    "caption": "HTTP Activity",
                    "extends": "network_activity",
                    "profiles": ["http_profile"],
                    "attributes": {
                        "http_method": {"requirement": "required"},
                    },
                },
            )

            classes, intermediates = MODULE.load_classes(schema_dir)

            self.assertIn("http", classes)
            self.assertIn("network_activity", intermediates)
            self.assertNotIn("network", intermediates)
            self.assertEqual(intermediates["network_activity"]["category_key"], "network")

            http_profiles = MODULE.resolve_profiles(classes["http"], classes, intermediates)
            self.assertEqual(http_profiles, ["http_profile", "base_profile"])

            inherited = MODULE.collect_inherited_attributes(
                classes["http"],
                {"attributes": {}},
                classes,
                intermediates,
            )
            self.assertEqual(
                inherited,
                [
                    ("Network Activity", [("src_endpoint", "recommended")]),
                    ("Base Event", [("time", "required")]),
                ],
            )

    def test_clean_description_rewrites_relative_links(self) -> None:
        rendered = MODULE.clean_description(
            "See <a href='file_activity'>File Activity</a> for details.",
        )
        self.assertEqual(rendered, "See [File Activity](file_activity.md) for details.")

    def test_main_generates_extension_detail_pages(self) -> None:
        with (
            tempfile.TemporaryDirectory() as schema_dir_str,
            tempfile.TemporaryDirectory() as output_dir_str,
        ):
            schema_dir = Path(schema_dir_str)
            output_dir = Path(output_dir_str)
            self._write_json(
                schema_dir / "categories.json",
                {
                    "attributes": {
                        "system": {
                            "caption": "System Activity",
                            "description": "System events.",
                            "uid": 1,
                        }
                    }
                },
            )
            self._write_json(
                schema_dir / "dictionary.json",
                {
                    "attributes": {
                        "time": {
                            "caption": "Time",
                            "description": "Event time.",
                            "type": "timestamp_t",
                        },
                        "process": {
                            "caption": "Process",
                            "description": "Process object.",
                            "type": "process",
                        },
                    }
                },
            )
            self._write_json(
                schema_dir / "events" / "base_event.json",
                {
                    "name": "base_event",
                    "caption": "Base Event",
                    "attributes": {
                        "time": {"requirement": "required"},
                    },
                },
            )
            self._write_json(
                schema_dir / "events" / "system" / "system.json",
                {
                    "name": "system_activity",
                    "caption": "System Activity",
                    "extends": "base_event",
                    "attributes": {
                        "process": {"requirement": "recommended"},
                    },
                },
            )
            self._write_json(
                schema_dir / "objects" / "process.json",
                {
                    "caption": "Process",
                    "description": "A process.",
                    "attributes": {
                        "pid": {
                            "caption": "PID",
                            "description": "Process ID.",
                            "type": "integer_t",
                        }
                    },
                },
            )
            self._write_json(
                schema_dir / "extensions" / "linux" / "extension.json",
                {
                    "uid": 1,
                    "caption": "Linux",
                    "description": "Linux-specific fields.",
                    "name": "linux",
                    "version": "1.7.0",
                },
            )
            self._write_json(
                schema_dir / "extensions" / "linux" / "dictionary.json",
                {
                    "attributes": {
                        "auid": {
                            "caption": "Audit User ID",
                            "description": "Audit user identifier.",
                            "type": "integer_t",
                        }
                    }
                },
            )
            self._write_json(
                schema_dir / "extensions" / "linux" / "profiles" / "linux_users.json",
                {
                    "caption": "Linux Users",
                    "description": "Linux user fields.",
                    "name": "linux_users",
                    "attributes": {
                        "auid": {"requirement": "optional"},
                    },
                },
            )
            self._write_json(
                schema_dir / "extensions" / "linux" / "objects" / "process.json",
                {
                    "caption": "Linux Process",
                    "description": "Extends the process object.",
                    "extends": "process",
                    "profiles": ["linux/linux_users"],
                    "attributes": {},
                },
            )
            self._write_json(
                schema_dir / "extensions" / "linux" / "events" / "process_exec.json",
                {
                    "uid": 42,
                    "caption": "Process Exec",
                    "description": "Linux process execution.",
                    "extends": "system_activity",
                    "profiles": ["linux/linux_users"],
                    "attributes": {
                        "process": {"requirement": "required"},
                    },
                },
            )

            with (
                mock.patch.object(
                    MODULE,
                    "parse_args",
                    return_value=MODULE.argparse.Namespace(
                        output_dir=str(output_dir),
                        version="1.7.0",
                        latest_only=False,
                    ),
                ),
                mock.patch.object(
                    MODULE,
                    "collect_version_specs",
                    return_value=[MODULE.VersionSpec("1.7.0", "v1.7.0", True)],
                ),
                mock.patch.object(MODULE, "clone_schema", return_value=schema_dir),
                mock.patch.object(MODULE, "fetch_pages", return_value=[]),
                mock.patch.object(MODULE, "fetch_text", return_value="# Understanding OCSF\n"),
            ):
                MODULE.main()

            extension_dir = output_dir / "v1.7.0" / "extensions" / "linux"
            self.assertTrue((extension_dir / "index.md").exists())
            self.assertTrue((extension_dir / "events" / "process_exec.md").exists())
            self.assertTrue((extension_dir / "objects" / "process.md").exists())
            self.assertTrue((extension_dir / "profiles" / "linux_users.md").exists())

            extensions_index = (output_dir / "v1.7.0" / "extensions.md").read_text(encoding="utf-8")
            self.assertIn("(extensions/linux/index.md)", extensions_index)

            object_page = (extension_dir / "objects" / "process.md").read_text(encoding="utf-8")
            self.assertIn("[Linux Users](../profiles/linux_users.md)", object_page)

            profile_page = (extension_dir / "profiles" / "linux_users.md").read_text(encoding="utf-8")
            self.assertIn("### `auid`", profile_page)
            self.assertIn("Audit user identifier.", profile_page)
            self.assertIn("## Applies to", profile_page)
            self.assertIn("- Linux Process", profile_page)
            self.assertIn("- Process Exec", profile_page)

            event_page = (extension_dir / "events" / "process_exec.md").read_text(encoding="utf-8")
            self.assertIn("[Linux Users](../profiles/linux_users.md)", event_page)
            self.assertIn("[`process`](../objects/process.md)", event_page)

    @staticmethod
    def _write_json(path: Path, data: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(MODULE.json.dumps(data), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
