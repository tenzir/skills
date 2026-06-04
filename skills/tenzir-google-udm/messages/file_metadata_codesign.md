# FileMetadataCodesign

File metadata from the codesign utility.

- **Full name**: `google.backstory.FileMetadataCodesign`
- **Fields**: `4`

## Fields

### `id`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `id`

Code sign identifier.

### `format`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `format`

Code sign format.

### `compilation_time`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `compilationTime`

Code sign timestamp

### `team_id`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `teamId`

The assigned team identifier of the developer who signed the application.
