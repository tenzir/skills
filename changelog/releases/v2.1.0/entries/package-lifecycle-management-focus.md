---
title: Package lifecycle management focus
type: change
authors:
  - mavam
  - codex
prs:
  - 13
created: 2026-06-05T06:39:19.409916Z
---

The `tenzir-manage-packages` skill now focuses on package lifecycle management instead of package content development.

It routes agents through package surfaces such as manifests, UDO files, pipelines, examples, tests, changelog entries, and publishing while leaving operator implementation details to the relevant docs or specialized skills.
