# FTP Activity (ftp_activity)

File Transfer Protocol (FTP) Activity events report file transfers between a server and a client as seen on the network.

- **Class UID**: `4008`
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
- `1`: `Put` - File upload to the FTP or SFTP site.
- `2`: `Get` - File download from the FTP or SFTP site.
- `3`: `Poll` - Poll directory for specific file(s) or folder(s) at the FTP or SFTP site location.
- `4`: `Delete` - Delete file(s) from the FTP or SFTP site.
- `5`: `Rename` - Rename the file(s) in the FTP or SFTP site.
- `6`: `List` - List files in a specified directory.
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `codes`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The list of return codes to the FTP command.

### `command`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The FTP command.

### `command_responses`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The list of responses to the FTP command.

### `name`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The name of the data affiliated with the command.

### `port`

- **Type**: `port_t`
- **Requirement**: recommended
- **Group**: primary

The dynamic port established for impending data transfers.

### `type`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The type of FTP network connection (e.g. active, passive).

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4008`: `FTP Activity` - File Transfer Protocol (FTP) Activity events report file transfers between a server and a client as seen on the network.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `400800`: `FTP Activity: Unknown`
- `400801`: `FTP Activity: Put` - File upload to the FTP or SFTP site.
- `400802`: `FTP Activity: Get` - File download from the FTP or SFTP site.
- `400803`: `FTP Activity: Poll` - Poll directory for specific file(s) or folder(s) at the FTP or SFTP site location.
- `400804`: `FTP Activity: Delete` - Delete file(s) from the FTP or SFTP site.
- `400805`: `FTP Activity: Rename` - Rename the file(s) in the FTP or SFTP site.
- `400806`: `FTP Activity: List` - List files in a specified directory.
- `400899`: `FTP Activity: Other`

The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
