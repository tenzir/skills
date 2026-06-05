---
name: tenzir-manage-packages
description: >-
  Manage Tenzir packages across the full lifecycle: add new packages, inspect
  existing packages, update manifests, extend or remove package capabilities,
  refactor user-defined operators, maintain tests and examples, configure
  inputs and contexts, ship deployable pipelines, publish packages, and retire
  obsolete package surfaces. Use when the user is working in the context of a
  Tenzir package or wants to organize reusable capabilities as a package.
metadata:
  requires:
    skills:
      - tenzir-docs
  uses:
    skills:
      - name: tenzir-ship
        when: Package changelog entries, release notes, or publishing workflows are in scope.
---

# Manage Tenzir packages

Use this skill as the package-lifecycle entry point into the `tenzir-docs`
skill. Start by identifying the lifecycle task, load the relevant docs set, and
select the branches that match the user's request. Keep package changes coherent
across manifest entries, operators, pipelines, examples, tests, contexts, and
changelog entries.

Package work includes scaffolding packages, changing manifests, adding or
removing UDOs, managing contexts, pipelines, examples, and tests, publishing
packages, and retiring obsolete capabilities.

## Triage

Identify the package's purpose, intended users, and reusable capabilities.
Determine the lifecycle task: add, inspect, update, extend, refactor,
deprecate, remove, test, publish, or migrate a package capability.

Use `tenzir-docs` as the primary source for implementation guidance. Read the
relevant set of package pages that covers the selected lifecycle branches.

Routing:

- Package foundation:
  - Package model and design: `explanations/packages.md`,
    `tutorials/write-a-package.md`
  - New package or scaffold repair: `guides/packages/create-a-package.md`
- Manifest and installation:
  - Installation behavior: `guides/packages/install-a-package.md`
  - Inputs and configuration: `guides/packages/configure-inputs.md`
  - Context declarations: `guides/packages/add-contexts.md`
- Package surfaces:
  - User-defined operators: `guides/packages/add-operators.md`
  - Deployable pipelines: `guides/packages/add-pipelines.md`
  - Package tests: `guides/packages/test-packages.md`,
    `guides/testing/run-tests.md`, `guides/testing/write-tests.md`
- Review and release:
  - Changelog entries: `guides/packages/maintain-a-changelog.md`
  - Publishing: `guides/packages/publish-a-package.md`

## Lifecycle branches

Select the branches that match the task. Use each branch's results as exit
criteria for that part of the work.

### Create or reconcile package structure

Set up or reconcile the package as a complete contribution unit. Keep package
IDs stable, short, and lowercase. Use the repository's existing package naming
and directory style. When removing or deprecating capabilities, retire the
manifest entries, directories, tests, examples, pipelines, and changelog
references that belong to that capability together.

**Results:**

- `package.yaml` with `id`, `name`, author metadata, icon, Markdown
  description, valid categories, opaque `metadata`, inputs, and contexts where
  needed
- Standard directories as needed: `operators/`, `examples/`, `pipelines/`,
  `tests/`, and `changelog/`
- Renamed, moved, or removed capabilities retire their stale package entries
- Test samples stored close to the tests that use them: inline `.input` files
  for single-test fixtures and local `inputs/` directories for shared fixtures

**Docs resources**:

- `guides/packages/create-a-package.md`
- `guides/packages/configure-inputs.md`
- `guides/packages/add-contexts.md`

### Manage manifest, inputs, and contexts

Use this branch when changing package metadata, categories, installation
behavior, user-configurable inputs, or contexts. Keep manifest entries aligned
with the operators and pipelines that consume them. Prefer package inputs for
user-specific URLs, credentials, intervals, topics, destinations, and other
deployment-time values.

**Results:**

- Manifest categories, metadata, inputs, and contexts match the package's
  current capabilities
- Inputs are referenced by the operators or pipelines that need user-provided
  values
- Context definitions are paired with the operators, pipelines, examples, and
  tests that populate or query them
- Removed capabilities retire their unused manifest inputs, contexts, and
  install behavior

**Docs resources**:

