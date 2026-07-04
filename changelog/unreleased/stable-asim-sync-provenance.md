---
title: Stable ASIM sync provenance
type: bugfix
authors:
  - mavam
  - codex
created: 2026-07-04T08:37:09.076055Z
prs:
  - 29
---

Scheduled updates of the `tenzir-asim` skill no longer create release churn
when the Microsoft Defender Docs `public` branch moves but the copied ASIM
source content has not changed.

The generated provenance page still links to Microsoft's upstream files and
keeps local raw Markdown copies for audit, but branch movement alone no longer
rewrites every upstream link.
