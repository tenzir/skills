---
title: "Directory Layout"
canonical: https://tenzir.com/docs/reference/directory-layout
source: https://tenzir.com/docs/reference/directory-layout.md
section: "Docs"
---

# Directory Layout

> A configuration and a package are both folders of plain files in fixed places. This page lists what each folder may contain, how a package’s files become names in TQL, where packages live in a configuration and in a repository, and the limits on their files. Our explanations of configurations and modules describe the model behind them.

A configuration and a package are both folders of plain files in fixed places. This page lists what each folder may contain, how a package’s files become names in TQL, where packages live in a configuration and in a repository, and the limits on their files. Our explanations of [configurations](../explanations/configuration.md) and [modules](../explanations/packages.md#modules) describe the model behind them.

## Configuration

A configuration holds the pipelines and contexts that a deployment runs, and the packages those pipelines use:

* pipelines/

  * onboard-suricata.tql

  * routing/

    * to-splunk.tql

* contexts/

  * threat-indicators.yaml

* packages/

  * myteam/

    * …

* package.yaml

* package.lock

| Path           | Required | Description                                                                                                                                              |
| -------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pipelines/`   | no       | The [pipelines](directory-layout.md#pipelines) that the deployment runs, one per `.tql` file, in any depth of folders. |
| `contexts/`    | no       | The [contexts](contexts.md) that the deployment keeps, one per `.yaml` file.                                           |
| `packages/`    | no       | The configuration’s [own packages](directory-layout.md#packages-in-a-configuration), one folder per package.           |
| `package.yaml` | yes      | The [configuration manifest](manifest.md#configuration-manifest).                                                      |
| `package.lock` | no       | The [lock](lock.md) that pins every package the configuration uses.                                                    |

A file that the deployment can’t read refuses the whole configuration, and the running pipelines stay as they are.

### Pipelines

Every `.tql` file below `pipelines/` is one pipeline. Its path identifies the pipeline, so `pipelines/routing/to-splunk.tql` stays the same pipeline across deploys, and renaming the file replaces it with a new one.

An optional frontmatter between two `---` lines at the top of the file holds the pipeline’s settings:

pipelines/onboard-suricata.tql

```tql
---
name: Onboard Suricata from TCP
disabled: false
---


accept_tcp "0.0.0.0:34343" {
  read_suricata
}
publish "suricata"
```

| Key        | Type    | Default       | Description                                                        |
| ---------- | ------- | ------------- | ------------------------------------------------------------------ |
| `name`     | string  | the file stem | The name that the platform shows for the pipeline.                 |
| `disabled` | boolean | `false`       | Whether the deployment leaves the pipeline stopped after a deploy. |

Our explanation of [what a deploy guarantees](../explanations/configuration.md#what-a-deploy-guarantees) describes what a deploy does with a pipeline that changed, finished, or that you stopped.

### Contexts

Every `.yaml` file in `contexts/` declares one context, as our reference on [contexts](contexts.md) lists.

### Packages in a configuration

A configuration keeps its own packages under `packages/`, one folder per package, named after the package’s id:

* package.yaml

* package.lock

* pipelines/

  * onboard-firewall.tql

* packages/

  * myteam/

    * package.yaml

    * operators/

      * normalize.tql

  * shared/

    * package.yaml
    * constants.tql

- Every folder directly under `packages/` holds a `package.yaml` with a `name`. The folder’s name is the package’s id, and an `id` in its manifest must agree.
- A pipeline sees a package under `packages/` only once the configuration’s `package.yaml` lists it with `path`, such as `path: packages/myteam`.
- A package under `packages/` declares its own `dependencies`, from a repository or from another package under `packages/` by `path`. The configuration’s `package.lock` locks them.
- A deploy refuses a file directly in `packages/`, a folder there without a `package.yaml`, and files under `packages/<id>/` for a package `<id>` that the lock pins, because the platform puts the locked package there.
- A configuration has no `operators/`, `constants.tql`, or `src/` at its root. Its own operators go in a package under `packages/`.

Our explanation of [packages in a configuration](../explanations/packages.md#packages-in-a-configuration) shows how both kinds of packages reach a deployment.

## Package

A package holds operators and constants that pipelines call, in these files:

* suricata/

  * package.yaml

  * operators/

    * ocsf/

      * normalize.tql

  * constants.tql

  * examples/

    * onboard.tql

  * tests/

    * ocsf/

      * alert.tql
      * alert.txt

    * inputs/

      * alert.json

  * changelog/

    * unreleased/

      * …

    * releases/

      * …

  * package.svg

  * package.lock

| Path            | Required | Description                                                                                                                                       |
| --------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `package.yaml`  | yes      | The [package manifest](manifest.md#package-manifest).                                                           |
| `operators/`    | no       | [User-defined operators](directory-layout.md#operators), one per `.tql` file, in any depth of folders.          |
| `constants.tql` | no       | [Constants](directory-layout.md#constants) that the package’s operators and its users share, as `let` bindings. |
| `examples/`     | no       | Runnable example pipelines, one per `.tql` file directly in the folder.                                                                           |
| `tests/`        | no       | Tests that [`tenzir-test`](test-framework.md) runs, with sample data in `tests/inputs/`.                        |
| `changelog/`    | no       | The changelog and release notes that [`tenzir-ship`](ship-framework.md) writes.                                 |
| `package.svg`   | no       | The package’s icon, by our library’s convention, which `package_icon` links.                                                                      |
| `package.lock`  | no       | The [lock](lock.md) of the package’s dependencies, for a package of its own outside a configuration. Commit it. |

A package under a configuration’s `packages/` has no `package.lock` of its own: the configuration’s lock pins its dependencies. A configuration that installs a package from a repository ignores the package’s lock and resolves its `dependencies` anew, as our reference on [lock locations](lock.md#location) lists.

Tenzir reads only `package.yaml`, the `.tql` files under `operators/`, `constants.tql`, and the `.tql` files directly in `examples/`, and, when you run or test the package on its own, its `package.lock`. Every other file, such as the tests, the changelog, the icon, or a `README.md`, is part of the package, counts towards its [content hash](lock.md#content-hash) and its [size limits](directory-layout.md#size-limits), and reaches the deployment, but Tenzir doesn’t interpret it.

### Operators

Every `.tql` file below `operators/` defines one user-defined operator, which its path [names](directory-layout.md#module-names). The file holds the operator’s pipeline, optionally after a YAML frontmatter between two `---` lines:

operators/ocsf/tag.tql

```tql
---
description: Sets a field to a value, with an optional prefix.
args:
  positional:
    - name: field
      type: field
    - name: value
      type: string
  named:
    - name: prefix
      type: string
      default: ""
---


$field = f"{$prefix}{$value}"
```

Our guide on [adding operators](../guides/manage-packages.md#add-operators) walks through examples of each kind of parameter.

#### Frontmatter

| Key               | Type   | Description                                                                                                                      |
| ----------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `description`     | string | What the operator does.                                                                                                          |
| `args.positional` | list   | The [parameters](directory-layout.md#parameters) that callers pass by position, in this order. |
| `args.named`      | list   | The [parameters](directory-layout.md#parameters) that callers pass by name, as `name=value`.   |

A list in place of the `args` record lists positional parameters only. Any other key, in the frontmatter, under `args`, or in a parameter, fails the package with “unknown key”.

#### Parameters

Each entry of `args.positional` and `args.named` is a record with these keys:

| Key           | Required | Description                                                                                                                                       |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | yes      | The parameter’s name. The body refers to its argument as `$<name>`.                                                                               |
| `type`        | no       | The [type](directory-layout.md#types) that the argument must have. Without it, the parameter accepts any value. |
| `description` | no       | What the parameter does, shown with every diagnostic that a call of the operator produces.                                                        |
| `default`     | no       | The value that an omitted argument takes, as YAML. Without it, the argument is required.                                                          |

The parameters of one operator follow these rules:

* Every name appears once across `args.positional` and `args.named`.
* A positional parameter with a `default` is optional, and every positional parameter after it needs a `default` too.
* A named parameter without a `default` is required: a call without it fails with “required argument `<name>` was not provided”.
* A call that passes a named argument the operator doesn’t declare fails with “named argument `<name>` does not exist”, and the message suggests a close name if there is one.
* Every diagnostic from a call shows the operator’s usage, such as `vendor::tag field:field, value:string, [prefix=string]`, and a table of its parameters with their types, defaults, and descriptions.

#### Types

The `type` key takes one of these TQL types:

| Type       | Accepts                                                            |
| ---------- | ------------------------------------------------------------------ |
| `field`    | A selector, such as `name`, `this`, or `src.ip`, to read or write. |
| `string`   | A string.                                                          |
| `int`      | A signed integer.                                                  |
| `uint`     | An unsigned integer.                                               |
| `float`    | A floating-point number.                                           |
| `bool`     | A boolean.                                                         |
| `duration` | A duration, such as `5min`.                                        |
| `time`     | A timestamp.                                                       |
| `ip`       | An IP address.                                                     |
| `subnet`   | A subnet.                                                          |
| `blob`     | A blob.                                                            |
| `secret`   | A secret. A constant string becomes a secret.                      |
| `null`     | Only `null`.                                                       |
| `[<type>]` | A list of values of the type, such as `"[string]"`.                |

Quote a list type in YAML, as in `type: "[string]"`. A record type and a type alias fail the package with “invalid type”.

#### Null and type checks

Arguments meet their parameters’ types by these rules:

* Every type accepts `null`, so `default: null` makes a parameter optional without a fallback value. The body tells an omitted argument by comparing it with `null`, as in `if $suffix != null { … }`.
* A caller may pass `null` explicitly for any parameter but a `field` parameter, which fails with “expected a selector”.
* The default of a `field` parameter must be `null` or a selector. With a `null` default, the body may read the parameter. A body that assigns to it fails to compile when the caller omits the argument, even inside an `if` that doesn’t run, because an omitted argument stands for no field.
* An argument that is a constant, such as `42` or `"abc"`, is checked when the pipeline compiles. A mismatch fails with “argument `<name>` must be of type `<type>` (got `<type>`)”.
* An argument that depends on events, such as a field of the caller’s events, isn’t checked against the type. The body receives it as is.

### Constants

The `constants.tql` file holds the package’s constants as `let` bindings:

constants.tql

```tql
let $high_severity = 8
let $threshold = $high_severity + 1
let $severities = {low: 2, medium: 3, high: 4, critical: 5}
```

Each binding defines the constant `<id>::$<name>`, as [module names](directory-layout.md#module-names) lists. Tenzir evaluates a binding once and uses its value at every reference, so a binding must hold the same value every time. The rules split into those that fail the package and those that fail each pipeline that references the binding:

| Rule                                                                                | Message on a violation                                                          | Fails                            |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------- |
| The file holds only `let` bindings.                                                 | “`constants.tql` may only contain `let` bindings”                               | The package.                     |
| Every name appears once.                                                            | “duplicate package binding”                                                     | The package.                     |
| A binding references only bindings before it, by `$<name>` or `<id>::$<name>`.      | “`$<name>` is referenced before it is defined”                                  | The package.                     |
| A binding is deterministic: no `now()`, `random()`, or `secret()`, and no pipeline. | “package binding `<id>::$<name>` is not a constant”                             | The pipelines that reference it. |
| A binding is a constant value: no field such as `this` or `src_ip`, and no lambda.  | “expected a constant expression” or “expected a value expression, got a lambda” | The pipelines that reference it. |
| Bindings of different packages don’t reference each other in a cycle.               | “cyclic package binding”                                                        | The pipelines that reference it. |

A binding may reference the constants of the packages that its package declares, by their full names. A reference to a binding that doesn’t exist fails with “package binding `<id>::$<name>` not found”. Our guide on [adding constants](../guides/manage-packages.md#add-constants) shows constants in use.

### Examples

Every `.tql` file directly in `examples/` is one example, which our library catalog shows next to the package. Its optional frontmatter takes a `name` and a `description`. Another key fails the package, and so does an example that doesn’t parse.

### Tests

The `tests/` folder holds the tests that `tenzir-test` runs in package mode: TQL files with the expected output next to them, such as `tests/ocsf/alert.tql` and `tests/ocsf/alert.txt`. The sample data that tests read lies in `tests/inputs/`, which `tenzir-test` exposes as `TENZIR_INPUTS`. Our guide on [testing packages](../guides/write-tests.md#test-packages) runs them.

### Changelog

The `changelog/` folder holds the entries in `changelog/unreleased/` and one folder per release in `changelog/releases/`, such as `changelog/releases/v0.2.0/` with a `manifest.yaml`, a `notes.md`, and the released entries in `entries/`. Our guide on [releasing a package](../guides/manage-packages.md#release-a-package) creates them.

## Module names

Every package is a module named after its [id](manifest.md#the-id). An operator’s name is the package id, followed by the folders below `operators/` and the file name without `.tql`, joined by `::`:

| File                                    | Operator                    |
| --------------------------------------- | --------------------------- |
| `suricata/operators/normalize.tql`      | `suricata::normalize`       |
| `suricata/operators/ocsf/normalize.tql` | `suricata::ocsf::normalize` |
| `suricata/operators/ocsf/map/dns.tql`   | `suricata::ocsf::map::dns`  |

Every folder name and file name on the way must be an identifier that matches `[A-Za-z_][A-Za-z0-9_]*`, so `operators/ocsf-v1/map.tql` fails the package.

A constant’s name is the package id, `::`, and the binding’s name with its `$`. For example, the binding `let $ports = [53, 853]` in `suricata/constants.tql` defines `suricata::$ports`.

The names that a pipeline or a package can use depend on what it declares, as our reference on [package dependencies](dependencies.md#visibility) lists. A package’s operators call its other operators and constants by the same full names, such as `suricata::ocsf::normalize` and `suricata::$ports`.

## Pipelines and contexts in a package

A package holds no pipelines and no contexts: they belong to the configuration, which decides what runs where. A deploy refuses a configuration with a package that has `.tql` files in a `pipelines/` folder, or a `pipelines` or `contexts` key in its manifest, with the message “a package in a configuration may not contain pipelines or contexts”. The `tenzir run` command on your machine ignores them.

Pipelines go in the configuration’s [`pipelines/`](directory-layout.md#pipelines) folder and contexts in its [`contexts/`](directory-layout.md#contexts) folder instead.

## Packages in a repository

A Git repository serves packages to other configurations in one of two layouts.

### Many packages

A repository may hold many packages, one per top-level folder named after the package’s id, as our library does:

* acme-tenzir-packages/

  * acme\_common/

    * package.yaml
    * constants.tql

  * acme\_firewall/

    * package.yaml

    * operators/

      * ocsf/

        * normalize.tql

Each package’s releases are tagged with its folder in front, such as `acme_firewall/v1.5.0`. A dependency names the package by its id and the repository by its URL:

package.yaml

```yaml
dependencies:
  acme_firewall:
    git: https://github.com/acme/tenzir-packages.git
    version: "^1.5"
```

Only top-level folders hold packages: Tenzir looks for a package with the id `<id>` in `<id>/package.yaml` and doesn’t search deeper folders.

### One package

A repository may also hold a single package at its root, with its `package.yaml` next to the repository’s other files. Its releases are tagged `v<version>`, such as `v1.5.0`, and the dependency’s key names the package. An `id` in its manifest must match that key. The package then consists of every file in the repository, all of which count towards its hash and its limits.

Our reference on [package dependencies](dependencies.md#releases) lists how releases are found in both layouts, and our guide on [hosting a package repository](../guides/manage-packages.md#host-a-package-repository) sets one up.

## File rules

A package from a repository holds only regular files. Tenzir refuses a package with a symbolic link or a Git submodule in its folder, since either would leave the package without files it names. Every path in it must work on every platform:

* The path is valid UTF-8.
* No segment holds a control character or one of `\ : < > | ? * "`.
* No segment ends in a dot or a space.
* No segment is a name that Windows reserves for a device, such as `con`, `nul`, `com1`, or `lpt1`, with or without an extension.

Unpacking a package into the [package cache](lock.md#package-cache) fails on a file system that ignores case when two of its paths differ only in case.

## Size limits

The platform enforces these limits on every package that it fetches, and on every configuration archive that it builds, with the locked packages under `packages/` included:

| Limit            | A package from a repository | A configuration archive   |
| ---------------- | --------------------------- | ------------------------- |
| Total size       | 64 MiB of file content      | 64 MiB as a `tar` archive |
| Size of one file | 32 MiB                      | 32 MiB                    |
| Number of files  | 10,000                      | 10,000                    |
| Length of a path | as in the archive           | 1,024 bytes of UTF-8      |

The archive counts what the `tar` format adds: a 512-byte header per file, and each file’s content rounded up to a multiple of 512 bytes. A path in the archive includes its folder, such as `packages/suricata/operators/ocsf/normalize.tql`. The platform checks the archive again after adding each package, so many small packages can exceed the limit together.
