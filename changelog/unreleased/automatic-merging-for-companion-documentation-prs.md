---
title: Automatic merging for companion documentation PRs
type: feature
authors:
  - mavam
  - codex
prs:
  - 31
created: 2026-07-15T07:31:39.856318Z
---

The `tenzir-update-docs` skill now applies the `automerge` label to companion `tenzir/content` pull requests after cross-linking them. This opts them into CI that waits for the linked code PR and green docs checks before squash-merging.
