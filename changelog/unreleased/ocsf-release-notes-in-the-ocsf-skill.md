---
title: OCSF release notes in the OCSF skill
type: feature
authors:
  - zedoraps
created: 2026-10-22T16:35:28.147942Z
---

The `tenzir-ocsf` skill now includes the upstream OCSF release notes for each
schema version, so agents can answer what changed in a release beyond the
added and removed classes, objects, and profiles.

Each version directory has a `changelog.md` with that release's section of the
OCSF changelog, for example `v1.9.0/changelog.md`. The development snapshot
carries the unreleased changes. Entries link to the upstream pull requests.
