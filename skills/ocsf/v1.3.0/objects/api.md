# API (api)

The API, or Application Programming Interface, object represents  information pertaining to an API request and response.

- **Extends**: `object`

## Attributes

### `group`

- **Type**: `group`
- **Requirement**: optional

The information pertaining to the API group.

### `operation`

- **Type**: `string_t`
- **Requirement**: required

Verb/Operation associated with the request

### `request`

- **Type**: `request`
- **Requirement**: recommended

Details pertaining to the API request.

### `response`

- **Type**: `response`
- **Requirement**: recommended

Details pertaining to the API response.

### `service`

- **Type**: `service`
- **Requirement**: optional

The information pertaining to the API service.

### `version`

- **Type**: `string_t`
- **Requirement**: optional

The version of the API service.
