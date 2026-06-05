---
name: tenzir-manage-packages
description: >-
  Manage Tenzir packages across the full lifecycle: add new packages, inspect
  existing packages, update manifests, extend or remove package capabilities,
  refactor user-defined operators, maintain tests and examples, configure
  inputs and contexts, ship deployable pipelines, publish packages, and map data
  to schemas such as OCSF, Google UDM, ECS, or ASIM. Use when the user is
  working in the context of a Tenzir package or wants to turn exploratory TQL
  work into package-managed, reusable capabilities.
metadata:
  requires:
    skills:
      - tenzir-docs
  uses:
    skills:
      - name: tenzir-google-udm
        when: Google UDM mapping or Google SecOps field semantics are in scope.
      - name: tenzir-ocsf
        when: OCSF mapping or OCSF schema semantics are in scope.
      - name: tenzir-ship
        when: Package changelog entries, release notes, or publishing workflows are in scope.
---

# Manage Tenzir Packages

Use this skill as the package-lifecycle entry point into the `tenzir-docs`
skill. The value here is routing: detect what part of a package lifecycle the
user is working on, load the relevant Tenzir docs guide, and keep the package as
one coherent artifact while the implementation changes.

Package work can include scaffolding a package, changing a manifest, adding or
removing UDOs, parsing data, normalizing values, mapping to a target schema,
adding contexts, wiring deployable pipelines, maintaining examples and tests,
publishing, or retiring obsolete capabilities. Schema mapping is one package
capability among others; route schema-specific questions to the right schema
skill only when the target schema requires it.

## Workflow

Execute each step in order. Verify the **Results** before moving on.

### 1. Understand the package state and intent

Identify the package's vendor, product, audience, and role in the Tenzir
Library. Determine the lifecycle task: add, inspect, update, extend, refactor,
deprecate, remove, test, publish, or migrate a package capability. Decide which
user-facing Library categories apply (`sources`, `destinations`, `mappings`,
`contexts`) and whether the package is a source, destination, mapping,
enrichment, utility, or a combination of these.

For existing packages, inspect the current manifest, operators, pipelines,
examples, tests, changelog, and open work before editing. Inspect similar
packages in the library before introducing new naming or layout conventions.

**Results:**

- Vendor and product names
- Valid package categories and target use cases
- Current package state, when the package already exists
- Lifecycle task type: add, inspect, update, extend, refactor, deprecate, or
  remove a package or package capability
- Installation behavior, including which pipelines should run automatically
- Target schema, destination, context, or integration requirements, when any are
  in scope

### 2. Dispatch to the right docs guides

Use `tenzir-docs` as the primary source for implementation guidance. Read the
smallest set of pages that covers the task instead of relying on this skill to
duplicate package documentation.

| Task area | Read via `tenzir-docs` |
| --- | --- |
| Package model and design | `explanations/packages.md`, `tutorials/write-a-package.md` |
| New package or scaffold repair | `guides/packages/create-a-package.md` |
| Package installation behavior | `guides/packages/install-a-package.md` |
| Manifest inputs and configuration | `guides/packages/configure-inputs.md` |
| User-defined operators | `guides/packages/add-operators.md` |
| Deployable pipelines | `guides/packages/add-pipelines.md` |
| Package contexts | `guides/packages/add-contexts.md` |
| Package tests | `guides/packages/test-packages.md`, `guides/testing/run-tests.md`, `guides/testing/write-tests.md` |
| Changelog and release notes | `guides/packages/maintain-a-changelog.md` |
| Publishing | `guides/packages/publish-a-package.md` |
| Parsing raw data | `guides/parsing/parse-delimited-text.md`, `guides/parsing/parse-binary-data.md`, `guides/parsing/parse-string-fields.md` |
| Data shaping | `guides/transformation/shape-records.md`, `guides/transformation/reshape-complex-data.md` |
| Normalization workflow | `guides/normalization.md`, `guides/normalization/clean-up-values.md` |
| OCSF mapping | `guides/normalization/map-to-ocsf.md` |
| Google UDM mapping | `guides/normalization/map-to-udm.md` |
| ECS, ASIM, or other schemas | `guides/normalization/map-to-other-schemas.md` |
| Enrichment and lookup data | `guides/enrichment/work-with-lookup-tables.md`, `guides/enrichment/enrich-with-network-inventory.md`, `guides/enrichment/enrich-with-threat-intel.md` |
| Collection and destinations | `guides/collecting.md`, `guides/routing/send-to-destinations.md` |
| Stream routing | `guides/routing/split-and-merge-streams.md`, `guides/routing/fan-out-with-subpipelines.md`, `guides/routing/load-balance-pipelines.md` |
| Idiomatic TQL | `tutorials/learn-idiomatic-tql.md` |

**Results:**

- Relevant guide paths selected before editing
- Any schema-specific skill selected only when schema details are needed
- No copied guide content embedded into package workflow instructions

