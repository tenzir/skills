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
- Use [data/fields.yaml](data/fields.yaml) as a field-name to field-file manifest.
- Use `data/fields/<field>.yaml` for field meaning across schemas.
- Use [data/aliases.yaml](data/aliases.yaml) to resolve alias fields and conditional alias rules.
- Use `data/guidance/*.yaml` for schema selection, common-field, entity-role, and normalized-content guidance.

## Question routing

| Question pattern | Start here |
| --- | --- |
| Which ASIM schema should I map this event or entity to? | [data/guidance/mapping.yaml](data/guidance/mapping.yaml), then [data/catalog.yaml](data/catalog.yaml) |
| What fields does schema X contain? | `data/schemas/<schema>.yaml` |
| What does field X mean? | [data/fields.yaml](data/fields.yaml), then `data/fields/<field>.yaml` |
| Which field should an alias use? | [data/aliases.yaml](data/aliases.yaml), then target field files |
| How do user/device/application roles map? | [data/guidance/entities.yaml](data/guidance/entities.yaml) and the selected schema file |
| What normalized content uses ASIM? | [data/guidance/content.yaml](data/guidance/content.yaml) |

For provenance, the pinned Microsoft Defender Docs commit, and raw source copies, use [source.md](source.md) as the last anchor.
