# Maintain a changelog


This guide shows you how to maintain changelogs for packages using [`tenzir-ship`](../../reference/ship-framework.md).

## Add an entry

Run `tenzir-ship add` from your package directory while preparing a pull request. The CLI prompts for title, type, and description, and infers the author automatically.

```sh
uvx tenzir-ship add
```

The first invocation scaffolds a `changelog/` subdirectory automatically.

## Release a package

When you’re ready to release, create the release manifest:

```sh
uvx tenzir-ship release create --minor --yes
```

Then publish to GitHub:

```sh
uvx tenzir-ship release publish --commit --tag --yes
```

This commits staged changes, creates a git tag, and publishes the GitHub release.

## Release a library

A library acts as a parent workspace containing multiple packages as modules. When releasing the library:

1. Release each package that has unreleased changes
2. Create the library release—it automatically aggregates module changes

```sh
# From the library root
uvx tenzir-ship release create --minor --yes
```

The release notes include a summary section for each module with changes since the previous library release.

## See also

* [Ship Framework](../../reference/ship-framework.md)
* [Write a package](../../tutorials/write-a-package.md)