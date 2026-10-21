---
title: OCSF schema parity with the official compiler
type: bugfix
authors:
  - zedoraps
created: 2026-10-21T05:24:59.679339Z
---

The `tenzir-ocsf` skill now matches the OCSF schema as the official OCSF
tooling resolves it, so agents see the same requirements, enum values, and
inherited attributes as the OCSF schema browser.

Previously, attributes that a class or object only partially redefined lost
details from their parent. For example, the Process Activity page didn't mark
`activity_id` and `actor` as required and omitted the `0` (Unknown) and `99`
(Other) activity values, and the Device page listed only two of the device
`type_id` values. Some required attributes, such as `time` and `activity_id` on
Detection Finding, were missing entirely. For OCSF 1.0.0 through 1.3.0, class
pages missed most Base Event attributes, including `class_uid` and `time`.

Additional fixes:

- Object pages list inherited attributes, applicable profiles, and the object's
  observable type ID. Profile pages list the objects they apply to.
- The types page shows observable type IDs, and the Observable page lists all
  observable `type_id` values.
- Class pages show the class-specific `class_uid` and `type_uid` values.
- Findings and Discovery are listed as base classes rather than event classes.
- Windows extension classes show their full class UID, for example `201001` for
  Registry Key Activity, and extension objects use their schema names, such as
  `reg_key`.
