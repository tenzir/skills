---
title: Structured YAML schema data in the OCSF skill
type: change
authors:
  - zedoraps
created: 2026-10-21T08:23:40.782693Z
---

The `tenzir-ocsf` skill now provides the OCSF schema as structured YAML instead
of Markdown pages, so agents get exact, complete schema data for every class
and object.

Each version directory contains indexes (`classes.yaml`, `objects.yaml`,
`profiles.yaml`, `categories.yaml`, `types.yaml`, `attributes.yaml`,
`version.yaml`) and one fully resolved file per class and object, for example
`v1.9.0/classes/process_activity.yaml`. Each file lists every attribute,
including inherited attributes, optional attributes, and attributes added by
profiles, together with requirement levels, enum values, constraints,
associations, observable type IDs, and deprecation details:

```yaml
attributes:
  actor:
    caption: Actor
    type: object_t
    object: actor
    requirement: required
    group: primary
```

Objects now list the classes and objects that reference them, and the attribute
dictionary lists where each attribute is used. Extension classes, objects, and
patches of core items live under `{version}/extensions/{extension}/`. The OCSF
introduction, FAQs, and articles moved to `docs/`.
