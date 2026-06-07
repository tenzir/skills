---
name: tenzir-google-udm
description: Answer questions about Google SecOps / Chronicle UDM (Unified Data Model) record fields, normalization guidance, mapping logs to UDM event or entity objects, and generating UDM API ingestion payloads. Use whenever the user asks about UDM fields, event types, entity types, required fields, field formats, field-path prefixes for YARA-L, rules, Detect Engine, or CBN, records, enums, entity nouns, metadata.event_type / metadata.eventType, security_result / securityResult, network, Chronicle normalization, UDM API payloads, or Google SecOps ingestion endpoints.
---

# Google UDM

Google UDM (Unified Data Model) is the Google SecOps data model
for normalized security telemetry. It represents events and
entities as common records so logs from different products
can describe actors, assets, resources, network activity,
security outcomes, and product context with consistent field
names and enum values.

Use this skill for two primary workflows: mapping logs into
UDM event or entity objects for Google SecOps UDM API
ingestion, and referencing UDM fields in YARA-L, Detect
Engine, CBN, or other dotted field-path contexts. It also
answers which event or entity type to choose, which fields to
populate, and how Google expects values to be formatted.

## Field Name Forms

Record YAML files use field keys as the dotted field-path form.
When Google SecOps ingestion uses a different field name, the field
record adds an `ingestion_name` value:

`event_type: { ingestion_name: eventType, ... }`

Use the YAML field key for field names in YARA-L, Detect Engine, CBN,
and other dotted field-path contexts. Keep the root and prefix
required by that context, for example `$event.metadata.event_type`.
Use `ingestion_name` when mapping logs into UDM event or entity
records for Google SecOps UDM API ingestion, for example
`metadata.eventType`. If `ingestion_name` is absent, both contexts
use the YAML field key.

Current irregular mappings:

- `EntityRisk.DEPRECATED_risk_score` / `EntityRisk.DEPRECATEDRiskScore`

## Top-level Records

UDM uses two top-level data shapes: event records for telemetry and
entity records for contextual objects such as users, assets, domains,
files, URLs, and IP addresses.

The event ingestion path imports UDM events. Entity records are
ingested as entity context through the entity ingestion path.

### Event

| Field | Cardinality | Type | Description |
| --- | --- | --- | --- |
| `metadata` | `singular` | [`Metadata`](records/metadata.yaml) | Event metadata such as timestamp, source product, etc. |
| `additional` | `singular` | `variant` | Any important vendor-specific event data that cannot be adequately represented within the formal se... |
| `principal` | `singular` | [`Noun`](records/noun.yaml) | Represents the acting entity that originates the activity described in the event. The principal mus... |
| `src` | `singular` | [`Noun`](records/noun.yaml) | Represents a source entity being acted upon by the participant along with the device or process con... |
| `target` | `singular` | [`Noun`](records/noun.yaml) | Represents a target entity being referenced by the event or an object on the target entity. For exa... |
| `intermediary` | `repeated` | [`Noun`](records/noun.yaml) | Represents details on one or more intermediate entities processing activity described in the event.... |
| `observer` | `singular` | [`Noun`](records/noun.yaml) | Represents an observer entity (for example, a packet sniffer or network-based vulnerability scanner... |
| `about` | `repeated` | [`Noun`](records/noun.yaml) | Represents entities referenced by the event that are not otherwise described in principal, src, tar... |
| `security_result` / `securityResult` | `repeated` | [`SecurityResult`](records/security_result.yaml) | A list of security results. |
| `network` | `singular` | [`Network`](records/network.yaml) | All network details go here, including nested records with details on each protocol (for example, D... |
| `extensions` | `singular` | [`Extensions`](records/extensions.yaml) | All other first-class, event-specific metadata goes in this record. Do not place protocol metadata... |
| `extracted` | `singular` | `variant` | Flattened fields extracted from the log. |
| `grouped` | `optional` | [`GroupedFields`](records/grouped_fields.yaml) | Related UDM fields that are grouped together. |

### Entity

| Field | Cardinality | Type | Description |
| --- | --- | --- | --- |
| `metadata` | `singular` | [`EntityMetadata`](records/entity_metadata.yaml) | Entity metadata such as timestamp, product, etc. |
| `entity` | `singular` | [`Noun`](records/noun.yaml) | Noun in the UDM event that this entity represents. |
| `relations` | `repeated` | [`Relation`](records/relation.yaml) | One or more relationships between the entity (a) and other entities, including the relationship typ... |
| `additional` | `singular` | `variant` | Important entity data that cannot be adequately represented within the formal sections of the Entit... |
| `risk_score` / `riskScore` | `optional` | [`EntityRisk`](records/entity_risk.yaml) | Stores information related to the entity's risk score. |
| `metric` | `singular` | [`Metric`](records/metric.yaml) | Stores statistical metrics about the entity. Used if metadata.entity_type is METRIC. |

## Question routing

| Question pattern | Start here |
| --- | --- |
| What fields exist? | [Records](records.md) and the specific record YAML leaf |
| What values can enum X take? | [Enums](enums.md) -> specific enum page |
| How should I map this event? | [Event types](event-types.md), [Record field guidance](record-guidance.md), then relevant record YAML leaves |
| Which `metadata.event_type` / `metadata.eventType` should I use? | [Event type categories](event-type-categories.md), then [Event types](event-types.md) |
| Required or forbidden fields? | [Event types](event-types.md), [Entity types](entity-types.md), and [Record field guidance](record-guidance.md) |
| Field formats or examples? | [Record field guidance](record-guidance.md) and [Datatypes](datatypes.md) |
| How do I reference UDM fields in rules, Detect Engine, or CBN? | [Field paths](field-paths.md) |
| What are `principal`, `src`, `target`, `observer`, `intermediary`, or `about`? | [UDM record](records/udm.yaml) and [Noun](records/noun.yaml) |
| What fields exist for network/protocol details? | [Network](records/network.yaml) and protocol records such as DNS/HTTP/TLS/DHCP |
| What fields exist for entities? | [Entity](records/entity.yaml), [Entity types](entity-types.md), and [EntityMetadata](records/entity_metadata.yaml) |
| What is the top-level event record? | This file, then [UDM](records/udm.yaml) |

When a question asks for modeling guidance, read both layers.
Event, entity, and record guidance explains how Google says to
populate the data; record YAML leaves show the exact fields.
If they differ, state both facts instead of silently
reconciling them.

## Domain knowledge

- UDM events center on `metadata`, participant nouns (`principal`, `src`,
  `target`, `intermediary`, `observer`, `about`), `security_result` /
  `securityResult`, `network`, and `extensions`.
- UDM entities center on `metadata`, an `entity` noun, `relations`,
  optional `risk_score` / `riskScore`, and optional `metric` data.
- `metadata.event_type` / `metadata.eventType` classifies the event. It is
  the first place to look when deciding how an event should be represented.
- `metadata.entity_type` / `metadata.entityType` classifies entity records
  and drives entity-specific requirements.
- `Noun` carries entity details such as users, assets, processes, files,
  resources, cloud context, and labels.
