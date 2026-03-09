# Image (image)

The Image object provides a description of a specific Virtual Machine (VM) or Container image.

- **Extends**: `_entity`

## Attributes

### `labels`

- **Type**: `string_t`
- **Requirement**: optional

The list of labels associated to the image.

### `name`

- **Type**: `string_t`

The image name. For example: `elixir`.

### `path`

- **Type**: `string_t`
- **Requirement**: optional

The full path to the image file.

### `tag`

- **Type**: `string_t`
- **Requirement**: optional

The image tag. For example: `1.11-alpine`.

### `tags`

- **Type**: `key_value_object`
- **Requirement**: optional

The list of tags; `{key:value}` pairs associated to the image.

### `uid`

- **Type**: `string_t`
- **Requirement**: required

The unique image ID. For example: `77af4d6b9913`.
