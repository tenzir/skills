---
name: tenzir-microsoft-asim
description: Answer questions about Microsoft Sentinel ASIM (Advanced Security Information Model). Use whenever the user asks about ASIM schemas, normalized Microsoft Sentinel fields, aliases, entities, enumerations, schema mapping, or mapping events into ASIM.
---

# Microsoft Sentinel ASIM

Use this generated reference to answer Microsoft Sentinel ASIM schema and
mapping questions. The schema pages are generated from Azure Sentinel ASIM
YAML and are the local source of truth for field names, aliases, entities,
and enumerations. The guidance pages summarize Microsoft Learn semantics.

Read the relevant generated files before answering. Do not invent fields or
schema behavior that is not present in these files. When Learn guidance and
YAML disagree on field availability, treat the YAML-derived pages as the
schema source of truth and mention the difference if it matters.

## Source

- [Source summary](source.md)
- Requested ref: `master`
- Resolved commit: `0db4cc9a326a610d44000d6af1b7035432db74ba`

## File layout

```
source.md                         # Source refs, links, and counts
schemas.md                        # Schema index
schemas/{schema}.md               # Resolved schema fields
fields.md                         # Field index
fields/{field}.md                 # Field occurrences and aliases
enumerations.md                   # Enumeration values
entities.md                       # Entity fragment index
entities/{entity}.md              # Raw entity fragment fields
common.md                         # Common fragment index
common/{fragment}.md              # Raw common fragment fields
guidance.md                       # ASIM mapping guidance index
guidance/{topic}.md               # ASIM semantics and mapping guidance
```

## Question routing

| Question pattern | Start here |
| --- | --- |
| Which ASIM schema should I map this event to? | [Schema semantics](guidance/schema-semantics.md) -> [Schemas](schemas.md) -> candidate schema pages |
| What fields does schema X contain? | [Schemas](schemas.md) -> specific schema page |
| What does field X mean? | [Fields](fields.md) -> specific field page |
| Which field should an alias use? | [Fields](fields.md), then alias and target field pages |
| How do user/device/process roles map? | [Schema semantics](guidance/schema-semantics.md) and [Entities](entities.md) |
| Which enum values are allowed? | [Enumerations](enumerations.md) |
| What normalized content uses ASIM? | [Security content](guidance/security-content.md) |

When advising on mappings, prefer the normalized field over an alias for
reusable detections, rules, and workbooks. Use aliases mainly to explain
interactive query convenience.
