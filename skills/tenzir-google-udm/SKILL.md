---
name: tenzir-google-udm
description: Answer questions about Google SecOps / Chronicle UDM (Unified Data Model) schema and normalization guidance. Use whenever the user asks about UDM fields, event types, entity types, required fields, field formats, field-path prefixes, messages, enums, entity nouns, metadata, securityResult, network, Chronicle normalization, or Google SecOps event schema.
---

# Google UDM

Look up the generated Google UDM schema and usage references before
answering. The schema pages are generated from `backstory/udm.proto`
and `backstory/entity.proto`; they are the ground truth for field
existence, REST field keys, types, oneofs, and deprecation.
The guidance sections are generated from targeted Google documentation;
they are the source for population policy, required fields,
field-path prefixes, datatype notes, and examples.

## Source

- [Schema summary](schema.md)
- [Usage guidance](usage.md)
- Source ref: `master`
- Resolved commit: `0db4dc67dd805d20294c6dc34068c37f546d71da`
- Usage guide last updated: `2026-06-03 UTC`
- Field list last updated: `2026-06-03 UTC`

## File layout

```
schema.md                  # Proto sources and top-level UDM and Entity fields
messages.md                # Message index
messages/{message}.md      # Message fields and population guidance
enums.md                   # Enum index
enums/{enum}.md            # Enum values
event-types.md             # EventType values and event guidance
usage.md                   # Guidance source summary and routing
field-paths.md             # Rules, Detect Engine, and CBN prefixes
datatypes.md               # Standard datatype notes
```

## Question routing

| Question pattern | Start here |
| --- | --- |
| What fields exist? | [Schema](schema.md), [Messages](messages.md), and specific message page |
| What values can enum X take? | [Enums](enums.md) -> specific enum page |
| How should I map this event? | [Event types](event-types.md), then relevant message pages |
| Which `metadata.eventType` should I use? | [Event type categories](event-type-categories.md), then [Event types](event-types.md) |
| Required or forbidden fields? | [Event types](event-types.md), [Entity](messages/entity.md), or relevant message page |
| Field formats or examples? | Relevant message page guidance and [Datatypes](datatypes.md) |
| Which field path prefix? | [Field paths](field-paths.md) |
| What are `principal`, `src`, `target`, `observer`, `intermediary`, or `about`? | [UDM message](messages/udm.md) and [Noun](messages/noun.md) |
| What fields exist for network/protocol details? | [Network](messages/network.md) and protocol messages such as DNS/HTTP/TLS/DHCP |
| What fields exist for entities? | [Entity](messages/entity.md) and [EntityMetadata](messages/entity_metadata.md) |
| What is the top-level event shape? | [Schema summary](schema.md) and [UDM](messages/udm.md) |

When a question asks for modeling guidance, read both layers.
Message, event, or entity guidance explains how Google says to
populate the data; schema pages show the exact field structure.
If they differ, state both facts and identify which source each
fact comes from.

## Domain knowledge

- UDM events center on `metadata`, participant nouns (`principal`, `src`,
  `target`, `intermediary`, `observer`, `about`), `securityResult`,
  `network`, and `extensions`.
- UDM entities center on `metadata`, an `entity` noun, `relations`,
  optional `risk_score`, and optional `metric` data.
- `metadata.eventType` classifies the event. It is the first place to look
  when deciding how an event should be represented.
- `metadata.entityType` classifies entity records and drives entity-specific
  requirements.
- `Noun` carries entity details such as users, assets, processes, files,
  resources, cloud context, and labels.

## Answering principles

- Read before answering. Every schema or guidance claim must trace back to
  a generated file in this skill.
- Prefer exact field names, enum names, and message names from the reference.
- Distinguish proto structure from mapping policy. Required-field and
  population rules come from generated guidance sections, not from
  proto field presence.
- Do not invent UDM semantics from memory.
