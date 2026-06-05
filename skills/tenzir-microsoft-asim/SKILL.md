---
name: tenzir-microsoft-asim
description: Answer questions about Microsoft Sentinel ASIM (Advanced Security Information Model). Use whenever the user asks about ASIM schemas, normalized Microsoft Sentinel fields, field classes, aliases, schema mapping, or mapping events and entities into ASIM.
---

# Microsoft Sentinel ASIM

Microsoft Sentinel ASIM (Advanced Security Information Model) normalizes security telemetry from many products into source-independent records that analysts can query consistently.
Use this skill to choose the right ASIM schema, inspect normalized fields, resolve aliases, explain field classes and logical types, and map events or entities into ASIM.

The generated YAML files are the authoritative reference for this skill.
If a field, alias, enum value, schema version, condition, or schema behavior is not present in the YAML data, say that it is not documented here.
Use [source.md](source.md) only as the final provenance anchor for the pinned Microsoft Defender Docs commit and raw Markdown copies.

## How ASIM fits together

ASIM is organized around schemas.
A schema is a named contract for one kind of activity or entity, with a version, status, and field set.
Event schemas describe activity records such as DNS, authentication, network, process, registry, file, audit, alert, web, DHCP, agent, and user-management events.
Entity schemas describe standalone entity records, such as `AssetEntity`.
A normalized event record identifies its contract with `EventSchema` and `EventSchemaVersion`; an entity record uses `EntitySchema` and `EntitySchemaVersion`.

Fields are schema-scoped contracts, not just names. A field can appear in several schemas with different classes, allowed values, conditions, or examples.
Common fields describe shared event or entity metadata, such as time, product, result, severity, schema, and reporting device details.
Entity fields describe participants in an event. ASIM uses role prefixes such as `Src`, `Dst`, `Actor`, `Target`, `Acting`, and `Dvc` to distinguish those participants.
Logical types define the ASIM compatibility contract for a value, even when the underlying Log Analytics physical type is less specific.

A field class describes mapping priority and requirement level: `Mandatory`, `Recommended`, `Conditional`, `Optional`, or `Alias`.
Aliases are query-convenience names that point to one or more canonical fields; prefer canonical target fields when mapping data or writing reusable detections, rules, and workbooks.
`value` records document schema constants, `allowed_values` records document normalized enum values, and `required_if` records document when a conditional field is required.
When ASIM has no direct field for source-specific details, preserve the value in its original field or in `AdditionalFields`.

For mapping work, start with the activity or entity semantics, choose the schema, and treat that schema file as authoritative.
Use field files only when you need a cross-schema view of one field.

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
