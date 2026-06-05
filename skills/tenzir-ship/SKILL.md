---
name: tenzir-ship
description: Use when adding changelog entries, creating release notes, cutting releases, and publishing them to GitHub.
---

# tenzir-ship

This skill bundles key release engineering use cases with tenzir-ship.

## Changelog history

Treat released changelog data as published history. Files under
`changelog/releases/`, including release notes, manifests, and release entry
files, are immutable once published because they may already exist in GitHub
releases, package registries, documentation, and downstream copies.

For normal follow-up work, add a new changelog entry on top of the existing
history. Edit historical release artifacts only for severe publication defects,
such as legally or operationally unsafe content, and only when the user
explicitly asks for that correction.

## Available scripts

- `bash <skill-dir>/scripts/detect-change-scope.sh`: Detects the current
  changelog scope. Use this before adding a changelog entry to identify whether
  staged, unstaged, or branch changes should drive the entry; the script prints
  a suggested diff command and the files in scope.

## Use Cases

### Initialize a changelog project

Set up a new changelog workspace before the first entry exists. Prefer the
explicit `init` command when the task is project setup rather than entry
creation.

Instructions: `references/init-changelog-project.md`

### Add a changelog entry

Add changelog entries as part of shipping bugfixes, changes, and features during
day-to-day development.

Instructions: `references/add-changelog-entry.md`

### Create a release

We distinguish two types of releases:

1. [Remote](references/create-remote-release.md): triggers a CI workflow
2. [Local](references/create-local-release.md): releases from a local repository

Prefer a remote release if a workflow exists, and use a local release otherwise.

## Documentation

When running into errors during the release process, obtain additional help
by reading the official documentation:

- <https://docs.tenzir.com/reference/ship-framework.md>
- <https://docs.tenzir.com/guides/packages/maintain-a-changelog.md>
