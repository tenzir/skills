# Google UDM schema

Generated from the canonical Google UDM protocol buffer definitions.

- **Sources**:
  - [backstory/udm.proto](https://github.com/googleapis/googleapis/blob/0db4dc67dd805d20294c6dc34068c37f546d71da/backstory/udm.proto)
  - [backstory/entity.proto](https://github.com/googleapis/googleapis/blob/0db4dc67dd805d20294c6dc34068c37f546d71da/backstory/entity.proto)
- **Requested ref**: `master`
- **Resolved commit**: `0db4dc67dd805d20294c6dc34068c37f546d71da`

## Imports

- `backstory/data_access.proto`
- `backstory/entity.proto`
- `backstory/entity_risk.proto`
- `backstory/id.proto`
- `google/type/interval.proto`
- `google/type/latlng.proto`

## Indexes

- [Messages](messages.md)
- [Enums](enums.md)
- [Event types](event-types.md)
- [Usage guidance](usage.md)

## Top-level UDM event fields

| Field | Cardinality | Type | Description |
| --- | --- | --- | --- |
| `metadata` | `singular` | [`Metadata`](messages/metadata.md) | Event metadata such as timestamp, source product, etc. |
| `additional` | `singular` | `google.protobuf.Struct` | Any important vendor-specific event data that cannot be adequately represented within the formal se... |
| `principal` | `singular` | [`Noun`](messages/noun.md) | Represents the acting entity that originates the activity described in the event. The principal mus... |
| `src` | `singular` | [`Noun`](messages/noun.md) | Represents a source entity being acted upon by the participant along with the device or process con... |
| `target` | `singular` | [`Noun`](messages/noun.md) | Represents a target entity being referenced by the event or an object on the target entity. For exa... |
| `intermediary` | `repeated` | [`Noun`](messages/noun.md) | Represents details on one or more intermediate entities processing activity described in the event.... |
| `observer` | `singular` | [`Noun`](messages/noun.md) | Represents an observer entity (for example, a packet sniffer or network-based vulnerability scanner... |
| `about` | `repeated` | [`Noun`](messages/noun.md) | Represents entities referenced by the event that are not otherwise described in principal, src, tar... |
| `securityResult` | `repeated` | [`SecurityResult`](messages/security_result.md) | A list of security results. |
| `network` | `singular` | [`Network`](messages/network.md) | All network details go here, including sub-messages with details on each protocol (for example, DHC... |
| `extensions` | `singular` | [`Extensions`](messages/extensions.md) | All other first-class, event-specific metadata goes in this message. Do not place protocol metadata... |
| `extracted` | `singular` | `google.protobuf.Struct` | Flattened fields extracted from the log. |
| `grouped` | `optional` | [`GroupedFields`](messages/grouped_fields.md) | Related UDM fields that are grouped together. |

## Top-level Entity graph fields

| Field | Cardinality | Type | Description |
| --- | --- | --- | --- |
| `metadata` | `singular` | [`EntityMetadata`](messages/entity_metadata.md) | Entity metadata such as timestamp, product, etc. |
| `entity` | `singular` | [`Noun`](messages/noun.md) | Noun in the UDM event that this entity represents. |
| `relations` | `repeated` | [`Relation`](messages/relation.md) | One or more relationships between the entity (a) and other entities, including the relationship typ... |
| `additional` | `singular` | `google.protobuf.Struct` | Important entity data that cannot be adequately represented within the formal sections of the Entit... |
| `riskScore` | `optional` | [`EntityRisk`](messages/entity_risk.md) | Stores information related to the entity's risk score. |
| `metric` | `singular` | [`Metric`](messages/metric.md) | Stores statistical metrics about the entity. Used if metadata.entityType is METRIC. |
