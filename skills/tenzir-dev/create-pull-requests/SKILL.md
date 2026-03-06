---
name: create-pull-requests
description: >-
  Ship changes via pull request in Tenzir projects. Use when opening PRs,
  adding changelog entries, and performing follow-up changes.
metadata:
  requires:
    skills:
      - commit-changes
      - update-documentation
---

# Create Pull Requests

Create pull requests and keep their changelog current.

## Workflow

1. Ensure the code changes are committed in coherent units.
2. Create a pull request from the current worktree branch.
3. Add and commit a changelog entry.
4. Push the branch.

When doing follow-up edits, ensure that the changelog entries remains in sync
with the changed functionatliy.
