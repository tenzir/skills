# Google UDM schema

Generated from the canonical Google UDM protocol buffer definitions.

- **Sources**:
  - [backstory/udm.proto](https://github.com/googleapis/googleapis/blob/0db4dc67dd805d20294c6dc34068c37f546d71da/backstory/udm.proto)
  - [backstory/entity.proto](https://github.com/googleapis/googleapis/blob/0db4dc67dd805d20294c6dc34068c37f546d71da/backstory/entity.proto)
- **Requested ref**: `master`
- **Resolved commit**: `0db4dc67dd805d20294c6dc34068c37f546d71da`
- **Package**: `google.backstory`
- **Messages**: `129`
- **Enums**: `70`
- **Fields**: `1030`
- **Enum values**: `1012`

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

| Field | No. | Cardinality | Type | Description |
| --- | ---: | --- | --- | --- |
| `metadata` | `1` | `singular` | [`Metadata`](messages/metadata.md) | Event metadata such as timestamp, source product, etc. |
| `additional` | `2` | `singular` | `google.protobuf.Struct` | Any important vendor-specific event data that cannot be adequately represented within the formal se... |
| `principal` | `3` | `singular` | [`Noun`](messages/noun.md) | Represents the acting entity that originates the activity described in the event. The principal mus... |
| `src` | `4` | `singular` | [`Noun`](messages/noun.md) | Represents a source entity being acted upon by the participant along with the device or process con... |
| `target` | `5` | `singular` | [`Noun`](messages/noun.md) | Represents a target entity being referenced by the event or an object on the target entity. For exa... |
| `intermediary` | `6` | `repeated` | [`Noun`](messages/noun.md) | Represents details on one or more intermediate entities processing activity described in the event.... |
| `observer` | `7` | `singular` | [`Noun`](messages/noun.md) | Represents an observer entity (for example, a packet sniffer or network-based vulnerability scanner... |
| `about` | `8` | `repeated` | [`Noun`](messages/noun.md) | Represents entities referenced by the event that are not otherwise described in principal, src, tar... |
| `security_result` | `9` | `repeated` | [`SecurityResult`](messages/security_result.md) | A list of security results. |
| `network` | `10` | `singular` | [`Network`](messages/network.md) | All network details go here, including sub-messages with details on each protocol (for example, DHC... |
| `extensions` | `11` | `singular` | [`Extensions`](messages/extensions.md) | All other first-class, event-specific metadata goes in this message. Do not place protocol metadata... |
| `extracted` | `12` | `singular` | `google.protobuf.Struct` | Flattened fields extracted from the log. |
| `grouped` | `13` | `optional` | [`GroupedFields`](messages/grouped_fields.md) | Related UDM fields that are grouped together. |

## Top-level Entity graph fields

| Field | No. | Cardinality | Type | Description |
| --- | ---: | --- | --- | --- |
| `metadata` | `1` | `singular` | [`EntityMetadata`](messages/entity_metadata.md) | Entity metadata such as timestamp, product, etc. |
| `entity` | `2` | `singular` | [`Noun`](messages/noun.md) | Noun in the UDM event that this entity represents. |
| `relations` | `4` | `repeated` | [`Relation`](messages/relation.md) | One or more relationships between the entity (a) and other entities, including the relationship typ... |
| `additional` | `3` | `singular` | `google.protobuf.Struct` | Important entity data that cannot be adequately represented within the formal sections of the Entit... |
| `risk_score` | `5` | `optional` | [`EntityRisk`](messages/entity_risk.md) | Stores information related to the entity's risk score. |
| `metric` | `6` | `singular` | [`Metric`](messages/metric.md) | Stores statistical metrics about the entity. Used if metadata.entity_type is METRIC. |
