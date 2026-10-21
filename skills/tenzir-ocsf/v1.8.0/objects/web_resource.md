# Web Resource (web_resource)

The Web Resource object describes characteristics of a web resource that was affected by the activity/event.

- **Extends**: [Resource (_resource)](_resource.md)
- **Profiles**: [Data Classification](../profiles/data_classification.md), [Date/Time](../profiles/datetime.md)

## Constraints

- **At least one of**: `name`, `uid`

## Attributes

### `data`

- **Type**: `json_t`
- **Requirement**: optional

Details of the web resource, e.g, `file` details, `search` results or application-defined resource.

### `desc`

- **Type**: `string_t`
- **Requirement**: optional

Description of the web resource.

### `name`

- **Type**: `string_t`
- **Requirement**: recommended

The name of the web resource.

### `type`

- **Type**: `string_t`
- **Requirement**: optional

The web resource type as defined by the event source.

### `uid`

- **Type**: `resource_uid_t`
- **Requirement**: recommended

The unique identifier of the web resource.

### `url_string`

- **Type**: `url_t`
- **Requirement**: recommended

The URL pointing towards the source of the web resource.
