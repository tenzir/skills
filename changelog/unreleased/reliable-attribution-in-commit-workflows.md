---
title: Reliable attribution in commit workflows
type: bugfix
authors:
  - mavam
  - codex
prs:
  - 34
created: 2026-08-09T17:22:40.245896Z
---

The `tenzir-commit-changes` skill no longer asks agents to generate `Assisted-by` trailers. This prevents inaccurate model and harness attribution when runtime identity is unavailable; runtime-aware tooling can add provenance instead.
