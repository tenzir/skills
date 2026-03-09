# Tenzir Ship

> Ship faster with automated release engineering. Manage changelogs, generate release notes, publish GitHub releases.


Ship faster with automated release engineering. Manage changelogs, generate release notes, publish GitHub releases.

[ GitHub ](https://github.com/tenzir/ship/releases)

[Download releases and artifacts](https://github.com/tenzir/ship/releases)

[ RSS Feed ](/changelog/tenzir-ship.xml)

[Subscribe to release updates](/changelog/tenzir-ship.xml)

## Releases

* [v1.3.1 Mar 4, 2026](tenzir-ship/v1-3-1.md)

  [This release improves clarity and efficacy of the releasing process in the tenzir-ship agent skill.](tenzir-ship/v1-3-1.md)
* [v1.3.0 Mar 2, 2026](tenzir-ship/v1-3-0.md)

  [This release adds automatic version file updates during release creation and introduces tooling to keep release manifests in sync across package types.](tenzir-ship/v1-3-0.md)
* [v1.2.0 Feb 28, 2026](tenzir-ship/v1-2-0.md)

  [This release adds support for creating releases with only introductory text and no changelog entries, and splits the reusable release workflow into minimal and advanced variants. It also fixes changelog structure validation and release progress panel display issues.](tenzir-ship/v1-2-0.md)
* [v1.1.2 Jan 26, 2026](tenzir-ship/v1-1-2.md)

  [This release fixes bugs in changelog entry processing and version detection. The `authors` field now correctly normalizes single string values, and the `show` command no longer misidentifies entry IDs as release versions.](tenzir-ship/v1-1-2.md)
* [v1.1.1 Jan 23, 2026](tenzir-ship/v1-1-1.md)

  [This release fixes two bugs: the multi-project `show` command now displays entries in consistent chronological order, and release recovery instructions show the actual branch name instead of a placeholder.](tenzir-ship/v1-1-1.md)
* [v1.1.0 Jan 17, 2026](tenzir-ship/v1-1-0.md)

  [This release improves the user experience when `release publish` encounters failures mid-workflow. You now see a clear progress summary showing which steps completed, which step failed, and what remains pending—making recovery straightforward.](tenzir-ship/v1-1-0.md)
* [v1.0.0 Jan 9, 2026](tenzir-ship/v1-0-0.md)

  [This major release renames the package from `tenzir-changelog` to `tenzir-ship` and introduces several breaking changes to streamline the CLI interface. The `show` command now uses intuitive positional tokens (`unreleased`, `released`, `latest`, `all`) instead of flags, and the `release notes` co...](tenzir-ship/v1-0-0.md)
* [v0.19.1 Jan 4, 2026](tenzir-ship/v0-19-1.md)

  [This release adds initial release support with implicit version bumping and fixes row numbering in multi-project views.](tenzir-ship/v0-19-1.md)
* [v0.19.0 Dec 30, 2025](tenzir-ship/v0-19-0.md)

  [This release adds configuration options to disable automatic PR and author detection, giving projects more control over changelog entry metadata.](tenzir-ship/v0-19-0.md)
* [v0.18.2 Dec 24, 2025](tenzir-ship/v0-18-2.md)

  [This release adds persistent configuration support for explicit link formatting, allowing projects to set a default link rendering style in `config.yaml` that applies across all commands.](tenzir-ship/v0-18-2.md)
* [v0.18.1 Dec 24, 2025](tenzir-ship/v0-18-1.md)

  [This release adds explicit Markdown link conversion for GitHub references, enabling better compatibility with external documentation sites and Markdown renderers that don't automatically link @mentions and #PR references.](tenzir-ship/v0-18-1.md)
* [v0.18.0 Dec 21, 2025](tenzir-ship/v0-18-0.md)

  [This release introduces a version-agnostic release workflow that simplifies publishing and CI integration, allowing commands to default to the latest release version. It also improves changelog browsing by sorting module entries chronologically rather than grouping them by project.](tenzir-ship/v0-18-0.md)
* [v0.17.2 Dec 21, 2025](tenzir-ship/v0-17-2.md)
* [v0.17.1 Dec 21, 2025](tenzir-ship/v0-17-1.md)

  [This release fixes a critical bug where status messages were written to stdout instead of stderr, breaking GitHub workflows and scripts that capture version output from commands like `release create`.](tenzir-ship/v0-17-1.md)
* [v0.17.0 Dec 19, 2025](tenzir-ship/v0-17-0.md)

  [This release enhances shell scripting capabilities by making `release create` output the version to stdout. All Rich UI elements now go to stderr, enabling clean machine-readable results for automation workflows.](tenzir-ship/v0-17-0.md)
* [v0.16.0 Dec 19, 2025](tenzir-ship/v0-16-0.md)

  [This release introduces aggregated module changelog summaries in release notes, allowing parent projects to automatically include a summary of changes from their modules. It also fixes a minor issue with redundant version fields in JSON output.](tenzir-ship/v0-16-0.md)
* [v0.15.0 Dec 18, 2025](tenzir-ship/v0-15-0.md)

  [This release adds new options to the `release publish` command for more flexible release automation. You can now prevent GitHub from marking a release as latest with `--no-latest` (useful for backport releases), and automatically commit staged changes before tagging with `--commit`.](tenzir-ship/v0-15-0.md)
* [v0.14.0 Dec 17, 2025](tenzir-ship/v0-14-0.md)

  [This release adds H1 headings to release notes output, making documents more structured and easier to navigate.](tenzir-ship/v0-14-0.md)
* [v0.13.1 Dec 16, 2025](tenzir-ship/v0-13-1.md)

  [This release streamlines module mode by removing the multi-project feature in favor of the dedicated `modules` configuration. It removes the `--include-modules` flag (modules are now always included when configured) and enhances module mode to show released entries with version numbers. The relea...](tenzir-ship/v0-13-1.md)
* [v0.13.0 Dec 16, 2025](tenzir-ship/v0-13-0.md)

  [This release streamlines module mode by removing the multi-project feature in favor of the dedicated `modules` configuration. It removes the `--include-modules` flag (modules are now always included when configured) and enhances module mode to show released entries with version numbers. The relea...](tenzir-ship/v0-13-0.md)
* [v0.12.0 Dec 15, 2025](tenzir-ship/v0-12-0.md)

  [This release adds support for nested changelog projects through modules, improves export formats with structured URL fields in JSON, and enhances the CLI with better export options and configuration flexibility for components.](tenzir-ship/v0-12-0.md)
* [v0.11.1 Dec 11, 2025](tenzir-ship/v0-11-1.md)

  [This patch release improves the CLI display with better card view styling and author formatting. The card view now displays type-colored borders and properly formats non-GitHub authors without the @ prefix for improved readability.](tenzir-ship/v0-11-1.md)
* [v0.11.0 Dec 5, 2025](tenzir-ship/v0-11-0.md)

  [This release adds the `--co-author` option for crediting additional authors (useful for AI-assisted development) and improves entry parsing to accept the plural `components` key in frontmatter.](tenzir-ship/v0-11-0.md)
* [v0.10.0 Dec 4, 2025](tenzir-ship/v0-10-0.md)

  [This release adds support for reading changelog entry descriptions from files or stdin, making it easier to integrate with automated workflows and pipelines.](tenzir-ship/v0-10-0.md)
* [v0.9.1 Dec 3, 2025](tenzir-ship/v0-9-1.md)
* [v0.9.0 Dec 3, 2025](tenzir-ship/v0-9-0.md)
* [v0.8.1 Nov 10, 2025](tenzir-ship/v0-8-1.md)

  [Patch release to stabilize GitHub context inference tests.](tenzir-ship/v0-8-1.md)
* [v0.8.0 Nov 10, 2025](tenzir-ship/v0-8-0.md)

  [Infer GitHub context for entries, keep the Python API non-interactive, and showcase components in the dogfooded project.](tenzir-ship/v0-8-0.md)
* [v0.7.0 Nov 9, 2025](tenzir-ship/v0-7-0.md)

  [Expose the CLI as a Python API.](tenzir-ship/v0-7-0.md)
* [v0.6.0 Nov 2, 2025](tenzir-ship/v0-6-0.md)

  [Refine release manifest format: rename 'description' to 'intro' and render it with a folded YAML block for better readability.](tenzir-ship/v0-6-0.md)
* [v0.5.0 Nov 2, 2025](tenzir-ship/v0-5-0.md)

  [This release adds support for multi-project operations and package-aware discovery.](tenzir-ship/v0-5-0.md)
* [v0.4.1 Oct 27, 2025](tenzir-ship/v0-4-1.md)

  [This release improves GitHub release note formatting.](tenzir-ship/v0-4-1.md)
* [v0.4.0 Oct 27, 2025](tenzir-ship/v0-4-0.md)

  [This release adds components to entries, supports tagging during publish, and polishes release creation output while inverting the show table order.](tenzir-ship/v0-4-0.md)
* [v0.3.0 Oct 24, 2025](tenzir-ship/v0-3-0.md)

  [This release refines the workflow and exports, introduces numeric entry prefixes and emoji-styled types, and improves table layout and PR metadata.](tenzir-ship/v0-3-0.md)
* [v0.2.0 Oct 21, 2025](tenzir-ship/v0-2-0.md)

  [This release improves table and export layouts, simplifies configuration, and streamlines the release archive while fixing logging and ordering.](tenzir-ship/v0-2-0.md)
* [v0.1.0 Oct 21, 2025](tenzir-ship/v0-1-0.md)

  [This initial version introduces the inaugural `tenzir-changelog` CLI, covering project bootstrapping, entry capture, rich browsing, release assembly, documentation, and validation tooling.](tenzir-ship/v0-1-0.md)