# DataAccessLabels

Label used in data access.

- **Full name**: `google.backstory.DataAccessLabels`
- **Fields**: `6`

## Fields

### `logTypes`

- Type: `string` (repeated)

All the LogType labels.

### `ingestionLabels`

- Type: `string` (repeated)
- Deprecated: `true`

All the ingestion labels.

### `namespaces`

- Type: `string` (repeated)

All the namespaces.

### `customLabels`

- Type: `string` (repeated)

All the complex labels (UDM search syntax based).

### `ingestionKvLabels`

- Type: [`DataAccessIngestionLabel`](data_access_ingestion_label.md) (repeated)

All the ingestion labels (key/value pairs).

### `allowScopedAccess`

- Type: `bool` (singular)

Are the labels ready for scoped access
