---
title: Local skill marketplace loading
type: bugfix
authors:
  - mavam
prs:
  - 41
created: 2026-09-14T07:39:37.403899Z
---

The local Tenzir skills marketplace now loads and installs as a single `skills` plugin in Codex and Claude Code. This fixes the missing `source` error and mismatched plugin names. Individual skills remain discoverable with `npx skills`.
