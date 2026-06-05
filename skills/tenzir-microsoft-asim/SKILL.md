---
name: tenzir-microsoft-asim
description: Answer questions about Microsoft Sentinel ASIM (Advanced Security Information Model). Use whenever the user asks about ASIM schemas, normalized Microsoft Sentinel fields, field classes, aliases, schema mapping, or mapping events and entities into ASIM.
---

# Microsoft Sentinel ASIM

Use this generated reference to answer Microsoft Sentinel ASIM schema and mapping questions.
The data files are optimized for agent context: load the smallest YAML file that answers the question, then follow cross-references only when needed.

Do not invent fields, aliases, enum values, schema versions, or schema behavior that is not present in the generated YAML data.

## Data files

- Use [data/catalog.yaml](data/catalog.yaml) to choose a schema and find the schema data file.
- Use `data/schemas/<schema>.yaml` to map telemetry into one ASIM schema.
- Use [data/fields.yaml](data/fields.yaml) directly as the field-name to field-file manifest.
- Use `data/fields/<field>.yaml` for field meaning across schemas.
- Use [data/aliases.yaml](data/aliases.yaml) to resolve alias fields and conditional alias rules.

## Mapping rules

- Start from activity or entity semantics, choose the ASIM schema in [data/catalog.yaml](data/catalog.yaml), then load the schema file.
- Populate `Mandatory` and useful `Recommended` fields first, then add `Optional` fields when the source provides useful context.
- Populate `Conditional` fields when the field record's `required_if` condition applies.
- Prefer canonical normalized fields over aliases for reusable detections, analytics rules, workbooks, and mappings.
- Use aliases to explain Microsoft-documented query convenience, but resolve them through [data/aliases.yaml](data/aliases.yaml) before mapping.
- Preserve source-specific values in original fields or `AdditionalFields` when ASIM has no direct normalized field.
- When a schema defines both a value field and a type field, populate the type field when the identifier format is known.
- Treat fields with `role: common` as shared event/entity metadata, but obey schema-specific `value`, `allowed_values`, and `required_if` records.

## Field classes

| Class | Meaning |
| --- | --- |
| `Mandatory` | Populate for normalized records of that schema. |
| `Recommended` | Populate when the source provides enough information because it improves analytic value. |
| `Conditional` | Populate when the field record's condition applies. |
| `Optional` | Populate for useful context when the source provides it. |
| `Alias` | Query convenience field; prefer canonical target fields for reusable content. |

## Role prefixes

| Prefix | Role |
| --- | --- |
| `Src` | Source system, identity, or application initiating the activity. |
| `Dst` | Destination system, identity, or application targeted by the activity. |
| `Actor` | User or identity performing the operation. |
| `Target` | User, system, object, or application affected by the operation. |
| `Acting` | Process or application acting on behalf of an actor. |
| `Dvc` | Reporting device or collector unless the selected schema defines a more specific role. |

## Question routing

| Question pattern | Start here |
| --- | --- |
| Which ASIM schema should I map this event or entity to? | [data/catalog.yaml](data/catalog.yaml), then the selected schema file |
| What fields does schema X contain? | `data/schemas/<schema>.yaml` |
| What does field X mean? | [data/fields.yaml](data/fields.yaml), then `data/fields/<field>.yaml` |
| Which field should an alias use? | [data/aliases.yaml](data/aliases.yaml), then target field files |
| How do user/device/application roles map? | Role-prefix table above, then the selected schema file |
| What raw Microsoft source backs this data? | [source.md](source.md) |

For provenance, the pinned Microsoft Defender Docs commit, and raw source copies, use [source.md](source.md) as the last anchor.
