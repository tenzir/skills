---
name: tenzir-ship
description: >-
  Use when adding changelog entries, creating release notes, cutting releases,
  publishing them to GitHub, or when the user says "release this", "ship it",
  "add a changelog entry", "what changed", "prepare a release", or "bump the
  version." Also use for any release engineering task involving tenzir-ship.
metadata:
  requires:
    skills:
      - technical-writing
---

# tenzir-ship

This skill bundles key release engineering use cases with tenzir-ship.

## Use Cases

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