- `guides/packages/configure-inputs.md`
- `guides/packages/add-contexts.md`
- `guides/packages/install-a-package.md`

### Manage UDOs and reusable capabilities

Treat UDOs as the package's reusable public API. Add, update, refactor,
deprecate, or remove operator files as package capabilities. Choose names from
stable user-facing semantics and the package directory structure rather than
from one-off pipeline names.

Add operator frontmatter arguments for configurable fields, URLs, credentials,
modes, output topics, and destinations. Preserve existing public operator names
unless a rename is intentional and reflected in examples, pipelines, tests, and
changelog entries. Use `tenzir-docs` for operator-body behavior when the user
asks for implementation details.

**Results:**

- UDOs under `operators/` with clear names and descriptions
- Field and value parameters for reusable behavior
- Compatibility decisions documented in code, tests, or changelog entries where
  user-facing behavior changes
- Tests for each public operator and important argument combination

### Manage deployable pipelines

Use `pipelines/` for complete deployable workflows with an input and an output.
Pipelines should orchestrate package UDOs instead of embedding reusable
transformation logic.

Ship operational pipelines as disabled by default unless the package is
intentionally an always-on feed or context updater. Use `restart-on-error` for
long-running or periodic workflows where restart behavior is desirable.

**Results:**

- Pipelines with frontmatter `name` and `description`
- Optional operational pipelines marked `disabled: true`
- Package inputs used for user-specific URLs, credentials, intervals, topics,
  and destinations
- Pipelines that compose UDOs and publish, update contexts, or export
  to destinations
- Deployable pipelines reference current UDO names after removals or renames

**Docs resources**:

- `guides/packages/add-pipelines.md`
- `guides/packages/configure-inputs.md`

### Manage examples

Use `examples/` for focused runnable snippets that teach users how to use the
package. Examples should demonstrate one package surface at a time, such as
invoking a UDO, configuring an input, using a context, or running a pipeline.

Keep examples separate from tests and deployable pipelines. Make them
self-contained and easy to adapt after package installation.

**Results:**

- Examples with frontmatter `name` and `description`
- One primary example for the package's core use case
- Additional examples for important variants or integrations
- Examples updated or removed when public package capabilities change

**Docs resources**:

- `guides/packages/create-a-package.md`
- `guides/packages/add-operators.md`
- `guides/packages/add-pipelines.md`

### Manage tests

Use this branch when adding, updating, or removing public package behavior.
Tests should cover public operators, important argument combinations, context
behavior, and examples that encode user-facing contracts. Keep fixtures close to
the tests that use them.

**Results:**

- Public operators and important configuration paths have deterministic tests
- Fixtures use inline `.input` files for single-test samples and local `inputs/`
  directories for shared samples
- Tests, fixtures, and expected outputs reflect renamed or removed capabilities

**Docs resources**:

- `guides/packages/test-packages.md`
- `guides/testing/run-tests.md`
- `guides/testing/write-tests.md`

### Publish, deprecate, or remove capabilities

For publishing, changelog, and release-note tasks, use the `tenzir-ship` skill
after selecting the relevant package docs. For deprecations and removals, keep
the user-facing compatibility story explicit and retire the affected manifest
entries, operators, examples, pipelines, tests, contexts, and changelog entries
together.

**Results:**

- Changelog entries describe user-facing package changes
- Publishing tasks use the package publishing docs and `tenzir-ship` release
  guidance
- Deprecated capabilities have a clear migration path when users need one
- Removed capabilities retire stale manifest entries, files, examples,
  pipelines, tests, and docs references

**Docs resources**:

- `guides/packages/maintain-a-changelog.md`
- `guides/packages/publish-a-package.md`
- `guides/packages/install-a-package.md`

## Final validation

Review the package as a user-facing artifact. Ensure the manifest describes the
package's capabilities, public UDOs have tests, examples are runnable, and
pipelines are safe to install. For package changes, add a user-facing changelog
entry when the repository expects one.

**Results:**

- Tests pass with deterministic baselines
- Package manifest, examples, pipelines, and changelog are ready for review

**Docs resources**:

- `guides/packages/test-packages.md`
- `guides/packages/maintain-a-changelog.md`
