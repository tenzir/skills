---
name: tenzir-google-udm
description: Answer questions about Google SecOps / Chronicle UDM (Unified Data Model) schema. Use whenever the user asks about UDM fields, event types, messages, enums, entity nouns, metadata, security_result, network, Chronicle normalization, or Google SecOps event schema.
---

# Google UDM

Look up the generated Google UDM schema reference and answer from those
files. The reference is generated from `backstory/udm.proto`, which is
the ground truth for this skill. Only state schema facts from files you
read. If the generated files do not cover the question, say so.

## Source

- [Schema summary](schema.md)
- Source ref: `master`
- Resolved commit: `5ff4b410beb15f65d3d0b7a160f52d803bce7c97`

## File layout

```
schema.md                  # Source, counts, imports, top-level UDM fields
messages.md                # Message index
messages/{message}.md      # Message fields and nested types
enums.md                   # Enum index
enums/{enum}.md            # Enum values
event-types.md             # Dedicated Metadata.EventType reference
```

## Question routing

| Question pattern | Start here |
| --- | --- |
| What fields does UDM/message X have? | [Messages](messages.md) -> specific message page |
| What values can enum X take? | [Enums](enums.md) -> specific enum page |
| Which `metadata.event_type` should I use? | [Event types](event-types.md), then candidate message pages |
| What are `principal`, `src`, `target`, `observer`, `intermediary`, or `about`? | [UDM message](messages/udm.md) and [Noun](messages/noun.md) |
| What fields exist for network/protocol details? | [Network](messages/network.md), then protocol messages such as DNS, HTTP, TLS, DHCP |
| What fields exist for detections or alerts? | [SecurityResult](messages/security_result.md) and related nested enums |
| What is the top-level event shape? | [Schema summary](schema.md) and [UDM](messages/udm.md) |

When a question asks for modeling guidance, read the relevant event type,
top-level UDM noun fields, and candidate message pages. Explain what the
proto comments say and call out any requirement that is not represented in
the generated reference.

## Domain knowledge

- UDM events center on `metadata`, participant nouns (`principal`, `src`,
  `target`, `intermediary`, `observer`, `about`), `security_result`,
  `network`, and `extensions`.
- `metadata.event_type` classifies the event. It is the first place to look
  when deciding how an event should be represented.
- `Noun` carries entity details such as users, assets, processes, files,
  resources, cloud context, and labels.
- The generated Google UDM field list is derived from the proto. Use this
  skill's proto-derived files as the local source of truth.

## Answering principles

- Read before answering. Every schema claim must trace back to a generated
  file in this skill.
- Prefer exact field names, enum names, and message names from the reference.
- Distinguish proto structure from mapping policy. If a required-field or
  validation rule is not in the generated files, say it is not covered here.
- Do not invent UDM semantics from memory.
