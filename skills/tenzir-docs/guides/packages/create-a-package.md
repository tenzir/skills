# Create a package


This guide shows you how to create a package from scratch. You’ll learn how to set up the directory structure, write the manifest, and add runnable examples.

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

  * package.yaml Manifest: metadata, contexts, and inputs

The `tests/inputs/` directory holds sample data that the test harness makes available via the `TENZIR_INPUTS` environment variable. Reference these files from test pipelines using `f"{env("TENZIR_INPUTS")}/filename.txt"`.

## Add the package manifest

The `package.yaml` file is the **package manifest**. It identifies the directory as a package and contains metadata, context definitions, and input specifications.

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
```

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