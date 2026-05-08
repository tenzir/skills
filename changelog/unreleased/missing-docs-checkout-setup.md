---
title: Missing docs checkout setup
type: bugfix
authors:
  - mavam
  - codex
prs:
  - 4
created: 2026-05-08T09:19:22.180798Z
---

The docs update workflow now tells agents to clone `.docs` when the checkout is missing, so documentation updates can proceed in repositories that do not already have the docs repository checked out.
