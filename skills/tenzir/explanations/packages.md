---
title: "Packages"
description: "Understand what a package contains, how a configuration and its packages depend on each other by version, how releases work, and what our library offers."
canonical: https://tenzir.com/docs/explanations/packages
source: https://tenzir.com/docs/explanations/packages.md
section: "Docs"
---

# Packages

> Understand what a package contains, how a configuration and its packages depend on each other by version, how releases work, and what our library offers.

A **package** bundles reusable TQL for one use case, such as parsing and mapping the logs of one product: user-defined operators, constants, runnable examples, and tests. The pipelines of a [configuration](configuration.md) call the operators of the packages it depends on, so a mapping that someone wrote and tested once serves every pipeline that needs it, instead of being copied into each.

Packages depend on each other by version, the way libraries do in a programming language. This page explains what a package contains, how a configuration declares and locks the packages it uses, how the versions of many packages fit together, what a release promises, and what our library offers.

## What a package contains

A package is a folder with a manifest and TQL files:

* suricata/

  * package.yaml the manifest

  * operators/ user-defined operators, one per file

    * ocsf/

      * normalize.tql

  * constants.tql shared values, optional

  * examples/ runnable examples

    * onboard.tql

  * tests/ tests for the operators

    * …

  * changelog/ the changes in each release

    * …

