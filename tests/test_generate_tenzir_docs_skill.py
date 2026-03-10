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
        self.assertTrue(MODULE.is_excluded_source_path("reference/ocsf.md"))
        self.assertTrue(MODULE.is_excluded_source_path("/reference/ocsf/1-7-0/classes.md"))
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
            markdown_files = [
                f for f in MODULE.collect_markdown_files(input_dir) if f != "sitemap.md"
            ]
            available_source_paths = MODULE.build_available_source_paths(markdown_files)
            skill_markdown = MODULE.generate_skill_markdown(
                input_dir, sitemap_root, available_source_paths
            )
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

    def test_out_of_bundle_docs_targets_stay_absolute(self) -> None:
        available_source_paths = {
            "reference/operators/api.md",
            "tutorials/map-data-to-ocsf.md",
        }

        self.assertEqual(
            MODULE.rewrite_link_destination(
                "/reference/operators/api.md",
                "tutorials/map-data-to-ocsf.md",
                available_source_paths,
            ),
            "../reference/operators/api.md",
        )
        self.assertEqual(
            MODULE.rewrite_link_destination(
                "/reference/node/api",
                "reference/operators/api.md",
                available_source_paths,
            ),
            "https://docs.tenzir.com/reference/node/api",
        )
        self.assertEqual(
            MODULE.rewrite_link_destination(
                "/packages/zeek/tests/inputs/conn.log.md",
                "tutorials/map-data-to-ocsf.md",
                available_source_paths,
            ),
            "https://docs.tenzir.com/packages/zeek/tests/inputs/conn.log.md",
        )

    def test_generation_adds_compact_reference_indexes_and_deeper_leaf_pages(self) -> None:
        with tempfile.TemporaryDirectory() as input_dir_str:
            input_dir = Path(input_dir_str)

            self._write(
                input_dir / "sitemap.md",
                "\n".join(
                    [
                        "# [Tenzir Documentation Map](https://docs.tenzir.com/sitemap.md)",
                        "",
                        "## [Guides](https://docs.tenzir.com/guides.md)",
                        "",
                        "### Setup",
                        "",
                        "#### [Node Setup](https://docs.tenzir.com/guides/node-setup.md)",
                        "",
                        "##### [Deploy a node](https://docs.tenzir.com/guides/node-setup/deploy-a-node.md)",
                        "",
                        "## [Reference](https://docs.tenzir.com/reference.md)",
                        "",
                        "### Language (TQL)",
                        "",
                        "#### [Operators](https://docs.tenzir.com/reference/operators.md)",
                        "",
                        "##### [api](https://docs.tenzir.com/reference/operators/api.md)",
                        "",
                        "#### [Functions](https://docs.tenzir.com/reference/functions.md)",
                        "",
                        "##### [count](https://docs.tenzir.com/reference/functions/count.md)",
                        "",
                        "#### [Node](https://docs.tenzir.com/reference/node.md)",
                        "",
                        "##### [Configuration](https://docs.tenzir.com/reference/node/configuration.md)",
                        "",
                        "#### [Platform](https://docs.tenzir.com/reference/platform.md)",
                        "",
                        "##### [Command line interface](https://docs.tenzir.com/reference/platform/command-line-interface.md)",
                        "",
                        "#### [Claude Marketplace](https://docs.tenzir.com/reference/claude-plugins.md)",
                        "",
                        "##### [Python](https://docs.tenzir.com/reference/claude-plugins/python.md)",
                        "",
                        "#### [OCSF](https://docs.tenzir.com/reference/ocsf.md)",
                        "",
                        "##### [Classes](https://docs.tenzir.com/reference/ocsf/1-7-0/classes.md)",
                        "",
                        "## [Integrations](https://docs.tenzir.com/integrations.md)",
                        "",
                        "### Cloud Providers",
                        "",
                        "#### [Amazon](https://docs.tenzir.com/integrations/amazon.md)",
                        "",
                        "##### [GuardDuty](https://docs.tenzir.com/integrations/amazon/guardduty.md)",
                        "",
                    ]
                ),
            )
            self._write(input_dir / "guides/node-setup.md", "# Node Setup\n")
            self._write(input_dir / "guides/node-setup/deploy-a-node.md", "# Deploy a node\n")
            self._write(input_dir / "reference/operators/api.md", "# api\n")
            self._write(input_dir / "reference/operators/chart_area.md", "# chart_area\n")
            self._write(input_dir / "reference/functions/count.md", "# count\n")
            self._write(input_dir / "reference/node.md", "# Node\n")
            self._write(input_dir / "reference/node/configuration.md", "# Configuration\n")
            self._write(input_dir / "reference/platform.md", "# Platform\n")
            self._write(
                input_dir / "reference/platform/command-line-interface.md",
                "# Command line interface\n",
            )
            self._write(input_dir / "reference/claude-plugins.md", "# Claude Marketplace\n")
            self._write(input_dir / "reference/claude-plugins/python.md", "# Python\n")
            self._write(input_dir / "reference/ocsf.md", "# OCSF\n")
            self._write(input_dir / "reference/ocsf/1-7-0/classes.md", "# Classes\n")
            self._write(input_dir / "integrations/amazon.md", "# Amazon\n")
            self._write(input_dir / "integrations/amazon/guardduty.md", "# GuardDuty\n")
            self._write(
                input_dir / "reference/operators.md",
                "\n".join(
                    [
                        "# Operators",
                        "",
                        "## Query",
                        "",
                        "### [api](https://docs.tenzir.com/reference/operators/api.md)",
                        "",
                        "Use Tenzir's REST API directly from a pipeline.",
                        "",
                        "### [chart\\_area](https://docs.tenzir.com/reference/operators/chart_area.md)",
                        "",
                        "Plots events on an area chart.",
                        "",
                        "### [where](https://docs.tenzir.com/reference/operators/where.md)",
                        "",
                        "Filters events by predicate.",
                        "",
                    ]
                ),
            )
            self._write(
                input_dir / "reference/functions.md",
                "\n".join(
                    [
                        "# Functions",
                        "",
                        "## Aggregation",
                        "",
                        "### [count](https://docs.tenzir.com/reference/functions/count.md)",
                        "",
                        "Counts events.",
                        "",
                    ]
                ),
            )

            sitemap_root = MODULE.parse_heading_tree(
                (input_dir / "sitemap.md").read_text(encoding="utf-8")
            )
            markdown_files = [
                f for f in MODULE.collect_markdown_files(input_dir) if f != "sitemap.md"
            ]
            available_source_paths = MODULE.build_available_source_paths(markdown_files)
            skill_markdown = MODULE.generate_skill_markdown(
                input_dir, sitemap_root, available_source_paths
            )

            self.assertIn("##### [Deploy a node](guides/node-setup/deploy-a-node.md)", skill_markdown)
            self.assertIn("##### [GuardDuty](integrations/amazon/guardduty.md)", skill_markdown)
            # Operator and function indexes are extracted to separate files,
            # so they must NOT appear inline in SKILL.md.
            self.assertNotIn("#### Operator Index", skill_markdown)
            self.assertNotIn("#### Function Index", skill_markdown)
            # Instead, a pointer section directs the model to the extracted
            # index files.
            self.assertIn("### Indexes", skill_markdown)
            self.assertIn("[Operator Index](reference/operators-index.md)", skill_markdown)
            self.assertIn("[Function Index](reference/functions-index.md)", skill_markdown)
            # Non-operator/function reference indexes remain inline.
            self.assertIn("#### Claude Marketplace Index", skill_markdown)
            self.assertIn("- [Python](reference/claude-plugins/python.md)", skill_markdown)
            self.assertIn("#### Node Index", skill_markdown)
            self.assertIn("- [Configuration](reference/node/configuration.md)", skill_markdown)
            self.assertIn("#### Platform Index", skill_markdown)
            self.assertIn(
                "- [Command line interface](reference/platform/command-line-interface.md)",
                skill_markdown,
            )
            # Per-category operator/function entries are in the extracted
            # files, not inline.
            self.assertNotIn("##### Query", skill_markdown)
            self.assertNotIn("- [api](reference/operators/api.md)", skill_markdown)
            self.assertNotIn("- [chart_area](reference/operators/chart_area.md)", skill_markdown)
            self.assertNotIn("reference/ocsf.md", skill_markdown)
            self.assertNotIn("reference/ocsf/1-7-0/classes.md", skill_markdown)
            self.assertNotIn("[chart\\_area]", skill_markdown)
            self.assertNotIn("Use Tenzir's REST API directly from a pipeline.", skill_markdown)
            self.assertNotIn("Plots events on an area chart.", skill_markdown)
            self.assertNotIn("Filters events by predicate.", skill_markdown)
            self.assertNotIn("Counts events.", skill_markdown)

    def test_generation_adds_synthetic_reference_indexes_without_parent_pages(self) -> None:
        with tempfile.TemporaryDirectory() as input_dir_str:
            input_dir = Path(input_dir_str)

            self._write(
                input_dir / "sitemap.md",
                "\n".join(
                    [
                        "# [Tenzir Documentation Map](https://docs.tenzir.com/sitemap.md)",
                        "",
                        "## [Reference](https://docs.tenzir.com/reference.md)",
                        "",
                        "### Tools",
                        "",
                    ]
                ),
            )
            self._write(
                input_dir / "reference/node/configuration.md",
                "# Configuration\n",
            )
            self._write(
                input_dir / "reference/platform/command-line-interface.md",
                "# Command line interface\n",
            )

            sitemap_root = MODULE.parse_heading_tree(
                (input_dir / "sitemap.md").read_text(encoding="utf-8")
            )
            markdown_files = [
                f for f in MODULE.collect_markdown_files(input_dir) if f != "sitemap.md"
            ]
            available_source_paths = MODULE.build_available_source_paths(markdown_files)
            skill_markdown = MODULE.generate_skill_markdown(
                input_dir, sitemap_root, available_source_paths
            )

            self.assertIn("#### Node Index", skill_markdown)
            self.assertIn("- [Configuration](reference/node/configuration.md)", skill_markdown)
            self.assertIn("#### Platform Index", skill_markdown)
            self.assertIn(
                "- [Command line interface](reference/platform/command-line-interface.md)",
                skill_markdown,
            )

    def test_generation_keeps_unindexed_special_reference_children(self) -> None:
        with tempfile.TemporaryDirectory() as input_dir_str:
            input_dir = Path(input_dir_str)

            self._write(
                input_dir / "sitemap.md",
                "\n".join(
                    [
                        "# [Tenzir Documentation Map](https://docs.tenzir.com/sitemap.md)",
                        "",
                        "## [Reference](https://docs.tenzir.com/reference.md)",
                        "",
                        "### Language (TQL)",
                        "",
                        "#### [Functions](https://docs.tenzir.com/reference/functions.md)",
                        "",
                        "##### [count](https://docs.tenzir.com/reference/functions/count.md)",
                        "",
                    ]
                ),
            )
            self._write(
                input_dir / "reference/functions.md",
                "\n".join(
                    [
                        "# Functions",
                        "",
                        "## Aggregation",
                        "",
                        "### [count](https://docs.tenzir.com/reference/functions/count.md)",
                        "",
                        "Counts events.",
                        "",
                    ]
                ),
            )
            self._write(input_dir / "reference/functions/count.md", "# count\n")
            self._write(input_dir / "reference/functions/hmac.md", "# hmac\n")

            sitemap_root = MODULE.parse_heading_tree(
                (input_dir / "sitemap.md").read_text(encoding="utf-8")
            )
            markdown_files = [
                f for f in MODULE.collect_markdown_files(input_dir) if f != "sitemap.md"
            ]
            available_source_paths = MODULE.build_available_source_paths(markdown_files)
            skill_markdown = MODULE.generate_skill_markdown(
                input_dir, sitemap_root, available_source_paths
            )

            # The Function Index is extracted to a separate file, not
            # inlined in SKILL.md.
            self.assertNotIn("#### Function Index", skill_markdown)
            self.assertIn("[Function Index](reference/functions-index.md)", skill_markdown)

            # Verify the extracted index contains both the categorized
            # entries and the unindexed "hmac" page.
            func_index = MODULE.generate_extracted_index(
                input_dir,
                "reference/functions.md",
                "Function Index",
                "reference/functions-index.md",
                available_source_paths,
            )
            self.assertIsNotNone(func_index)
            self.assertIn("## Aggregation", func_index)
            self.assertIn("- [count](functions/count.md)", func_index)
            self.assertIn("## Additional Pages", func_index)
            self.assertIn("- [hmac](functions/hmac.md)", func_index)

    @staticmethod
    def _write(path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
