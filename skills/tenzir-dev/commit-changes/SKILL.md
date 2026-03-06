---
name: commit-changes
description: >-
  Commit changes in Tenzir projects. Use when committing changes into a local
  git repository.
---

# Commit Changes

Commit changes as clean, reviewable snapshots.

## Workflow

### 1. Gather change context

Gather `git` context to identify what changed.

### 2. Run project checks

Run the project's relevant linters, type checkers, and formatters.

### 3. Perform commits

Split orthogonal changes into separate logical units. For each unit:

1. Stage the relevant files.
2. [Create the commit message](references/write-commit-messages.md).
3. Perform the commit.
