---
name: tenzir-create-package
description: >-
  Create library-quality Tenzir packages with user-defined operators, tests,
  examples, disabled-by-default pipelines, inputs, contexts, and optional OCSF
  mappings. Use whenever the user wants to build, scaffold, package, parse,
  normalize, enrich, export, map to OCSF, or add reusable Tenzir package
  capabilities, even if they only mention one part such as "create a parser",
  "add an operator", "build a package", or "map this data to OCSF."
metadata:
  requires:
    skills:
      - tenzir-docs
      - tenzir-ocsf
---

# Create a Tenzir Package

Build a Tenzir package as a complete library-quality unit. A package should
provide reusable user-defined operators (UDOs), tests, examples, deployable
pipelines, and clear metadata. OCSF mapping is one optional capability within
that package, not a separate workflow.

## Workflow

Execute each step in order. Verify the **Results** before moving on.

### 1. Understand the package intent

Identify the package's vendor, product, audience, and role in the Tenzir
Library. Decide whether the package is primarily a source, destination, mapping,
enrichment, utility, or a combination of these. Inspect similar packages in the
library before introducing new naming or layout conventions.

Use the `tenzir-docs` skill for package, TQL, operator, pipeline, context, and
test guidance. Use the `tenzir-ocsf` skill only when the package includes OCSF
mapping.

**Results:**

- Vendor and product names
- Package categories and target use cases
- Installation behavior, including which pipelines should run automatically
- Decision on whether OCSF mapping is in scope

**Resources** (read via `tenzir-docs`):

- `guides/packages/create-a-package.md`
- `tutorials/learn-idiomatic-tql.md`

### 2. Create or update the package scaffold

Set up the package as a complete contribution unit. Keep package IDs stable,
short, and lowercase. Use the repository's existing package naming and directory
style.

**Results:**

- `package.yaml` with `id`, `name`, author metadata, icon, Markdown
  description, categories, inputs, and contexts where needed
- Standard directories as needed: `operators/`, `examples/`, `pipelines/`,
  `tests/inputs/`, and `changelog/`
- Samples stored close to the tests that use them

**Resources** (read via `tenzir-docs`):

- `guides/packages/create-a-package.md`
- `guides/packages/configure-inputs.md`
- `guides/packages/add-contexts.md`

### 3. Design the UDO API

Treat UDOs as the package's reusable public API. Add operators for reusable
capabilities such as fetching, parsing, cleaning, enriching, mapping, casting,
or exporting. Choose names from stable user-facing semantics and the package
directory structure rather than from one-off pipeline names.

Add operator frontmatter arguments for configurable fields, URLs, credentials,
modes, output topics, and destinations. Prefer small composable operators over
large pipelines with embedded transformation logic.

**Results:**

- UDOs under `operators/` with clear names and descriptions
- Parse and clean operators only when the input format needs them
- Field and value parameters for reusable behavior
- Tests for each public operator and important argument combination

**Resources** (read via `tenzir-docs`):

- `guides/packages/add-operators.md`
- `guides/packages/test-packages.md`
- `guides/parsing/parse-delimited-text.md`
- `guides/parsing/parse-string-fields.md`
- `guides/normalization/clean-up-values.md`

### 4. Add optional OCSF mapping

When the package maps events to OCSF, keep the mapping as part of the package's
operator API. Use a shared mapping operator plus event-specific operators when
the source has multiple event types. Let the main mapping operator initialize
shared OCSF fields, preserve raw input when available, collect source residue in
`unmapped`, normalize common sentinels, and dispatch on a stable discriminator.

Event-specific mapping operators should set the OCSF class, activity, `type_uid`,
and `@name`, then move source fields from `unmapped` into their OCSF homes. Use
small lookup records for event-code-to-enum mappings. Leave source fields in
`unmapped` when they do not have a clean OCSF home, with concise comments for
non-obvious decisions.

**Results:**

- Main mapping operator such as `vendor::product::ocsf::map`
- Event-specific operators under an established local namespace such as
  `operators/<product>/ocsf/events/`
- Raw source preserved in `raw_data` and `raw_data_size` when mapping from raw
  events
- OCSF metadata, profiles, version, timestamps, product, and device fields set
  consistently
- Unknown or unsupported events mapped to a clear fallback instead of silently
  disappearing

**Resources:**

- Use the `tenzir-ocsf` skill to select event classes, attributes, objects,
  profiles, and extensions
- Read via `tenzir-docs`: `guides/normalization/map-to-ocsf.md`

### 5. Add deployable pipelines

Use `pipelines/` for complete deployable workflows with an input and an output.
Pipelines should orchestrate package UDOs instead of embedding reusable
transformation logic.

Ship ingestion, export, and OCSF publishing pipelines as disabled by default
unless the package is intentionally an always-on feed or context updater. Use
`restart-on-error` for long-running or periodic workflows where restart behavior
is desirable.

**Results:**

- Pipelines with frontmatter `name` and `description`
- Optional operational pipelines marked `disabled: true`
- Package inputs used for user-specific URLs, credentials, intervals, topics,
  and destinations
- Pipelines that compose UDOs and publish, import, update contexts, or export
  to destinations

**Resources** (read via `tenzir-docs`):

- `guides/packages/add-pipelines.md`
- `guides/packages/configure-inputs.md`
- `guides/collecting.md`

### 6. Add examples

Use `examples/` for focused runnable snippets that teach users how to use the
package. Examples should demonstrate one concept at a time, such as ingesting a
source, invoking a UDO, mapping to OCSF, enriching with a context, or exporting
to a destination.

Examples are not a replacement for tests or deployable pipelines. Keep them
self-contained and easy to adapt after package installation.

**Results:**

- Examples with frontmatter `name` and `description`
- One primary example for the package's core use case
- Additional examples for important variants or integrations

**Resources** (read via `tenzir-docs`):

- `guides/packages/create-a-package.md`
- `guides/collecting.md`

### 7. Finalize and validate

Review the package as a user-facing artifact. Ensure the manifest describes the
package's capabilities, every public UDO has a test, examples are runnable, and
pipelines are safe to install. For library contributions, add a user-facing
changelog entry.

**Results:**

- TQL follows idiomatic patterns
- Tests pass with deterministic baselines
- OCSF mappings, when present, pass `ocsf::derive` and `ocsf::cast` without
  warnings
- Package manifest, examples, pipelines, and changelog are ready for review

**Resources** (read via `tenzir-docs`):

- `guides/packages/test-packages.md`
- `guides/packages/maintain-a-changelog.md`
- `tutorials/learn-idiomatic-tql.md`
