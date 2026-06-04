# DataAccessLabels

Label used in data access.

- **Full name**: `google.backstory.DataAccessLabels`
- **Fields**: `6`

## Fields

### `log_types`

- **Number**: `1`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `logTypes`

All the LogType labels.

### `ingestion_labels`

- **Number**: `2`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `ingestionLabels`
- **Deprecated**: `true`

All the ingestion labels.

### `namespaces`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `namespaces`

All the namespaces.

### `custom_labels`

- **Number**: `4`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `customLabels`

All the complex labels (UDM search syntax based).

### `ingestion_kv_labels`

- **Number**: `5`
- **Cardinality**: `repeated`
- **Type**: [`DataAccessIngestionLabel`](data_access_ingestion_label.md)
- **JSON name**: `ingestionKvLabels`

All the ingestion labels (key/value pairs).

### `allow_scoped_access`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `allowScopedAccess`

Are the labels ready for scoped access
