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
3. Add and commit a changelog entry. Do not create or edit changelog entries
   manually here; use the `tenzir-ship` skill for generating, formatting, and
   updating the entry.
4. If the change affects user-facing behavior documented on docs.tenzir.com,
   follow the `update-documentation` skill to open a companion docs PR and
   cross-link the two PRs.
5. Push the branch.

When doing follow-up edits, ensure that the changelog entries remain in sync
with the changed functionality by routing any entry updates through
`tenzir-ship` rather than editing changelog files by hand.

## PR body

Use this template for the pull request description:

```markdown
## 🔍 Problem

<!-- What is the problem, gap, or pain point this PR addresses? -->

## 🛠️ Solution

<!-- How does this PR address the problem? -->

## 💬 Review

<!-- Where should reviewers focus? Architecture decisions, trade-offs, risks, open questions. -->
```

Instructions:

- The target audience is a senior software engineer. Be brief and to the point.
- Replace each HTML comment with a terse explanation.
- Prefer bullet lists over elaborate prose.
- The diff speaks for itself, don't explain what files you changed.
