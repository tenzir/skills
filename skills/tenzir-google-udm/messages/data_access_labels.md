# DataAccessLabels

Label used in data access.

## Fields

### `log_types` / `logTypes`

- Type: `string` (repeated)

All the LogType labels.

### `ingestion_labels` / `ingestionLabels`

- Type: `string` (repeated)
- Deprecated: `true`

All the ingestion labels.

### `namespaces`

- Type: `string` (repeated)

All the namespaces.

### `custom_labels` / `customLabels`

- Type: `string` (repeated)

All the complex labels (UDM search syntax based).

### `ingestion_kv_labels` / `ingestionKvLabels`

- Type: [`DataAccessIngestionLabel`](data_access_ingestion_label.md) (repeated)

All the ingestion labels (key/value pairs).

### `allow_scoped_access` / `allowScopedAccess`

- Type: `bool` (singular)

Are the labels ready for scoped access
