# Memory Activity (memory)

Memory Activity events report when a process has memory allocated, read/modified, or other manipulation activities - such as a buffer overflow or turning off data execution protection (DEP).

- **UID**: `4`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `actual_permissions`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: primary

The permissions that were granted to the in a platform-native format.

### `base_address`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The memory address that was access or requested.

### `requested_permissions`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: primary

The permissions mask that were requested by the process.

### `size`

- **Type**: `long_t`
- **Group**: primary

The memory size that was access or requested.

### `process`

- **Type**: `process`
- **Requirement**: required
- **Group**: primary

The process that had memory allocated, read/written, or had other manipulation activities performed on it.
