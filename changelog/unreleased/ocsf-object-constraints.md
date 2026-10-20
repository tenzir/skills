---
title: OCSF object constraints
type: bugfix
authors:
  - zedoraps
prs:
  - 42
created: 2026-10-20T21:52:33.205744Z
---

The `tenzir-ocsf` skill now lists the attribute constraints of OCSF objects,
not just those of event classes. For example, the Network Endpoint page now
states that at least one of `ip`, `uid`, `name`, `hostname`, `svc_name`,
`instance_uid`, `interface_uid`, `interface_name`, or `domain` must be set, and
the Vulnerability page states that exactly one of `advisory`, `cve`, or `cwe`
applies. Objects that inherit constraints from a parent object, such as Device
from Endpoint, show the inherited rules.

This helps agents produce OCSF events that satisfy the schema's "at least one
of" and "exactly one of" requirements on nested objects.
