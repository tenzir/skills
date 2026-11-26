---
title: "Test Framework"
canonical: https://tenzir.com/docs/reference/test-framework
source: https://tenzir.com/docs/reference/test-framework.md
section: "Docs"
---

# Test Framework

> The tenzir-test harness discovers and runs integration tests for pipelines, fixtures, and custom runners. Use this page as a reference for concepts, configuration, and CLI details. For step-by-step walkthroughs, see the guides for running tests, writing tests, creating fixtures, adding custom runners, and configuring project hooks.

The [`tenzir-test`](https://github.com/tenzir/test) harness discovers and runs integration tests for pipelines, fixtures, and custom runners. Use this page as a reference for concepts, configuration, and CLI details. For step-by-step walkthroughs, see the guides for [running tests](../guides/write-tests.md), [writing tests](../guides/write-tests.md), [creating fixtures](../guides/write-tests.md), [adding custom runners](../guides/write-tests.md), and [configuring project hooks](../guides/write-tests.md).

## Install

The `tenzir-test` harness ships as a Python package that requires Python 3.13 or later. With [`uv`](https://docs.astral.sh/uv/), `uvx tenzir-test` runs the harness without an install and provides a matching Python when the system lacks one. To pin the harness in a Python project, add it with `uv add tenzir-test` (or `pip`). Verify the console script:

```sh
uvx tenzir-test --help
```

The harness requires Tenzir 7 and runs pipelines with `tenzir run`. To test against Tenzir 6, pin an earlier release with `uvx 'tenzir-test<3'`.

## Core concepts

* **Project root** – Directory passed to `--root`; typically contains `fixtures/`, `inputs/`, `runners/`, and `tests/`.
* **Mode** – Auto-detected as *project* or *package*. A `package.yaml` in the current directory (or its parent when you run from `<package>/tests`) switches to package mode.
* **Library** – A root that contains multiple packages (each with a `package.yaml` and its own `tests/`). The harness can discover all packages under such a library root and run their suites in one invocation. Use `--package-dirs` to load packages so their operators can cross-import.
* **Test** – Any supported file under `tests/`; frontmatter controls execution.
* **Runner** – Named strategy that executes a test (`tenzir`, `python`, custom entries).
* **Hook** – Project-level Python callback registered under `hooks/` or `hooks.py` and invoked at stable lifecycle points.
* **Fixture** – Reusable environment provider registered under `fixtures/` and requested via frontmatter.
* **Suite** – Directory-owned group of tests that share fixtures. Declare it with `suite:` in a `test.yaml`; all descendants join automatically. Members run sequentially by default, or concurrently when `mode: parallel` is set.
* **Input** – Data accessed with `TENZIR_INPUTS`; defaults to `<root>/inputs` but you can override it per directory or per test with an `inputs:` setting. The harness also supports inline inputs via `TENZIR_INPUT` for test-specific data files.
* **Stdin** – Content piped to the test process via a `.stdin` file placed next to the test. The harness exposes the file path via `TENZIR_STDIN` and automatically pipes its content to the subprocess stdin.
* **Scratch directory** – Ephemeral directory exposed as `TENZIR_TMP_DIR` during each test run.
* **Artifact / Baseline** – Runner output persisted next to the test; regenerate with `--update`. For TQL and shell tests, the baseline records diagnostics from stderr before normal output from stdout. The harness captures both channels separately, so their runtime scheduling does not affect the baseline.
* **Configuration sources** – Frontmatter plus inherited `test.yaml` files; `tenzir.yaml` still configures the Tenzir binary.

A typical project layout looks like this:

```text
project-root/
├── fixtures/
│   └── __init__.py
├── hooks/
│   └── __init__.py
├── inputs/
│   └── sample.ndjson
├── runners/
│   └── __init__.py
└── tests/
    ├── alerts/
    │   ├── sample.tql
    │   └── sample.txt
    ├── parsing/
    │   ├── csv.input           # Inline input for this test
    │   ├── csv.tql
    │   └── csv.txt
    ├── shell/
    │   ├── echo.sh
    │   ├── echo.stdin          # Stdin content piped to the test
    │   └── echo.txt
    └── python/
        └── quick-check.py
```

For a package layout (with `package.yaml`), the structure may look like:

```text
my-package/
├── package.yaml
├── operators/
│   └── custom-op.tql
├── fixtures/
│   └── __init__.py
├── runners/
│   └── __init__.py
└── tests/
    ├── inputs/
    │   └── sample.ndjson
    └── operators/
        ├── custom-op.tql
        └── custom-op.txt
```

The harness loads `fixtures/`, `runners/`, and `hooks/` from the project root, which is the directory you run it from or pass to `--root`. Run it from the package directory to use the folders next to `package.yaml`; a run from `<package>/tests` looks for them in `tests/` instead. The package holds operators but no pipelines, because Tenzir 7 refuses a package with a `pipelines/` folder in a configuration. Test the operators from `.tql` files under `tests/` instead.

## Execution modes and packages

* Mode resolution:

  * `--root` with `tests/` → **project mode**.
  * `--root` (or its parent when named `tests`) with a `package.yaml` → **package mode**.

* All built-in runners, including `shell`, provide `TENZIR_INPUTS` for [input data](test-framework.md#inputs). Custom runners can obtain it through `run.get_test_env_and_config_args(test)`.

* The built-in `tenzir` and `python` runners automatically prepare package context for tests inside a package:

  * Set `TENZIR_PACKAGE_ROOT` to the absolute package directory.
  * Resolve `TENZIR_INPUTS` to the nearest `inputs/` directory within the owning package boundary, falling back to `<package>/tests/inputs/`. Explicit directory `test.yaml` or test frontmatter overrides take precedence.
  * Include `--package-dirs=<package>` in `tenzir` runner invocations and Python `Executor` commands.
  * Set `TENZIR_WORKSPACE` to choose the workspace that Tenzir runs the test’s pipelines in, as described in [Workspaces](test-framework.md#workspaces).

* Without a manifest the harness stays in **project mode**, recursively discovers tests under `tests/`, and applies global fixtures, runners, and inputs.

### Package directories

The built-in `python` and `tenzir` runners use the same package-directory resolution. The harness combines these sources in order:

1. The package that owns the test, if any.
2. The effective directory-level `package-dirs` setting from `test.yaml`.
3. The CLI `--package-dirs` entries.

The harness expands library directories into their packages, normalizes paths, and removes duplicates while preserving the first occurrence. A nonempty result replaces ambient `TENZIR_PACKAGE_DIRS` with the comma-separated list. With no computed entries, the harness leaves the ambient value unchanged and adds no package flag to the Python fixture context. The `shell` runner and `DiffRunner` do not automatically compute this package list, and they do not set `TENZIR_WORKSPACE` either.

For Python tests, package preparation happens before fixture activation, so fixture factories can read the prepared values from `FixtureContext.env`. Factory-returned environment mappings overlay the child Python environment afterward and can override these values. These returned mappings are not progressively propagated to later fixture factories.

### Workspaces

A *workspace* in this section is a directory on your machine whose `package.yaml` decides which packages `tenzir run` loads, as in the help text of the `tenzir package` commands. It is not a workspace of deployments on the platform.

The `tenzir run` command looks for a workspace from its working directory, which is the nearest directory at or above it with a `package.yaml`. In a workspace, Tenzir loads only the packages that the workspace uses and ignores `--package-dirs`. Because the harness runs tests from the project root, a package at the root would otherwise hide every other package directory. The built-in `tenzir` and `python` runners therefore set `TENZIR_WORKSPACE` for the tests they prepare packages for:

* A test runs in its package’s workspace when the package has a `package.lock`. Tenzir then loads the package and its locked dependencies from the package cache.
* A test of a package under the `packages/` directory of a workspace, or of the workspace itself, runs in that workspace.
* Every other test with package directories runs in no workspace (`TENZIR_WORKSPACE=none`), so that Tenzir loads the package directories.
* A `TENZIR_WORKSPACE` in the environment takes precedence, and the harness leaves it unchanged.

A package with a lock runs in its own workspace, which loads no package directories. For its tests, the harness ignores the `package-dirs` entries from `test.yaml` and the CLI `--package-dirs` entries, and prints a warning that names them. Packages of the same workspace do not count as ignored, because the workspace loads them anyway. List every package that the tests use under `dependencies` in the `package.yaml` and lock them instead:

package.yaml

```yaml
id: acme
name: Acme
dependencies:
  stix: ^0.0.1
```

A package that lists `dependencies` without a `package.lock` runs in no workspace, so its dependencies load from package directories. This suits a repository that holds several packages, where a package’s tests use the sibling packages in their current state. Name the siblings in `package-dirs`:

acme/tests/test.yaml

```yaml
package-dirs:
  - ../../stix
```

### Locked dependencies

Tenzir loads locked packages only from its package cache in `$XDG_CACHE_HOME/tenzir/packages`, which defaults to `~/.cache/tenzir/packages`. Before it runs the tests of a project, the harness checks the `package.lock` of every workspace that the selected tests run in. When the cache lacks a locked package, the harness runs this command in that workspace:

```sh
tenzir package fetch --locked
```

The fetch clones the repositories that the locked packages come from, so it needs `git` and network access, but no sign-in. With `--locked`, it never changes `package.lock`. When the lock no longer matches `package.yaml`, the fetch fails; run `tenzir package lock` and commit the updated lock. To keep CI runs from fetching the same packages again, cache `~/.cache/tenzir/packages` keyed on the `package.lock` files.

The harness derives the fetch command from the command it runs tests with, by dropping `run`. The fetch needs a Tenzir installation that includes the platform commands. If the test command names no `tenzir` executable, or the fetch fails, the harness prints a warning with the command to run by hand. The affected tests then fail with Tenzir’s diagnostic about the missing package.

## CLI reference

Run the tests from the project root:

```sh
uvx tenzir-test
```

Useful options:

* `--root <path>`: The project root. Defaults to `TENZIR_TEST_ROOT`, or the current directory without it.
* `--update` (`-u`): Rewrite reference artifacts next to each test.
* `--purge`: Remove generated artifacts (diffs, text outputs) from previous runs and exit.
* `--jobs N` (`-j`): Control concurrency (`4 * CPU cores` by default).
* `--coverage` and `--coverage-source-dir`: Enable LLVM coverage.
* `--keep` (`-k`): Preserve per-test scratch directories instead of deleting them (same as setting `TENZIR_KEEP_TMP_DIRS=1`).
* `--package-dirs <path>`: Extra package directories for Tenzir binaries. Repeatable and accepts comma-separated lists. Entries follow the owning package and effective directory YAML entries in the [package-directory resolution order](test-framework.md#package-directories). Tests of a package with a lock ignore them, as described in [Workspaces](test-framework.md#workspaces).
* `--debug` (`-d`): Emit framework-level diagnostics (fixture lifecycle, discovery notes, comparison targets, etc.) and automatically enable verbose output so you see all test results (pass/skip/fail) instead of only failures. The same mode is available via `TENZIR_TEST_DEBUG=1`.
* `--summary`: Print the tabular breakdown and failure tree after each project.
* `--runner-summary` and `--fixture-summary`: Add per-runner and per-fixture statistics to the summary table.
* `--report-json FILE`: Write a versioned JSON report. Use `-` to emit tagged JSON records in stdout for CI wrappers and sandboxed builds. Reports also work with `--no-hooks` and `--no-diff`, but not with standalone `--fixture` mode.
* `--diff/--no-diff`: Toggle unified diff output for failed comparisons. Diffs are shown by default; disable them when you only need aggregated statistics.
* `--diff-stat/--no-diff-stat`: Show (or suppress) the per-file change counter, which summarizes additions and deletions even when the diff body is hidden.
* `--passthrough` (`-p`): Stream raw stdout/stderr to the terminal instead of comparing against reference artifacts. The harness forces single-job execution (overriding `--jobs` when necessary) and ignores `--update` while passthrough is active. Passthrough mode automatically enables verbose output.
* `--verbose` (`-v`): Print individual test results as they complete. By default (quiet mode) the harness only shows failures and a compact summary, significantly reducing noise for large test suites. Verbose mode displays passing and skipped tests alongside failures. Use `--summary` together with `--verbose` to include the tree summary at the end of the run.
* `--run-skipped`: Run all skipped tests unconditionally. Both static skips (`skip: reason`) and conditional skips (`skip: {on: fixture-unavailable}`) are bypassed. When a fixture raises `FixtureUnavailable` and `--run-skipped` is active, the exception propagates as a hard failure instead of being caught. Use it when you want to force every skipped test to execute regardless of its skip reason.
* `--run-skipped-reason`: Selectively run skipped tests whose reason matches a substring or glob pattern. Bare strings match as substrings; patterns containing `*`, `?`, or `[` use fnmatch syntax, the same matching semantics as `--match`. Repeatable; a test runs if its skip reason matches any provided pattern. The match applies to the final displayed reason, including the `fixture unavailable:` prefix for conditional skips. When both `--run-skipped` and `--run-skipped-reason` are provided, `--run-skipped` takes precedence and all skipped tests run. When no skipped tests match the reason filters, the harness prints a diagnostic message.
* `--all-projects` (`-a`): Run the root project together with any satellites provided on the command line.
* `--match` (`-m`): Select tests whose relative path matches a substring or glob pattern. Bare strings (without `*`, `?`, or `[`) match as substrings, so `--match mysql` selects any test with “mysql” anywhere in its path. Patterns containing glob metacharacters use fnmatch syntax. Repeatable; tests matching any pattern are selected. When combined with positional TEST paths, only tests matching both are run (intersection).
* `--fixture-name`: Select tests that request a fixture with the given name. Matching is case-sensitive and uses the configured fixture name, not fixture options. Repeatable; tests matching any selected fixture name or fixture tag are selected.
* `--fixture-tag`: Select tests that request fixtures with the given tag. Repeatable; tests matching any selected fixture tag or fixture name are selected. When combined with positional TEST paths or `--match` patterns, only tests matching all selectors are run (intersection). Use `--fixture-tag container` to run tests backed by container fixtures, or `--fixture-tag docker-compose` to run tests using the built-in Docker Compose fixture.
* `--fixture`: Activate fixtures in standalone foreground mode without running tests. Repeatable. Accepts bare names (`--fixture mysql`) or YAML mapping specs (`--fixture 'kafka: {port: 9092}'`). When provided, positional TEST arguments are not allowed. See the [run fixtures](../guides/write-tests.md) guide.
* `--no-hooks`: Disable project hook loading and invocation. Use this when you need to recover from a broken hook or compare behavior without hook side effects.
* `--disable-inline-dependency-install`: Disable runtime installation for inline Python dependencies declared by tests or fixtures. Use this when another tool provisions the Python environment.

Set `TENZIR_TEST_DEBUG=1` in CI when you want the same diagnostics without passing `--debug` on the command line.

## Structured reports

Use `--report-json` to collect test results without parsing terminal output:

```sh
uvx tenzir-test --root test --report-json artifacts/tests.json
```

Reports do not change the test exit code or terminal output. They work with `--no-hooks`, `--no-diff`, parallel jobs, suites, retries, and satellite projects. Report paths are relative to the working directory at the start of the invocation, independently of `--root` and the report file’s location. Run the harness from the checkout root to produce repository-relative paths for CI. Paths use forward slashes and can contain `..` for projects outside that directory. Consumers must validate paths before linking or annotating source files.

### File format

The report is a UTF-8 JSON document with these fields:

* `schema_version`: The format version, currently `1`.
* `root`: The absolute working directory at the start of the invocation.
* `exit_code`: The harness exit code.
* `interrupted`: Whether the run was interrupted.
* `errors`: Harness-level errors, such as configuration or hook failures.
* `summary`: Counts named `total`, `passed`, `failed`, and `skipped`.
* `tests`: Final results sorted by project and path.

Each test result contains:

* `path` and `project`: The test file and project directory, relative to `root`.
* `runner` and `suite`: The runner name and optional suite name.
* `outcome`: `passed`, `failed`, or `skipped`.
* `attempts` and `duration`: The attempt count and elapsed seconds.
* `reason`: A failure diagnostic or skip reason, when available.
* `stdout`, `stderr`, and `returncode`: Captured subprocess output and exit code for a failing test. These describe the last subprocess captured through the harness’s `run_subprocess` helper. Output from custom runners that bypass that helper or stream output in passthrough mode is not captured.
* `diff`: Plain unified diffs, including reference filenames, for mismatched expectations. Multiple comparisons are concatenated.
* `truncated`: Whether any diagnostic was shortened.

Diagnostic text has no ANSI styling. Each text field is bounded to 6,000 characters after JSON encoding. Keep raw logs as a companion artifact when you need complete output. Only the final retry contributes diagnostics; a test that passes after retrying has no failure output.

A suite-level fixture failure appears as a failed result for the suite’s `test.yaml`, with `runner` set to `suite`. It contributes to report counts even if no individual test ran. Harness-level errors do not increase failed-test counts, so consumers must also check `exit_code`, `errors`, and `interrupted`.

The harness writes reports on normal completion, test failures, harness errors, and handled interruptions. It atomically replaces an existing report and creates parent directories when needed. A forced process kill cannot write a final report. An error writing a report fails the invocation rather than silently leaving an old result behind.

### Forward reports through build logs

When tests run in a build sandbox, use `--report-json -`:

```sh
uvx tenzir-test --root test --report-json -
```

Instead of a JSON document, this emits tagged JSON lines alongside normal terminal output. Every record begins with the literal `TENZIR_TEST_REPORT `, followed by a JSON object containing `schema_version: 1` and an `event`:

* `start`: Contains `root` and begins one invocation.
* `test`: Contains one final test result in `test`.
* `finish`: Contains `exit_code`, `interrupted`, `errors`, and `summary`.

Records are flushed as tests complete, so consumers can preserve partial results when the build is interrupted. A missing `finish` means the invocation is incomplete, not successful. Multiple invocations can share one build log; each `start` begins a separate report. Build tools may prepend a log prefix to each line. Consumers should remove that prefix, decode only tagged records, and keep the remaining lines as human-readable logs. Do not infer failures from terminal symbols or parse diffs from display formatting.

Within schema version 1, consumers should ignore unknown fields and events. Incompatible format changes increment `schema_version`.

## Continuous integration

A CI job that runs `uvx tenzir-test` needs these pieces:

| Need            | How the job meets it                                                                                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `uv`            | Install it, for example with the `astral-sh/setup-uv` action.                                                                                                                                           |
| Python 3.13+    | The `uv` tool provides it. With `astral-sh/setup-uv`, request it with `python-version: "3.13"`.                                                                                                         |
| Tenzir 7        | No separate install: without `TENZIR_BINARY` and a `tenzir` on `PATH`, the harness uses `uvx tenzir`, as in [Binary resolution](test-framework.md#binary-resolution). |
| Locked packages | `git` and network access, without sign-in, for the [fetch](test-framework.md#locked-dependencies) before the tests of a package with a lock.                          |
| Package cache   | Optional: cache `~/.cache/tenzir/packages`, keyed on the `package.lock` files, so that runs don’t fetch the same packages again.                                                                        |
| Results         | Optional: a [structured report](test-framework.md#structured-reports) with `--report-json`, uploaded even when the test step fails.                                   |

To test against the next Tenzir release as well, run the tests a second time with `TENZIR_BINARY="uvx --prerelease allow tenzir"`.

## Python API

The harness is also available as a typed Python library. Import `tenzir_test` and call `execute()` when you need to run scenarios from automation or another tool without shelling out to the CLI:

```python
from pathlib import Path


from tenzir_test import ExecutionResult, execute


result: ExecutionResult = execute(tests=[Path("tests/pipeline.tql")])
if result.exit_code:
    # propagate non-zero status to your orchestration layer
    raise SystemExit(result.exit_code)
for project in result.project_results:
    print(project.selection.root, project.summary.total)
```

The helper mirrors the CLI options but returns an `ExecutionResult` with aggregated `Summary` objects and metadata you can inspect or serialize. Errors surface as `HarnessError` exceptions so callers can control reporting and retry logic.

The `execute()` and `tenzir_test.run.run_cli()` helpers accept `report_json` as an optional `Path` argument:

```python
result = execute(
    root=Path("test"),
    report_json=Path("artifacts/tests.json"),
)
```

## Selections

A *selection* is the ordered list of positional paths you pass after the CLI flags. Each element can point to a single test file, a directory, or an entire project. The harness resolves every element relative to the current working directory first and then relative to the root project. How you shape the selection determines which projects run:

* No positional arguments → run every test in the root project.
* Paths inside the root project → run only those targets (plus any explicitly named satellites).
* Paths that resolve to satellite projects → run those satellites, skipping the root unless you also request it.

Use `--all-projects` when you want the root project to execute alongside a selection that only names satellites. This keeps the CLI predictable: the selection lists the exact satellites you care about, and the flag opts the root back in without duplicating its path on the command line.

## Suites

Suites let you run several tests under one shared fixture lifecycle. Declare a suite in a directory-level `test.yaml`; the definition applies to every test under that directory, including nested subdirectories.

The `suite` key accepts a plain string or a mapping with `name` and `mode`:

```yaml
# tests/http/test.yaml  -  sequential (default)
suite: smoke-http
fixtures: [http]
timeout: 45
```

The mapping form adds a `mode` field:

```yaml
# tests/http/test.yaml  -  parallel execution
suite:
  name: parallel-http
  mode: parallel
fixtures: [http]
timeout: 30
```

Adding `min_jobs` ensures the suite only starts when enough workers are available:

```yaml
# tests/http/test.yaml  -  parallel with minimum worker requirement
suite:
  name: parallel-http
  mode: parallel
  min_jobs: 2
fixtures: [http]
timeout: 30
```

The `mode` field controls how members execute:

* `sequential` (default): members run one after another in lexicographic order.
* `parallel`: all members run concurrently on separate threads while sharing the same fixture lifecycle. Fixture assertions are serialized to maintain correctness. Use this when tests are independent and can safely share fixtures at the same time.

The optional `min_jobs` key (positive integer) declares how many concurrent workers a parallel suite needs for correct execution. When set, the run fails immediately if `--jobs` is lower than `min_jobs`, and it also fails at runtime if the suite cannot reserve at least that many workers under slot contention. Use this for suites whose members must run concurrently (for example, publisher/subscriber pairs). The harness also warns when a parallel suite has more tests than available jobs, since not all members can run at once.

The plain string form (`suite: smoke-http`) is equivalent to `suite: {name: smoke-http, mode: sequential}`.

Key rules:

* Suites are directory-owned. Once a `test.yaml` sets `suite`, all descendants belong to that suite. Put tests that should remain independent outside the suite directory or in a sibling directory with a different suite.
* Per-test frontmatter may not declare `suite`.
* Suite members inherit the directory defaults and can still override most keys on a per-file basis. The exceptions are `fixtures` and `retry`, which must be defined at the directory level once a suite is active so every member agrees on the shared lifecycle. Outside suites you can still set those keys directly in frontmatter.
* A sequential suite occupies a single worker. A parallel suite reserves as many workers as it has members, up to `--jobs`, and runs its members in batches of that size. Different suites (and standalone tests) can run in parallel when `--jobs` allows it.
* The harness queues suites and standalone tests in path order, but starts parallel suites first so that they can reserve their workers.
* Run the directory that defines the suite (for example `tenzir-test tests/http`) when you want to focus on it. Selecting an individual member raises an error so every run exercises the full lifecycle and shared fixtures stay in sync. A `--match` pattern or fixture selector that matches a member selects the whole suite.

## Inputs

Tests access input data through the `TENZIR_INPUTS` environment variable. By default this points to `<root>/inputs` or `<package>/tests/inputs/` in package mode. The harness supports two additional mechanisms for placing inputs closer to the tests that use them.

### Inline inputs

Place a `.input` file next to a test to provide test-specific input data. The harness exposes the file path via `TENZIR_INPUT` (singular):

```text
tests/parsing/
  parse-csv.input      # Input data for this test
  parse-csv.tql        # Test file
  parse-csv.txt        # Expected output baseline
```

Access the inline input in TQL:

```tql
from_file env("TENZIR_INPUT") {
  read_csv
}
```

Or in a shell script:

```sh
cat "$TENZIR_INPUT" | tenzir 'read_csv'
```

The harness sets `TENZIR_INPUT` only when a matching `.input` file exists. Tests can use both `TENZIR_INPUT` and `TENZIR_INPUTS` together when they need a test-specific file plus access to shared data.

### Local inputs directories

Place an `inputs/` directory at any level in the test hierarchy to provide shared inputs for tests in that subtree. The harness walks up from each test directory and uses the nearest `inputs/` directory it finds:

```text
tests/
  network/
    inputs/               # Shared inputs for network tests
      sample.pcap
      flows.ndjson
    tcp/
      analysis.tql        # env("TENZIR_INPUTS") → ../inputs/
      analysis.txt
    udp/
      stats.tql
      stats.txt
inputs/                   # Global inputs (fallback)
  common.json
```

Resolution hierarchy for `TENZIR_INPUTS`:

1. `inputs:` override in test frontmatter or `test.yaml` (highest priority)
2. Nearest `inputs/` directory walking up from the test directory
3. Package-level `tests/inputs/` directory
4. Project-level `inputs/` directory (fallback)

When multiple `inputs/` directories exist in the hierarchy, the nearest one shadows the others. This keeps the mental model simple: move inputs closer to the tests that use them without worrying about inheritance.

### Stdin inputs

Place a `.stdin` file next to a test to provide content that the harness pipes to the subprocess stdin. For TQL tests, this lets pipelines start with a parser directly as an alternative to using `.input` files with `from_file`:

```text
tests/parsing/
  csv.stdin          # CSV data piped to stdin
  csv.tql            # Test file starting with read_csv
  csv.txt            # Expected output baseline
```

The TQL test reads directly from stdin:

```tql
read_csv
sort name
```

For shell scripts, the same mechanism applies:

```text
tests/shell/
  echo.stdin         # Content piped to stdin
  echo.sh            # Test file
  echo.txt           # Expected output baseline
```

```sh
#!/bin/sh
cat
```

The harness pipes the contents of the `.stdin` file automatically. Tests can combine `.stdin` with `.input` when they need both stdin content and a test-specific input file:

```text
tests/shell/
  process.stdin      # Content piped to stdin
  process.input      # Input file accessible via TENZIR_INPUT
  process.sh         # Test file
  process.txt        # Expected output baseline
```

A script using both mechanisms:

```sh
#!/bin/sh
echo "from stdin:"
cat
echo "from TENZIR_INPUT:"
cat "$TENZIR_INPUT"
```

The harness sets `TENZIR_STDIN` only when a matching `.stdin` file exists. TQL tests can also combine both mechanisms: start with a parser for stdin data while using `env("TENZIR_INPUT")` to reference additional files.

## Run a subset of tests

Pass individual files or directories to run specific tests:

```sh
uvx tenzir-test tests/alerts/high-severity.tql
```

You can list multiple paths in a single invocation. `tenzir-test` wires every argument into the same runner and fixture registry, so you can mix scenarios from the project and external checkouts:

```sh
uvx tenzir-test tests/alerts ../contrib/plugins/*/tests
```

### Filter tests by pattern

Use `--match` to select tests by matching against their relative path. Bare strings default to substring matching, so you can write short keywords without glob syntax:

```sh
uvx tenzir-test --match mysql         # runs every test with "mysql" in its path
uvx tenzir-test --match connect       # runs every test with "connect" in its path
```

Patterns containing glob metacharacters (`*`, `?`, `[`) still use fnmatch syntax, which is fully backwards-compatible:

```sh
uvx tenzir-test --match '*mysql*'             # equivalent to --match mysql
uvx tenzir-test --match 'tests/*/connect.tql' # glob with wildcard
```

Repeat the flag to match multiple patterns (logical OR):

```sh
uvx tenzir-test --match context --match create     # tests matching either substring
```

When you combine positional TEST paths with `--match` patterns, the harness runs only tests that satisfy both constraints (intersection):

```sh
uvx tenzir-test tests/integrations/ --match mysql  # only mysql tests under integrations/
```

If a matched test belongs to a suite (configured via `test.yaml`), all tests in that suite are included automatically so the shared fixture lifecycle stays intact.

### Filter tests by fixture

Use `--fixture-name` to select tests that request a fixture directly:

```sh
uvx tenzir-test --fixture-name mysql
uvx tenzir-test --fixture-name docker-compose
```

Fixture-name matching is case-sensitive and uses the fixture name from the `fixtures` configuration, ignoring fixture options.

Use `--fixture-tag` to select tests by metadata inherited from their requested fixtures:

```sh
uvx tenzir-test --fixture-tag container
uvx tenzir-test --fixture-tag docker-compose
```

Fixture tags are cumulative. The built-in `docker-compose` fixture has both the `container` and `docker-compose` tags, so `--fixture-tag container` includes Docker Compose tests and `--fixture-tag docker-compose` selects only tests that request the Docker Compose fixture.

Repeat fixture selectors to match any selected fixture name or tag:

```sh
uvx tenzir-test --fixture-name mysql --fixture-name sink
uvx tenzir-test --fixture-tag container --fixture-tag database
uvx tenzir-test --fixture-name mysql --fixture-tag container
```

Combine fixture selectors with positional paths or `--match` patterns to narrow the selection:

```sh
uvx tenzir-test tests/integrations/ --match kafka --fixture-name docker-compose
uvx tenzir-test tests/integrations/ --match kafka --fixture-tag container
```

The fixture selector is separate from `--fixture`, which starts fixtures in standalone foreground mode without running tests.

The harness infers tags from tagged fixture abstractions. Fixtures that use `tenzir_test.fixtures.container_runtime` inherit the `container` tag automatically. Fixtures that use custom abstractions can pass explicit tags at registration time:

```python
from tenzir_test import fixture


@fixture(name="localstack", tags=("container", "localstack"))
def localstack():
    ...
```

If a selected test belongs to a suite, the harness includes every test in that suite to keep the shared fixture lifecycle intact.

### Run multiple projects with one command

Pass additional project directories after `--root` to execute several projects in one go. Include `--all-projects` so the root executes next to its satellites. The directory given to `--root` acts as the **root project**; all other directories are treated as **satellites**:

```sh
uvx tenzir-test --root example-project --all-projects example-satellite
```

The harness prints a project listing before execution that identifies each project with a marker and path:

```text
i found 3 projects
i   ■ test
i   □ ../contrib/plugins/context/test
i   □ ../contrib/plugins/packages/test
```

Marker semantics:

* **Filled markers** indicate the root project; **empty markers** indicate satellites.
* **Squares** (■ □) represent regular projects; **circles** (● ○) represent packages or libraries.

Satellite paths display relative to the root project, making projects with identical directory names distinguishable.

Key rules:

* The root project provides the baseline configuration (fixtures, runners, `test.yaml` defaults, inputs). Satellites layer their own fixtures and runners on top; duplicate names raise an error so conflicts surface early.
* Paths printed in the CLI summary are relative to the working directory. The harness announces each project before running it and lists the runner mix per project for quick insight.
* You can target subsets inside each project with additional positional arguments (`tenzir-test --root main --all-projects secondary tests/smoke`). When you skip `--root` entirely and only list satellite directories, the harness runs those satellites in isolation.
* Satellites keep their own `tests/`, `inputs/`, `fixtures/`, and `runners/` folders. A root project can host shared assets that satellites reuse without duplication. For example, the example repository includes an `example-satellite/` directory that consumes the `xxd` runner exported by the root project while defining a satellite-specific fixture.

To regenerate baselines while targeting a specific binary and project root:

```sh
TENZIR_BINARY=/opt/tenzir/bin/tenzir \
uvx tenzir-test --root tests --update
```

## Hooks

Hooks are Python callbacks in `hooks/__init__.py` or `hooks.py` at the project root. They can run at invocation, project, and test lifecycle points. When both files exist, the harness loads only the `hooks/` package. It doesn’t load hooks from nested test directories.

Register a hook with the decorator of its event from `tenzir_test.hooks`, such as `@hooks.startup` or `@hooks.test_failure`. The decorators work only while the harness loads the project’s hooks. Each hook receives one argument, `ctx`, with the attributes of its event.

Available events:

| Event            | When it runs                                                                |
| ---------------- | --------------------------------------------------------------------------- |
| `startup`        | Once per invocation, before settings and binary discovery.                  |
| `shutdown`       | Once before the invocation exits normally.                                  |
| `project_start`  | Before the harness starts executing a root project or satellite.            |
| `project_finish` | After the harness finishes a root project or satellite.                     |
| `test_start`     | Before a logical test starts. Static skips don’t trigger this event.        |
| `test_finish`    | After the final outcome for passed, failed, skipped, and parse-error tests. |
| `test_failure`   | After `test_finish` for failed tests, before `TENZIR_TMP_DIR` cleanup.      |

The `test_failure` event runs only for final failures, not for intermediate retry attempts.

### Hook contexts

The `ctx` argument carries these attributes per event:

| Event            | Attributes of `ctx`                                                                                                                    |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `startup`        | `root`, `env`, `path`, `debug`                                                                                                         |
| `shutdown`       | `root`, `exit_code`, `interrupted`, `summary`, `project_results`, `debug`                                                              |
| `project_start`  | `root`, `project`, `previous_project`, `kind`, `env`, `path`, `debug`, `update`, `coverage`                                            |
| `project_finish` | `root`, `project`, `next_project`, `kind`, `summary`, `interrupted`, `debug`                                                           |
| `test_start`     | `root`, `project`, `test`, `runner`, `fixtures`, `suite`, `update`, `coverage`, `attempt_limit`                                        |
| `test_finish`    | `root`, `project`, `test`, `runner`, `outcome`, `reason`, `attempts`, `duration`, `fixtures`, `suite`, `tmp_dir`, `update`, `coverage` |
| `test_failure`   | The attributes of `test_finish` except `outcome`                                                                                       |

The attributes mean:

| Attribute                          | Type                      | Description                                                                                       |
| ---------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------- |
| `root`                             | `Path`                    | The invocation root.                                                                              |
| `env`                              | mutable mapping           | Environment variables to change. Setting or deleting `PATH` raises an error; edit `path` instead. |
| `path`                             | `list[str]`               | The entries of `PATH`, which the harness applies after the hook returns.                          |
| `debug`                            | `bool`                    | Whether debug mode is on.                                                                         |
| `project`                          | project view              | The current project, with `root` (`Path`) and `kind` (`"root"` or `"satellite"`).                 |
| `previous_project`, `next_project` | project view or `None`    | The project that ran before or runs after this one.                                               |
| `kind`                             | `"root"` or `"satellite"` | The kind of the current project.                                                                  |
| `update`, `coverage`               | `bool`                    | Whether `--update` or `--coverage` is on.                                                         |
| `test`                             | `Path`                    | The test file.                                                                                    |
| `runner`                           | `str`                     | The name of the runner that runs the test.                                                        |
| `fixtures`                         | tuple of fixture views    | The requested fixtures, each with `name` and `options`.                                           |
| `suite`                            | suite view or `None`      | The test’s suite, with `name` and `directory`.                                                    |
| `attempt_limit`                    | `int`                     | The attempt budget from `retry`.                                                                  |
| `outcome`                          | `str`                     | `passed`, `failed`, or `skipped`.                                                                 |
| `reason`                           | `str` or `None`           | The failure diagnostic or skip reason.                                                            |
| `attempts`, `duration`             | `int`, `float`            | The attempts made and the elapsed seconds.                                                        |
| `tmp_dir`                          | `Path` or `None`          | The test’s scratch directory, which still exists while the hook runs.                             |
| `summary`                          | summary view              | Counts named `failed`, `total`, and `skipped`.                                                    |
| `exit_code`, `interrupted`         | `int`, `bool`             | The harness exit code and whether the run was interrupted.                                        |
| `project_results`                  | tuple of result views     | One entry per project, with `project`, `summary`, and `queue_size`.                               |

### Hook scope and order

* The `env` and `path` of `startup` apply to the whole invocation, including settings and binary discovery, which run after the hook. Set `TENZIR_BINARY` there to choose the Tenzir binary.
* The `env` and `path` of `project_start` apply only to the tests of that project and don’t leak into the next project.
* The contexts of all other events are read-only.
* Only the invocation root’s `startup` and `shutdown` hooks run. A satellite’s `startup` hook runs only when the satellite is the invocation root.
* In a run of multiple projects, root hooks wrap satellite hooks. Start events run root first, then satellite. Finish and failure events run satellite first, then root. Within one project, finish and failure hooks run in reverse registration order.
* An exception in a hook fails the invocation with an error that names the hook. In `startup`, `project_start`, `test_start`, and `test_failure`, the first exception skips the remaining hooks of the event, and a failing `test_start` hook also fails its test. In `test_finish`, `project_finish`, and `shutdown`, the harness runs every hook first and then reports all errors.
* The `--no-hooks` flag and `TENZIR_TEST_DISABLE_HOOKS=1` turn hook loading off.

For examples, see the [configure project hooks](../guides/write-tests.md) guide.

## Runners

| Runner   | Command/behavior                                               | Input extension | Artifact |
| -------- | -------------------------------------------------------------- | --------------- | -------- |
| `tenzir` | `tenzir run --bare-mode --console-verbosity=warning -f <test>` | `.tql`          | `.txt`   |
| `python` | Execute with the active Python runtime                         | `.py`           | `.txt`   |
| `shell`  | `sh -eu <test>` via the harness helper                         | `.sh`           | `.txt`   |

The `tenzir` runner uses the [resolved binary](test-framework.md#binary-resolution) in place of `tenzir run` and adds `--config` and `--package-dirs` arguments as the test needs them.

Selection flow:

1. The harness chooses the first registered runner that claimed the file extension.
2. Default suffix mapping applies when no runner explicitly claims an extension: `.tql → tenzir`, `.py → python`, `.sh → shell`.
3. A `runner: <name>` frontmatter entry overrides the automatic choice.
4. If no runner claims the extension and none is specified in frontmatter, the harness fails with an error instead of guessing.

### Python runner

The built-in `python` runner passes the prepared package environment to the Python subprocess. Its fixture context carries only the resolved package flag in `config_args`, not `--config` arguments from adjacent `tenzir.yaml` files. This does not introduce general Tenzir configuration inheritance for Python tests. The subprocess also inherits the `TENZIR_WORKSPACE` that the harness chose for the test, so Tenzir commands it runs use the same [workspace](test-framework.md#workspaces).

The subprocess registers the same project fixtures as the harness: those of the root project and, for a test in a satellite, the satellite’s own. The harness passes their project directories in `TENZIR_TEST_FIXTURE_ROOTS`. A test can therefore call `acquire_fixture("name")` for any of them without importing anything. An explicit `import fixtures` still works and returns the fixtures of the test’s own project, which the subprocess has imported under that name already.

Use [`Executor`](test-framework.md#executor) to capture the prepared package directories and pass them as a CLI argument to Tenzir commands. Other Python subprocesses inherit `TENZIR_PACKAGE_DIRS` by default, so Tenzir commands can also load these packages through the environment. The harness does not add CLI arguments to arbitrary Python subprocess calls.

### Shell runner

Place scripts (for example under `tests/shell/`) with the `.sh` suffix to run them under `sh -eu` via the `shell` runner. The harness also prepends `<root>/_shell` to `PATH` so project-specific helper binaries become discoverable. The runner captures stdout and stderr separately and compares stderr followed by stdout with `<test>.txt`; run `tenzir-test --update path/to/test.sh` when you need to refresh the baseline.

### Runner API

Register custom runners in `runners/__init__.py` at the project root, which the harness imports on startup. The `tenzir_test.runners` module provides:

| Name                                            | Description                                                                                                                       |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `ExtRunner(name=..., ext=...)`                  | Base class for a runner that claims every file with the extension `ext`. The extensions `txt`, `input`, and `stdin` are reserved. |
| `Runner(name=...)`                              | Abstract base class for runners with their own discovery through `collect_tests()` and `purge()`.                                 |
| `run(self, test, update, coverage=False)`       | The method a runner implements. Returns `True` for a pass, `False` for a failure, or `"skipped"`.                                 |
| `register(runner, replace=False, aliases=None)` | Registers a runner instance. Registering a taken name fails unless `replace=True`, which also overrides a bundled runner.         |
| `@startup(replace=False, aliases=None)`         | Decorator for a factory function that returns a runner, which it registers.                                                       |
| `register_alias(alias, target, replace=False)`  | Publishes another name for a registered runner, for use in `runner:` frontmatter.                                                 |
| `unregister(name)`                              | Removes a runner and its aliases.                                                                                                 |

A runner’s `run()` method reports through the helpers of the `tenzir_test.run` module, which `tenzir_test.runners._utils.get_run_module()` returns:

| Helper                                                                                                             | Description                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `run_subprocess(args, *, capture_output, check=False, text=False, force_capture=False, stdin_data=None, **kwargs)` | Runs a command and honors [passthrough mode](test-framework.md#passthrough-aware-subprocesses). |
| `get_test_env_and_config_args(test, *, inputs=None)`                                                               | Returns the test’s environment, including `TENZIR_INPUTS`, and its `--config` arguments.                                          |
| `get_stdin_content(env)`                                                                                           | Returns the content of the test’s `.stdin` file, or `None` without one.                                                           |
| `success(test)`                                                                                                    | Reports a pass. Prints only in verbose mode.                                                                                      |
| `report_failure(test, message)`                                                                                    | Reports a failure with a message, which may be empty.                                                                             |
| `print_diff(expected, actual, path)`                                                                               | Prints a unified diff between the baseline bytes and the actual bytes.                                                            |
| `log_comparison(test, ref_path, *, mode)`                                                                          | Logs the comparison target in debug mode.                                                                                         |
| `is_passthrough_enabled()`, `is_update_mode()`, `get_harness_mode()`                                               | Report the [harness mode](test-framework.md#passthrough-aware-subprocesses).                    |

The [runner guide](../guides/write-tests.md) contains a full example (`XxdRunner`).

### Passthrough-aware subprocesses

When passthrough mode is active the harness streams stdout/stderr directly to the terminal and skips reference comparisons. Runner implementations can respect this automatically by spawning processes through `tenzir_test.run.run_subprocess(...)`. The helper captures output when the harness needs it and inherits the parent descriptors otherwise. Pass `force_capture=True` when your runner must collect stdout even in passthrough mode. If you need to branch on the current behavior, call `tenzir_test.run.get_harness_mode()` or `tenzir_test.run.is_passthrough_enabled()`.

The harness cycles between three internal modes:

* `HarnessMode.COMPARE` – default behavior; compare actual output with stored baselines.
* `HarnessMode.UPDATE` – engaged when you pass `--update`; runners should overwrite reference files.
* `HarnessMode.PASSTHROUGH` – enabled via `--passthrough`; stream output directly without touching baselines.

The `get_harness_mode()` function returns the current enum value so custom runners can adapt logic if needed.

## Configuration and frontmatter

The harness merges configuration sources in this order (later wins):

1. Project defaults (`test.yaml` files, applied per directory).
2. Per-test frontmatter (YAML for `.tql`/`.xxd`, `# key: value` comments for Python and shell scripts).

Common frontmatter keys:

| Key            | Type            | Default   | Description                                                                                                                                                                                    |
| -------------- | --------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `runner`       | string          | by suffix | Runner name (`tenzir`, `python`, `shell`, custom).                                                                                                                                             |
| `fixtures`     | list            | `[]`      | Requested fixtures. Accepts bare names and structured options mappings.                                                                                                                        |
| `timeout`      | integer (s)     | `30`      | Command timeout. (`--coverage` multiplies it by five.)                                                                                                                                         |
| `error`        | boolean         | `false`   | Expect a non-zero exit code.                                                                                                                                                                   |
| `quiet`        | boolean         | `false`   | Suppress runtime warnings from the test pipeline with the `tenzir` runner. See [runtime warning suppression](test-framework.md#runtime-warning-suppression). |
| `skip`         | string or dict  | unset     | Mark tests as skipped. See [skip configuration](test-framework.md#skip-configuration).                                                                       |
| `requires`     | mapping         | unset     | Capability requirements. See [capability requirements](test-framework.md#capability-requirements). Directory-level only.                                     |
| `inputs`       | string          | project   | Override `TENZIR_INPUTS` for this directory or test.                                                                                                                                           |
| `assertions`   | mapping         | `{}`      | Post-test assertion payloads. See [assertions](test-framework.md#assertions).                                                                                |
| `pre-compare`  | string or list  | `[]`      | Transform the baseline and the actual output before comparing them. See [pre-compare transforms](test-framework.md#pre-compare-transforms).                  |
| `retry`        | integer         | `1`       | Total attempt budget for flaky tests (see below).                                                                                                                                              |
| `package-dirs` | list of strings | inherit   | Directory-only; extra packages merged with CLI `--package-dirs`.                                                                                                                               |
| `suite`        | string or dict  | unset     | Directory-only; groups the directory’s tests into a [suite](test-framework.md#suites).                                                                       |

Any other key is an “Unknown configuration key” error. The harness accepts `fixture`, `package_dirs`, and `pre_compare` as spellings of `fixtures`, `package-dirs`, and `pre-compare`. A `runner` value can name a custom runner or an alias that a project registers, as in [Runner API](test-framework.md#runner-api).

The `test.yaml` files accept the same keys and apply recursively to child directories. A relative `inputs:` value resolves against the file that defines it, so `inputs: ../data` inside `tests/alerts/test.yaml` points at `tests/data/`. Frontmatter values follow the same rule and win over directory defaults. Adjacent `tenzir.yaml` files configure the bundled Tenzir runners as described in [Tenzir configuration files](test-framework.md#tenzir-configuration-files). This lookup also works for extra directories selected on the command line; it does not add `--config` arguments to the Python runner’s fixture context.

The `retry` key represents the **total number of attempts** the harness should make before declaring the test failed. Intermediate attempts stay quiet; the final outcome line includes `attempts=N/M` whenever the budget exceeds one. Keep the value small and treat it as a temporary guardrail while you fix the underlying flakiness.

### Directory package settings

The directory-only key `package-dirs` (also accepted as `package_dirs`) lists extra package directories or libraries:

```yaml
package-dirs: [../../shared-packages]
```

Relative entries resolve against the directory containing the declaring `test.yaml`, including when inherited by descendants. A child `test.yaml` replaces the inherited list rather than extending it. Set `package-dirs: []` to clear inherited YAML entries; this does not remove the automatic owning package or CLI entries. Tests of a package with a lock ignore these entries; lock the packages as dependencies instead, as described in [Workspaces](test-framework.md#workspaces).

### Runtime warning suppression

Set `quiet: true` when runtime warnings are irrelevant to the behavior your test verifies. Leave it disabled when the warning diagnostics themselves are part of the expected output.

For example, this test checks the result of parsing an invalid timestamp, not the warning diagnostic:

```tql
---
quiet: true
---
from {time: "not a timestamp"}
time = time.parse_time("%Y-%m-%d")
```

The `tenzir` runner evaluates the test inside a [`quiet`](operators/quiet.md) block. Runtime warnings from the pipeline and its nested pipelines are suppressed, while events and bytes flow through unchanged. Errors still fail the test unless you set `error: true`, and compilation diagnostics remain visible. The setting works in comparison, update, and passthrough modes and requires a Tenzir binary that supports `quiet`.

To apply the setting to a directory and its descendants, add it to `test.yaml`:

```yaml
quiet: true
```

Set `quiet: false` in a test’s frontmatter or a child directory’s `test.yaml` to restore runtime warnings. The setting does not suppress warnings from fixtures, other runners, or command-line logging. It suppresses all runtime warnings from the test pipeline, not individual warning messages. To limit suppression to part of a pipeline, use the TQL `quiet` operator directly instead.

Diagnostic line numbers reflect the additional `quiet` block around the test. Use `--keep` to retain the wrapped pipeline in `TENZIR_TMP_DIR` for inspection.

### Skip configuration

The `skip` key supports two forms:

**String form** marks the test (or every test in the directory) as unconditionally skipped. The value is the reason:

```yaml
skip: "pending upstream fix"
```

**Structured form** conditionally skips tests when a runtime condition occurs. Use this when a fixture or suite capability depends on an external resource that may not be available in every environment:

```yaml
skip:
  on: fixture-unavailable
```

The `on` field accepts the following values:

* `fixture-unavailable`: Skip when a fixture raises `FixtureUnavailable` during initialization. See [Fixture unavailability](test-framework.md#fixture-unavailability).
* `capability-unavailable`: Skip when a required capability (declared via [`requires`](test-framework.md#capability-requirements)) is missing from the runtime environment. This value is only valid in directory-level `test.yaml` files.

The `fixture-unavailable` condition follows fixture activation scope. If a fixture is selected by one test, put `skip: {on: fixture-unavailable}` in that test’s frontmatter or inherit it from a directory-level `test.yaml`; only that test is skipped when the fixture is unavailable. If a suite fixture is selected in `test.yaml`, put the skip opt-in in the suite’s directory-level configuration; suite setup happens before any member test runs, so member frontmatter cannot control a suite fixture failure.

You can combine multiple conditions by passing a list:

```yaml
skip:
  on:
    - fixture-unavailable
    - capability-unavailable
```

When the triggering condition occurs and the active scope carries the matching `on` value, the affected test or suite is marked as skipped with exit code 0. Without the opt-in configuration the exception propagates normally and causes a test failure.

The optional `reason` field provides additional context that is combined with the condition message in the skip output.

### Capability requirements

The `requires` key declares capabilities that must be present for a suite to run. It is only allowed in directory-level `test.yaml` files. Currently, the only supported category is `operators`:

tests/gcs/test.yaml

```yaml
suite: gcs-integration
requires:
  operators: [from_google_cloud_storage, to_google_cloud_storage]
skip:
  on: capability-unavailable
  reason: requires GCS operators
```

Before running the suite, the harness checks the listed requirements. It evaluates `requires` only for suites, so outside a suite the key has no effect. If any are missing and the suite carries `skip: {on: capability-unavailable}`, the tests are skipped. Without the skip opt-in, missing capabilities cause a hard failure with a message listing the missing entries.

The harness probes each operator with the [resolved Tenzir binary](test-framework.md#binary-resolution), the suite’s configuration, and its package directories, by running `plugins | where name == "<operator>"`. An operator is available when the probe prints a result. The harness caches the result per operator and configuration for the rest of the run.

### Tenzir configuration files

* The harness inspects the directory that owns each test. If it finds `tenzir.yaml`, it appends `--config=<path>` to every invocation of the bundled `tenzir`/`tql`/`diff` runners. The path also seeds `TENZIR_CONFIG` unless you set that variable yourself. Custom runners that call the Tenzir binary should either use `run.get_test_env_and_config_args(test)` or honor the exported environment variables explicitly.

## Fixtures

### Declaring fixtures

* List fixture names in frontmatter (`fixtures: [mysql, http]`). Entries can be bare strings or single-key mappings with structured options:

  ```yaml
  # Bare names (backward compatible)
  fixtures: [mysql, http]


  # With structured options
  fixtures:
    - mysql:
        tls: true
        port: 3306
    - http


  # Mixed form
  fixtures:
    - mysql:
        tls: true
    - http
  ```

  The harness registers custom fixtures by importing the project’s `fixtures` package or `fixtures.py`, whose decorators run as a side effect. A satellite sees the fixtures of the root project and its own. The process of a [Python test](test-framework.md#python-runner) registers the same fixtures, so tests don’t need to import them.

* The harness encodes requests in `TENZIR_TEST_FIXTURES` and exposes helper APIs in `tenzir_test.fixtures`:

  * `fixtures()` – Read-only view of active fixtures. Attribute access is supported, e.g. `fixtures().mysql` returns `True` if the fixture was requested and raises `AttributeError` otherwise.
  * `acquire_fixture("name")` – Manual controller for the named fixture, built in or defined by the project. Use it as a context manager for automatic `start()`/`stop()` or call those methods explicitly to interleave lifecycle steps and optional hooks (for example `kill()` or `restart()`).
  * `require("name")` – Assert that a fixture was requested.
  * `Executor()` – Convenience wrapper that runs Tenzir commands with resolved binaries and timeout budget.

Example use from a Python helper:

```python
from tenzir_test.fixtures import Executor


executor = Executor()
result = executor.run("from_file 'inputs/events.ndjson' | where severity >= 5\n")
assert result.returncode == 0
```

### Executor

The `Executor(env=...)` helper selects `env or os.environ` as its configuration source, so an empty mapping falls back to `os.environ`. At construction, it captures these values from the source:

* The command from `TENZIR_PYTHON_FIXTURE_BINARY`, falling back to `TENZIR_BINARY`. The Python runner sets both for its tests.
* The time budget from `TENZIR_PYTHON_FIXTURE_TIMEOUT`.
* An optional endpoint from `TENZIR_PYTHON_FIXTURE_ENDPOINT`. When it is set, each command also gets `--endpoint=<value>`. A project fixture can yield it, so that `Executor.from_env(controller.env)` uses the fixture’s endpoint.
* The package directories from `TENZIR_PACKAGE_DIRS`.

If the captured package value is nonempty, each command appends `--package-dirs=<captured value>` after the binary command prefix. The value is passed unchanged, without further path expansion or deduplication. This flag takes precedence over earlier package flags in the prefix. Later mutations to the selected source mapping or ambient environment do not change it.

An empty or absent captured value generates no package flag. It does not suppress `TENZIR_PACKAGE_DIRS` inherited through the subprocess’s actual environment. The selected mapping is not forwarded wholesale as the subprocess environment; the subprocess inherits the environment at execution time.

### Built-in docker-compose fixture

* Request the fixture with `fixtures: [docker-compose]` or pass structured options in `test.yaml` or frontmatter. The fixture manages Docker Compose services for the duration of the test or suite.
* The fixture requires `docker compose` (v2) on the host. When Docker Compose is not available, it raises `FixtureUnavailable` so tests can skip gracefully via `skip: {on: fixture-unavailable}`.
* Configuration uses three nested dataclasses: `DockerComposeOptions` (top level), `DockerComposeWaitOptions` (readiness polling), and `DockerComposeDownOptions` (teardown behavior).

#### Options reference

Top-level options (`DockerComposeOptions`):

| Field            | Type           | Default     | Description                                                                               |
| ---------------- | -------------- | ----------- | ----------------------------------------------------------------------------------------- |
| `file`           | string         | `""`        | Path to the Compose file, resolved relative to the test directory.                        |
| `project_name`   | string         | `""`        | Compose project name. Auto-generated from the test file name when empty.                  |
| `profiles`       | list of string | `[]`        | Compose profiles to activate.                                                             |
| `services`       | list of string | `[]`        | Services to start. When empty, all services in the Compose file start.                    |
| `env_file`       | string or null | `null`      | Path to an env file passed to `docker compose --env-file`, resolved relative to the test. |
| `env`            | dict           | `{}`        | Extra environment variables injected into the Compose process.                            |
| `pull`           | string         | `"missing"` | Image pull policy: `missing`, `always`, or `never`.                                       |
| `build`          | boolean        | `false`     | Pass `--build` to `docker compose up`.                                                    |
| `wait`           | object         | see below   | Readiness polling settings.                                                               |
| `down`           | object         | see below   | Teardown settings.                                                                        |
| `log_on_failure` | boolean        | `true`      | Collect and attach Docker Compose logs when the fixture fails.                            |

Wait options (`DockerComposeWaitOptions`):

| Field                   | Type  | Default | Description                                        |
| ----------------------- | ----- | ------- | -------------------------------------------------- |
| `timeout_seconds`       | float | `120.0` | Maximum time to wait for all services to be ready. |
| `poll_interval_seconds` | float | `1.0`   | Interval between readiness checks.                 |

Down options (`DockerComposeDownOptions`):

| Field             | Type    | Default | Description                                      |
| ----------------- | ------- | ------- | ------------------------------------------------ |
| `volumes`         | boolean | `true`  | Remove volumes on teardown (`--volumes`).        |
| `remove_orphans`  | boolean | `true`  | Remove orphan containers (`--remove-orphans`).   |
| `timeout_seconds` | integer | `20`    | Timeout for `docker compose down` (`--timeout`). |

#### Example configuration

Minimal configuration in `test.yaml`:

```yaml
suite: compose-demo
fixtures:
  - docker-compose:
      file: compose.yaml
skip:
  on: fixture-unavailable
  reason: requires docker compose
```

Full configuration with all options:

```yaml
fixtures:
  - docker-compose:
      file: compose.yaml
      project_name: my-project
      profiles: [integration]
      services: [redis, postgres]
      env_file: compose.env
      env:
        COMPOSE_PARALLEL_LIMIT: 8
      pull: always
      build: true
      wait:
        timeout_seconds: 90
        poll_interval_seconds: 2.0
      down:
        volumes: true
        remove_orphans: true
        timeout_seconds: 30
      log_on_failure: true
```

#### Readiness detection

The fixture polls each container until it is ready. If a container defines a health check, the fixture waits for the `healthy` status. Otherwise, it falls back to checking that the container is in the `running` state. The `wait.timeout_seconds` setting controls how long the fixture waits before raising an error.

#### Exported environment variables

Once all services are running, the fixture exports the following variables to the test environment:

| Variable                                            | Description                                                                                          |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `DOCKER_COMPOSE_PROVIDER`                           | Always `docker`.                                                                                     |
| `DOCKER_COMPOSE_PROJECT_NAME`                       | The Compose project name (explicit or auto-generated).                                               |
| `DOCKER_COMPOSE_FILE`                               | Absolute path to the resolved Compose file.                                                          |
| `DOCKER_COMPOSE_SERVICE_<NAME>_CONTAINER_ID`        | Container ID for the service. `<NAME>` is the uppercased, normalized service name.                   |
| `DOCKER_COMPOSE_SERVICE_<NAME>_HOST`                | Always `127.0.0.1`.                                                                                  |
| `DOCKER_COMPOSE_SERVICE_<NAME>_PORT_<PORT>_<PROTO>` | Host-mapped port for a specific container port and protocol (for example `_PORT_6379_TCP`).          |
| `DOCKER_COMPOSE_SERVICE_<NAME>_PORT`                | Shorthand for the single published port, set only when the service exposes exactly one port binding. |

Service names are normalized to uppercase with non-alphanumeric characters replaced by underscores. For a service named `redis`, the prefix is `DOCKER_COMPOSE_SERVICE_REDIS_`.

#### Teardown

When the test (or suite) completes, the fixture runs `docker compose down` with the configured teardown options. Volumes are removed by default to avoid leaking state between test runs. The fixture always attempts teardown even when the test fails.

### Registering fixtures

Implement fixtures in `fixtures/` and register them with `@tenzir_test.fixture()`. Decorate a generator function, yield the environment mapping, and handle cleanup in a `finally` block:

```python
from tenzir_test import fixture


@fixture()
def http():
    server = _start_server()
    try:
        yield {"HTTP_FIXTURE_URL": server.url}
    finally:
        server.stop()
```

`@fixture` also accepts regular callables returning dictionaries, context managers, or `FixtureHandle` instances for advanced scenarios.

A fixture’s name defaults to the file name of its module without `.py`, not to the function name: `def http()` in `fixtures/http.py` registers `http`, and a fixture defined in `fixtures/__init__.py` registers `__init__`. Pass `name=` to choose the name explicitly.

Registering a name that another fixture already holds fails, unless you pass `replace=True`. Registering the same definition again, as a second import of its module does, replaces the earlier registration without an error.

The [fixture guide](../guides/write-tests.md) demonstrates an HTTP echo server that exposes `HTTP_FIXTURE_URL` and tears down cleanly.

### Fixture API

The `tenzir_test` package exports the names that fixture modules use; the rest live in `tenzir_test.fixtures`:

| Name                                                                                               | Description                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@fixture(name=None, replace=False, log_teardown=False, options=None, assertions=None, tags=None)` | Registers a fixture factory. The `options` and `assertions` arguments take frozen dataclass types; `tags` takes a string or strings.                                                          |
| `register(name, factory, *, replace=False, options=None, assertions=None, tags=None)`              | Registers a factory without the decorator.                                                                                                                                                    |
| `FixtureHandle(env=None, teardown=None, hooks=None)`                                               | A factory’s return value: the environment mapping, a callable that tears down, and a mapping of hook names to callables.                                                                      |
| `FixtureUnavailable(message)`                                                                      | Exception that a factory raises before it yields when it can’t provide its service. See [Fixture unavailability](test-framework.md#fixture-unavailability). |
| `current_options(name)`                                                                            | The typed options of the named fixture in the active context, or the dataclass defaults, or `{}` without an options class.                                                                    |
| `current_assertions(name)`                                                                         | The assertions payload of the named fixture in the active context, typed like the `assertions` argument of `assert_test`, or `{}`.                                                            |
| `acquire_fixture(name)`                                                                            | A `FixtureController` for driving the named fixture by hand.                                                                                                                                  |
| `fixtures()`                                                                                       | A read-only view of the requested fixtures, with attribute access such as `fixtures().mysql`.                                                                                                 |
| `require(*names)`, `has(name)`                                                                     | Assert, or check, that the test requested fixtures.                                                                                                                                           |
| `Executor(env=None)`                                                                               | Runs Tenzir commands, as described in [Executor](test-framework.md#executor).                                                                               |

A `FixtureController` has these members:

| Member        | Description                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------ |
| `start()`     | Starts the fixture and returns its environment mapping. Fails if the fixture already runs.             |
| `stop()`      | Tears the fixture down. Does nothing if it doesn’t run.                                                |
| `restart()`   | Stops and starts the fixture.                                                                          |
| `env`         | The environment mapping of the running fixture, or `{}`.                                               |
| `is_running`  | Whether the fixture runs.                                                                              |
| `<hook>(...)` | Each hook of the `FixtureHandle`, such as `kill()`. Calling a hook while the fixture is stopped fails. |

The controller also works as a context manager that calls `start()` on entry and `stop()` on exit.

### Fixture dependencies

Project fixture modules can declare Python package dependencies with a PEP 723 script metadata block:

```python
# /// script
# dependencies = ["boto3"]
# ///


from tenzir_test import fixture
```

This applies to normal test execution and standalone fixture mode with `tenzir-test --fixture`. When fixture files declare dependencies, `uv` must be available on `PATH`. See the [fixture guide](../guides/write-tests.md#declare-python-dependencies) for a complete example.

### Fixture options

Fixtures can declare a frozen dataclass via `options=` on `@fixture()`. The harness constructs a typed instance from frontmatter values:

```python
@dataclass(frozen=True)
class HttpOptions:
    port: int = 0


@fixture(options=HttpOptions)
def http() -> Iterator[dict[str, str]]:
    opts = current_options("http")  # HttpOptions instance
    ...
```

```yaml
fixtures:
  - http:
      port: 9090
```

Bare names (`fixtures: [http]`) produce the dataclass defaults.

Note

Option fields can be nested dataclasses. The harness instantiates them recursively. See the [fixture guide](../guides/write-tests.md) for a complete walkthrough.

### Fixture unavailability

Fixtures can signal that they cannot provide their service by raising `FixtureUnavailable` during initialization (before yielding). This is useful when a fixture depends on an external tool or runtime that may not be present in every environment.

```python
from tenzir_test.fixtures import FixtureUnavailable, fixture


@fixture()
def mysql():
    if not shutil.which("docker"):
        raise FixtureUnavailable("docker not found")
    # ... start container, yield env, cleanup ...
```

By default the exception propagates and causes a test failure. To convert a suite fixture failure into a skip, add a structured `skip` entry to the suite’s `test.yaml`:

tests/mysql/test.yaml

```yaml
suite: mysql-integration
fixtures: [mysql]
skip:
  on: fixture-unavailable
  reason: "needs container runtime"
```

When the fixture raises `FixtureUnavailable` and the suite carries this configuration, the harness marks every test in the suite as skipped (exit code 0) and logs the combined reason. Without the opt-in configuration the exception surfaces as a regular failure. See [skip configuration](test-framework.md#skip-configuration) for the full syntax of the `skip` key.

For fixtures that are selected by individual tests, use the same skip mapping in test frontmatter:

```yaml
---
fixtures: [mysql]
skip:
  on: fixture-unavailable
  reason: "needs container runtime"
---
```

In this form, an unavailable fixture skips only that test. Suite fixture skips remain controlled by directory-level configuration.

### Container runtime helpers

The `tenzir_test.fixtures.container_runtime` module provides shared building blocks for fixtures that manage containers directly (without Docker Compose): runtime detection, detached container startup, readiness polling, and lifecycle management. Fixtures that use these helpers inherit the `container` fixture tag, so you can select their tests with `tenzir-test --fixture-tag container`.

The built-in `docker-compose` fixture has both the `container` and `docker-compose` tags. Use `tenzir-test --fixture-tag docker-compose` when you want only tests that request that fixture.

See the [create fixtures](../guides/write-tests.md#use-container-runtime-helpers) guide for a step-by-step walkthrough.

## Assertions

The `assertions` frontmatter key holds post-test validation payloads. Each top-level key inside `assertions` identifies an assertion category, and `fixtures` is the only category. The harness evaluates assertions after the test succeeds but before teardown, so resources are still live when checks run. A raised exception fails the test.

### Fixture assertions

Fixture assertions let a fixture verify what happened during the test. Declare payloads under `assertions.fixtures.<name>`:

```yaml
assertions:
  fixtures:
    http:
      expected_request:
        count: 1
        method: POST
        path: /status/not-found
        body: '{"foo":"bar"}'
```

After every successful test, the harness invokes the `assert_test` hook of each requested fixture whose `FixtureHandle` provides one. It passes these keyword arguments:

| Argument     | Description                                                                                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `test`       | The path of the test.                                                                                                                                                            |
| `assertions` | The test’s payload for this fixture, as an instance of the fixture’s assertions dataclass, or as a dict without one. An empty dict when the test has no payload for the fixture. |
| `fixture`    | The fixture’s name.                                                                                                                                                              |

Accept further keyword arguments with `**_` so that hooks keep working when the harness adds some. Because the hook also runs for tests without a payload, check for an empty mapping before reading the dataclass fields. For suite tests, the hook runs after each member rather than once at the end, and parallel suites run one hook at a time.

The [fixture guide](../guides/write-tests.md#add-fixture-assertions) walks through the full implementation.

## Environment variables

The harness recognizes the following environment variables:

* `TENZIR_TEST_ROOT` – Default test root when `--root` is omitted.
* `TENZIR_BINARY` – Override binary auto-detection. Supports multi-part commands like `TENZIR_BINARY="uvx tenzir"`. The harness adds `run` to a command that ends with the `tenzir` executable, as described in [Binary resolution](test-framework.md#binary-resolution).
* `TENZIR_WORKSPACE` – The workspace that Tenzir runs pipelines in, or `none` for none. The built-in `tenzir` and [Python runner](test-framework.md#python-runner) set it for tests with package directories, as described in [Workspaces](test-framework.md#workspaces). A value in the environment takes precedence.
* `XDG_CACHE_HOME` – Locates the package cache in `$XDG_CACHE_HOME/tenzir/packages`, where Tenzir reads [locked dependencies](test-framework.md#locked-dependencies) from.
* `TENZIR_INPUTS` – Preferred data directory. Defaults to the nearest `inputs/` directory walking up from the test, falling back to the project-level inputs folder. Reflects any `inputs:` override from `test.yaml` or frontmatter.
* `TENZIR_PACKAGE_DIRS` – Comma-separated package directories. The built-in `tenzir` and [Python runner](test-framework.md#python-runner) prepare this value for tests and fixtures as described in [Package directories](test-framework.md#package-directories). [`Executor`](test-framework.md#executor) captures it when constructed.
* `TENZIR_INPUT` – Path to the inline input file when a `.input` file exists next to the test. Not set otherwise.
* `TENZIR_STDIN` – Path to the stdin file when a `.stdin` file exists next to the test. The harness pipes this file’s content to the subprocess stdin. Not set otherwise.
* `TENZIR_KEEP_TMP_DIRS` – Keep per-test scratch directories (equivalent to `--keep`).
* `TENZIR_TEST_DEBUG` – Enable debug logging and verbose output (equivalent to `--debug`).
* `TENZIR_TEST_DISABLE_HOOKS` – Disable project hook loading and invocation (equivalent to `--no-hooks`).
* `TENZIR_TEST_DISABLE_INLINE_DEPENDENCY_INSTALL` – Disable runtime installation for inline Python dependencies declared by tests or fixtures. Equivalent to `--disable-inline-dependency-install`.

### Binary resolution

The harness automatically detects the `tenzir` binary using this precedence:

1. `TENZIR_BINARY` environment variable (highest priority)
2. Local installation found via `PATH` lookup (`shutil.which`)
3. Fallback to `uvx tenzir` when `uv` is installed

Most users can run `tenzir-test` without any configuration. When `uv` is installed, the harness automatically uses `uvx` to fetch and run Tenzir on demand.

Environment variables support multi-part commands, allowing invocations like `TENZIR_BINARY="uvx tenzir"` or `TENZIR_BINARY="docker exec box tenzir"`. The harness splits these values into argument lists using shell tokenization rules.

The harness runs pipelines with `tenzir run`, because a bare `tenzir` runs platform commands rather than pipelines. When the resolved command ends with the `tenzir` executable, the harness appends `run`. This applies to a `tenzir` on `PATH`, to the `uvx` fallback, and to a `TENZIR_BINARY` such as `uvx tenzir`, `uvx --prerelease allow tenzir`, `uvx tenzir==<version>`, or `/opt/tenzir/bin/tenzir`. Commands that already end with `run`, or that name another executable such as a wrapper script, stay as they are.

Fixtures often publish additional variables, for example `HTTP_FIXTURE_URL`.

During execution the harness also adds transient variables such as `TENZIR_TMP_DIR` so tests and fixtures can create temporary artifacts without polluting the repository. Combine it with `--keep` (or `TENZIR_KEEP_TMP_DIRS=1`) when you need to inspect the generated files after a run.

## Baselines and artifacts

Regenerate reference output whenever behavior changes intentionally:

```sh
uvx tenzir-test --update
```

`--purge` removes stale artifacts (diffs, temporary files). Keep generated `.txt` files under version control so future runs can diff against them.

The harness rewrites absolute paths in captured output, such as the ones that `tenzir` prints in diagnostics, as relative paths. Paths inside the package that owns a test are relative to that package, so a baseline stays valid whether you run the harness on the package, on its `tests` directory, or on the surrounding library. All other paths are relative to the project root.

For example, a baseline that captures a diagnostic from a test in the `microsoft` package refers to that package’s operators without the package prefix:

```text
warning: assertion failed: unsupported OCSF to ASIM mapping
  --> operators/asim/ocsf/map.tql:61:12
```

### Pre-compare transforms

Use `pre-compare` when a test produces the right events in an unpredictable order. The harness transforms the baseline and the actual output the same way, then compares the results.

`sort` is the only transform. It moves the ordering requirement out of the pipeline, so a test no longer needs a trailing `sort` operator that the package itself would never run.

Before, where the last operator exists only to make the baseline stable:

```tql
from_file "events.ndjson" {
  read_ndjson
}
summarize severity, events=count()
sort severity
```

After, where the frontmatter carries that requirement:

```tql
---
pre-compare: sort
---
from_file "events.ndjson" {
  read_ndjson
}
summarize severity, events=count()
```

`sort` orders whole events, not lines. It reads a `{` alone in the first column as the start of an event and the matching `}` in the first column as its end, which is how TQL prints events by default. Everything else counts as one unit per line, so NDJSON sorts one event per line.

Two kinds of output have no first-column braces, so `sort` shuffles their lines and destroys them. Do not use it on either one:

* Indented structured output, such as a pretty-printed JSON array.
* Multiline diagnostics, where the continuation lines sort away from the header they belong to.

`--update` writes raw output to the baseline. Transforms run at comparison time only, so the file on disk keeps the order the test produced.

## Troubleshooting

* **Missing binaries** – The harness auto-detects binaries on `PATH` and falls back to `uvx tenzir` when `uv` is installed. If neither is available, set `TENZIR_BINARY` to point at your Tenzir 7 installation.
* **Packages missing from the cache** – When a test fails because a package is not in the package cache, run `tenzir package fetch --locked` in the package directory and check the warning that the harness printed before the tests. See [Locked dependencies](test-framework.md#locked-dependencies).
* **Ignored package directories** – The tests of a package with a lock ignore `package-dirs` and `--package-dirs`. Lock the packages that its tests use as dependencies instead. See [Workspaces](test-framework.md#workspaces).
* **Unexpected exits** – Set `error: true` in frontmatter when a non-zero exit is expected.
* **Skipped tests** – Use `skip: reason` to document temporary skips; baseline files can stay empty. For fixture-dependent suites, put `skip: {on: fixture-unavailable}` in `test.yaml`. For fixtures selected by one test, use the same mapping in frontmatter. For capability-dependent suites, combine `requires` with `skip: {on: capability-unavailable}`.
* **Noisy output** – Use `--jobs 1` to serialize worker logs, and enable `--debug` (or set `TENZIR_TEST_DEBUG=1`) when you need to trace comparisons and fixture activity. Note that `--debug` automatically enables verbose output.
* **Unregistered fixtures** – The harness loads `fixtures/` from the project root only and names each fixture after its module’s file name. Run the harness from the directory that holds `fixtures/`, or pass `name=` to `@fixture()`. See [Registering fixtures](test-framework.md#registering-fixtures).

## See Also

* [Write tests](../guides/write-tests.md)
