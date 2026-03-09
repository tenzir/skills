# Timeline

> A chronological view of all changes across all Tenzir projects.


Browse all release updates across Tenzir projects in reverse-chronological order. Use the toggle to include unreleased changes that are in development.

[ GitHub ](https://github.com/tenzir)

[Tenzir open source projects](https://github.com/tenzir)

[ RSS Feed ](/changelog/feed.xml)

[Subscribe to all release updates](/changelog/feed.xml)

## Releases

* [ Tenzir Node v5.28.0 Mar 6, 2026](tenzir/v5-28-0.md)

  [This release adds support for parsing Check Point syslog structured-data dialects that deviate from RFC 5424, improving out-of-the-box interoperability with Check Point exports. It also makes DNS hostname resolution in the load\_tcp operator opt-in and fixes several parser bugs related to schema c...](tenzir/v5-28-0.md)
* [ Tenzir Platform v1.29.0 Mar 5, 2026](platform/v1-29-0.md)

  [With this release, the Tenzir Platform preserves deep links through the login flow, so users are redirected to their original destination after signing in. It also includes several bug fixes and a performance improvement for loading across the platform.](platform/v1-29-0.md)
* [ Tenzir Ship v1.3.1 Mar 4, 2026](tenzir-ship/v1-3-1.md)

  [This release improves clarity and efficacy of the releasing process in the tenzir-ship agent skill.](tenzir-ship/v1-3-1.md)
* [ Tenzir Node v5.27.3 Mar 3, 2026](tenzir/v5-27-3.md)

  [This release fixes a crash that could occur when reading JSON data. It also improves CEF parsing to handle non-conforming unescaped equals characters.](tenzir/v5-27-3.md)
* [ Tenzir Ship v1.3.0 Mar 2, 2026](tenzir-ship/v1-3-0.md)

  [This release adds automatic version file updates during release creation and introduces tooling to keep release manifests in sync across package types.](tenzir-ship/v1-3-0.md)
* [ Tenzir Ship v1.2.0 Feb 28, 2026](tenzir-ship/v1-2-0.md)

  [This release adds support for creating releases with only introductory text and no changelog entries, and splits the reusable release workflow into minimal and advanced variants. It also fixes changelog structure validation and release progress panel display issues.](tenzir-ship/v1-2-0.md)
* [ Tenzir Node v5.27.2 Feb 27, 2026](tenzir/v5-27-2.md)

  [This release adds the hmac function for computing Hash-based Message Authentication Codes over strings and blobs. It also fixes an assertion failure in array slicing that was introduced in v5.27.0.](tenzir/v5-27-2.md)
* [ Tenzir Test v1.7.3 Feb 27, 2026](tenzir-test/v1-7-3.md)

  [This release improves parallel suite scheduling reliability and adds correctness guards via suite.min\_jobs in test.yaml.](tenzir-test/v1-7-3.md)
* [ Tenzir Node v5.27.1 Feb 25, 2026](tenzir/v5-27-1.md)

  [This release fixes an issue where the platform plugin did not correctly use the configured certfile, keyfile, and cafile options for client certificate authentication.](tenzir/v5-27-1.md)
* [ Tenzir Test v1.7.2 Feb 25, 2026](tenzir-test/v1-7-2.md)

  [This release fixes enum serialization errors when Python fixture tests use configuration values like mode: sequential in test.yaml.](tenzir-test/v1-7-2.md)
* [ Tenzir Test v1.7.1 Feb 25, 2026](tenzir-test/v1-7-1.md)

  [This release adds parallel suite execution and fixes several bugs, including clean Ctrl+C handling, consistent default fixture options, and reliable shell runner defaults for .sh test files.](tenzir-test/v1-7-1.md)
* [ Tenzir Node v5.27.0 Feb 24, 2026](tenzir/v5-27-0.md)

  [This release enhances the sort function with custom comparators and descending order support, and extends the slice function to work with lists.](tenzir/v5-27-0.md)
* [ Tenzir Platform v1.28.3 Feb 24, 2026](platform/v1-28-3.md)

  [This release improves the clarity and usability of Explorer charts with better legends, tooltips, and an expanded color palette. It also fixes several UI bugs including unresponsive pipeline lists and stale workspace cleanup.](platform/v1-28-3.md)
* [ Tenzir Test v1.7.0 Feb 22, 2026](tenzir-test/v1-7-0.md)

  [This release adds suite-level capability requirements, letting test suites declare required operators and skip gracefully when those capabilities are unavailable in the target build.](tenzir-test/v1-7-0.md)
* [ Tenzir Test v1.6.0 Feb 19, 2026](tenzir-test/v1-6-0.md)

  [This release adds fixture assertion hooks that enable post-test validation of side effects while fixtures remain active. Assertion results are tracked separately in the run summary.](tenzir-test/v1-6-0.md)
* [ Tenzir Platform v1.28.2 Feb 17, 2026](platform/v1-28-2.md)

  [This release brings the Platform's dependencies up to date with the latest CVE fixes.](platform/v1-28-2.md)
* [ Tenzir Test v1.5.1 Feb 16, 2026](tenzir-test/v1-5-1.md)

  [This release improves error handling by showing clean messages for unavailable fixtures and avoids unnecessary fixture initialization for fully skipped test suites.](tenzir-test/v1-5-1.md)
* [ Tenzir Test v1.5.0 Feb 16, 2026](tenzir-test/v1-5-0.md)

  [This release adds fine-grained controls for running skipped tests, including a new --run-skipped-reason flag with substring and glob matching semantics.](tenzir-test/v1-5-0.md)
* [ Tenzir Test v1.4.0 Feb 15, 2026](tenzir-test/v1-4-0.md)

  [This release introduces a standalone fixture mode for starting fixtures without running tests, adds a built-in docker-compose fixture with structured options, and provides shared container runtime helpers for writing custom fixtures.](tenzir-test/v1-4-0.md)
* [ Tenzir Node v5.26.0 Feb 13, 2026](tenzir/v5-26-0.md)

  [This release introduces the from\_mysql operator for reading data directly from MySQL databases, with support for live streaming, custom SQL queries, and TLS connections. It also adds link-based HTTP pagination and optional field parameters for user-defined operators.](tenzir/v5-26-0.md)
* [ Tenzir Test v1.3.2 Feb 13, 2026](tenzir-test/v1-3-2.md)

  [This release improves the readability of configuration override log messages by using relative paths and human-friendly formatting.](tenzir-test/v1-3-2.md)
* [ Claude Marketplace > Dev Plugin v4.2.0 Feb 13, 2026](claude-plugins/dev/v4-2-0.md)

  [This release adds remote release workflow detection to `/dev:release`, letting you trigger GitHub Actions workflows instead of running local release steps. It also modularizes the documentation editing architecture and improves issue identifier guidance in the PR maker agent.](claude-plugins/dev/v4-2-0.md)
* [ Tenzir Test v1.3.1 Feb 11, 2026](tenzir-test/v1-3-1.md)

  [This release adds support for nested dataclass hierarchies in fixture options, enabling multi-level structured configurations in test frontmatter.](tenzir-test/v1-3-1.md)
* [ Tenzir Platform v1.28.1 Feb 10, 2026](platform/v1-28-1.md)

  [This release upgrades pnpm to 9.15.0 in the frontend Docker image to address CVE-2024-53866.](platform/v1-28-1.md)
* [ Tenzir Test v1.3.0 Feb 10, 2026](tenzir-test/v1-3-0.md)

  [This release adds structured configuration options for fixtures, letting tests pass typed parameters through YAML frontmatter using frozen dataclasses.](tenzir-test/v1-3-0.md)
* [ Tenzir Node v5.25.2 Feb 9, 2026](tenzir/v5-25-2.md)

  [This release fixes the sigma operator to correctly load all rule files from a directory.](tenzir/v5-25-2.md)
* [ Tenzir Platform v1.28.0 Feb 9, 2026](platform/v1-28-0.md)

  [This release unifies the library's Available and Installed tabs into a single view, making package management more streamlined. It also adds pipeline activity sorting, series isolation in activity charts, a line wrap toggle in the Inspector, platform version display, and a backslash escaping fix.](platform/v1-28-0.md)
* [ Tenzir Test v1.2.2 Feb 9, 2026](tenzir-test/v1-2-2.md)

  [This release fixes a serialization bug where Python fixture tests with `skip` configurations in `test.yaml` failed with a JSON serialization error.](tenzir-test/v1-2-2.md)
* [ Tenzir Test v1.2.1 Feb 6, 2026](tenzir-test/v1-2-1.md)

  [This patch release improves the `-m`/`--match` flag with automatic substring matching and centralizes skip handling in the engine for more consistent test reporting.](tenzir-test/v1-2-1.md)
* [ Tenzir Test v1.2.0 Feb 6, 2026](tenzir-test/v1-2-0.md)

  [This release adds support for selecting tests by name using glob patterns via the new `-m`/`--match` CLI option.](tenzir-test/v1-2-0.md)
* [ Tenzir Test v1.1.1 Feb 6, 2026](tenzir-test/v1-1-1.md)

  [This release improves the CLI help text with usage examples and a link to the documentation.](tenzir-test/v1-1-1.md)
* [ Tenzir Platform v1.27.1 Feb 2, 2026](platform/v1-27-1.md)

  [This release fixes a bug where users could experience authentication failures due to stale user keys in their session. The platform now proactively checks for expired keys and refreshes them automatically.](platform/v1-27-1.md)
* [ Tenzir Test v1.1.0 Jan 31, 2026](tenzir-test/v1-1-0.md)

  [This release adds stdin file support for piping data directly to tests, and improves satellite project display in project listings.](tenzir-test/v1-1-0.md)
* [ Tenzir Node v5.25.1 Jan 30, 2026](tenzir/v5-25-1.md)

  [This release includes several bug fixes for the JSON parser, `where`, `replace`, and `if` operators, along with Kafka decompression support and a new `raw_message` option for the `read_syslog` operator.](tenzir/v5-25-1.md)
* [ Claude Marketplace > Dev Plugin v4.1.0 Jan 30, 2026](claude-plugins/dev/v4-1-0.md)

  [This release improves workflow automation for changelog creation and code review. The changelog-adder agent now auto-detects changed files and provides clearer guidance for writing user-focused entries. The review command streamlines decision points, reducing prompts while maintaining control ove...](claude-plugins/dev/v4-1-0.md)
* [ Claude Marketplace > Dev Plugin v4.0.0 Jan 28, 2026](claude-plugins/dev/v4-0-0.md)

  [This release introduces a unified code review and fix workflow that consolidates the review, triage, planning, and execution phases into a single `/dev:review` command. The workflow spawns specialized reviewers in parallel, filters findings by confidence, plans fixes with proper dependencies, and...](claude-plugins/dev/v4-0-0.md)
* [ Claude Marketplace > Tenzir Plugin v0.0.1 Jan 28, 2026](claude-plugins/tenzir/v0-0-1.md)

  [This release introduces the `tenzir:guide` subagent for fast documentation lookups and adds dynamic documentation syncing from the latest Tenzir release.](claude-plugins/tenzir/v0-0-1.md)
* [ Tenzir Node v5.25.0 Jan 27, 2026](tenzir/v5-25-0.md)

  [This release adds periodic emission to the summarize operator, enabling real-time streaming analytics with configurable intervals and accumulation modes. It also introduces AWS IAM authentication across SQS, S3, and Kafka operators, and fixes memory instability in from\_http when used with slow do...](tenzir/v5-25-0.md)
* [ Tenzir Test v1.0.2 Jan 27, 2026](tenzir-test/v1-0-2.md)

  [This release improves the debugging experience by making the `--debug` flag automatically enable verbose output, so you see all test results when diagnosing failures.](tenzir-test/v1-0-2.md)
* [ Tenzir Platform v1.27.0 Jan 26, 2026](platform/v1-27-0.md)

  [This release improves the pipeline detail view with faster loading and a convenient close button for quick navigation. Error messages are now cleaner with collapsible technical details, and we fixed issues where the UI could hang or become unresponsive. This release also includes security hardeni...](platform/v1-27-0.md)
* [ Tenzir Ship v1.1.2 Jan 26, 2026](tenzir-ship/v1-1-2.md)

  [This release fixes bugs in changelog entry processing and version detection. The `authors` field now correctly normalizes single string values, and the `show` command no longer misidentifies entry IDs as release versions.](tenzir-ship/v1-1-2.md)
* [ Tenzir Test v1.0.1 Jan 23, 2026](tenzir-test/v1-0-1.md)

  [This release fixes an issue with diff tests failing when using multi-word Tenzir commands.](tenzir-test/v1-0-1.md)
* [ Tenzir Test v1.0.0 Jan 23, 2026](tenzir-test/v1-0-0.md)

  [This release introduces automatic binary detection with a clear precedence order: environment variables take priority, followed by PATH lookup, with `uvx` as fallback. Environment variables now support multi-part commands for full control over binary invocation. The `--tenzir-binary` and \`--tenzi...](tenzir-test/v1-0-0.md)
* [ Tenzir Test v0.15.0 Jan 23, 2026](tenzir-test/v0-15-0.md)

  [This release adds the `--verbose` flag for controlling test output verbosity. By default, only failures are shown, reducing noise in large test suites while still providing all details when needed.](tenzir-test/v0-15-0.md)
* [ Tenzir Ship v1.1.1 Jan 23, 2026](tenzir-ship/v1-1-1.md)

  [This release fixes two bugs: the multi-project `show` command now displays entries in consistent chronological order, and release recovery instructions show the actual branch name instead of a placeholder.](tenzir-ship/v1-1-1.md)
* [ Claude Marketplace v3.0.0 Jan 22, 2026](claude-plugins/v3-0-0.md)

  [This release consolidates several plugins into unified packages. The dev plugin now includes documentation, technical writing, git workflows, plan review, and auto-formatting. The tenzir plugin combines TQL and OCSF functionality.](claude-plugins/v3-0-0.md)

  [A new emoji reaction-based changelog workflow lets you approve, r...](claude-plugins/v3-0-0.md)
* [ Claude Marketplace > Dev Plugin v3.0.0 Jan 22, 2026](claude-plugins/dev/v3-0-0.md)

  [This release consolidates developer utilities into a unified plugin. The docs, prose, and ship plugins have merged into dev, providing changelog management, code review, and documentation workflows in one place.](claude-plugins/dev/v3-0-0.md)

  [The new `/dev:review` command spawns seven specialized reviewers in parallel to anal...](claude-plugins/dev/v3-0-0.md)
* [ Claude Marketplace > Python Plugin v1.1.1 Jan 22, 2026](claude-plugins/python/v1-1-1.md)

  [This release expands the Python conventions skill with guidance on default libraries (pydantic, FastAPI, Click), package structure best practices, and testing patterns with pytest.](claude-plugins/python/v1-1-1.md)
* [ Tenzir Ship v1.1.0 Jan 17, 2026](tenzir-ship/v1-1-0.md)

  [This release improves the user experience when `release publish` encounters failures mid-workflow. You now see a clear progress summary showing which steps completed, which step failed, and what remains pending—making recovery straightforward.](tenzir-ship/v1-1-0.md)
* [ Tenzir Node v5.24.0 Jan 16, 2026](tenzir/v5-24-0.md)

  [This release adds XML parsing functions (`parse_xml` and `parse_winlog`) for analyzing XML-formatted logs including Windows Event Logs. It also introduces the `parallel` operator for parallel pipeline execution, fixes a socket leak in `from_http` that could cause resource exhaustion, and includes...](tenzir/v5-24-0.md)
* [ Tenzir Test v0.14.0 Jan 15, 2026](tenzir-test/v0-14-0.md)

  [This release introduces inline test inputs for better test organization in deeply nested hierarchies. Tests can now place input data directly alongside test files, and you can create local `inputs/` directories at any level with automatic shadowing semantics.](tenzir-test/v0-14-0.md)
* [ Claude Marketplace > Dev Plugin v2.2.2 Jan 15, 2026](claude-plugins/dev/v2-2-2.md)

  [This release updates the docs plugin command scripts to use bun instead of pnpm, aligning with the Tenzir documentation site's package manager migration.](claude-plugins/dev/v2-2-2.md)
* [ Tenzir Ship v1.0.0 Jan 9, 2026](tenzir-ship/v1-0-0.md)

  [This major release renames the package from `tenzir-changelog` to `tenzir-ship` and introduces several breaking changes to streamline the CLI interface. The `show` command now uses intuitive positional tokens (`unreleased`, `released`, `latest`, `all`) instead of flags, and the `release notes` co...](tenzir-ship/v1-0-0.md)
* [ Claude Marketplace v2.0.0 Jan 9, 2026](claude-plugins/v2-0-0.md)

  [This major release renames the `changelog` plugin to `ship` to better reflect its focus on release engineering. Subagents now require explicit skill declarations in their YAML frontmatter, and tool configurations have been updated to use the consolidated `Skill` tool.](claude-plugins/v2-0-0.md)
* [ Claude Marketplace > Dev Plugin v2.2.1 Jan 8, 2026](claude-plugins/dev/v2-2-1.md)

  [This release fixes two bugs in the documentation reader subagent. The reader now reports all examples from operator and function pages instead of only the first one, and only reports verbatim examples from the documentation instead of synthesizing potentially incorrect code.](claude-plugins/dev/v2-2-1.md)
* [ Claude Marketplace > Excalidraw Plugin v0.1.1 Jan 8, 2026](claude-plugins/excalidraw/v0-1-1.md)

  [This release improves the accuracy and reliability of Excalidraw diagram generation through better documentation and corrected defaults. It fixes several bugs related to polygon path closing, text positioning formulas, and roughness settings, while also enhancing documentation to clarify technica...](claude-plugins/excalidraw/v0-1-1.md)
* [ Tenzir Ship v0.19.1 Jan 4, 2026](tenzir-ship/v0-19-1.md)

  [This release adds initial release support with implicit version bumping and fixes row numbering in multi-project views.](tenzir-ship/v0-19-1.md)
* [ Claude Marketplace v1.1.0 Jan 4, 2026](claude-plugins/v1-1-0.md)

  [This release introduces the OCSF plugin for navigating the Open Cybersecurity Schema Framework with versioned reference documentation, and the Excalidraw plugin for generating valid diagrams. It also adds a reusable GitHub Action for automated changelog entries in CI.](claude-plugins/v1-1-0.md)

  [Breaking changes include re...](claude-plugins/v1-1-0.md)
* [ Claude Marketplace > Dev Plugin v2.2.0 Jan 4, 2026](claude-plugins/dev/v2-2-0.md)

  [This release restores the `/docs:pr` command with enhanced cross-referencing capabilities that automatically link documentation PRs with parent project PRs. It also improves the synchronization workflow by automatically cloning the documentation repository when needed, eliminating manual setup st...](claude-plugins/dev/v2-2-0.md)
* [ Claude Marketplace > Excalidraw Plugin v0.1.0 Jan 4, 2026](claude-plugins/excalidraw/v0-1-0.md)

  [Initial release of the Excalidraw plugin for generating valid diagram files. The plugin supports flowcharts, ER diagrams, sequence diagrams, and architecture diagrams with proper element bindings and Excalidraw-native styling.](claude-plugins/excalidraw/v0-1-0.md)
* [ Tenzir Node v5.23.1 Jan 2, 2026](tenzir/v5-23-1.md)

  [This release fixes internal errors in expression evaluation for heterogeneous data, resolves a crash in the operator when using , and ensures the connector shuts down gracefully.](tenzir/v5-23-1.md)
* [ Tenzir Ship v0.19.0 Dec 30, 2025](tenzir-ship/v0-19-0.md)

  [This release adds configuration options to disable automatic PR and author detection, giving projects more control over changelog entry metadata.](tenzir-ship/v0-19-0.md)
* [ Claude Marketplace > Dev Plugin v2.1.0 Dec 28, 2025](claude-plugins/dev/v2-1-0.md)

  [This release adds a documentation reader subagent that answers questions about Tenzir by navigating the live documentation at docs.tenzir.com. It also makes the docs:writer subagent fully autonomous by handling PR creation directly from within the .docs/ repository.](claude-plugins/dev/v2-1-0.md)
* [ Claude Marketplace > Dev Plugin v2.0.0 Dec 28, 2025](claude-plugins/dev/v2-0-0.md)

  [This major release renames the `docs:writing` skill to `docs:authoring` to better reflect its comprehensive scope beyond prose writing. It also introduces an intelligent documentation sync hook that automatically keeps the `.docs/` repository synchronized while preventing conflicts.](claude-plugins/dev/v2-0-0.md)
* [ Tenzir Ship v0.18.2 Dec 24, 2025](tenzir-ship/v0-18-2.md)

  [This release adds persistent configuration support for explicit link formatting, allowing projects to set a default link rendering style in `config.yaml` that applies across all commands.](tenzir-ship/v0-18-2.md)
* [ Tenzir Ship v0.18.1 Dec 24, 2025](tenzir-ship/v0-18-1.md)

  [This release adds explicit Markdown link conversion for GitHub references, enabling better compatibility with external documentation sites and Markdown renderers that don't automatically link @mentions and #PR references.](tenzir-ship/v0-18-1.md)
* [ Tenzir Node v5.23.0 Dec 23, 2025](tenzir/v5-23-0.md)

  [This release introduces centralized node-level TLS configuration, allowing you to configure TLS settings once in tenzir.yaml instead of passing options to each operator individually. It also adds support for event-timestamp-based compaction rules and a count field in the deduplicate operator.](tenzir/v5-23-0.md)
* [ Tenzir Platform v1.26.0 Dec 23, 2025](platform/v1-26-0.md)

  [This release adds HashiCorp Vault as an external secret store for workspaces. The integration supports token and AppRole authentication with the KV v2 secrets engine.](platform/v1-26-0.md)
* [ Claude Marketplace > Python Plugin v1.1.0 Dec 23, 2025](claude-plugins/python/v1-1-0.md)

  [This release adds Pyright language server integration for enhanced Python development capabilities. The LSP configuration provides go-to-definition, find-references, hover information, and diagnostics for Python files.](claude-plugins/python/v1-1-0.md)
* [ Claude Marketplace > Dev Plugin v1.1.1 Dec 22, 2025](claude-plugins/dev/v1-1-1.md)

  [This release ensures the `/docs:write` command works with up-to-date documentation by synchronizing the `.docs/` clone with the latest changes from `main` before writing.](claude-plugins/dev/v1-1-1.md)
* [ Tenzir Node v5.22.2 Dec 21, 2025](tenzir/v5-22-2.md)

  [This release fixes a performance regression when parsing lists with mixed-type elements, where batch processing was inadvertently broken. It also resolves an assertion failure that could crash Tenzir when encountering events with duplicate keys.](tenzir/v5-22-2.md)
* [ Tenzir Ship v0.18.0 Dec 21, 2025](tenzir-ship/v0-18-0.md)

  [This release introduces a version-agnostic release workflow that simplifies publishing and CI integration, allowing commands to default to the latest release version. It also improves changelog browsing by sorting module entries chronologically rather than grouping them by project.](tenzir-ship/v0-18-0.md)
* [ Tenzir Ship v0.17.2 Dec 21, 2025](tenzir-ship/v0-17-2.md)
* [ Tenzir Ship v0.17.1 Dec 21, 2025](tenzir-ship/v0-17-1.md)

  [This release fixes a critical bug where status messages were written to stdout instead of stderr, breaking GitHub workflows and scripts that capture version output from commands like `release create`.](tenzir-ship/v0-17-1.md)
* [ Tenzir MCP Server v0.4.5 Dec 19, 2025](mcp/v0-4-5.md)

  [This release updates the embedded OCSF schemas and Tenzir documentation to their latest versions, ensuring AI agents have access to the most current reference material.](mcp/v0-4-5.md)
* [ Tenzir Ship v0.17.0 Dec 19, 2025](tenzir-ship/v0-17-0.md)

  [This release enhances shell scripting capabilities by making `release create` output the version to stdout. All Rich UI elements now go to stderr, enabling clean machine-readable results for automation workflows.](tenzir-ship/v0-17-0.md)
* [ Tenzir Ship v0.16.0 Dec 19, 2025](tenzir-ship/v0-16-0.md)

  [This release introduces aggregated module changelog summaries in release notes, allowing parent projects to automatically include a summary of changes from their modules. It also fixes a minor issue with redundant version fields in JSON output.](tenzir-ship/v0-16-0.md)
* [ Claude Marketplace v1.0.0 Dec 19, 2025](claude-plugins/v1-0-0.md)

  [This is the first stable release of the Tenzir Claude Marketplace, a collection of plugins that extend Claude Code's capabilities for working with the Tenzir ecosystem.](claude-plugins/v1-0-0.md)

  [This release introduces fully qualified skill names across all plugins for clarity and consistency. The `writing` plugin has be...](claude-plugins/v1-0-0.md)
* [ Claude Marketplace > Dev Plugin v1.1.0 Dec 19, 2025](claude-plugins/dev/v1-1-0.md)

  [This release introduces autonomous documentation workflows with the new `/docs:review` command and `docs:writer` subagent. The plugin now uses `.docs` as the unconditional documentation root and streamlines command naming by renaming `/docs:write-docs` to `/docs:write`.](claude-plugins/dev/v1-1-0.md)
* [ Tenzir Node v5.22.1 Dec 18, 2025](tenzir/v5-22-1.md)

  [This release fixes a bug where the `publish` operator could drop events.](tenzir/v5-22-1.md)
* [ Tenzir Ship v0.15.0 Dec 18, 2025](tenzir-ship/v0-15-0.md)

  [This release adds new options to the `release publish` command for more flexible release automation. You can now prevent GitHub from marking a release as latest with `--no-latest` (useful for backport releases), and automatically commit staged changes before tagging with `--commit`.](tenzir-ship/v0-15-0.md)
* [ Tenzir Ship v0.14.0 Dec 17, 2025](tenzir-ship/v0-14-0.md)

  [This release adds H1 headings to release notes output, making documents more structured and easier to navigate.](tenzir-ship/v0-14-0.md)
* [ Tenzir Node v5.22.0 Dec 16, 2025](tenzir/v5-22-0.md)

  [This release introduces support for arguments in user-defined operators, letting operators declare positional and named parameters with optional default values and use them just like built-in operators. It also enhances parser behavior for duplicate keys and includes several important stability, ...](tenzir/v5-22-0.md)
* [ Tenzir Platform v1.25.1 Dec 16, 2025](platform/v1-25-1.md)

  [This patch release fixes an issue with default filesystem paths in the Tenzir Platform docker containers for Sovereign Edition users.](platform/v1-25-1.md)
* [ Tenzir Ship v0.13.1 Dec 16, 2025](tenzir-ship/v0-13-1.md)

  [This release streamlines module mode by removing the multi-project feature in favor of the dedicated `modules` configuration. It removes the `--include-modules` flag (modules are now always included when configured) and enhances module mode to show released entries with version numbers. The relea...](tenzir-ship/v0-13-1.md)
* [ Tenzir Ship v0.13.0 Dec 16, 2025](tenzir-ship/v0-13-0.md)

  [This release streamlines module mode by removing the multi-project feature in favor of the dedicated `modules` configuration. It removes the `--include-modules` flag (modules are now always included when configured) and enhances module mode to show released entries with version numbers. The relea...](tenzir-ship/v0-13-0.md)
* [ Tree-sitter TQL v1.0.0 Dec 16, 2025](tree-sitter-tql/v1-0-0.md)

  [This release marks the first stable version of the Tree-sitter TQL grammar. It adds prebuilt native binaries and npm publishing with OIDC provenance, eliminating compilation for most users.](tree-sitter-tql/v1-0-0.md)
* [ Tenzir Platform v1.25.0 Dec 15, 2025](platform/v1-25-0.md)

  [This release includes some UI fixes and minor improvements to smooth out common workflows. We fixed incorrect rendering of negative durations, resolved an issue where the node selector reset during navigation, and addressed a layout issue that could hide the install button in the package drawer.](platform/v1-25-0.md)
* [ Tenzir Ship v0.12.0 Dec 15, 2025](tenzir-ship/v0-12-0.md)

  [This release adds support for nested changelog projects through modules, improves export formats with structured URL fields in JSON, and enhances the CLI with better export options and configuration flexibility for components.](tenzir-ship/v0-12-0.md)
* [ Claude Marketplace > Brand Plugin v1.0.0 Dec 15, 2025](claude-plugins/brand/v1-0-0.md)

  [This is the initial major release of the brand plugin, providing comprehensive Tenzir design system specifications for frontend development. The plugin includes design tokens for colors, typography, spacing, and shadows, along with detailed component specifications for 10+ UI elements. It feature...](claude-plugins/brand/v1-0-0.md)
* [ Claude Marketplace > Dev Plugin v1.0.0 Dec 15, 2025](claude-plugins/dev/v1-0-0.md)

  [This is the first stable release of the docs plugin. It introduces a streamlined workflow with dedicated commands for documentation management, replacing the previous agent-based approach. The plugin now features intelligent path detection, SSH-based repository cloning, and a simplified directory...](claude-plugins/dev/v1-0-0.md)
* [ Claude Marketplace > Python Plugin v1.0.0 Dec 15, 2025](claude-plugins/python/v1-0-0.md)

  [This major release standardizes skill naming with `python:following-conventions` and replaces the plugin-specific release command with the generic `/changelog:release` command. It also adds a dependency upgrade guide for Python projects.](claude-plugins/python/v1-0-0.md)
* [ Tenzir MCP Server v0.4.4 Dec 12, 2025](mcp/v0-4-4.md)

  [This release fixes broken CI/CD workflows that were preventing successful publishing to PyPI. The workflows have been refactored with reusable composite actions and proper version verification after publishing.](mcp/v0-4-4.md)
* [ Tenzir MCP Server v0.4.3 Dec 12, 2025](mcp/v0-4-3.md)

  [This patch release updates the server to use FastMCP's built-in logging infrastructure. The custom file-based logging has been removed, eliminating the creation of `tenzir-mcp.log` files in the working directory. Use `FASTMCP_LOG_LEVEL=DEBUG` for verbose output when troubleshooting.](mcp/v0-4-3.md)
* [ Tenzir Ship v0.11.1 Dec 11, 2025](tenzir-ship/v0-11-1.md)

  [This patch release improves the CLI display with better card view styling and author formatting. The card view now displays type-colored borders and properly formats non-GitHub authors without the @ prefix for improved readability.](tenzir-ship/v0-11-1.md)
* [ Tenzir Platform v1.24.0 Dec 10, 2025](platform/v1-24-0.md)

  [This release includes many small UI fixes, as well as new TLS options for the websocket gateway.](platform/v1-24-0.md)
* [ Tenzir MCP Server v0.4.2 Dec 9, 2025](mcp/v0-4-2.md)

  [This release streamlines the prompts for the `make_parser` and `make_ocsf_mapping` tools, reducing model errors and speeding up agent completion.](mcp/v0-4-2.md)
* [ Claude Marketplace > Dev Plugin v0.1.0 Dec 9, 2025](claude-plugins/dev/v0-1-0.md)

  [Initial release of the docs plugin.](claude-plugins/dev/v0-1-0.md)
* [ Tenzir Test v0.13.1 Dec 8, 2025](tenzir-test/v0-13-1.md)

  [This release fixes path handling in the diff runner to strip root path prefixes from output, making paths relative and consistent with other test runners.](tenzir-test/v0-13-1.md)
* [ Claude Marketplace > Brand Plugin v0.1.0 Dec 8, 2025](claude-plugins/brand/v0-1-0.md)

  [Initial release of the brand plugin.](claude-plugins/brand/v0-1-0.md)
* [ Tenzir Ship v0.11.0 Dec 5, 2025](tenzir-ship/v0-11-0.md)

  [This release adds the `--co-author` option for crediting additional authors (useful for AI-assisted development) and improves entry parsing to accept the plural `components` key in frontmatter.](tenzir-ship/v0-11-0.md)
* [ Tenzir Ship v0.10.0 Dec 4, 2025](tenzir-ship/v0-10-0.md)

  [This release adds support for reading changelog entry descriptions from files or stdin, making it easier to integrate with automated workflows and pipelines.](tenzir-ship/v0-10-0.md)
* [ Claude Marketplace > Python Plugin v0.1.0 Dec 4, 2025](claude-plugins/python/v0-1-0.md)

  [Initial release of the python plugin.](claude-plugins/python/v0-1-0.md)
* [ Tenzir Test v0.13.0 Dec 3, 2025](tenzir-test/v0-13-0.md)

  [This release adds `--package-dirs` support and improves startup diagnostics.](tenzir-test/v0-13-0.md)
* [ Tenzir Ship v0.9.1 Dec 3, 2025](tenzir-ship/v0-9-1.md)
* [ Tenzir Ship v0.9.0 Dec 3, 2025](tenzir-ship/v0-9-0.md)
* [ Tenzir Node v5.21.2 Nov 28, 2025](tenzir/v5-21-2.md)

  [This is a bugfix release that fixes timestamp handling in the python operator and the backpressure handling in publish and subscribe.](tenzir/v5-21-2.md)
* [ Tenzir Node v5.20.2 Nov 25, 2025](tenzir/v5-20-2.md)

  [This release backports the changes made in v5.21.1 to v5.20.1.](tenzir/v5-20-2.md)
* [ Tenzir Node v5.21.1 Nov 24, 2025](tenzir/v5-21-1.md)

  [This release features new and improved hash functions as well as a couple of bugfixes.](tenzir/v5-21-1.md)
* [ Tenzir Platform v1.23.1 Nov 24, 2025](platform/v1-23-1.md)

  [We fixed an issue where dashboard cells without a fixed node ID sometimes failed to render. These cells now render correctly using sensible fallbacks.](platform/v1-23-1.md)
* [ Tenzir Platform v1.23.0 Nov 20, 2025](platform/v1-23-0.md)

  [The seaweedfs service in our example setups now runs as non-root user and automatically adds the correct CORS headers. Be sure to read the "Changes" section below if you're using it in a self-hosted environment. As always, a slew of frontend improvements are included in this release as well.](platform/v1-23-0.md)
* [ Tenzir Node v5.21.0 Nov 19, 2025](tenzir/v5-21-0.md)

  [This release improves the stability of pipelines by applying backpressure more effectively, ensuring upstream components slow down before overwhelming subscribers. It also enhances daily operations by improving parquet reliability, adding Base58 support, and extending the built-in OCSF operators ...](tenzir/v5-21-0.md)
* [ Tenzir Node v5.20.1 Nov 13, 2025](tenzir/v5-20-1.md)

  [This patch release comes with a few new experimental memory metrics. Furthermore, it resolves an issue where the memory usage would grow without bounds on some systems.](tenzir/v5-20-1.md)
* [ Tenzir Platform v1.22.0 Nov 13, 2025](platform/v1-22-0.md)

  [This release includes a variety of UI improvements and bugfixes, as well as a new configuration option for working with external OIDC providers.](platform/v1-22-0.md)
* [ Tenzir MCP Server v0.4.1 Nov 13, 2025](mcp/v0-4-1.md)
* [ Tenzir MCP Server v0.4.0 Nov 10, 2025](mcp/v0-4-0.md)
* [ Tenzir Ship v0.8.1 Nov 10, 2025](tenzir-ship/v0-8-1.md)

  [Patch release to stabilize GitHub context inference tests.](tenzir-ship/v0-8-1.md)
* [ Tenzir Ship v0.8.0 Nov 10, 2025](tenzir-ship/v0-8-0.md)

  [Infer GitHub context for entries, keep the Python API non-interactive, and showcase components in the dogfooded project.](tenzir-ship/v0-8-0.md)
* [ Tenzir Ship v0.7.0 Nov 9, 2025](tenzir-ship/v0-7-0.md)

  [Expose the CLI as a Python API.](tenzir-ship/v0-7-0.md)
* [ Tenzir Test v0.12.0 Nov 5, 2025](tenzir-test/v0-12-0.md)

  [Minor release with improved NO\_COLOR handling.](tenzir-test/v0-12-0.md)
* [ Tenzir Test v0.11.0 Nov 4, 2025](tenzir-test/v0-11-0.md)

  [Expose tenzir-test as a reusable Python library.](tenzir-test/v0-11-0.md)
* [ Tenzir Node v5.20.0 Nov 3, 2025](tenzir/v5-20-0.md)

  [We continue our quest for better memory usage by switching out the memory allocator to the battle-tested `mimalloc`, as well as adding metrics collecting for memory usage.](tenzir/v5-20-0.md)
* [ Tenzir Platform v1.21.0 Nov 3, 2025](platform/v1-21-0.md)

  [This release improves how you browse, edit, and share pipelines. We fixed overlapping timestamps in the activity chart, made pipeline updates more reliable and visible, sped up library loading, and added a new button in the editor to copy a link to the current pipeline.](platform/v1-21-0.md)
* [ Tenzir Ship v0.6.0 Nov 2, 2025](tenzir-ship/v0-6-0.md)

  [Refine release manifest format: rename 'description' to 'intro' and render it with a folded YAML block for better readability.](tenzir-ship/v0-6-0.md)
* [ Tenzir Ship v0.5.0 Nov 2, 2025](tenzir-ship/v0-5-0.md)

  [This release adds support for multi-project operations and package-aware discovery.](tenzir-ship/v0-5-0.md)
* [ Tenzir Node v5.19.0 Oct 27, 2025](tenzir/v5-19-0.md)

  [This release introduces the `ocsf::cast` operator to streamline schema transformations for OCSF events and adds support for one-level recursion in OCSF objects, enabling recursive relations such as `process.parent_process` and `analytic.related_analytics`.](tenzir/v5-19-0.md)
* [ Tenzir Ship v0.4.1 Oct 27, 2025](tenzir-ship/v0-4-1.md)

  [This release improves GitHub release note formatting.](tenzir-ship/v0-4-1.md)
* [ Tenzir Ship v0.4.0 Oct 27, 2025](tenzir-ship/v0-4-0.md)

  [This release adds components to entries, supports tagging during publish, and polishes release creation output while inverting the show table order.](tenzir-ship/v0-4-0.md)
* [ Tenzir Ship v0.3.0 Oct 24, 2025](tenzir-ship/v0-3-0.md)

  [This release refines the workflow and exports, introduces numeric entry prefixes and emoji-styled types, and improves table layout and PR metadata.](tenzir-ship/v0-3-0.md)
* [ Tenzir Platform v1.20.0 Oct 22, 2025](platform/v1-20-0.md)

  [This release introduces keyboard shortcut indicators for buttons, ensures consistent blob rendering, shows UDOs in the package info, and includes fixes for big number rendering and history position.](platform/v1-20-0.md)
* [ Tenzir Ship v0.2.0 Oct 21, 2025](tenzir-ship/v0-2-0.md)

  [This release improves table and export layouts, simplifies configuration, and streamlines the release archive while fixing logging and ordering.](tenzir-ship/v0-2-0.md)
* [ Tenzir Ship v0.1.0 Oct 21, 2025](tenzir-ship/v0-1-0.md)

  [This initial version introduces the inaugural `tenzir-changelog` CLI, covering project bootstrapping, entry capture, rich browsing, release assembly, documentation, and validation tooling.](tenzir-ship/v0-1-0.md)
* [ Tenzir Node v5.18.0 Oct 20, 2025](tenzir/v5-18-0.md)

  [This release focuses on improving performance and memory usage. Pipelines are now faster, especially when using if conditions or parsing highly heterogeneous events. Memory usage has also been substantially reduced.](tenzir/v5-18-0.md)
* [ Tenzir Node v5.17.0 Oct 13, 2025](tenzir/v5-17-0.md)

  [This release introduces user-defined operators in packages, allowing you to extend Tenzir with custom operators defined in TQL files. It also adds list manipulation functions, a recursive search function, and improved memory management.](tenzir/v5-17-0.md)
* [ Tenzir Platform v1.19.1 Oct 13, 2025](platform/v1-19-1.md)

  [This release fixes several bugs in the Tenzir Platform; from the Secret Store API to the way ephemeral node tokens are generated.](platform/v1-19-1.md)
* [ Tenzir Platform v1.19.0 Sep 30, 2025](platform/v1-19-0.md)

  [This release adds a new detail page, as well as many UI fixes and improvements.](platform/v1-19-0.md)
* [ Tenzir Node v5.16.0 Sep 26, 2025](tenzir/v5-16-0.md)

  [This release brings forth stability improvements under high load that could cause platform unresponsiveness, fixes API request isolation problems, better kafka diagnostics and more.](tenzir/v5-16-0.md)
* [ Tenzir Node v5.15.0 Sep 19, 2025](tenzir/v5-15-0.md)

  [This release enhances TQL's data transformation capabilities with lambda expressions that can capture surrounding fields in `map` and `where` functions, plus grouped enumeration for separate event counting. We've also improved operator composability with enhanced `to_splunk` parameters, added oct...](tenzir/v5-15-0.md)
* [ Tenzir Node v5.14.0 Sep 11, 2025](tenzir/v5-14-0.md)

  [This release introduces an integration fo SentinelOne Singularity™ Data Lake and a new message based `to_kafka` operator that features a one to one event to message relation.](tenzir/v5-14-0.md)
* [ Tenzir Platform v1.18.0 Sep 2, 2025](platform/v1-18-0.md)

  [With this release of the Tenzir Platform, we reorganized the UI to make the most important pages more accessible.](platform/v1-18-0.md)
* [ Tenzir Node v5.13.2 Sep 1, 2025](tenzir/v5-13-2.md)

  [This release adds a new S3 operator and fixes a bug within the `fork` operator.](tenzir/v5-13-2.md)
* [ Tenzir Node v5.13.1 Aug 28, 2025](tenzir/v5-13-1.md)

  [This release adds a new Azure Blob Storage operator with account key authentication and improves Google Security Operations retry handling. It also contains various small fixes and improvements.](tenzir/v5-13-1.md)
* [ Tenzir Platform v1.17.4 Aug 28, 2025](platform/v1-17-4.md)

  [This patch release contains no public-facing bug-fixes or features.](platform/v1-17-4.md)
* [ Tenzir Node v5.13.0 Aug 20, 2025](tenzir/v5-13-0.md)

  [This release enhances UDP ingestion with the new `from_udp` operator that produces structured events with sender metadata. We also improved the execution model for `every` and `cron` subpipelines, added DNS lookup capabilities, and made the Syslog parser more flexible.](tenzir/v5-13-0.md)
* [ Tenzir Platform v1.17.3 Aug 7, 2025](platform/v1-17-3.md)

  [This bugfix release fixes an issue where the Tenzir Platform would generate download URLs with an incorrect signature.](platform/v1-17-3.md)
* [ Tenzir Node v5.12.1 Aug 6, 2025](tenzir/v5-12-1.md)

  [We fixed two bugs in the `to_google_secops` and `to_amazon_security_lake` operators.](tenzir/v5-12-1.md)
* [ Tenzir Platform v1.17.2 Aug 6, 2025](platform/v1-17-2.md)

  [You can now select parts of a pipeline from the history pane without closing it and the bottom bar in charts does not overlap with the contant any more.](platform/v1-17-2.md)
* [ Tenzir Node v5.12.0 Aug 4, 2025](tenzir/v5-12-0.md)

  [This release adds support for OCSF 1.6.0 and introduces the `replace` operator.](tenzir/v5-12-0.md)
* [ Tenzir Platform v1.17.1 Aug 4, 2025](platform/v1-17-1.md)

  [The app now renders durations of length `0` correctly in the detailed event view.](platform/v1-17-1.md)
* [ Tenzir Node v5.11.1 Aug 1, 2025](tenzir/v5-11-1.md)

  [This release introduces payload compression for Azure Log Analytics to reduce bandwidth usage, as well as an important fix for a `from_http` bug that was introduced with the previous release.](tenzir/v5-11-1.md)
* [ Tenzir Node v5.11.0 Aug 1, 2025](tenzir/v5-11-0.md)

  [This release delivers significant performance improvements for situations with many concurrent pipelines, making Tenzir more robust under high-load scenarios. New features include AWS role assumption support, enhanced string trimming functionality, and improved HTTP error handling capabilities. A...](tenzir/v5-11-0.md)
* [ Tenzir Platform v1.17.0 Jul 30, 2025](platform/v1-17-0.md)

  [This release fixes the display of example pipelines in packages.](platform/v1-17-0.md)
* [ Tenzir Node v5.10.0 Jul 22, 2025](tenzir/v5-10-0.md)

  [This release introduces two new powerful OCSF operators that automate enum derivation and provide intelligent field trimming. The update also includes string padding functions, better HTTP requests, IP categorization and much more!](tenzir/v5-10-0.md)
* [ Tenzir Platform v1.16.1 Jul 18, 2025](platform/v1-16-1.md)

  [This release fixes two issues in the Tenzir UI that were found since the last release.](platform/v1-16-1.md)
* [ Tenzir Platform v1.16.0 Jul 16, 2025](platform/v1-16-0.md)

  [This release adds two mechanism for a better diagnostics experience. Diagnostics are now shown directly in the editor. Additionally, the diagnostics heatmap in the pipeline overview can now be interacted with.](platform/v1-16-0.md)
* [ Tenzir Platform v1.15.0 Jul 9, 2025](platform/v1-15-0.md)

  [This release adds support for reading externally-supplied JWT tokens from a header, instead of manually clicking on the *Log In* button.](platform/v1-15-0.md)
* [ Tenzir Node v5.9.0 Jul 6, 2025](tenzir/v5-9-0.md)

  [This release brings a family of UUID functions to TQL, making it easier to generate random numbers for a variety of use cases.](tenzir/v5-9-0.md)
* [ Tenzir Platform v1.14.1 Jul 4, 2025](platform/v1-14-1.md)

  [We resolved an issue where some rows in the pipelines table were being cut off. The table now scrolls properly when there are many entries.](platform/v1-14-1.md)
* [ Tenzir Node v5.8.0 Jul 3, 2025](tenzir/v5-8-0.md)

  [This release introduces format and compression inference from URLs for HTTP data sources, streamlining data loading workflows. It also includes bug fixes for secret resolution and HTTP server mode.](tenzir/v5-8-0.md)
* [ Tenzir Node v5.7.0 Jul 1, 2025](tenzir/v5-7-0.md)

  [Tenzir Node v5.7.0 introduces a new secret type that keeps its sensitive content hidden while enabling flexible secret retrieval. This release also adds support for OCSF extensions and brings several improvements to the operator.](tenzir/v5-7-0.md)
* [ Tenzir Platform v1.14.0 Jul 1, 2025](platform/v1-14-0.md)

  [This release adds CLI support for adding, removing and updating secrets. It also adds a new three-dot menu on the pipelines page, as well as partial pipeline execution from the history.](platform/v1-14-0.md)
* [ Tenzir Platform v1.13.0 Jun 26, 2025](platform/v1-13-0.md)

  [This release contains improved integration for running the Tenzir Platform inside GCP, a new Schema Search functionality, and an option for showing the total diagnostic count in heatmap cells.](platform/v1-13-0.md)
* [ Tenzir Node v5.6.1 Jun 24, 2025](tenzir/v5-6-1.md)

  [This release restores an aggregation function that was accidentally made unavailable in Tenzir Node v5.6.0.](tenzir/v5-6-1.md)
* [ Tenzir Node v5.6.0 Jun 24, 2025](tenzir/v5-6-0.md)

  [The operator now supports event-dependent topics, making routing between pipelines more flexible. Additionally, new and operators make taking apart custom logs easier than before.](tenzir/v5-6-0.md)
* [ Tenzir Node v5.5.0 Jun 18, 2025](tenzir/v5-5-0.md)

  [Built-in support for normalizing OCSF events to their upstream schema makes normalizations easier than ever with Tenzir Node v5.5.](tenzir/v5-5-0.md)
* [ Tenzir Platform v1.12.0 Jun 18, 2025](platform/v1-12-0.md)

  [Tenzir Platform v1.12 introduces an action bar at the bottom of the Explorer, providing easier access to view settings. Additionally, the widget row on the nodes page has been enhanced with numerous improvements and bug fixes.](platform/v1-12-0.md)
* [ Tenzir Node v5.4.1 Jun 13, 2025](tenzir/v5-4-1.md)

  [This release fixes a bug within the JSON printer that could lead to invalid JSON being produced, and also led to response timeouts when using the Tenzir Platform.](tenzir/v5-4-1.md)
* [ Tenzir Node v5.4.0 Jun 12, 2025](tenzir/v5-4-0.md)

  [With the introduction of format strings to TQL, this release makes string construction from multiple parts easier than ever before.](tenzir/v5-4-0.md)
* [ Tenzir Node v5.3.4 Jun 10, 2025](tenzir/v5-3-4.md)

  [This release fixes a bug that caused package installation outside of the Tenzir Library to fail, which caused Demo Nodes in the Tenzir Platform to not have any packages installed.](tenzir/v5-3-4.md)
* [ Tenzir Platform v1.11.1 Jun 10, 2025](platform/v1-11-1.md)

  [The all-new pipeline widgets make it easy to see at a glance which the total ingress and egress of all pipelines, and to easily figure out which pipelines had warnings and errors.](platform/v1-11-1.md)
* [ Tenzir Node v5.3.3 Jun 6, 2025](tenzir/v5-3-3.md)

  [The from\_http and http operators now support response sizes upto 2GiB](tenzir/v5-3-3.md)
* [ Tenzir Node v5.3.2 Jun 3, 2025](tenzir/v5-3-2.md)

  [Tenzir Node v5.3.1 updated the pyproject version but did not actually commit it, causing the Python operator to fail to start. This release fixes the issue.](tenzir/v5-3-2.md)
* [ Tenzir Node v5.3.0 Jun 3, 2025](tenzir/v5-3-0.md)

  [This release brings forth improvements to HTTP support in Tenzir, supporting requests as transformations and paginating APIs.](tenzir/v5-3-0.md)
* [ Tenzir Platform v1.10.4 Jun 2, 2025](platform/v1-10-4.md)

  [This release adds a custom icon for ephemeral nodes, making them easier to distinguish from regular ones.](platform/v1-10-4.md)
* [ Tenzir Platform v1.10.3 Jun 1, 2025](platform/v1-10-3.md)

  [As of this release, there is a detailed changelog for the Tenzir Platform on the revamped docs.tenzir.com.](platform/v1-10-3.md)
* [ Tenzir Node v5.2.0 May 23, 2025](tenzir/v5-2-0.md)
* [ Tenzir Platform v1.10.2 May 21, 2025](platform/v1-10-2.md)

  [This patch release contains a number of additional bugfixes since Tenzir Platform v1.10.1:](platform/v1-10-2.md)
* [ Tenzir Node v5.1.8 May 20, 2025](tenzir/v5-1-8.md)
* [ Tenzir Platform v1.10.1 May 20, 2025](platform/v1-10-1.md)

  [This patch release fixes a number of issues found since the release of Tenzir Platform v1.10:](platform/v1-10-1.md)
* [ Tenzir Node v5.1.7 May 19, 2025](tenzir/v5-1-7.md)
* [ Tenzir Platform v1.10.0 May 16, 2025](platform/v1-10-0.md)

  [This release restructures the page layout for better usability and adds the ability to statically define workspaces in on-prem environments.](platform/v1-10-0.md)
* [ Tenzir Node v5.1.6 May 15, 2025](tenzir/v5-1-6.md)
* [ Tenzir Node v5.1.5 May 12, 2025](tenzir/v5-1-5.md)
* [ Tenzir Node v5.1.4 May 8, 2025](tenzir/v5-1-4.md)
* [ Tenzir Node v5.1.3 May 5, 2025](tenzir/v5-1-3.md)
* [ Tenzir Node v5.1.2 Apr 30, 2025](tenzir/v5-1-2.md)
* [ Tenzir Node v5.1.1 Apr 28, 2025](tenzir/v5-1-1.md)
* [ Tenzir Node v5.1.0 Apr 25, 2025](tenzir/v5-1-0.md)
* [ Tenzir Node v5.0.1 Apr 22, 2025](tenzir/v5-0-1.md)
* [ Tenzir Node v5.0.0 Apr 17, 2025](tenzir/v5-0-0.md)
* [ Tenzir Platform v1.9.7 Apr 17, 2025](platform/v1-9-7.md)

  [This patch release comes with a number of frontend improvements since Tenzir Platform v1.9.6:](platform/v1-9-7.md)
* [ Tenzir Platform v1.9.6 Apr 14, 2025](platform/v1-9-6.md)

  [This patch release includes the following improvements over Tenzir Platform v1.9.5:](platform/v1-9-6.md)
* [ Tenzir Platform v1.9.5 Apr 11, 2025](platform/v1-9-5.md)

  [This patch release includes the following improvements over Tenzir Platform v1.9.4:](platform/v1-9-5.md)
* [ Tenzir Node v4.32.1 Apr 8, 2025](tenzir/v4-32-1.md)
* [ Tenzir Node v4.32.0 Apr 4, 2025](tenzir/v4-32-0.md)
* [ Tenzir Platform v1.9.4 Apr 3, 2025](platform/v1-9-4.md)

  [This patch release includes the following improvements over Tenzir Platform v1.9.3:](platform/v1-9-4.md)
* [ Tenzir Platform v1.9.3 Apr 2, 2025](platform/v1-9-3.md)

  [This patch release includes the following bug fixes over Tenzir Platform v1.9.2:](platform/v1-9-3.md)
* [ Tenzir Node v4.31.2 Apr 1, 2025](tenzir/v4-31-2.md)
* [ Tenzir Node v4.31.0 Mar 31, 2025](tenzir/v4-31-0.md)
* [ Tenzir Node v4.30.3 Mar 25, 2025](tenzir/v4-30-3.md)
* [ Tenzir Node v4.30.2 Mar 22, 2025](tenzir/v4-30-2.md)
* [ Tenzir Node v4.30.1 Mar 20, 2025](tenzir/v4-30-1.md)
* [ Tenzir Node v4.30.0 Mar 18, 2025](tenzir/v4-30-0.md)
* [ Tenzir Platform v1.9.2 Mar 18, 2025](platform/v1-9-2.md)

  [This patch release includes the following bug fixes over Tenzir Platform v1.9.1:](platform/v1-9-2.md)
* [ Tenzir Platform v1.9.1 Mar 17, 2025](platform/v1-9-1.md)

  [This patch release includes the following bug fixes over Tenzir Platform v1.9.0, all of them geared towards Sovereign Edition users:](platform/v1-9-1.md)
* [ Tenzir Platform v1.9.0 Mar 14, 2025](platform/v1-9-0.md)

  [This release revamps the Explorer to better support large datasets.](platform/v1-9-0.md)
* [ Tenzir Node v4.29.2 Mar 11, 2025](tenzir/v4-29-2.md)
* [ Tenzir Platform v1.8.5 Mar 7, 2025](platform/v1-8-5.md)

  [This release does not contain any user-facing changes, only improvements to the internal CI release workflow.](platform/v1-8-5.md)
* [ Tenzir Platform v1.8.4 Mar 6, 2025](platform/v1-8-4.md)

  [This patch release includes the following bug fixes over Tenzir Platform v1.8.3:](platform/v1-8-4.md)
* [ Tenzir Node v4.29.1 Mar 3, 2025](tenzir/v4-29-1.md)
* [ Tenzir Node v4.29.0 Feb 25, 2025](tenzir/v4-29-0.md)
* [ Tenzir Platform v1.8.3 Feb 21, 2025](platform/v1-8-3.md)

  [This patch release includes the following bug fixes over Tenzir Platform v1.8.2:](platform/v1-8-3.md)
* [ Tenzir Platform v1.8.2 Feb 19, 2025](platform/v1-8-2.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.8.1:](platform/v1-8-2.md)
* [ Tenzir Node v4.28.2 Feb 13, 2025](tenzir/v4-28-2.md)
* [ Tenzir Node v4.28.0 Feb 10, 2025](tenzir/v4-28-0.md)
* [ Tenzir Platform v1.8.1 Feb 6, 2025](platform/v1-8-1.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.8:](platform/v1-8-1.md)
* [ Tenzir Node v4.27.0 Jan 30, 2025](tenzir/v4-27-0.md)
* [ Tenzir Platform v1.8.0 Jan 30, 2025](platform/v1-8-0.md)

  [This release adds support for the new and improved charting operators of Tenzir Node v4.27, and revamps example deployments in the platform repository.](platform/v1-8-0.md)
* [ Tenzir Node v4.26.0 Jan 22, 2025](tenzir/v4-26-0.md)
* [ Tenzir Platform v1.7.2 Jan 20, 2025](platform/v1-7-2.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.7.1:](platform/v1-7-2.md)
* [ Tenzir Platform v1.7.1 Jan 14, 2025](platform/v1-7-1.md)

  [This patch release contains the following bug fixes and improvements over Tenzir Platform v1.7:](platform/v1-7-1.md)
* [ Tenzir Node v4.25.0 Jan 9, 2025](tenzir/v4-25-0.md)
* [ Tenzir Platform v1.7.0 Jan 8, 2025](platform/v1-7-0.md)

  [This release introduces a new Drag'n'Drop feature to easily work with data from local files, and adds additional configuration knobs for Sovereign Edition users.](platform/v1-7-0.md)
* [ Tenzir Platform v1.6.1 Dec 18, 2024](platform/v1-6-1.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.6:](platform/v1-6-1.md)
* [ Tenzir Platform v1.6.0 Dec 17, 2024](platform/v1-6-0.md)

  [This release features a new UI for example pipelines and adds support for the new TQL2 mode for nodes.](platform/v1-6-0.md)
* [ Tenzir Node v4.24.1 Dec 12, 2024](tenzir/v4-24-1.md)
* [ Tenzir Platform v1.5.0 Dec 6, 2024](platform/v1-5-0.md)

  [This release brings a major upgrade to Dashboards making them independent of nodes.](platform/v1-5-0.md)
* [ Tenzir Node v4.24.0 Dec 3, 2024](tenzir/v4-24-0.md)
* [ Tenzir Node v4.23.1 Nov 21, 2024](tenzir/v4-23-1.md)
* [ Tenzir Platform v1.4.1 Nov 21, 2024](platform/v1-4-1.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.4:](platform/v1-4-1.md)
* [ Tenzir Platform v1.4.0 Nov 19, 2024](platform/v1-4-0.md)

  [This release introduces **alerts** for the Tenzir Platform, allowing users to get notified when a node is unexpectedly offline.](platform/v1-4-0.md)
* [ Tenzir Node v4.23.0 Nov 7, 2024](tenzir/v4-23-0.md)
* [ Tenzir Platform v1.3.0 Nov 7, 2024](platform/v1-3-0.md)

  [This release introduces a new **vertical layout** option to make better use of the screen space available for event data and longer pipelines:](platform/v1-3-0.md)
* [ Tenzir Node v4.22.2 Oct 28, 2024](tenzir/v4-22-2.md)
* [ Tenzir Node v4.22.1 Oct 23, 2024](tenzir/v4-22-1.md)
* [ Tenzir Platform v1.2.1 Oct 23, 2024](platform/v1-2-1.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.2:](platform/v1-2-1.md)
* [ Tenzir Platform v1.2.0 Oct 23, 2024](platform/v1-2-0.md)

  [This release brings improvements to diagnostics in the Explorer, adds the ability to download charts, and includes many stability improvements.](platform/v1-2-0.md)
* [ Tenzir Node v4.22.0 Oct 18, 2024](tenzir/v4-22-0.md)
* [ Tenzir Platform v1.1.2 Oct 15, 2024](platform/v1-1-2.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.1.1:](platform/v1-1-2.md)
* [ Tenzir Node v4.21.1 Oct 11, 2024](tenzir/v4-21-1.md)
* [ Tenzir Platform v1.1.1 Oct 11, 2024](platform/v1-1-1.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.1:](platform/v1-1-1.md)
* [ Tenzir Node v4.21.0 Oct 4, 2024](tenzir/v4-21-0.md)
* [ Tenzir Platform v1.1.0 Oct 4, 2024](platform/v1-1-0.md)

  [This release brings key enhancements, including improved diagnostics, authentication updates, and various bug fixes for a smoother user experience.](platform/v1-1-0.md)
* [ Tenzir Platform v1.0.8 Sep 19, 2024](platform/v1-0-8.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.0.7:](platform/v1-0-8.md)
* [ Tenzir Platform v1.0.7 Sep 16, 2024](platform/v1-0-7.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.0.6:](platform/v1-0-7.md)
* [ Tenzir Platform v1.0.6 Sep 12, 2024](platform/v1-0-6.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.0.5:](platform/v1-0-6.md)
* [ Tenzir Node v4.20.3 Sep 9, 2024](tenzir/v4-20-3.md)
* [ Tenzir Node v4.20.2 Sep 6, 2024](tenzir/v4-20-2.md)
* [ Tenzir Platform v1.0.5 Sep 3, 2024](platform/v1-0-5.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.0.4:](platform/v1-0-5.md)
* [ Tenzir Node v4.20.1 Sep 2, 2024](tenzir/v4-20-1.md)
* [ Tenzir Node v4.20.0 Aug 30, 2024](tenzir/v4-20-0.md)
* [ Tenzir Platform v1.0.4 Aug 26, 2024](platform/v1-0-4.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.0.3:](platform/v1-0-4.md)
* [ Tenzir Node v4.19.6 Aug 15, 2024](tenzir/v4-19-6.md)
* [ Tenzir Node v4.19.5 Aug 13, 2024](tenzir/v4-19-5.md)
* [ Tenzir Platform v1.0.3 Aug 13, 2024](platform/v1-0-3.md)

  [This patch release contains the following bug fixes and improvements over Tenzir Platform v1.0.2:](platform/v1-0-3.md)
* [ Tenzir Platform v1.0.2 Aug 13, 2024](platform/v1-0-2.md)

  [This patch release contains the following bug fixes and improvements over Tenzir Platform v1.0.1:](platform/v1-0-2.md)
* [ Tenzir Node v4.19.4 Aug 8, 2024](tenzir/v4-19-4.md)
* [ Tenzir Platform v1.0.1 Aug 8, 2024](platform/v1-0-1.md)

  [This patch release contains the following bug fixes and improvements over Tenzir Platform v1.0.0:](platform/v1-0-1.md)
* [ Tenzir Node v4.19.3 Aug 6, 2024](tenzir/v4-19-3.md)
* [ Tenzir Node v4.19.2 Aug 6, 2024](tenzir/v4-19-2.md)
* [ Tenzir Platform v1.0.0 Aug 6, 2024](platform/v1-0-0.md)

  [Tenzir Platform becomes generally available.](platform/v1-0-0.md)
* [ Tenzir Node v4.19.1 Aug 2, 2024](tenzir/v4-19-1.md)
* [ Tenzir Platform v0.20.2 Aug 1, 2024](platform/v0-20-2.md)

  [This bugfix release contains various small fixes and reliability improvements for the Tenzir Platform:](platform/v0-20-2.md)
* [ Tenzir Node v4.19.0 Jul 26, 2024](tenzir/v4-19-0.md)
* [ Tenzir Node v4.18.5 Jul 19, 2024](tenzir/v4-18-5.md)
* [ Tenzir Platform v0.20.1 Jul 18, 2024](platform/v0-20-1.md)

  [This release brings the following improvements and changes:](platform/v0-20-1.md)
* [ Tenzir Node v4.18.4 Jul 17, 2024](tenzir/v4-18-4.md)
* [ Tenzir Platform v0.20.0 Jul 17, 2024](platform/v0-20-0.md)

  [This release brings the following improvements and changes:](platform/v0-20-0.md)
* [ Tenzir Node v4.18.3 Jul 16, 2024](tenzir/v4-18-3.md)
* [ Tenzir Platform v0.19.1 Jul 16, 2024](platform/v0-19-1.md)
  [* This release fixes the CI not triggering for the Tenzir Platform v0.19 release, which caused the release artifacts not to be created.](platform/v0-19-1.md)
* [ Tenzir Platform v0.19.0 Jul 16, 2024](platform/v0-19-0.md)
  [* This release moves pipeline filters into the pipeline table's header, preparing for further upcoming changes to the table* This release adds a detailed activity view to the detailed pipeline view that opens when clicking on a pipeline* Clicking on the diagnostics column in the pipelines t...](platform/v0-19-0.md)
* [ Tenzir Node v4.18.2 Jul 15, 2024](tenzir/v4-18-2.md)
* [ Tenzir Node v4.18.1 Jul 12, 2024](tenzir/v4-18-1.md)
* [ Tenzir Node v4.18.0 Jul 11, 2024](tenzir/v4-18-0.md)
* [ Tenzir Platform v0.18.2 Jul 10, 2024](platform/v0-18-2.md)

  [This bugfix release: \* Improves the fix for the memory leak on the overview page \* Fixes an argument parsing bug in the `tenzir-platform admin delete-auth-rule` CLI command](platform/v0-18-2.md)
* [ Tenzir Platform v0.18.1 Jul 8, 2024](platform/v0-18-1.md)
  [* This release fixes a memory leak in the overview page \* This release updates the docker compose examples by automatically pinning them to the corresponding platform version](platform/v0-18-1.md)
* [ Tenzir Platform v0.18.0 Jul 4, 2024](platform/v0-18-0.md)

  [This release introduces diagnostics on the overview page on app.tenzir.com, making it easier to spot mistakes in pipelines. The overview page becomes more responsive when viewing a node with many running pipelines.](platform/v0-18-0.md)
* [ Tenzir Platform v0.17.2 Jul 2, 2024](platform/v0-17-2.md)

  [This release fixes a bug in the `tenzir-platform auth` subcommand.](platform/v0-17-2.md)
* [ Tenzir Platform v0.17.1 Jul 1, 2024](platform/v0-17-1.md)

  [This patch release fixes a bug where very long-running instances of the tenant-manager issue expired user keys, making it impossible for users to log in successfully.](platform/v0-17-1.md)
* [ Tenzir Node v4.17.4 Jun 27, 2024](tenzir/v4-17-4.md)
* [ Tenzir Node v4.17.3 Jun 25, 2024](tenzir/v4-17-3.md)
* [ Tenzir Node v4.17.2 Jun 24, 2024](tenzir/v4-17-2.md)
* [ Tenzir Node v4.17.1 Jun 21, 2024](tenzir/v4-17-1.md)
* [ Tenzir Node v4.17.0 Jun 21, 2024](tenzir/v4-17-0.md)
* [ Tenzir Platform v0.17.0 Jun 21, 2024](platform/v0-17-0.md)

  [This release introduces the ability to change pipelines on app.tenzir.com more quickly. Users can click on any pipeline on the overview page to open a detailed view, directly edit the definition or options, and use the new action menu to quickly start, pause, stop, duplicate, or delete pipelines.](platform/v0-17-0.md)
* [ Tenzir Platform v0.16.0 Jun 7, 2024](platform/v0-16-0.md)

  [This release introduces the initial public version of the on-premise Tenzir Platform for Sovereign Edition customers.](platform/v0-16-0.md)
* [ Tenzir Node v4.16.0 Jun 5, 2024](tenzir/v4-16-0.md)
* [ Tenzir Node v4.15.2 May 31, 2024](tenzir/v4-15-2.md)
* [ Tenzir Node v4.15.1 May 31, 2024](tenzir/v4-15-1.md)
* [ Tenzir Node v4.15.0 May 31, 2024](tenzir/v4-15-0.md)
* [ Tenzir Node v4.14.0 May 17, 2024](tenzir/v4-14-0.md)
* [ Tenzir Node v4.13.1 May 14, 2024](tenzir/v4-13-1.md)
* [ Tenzir Node v4.13.0 May 10, 2024](tenzir/v4-13-0.md)
* [ Tenzir Node v4.12.2 Apr 30, 2024](tenzir/v4-12-2.md)
* [ Tenzir Node v4.12.1 Apr 26, 2024](tenzir/v4-12-1.md)
* [ Tenzir Node v4.12.0 Apr 24, 2024](tenzir/v4-12-0.md)
* [ Tenzir Node v4.11.2 Mar 26, 2024](tenzir/v4-11-2.md)
* [ Tenzir Node v4.11.0 Mar 22, 2024](tenzir/v4-11-0.md)
* [ Tenzir Node v4.10.4 Mar 13, 2024](tenzir/v4-10-4.md)
* [ Tenzir Node v4.10.3 Mar 12, 2024](tenzir/v4-10-3.md)
* [ Tenzir Node v4.10.1 Mar 11, 2024](tenzir/v4-10-1.md)
* [ Tenzir Node v4.10.0 Mar 11, 2024](tenzir/v4-10-0.md)
* [ Tenzir Node v4.9.0 Feb 21, 2024](tenzir/v4-9-0.md)
* [ Tenzir Node v4.8.2 Jan 24, 2024](tenzir/v4-8-2.md)
* [ Tenzir Node v4.8.1 Jan 23, 2024](tenzir/v4-8-1.md)
* [ Tenzir Node v4.8.0 Jan 22, 2024](tenzir/v4-8-0.md)
* [ Tenzir Node v4.7.1 Dec 20, 2023](tenzir/v4-7-1.md)
* [ Tenzir Node v4.7.0 Dec 19, 2023](tenzir/v4-7-0.md)
* [ Tenzir Node v4.6.4 Dec 7, 2023](tenzir/v4-6-4.md)
* [ Tenzir Node v4.6.3 Dec 4, 2023](tenzir/v4-6-3.md)
* [ Tenzir Node v4.6.0 Dec 1, 2023](tenzir/v4-6-0.md)
* [ Tenzir Node v4.5.0 Nov 16, 2023](tenzir/v4-5-0.md)
* [ Tenzir Node v4.4.0 Nov 6, 2023](tenzir/v4-4-0.md)
* [ Tenzir Node v4.3.0 Oct 10, 2023](tenzir/v4-3-0.md)
* [ Tenzir Node v4.2.0 Sep 19, 2023](tenzir/v4-2-0.md)
* [ Tenzir Node v4.1.0 Aug 31, 2023](tenzir/v4-1-0.md)
* [ Tenzir Node v4.0.1 Aug 9, 2023](tenzir/v4-0-1.md)
* [ Tenzir Node v4.0.0 Aug 7, 2023](tenzir/v4-0-0.md)
* [ Tenzir Node v3.1.0 May 12, 2023](tenzir/v3-1-0.md)
* [ Tenzir Node v3.0.4 Apr 18, 2023](tenzir/v3-0-4.md)
* [ Tenzir Node v3.0.3 Mar 31, 2023](tenzir/v3-0-3.md)
* [ Tenzir Node v2.4.2 Mar 31, 2023](tenzir/v2-4-2.md)
* [ Tenzir Node v3.0.2 Mar 21, 2023](tenzir/v3-0-2.md)
* [ Tenzir Node v3.0.1 Mar 16, 2023](tenzir/v3-0-1.md)
* [ Tenzir Node v3.0.0 Mar 14, 2023](tenzir/v3-0-0.md)
* [ Tenzir Node v2.4.1 Dec 19, 2022](tenzir/v2-4-1.md)
* [ Tenzir Node v2.4.0 Dec 9, 2022](tenzir/v2-4-0.md)
* [ Tenzir Node v2.3.1 Oct 14, 2022](tenzir/v2-3-1.md)
* [ Tenzir Node v2.3.0 Sep 1, 2022](tenzir/v2-3-0.md)
* [ Tenzir Node v2.2.0 Aug 5, 2022](tenzir/v2-2-0.md)
* [ Tenzir Node v2.1.0 Jul 7, 2022](tenzir/v2-1-0.md)
* [ Tenzir Node v2.0.0 May 16, 2022](tenzir/v2-0-0.md)
* [ Tenzir Node v1.1.2 Mar 29, 2022](tenzir/v1-1-2.md)
* [ Tenzir Node v1.1.1 Mar 25, 2022](tenzir/v1-1-1.md)
* [ Tenzir Node v1.1.0 Mar 3, 2022](tenzir/v1-1-0.md)
* [ Tenzir Node v1.0.0 Jan 27, 2022](tenzir/v1-0-0.md)