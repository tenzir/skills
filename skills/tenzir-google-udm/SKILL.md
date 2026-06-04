---
name: tenzir-google-udm
description: Answer questions about Google SecOps / Chronicle UDM (Unified Data Model) field structure and normalization guidance. Use whenever the user asks about UDM fields, event types, entity types, required fields, field formats, field-path prefixes, messages, enums, entity nouns, metadata, securityResult, network, Chronicle normalization, or Google SecOps ingestion endpoints.
---

# Google UDM

Google UDM (Unified Data Model) is the Google SecOps data model
for normalized security telemetry. It represents events and
entities in a common structure so logs from different products
can describe actors, assets, resources, network activity,
security outcomes, and product context with consistent field
names and enum values.

Use this skill to answer how a log should map to UDM, which
event or entity type to choose, which UDM fields to populate,
and how Google expects values and field paths to be formatted.

## Top-level structure

UDM uses two top-level data shapes: event records for telemetry and
entity records for contextual objects such as users, assets, domains,
files, URLs, and IP addresses.

The event ingestion path imports UDM events. Entity records are
ingested as entity context through the entity ingestion path.

### Event

| Field | Cardinality | Type | Description |
| --- | --- | --- | --- |
| `metadata` | `singular` | [`Metadata`](messages/metadata.md) | Event metadata such as timestamp, source product, etc. |
| `additional` | `singular` | `object` | Any important vendor-specific event data that cannot be adequately represented within the formal se... |
| `principal` | `singular` | [`Noun`](messages/noun.md) | Represents the acting entity that originates the activity described in the event. The principal mus... |
| `src` | `singular` | [`Noun`](messages/noun.md) | Represents a source entity being acted upon by the participant along with the device or process con... |
| `target` | `singular` | [`Noun`](messages/noun.md) | Represents a target entity being referenced by the event or an object on the target entity. For exa... |
| `intermediary` | `repeated` | [`Noun`](messages/noun.md) | Represents details on one or more intermediate entities processing activity described in the event.... |
| `observer` | `singular` | [`Noun`](messages/noun.md) | Represents an observer entity (for example, a packet sniffer or network-based vulnerability scanner... |
| `about` | `repeated` | [`Noun`](messages/noun.md) | Represents entities referenced by the event that are not otherwise described in principal, src, tar... |
| `securityResult` | `repeated` | [`SecurityResult`](messages/security_result.md) | A list of security results. |
| `network` | `singular` | [`Network`](messages/network.md) | All network details go here, including sub-messages with details on each protocol (for example, DHC... |
| `extensions` | `singular` | [`Extensions`](messages/extensions.md) | All other first-class, event-specific metadata goes in this message. Do not place protocol metadata... |
| `extracted` | `singular` | `object` | Flattened fields extracted from the log. |
| `grouped` | `optional` | [`GroupedFields`](messages/grouped_fields.md) | Related UDM fields that are grouped together. |

### Entity

| Field | Cardinality | Type | Description |
| --- | --- | --- | --- |
| `metadata` | `singular` | [`EntityMetadata`](messages/entity_metadata.md) | Entity metadata such as timestamp, product, etc. |
| `entity` | `singular` | [`Noun`](messages/noun.md) | Noun in the UDM event that this entity represents. |
| `relations` | `repeated` | [`Relation`](messages/relation.md) | One or more relationships between the entity (a) and other entities, including the relationship typ... |
| `additional` | `singular` | `object` | Important entity data that cannot be adequately represented within the formal sections of the Entit... |
| `riskScore` | `optional` | [`EntityRisk`](messages/entity_risk.md) | Stores information related to the entity's risk score. |
| `metric` | `singular` | [`Metric`](messages/metric.md) | Stores statistical metrics about the entity. Used if metadata.entityType is METRIC. |

## Question routing

| Question pattern | Start here |
| --- | --- |
| What fields exist? | [Messages](messages.md) and the specific message page |
| What values can enum X take? | [Enums](enums.md) -> specific enum page |
| How should I map this event? | [Event types](event-types.md), then relevant message pages |
| Which `metadata.eventType` should I use? | [Event type categories](event-type-categories.md), then [Event types](event-types.md) |
| Required or forbidden fields? | [Event types](event-types.md), [Entity](messages/entity.md), or relevant message page |
| Field formats or examples? | Relevant message page guidance and [Datatypes](datatypes.md) |
| Which field path prefix? | [Field paths](field-paths.md) |
| What are `principal`, `src`, `target`, `observer`, `intermediary`, or `about`? | [UDM message](messages/udm.md) and [Noun](messages/noun.md) |
| What fields exist for network/protocol details? | [Network](messages/network.md) and protocol messages such as DNS/HTTP/TLS/DHCP |
| What fields exist for entities? | [Entity](messages/entity.md) and [EntityMetadata](messages/entity_metadata.md) |
| What is the top-level event shape? | This file, then [UDM](messages/udm.md) |

When a question asks for modeling guidance, read both layers.
Message, event, or entity guidance explains how Google says to
populate the data; message pages show the exact field structure.
If they differ, state both facts instead of silently
reconciling them.

## Domain knowledge

- UDM events center on `metadata`, participant nouns (`principal`, `src`,
  `target`, `intermediary`, `observer`, `about`), `securityResult`,
  `network`, and `extensions`.
- UDM entities center on `metadata`, an `entity` noun, `relations`,
  optional `riskScore`, and optional `metric` data.
- `metadata.eventType` classifies the event. It is the first place to look
  when deciding how an event should be represented.
- `metadata.entityType` classifies entity records and drives entity-specific
  requirements.
- `Noun` carries entity details such as users, assets, processes, files,
  resources, cloud context, and labels.
