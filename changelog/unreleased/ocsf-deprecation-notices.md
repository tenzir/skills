---
title: OCSF deprecation notices
type: bugfix
authors:
  - zedoraps
prs:
  - 37
created: 2026-08-19T10:12:45.507392Z
---

The `tenzir-ocsf` skill now identifies deprecated OCSF classes, objects,
profiles, attributes, and enum values, including the version and recommended
replacement. For example, the OCSF 1.9.0 User Access Management page now
directs users to the User Management class.

This helps agents avoid obsolete schema elements when answering OCSF questions.
