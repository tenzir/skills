---
name: tenzir-microsoft-asim
description: Answer questions about Microsoft Sentinel ASIM (Advanced Security Information Model). Use whenever the user asks about ASIM schemas, normalized Microsoft Sentinel fields, field classes, aliases, schema mapping, or mapping events and entities into ASIM.
---

# Microsoft Sentinel ASIM

Use this generated reference to answer Microsoft Sentinel ASIM schema and mapping questions.
The data files are optimized for agent context: load the smallest YAML file that answers the question, then follow cross-references only when needed.

Do not invent fields, aliases, enum values, schema versions, or schema behavior that is not present in the generated YAML data.

## Conceptual model

ASIM normalizes security telemetry from many products into source-independent records that can be queried consistently in Microsoft Sentinel.
A schema is the contract for one kind of activity or entity: event schemas describe activity records, while entity schemas describe standalone entity records.
A normalized event record identifies its contract with `EventSchema` and `EventSchemaVersion`; an entity record uses `EntitySchema` and `EntitySchemaVersion`.

Fields are schema-scoped contracts, not just names. A field can appear in several schemas with different classes, allowed values, conditions, or examples.
When mapping telemetry, load the schema file first and treat the selected schema's field records as authoritative.
Use field files only when you need a cross-schema view of one field.

Common fields describe shared event or entity metadata, such as time, product, result, severity, schema, and reporting device details.
Entity fields describe participants in an event. ASIM uses standard role prefixes such as `Src`, `Dst`, `Actor`, `Target`, `Acting`, and `Dvc` to distinguish those participants.
Logical types define the ASIM compatibility contract for a value, even when the underlying Log Analytics physical type is less specific.

Aliases are alternate names for analyst query convenience. Prefer canonical target fields when mapping data or writing reusable detections, rules, and workbooks.
When ASIM has no direct field for source-specific details, preserve the value in its original field or in `AdditionalFields`.

## Key terminology

| Term | Meaning |
| --- | --- |
| ASIM | Microsoft Sentinel's normalization model for source-independent security data. |
| Schema | A named field contract for an activity or entity, with a version and status. |
| Event schema | A schema for activity records such as DNS, authentication, network, process, registry, file, audit, alert, web, DHCP, agent, or user-management events. |
| Entity schema | A schema for a standalone entity record, such as the generated `AssetEntity` schema. |
| Field | A normalized attribute in a schema. Field records include class, type, role, description, constraints, examples, and documented constants when available. |
| Common field | A field shared across schemas. Schema-specific records can still constrain its value or meaning. |
| Role prefix | A prefix that identifies which participant a field describes, such as source, destination, actor, target, acting process, or reporting device. |
| Logical type | The ASIM type contract for a field value, such as `Enumerated`, `IP address`, `Hostname`, `SchemaVersion`, or `Date/time`. |
| Field class | A field's mapping priority and requirement level: `Mandatory`, `Recommended`, `Conditional`, `Optional`, or `Alias`. |
| Alias | A query-convenience field that points to one or more canonical fields. Use [data/aliases.yaml](data/aliases.yaml) to resolve it. |
| `value` | A documented constant for a field in a schema, such as `EventSchema: Dns`. |
| `allowed_values` | Documented normalized values for an enumerated or constrained field. |
| `required_if` | A condition that makes a conditional field required. |
| `AdditionalFields` | A dynamic field for source details that do not have a direct ASIM field. |

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
