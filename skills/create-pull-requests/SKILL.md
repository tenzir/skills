---
name: create-pull-requests
description: >-
  Ship changes via pull request in Tenzir projects. Use when the user wants to
  open a PR, push a branch, add or update changelog entries, create a pull
  request for review, or when they say "ship this", "open a PR", "send this for
  review", or "push and create a pull request." Also use for follow-up changes
  to an existing PR.
metadata:
  requires:
    skills:
      - commit-changes
      - tenzir-ship
      - update-documentation
---

# Create Pull Requests

Create pull requests and keep their changelog current.

## Workflow

1. Ensure changes are committed in coherent units. Use the `commit-changes`
   skill for staging, splitting, and writing commit messages.
2. Create a pull request from the current worktree branch.
3. Add and commit a changelog entry. Use the `tenzir-ship` skill for writing
   and formatting the entry.
4. If the change affects user-facing behavior documented on docs.tenzir.com,
   follow the `update-documentation` skill to open a companion docs PR and
   cross-link the two PRs.
5. Push the branch.

When doing follow-up edits, ensure that the changelog entries remain in sync
with the changed functionality.