- The **manifest** `package.yaml` names the package and describes it for the library: a display name, a description, an author, icons, and categories. Its `id` defaults to the folder name, and its `dependencies` list the other packages that its operators use.
- **Operators** are pipelines that you call like any builtin operator. Each file under `operators/` defines one, and its path sets the name.
- **Constants** are values that the operators share, such as a list of ports or a mapping table. An optional `constants.tql` next to the manifest defines them.
- **Examples** show how to use the operators, and the library displays them next to the package.
- **Tests** run the operators against sample data, so that a change to the package shows what it breaks before anyone deploys it.
- The **changelog** records what each release changes, and decides the number of the next release, as [versions and releases](packages.md#versions-and-releases) explains.

A package holds no pipelines and no contexts. These belong to the configuration, which decides what runs where, and a deployment refuses a package that contains either. Our reference on the [package layout](../reference/directory-layout.md) lists every file a package may contain.

## Modules

Every package is a **module** that namespaces its operators and constants with `::`. The package id comes first, and the path of an operator below `operators/` follows, so `suricata/operators/ocsf/normalize.tql` defines `suricata::ocsf::normalize`:

```tql
from_file "eve.json" {
  read_suricata
}
suricata::ocsf::normalize
```

Builtin operators and functions use flat names, such as [`where`](../reference/operators/where.md), so a package never shadows a builtin, and two packages never clash.

## Packages in a configuration

A configuration declares the packages its pipelines use in its own `package.yaml`, which holds nothing but `dependencies`:

package.yaml

```yaml
dependencies:
  suricata: "^1.2"
  acme:
    git: https://github.com/acme/tenzir-packages.git
    version: "^0.3"
  myteam:
    path: packages/myteam
```

A dependency comes from one of three places:

* **The library**: a version requirement on a package of [our library](packages.md#the-library), such as `"^1.2"`.
* **Another Git repository**: `git` names a public repository of packages on GitHub, with a `version` requirement on its releases or a `rev` that pins a commit or branch.
* **The configuration itself**: `path` names a package under `packages/` in the same repository. That’s where your own operators live, because a configuration has no `operators/` folder of its own.

Next to it, `package.lock` pins each dependency to one version, a commit, and a hash of its files, including the packages those depend on. The platform builds every configuration strictly from the lock: it fetches each locked package, checks it against its hash, and adds it to the archive that it sends to the deployment. The deployment never fetches a package itself, so it runs exactly the code that the commit locked, even if a newer release appears in the meantime.

A configuration’s package.yaml lists dependencies by version range, and package.lock pins each to a commit and a hash. The platform fetches the locked packages from the library or another Git repository, verifies their hashes, and adds them under packages/ to the archive next to the configuration’s own packages. The deployment’s pipelines call the operators of the direct dependencies, such as suricata::ocsf::normalize.

Our references on [dependencies](../reference/dependencies.md) and the [package lock](../reference/lock.md) spell out both files.

## Dependencies and resolution

A package declares its own `dependencies` in the same form as a configuration, so a mapping package can build on the operators of a shared helper package. Resolving turns all these declarations into one lock, and it follows a few rules.

### One version of each package

A configuration uses exactly one version of each package, however many packages ask for it. Requirements come from the configuration’s `package.yaml`, from every package under its `packages/` folder, and from every package that these pull in. Resolving looks for one version of each package that satisfies all of them at once. It prefers what the lock already pins and otherwise the newest release, and it goes back to older releases when a newer one conflicts with another requirement. When no combination fits, it fails and names the requirements that clash.

One version per package keeps a module name unambiguous: `suricata::ocsf::normalize` means the same operator in every pipeline and every package of a deployment. Packages also may not use each other in a cycle.

### The configuration decides where a package comes from

Every package that asks for another one names where it comes from, either our library or a Git repository. When these disagree, resolving fails, with one exception: a source that the configuration itself names wins for every package that asks for it. When the configuration depends on a fork of a package, all the packages that use it get the fork too, which is how you try a fix before its author releases it. Our guide on [overriding a package](../guides/manage-packages.md#override-a-package) shows how.

### Each package sees only what it declares

A package can call only its own operators and those of the packages it lists under `dependencies`. The same holds for a configuration’s pipelines, which see only the packages that its `package.yaml` lists. A package that only another package depends on is locked and shipped, but stays hidden. A package can therefore change its own dependencies without breaking the pipelines and packages that use it.

### Versions change only when you ask

Adding, removing, and locking packages keeps every locked version that still fits. Only an update moves a package to the newest version that its requirement accepts. A new release therefore never reaches your deployments by itself: it takes an update, a commit, and a deploy, as our guide on [updating packages](../guides/manage-packages.md#update-packages) walks through.

## Versions and releases

A release is a Git tag on the package’s repository. A package at the root of a repository is tagged `v1.2.3`, and a package in a folder of a repository that holds many packages is tagged with its folder in front, as in `suricata/v1.2.3`. The repository itself is the registry, so publishing a release takes nothing but a commit and a tag.

The released commit also states the version in the `version` field of the package’s `package.yaml`, as in `version: "1.2.3"`, and the field keeps that value until the next release. Resolving takes a release’s version from its tag, but a commit that is no release, such as a branch or a fork, has only its manifest to say which version it is.

### What a version promises

Versions follow [semantic versioning](https://semver.org/), applied to the callers of a package. A version number tells you whether your pipelines still compile after an update:

* A **breaking** change alters how callers use the package: it removes or renames an operator or constant, removes, renames, or retypes an argument, or makes an argument required. Some pipeline that calls the package has to change.
* A **change** alters only the data: an operator emits different events, for example because a mapping fills more OCSF attributes or fixes a wrong one, while every call stays valid.
* A **feature** adds an operator, a constant, or an optional argument.
* A **bug fix** fixes a defect.

Every entry in a package’s changelog has one of these types, and our [`tenzir-ship`](../reference/ship-framework.md) tool derives the next version from the entries since the last release:

| Highest entry type | Before 1.0 | From 1.0 on |
| ------------------ | ---------- | ----------- |
| Bug fix            | Patch      | Patch       |
| Feature or change  | Minor      | Minor       |
| Breaking change    | Minor      | Major       |

### What a requirement accepts

A requirement such as `^1.2` accepts version 1.2.0 and every later version that promises to stay compatible with it. From 1.0 on, that’s every 1.x release, so an update brings new features and data changes, but no change that breaks a call. Before 1.0, every minor version may break callers, so `^0.3` accepts only 0.3.x, and `^0.0.1` accepts only 0.0.1.

A data change can still matter to whatever consumes the events, such as a detection that matches on a field or a dashboard that counts one. Read the release notes before you update, or pin a package to one exact version with `=1.2.3` until you are ready.

## The library

Our library is a public Git repository at [github.com/tenzir/library](https://github.com/tenzir/library) with packages that we and the community maintain, under the Apache 2.0 license. It covers parsers and OCSF mappings for security products, sources and destinations, detections, and enrichment. A dependency that names no repository comes from the library, which is why `suricata: "^1.2"` is enough to use the Suricata package.

Every package in the library follows the same release process:

1. A contributor records each change in the package’s changelog and cuts the release in the same pull request.
2. CI checks the changelog, parses every TQL file, and runs the tests of each changed package against the latest Tenzir release and pre-release.
3. Once the pull request merges and CI passes, CI tags the release. A released version never changes afterwards.

You can browse the released packages and the use cases they cover in our [library catalog](https://tenzir.com/product/library.md), on the **Packages** page of the app, or with `tenzir package search`. Our guide on [contributing to the library](../guides/manage-packages.md#contribute-to-the-library) covers the pull request.

Tenzir 7.0 fetches packages only from public repositories on GitHub: our library or a repository of your own, as our guide on [hosting a package repository](../guides/manage-packages.md#host-a-package-repository) shows. A package that must stay private lives in your configuration under `packages/`.

## How package changes reach pipelines

A new package version reaches a deployment like any other change to the configuration: as a commit that updates `package.lock`, followed by a deploy. The deployment then compares what each pipeline compiles to, including the package operators it calls, and restarts exactly the pipelines whose compiled form changed. A pipeline that does not use the updated package keeps running. Our explanation of [what a deploy guarantees](configuration.md#what-a-deploy-guarantees) covers the details.

## See also

* [Configuration](configuration.md)
* [Manage packages](../guides/manage-packages.md#install-a-package)
* [Manage packages](../guides/manage-packages.md#update-packages)
* [Manage packages](../guides/manage-packages.md#create-a-package)
* [Manage packages](../guides/manage-packages.md#release-a-package)
* [Dependencies](../reference/dependencies.md)
