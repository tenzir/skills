# File System Activity (file_activity)

File System Activity events report when a process performs an action on a file or folder.

- **Class UID**: `1001`
- **Category**: System Activity
- **Extends**: [System Activity (system)](system.md)
- **Profiles**: [Host](../profiles/host.md), [Security Control](../profiles/security_control.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Associations

- `device` ↔ `actor.user`
- `actor.user` ↔ `device`

## Inherited attributes

**From System Activity:**
- `device` (required)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `access_mask`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: context

The access mask in a platform-native format.

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Create` - A request to create a new file on a file system.
- `2`: `Read` - A request to read data from a file on a file system.
- `3`: `Update` - A request to write data to a file on a file system.
- `4`: `Delete` - A request to delete a file on a file system.
- `5`: `Rename` - A request to rename a file on a file system.
- `6`: `Set Attributes` - A request to set attributes for a file on a file system.
- `7`: `Set Security` - A request to set security for a file on a file system.
- `8`: `Get Attributes` - A request to get attributes for a file on a file system.
- `9`: `Get Security` - A request to get security for a file on a file system.
- `10`: `Encrypt` - A request to encrypt a file on a file system.
- `11`: `Decrypt` - A request to decrypt a file on a file system.
- `12`: `Mount` - A request to mount a file on a file system.
- `13`: `Unmount` - A request to unmount a file from a file system.
- `14`: `Open` - A request to create a file handle.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: required
- **Group**: primary

The actor that performed the activity on the `file` object

### `component`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The name or relative pathname of a sub-component of the data object, if applicable.

For example: `attachment.doc`, `attachment.zip/bad.doc`, or `part.mime/part.cab/part.uue/part.doc`.

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

- **Type**: [`file`](../objects/file.md)
- **Requirement**: required
- **Group**: primary

The file that is the target of the activity.

### `file_diff`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

File content differences used for change detection. For example, a common use case is to identify itemized changes within INI or configuration/property setting values.

### `file_result`

- **Type**: [`file`](../objects/file.md)
- **Requirement**: optional
- **Group**: primary

The resulting file object when the activity was allowed and successful.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `1001`: `File System Activity` - File System Activity events report when a process performs an action on a file or folder.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `100100`: `File System Activity: Unknown`
- `100101`: `File System Activity: Create` - A request to create a new file on a file system.
- `100102`: `File System Activity: Read` - A request to read data from a file on a file system.
- `100103`: `File System Activity: Update` - A request to write data to a file on a file system.
- `100104`: `File System Activity: Delete` - A request to delete a file on a file system.
- `100105`: `File System Activity: Rename` - A request to rename a file on a file system.
- `100106`: `File System Activity: Set Attributes` - A request to set attributes for a file on a file system.
- `100107`: `File System Activity: Set Security` - A request to set security for a file on a file system.
- `100108`: `File System Activity: Get Attributes` - A request to get attributes for a file on a file system.
- `100109`: `File System Activity: Get Security` - A request to get security for a file on a file system.
- `100110`: `File System Activity: Encrypt` - A request to encrypt a file on a file system.
- `100111`: `File System Activity: Decrypt` - A request to decrypt a file on a file system.
- `100112`: `File System Activity: Mount` - A request to mount a file on a file system.
- `100113`: `File System Activity: Unmount` - A request to unmount a file from a file system.
- `100114`: `File System Activity: Open` - A request to create a file handle.
- `100199`: `File System Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
