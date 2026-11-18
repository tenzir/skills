---
title: "Package lock file"
canonical: https://tenzir.com/docs/reference/lock
source: https://tenzir.com/docs/reference/lock.md
section: "Docs"
---

# Package lock file

> The package.lock file pins every package that a configuration uses to one version, one commit, and a hash of its files, including the packages that these use in turn. The package commands write it, and the platform builds a configuration strictly from it. This page lists its format, when it is stale, and how the platform and tenzir run use it. Our explanation of packages in a configuration describes the model behind it.

The `package.lock` file pins every package that a configuration uses to one version, one commit, and a hash of its files, including the packages that these use in turn. The [package commands](cli.md) write it, and the platform builds a configuration strictly from it. This page lists its format, when it is stale, and how the platform and `tenzir run` use it. Our explanation of [packages in a configuration](../explanations/packages.md#packages-in-a-configuration) describes the model behind it.

## Format

A lock is a YAML file with a fixed header:

package.lock

```yaml
# Written by tenzir. Do not edit by hand.
format: 1
packages:
  - id: acme_common
    version: 1.2.4
    git: https://github.com/acme/tenzir-packages.git
    path: acme_common
    commit: b96aadd68d804ee4c66a811965737b5874908db5
    hash: sha256:80473f2b087693648226d5a24a60cf4ec8a0dcee295cbc87cc0e7ebe09e88804
  - id: acme_firewall
    version: 1.5.0
    git: https://github.com/acme/tenzir-packages.git
    path: acme_firewall
    commit: b96aadd68d804ee4c66a811965737b5874908db5
    hash: sha256:b7d73cf25410bca2a53c8bd5d9da59e098fa737813a53e4b15a44986ff70df7f
    dependencies:
      acme_common:
        git: https://github.com/acme/tenzir-packages.git
        version: ^1.2
  - id: suricata
    version: 0.2.0
    git: https://github.com/tenzir/library.git
    path: suricata
    commit: e8956fbbbc707824077c1593c1dace17ce08b929
    hash: sha256:739f962ccd549abbf01ef5607a27aebda716479ca902a3015cca3ce11200b886
```

| Key        | Type    | Description                                                        |
| ---------- | ------- | ------------------------------------------------------------------ |
| `format`   | integer | The format of the lock. Always `1`.                                |
| `packages` | list    | One entry per locked package, ordered by id. Each id appears once. |

Don’t edit the lock by hand. To change what it pins, change `package.yaml` and run [`tenzir package lock`](cli.md#tenzir-package-lock), or use the other package commands. A lock in a format that the platform or the engine doesn’t read is refused, with a hint to write it again with `tenzir package lock`.

## Entries

Each entry in `packages` pins one package:

| Key            | Type    | Description                                                                                                                                                      |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`           | string  | The package id.                                                                                                                                                  |
| `version`      | string  | The locked version: a release’s version from its tag, or a pinned revision’s from its manifest. Absent for a pinned revision whose manifest states no `version`. |
| `git`          | string  | The URL of the repository that the package comes from.                                                                                                           |
| `path`         | string  | The package’s folder in the repository. Absent for a package at the repository’s root.                                                                           |
| `rev`          | string  | The revision that the dependency names, for a [pinned revision](dependencies.md#pinned-revisions). Absent for a release.       |
| `commit`       | string  | The full 40-character commit id that the package is locked at.                                                                                                   |
| `hash`         | string  | The [content hash](lock.md#content-hash) of the package’s files at that commit: `sha256:` and 64 lowercase hex digits.         |
| `dependencies` | mapping | What the package’s own manifest lists under `dependencies`, in the same form. Absent when it lists none.                                                         |

The `dependencies` of each entry make the lock complete on its own: Tenzir can tell whether a lock still fits without fetching a package.

Packages under the configuration’s `packages/` folder are never locked. They are part of the configuration’s own commit.

## Content hash

The hash covers every file in the package’s folder at the locked commit, not only its TQL files. It is the SHA-256 digest of the files in the order of their paths, each encoded as its path, a NUL byte, its length in bytes as a decimal number, a NUL byte, and its content:

```text
<path>\0<length>\0<content><path>\0<length>\0<content>…
```

A path is relative to the package’s folder and separated by `/`, such as `operators/ocsf/normalize.tql`. The following Python computes the hash of a package folder:

```python
import hashlib, pathlib


def content_hash(folder):
    root = pathlib.Path(folder)
    digest = hashlib.sha256()
    for path in sorted(p.relative_to(root).as_posix()
                       for p in root.rglob("*") if p.is_file()):
        content = (root / path).read_bytes()
        digest.update(f"{path}\0{len(content)}\0".encode() + content)
    return "sha256:" + digest.hexdigest()
```

Run it on a checkout of the locked commit, which holds no other files in the folder, to compare a package with its lock entry.

## Stale locks

A lock is **stale** when it no longer fits the manifests. That is the case when:

* A requirement asks for a package that the lock doesn’t pin.
* A requirement doesn’t accept the locked version, or a revision without a version where it asks for one.
* A requirement names another repository or `rev` than the lock, unless the configuration [decides the repository](dependencies.md#choosing-a-repository) for that package.
* The lock pins a package that nothing asks for any more.
* The lock pins a package that is also under the configuration’s `packages/`.
* A locked package asks for another one by `path`.
* The locked packages use each other in a cycle.

The check reads only the manifests and the lock and needs no network. The **Packages** page of the app shows a stale lock and offers to sync it, and [`tenzir package lock`](cli.md#tenzir-package-lock) writes it anew, keeping every locked version that still fits.

## Location

The lock lives at the root that it locks, next to the root’s `package.yaml`:

| The manifest belongs to…                      | Its packages are locked in…                          |
| --------------------------------------------- | ---------------------------------------------------- |
| a configuration                               | `package.lock` at the configuration’s root.          |
| a package under a configuration’s `packages/` | `package.lock` at the configuration’s root.          |
| a package of its own, outside a configuration | `package.lock` next to the package’s `package.yaml`. |

A configuration has one lock for its own manifest and every package under its `packages/`, so all its pipelines and packages share one version of each package. A package of its own has a lock so that you can run and test it with its dependencies. When the package is a dependency of another root, Tenzir ignores its lock and resolves its `dependencies` anew.

## Package cache

The `tenzir run` command never fetches a package. The commands on your machine unpack every locked package into a cache, which `tenzir run` loads it from:

```text
$XDG_CACHE_HOME/tenzir/packages/<hex digits of the hash>/
```

Without `XDG_CACHE_HOME`, or with a relative one, the cache is `~/.cache/tenzir/packages/`. Every command that writes the lock fills the cache, and [`tenzir package fetch`](cli.md#tenzir-package-fetch) fills it for a lock that someone else wrote, such as after a `git pull`. Each folder holds exactly the files that its hash covers: an entry that doesn’t match its hash is fetched again. The Git clones that the commands fetch from also live under `$XDG_CACHE_HOME/tenzir/`.

When `tenzir run` starts in a configuration or a package, it loads each locked package from the cache by its hash. A package that isn’t there fails the run with a message that suggests `tenzir package fetch`. A requirement that the lock doesn’t pin fails it with a message that suggests `tenzir package lock`. Beyond that, `tenzir run` doesn’t check whether the lock is stale, so run `tenzir package fetch --locked` to check it before a run.

## Builds on the platform

When the platform builds a configuration’s commit for a deploy, it takes the packages from the lock and resolves nothing:

1. It refuses the commit if the lock is [stale](lock.md#stale-locks) or names a repository that it may not fetch from.
2. It refuses the commit if files of the configuration lie under `packages/<id>/` for a locked package `<id>`, where that package goes.
3. It fetches every locked package at its commit and checks the files against the hash. A package that differs from its hash fails the build.
4. It adds the files of each package under `packages/<id>/` to the archive that it sends to the deployment, next to the configuration’s own packages.

The deployment never fetches a package itself. It runs exactly the code that the commit locked, even when a newer release appears or a tag moves. The archive is subject to the size limits that our reference on the [package layout](directory-layout.md#size-limits) lists.