### 3. Manage package structure as one artifact

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
- No stale package entries left behind after a capability is renamed, moved, or
  removed
- Test samples stored close to the tests that use them: inline `.input` files
  for single-test fixtures and local `inputs/` directories for shared fixtures

**Resources** (read via `tenzir-docs`):

- `guides/packages/create-a-package.md`
- `guides/packages/configure-inputs.md`
- `guides/packages/add-contexts.md`

### 4. Manage UDOs and reusable package capabilities

Treat UDOs as the package's reusable public API. Add, update, refactor,
deprecate, or remove operators for reusable capabilities such as fetching,
parsing, cleaning, enriching, mapping, translating, routing, casting, or
exporting. Choose names from
stable user-facing semantics and the package directory structure rather than
from one-off pipeline names.

Add operator frontmatter arguments for configurable fields, URLs, credentials,
modes, output topics, and destinations. Preserve existing public operator names
unless a rename is intentional and reflected in examples, pipelines, tests, and
changelog entries. Prefer small composable operators over large pipelines with
embedded transformation logic.

**Results:**

- UDOs under `operators/` with clear names and descriptions
- Parse and clean operators only when the input format needs them
- Field and value parameters for reusable behavior
- Compatibility decisions documented in code, tests, or changelog entries where
  user-facing behavior changes
- Tests for each public operator and important argument combination

### 5. Route schema mapping work by target schema

When a package maps events to a schema, keep the mapping as part of the package's
operator API. Start with `guides/normalization.md` and
`guides/normalization/clean-up-values.md`, then dispatch by target schema:

| Target schema | Routing |
| --- | --- |
| OCSF | Read `guides/normalization/map-to-ocsf.md`, then use the `tenzir-ocsf` skill for classes, objects, attributes, profiles, extensions, and schema-version questions. |
| Google UDM | Read `guides/normalization/map-to-udm.md`, then use the `tenzir-google-udm` skill for event types, entity types, field structure, enum values, field-name forms, and Google SecOps ingestion shape. |
| ECS, ASIM, or another schema | Read `guides/normalization/map-to-other-schemas.md`, then use the best available schema reference for the requested target. |

Prefer source namespaces and explicit value conversions for every schema
mapping. Preserve source residue in the target schema's expected place, such as
`unmapped` for OCSF or `additional` for UDM. When removing or renaming mappings,
update the related operators, tests, examples, pipelines, and changelog entries
together.

**Results:**

- Target schema chosen deliberately
- Schema-specific docs or skills consulted before field and enum decisions
- Mapping operators, tests, examples, and pipeline references kept in sync
- Source residue preserved for review in a target-appropriate field

### 6. Manage deployable pipelines

Use `pipelines/` for complete deployable workflows with an input and an output.
Pipelines should orchestrate package UDOs instead of embedding reusable
transformation logic.

Ship ingestion, export, mapping, enrichment, and publishing pipelines as
disabled by default unless the package is intentionally an always-on feed or
context updater. Use `restart-on-error` for long-running or periodic workflows
where restart behavior is desirable.

**Results:**

- Pipelines with frontmatter `name` and `description`
- Optional operational pipelines marked `disabled: true`
- Package inputs used for user-specific URLs, credentials, intervals, topics,
  and destinations
- Pipelines that compose UDOs and publish, update contexts, or export
  to destinations
- Removed or renamed UDOs no longer referenced by deployable pipelines

**Resources** (read via `tenzir-docs`):

- `guides/packages/add-pipelines.md`
- `guides/packages/configure-inputs.md`
- `guides/collecting.md`

### 7. Manage examples

Use `examples/` for focused runnable snippets that teach users how to use the
package. Examples should demonstrate one concept at a time, such as ingesting a
source, invoking a UDO, mapping to a schema, enriching with a context, or
exporting to a destination.

Examples are not a replacement for tests or deployable pipelines. Keep them
self-contained and easy to adapt after package installation.

**Results:**

- Examples with frontmatter `name` and `description`
- One primary example for the package's core use case
- Additional examples for important variants or integrations
- Examples updated or removed when public package capabilities change

**Resources** (read via `tenzir-docs`):

- `guides/packages/create-a-package.md`
- `guides/collecting.md`

### 8. Finalize and validate

Review the package as a user-facing artifact. Ensure the manifest describes the
package's capabilities, every public UDO has a test, examples are runnable, and
pipelines are safe to install. For library contributions, add a user-facing
changelog entry.

**Results:**

- TQL follows idiomatic patterns
- Tests pass with deterministic baselines
- Schema mapping tests, when present, validate the target schema shape with the
  relevant docs guidance, operators, or schema-specific skill
- Package manifest, examples, pipelines, and changelog are ready for review

**Resources** (read via `tenzir-docs`):

- `guides/packages/test-packages.md`
- `guides/packages/maintain-a-changelog.md`
- `tutorials/learn-idiomatic-tql.md`
