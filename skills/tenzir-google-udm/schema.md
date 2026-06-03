# Google UDM schema

Generated from the canonical Google UDM protocol buffer definition.

- **Source**: [backstory/udm.proto](https://github.com/googleapis/googleapis/blob/5ff4b410beb15f65d3d0b7a160f52d803bce7c97/backstory/udm.proto)
- **Requested ref**: `master`
- **Resolved commit**: `5ff4b410beb15f65d3d0b7a160f52d803bce7c97`
- **Package**: `google.backstory`
- **Messages**: `118`
- **Enums**: `61`
- **Fields**: `944`
- **Enum values**: `884`

## Imports

- `backstory/data_access.proto`
- `backstory/entity_risk.proto`
- `backstory/id.proto`
- `google/type/interval.proto`
- `google/type/latlng.proto`

## Indexes

- [Messages](messages.md)
- [Enums](enums.md)
- [Event types](event-types.md)

## Top-level UDM fields

| Field | No. | Cardinality | Type | Description |
| --- | ---: | --- | --- | --- |
| `metadata` | `1` | `singular` | [`Metadata`](messages/metadata.md) | Event metadata such as timestamp, source product, etc. |
| `additional` | `2` | `singular` | `google.protobuf.Struct` (imported) | Any important vendor-specific event data that cannot be adequately represented within the formal se... |
| `principal` | `3` | `singular` | [`Noun`](messages/noun.md) | Represents the acting entity that originates the activity described in the event. The principal mus... |
| `src` | `4` | `singular` | [`Noun`](messages/noun.md) | Represents a source entity being acted upon by the participant along with the device or process con... |
| `target` | `5` | `singular` | [`Noun`](messages/noun.md) | Represents a target entity being referenced by the event or an object on the target entity. For exa... |
| `intermediary` | `6` | `repeated` | [`Noun`](messages/noun.md) | Represents details on one or more intermediate entities processing activity described in the event.... |
| `observer` | `7` | `singular` | [`Noun`](messages/noun.md) | Represents an observer entity (for example, a packet sniffer or network-based vulnerability scanner... |
| `about` | `8` | `repeated` | [`Noun`](messages/noun.md) | Represents entities referenced by the event that are not otherwise described in principal, src, tar... |
| `security_result` | `9` | `repeated` | [`SecurityResult`](messages/security_result.md) | A list of security results. |
| `network` | `10` | `singular` | [`Network`](messages/network.md) | All network details go here, including sub-messages with details on each protocol (for example, DHC... |
| `extensions` | `11` | `singular` | [`Extensions`](messages/extensions.md) | All other first-class, event-specific metadata goes in this message. Do not place protocol metadata... |
| `extracted` | `12` | `singular` | `google.protobuf.Struct` (imported) | Flattened fields extracted from the log. |
| `grouped` | `13` | `optional` | [`GroupedFields`](messages/grouped_fields.md) | Related UDM fields that are grouped together. |
