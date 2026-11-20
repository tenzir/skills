---
title: "Dependencies"
canonical: https://tenzir.com/docs/reference/dependencies
source: https://tenzir.com/docs/reference/dependencies.md
section: "Docs"
---

# Dependencies

> The dependencies key of a manifest lists the packages that a configuration or a package uses, by id. This page lists the forms of an entry, the version requirements it may state, how releases are tagged, and how Tenzir resolves all requirements into one lock. Our explanation of dependencies and resolution describes the model behind it.

The `dependencies` key of a [manifest](manifest.md) lists the packages that a configuration or a package uses, by id. This page lists the forms of an entry, the version requirements it may state, how releases are tagged, and how Tenzir resolves all requirements into one [lock](lock.md). Our explanation of [dependencies and resolution](../explanations/packages.md#dependencies-and-resolution) describes the model behind it.

## Entries

Every key under `dependencies` is a package id, which must be a valid [package id](manifest.md#the-id). Its value takes a short or a long form:

package.yaml

```yaml
dependencies:
  # Short form: a release of our library.
  suricata: "^0.2"
  # Long form: a release of another repository.
  acme_firewall:
    git: https://github.com/acme/tenzir-packages.git
    version: "^1.4"
  # Long form: a revision instead of a release.
  zeek:
    git: https://github.com/tenzir/library.git
    rev: main
  # Long form: a package of the configuration.
  myteam:
    path: packages/myteam
```

The **short form** `<id>: "<requirement>"` takes a release of our library at `https://github.com/tenzir/library.git` that satisfies the [version requirement](dependencies.md#version-requirements). The **long form** is a mapping with these keys:

| Key       | Type   | Description                                                                                                                                |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `version` | string | A [version requirement](dependencies.md#version-requirements). Without `git`, it applies to our library. |
| `git`     | string | The URL of the Git repository that holds the package. Defaults to our library.                                                             |
| `rev`     | string | A commit, tag, or branch to take the package at instead of a release. Requires `git`.                                                      |
| `path`    | string | A package of the configuration, under its `packages/` folder. Takes no other key.                                                          |

A version and a version requirement must be YAML strings. Most read as strings without quotes, such as `^0.2.0`, which is how the [package commands](cli.md) write them. Quote a value that YAML would read otherwise, such as `"1.2"`, which is a number, or `"*"`, which starts an alias. Tenzir refuses anything but a string. A key other than these four is an error.

### Repositories

The `git` key holds a URL, such as `https://github.com/acme/tenzir-packages.git`. It must not be a path on your machine, and it must not hold a user name or password, because the URL ends up in `package.lock`, in messages, and in logs. A package comes from that repository’s folder named after its id, or else from the repository’s root, as our reference on the [package layout](directory-layout.md#packages-in-a-repository) shows.

A long-form entry with `git` and without `version` or `rev` takes the newest release that is no pre-release, whatever its version.

### Pinned revisions

An entry with `rev` takes the package at a revision of its repository instead of a release:

package.yaml

```yaml
dependencies:
  suricata:
    git: https://github.com/tenzir/library.git
    rev: fix/dns-mapping
```

The `rev` value is a full 40-character commit id, or the exact name of a tag or a branch, such as `main` or `suricata/v0.2.0`. An abbreviated commit id doesn’t name a revision. A `rev` always needs `git`, also for our library.

A pinned revision is no release, so its version comes from the `version` key of the package’s [manifest](manifest.md#the-version) at that commit, and `package.lock` records it. A `version` next to `rev` is a requirement on that version:

package.yaml

```yaml
dependencies:
  suricata:
    git: https://github.com/acme/library-fork.git
    rev: main
    version: "^0.2"
```

Resolution fails when the manifest at the commit states a version that the requirement, or any other package’s requirement, doesn’t accept. It also fails when the manifest states no `version` and anything asks for a version.

The lock pins the commit that the revision named when it was locked. A branch that moves on stays at its locked commit until you [update the package](cli.md#tenzir-package-update).

### Packages of a configuration

An entry with `path` names a package under the configuration’s `packages/` folder. The path is relative to the `package.yaml` that holds the entry, must not be absolute, and must lead to `packages/<id>/`, the folder of the id that the entry names:

packages/myteam/package.yaml

```yaml
name: My Team
dependencies:
  shared:
    path: ../shared
```

Only a configuration’s manifest and the manifests of its packages under `packages/` may use `path`. A package of its own, outside a configuration, and a package from a repository can’t. A package under `packages/` can’t be asked for from a repository either: once it is a package of the configuration, every entry for it uses `path`.

## Sources in Tenzir 7.0

The platform fetches packages only over `https://` from public repositories on github.com, our library included. Since a URL can’t carry credentials, a private repository can’t serve packages yet. A package that must stay private lives in the configuration under `packages/` and comes in with `path`.

The [package commands](cli.md) on your machine reach any repository, also through a `file:///…` URL, which suits trying out a package before you publish it. The platform refuses to build a configuration whose lock names a repository it may not fetch from, so a configuration that you deploy uses github.com only. Our guide on [hosting a package repository](../guides/manage-packages.md#host-a-package-repository) sets one up.

## Version requirements

A version requirement has exactly one operator, followed by a version:

| Requirement | Accepts                                             | Equivalent to     |
| ----------- | --------------------------------------------------- | ----------------- |
| `^1.2.3`    | That version and the later ones compatible with it. | `>=1.2.3 <2.0.0`  |
| `~1.2.3`    | That version and the later patch releases of 1.2.   | `>=1.2.3 <1.3.0`  |
| `=1.2.3`    | Exactly that version.                               | `>=1.2.3 <=1.2.3` |
| `*`         | Any version that is no pre-release.                 |                   |

A requirement may leave off the patch part or the minor and patch parts:

| Requirement | Equivalent to    |
| ----------- | ---------------- |
| `^1.2`      | `>=1.2.0 <2.0.0` |
| `^1`        | `>=1.0.0 <2.0.0` |
| `~1.2`      | `>=1.2.0 <1.3.0` |
| `~1`        | `>=1.0.0 <2.0.0` |
| `=1.2`      | `>=1.2.0 <1.3.0` |

A bare version such as `1.2.3` is refused, because npm reads it as exact and Cargo as compatible. Write `^1.2.3` or `=1.2.3` instead. Ranges with two operators, such as `>=1.2 <1.5`, aren’t supported either.

### The caret before 1.0

Before 1.0, every minor version may break callers, so the caret treats the first non-zero part as the major version, as npm does:

| Requirement | Equivalent to    | Accepts                  |
| ----------- | ---------------- | ------------------------ |
| `^1.2.0`    | `>=1.2.0 <2.0.0` | Every 1.x from 1.2.0 on. |
| `^0.2.0`    | `>=0.2.0 <0.3.0` | The 0.2.x releases.      |
| `^0.2`      | `>=0.2.0 <0.3.0` | The 0.2.x releases.      |
| `^0.0.1`    | `>=0.0.1 <0.0.2` | Exactly 0.0.1.           |
| `^0`        | `>=0.0.0 <1.0.0` | Every 0.x.               |

Our explanation of [versions and releases](../explanations/packages.md#versions-and-releases) describes which changes raise which part.

### Pre-releases

A pre-release, such as `1.3.0-rc.1`, satisfies a requirement only when the requirement names a pre-release of the same version:

| Requirement   | `1.2.3-rc.2` | `1.2.3` | `1.3.0-rc.1` | `1.3.0` |
| ------------- | ------------ | ------- | ------------ | ------- |
| `^1.2`        | no           | yes     | no           | yes     |
| `^1.2.3-rc.1` | yes          | yes     | no           | yes     |
| `*`           | no           | yes     | no           | yes     |

## Releases

A release is a Git tag on the package’s repository whose name ends in `v` and a semantic version:

| The package sits…              | Its releases are tagged… | Example           |
| ------------------------------ | ------------------------ | ----------------- |
| in a folder named after its id | `<id>/v<version>`        | `suricata/v0.2.0` |
| at the root of the repository  | `v<version>`             | `v0.2.0`          |

When a repository has tags of the form `<id>/v<version>`, these are the releases of the package `<id>`, from its folder. Otherwise, the tags of the form `v<version>` are its releases, from the repository’s root. Tags that hold no semantic version after the `v` are no releases.

A locked release stays at its locked commit even when its tag moves or disappears, because the lock names the commit. Our library never changes a released tag, as our guide on [releasing a package](../guides/manage-packages.md#release-a-package) describes.

The platform lists a repository’s tags at most once a minute, so a new release can take a minute to be found. The **Packages** page of the app lists our library’s releases anew every 10 minutes.

## Resolution

Resolution turns every requirement into one lock, with exactly one version of each package. It collects the requirements from:

* The configuration’s `package.yaml`.
* The manifest of every package under the configuration’s `packages/`.
* The manifest of every package that it locks, which states what that package needs in turn.

A package of its own, outside a configuration, resolves the same way, with its own manifest in place of the configuration’s.

### Choosing a version

For each package, resolution tries the versions that every requirement on it accepts, the locked version first and then the newest release down. When a choice leads to a requirement that nothing can satisfy, it goes back and tries an older release of an earlier package. When no combination fits, it fails and names the requirements that clash, such as:

```text
`acme_common` 1.2.4 does not satisfy ^1.3 (`acme_firewall` 1.5.0), but ^1.2 (the workspace) chose it
```

Resolution fails rather than skip a release that it can’t fetch or read, such as one with a manifest that doesn’t parse, because skipping it would lock something other than what was asked for.

### Choosing a repository

Every requirement names a repository, our library or a `git` URL, and a `rev` if any. All requirements on a package must agree on both, with one exception: the repository and `rev` that the configuration’s own `package.yaml` names for a package hold for every package that asks for it. When the configuration names a fork, every package that uses the package gets the fork. Without such an entry, requirements that disagree fail resolution, and the message suggests listing the package in the configuration. Our guide on [overriding a package](../guides/manage-packages.md#override-a-package) uses this rule.

The packages under `packages/` don’t decide a repository for others. Only the configuration’s manifest does.

### Cycles

Packages that use each other, directly or through others, are refused, and so is a package that lists itself. Resolution goes back and tries other releases when a choice closes a cycle, and fails when every choice does.

### Modes

Resolution runs in one of two modes, which decide how far locked versions may move:

| Mode   | Commands                                                         | Locked versions                                                                                        |
| ------ | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Lock   | `package add`, `package remove`, `package lock`, `package fetch` | Every locked version that still satisfies all requirements stays. Others move to the newest that fits. |
| Update | `package update`, `package update <id>`                          | The named package and what it needs, or every package, move to the newest version that fits.           |

With `--latest`, `package update` first rewrites a requirement that rules out the newest stable release to `^<newest>`, then resolves in update mode. Without an id, it skips requirements pinned with `=`.

In both modes, a package that nothing asks for any more leaves the lock. Our reference on the [package commands](cli.md) lists what each command does.

## Visibility

A requirement makes a package visible only to whoever states it:

* A package sees its own operators and constants and those of the packages that its `dependencies` list.
* A configuration’s pipelines see the packages that the configuration’s `package.yaml` lists, including the ones it names with `path`.
* A package that only other packages depend on is locked and shipped to the deployment, but no pipeline can call it.

A package can therefore change its own dependencies without breaking whoever uses it. To call a package that another package pulls in, list it in your own `dependencies`. Our guide on [using other packages](../guides/manage-packages.md#use-other-packages) shows how.
