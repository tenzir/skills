# Discovery Result (discovery_result)

Discovery Result events report the results of a discovery request.

- **Category**: Discovery
- **Extends**: `base_event`

## Attributes

### `$include`

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Query` - The discovered results are via a query request.

The normalized identifier of the activity that triggered the event.

### `query_info`

- **Type**: `query_info`
- **Requirement**: recommended
- **Group**: primary

The search details associated with the query request.

### `query_result`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The result of the query.

### `query_result_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: primary
- **Sibling**: `query_result`

#### Enum values

- `0`: `Unknown` - The query result is unknown.
- `1`: `Exists` - The target was found.
- `2`: `Partial` - The target was partially found.
- `3`: `Does not exist` - The target was not found.
- `4`: `Error` - The discovery attempt failed.
- `5`: `Unsupported` - Discovery of the target was not supported.
- `99`: `Other` - The query result is not mapped. See the `query_result` attribute, which contains a data source specific value.

The normalized identifier of the query result.
