# Tenzir Test

> An integration testing framework that discovers tests, runs them with managed fixtures, and validates output against baselines.


An integration testing framework that discovers tests, runs them with managed fixtures, and validates output against baselines.

[ GitHub ](https://github.com/tenzir/test/releases)

[Download releases and artifacts](https://github.com/tenzir/test/releases)

[ RSS Feed ](/changelog/tenzir-test.xml)

[Subscribe to release updates](/changelog/tenzir-test.xml)

## Releases

* [v1.7.3 Feb 27, 2026](tenzir-test/v1-7-3.md)

  [This release improves parallel suite scheduling reliability and adds correctness guards via suite.min\_jobs in test.yaml.](tenzir-test/v1-7-3.md)
* [v1.7.2 Feb 25, 2026](tenzir-test/v1-7-2.md)

  [This release fixes enum serialization errors when Python fixture tests use configuration values like mode: sequential in test.yaml.](tenzir-test/v1-7-2.md)
* [v1.7.1 Feb 25, 2026](tenzir-test/v1-7-1.md)

  [This release adds parallel suite execution and fixes several bugs, including clean Ctrl+C handling, consistent default fixture options, and reliable shell runner defaults for .sh test files.](tenzir-test/v1-7-1.md)
* [v1.7.0 Feb 22, 2026](tenzir-test/v1-7-0.md)

  [This release adds suite-level capability requirements, letting test suites declare required operators and skip gracefully when those capabilities are unavailable in the target build.](tenzir-test/v1-7-0.md)
* [v1.6.0 Feb 19, 2026](tenzir-test/v1-6-0.md)

  [This release adds fixture assertion hooks that enable post-test validation of side effects while fixtures remain active. Assertion results are tracked separately in the run summary.](tenzir-test/v1-6-0.md)
* [v1.5.1 Feb 16, 2026](tenzir-test/v1-5-1.md)

  [This release improves error handling by showing clean messages for unavailable fixtures and avoids unnecessary fixture initialization for fully skipped test suites.](tenzir-test/v1-5-1.md)
* [v1.5.0 Feb 16, 2026](tenzir-test/v1-5-0.md)

  [This release adds fine-grained controls for running skipped tests, including a new --run-skipped-reason flag with substring and glob matching semantics.](tenzir-test/v1-5-0.md)
* [v1.4.0 Feb 15, 2026](tenzir-test/v1-4-0.md)

  [This release introduces a standalone fixture mode for starting fixtures without running tests, adds a built-in docker-compose fixture with structured options, and provides shared container runtime helpers for writing custom fixtures.](tenzir-test/v1-4-0.md)
* [v1.3.2 Feb 13, 2026](tenzir-test/v1-3-2.md)

  [This release improves the readability of configuration override log messages by using relative paths and human-friendly formatting.](tenzir-test/v1-3-2.md)
* [v1.3.1 Feb 11, 2026](tenzir-test/v1-3-1.md)

  [This release adds support for nested dataclass hierarchies in fixture options, enabling multi-level structured configurations in test frontmatter.](tenzir-test/v1-3-1.md)
* [v1.3.0 Feb 10, 2026](tenzir-test/v1-3-0.md)

  [This release adds structured configuration options for fixtures, letting tests pass typed parameters through YAML frontmatter using frozen dataclasses.](tenzir-test/v1-3-0.md)
* [v1.2.2 Feb 9, 2026](tenzir-test/v1-2-2.md)

  [This release fixes a serialization bug where Python fixture tests with `skip` configurations in `test.yaml` failed with a JSON serialization error.](tenzir-test/v1-2-2.md)
* [v1.2.1 Feb 6, 2026](tenzir-test/v1-2-1.md)

  [This patch release improves the `-m`/`--match` flag with automatic substring matching and centralizes skip handling in the engine for more consistent test reporting.](tenzir-test/v1-2-1.md)
* [v1.2.0 Feb 6, 2026](tenzir-test/v1-2-0.md)

  [This release adds support for selecting tests by name using glob patterns via the new `-m`/`--match` CLI option.](tenzir-test/v1-2-0.md)
* [v1.1.1 Feb 6, 2026](tenzir-test/v1-1-1.md)

  [This release improves the CLI help text with usage examples and a link to the documentation.](tenzir-test/v1-1-1.md)
* [v1.1.0 Jan 31, 2026](tenzir-test/v1-1-0.md)

  [This release adds stdin file support for piping data directly to tests, and improves satellite project display in project listings.](tenzir-test/v1-1-0.md)
* [v1.0.2 Jan 27, 2026](tenzir-test/v1-0-2.md)

  [This release improves the debugging experience by making the `--debug` flag automatically enable verbose output, so you see all test results when diagnosing failures.](tenzir-test/v1-0-2.md)
* [v1.0.1 Jan 23, 2026](tenzir-test/v1-0-1.md)

  [This release fixes an issue with diff tests failing when using multi-word Tenzir commands.](tenzir-test/v1-0-1.md)
* [v1.0.0 Jan 23, 2026](tenzir-test/v1-0-0.md)

  [This release introduces automatic binary detection with a clear precedence order: environment variables take priority, followed by PATH lookup, with `uvx` as fallback. Environment variables now support multi-part commands for full control over binary invocation. The `--tenzir-binary` and \`--tenzi...](tenzir-test/v1-0-0.md)
* [v0.15.0 Jan 23, 2026](tenzir-test/v0-15-0.md)

  [This release adds the `--verbose` flag for controlling test output verbosity. By default, only failures are shown, reducing noise in large test suites while still providing all details when needed.](tenzir-test/v0-15-0.md)
* [v0.14.0 Jan 15, 2026](tenzir-test/v0-14-0.md)

  [This release introduces inline test inputs for better test organization in deeply nested hierarchies. Tests can now place input data directly alongside test files, and you can create local `inputs/` directories at any level with automatic shadowing semantics.](tenzir-test/v0-14-0.md)
* [v0.13.1 Dec 8, 2025](tenzir-test/v0-13-1.md)

  [This release fixes path handling in the diff runner to strip root path prefixes from output, making paths relative and consistent with other test runners.](tenzir-test/v0-13-1.md)
* [v0.13.0 Dec 3, 2025](tenzir-test/v0-13-0.md)

  [This release adds `--package-dirs` support and improves startup diagnostics.](tenzir-test/v0-13-0.md)
* [v0.12.0 Nov 5, 2025](tenzir-test/v0-12-0.md)

  [Minor release with improved NO\_COLOR handling.](tenzir-test/v0-12-0.md)
* [v0.11.0 Nov 4, 2025](tenzir-test/v0-11-0.md)

  [Expose tenzir-test as a reusable Python library.](tenzir-test/v0-11-0.md)