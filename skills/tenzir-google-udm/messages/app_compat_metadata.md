# AppCompatMetadata

Windows AppCompatCache (Application Compatibility) metadata.

- **Full name**: `google.backstory.AppCompatMetadata`
- **Fields**: `3`

## Fields

### `sequence`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `sequence`

Indicates the chronological order in which the entry was added to the cache.

### `executed`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `executed`

Indicates whether the file associated with the entry was executed.

### `control_set`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `controlSet`

Indicates which registry Control Set the AppCompatCache data belongs to (e.g., "ControlSet001").
