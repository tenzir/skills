# SMB Activity (smb_activity)

Server Message Block (SMB) Protocol Activity events report client/server connections sharing resources within the network.

- **Class UID**: `4006`
- **Category**: Network Activity
- **Extends**: [Network Activity (network_activity)](network_activity.md)
- **Profiles**: [Host](../profiles/host.md), [Security Control](../profiles/security_control.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

**From Network Activity:**
- `dst_endpoint` (required)
- `src_endpoint` (required)
- `connection_info` (recommended)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `File Supersede` - The event pertains to file superseded activity (overwritten if it exists and created if not).
- `2`: `File Open` - The event pertains to file open activity (the file is opened if it exists and fails to open if it doesn't).
- `3`: `File Create` - The event pertains to file creation activity (a file is created if it does not exist and fails if it does).
- `4`: `File Open If` - The event pertains to file open activity (the file is opened if it exists and is created if it doesn't).
- `5`: `File Overwrite` - The event pertains to file overwrite activity (the file is opened in a truncated form if it exists and fails if it doesn't).
- `6`: `File Overwrite If` - The event pertains to file overwrite activity (the file is opened in a truncated form if it exists and created otherwise)
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `client_dialects`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: context

The list of SMB dialects that the client speaks.

### `command`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The command name (e.g. SMB2_COMMAND_CREATE, SMB1_COMMAND_WRITE_ANDX).

### `dce_rpc`

- **Type**: [`dce_rpc`](../objects/dce_rpc.md)
- **Requirement**: optional
- **Group**: context

The DCE/RPC object describes the remote procedure call system for distributed computing environments.

### `dialect`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: context

The negotiated protocol dialect.

### `file`

- **Type**: [`file`](../objects/file.md)
- **Requirement**: recommended
- **Group**: primary

The file that is the target of the SMB activity.

### `open_type`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

Indicates how the file was opened (e.g. normal, delete on close).

### `response`

- **Type**: [`response`](../objects/response.md)
- **Requirement**: recommended
- **Group**: primary

The server response in an SMB network connection.

### `share`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The SMB share name.

### `share_type`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The SMB share type, normalized to the caption of the share_type_id value. In the case of 'Other', it is defined by the event source.

### `share_type_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `share_type`

#### Enum values

- `0`: `Unknown` - The share type is not known.
- `1`: `File`
- `2`: `Pipe`
- `3`: `Print`
- `99`: `Other` - The share type is not mapped.

The normalized identifier of the SMB share type.

### `tree_uid`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The tree id is a unique SMB identifier which represents an open connection to a share.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4006`: `SMB Activity` - Server Message Block (SMB) Protocol Activity events report client/server connections sharing resources within the network.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `400600`: `SMB Activity: Unknown`
- `400601`: `SMB Activity: File Supersede` - The event pertains to file superseded activity (overwritten if it exists and created if not).
- `400602`: `SMB Activity: File Open` - The event pertains to file open activity (the file is opened if it exists and fails to open if it doesn't).
- `400603`: `SMB Activity: File Create` - The event pertains to file creation activity (a file is created if it does not exist and fails if it does).
- `400604`: `SMB Activity: File Open If` - The event pertains to file open activity (the file is opened if it exists and is created if it doesn't).
- `400605`: `SMB Activity: File Overwrite` - The event pertains to file overwrite activity (the file is opened in a truncated form if it exists and fails if it doesn't).
- `400606`: `SMB Activity: File Overwrite If` - The event pertains to file overwrite activity (the file is opened in a truncated form if it exists and created otherwise)
- `400699`: `SMB Activity: Other`

The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
