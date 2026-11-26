---
title: "Manifest"
canonical: https://tenzir.com/docs/reference/manifest
source: https://tenzir.com/docs/reference/manifest.md
section: "Docs"
---

# Manifest

> Every package and every configuration has a package.yaml at its root, its manifest. A package’s manifest names and describes the package and lists the packages it uses. A configuration’s manifest lists only the packages its pipelines use. This page lists the keys of both. Our explanation of packages describes the model behind them, and our guide on creating a package writes a manifest step by step.

Every package and every configuration has a `package.yaml` at its root, its **manifest**. A package’s manifest names and describes the package and lists the packages it uses. A configuration’s manifest lists only the packages its pipelines use. This page lists the keys of both. Our explanation of [packages](../explanations/packages.md) describes the model behind them, and our guide on [creating a package](../guides/manage-packages.md#create-a-package) writes a manifest step by step.

## Package manifest

A package’s `package.yaml` holds a YAML mapping:

acme\_firewall/package.yaml

```yaml
name: Acme Firewall
version: "1.4.0"
author: Acme Security
author_icon: https://github.com/acme.png
package_icon: https://raw.githubusercontent.com/acme/tenzir-packages/main/acme_firewall/package.svg
categories:
  - sources
  - mappings
description: |
  Parses the logs of Acme firewalls and maps them to
  [OCSF](https://schema.ocsf.io).
dependencies:
  acme_common:
    git: https://github.com/acme/tenzir-packages.git
    version: "^1.2"
metadata:
  owner: detection-engineering
```

It takes these keys:

| Key            | Type            | Default         | Description                                                                                                                                                                           |
| -------------- | --------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`           | string          | the folder name | The package id, which is also its module name. See [the id](manifest.md#the-id).                                                                    |
| `name`         | string          | required        | The display name. Its presence marks the file as a package’s manifest.                                                                                                                |
| `version`      | string          | none            | The version of the package’s latest release, quoted and without a `v`, such as `"1.4.0"`. See [the version](manifest.md#the-version).               |
| `description`  | string          | none            | What the package is and what it covers, in Markdown.                                                                                                                                  |
| `author`       | string          | none            | The display name of the author.                                                                                                                                                       |
| `author_icon`  | string          | none            | The URL of an image of the author.                                                                                                                                                    |
| `package_icon` | string          | none            | The URL of an image of the package.                                                                                                                                                   |
| `categories`   | list of strings | none            | Tags to filter packages by, such as `sources`, `destinations`, and `mappings`, which our library uses.                                                                                |
| `dependencies` | mapping         | none            | The packages that the package’s operators and constants use, by id. Our reference on [package dependencies](dependencies.md) describes the entries. |
| `metadata`     | any             | none            | Data for other tools. Tenzir never interprets it.                                                                                                                                     |

Tenzir refuses a manifest with a top-level key that it doesn’t know, so that a typo doesn’t go unnoticed. Put data of your own under `metadata`.

Our library catalog and the **Packages** page of the app show `name`, `description`, `author`, the icons, and `categories`. The **Packages** page shows an icon only from an `https://` URL. Our library keeps each package’s icon as `package.svg` in the package’s folder and links its raw URL on GitHub.

### The id

The id names the package in `dependencies`, in `package.lock`, and in code, where it prefixes the package’s operators and constants, as in `acme_firewall::ocsf::normalize`. Our reference on the [package layout](directory-layout.md#module-names) shows how names form.

An id is a TQL identifier: it matches `[A-Za-z_][A-Za-z0-9_]*`, so it has no dashes or dots. It must not be a keyword that TQL reads as something other than a name: `_`, `and`, `as`, `def`, `else`, `false`, `fn`, `for`, `function`, `if`, `in`, `is`, `let`, `match`, `mod`, `module`, `move`, `not`, `null`, `or`, `return`, `self`, `super`, `this`, `true`, `use`, or `while`.

Where a package sits decides its id, and an `id` in the manifest must agree:

| The package is…                                      | Its id is…                              |
| ---------------------------------------------------- | --------------------------------------- |
| in a folder of a repository that holds many packages | the folder name.                        |
| at the root of a repository                          | the id that the dependency on it names. |
| under a configuration’s `packages/`                  | the folder name.                        |
| a root of its own, outside a configuration           | its `id`, or else the folder name.      |

A manifest whose `id` differs from the id the package has where it sits fails to load, such as `id: suricata` in `packages/myteam/package.yaml`.

### The version

The `version` key states the version of the package’s latest release. It holds a full [semantic version](https://semver.org/) without a `v`, such as `0.2.0` or `1.0.0-rc.1`. It must be a YAML string, which a full version is even without quotes; Tenzir refuses a value that YAML reads as a number, such as an unquoted `1.2`. The same holds for every version requirement under `dependencies`.

Where Tenzir takes a package’s version from depends on how a dependency names the package:

* A **release** takes its version from its Git tag, such as `suricata/v0.2.0`. Tenzir doesn’t compare the tag with the manifest’s `version`.
* A **pinned revision**, a commit, branch, or tag that a dependency names with `rev`, takes its version from the manifest’s `version` at that commit. Version requirements on the package are checked against it, and `package.lock` records it. Without a `version`, the revision has no version, and every version requirement on it fails.

Our reference on [package dependencies](dependencies.md#pinned-revisions) covers pinned revisions in full.

The `version` stays at the last released version between releases. In package mode, [`tenzir-ship release create`](ship-framework.md) writes the version it releases into `version`, so the release and its manifest agree. Our library’s CI refuses a release whose manifest states another version, and a change of `version` without a release. Our guide on [releasing a package](../guides/manage-packages.md#release-a-package) walks through a release.

### The description

Describe what the package is for: what the integrated product is, what the package does for the user, and the caveats that decide whether to use it. How long that takes depends on how much the package covers. Leave out what has a home elsewhere: runnable TQL belongs in `examples/`, operator usage in the operator’s [frontmatter](directory-layout.md#frontmatter), edge cases in `tests/`, and release notes in `changelog/`. Our guide on [describing what a package is for](../guides/manage-packages.md#describe-what-the-package-is-for) shows an example.

## Configuration manifest

The `package.yaml` at the root of a [configuration](../explanations/configuration.md) lists the packages that its pipelines use, and nothing else:

package.yaml

```yaml
dependencies:
  suricata: "^0.2"
  acme_firewall:
    git: https://github.com/acme/tenzir-packages.git
    version: "^1.4"
  myteam:
    path: packages/myteam
```

Its only key is `dependencies`, in the form that our reference on [package dependencies](dependencies.md) describes. Any other key refuses the configuration, because a configuration has no operators or metadata of its own. For the same reason, a deploy refuses a configuration with an `operators/` folder, a `constants.tql`, or a `src/` folder at its root. The configuration’s own operators go in a package under `packages/`, which its manifest lists with `path`, as our reference on the [package layout](directory-layout.md#packages-in-a-configuration) shows.

An empty file, an empty `dependencies:`, or no `package.yaml` at all lists no packages. The [package commands](cli.md) need a `package.yaml` to work on, so start a configuration that uses packages with one that holds `dependencies:`.

## Package or configuration

Tenzir tells the two manifests apart by one key: a `package.yaml` with a `name` is a package’s, and one without is a configuration’s. A package’s manifest therefore needs a `name`, and a configuration’s must not have one.

Where the manifest sits decides what it belongs to. The [package commands](cli.md#where-the-package-commands-work) and `tenzir run` start at the current directory and take the nearest `package.yaml` at or above it. A package’s manifest directly under the `packages/` folder of a configuration belongs to that configuration. Any other package’s manifest is a root of its own, with a lock of its own.
