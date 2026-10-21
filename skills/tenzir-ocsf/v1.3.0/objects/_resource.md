# Resource (_resource)

The Resource object contains attributes that provide information about a particular resource. It serves as a base object, offering attributes that help identify and classify the resource effectively.

- **Extends**: [Entity (_entity)](_entity.md)
- **Profiles**: [Data Classification](../profiles/data_classification.md)

## Constraints

- **At least one of**: `name`, `uid`

## Attributes

### `data`

- **Type**: `json_t`
- **Requirement**: optional

Additional data describing the resource.

### `labels`

- **Type**: `string_t`
- **Requirement**: optional

The list of labels/tags associated to a resource.

### `name`

- **Type**: `string_t`
- **Requirement**: recommended

The name of the resource.

### `type`

- **Type**: `string_t`
- **Requirement**: optional

The resource type as defined by the event source.

### `uid`

- **Type**: `string_t`
- **Requirement**: recommended

The unique identifier of the resource.
