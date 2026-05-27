# Create a package


This guide shows you how to create a package from scratch. You’ll learn how to set up the directory structure, write the manifest, plan reusable operators, add deployable pipelines, and include runnable examples.

## Create the package scaffold

Create a directory with the standard package layout:

* acme/

  * changelog/ User-facing documentation of changes

    * …

  * examples/ Runnable snippets for users

    * …

  * operators/ Reusable building blocks for pipelines

    * …

  * pipelines/ Deployable pipelines

    * …

  * tests/ Integration tests

    * inputs/ Sample data for test pipelines

      * …

  * package.yaml Manifest: descriptive fields, metadata, contexts, and inputs

The `tests/inputs/` directory holds sample data that the test harness makes available via the `TENZIR_INPUTS` environment variable. Reference these files from test pipelines using `f"{env("TENZIR_INPUTS")}/filename.txt"`.

## Add the package manifest

The `package.yaml` file is the **package manifest**. It identifies the directory as a package and contains descriptive fields, categories, external metadata, context definitions, and input specifications.

### Add descriptive metadata

Start with the required and recommended metadata fields:

package.yaml

```yaml
# The unique ID of the package. (required)
id: acme


# The display name of the package and a path to an icon for the package.
name: My Package
package_icon: https://example.com/icon.svg


# The display name of the package author and a path to a profile picture.
author: Your Name
author_icon: https://github.com/yourusername.png


# A user-facing description of the package.
description: |
  A brief description of what your package does and the use cases it supports.
  You can use **Markdown** formatting here.


# User-facing categories for the Tenzir Library.
# Valid values: sources, destinations, mappings, contexts.
categories:
  - sources
  - mappings
```

### Add external metadata

Use top-level `categories` for the Library grouping. Valid values are `sources`, `destinations`, `mappings`, and `contexts`. Use the top-level `metadata` field for data consumed by external tools. Tenzir accepts this field but does not interpret its contents.

package.yaml

```yaml
metadata:
  vendor: Acme
  source: https://github.com/acme/tenzir-packages
```

Unknown top-level keys outside the package schema fail validation. Put non-engine package data under `metadata` instead.

### Define inputs

**Inputs** provide a templating mechanism that replaces variables with user-provided values during installation. This makes packages configurable without modifying source files.

package.yaml

```yaml
inputs:
  refresh_interval:
    name: Refresh Interval
    description: How often the pipeline refreshes the data source.
    default: 1h
```

Reference inputs using `{{ inputs.input-id }}` syntax. See [Configure inputs](configure-inputs.md) for the complete templating guide.

## Plan package capabilities

A package can expose several capabilities at once. Treat user-defined operators as the reusable API, deployable pipelines as operational templates, examples as short usage snippets, and tests as the executable contract.

* Put reusable package capabilities under `operators/`.
* If the package maps to OCSF, expose a main mapper such as `acme::ocsf::map` that accepts parsed source events, performs source-specific cleanup and shared OCSF setup, produces minimal OCSF, and dispatches to event-specific operators under a local namespace such as `operators/ocsf/events/`.
* Put complete workflows with an input and output under `pipelines/`. Disable optional operational pipelines by default with `disabled: true`.
* Put focused snippets under `examples/` so users can quickly try the package after installation.
* Put deterministic tests under `tests/`, including baselines for every public operator.

## Add examples

The `examples` directory contains self-contained code snippets that demonstrate how to use the package. These snippets appear in the [Tenzir Library](https://app.tenzir.com/library) and provide runnable TQL code that users can execute after installing the package.

Create example files that showcase your package’s features:

examples/basic-usage.tql

```tql
// Demonstrate the primary use case
acme::fetch
acme::transform
head 10
```

For more complex scenarios, combine multiple operators and show how they work together:

examples/advanced-usage.tql

```tql
// Show a more complex scenario
acme::fetch
where severity == "high"
acme::enrich
publish "alerts"
```

Keep examples focused and self-contained. Each example should demonstrate a single concept or use case.

## Define contexts

If your package uses enrichment contexts, add a `contexts` key to the manifest. See [Add contexts](add-contexts.md) for the full schema and usage details.

## See also

* [Install a package](install-a-package.md)
* [Configure inputs](configure-inputs.md)
* [Add operators](add-operators.md)
* [Add pipelines](add-pipelines.md)
* [Maintain a changelog](maintain-a-changelog.md)
* [Write a package](../../tutorials/write-a-package.md)
* [Packages](../../explanations/packages.md)