from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "generate-tenzir-docs-skill.py"
)
SPEC = importlib.util.spec_from_file_location("generate_tenzir_docs_skill", SCRIPT_PATH)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GenerateTenzirDocsSkillTest(unittest.TestCase):
    def test_changelog_exclusion_is_path_based(self) -> None:
        self.assertTrue(MODULE.is_excluded_source_path("changelog.md"))
        self.assertTrue(MODULE.is_excluded_source_path("changelog/tenzir-ship.md"))
        self.assertTrue(MODULE.is_excluded_source_path("/changelog/timeline/2026.md"))
        self.assertFalse(MODULE.is_excluded_source_path("reference/ship-framework.md"))
        self.assertFalse(
            MODULE.is_excluded_source_path("guides/packages/maintain-a-changelog.md")
        )

    def test_generation_keeps_release_docs_and_drops_changelog_tree(self) -> None:
        with tempfile.TemporaryDirectory() as input_dir_str, tempfile.TemporaryDirectory() as output_dir_str:
            input_dir = Path(input_dir_str)
            output_dir = Path(output_dir_str)

            self._write(
                input_dir / "sitemap.md",
                "\n".join(
                    [
                        "# [Tenzir Documentation Map](https://docs.tenzir.com/sitemap.md)",
                        "",
                        "## [Guides](https://docs.tenzir.com/guides.md)",
                        "",
                        "### [Maintain a changelog](https://docs.tenzir.com/guides/packages/maintain-a-changelog.md)",
                        "",
                        "## [Reference](https://docs.tenzir.com/reference.md)",
                        "",
                        "### [Ship Framework](https://docs.tenzir.com/reference/ship-framework.md)",
                        "",
                        "## [Changelog](https://docs.tenzir.com/changelog.md)",
                        "",
                        "### [Tenzir Ship](https://docs.tenzir.com/changelog/tenzir-ship.md)",
                        "",
                    ]
                ),
            )
            self._write(
                input_dir / "guides/packages/maintain-a-changelog.md",
                "[Ship Framework](/reference/ship-framework.md)\n\n"
                "[Recent releases](/changelog/tenzir-ship.md)\n",
            )
            self._write(
                input_dir / "reference/ship-framework.md",
                "[Package guide](/guides/packages/maintain-a-changelog.md)\n",
            )
            self._write(input_dir / "changelog.md", "# Changelog\n")
            self._write(input_dir / "changelog/tenzir-ship.md", "# Tenzir Ship\n")

            sitemap_root = MODULE.parse_heading_tree(
                (input_dir / "sitemap.md").read_text(encoding="utf-8")
            )
            skill_markdown = MODULE.generate_skill_markdown(sitemap_root)
            self.assertIn("guides/packages/maintain-a-changelog.md", skill_markdown)
            self.assertIn("reference/ship-framework.md", skill_markdown)
            self.assertNotIn("](changelog.md)", skill_markdown)
            self.assertNotIn("](changelog/tenzir-ship.md)", skill_markdown)
            self.assertNotIn("## [Changelog]", skill_markdown)

            markdown_files = [
                file_path
                for file_path in MODULE.collect_markdown_files(input_dir)
                if file_path != "sitemap.md"
            ]

            output_dir.mkdir(parents=True, exist_ok=True)
            (output_dir / "SKILL.md").write_text(skill_markdown, encoding="utf-8")
            copied = MODULE.write_skill_files(input_dir, output_dir, markdown_files)

            self.assertEqual(copied, 2)
            self.assertTrue((output_dir / "guides/packages/maintain-a-changelog.md").exists())
            self.assertTrue((output_dir / "reference/ship-framework.md").exists())
            self.assertFalse((output_dir / "changelog.md").exists())
            self.assertFalse((output_dir / "changelog/tenzir-ship.md").exists())

            guide_text = (output_dir / "guides/packages/maintain-a-changelog.md").read_text(
                encoding="utf-8"
            )
            self.assertIn("[Ship Framework](../../reference/ship-framework.md)", guide_text)
            self.assertIn("Recent releases", guide_text)
            self.assertNotIn("[Recent releases]", guide_text)

    @staticmethod
    def _write(path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
