---
title: "Write tests"
description: "Write and run tests for your pipelines and packages, with fixtures, custom runners, and project hooks when tests need more than TQL."
canonical: https://tenzir.com/docs/guides/write-tests
source: https://tenzir.com/docs/guides/write-tests.md
section: "Docs"
---

# Write tests

> Write and run tests for your pipelines and packages, with fixtures, custom runners, and project hooks when tests need more than TQL.

Tests prove that a pipeline or a package turns known input into the output you expect, and keep proving it as TQL, packages, and data change. This guide walks you through the life of a test with our `tenzir-test` harness: write a test, run it, update its baseline, and organize your tests, then extend the harness with fixtures, custom runners, and project hooks, and run everything in CI. Our [test framework reference](../reference/test-framework.md) lists every setting, flag, and API that the guide uses.

Before you begin

* Install [`uv`](https://docs.astral.sh/uv/). It runs the harness with `uvx tenzir-test` and provides the Python 3.13 that the harness requires.
* The harness runs pipelines with the `tenzir` command: the one in `TENZIR_BINARY`, else the one on your `PATH`, else `uvx tenzir`. Our reference describes the [binary resolution](../reference/test-framework.md#binary-resolution) in detail.

## Write a test

A test is a pipeline with the output it must produce stored next to it, the **baseline**. The harness runs the pipeline, compares its output with the baseline, and fails the test when the two differ. This section builds a first test from an empty directory to a committed baseline.

### Set up a project

The harness works on a **project root**: a directory with a `tests/` folder and the assets that the tests share. A package is a project root too. Its tests live in the `tests/` folder next to `package.yaml`, and the section on [testing packages](write-tests.md#test-packages) covers what’s specific to packages.

For a standalone project, create an empty directory:

```sh
mkdir demo
cd demo
```

The harness discovers tests recursively under `tests/`, so you can organize them by feature or risk level. Later sections add the optional `fixtures/`, `runners/`, and `hooks/` folders to the project root.

### Add input data

Tests read sample data from an `inputs/` folder, which the harness exposes in the `TENZIR_INPUTS` environment variable. In a package, the folder is `tests/inputs/`. Save a short NDJSON dataset of alerts as `inputs/alerts.ndjson`:

inputs/alerts.ndjson

```json
{"id": 1, "severity": 5, "message": "Disk usage above 90%"}
{"id": 2, "severity": 2, "message": "Routine backup completed"}
{"id": 3, "severity": 7, "message": "Authentication failure on admin"}
```

### Write the pipeline

Create your first test as `tests/high-severity.tql`:

tests/high-severity.tql

```tql
from_file f"{env("TENZIR_INPUTS")}/alerts.ndjson" {
  read_ndjson
}
where severity >= 5
select id, message
```

The harness also gives each test a unique scratch directory in `TENZIR_TMP_DIR`. Use it for transient files that don’t belong under version control, and pass `--keep` when you want to inspect them after the run.

### Preview the output

Before you record a baseline, look at what the pipeline produces. Passthrough mode, which `--passthrough` (`-p`) turns on, streams the output of `tenzir` to your terminal instead of comparing it:

```sh
uvx tenzir-test --passthrough tests/high-severity.tql
```

The harness still provides fixtures and environment variables and checks the exit code, but it skips comparisons, ignores `--update`, and runs one test at a time.

### Capture the baseline

When the output looks right, run the harness in update mode to write it next to the test:

```sh
uvx tenzir-test --update
```

The command produces `tests/high-severity.txt` with the captured output:

```tql
{
  id: 1,
  message: "Disk usage above 90%",
}
{
  id: 3,
  message: "Authentication failure on admin",
}
```

Review the baseline, adjust the pipeline if needed, and rerun `--update` until you’re satisfied. Commit the `.tql` test and its `.txt` baseline together. From now on, a plain [run](write-tests.md#run-tests) compares the output with this baseline.

For TQL and shell tests, the baseline records diagnostics from stderr before the output from stdout, so a test that expects a warning captures it too.

### Give a test its own input

Data that only one test uses belongs next to that test. Place a `.input` file with the test’s base name next to it, and the harness exposes its path in `TENZIR_INPUT` (singular):

* tests/

  * parsing/

    * parse-csv.input Input data
    * parse-csv.tql Test file
    * parse-csv.txt Expected baseline

tests/parsing/parse-csv.input

```csv
name,value
Alice,42
Bob,17
```

tests/parsing/parse-csv.tql

```tql
from_file env("TENZIR_INPUT") {
  read_csv
}
```

A test can use `TENZIR_INPUT` and `TENZIR_INPUTS` together when it needs a file of its own plus the shared data.

### Pipe data to stdin

Some tests read stdin rather than a file. Place a `.stdin` file next to the test, and the harness pipes its content to the test process. A TQL test can then start with a parser.

Create `tests/parsing/csv.stdin` with your test data:

tests/parsing/csv.stdin

```csv
name,count
alice,42
bob,23
```

Create `tests/parsing/csv.tql`, which reads from stdin:

tests/parsing/csv.tql

```tql
read_csv
```

Run the test with `--update` to capture the baseline:

```sh
uvx tenzir-test --update tests/parsing/csv.tql
```

The harness pipes the CSV data to the stdin of `tenzir`, so `read_csv` parses it directly. Choose a `.stdin` file or a `.input` file with `from_file`, whichever fits your test better.

Tests can also be shell scripts with the `.sh` suffix, which the `shell` runner executes with `sh -eu`. The same mechanism works for them. Create `tests/shell/echo.sh` and `tests/shell/echo.stdin`:

tests/shell/echo.sh

```sh
#!/bin/sh
cat
```

tests/shell/echo.stdin

```text
Hello from stdin!
```

A test can combine a `.stdin` file with a `.input` file. The harness pipes the stdin content to the process and exposes the input file in `TENZIR_INPUT`:

tests/shell/process.sh

```sh
#!/bin/sh
echo "from stdin:"
cat
echo "from TENZIR_INPUT:"
cat "$TENZIR_INPUT"
```

tests/shell/process.stdin

```text
stdin content
```

tests/shell/process.input

```text
input file content
```

After `--update`, the baseline holds both sources:

tests/shell/process.txt

```text
from stdin:
stdin content
from TENZIR_INPUT:
input file content
```

### Make the output deterministic

A baseline only works when every run produces the same output. Avoid timestamps and random values: use fixed input data rather than

[`now`](../reference/functions/now.md).

If the pipeline emits the right events in a varying order, as `summarize` does for its groups, add `pre-compare: sort` to the frontmatter instead of ending the pipeline with a `sort` operator, which would leave test scaffolding in the pipeline. Our reference explains how [pre-compare transforms](../reference/test-framework.md#pre-compare-transforms) order the output.

If runtime warnings are irrelevant to what a test checks, add `quiet: true` to its frontmatter to keep them out of the baseline. Leave the setting off when the warnings themselves are part of the expected output. Errors and compilation diagnostics remain visible. Our reference covers [runtime warning suppression](../reference/test-framework.md#runtime-warning-suppression) in full.

### Configure a test with frontmatter

YAML frontmatter between two `---` lines at the top of a TQL test controls how the harness runs it. Python and shell tests take the same keys as `# key: value` comments at the top of the script:

tests/slow-test.tql

```tql
---
timeout: 60
---


// Long-running test pipeline
```

Besides `timeout`, `pre-compare`, and `quiet`, the frontmatter sets the expected exit code with `error`, the runner, the fixtures a test needs, skips, and retries. The [configuration and frontmatter](../reference/test-framework.md#configuration-and-frontmatter) table in our reference lists every key with its type and default. A `test.yaml` file sets the same keys for a whole directory, as the section on [sharing settings](write-tests.md#share-settings-across-a-directory) shows.

## Test packages

A package’s tests call its operators the way your users do, so they catch a broken mapping before any configuration deploys the package. Tests are your safety net during development: change an operator, run the tests, review the diffs, and update the baselines. Start with a few key tests and expand coverage as your package grows.

### Lay out the tests

Place the tests in the `tests` folder of your package:

* vendor/

  * package.yaml

  * operators/

    * …

  * tests/

    * inputs/ Sample data that the tests share

      * auth.ndjson

    * parse.input Sample data for one test

    * parse.tql Test file

    * parse.txt Expected output baseline

    * ocsf/

      * test.yaml Suite configuration
      * 01-auth.tql First test in suite
      * 01-auth.txt
      * 02-dns.tql Second test in suite
      * 02-dns.txt

Each test consists of:

* A `.tql` file containing the test pipeline.
* An optional `.input` file with test-specific data.
* A `.txt` file with the expected output baseline.

Run `tenzir-test` from the package folder, where `package.yaml` lives, or from its `tests/` folder. The harness detects the package and switches to package mode: it loads the package’s operators, and `TENZIR_INPUTS` points to the nearest `inputs/` folder within the package, falling back to `tests/inputs/`. The harness loads `fixtures/`, `runners/`, and `hooks/` from the folder you run it from, so put them next to `package.yaml` when you run from the package folder.

### Test an operator

Test the operator your users call, not the building blocks it composes. An operator that writes into a field needs the test to lift the result:

tests/parse.tql

```tql
from_file env("TENZIR_INPUT") {
  read_lines
}
vendor::parse line, event
this = move event
```

tests/parse.input

```text
2024-01-15T10:30:00Z auth alice success
```

You can test any TQL code this way, but user-defined operators are the building blocks that others reuse, so they need tests most.

### Pin the output schema

Validate the schema your operator promises, so the baseline shows what consumers see. For OCSF, [`ocsf_cast`](../reference/functions/ocsf_cast.md) validates and [`drop_null_fields`](../reference/operators/drop_null_fields.md) keeps the baseline short:

tests/ocsf/01-auth.tql

```tql
from_file f"{env("TENZIR_INPUTS")}/auth.ndjson" {
  read_ndjson
}
vendor::ocsf::normalize
this = ocsf_cast(this)
drop_null_fields
```

Leave out what each caller decides, such as [`ocsf_derive`](../reference/functions/ocsf_derive.md), and replace non-deterministic values such as [`now`](../reference/functions/now.md). For a full package walkthrough, see [Onboard a data source](../tutorials/onboard-a-data-source.md).

### Test with different arguments

Create a separate test file for each argument combination:

tests/tag-defaults.tql

```tql
from {hash: "abc123"}
vendor::tag indicator
```

With a custom prefix:

tests/tag-with-prefix.tql

```tql
from {hash: "abc123"}
vendor::tag indicator, prefix="IOC: "
```

### Test error conditions

Set `error: true` in the frontmatter when a test must exit with a non-zero code, for example because the operator rejects its input. The baseline then captures the error diagnostic:

tests/invalid-input.tql

```tql
---
error: true
---


from {invalid: null}
vendor::strict_parse
```

### Test a package that uses other packages

When your operators call other packages, your tests need those packages too. Declare them as dependencies from your package’s folder, as our guide on [using other packages](manage-packages.md#use-other-packages) shows:

```sh
tenzir package add stix
```

The command writes the dependency to `package.yaml` and pins it in a `package.lock` next to it. Commit the lock, so that your tests use the same versions on every machine and in CI.

Then run the tests as before. For a package with a `package.lock`, the harness runs every test pipeline in the package’s own workspace, which holds your package and the packages it declares. A workspace in this sense is the folder of a `package.yaml` on your machine, as in the help text of the `tenzir package` commands, not a [workspace](../explanations/glossary.md#workspace) of deployments on the platform. Before the first test, the harness downloads every locked package that your local package cache lacks, which takes `git` and network access. To download them yourself, for example to prime a CI cache, run:

```sh
tenzir package fetch --locked
```

The tests see only the packages that your `package.yaml` declares. Package directories from `test.yaml` or `--package-dirs` don’t load for a package with a lock, so list every package your tests call under `dependencies` instead. After you edit `package.yaml` by hand, run `tenzir package lock` to bring the lock in line.

Without a `package.lock`, the harness doesn’t use a workspace, and your tests load other packages from the package directories in `test.yaml` or `--package-dirs`, as the section on [loading packages](write-tests.md#load-packages) shows. That suits a repository of packages that test against each other’s current state, such as our library. Our reference details how the harness picks the [workspace](../reference/test-framework.md#workspaces) for each test.

## Run tests

Running the tests compares every test’s output with its baseline. Run them after each change to see whether a pipeline still does what you expect.

### Run all tests

Execute all tests from the project root or the package folder:

```sh
uvx tenzir-test
```

The harness discovers the tests under `tests/`, runs them against their baselines, and returns a non-zero exit code when any output diverges. A failed comparison prints a unified diff between the baseline and the actual output.

### Choose the Tenzir binary

The harness runs each test pipeline with `tenzir run`, using the `tenzir` on your `PATH`, or `uvx tenzir` without one. To test against another Tenzir, such as the latest pre-release, name it in `TENZIR_BINARY`:

```sh
TENZIR_BINARY="uvx --prerelease allow tenzir" uvx tenzir-test
```

### Control the output

By default, the harness shows only failures, which keeps large test runs readable. Add `--verbose` to see passing and skipped tests as they complete:

```sh
uvx tenzir-test --verbose
```

Use `--debug` to see comparison targets and fixture lifecycle logs alongside the usual harness diagnostics. Debug mode also enables verbose output. In CI, set `TENZIR_TEST_DEBUG=1` instead of passing the flag.

Add `--summary` together with `--verbose` when you also want the tabular breakdown and failure tree at the end:

```sh
uvx tenzir-test --verbose --summary
```

To see raw output instead of comparisons, use the passthrough mode from the section on [previewing the output](write-tests.md#preview-the-output).

### Select tests

You don’t need to run every test while you work on one area. Select tests by path, by name, or by the fixtures they use.

#### By path

Pass individual files or directories as positional arguments, as many as you like:

```sh
uvx tenzir-test tests/alerts/high-severity.tql
uvx tenzir-test tests/alerts tests/parsing/csv.tql
```

#### By name pattern

Use `--match` (`-m`) to select tests whose path relative to the project root contains a given substring:

```sh
uvx tenzir-test --match context
```

For example, `--match mysql` matches any test whose path contains `mysql`, such as `tests/mysql/connect.tql`, the same as `--match "*mysql*"`.

Patterns containing `*`, `?`, or `[` use case-sensitive [fnmatch](https://docs.python.org/3/library/fnmatch.html) glob syntax:

```sh
uvx tenzir-test --match 'tests/*/connect.tql'
```

Multiple patterns act as an OR filter, so a test runs if it matches any of them:

```sh
uvx tenzir-test --match create --match update
```

Combine `--match` with positional paths to narrow a directory to a subset of its tests. The harness runs only tests that match both the path and a pattern:

```sh
uvx tenzir-test tests/context/ --match create
```

If a matched test belongs to a [suite](write-tests.md#group-tests-into-suites), the harness includes every test of that suite. It ignores empty and whitespace-only patterns.

#### By fixture

Use `--fixture-name` to select tests that request a [fixture](write-tests.md#create-fixtures) directly. The match is case-sensitive and uses the configured fixture name, not fixture options:

```sh
uvx tenzir-test --fixture-name mysql
uvx tenzir-test --fixture-name docker-compose
```

Use `--fixture-tag` to select tests by fixture metadata:

```sh
uvx tenzir-test --fixture-tag container
```

Fixtures get their tags from the abstractions they use. For example, fixtures that use `tenzir_test.fixtures.container_runtime` inherit the `container` tag. The built-in Docker Compose fixture has both the `container` and `docker-compose` tags:

```sh
uvx tenzir-test --fixture-tag docker-compose
```

Repeat `--fixture-name` or `--fixture-tag` to match any selected fixture name or tag. Combine fixture selectors with paths and `--match` to narrow the selection:

```sh
uvx tenzir-test tests/integrations/ --match kafka --fixture-name docker-compose
uvx tenzir-test tests/integrations/ --match kafka --fixture-tag container
```

The `--fixture` flag doesn’t select tests. It starts fixtures on their own, as the section on [running fixtures without tests](write-tests.md#run-fixtures-without-tests) shows.

### Run skipped tests

Tests that you [skip](write-tests.md#skip-tests) still need to work when their reason goes away. Pass `--run-skipped` to bypass all skip configuration and run every skipped test:

```sh
uvx tenzir-test --run-skipped
```

The flag bypasses both static skips (`skip: reason`) and conditional skips (`skip: {on: fixture-unavailable}`). Use it to verify that every skipped test still works.

To run only some skipped tests, use `--run-skipped-reason` with a pattern that matches the skip reason. The flag matches substrings and globs the same way as `--match`, and it’s repeatable:

```sh
uvx tenzir-test --run-skipped-reason maintenance
uvx tenzir-test --run-skipped-reason maintenance --run-skipped-reason '*docker*'
```

The pattern matches the displayed skip reason, which includes the `fixture unavailable:` prefix for conditional skips. For example, a suite with `skip: {on: fixture-unavailable, reason: requires docker}` has the displayed reason `fixture unavailable: requires docker`, and `--run-skipped-reason docker` matches it. When no skipped test matches, the harness prints a diagnostic so you know the patterns had no effect.

When you pass both flags, `--run-skipped` takes precedence and all skipped tests run.

### Run multiple projects

Large organizations often split tests across several repositories but still want one aggregated run. List additional project directories after `--root` and add `--all-projects` (`-a`) to run the root alongside its satellites in a single invocation:

```sh
uvx tenzir-test --root example-project --all-projects ../example-satellite
```

The root project, `example-project`, supplies the shared fixtures and runners. Satellites inherit those definitions, can register their own, and run their tests in isolation. Because the selection lists only the satellite, `--all-projects` keeps the root in scope. The harness prints how many tests each project contributes and which runners they use. Add `--verbose` to see individual results and `--summary` for the breakdown after each project. Our reference explains how [selections](../reference/test-framework.md#selections) decide which projects run.

### Load packages

When tests in a project, or in a package without a lock, call packages, point `--package-dirs` at the package directories or at a library folder that contains them. The flag is repeatable and accepts comma-separated lists:

```sh
uvx tenzir-test --package-dirs example-library
```

Here, `example-library` contains several packages, so the harness loads them all and makes sibling packages visible to each other. You can also declare package directories in a directory’s `test.yaml` with `package-dirs:`, which merge with `--package-dirs`. Tests of a package with a lock ignore both and use its [locked dependencies](write-tests.md#test-a-package-that-uses-other-packages) instead.

## Update baselines

When you change a pipeline on purpose, its output changes, and the baselines must follow. Rerun the affected tests in update mode, for all tests or for a path:

```sh
uvx tenzir-test --update tests/parse.tql
```

The harness rewrites the `.txt` files next to the tests. Review the change with `git diff` before you commit it, so that an unintended change in the output doesn’t slip into a baseline. The update writes raw output, so a [pre-compare transform](../reference/test-framework.md#pre-compare-transforms) such as `sort` applies only when the harness compares.

To remove generated artifacts from earlier runs, run `uvx tenzir-test --purge`.

## Organize tests

As a project grows, directory defaults keep its tests consistent, inputs move next to the tests that use them, and suites group tests that share setup.

### Share settings across a directory

Extract shared configuration into a `test.yaml` file. It accepts the same keys as the frontmatter and applies to every test in its directory and the directories below it:

tests/integrations/test.yaml

```yaml
fixtures: [http]
timeout: 120
# Optional: reuse datasets that live in tests/data/ instead of the project root.
inputs: ../data
```

Relative paths resolve against the directory that holds the YAML file, so `inputs: ../data` points at `tests/data/`. A child directory’s `test.yaml` and a test’s frontmatter override the inherited keys.

### Place inputs next to the tests that use them

Most tests in the [Tenzir Library](https://github.com/tenzir/library) read from a shared `inputs/` directory, because several tests exercise the same sample events through different operators. An `inputs/` directory works at any level of the test tree: the harness walks up from each test and points `TENZIR_INPUTS` at the nearest one:

* tests/

  * network/

    * inputs/ Shared by tests in network/ and below

      * packets.pcap
      * flows.json

    * tcp/

      * analysis.tql TENZIR\_INPUTS → ../inputs/

    * udp/

      * stats.tql TENZIR\_INPUTS → ../inputs/

  * inputs/ Fallback for tests without a closer inputs/

    * common.json

tests/network/tcp/analysis.tql

```tql
from_file f"{env("TENZIR_INPUTS")}/packets.pcap" {
  read_pcap
}
vendor::analyze
```

Place `inputs/` directories as close to the tests that use them as possible. This keeps related data together and makes clear which tests depend on which files. Our reference lists the full [resolution order](../reference/test-framework.md#local-inputs-directories).

### Group tests into suites

A **suite** runs the tests of a directory under one shared fixture lifecycle: the harness starts the suite’s fixtures once, runs all members, and tears the fixtures down afterwards. Declare a suite with the `suite` key in the directory’s `test.yaml`, next to the fixtures that its members share:

tests/http/test.yaml

```yaml
suite: smoke-http
fixtures: [http]
timeout: 45
retry: 2
```

By default, members run one after another in lexicographic order of their paths. To run them concurrently, use the mapping form with `mode: parallel`:

tests/http/test.yaml

```yaml
suite:
  name: parallel-http
  mode: parallel
fixtures: [http]
timeout: 30
```

Use parallel mode when tests are independent and can share fixtures at the same time, or must run at the same time, as a publisher and its subscribers do. For such suites, `min_jobs` declares how many workers the suite needs at once.

Suites follow these rules:

* Every test in the directory *and its subdirectories* joins the suite. Move tests that should stay independent into a sibling directory.
* Suite members can’t set `fixtures` or `retry` in their frontmatter, so that every member agrees on the shared lifecycle. They can override other keys, such as `timeout` or `inputs`.
* Other suites and standalone tests still run in parallel when `--jobs` allows it.

Run the directory that defines the suite when you iterate on it:

```sh
uvx tenzir-test tests/http
```

Selecting a single file inside a suite fails with a descriptive error, which keeps the fixture lifecycle predictable and prevents partial runs from leaving shared state behind. Our reference lists every rule of [suites](../reference/test-framework.md#suites), including how parallel suites claim workers.

### Skip tests

A test that can’t pass for now, or not in every environment, should skip rather than fail. To skip unconditionally, give the reason as the value of `skip`:

```yaml
---
skip: pending upstream fix
---
```

Some suites only make sense when the Tenzir build has certain operators. Declare them with `requires` in the suite’s `test.yaml`, and opt into skipping with `skip: {on: capability-unavailable}`:

tests/gcs/test.yaml

```yaml
suite: gcs-smoke
requires:
  operators: [from_google_cloud_storage]
skip:
  on: capability-unavailable
```

Before it runs the suite, the harness checks that Tenzir has each listed operator. When one is missing, it skips the suite. Without the `skip` opt-in, a missing operator fails the run.

Tests that depend on an external service can skip when its fixture isn’t available, as the section on [handling unavailable fixtures](write-tests.md#handle-unavailable-fixtures) shows. Combine both conditions when a suite depends on operators and fixtures:

```yaml
skip:
  on:
    - fixture-unavailable
    - capability-unavailable
```

Our reference covers the [skip configuration](../reference/test-framework.md#skip-configuration) and the [capability requirements](../reference/test-framework.md#capability-requirements) in detail.

### Retry flaky tests

If a test fails intermittently, for example because a service takes a while to start, add `retry` to its frontmatter so the harness reruns it before it reports a failure. The value is the **total** number of attempts:

```yaml
---
retry: 3
---
```

With `retry: 3`, the test runs up to three times. Intermediate attempts stay quiet, and the final result line includes the attempts, such as `attempts=3/3`. Treat retries as a temporary guardrail while you investigate the flake, and keep the budget small, because long retry chains mask race conditions. In a suite, set `retry` in the suite’s `test.yaml`.

## Create fixtures

Fixtures start the external resources that tests need, such as a database or an HTTP server, and expose their configuration through environment variables. This section starts with the built-in Docker Compose fixture, then builds a fixture of your own, an HTTP echo server, and extends it with options, assertions, and manual control.

### Start services with Docker Compose

When your tests need services such as databases or message brokers, the built-in `docker-compose` fixture starts them before a test or suite, waits until they are ready, exports their connection details, and tears everything down afterwards. You don’t write any fixture code for this.

#### Describe the services

Place a `compose.yaml` next to your test or next to the `test.yaml` of its suite:

tests/docker-compose/compose.yaml

```yaml
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 1s
      timeout: 3s
      retries: 30
```

Publish ports without a fixed host binding (`"6379"` instead of `"6379:6379"`) so that the fixture discovers the dynamically assigned host port.

#### Request the fixture

Reference the Compose file and select the services to start:

tests/docker-compose/test.yaml

```yaml
suite: docker-compose-demo
fixtures:
  - docker-compose:
      file: compose.yaml
      services: [redis]
      wait:
        timeout_seconds: 90
skip:
  on: fixture-unavailable
  reason: requires docker compose
```

The `skip` entry makes the suite skip cleanly on machines without Docker Compose instead of failing.

#### Read the connection details

The fixture exports environment variables for each service. For a service named `redis` that publishes port 6379, it sets `DOCKER_COMPOSE_SERVICE_REDIS_HOST` to `127.0.0.1` and `DOCKER_COMPOSE_SERVICE_REDIS_PORT_6379_TCP` to the assigned host port. When a service publishes exactly one port, the shorthand `DOCKER_COMPOSE_SERVICE_REDIS_PORT` is also available. A shell test can check them:

tests/docker-compose/check.sh

```sh
#!/bin/sh
set -eu


: "${DOCKER_COMPOSE_PROVIDER:?}"
: "${DOCKER_COMPOSE_PROJECT_NAME:?}"
: "${DOCKER_COMPOSE_FILE:?}"
: "${DOCKER_COMPOSE_SERVICE_REDIS_CONTAINER_ID:?}"
: "${DOCKER_COMPOSE_SERVICE_REDIS_HOST:?}"
: "${DOCKER_COMPOSE_SERVICE_REDIS_PORT_6379_TCP:?}"
: "${DOCKER_COMPOSE_SERVICE_REDIS_PORT:?}"


echo "docker-compose fixture ok"
```

A TQL test reads them with `env`:

```tql
from {
  host: env("DOCKER_COMPOSE_SERVICE_REDIS_HOST"),
  port: env("DOCKER_COMPOSE_SERVICE_REDIS_PORT_6379_TCP"),
  shorthand: env("DOCKER_COMPOSE_SERVICE_REDIS_PORT"),
}
```

```tql
{
  host: "127.0.0.1",
  port: "49152", // dynamically assigned
  shorthand: "49152",
}
```

Our reference on the [built-in docker-compose fixture](../reference/test-framework.md#built-in-docker-compose-fixture) lists all options, the readiness detection, and every exported variable.

### Register a fixture

Your own fixtures live in a `fixtures/` package at the project root. The harness imports `fixtures/__init__.py` on startup, and each module you import there registers its fixtures:

fixtures/\_\_init\_\_.py

```python
from . import http  # noqa: F401  (side effect: register fixture)
```

### Implement a fixture

A fixture is a generator decorated with `@fixture()`. It sets up a resource, yields a dictionary of environment variables for the tests, and cleans up in a `finally` block. Here is a minimal HTTP echo server:

fixtures/http.py

```python
from tenzir_test import fixture


@fixture()
def http():
    server = start_echo_server()          # your setup logic
    try:
        yield {"HTTP_FIXTURE_URL": server.url}  # expose to tests
    finally:
        server.shutdown()                 # always clean up
```

The harness calls the generator once per fixture activation. Everything before `yield` is setup, the dictionary becomes environment variables, and the `finally` block runs whether the test passes or fails. The fixture’s name defaults to its module’s file name, `http` here; pass `name=` to `@fixture()` to choose another.

### Use the fixture in a test

Request a fixture by name in the test’s frontmatter. The harness starts it before the test runs and exports its environment variables. Create `tests/http/echo.tql`, which sends an event to the echo server and parses the response:

tests/http/echo.tql

```tql
---
fixtures: [http]
timeout: 10
---


from {x: 42, y: "foo"}
each {
  from_http env("HTTP_FIXTURE_URL"), body=$this {
    read_json
  }
}
```

Because the test talks to a server, it also sets a short timeout. The fixture starts the server before the test and tears it down after the run.

### Capture the fixture’s baseline

Run the harness in update mode to record the expected output:

```sh
uvx tenzir-test --update tests/http/echo.tql
```

This creates `tests/http/echo.txt` with the server’s response. Later runs compare the live output with this baseline. Add `--debug` to see the fixture’s lifecycle logs.

### Share a fixture across a suite

By default, each test gets its own fixture lifecycle. To start the server once for all tests in `tests/http/`, turn the directory into a suite and move the fixture into its `test.yaml`:

tests/http/test.yaml

```yaml
suite: smoke-http
fixtures: [http]
timeout: 45
```

The members then drop `fixtures` from their frontmatter, and you run the suite as a directory, as the section on [grouping tests into suites](write-tests.md#group-tests-into-suites) describes.

### Handle unavailable fixtures

Fixtures that depend on external tools, such as a container runtime or a cloud CLI, should raise `FixtureUnavailable` when the dependency is missing:

fixtures/mysql.py

```python
import shutil


from tenzir_test.fixtures import FixtureUnavailable, fixture


@fixture()
def mysql():
    if not shutil.which("docker"):
        raise FixtureUnavailable("docker not found")
    # ...
```

By default, this fails the test. To turn a suite fixture failure into a skip, add a structured `skip` entry to the suite’s `test.yaml`:

```yaml
suite: mysql-integration
fixtures: [mysql]
skip:
  on: fixture-unavailable
```

The harness then marks every test in the suite as skipped and includes the exception message in the output. This opt-in design keeps suites failing loudly by default, so you only suppress the failure where the missing dependency is expected.

If one test selects the fixture directly, put the same skip mapping in that test’s frontmatter instead:

```yaml
---
fixtures: [mysql]
skip:
  on: fixture-unavailable
---
```

An unavailable fixture then skips only that test. Frontmatter can’t control suite fixture setup, because suite fixtures start before any member test runs.

### Declare Python dependencies

Fixture modules can declare Python package dependencies with PEP 723 script metadata. Use this when a fixture imports packages that aren’t part of `tenzir-test` itself:

fixtures/localstack.py

```python
# /// script
# dependencies = ["boto3"]
# ///


from tenzir_test import fixture


@fixture()
def localstack():
    ...
```

When a fixture file declares dependencies, `tenzir-test` installs the missing packages into the active Python environment with `uv` before it imports the project’s fixtures:

```sh
uv pip install --python <current-python> boto3
```

If a bare dependency name, such as `boto3`, is already installed, the harness reuses it instead of running `uv pip install`. Versioned requirements, such as `boto3>=1.34`, still go through `uv` so that the requested version holds.

This works for `fixtures.py` and for any Python module under `fixtures/`, including nested modules that `fixtures/__init__.py` imports. It also applies when you [run fixtures without tests](write-tests.md#run-fixtures-without-tests), such as with `uvx tenzir-test --fixture localstack`.

Make sure `uv` is on `PATH` when fixture files declare dependencies. If a fixture imports an undeclared package, `tenzir-test` reports the missing dependency and suggests running the harness from a project environment or with `uvx --with`.

Pass `--disable-inline-dependency-install`, or set `TENZIR_TEST_DISABLE_INLINE_DEPENDENCY_INSTALL=1`, when another tool, such as Nix, provides all fixture dependencies and `tenzir-test` shouldn’t install packages at runtime. The harness still reads the dependency metadata, but fixture imports fail if a dependency isn’t actually available.

### Use container runtime helpers

When a fixture manages a single container directly rather than orchestrating services through Docker Compose, the `tenzir_test.fixtures.container_runtime` module handles the repetitive parts: finding a runtime, running containers, polling for readiness, and tearing down. A container-backed fixture follows four steps:

1. **Detect the runtime.** The `detect_runtime()` function probes the system for Podman first, then Docker, and returns a `RuntimeSpec`. When it finds no runtime, it returns `None`. Raise `FixtureUnavailable` then, so that the suite can [skip](write-tests.md#handle-unavailable-fixtures).

2. **Start the container.** The `start_detached(runtime, args)` function runs `<runtime> run -d` and returns a `ManagedContainer` handle. Pass the same flags you would use on the command line, such as port mappings, environment variables, and the image name.

3. **Wait for readiness.** The `wait_until_ready(probe, ...)` function calls your probe repeatedly until it returns `(True, observation)`. On timeout, it raises `ContainerReadinessTimeout` with the context string and the last observation, so you can tell *why* the service didn’t come up.

4. **Clean up.** Call `container.stop()` in a `finally` block. The `ManagedContainer` handle also offers `exec()`, `inspect_json()`, `is_running()`, and `copy_from()` for anything you need during the test.

The [`container.py`](https://github.com/tenzir/test/blob/main/example-project/fixtures/container.py) fixture of the example project in the `tenzir-test` repository applies the pattern end to end. Fixtures that use these helpers carry the `container` tag, so `--fixture-tag container` selects their tests.

### Add structured options

When a fixture needs runtime configuration, such as a custom port, a TLS toggle, or a database name, declare a frozen dataclass and pass it to `@fixture()`:

fixtures/http.py

```python
from dataclasses import dataclass
from tenzir_test import current_options, fixture


@dataclass(frozen=True)
class HttpOptions:
    port: int = 0


@fixture(options=HttpOptions)
def http():
    opts = current_options("http")
    server = start_echo_server(port=opts.port)
    # ...
```

Every field needs a default, so that bare requests such as `fixtures: [http]` keep working. Test authors provide values with a mapping in `test.yaml` or the frontmatter:

```yaml
fixtures:
  - http:
      port: 9090
```

The harness constructs the dataclass from the YAML mapping. Nested dataclasses work too, because the harness walks the type annotations recursively. Our reference covers the [fixture options](../reference/test-framework.md#fixture-options).

### Add fixture assertions

A test’s baseline captures what the pipeline printed, not what it did to the outside world. Fixture assertions close that gap: after a test succeeds and before teardown, the fixture checks what happened during the test, such as the requests that the server received. The fixture declares an assertions dataclass and an `assert_test` hook, and each test states what it expects.

#### Declare the assertions dataclass

Define a frozen dataclass that describes the expected shape. Nested dataclasses work the same way as for options:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class ExpectedRequest:
    count: int = 1
    method: str = "POST"
    path: str = "/"
    body: str = ""


@dataclass(frozen=True)
class HttpAssertions:
    expected_request: ExpectedRequest | None = None
```

#### Register assertions with the fixture

Pass the dataclass to `@fixture(assertions=...)` and return a `FixtureHandle` whose hooks include `assert_test`:

fixtures/http.py

```python
from pathlib import Path
from typing import Any


from tenzir_test import FixtureHandle, current_options, fixture


@fixture(options=HttpOptions, assertions=HttpAssertions)
def http() -> FixtureHandle:
    opts = current_options("http")
    server = start_echo_server(port=opts.port)


    def _assert_test(
        *, test: Path, assertions: HttpAssertions | dict[str, Any], **_: Any
    ) -> None:
        # A test without a payload for this fixture passes an empty mapping.
        if not isinstance(assertions, HttpAssertions):
            return
        if assertions.expected_request is None:
            return
        observed = server.get_request_log()
        expected = assertions.expected_request
        if len(observed) != expected.count:
            raise AssertionError(
                f"expected {expected.count} request(s), got {len(observed)}"
            )
        # ... validate method, path, body ...


    return FixtureHandle(
        env={"HTTP_FIXTURE_URL": server.url},
        teardown=server.shutdown,
        hooks={"assert_test": _assert_test},
    )
```

The hook runs after every successful test that requests the fixture, with the keyword arguments `test`, `assertions`, and `fixture`. When it raises an exception, the harness reports the test as failed. Our reference lists the [fixture API](../reference/test-framework.md#fixture-api), including the fields of `FixtureHandle` and the arguments of `assert_test`.

#### Write assertion payloads in test frontmatter

Test authors declare what they expect under `assertions.fixtures.<name>`:

```yaml
---
fixtures: [http]
assertions:
  fixtures:
    http:
      expected_request:
        count: 1
        method: POST
        path: /status/not-found
        body: '{"foo":"bar"}'
---
```

The harness constructs an `HttpAssertions` instance from the payload and passes it to the hook. Inside the fixture, `current_assertions("http")` returns the same instance. Our reference covers [fixture assertions](../reference/test-framework.md#fixture-assertions) in suites.

### Control fixtures from Python tests

The declarative `fixtures: [http]` covers most cases. When a test needs to start, stop, or restart a fixture itself, for example to simulate a crash, write it in Python. A `.py` file under `tests/` runs with the `python` runner, which preloads helpers such as `acquire_fixture`, `Executor`, and `fixtures` and registers the project’s fixtures, so the test needs no imports:

tests/python/manual-http.py

```python
# timeout: 20


# Context-manager style: `with` calls start() on enter and stop() on exit.
with acquire_fixture("http") as http:
    url = http.env["HTTP_FIXTURE_URL"]
    result = Executor().run(
        f'from {{x: 1}} | each {{ from_http "{url}", body=$this {{ read_json }} }}'
    )
    print(result.stdout.decode(), end="")


# Manual style: start and stop a fresh instance yourself.
http.start()
print(http.env["HTTP_FIXTURE_URL"].startswith("http://"))
http.stop()
```

The `acquire_fixture()` function returns a controller for the registered fixture. Its `start()` method enters the fixture and stores the environment mapping in `env`, and `stop()` runs the cleanup. Use the context manager when a single lifecycle suffices, or call `start()` and `stop()` yourself when you need several cycles.

Fixtures can offer extra operations to such tests, such as a `kill()` for fault injection. Return a `FixtureHandle` with named hooks:

fixtures/server.py

```python
from signal import SIGTERM


from tenzir_test import FixtureHandle, fixture


@fixture()
def server():
    process = _start_server()
    return FixtureHandle(
        env=_make_env(process),
        teardown=lambda: process.terminate(),
        hooks={"kill": lambda sig=SIGTERM: process.send_signal(sig)},
    )
```

Tests call the hooks as methods of the running controller. Assert their presence so that tests fail immediately when the contract changes:

```python
import signal


server = acquire_fixture("server")
server.start()
assert hasattr(server, "kill")
server.kill(signal.SIGKILL)
server.stop()
```

## Run fixtures without tests

Sometimes you want the service a fixture manages, such as a database, a message broker, or an HTTP server, without running any tests: to develop a pipeline against it, or to debug it. The standalone fixture mode starts fixtures and keeps them running until you stop them.

### Start a fixture

Pass `--fixture` with the fixture name:

```sh
uvx tenzir-test --fixture mysql
```

The harness discovers the project’s fixtures, activates the one you requested, prints the environment variables it exports, and blocks until you interrupt it:

```text
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

Copy these values into another terminal session or pass them to an external tool.

### Pass options to a fixture

Fixtures with [structured options](write-tests.md#add-structured-options) accept them as a YAML mapping after the fixture name:

```sh
uvx tenzir-test --fixture 'kafka: {port: 9092}'
```

The syntax matches the `fixtures:` key of a test. A bare name uses the fixture’s default options, and the mapping overrides specific fields.

### Start multiple fixtures

The `--fixture` flag is repeatable:

```sh
uvx tenzir-test --fixture mysql --fixture redis
```

All requested fixtures start together, and the harness prints their combined environment variables, sorted by key.

Combine with other flags

Several flags of a regular test run also work in fixture mode:

* `--debug` logs the fixture lifecycle, including startup and health-check details.
* `--keep` (`-k`) preserves temporary directories after shutdown, so you can inspect state or log files that a fixture wrote.
* `--package-dirs` passes package directories to the fixture environment in `TENZIR_PACKAGE_DIRS`, so fixtures that run Tenzir find the right packages.

```sh
uvx tenzir-test --fixture mysql --debug --keep
```

### Shut down

Press **Ctrl+C** or send `SIGTERM` to stop. The harness tears the fixtures down in reverse order, as it does after a regular test run, and removes temporary directories unless you passed `--keep`.

Note

You can’t combine `--fixture` with test paths. To run a specific test with a fixture, request the fixture in its frontmatter or `test.yaml` instead.

## Add custom runners

Runners tell `tenzir-test` how to execute a discovered file. The built-in runners cover TQL, Python, and shell tests. This section adds the `xxd` runner from our example project, which compares binary artifacts by dumping their hexadecimal representation with the [`xxd`](https://man.archlinux.org/man/xxd.1.en) utility that ships with most platforms.

### Prepare the runners package

Create `runners/__init__.py` in the project root if it doesn’t exist yet. The harness imports this module on startup.

```sh
mkdir -p runners
touch runners/__init__.py
```

### Implement the runner

Copy the runner from the example project and keep it under version control so that teammates use the same convention. The latest reference implementation lives in [example-project/runners/xxd.py](https://github.com/tenzir/test/blob/main/example-project/runners/xxd.py).

To start from a scaffold instead, save the following template as `runners/xxd.py` and adapt the `TODO` notes, for example when you call a different tool or emit more artifacts:

runners/xxd.py

```python
from __future__ import annotations


from pathlib import Path


from tenzir_test import runners
from tenzir_test.runners._utils import get_run_module


class XxdRunner(runners.ExtRunner):
    """Hexdump runner that turns *.xxd files into reference artifacts."""


    def __init__(self) -> None:
        super().__init__(name="xxd", ext="xxd")


    def run(self, test: Path, update: bool, coverage: bool = False) -> bool:
        del coverage  # this runner does not integrate with LLVM coverage


        run_mod = get_run_module()
        passthrough = run_mod.is_passthrough_enabled()


        # 1. Prepare the command. Adjust flags or the executable for your tool.
        cmd = ["xxd", "-g1", str(test)]
        # TODO: Replace "xxd" or tweak arguments when you wrap a different command.


        try:
            completed = run_mod.run_subprocess(
                cmd,
                capture_output=not passthrough,
            )
        except FileNotFoundError:
            run_mod.report_failure(test, "└─▶ xxd is not available on PATH")
            return False


        if completed.returncode != 0:
            # 2. Surface a readable error message and bail out early.
            run_mod.report_failure(test, f"└─▶ xxd exited with {completed.returncode}")
            return False


        if passthrough:
            # 3. Passthrough runs stop after executing the command.
            run_mod.success(test)
            return True


        output = completed.stdout or b""


        # 4. Update reference artifacts when requested.
        ref_path = test.with_suffix(".txt")
        if update:
            ref_path.write_bytes(output)
            run_mod.success(test)
            return True


        if not ref_path.exists():
            run_mod.report_failure(test, f"└─▶ Missing reference file {ref_path}")
            return False


        # 5. Compare against the baseline and print a diff on mismatch.
        expected = ref_path.read_bytes()
        if expected != output:
            run_mod.report_failure(test, "")
            run_mod.print_diff(expected, output, ref_path)
            return False


        run_mod.success(test)
        return True


runners.register(XxdRunner())
```

The runner claims the `.xxd` extension, and its `run()` method returns whether the test passed. Our reference lists the [runner API](../reference/test-framework.md#runner-api), including the helpers that the template calls.

Finally, import the runner in `runners/__init__.py` so that the harness registers it on startup:

runners/\_\_init\_\_.py

```python
"""Project runners."""


# Import bundled runners so they register on package import.
from . import xxd  # noqa: F401


__all__ = ["xxd"]
```

### Add a hexdump test

Create a directory for the new tests and add a sample input string:

```sh
mkdir -p tests/hex
cat <<EOD > tests/hex/hello.xxd
Hello Tenzir!
EOD
```

### Capture the hexdump baseline

Run the harness in update mode so that it writes the expected hexdump next to the `.xxd` file:

```sh
uvx tenzir-test --update
```

The command produces `tests/hex/hello.txt`, similar to the following snippet:

```text
00000000: 48 65 6c 6c 6f 20 54 65 6e 7a 69 72 21 0a        Hello Tenzir!.
```

Later runs without `--update` rerun `xxd` and compare the fresh dump with the stored baseline. Pass `--debug` to see runner details together with the comparison activity.

### Share the runner across projects

Keep the runner in your template repository or internal tooling so that other projects can copy it verbatim. Use `runners.register_alias("xxd-hexdump", "xxd")` when you prefer a more descriptive name in frontmatter.

In a [run of multiple projects](write-tests.md#run-multiple-projects), the root project’s runners load first, and satellites reuse them. That keeps shared runners like `xxd` in a central project while satellite projects focus on their own tests.

## Configure project hooks

Project hooks run your Python code at fixed points of a test run, for setup and cleanup that belongs next to your tests: choosing a local Tenzir build before discovery, setting environment variables for one project, or collecting artifacts from failed tests.

### Choose a hook location

Create a `hooks/` package at the project root:

```sh
mkdir -p hooks
touch hooks/__init__.py
```

The harness also supports a single `hooks.py` file at the project root. Use one form per project; when both exist, the harness loads only the package. It doesn’t load hooks from nested directories such as `tests/foo/hooks/`.

### Select local Tenzir binaries before discovery

Use a `startup` hook when your project chooses `tenzir` before the harness resolves executables, for example to run tests against a local build instead of the binaries on `PATH`. Add the following hook to `hooks/__init__.py`:

hooks/\_\_init\_\_.py

```python
import subprocess
from pathlib import Path


from tenzir_test import hooks


@hooks.startup
def use_local_tenzir_build(ctx):
    # Use ctx.root to resolve paths from the invocation root.
    build_script = ctx.root / "scripts" / "build.sh"


    # Run helper commands with ctx.env so earlier hook changes apply.
    build_dir = Path(
        subprocess.check_output(
            [build_script, "--print-build-dir"],
            cwd=ctx.root,
            env=ctx.env,
            text=True,
        ).strip()
    )
    if not build_dir.is_absolute():
        build_dir = ctx.root / build_dir


    # ctx.path is a plain list that becomes PATH after the hook returns.
    bin_dir = build_dir / "bin"
    ctx.path.insert(0, str(bin_dir))


    # Mutate ctx.env for variables that tenzir-test should apply globally.
    # The harness appends `run`, because the command ends with `tenzir`.
    ctx.env["TENZIR_BINARY"] = str(bin_dir / "tenzir")


    # Use ctx.debug to emit optional diagnostics only in debug mode.
    if ctx.debug:
        print(f"using Tenzir binaries from {bin_dir}")
```

This example uses the `ctx` object to:

* Resolve project-local paths with `ctx.root`.
* Run a helper command with `subprocess.check_output()` and `ctx.env`.
* Update `PATH` by editing the plain `ctx.path` list.
* Set global environment variables through `ctx.env`.
* Print extra details only when `ctx.debug` is enabled.

Run the tests as usual:

```sh
uvx tenzir-test
```

The `startup` hook runs before settings and binary discovery, so changes to `ctx.env`, `ctx.path`, and `TENZIR_BINARY` affect the whole invocation. Edit `ctx.path` instead of `ctx.env["PATH"]`, which the harness rejects.

### Set environment variables for one project

Use `project_start` for environment values that apply only to the tests of the current project:

hooks/\_\_init\_\_.py

```python
from tenzir_test import hooks


@hooks.project_start
def configure_project(ctx):
    ctx.env["TENZIR_TEST_DATASET"] = ctx.project.root.name
```

The mapping in `ctx.env` and the list in `ctx.path` belong to this project. Changes apply to its tests and don’t leak into the next project of a run with multiple projects.

### Collect failed-test artifacts

Use `test_failure` to copy files from the test’s scratch directory before the harness removes it:

hooks/\_\_init\_\_.py

```python
import shutil


from tenzir_test import hooks


@hooks.test_failure
def save_failure_artifacts(ctx):
    if ctx.tmp_dir is None:
        return
    relative_test = ctx.test.relative_to(ctx.project.root).with_suffix("")
    target = ctx.project.root / ".tenzir-test-failures" / relative_test
    shutil.copytree(ctx.tmp_dir, target, dirs_exist_ok=True)
    print(f"saved failure artifacts to {target}")
```

This hook runs after `test_finish` and only for final failures, not for intermediate retry attempts. Our reference lists the [hook events](../reference/test-framework.md#hooks) and the attributes of `ctx` for each one.

Hook ordering

In a run of multiple projects, root hooks wrap satellite hooks: start events run from the root to the satellite, and finish and failure events run from the satellite back to the root. For a satellite test, the order is:

```text
root.project_start
satellite.project_start
root.test_start
satellite.test_start
run test
satellite.test_finish
root.test_finish
satellite.test_failure  # failed tests only
root.test_failure       # failed tests only
satellite.project_finish
root.project_finish
```

Only the invocation root’s `startup` and `shutdown` hooks run. A satellite’s `startup` hook runs only when you run that satellite as the root.

Disable hooks during recovery

If a hook keeps the harness from starting, disable hooks for one invocation:

```sh
uvx tenzir-test --no-hooks
```

In scripts or CI, set the environment variable instead:

```sh
TENZIR_TEST_DISABLE_HOOKS=1 uvx tenzir-test
```

## Run tests in CI

Once the tests pass locally, run them on every pull request, so that a change that breaks a pipeline never reaches the main branch.

### Set up the job

A CI job needs little more than `uv`:

* Install `uv`, for example with [`astral-sh/setup-uv`](https://github.com/astral-sh/setup-uv), and ask it for Python 3.13, which the harness requires.
* Run `uvx tenzir-test`. You don’t need to install Tenzir separately: without a `tenzir` on `PATH`, the harness falls back to `uvx tenzir`. Set `TENZIR_BINARY` to test against another build, such as `uvx --prerelease allow tenzir` for the next release.
* Let the job reach GitHub. Before the tests of a package with a lock, the harness fetches the locked packages with `git`, which needs network access but no sign-in.
* Cache `~/.cache/tenzir/packages` keyed on your `package.lock` files, so that runs don’t download the same packages again.

In a GitHub Actions workflow, these steps look like this:

.github/workflows/test.yml

```yaml
steps:
  - name: Check out repository
    uses: actions/checkout@v4


  - name: Install uv
    uses: astral-sh/setup-uv@v5
    with:
      python-version: "3.13"


  - name: Cache locked packages
    uses: actions/cache@v4
    with:
      path: ~/.cache/tenzir/packages
      key: tenzir-packages-${{ hashFiles('**/package.lock') }}


  - name: Run tests
    run: uvx tenzir-test --root .
```

Our guide on managing packages shows the complete workflow for [testing packages in CI](manage-packages.md#test-packages-in-ci), including a second run against the Tenzir pre-release. For reproducible results, keep your datasets small and deterministic, and prefer fixtures that wipe state between runs.

### Export CI reports

Write a structured report when you need CI to identify failed tests without searching terminal logs. Run the command from the checkout root so that paths in the report match files in your repository:

```sh
uvx tenzir-test --root . --report-json artifacts/tests.json
```

The report includes final outcomes, failed test paths, diagnostics, and plain diffs. It also records skipped tests and harness-level errors. Keep the raw log as a companion artifact, because the harness truncates long diagnostic fields.

Upload the report even when the test step fails:

```yaml
- name: Run integration tests
  run: uvx tenzir-test --root . --report-json artifacts/tests.json
- name: Upload test reports
  if: always()
  uses: actions/upload-artifact@v7
  with:
    name: test-results
    path: artifacts/tests.json
```

Your CI wrapper can use the report to publish test summaries and source-file annotations. The harness doesn’t create those itself.

If tests run inside a build sandbox that can’t export a report file, use `--report-json -` instead. This emits tagged JSON records alongside the normal log, so the wrapper can retain partial results as tests finish. Treat a missing completion record as an incomplete run, not a success. Our reference on [structured reports](../reference/test-framework.md#structured-reports) describes the schema, the stream protocol, path validation, and diagnostic limits.

## Troubleshoot tests

### Test fails with “file not found”

Verify that the `.input` file exists next to the test file with the same base name. Check that you use `env("TENZIR_INPUT")` (singular) for a test’s own input and `env("TENZIR_INPUTS")` (plural) for the shared folder.

### Output differs between runs

Tests must produce deterministic output. Follow the section on [making the output deterministic](write-tests.md#make-the-output-deterministic): fix the input data and use `pre-compare: sort` when only the order varies.

### Baseline mismatch after changes

Run `uvx tenzir-test --update` to regenerate baselines after intentional changes, and review the diff to verify that the changes are expected, as the section on [updating baselines](write-tests.md#update-baselines) describes.

### A package is not in the package cache

The harness couldn’t download a locked package. Check that `git` is installed and the network reaches GitHub, then run `tenzir package fetch --locked` in your package’s folder to see the error. If the command reports that `package.lock` doesn’t match `package.yaml`, run `tenzir package lock` first.

### An operator of another package is unknown

Your tests see only the packages that your `package.yaml` declares. Add the package with `tenzir package add`, even if one of your dependencies already uses it.

### A fixture is not registered

The harness loads fixtures from the `fixtures/` folder of the directory you run it from, and names each one after its module’s file name unless you pass `name=` to `@fixture()`. Run the harness from the project root or package folder, and check that `fixtures/__init__.py` imports the module.

## See also

* [Manage packages](manage-packages.md)
* [Test Framework](../reference/test-framework.md)
* [Onboard a data source](../tutorials/onboard-a-data-source.md)
