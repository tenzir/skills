from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


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
                classes,
                intermediates,
                {"attributes": {}},
            )
            self.assertEqual(
                inherited,
                [
                    ("Network Activity", [("src_endpoint", "recommended")]),
                    ("Base Event", [("time", "required")]),
                ],
            )

    @staticmethod
    def _write_json(path: Path, data: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(MODULE.json.dumps(data), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
