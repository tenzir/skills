---
title: "Create a package"
canonical: https://tenzir.com/docs/guides/packages/create-a-package
source: https://tenzir.com/docs/guides/packages/create-a-package.md
section: "Docs"
---

# Create a package

> This guide shows you how to create a package from scratch. You’ll learn how to set up the directory structure, write the manifest, plan reusable operators, add deployable pipelines, and include runnable examples.

This guide shows you how to create a package from scratch. You’ll learn how to set up the directory structure, write the manifest, plan reusable operators, add deployable pipelines, and include runnable examples.

## Create the package scaffold

Create a directory with the standard package layout:

* vendor/

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
id: vendor


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
  vendor: Vendor
  source: https://github.com/vendor/tenzir-packages
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
* Give parsers a required positional input field and a named `into` output that defaults to `this`. Parsers turn raw input into structured source events.
* If the package maps to OCSF, expose a main mapper such as `vendor::ocsf::map`. Give it an optional positional event field and a named `into` output, both defaulting to `this`. Snapshot the source under the output before mapping.
* Expose a paved-road operator such as `vendor::ocsf::normalize` for the product’s complete standard procedure. It should accept every product representation the package supports, parse strings when necessary, proceed directly when the input is already structured, map to the target schema, apply standard policy, and write the complete result to `into=this` by default.
* Name the package after the vendor and give each of the vendor’s products a directory below it, as our guide on [choosing a namespace](add-operators.md#choose-a-namespace) explains.
* If the package maps between normalized schemas, put the target schema before the source schema in the operator namespace, for example `vendor::cim::ocsf::map` for OCSF-to-CIM mapping.
* Prefer operator arguments over installation inputs for anything a caller might vary. Arguments are typed and checked per call, while an input is fixed for the whole installation.
* Put complete workflows with an input and output under `pipelines/` only when the package must own a running workflow, and disable them by default with `disabled: true`. Otherwise let users build pipelines from your operators.
* Put focused snippets under `examples/` so users can quickly try the package after installation.
* Put deterministic tests under `tests/`, including baselines for every public operator.

## Add examples

The `examples` directory contains self-contained code snippets that demonstrate how to use the package. These snippets appear in the [Tenzir Library](https://app.tenzir.com/library) and provide runnable TQL code that users can execute after installing the package.

Create example files that showcase your package’s features:

examples/basic-usage.tql

```tql
// Demonstrate the primary use case
vendor::fetch
vendor::transform
head 10
```

For more complex scenarios, combine multiple operators and show how they work together:

examples/advanced-usage.tql

```tql
// Show a more complex scenario
vendor::fetch
where severity == "high"
vendor::enrich
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
* [Add constants](add-constants.md)
* [Maintain a changelog](maintain-a-changelog.md)
* [Onboard a data source](../../tutorials/onboard-a-data-source.md)
* [Packages](../../explanations/packages.md)
