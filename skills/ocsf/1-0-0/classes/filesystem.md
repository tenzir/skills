# File System Activity (filesystem)

File System Activity events report when a process performs an action on a file or folder.

- **UID**: `1`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `access_mask`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: context

The access mask in a platform-native format.

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `99`: `Other` - The event activity is not mapped.

The activity ID of the event.

### `actor`

- **Type**: `actor`
- **Requirement**: required

The actor that performed the activity on the `file` object

### `component`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The name or relative pathname of a sub-component of the data object, if applicable. For example: `attachment.doc`, `attachment.zip/bad.doc`, or `part.mime/part.cab/part.uue/part.doc`.

### `connection_uid`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The network connection identifier.

### `create_mask`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The original Windows mask that is required to create the object.

### `file`

- **Type**: `file`
- **Requirement**: required
- **Group**: primary

The file that is the target of the activity.

### `file_diff`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

File content differences used for change detection. For example, a common use case is to identify itemized changes within INI or configuration/property setting values.

### `file_result`

- **Type**: `file`
- **Requirement**: optional
- **Group**: primary

The resulting file object when the activity was allowed and successful.
