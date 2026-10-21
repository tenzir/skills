# File Hosting Activity (file_hosting)

File Hosting Activity events report the actions taken by file management applications, including file sharing servers like Sharepoint and services such as Box, MS OneDrive, or Google Drive.

- **Class UID**: `6006`
- **Category**: Application Activity
- **Extends**: [Application Activity (application)](application.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [OSINT](../profiles/osint.md)

## Inherited attributes

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
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
- `1`: `Upload` - Upload a file.
- `2`: `Download` - Download a file.
- `3`: `Update` - Update a file.
- `4`: `Delete` - Delete a file.
- `5`: `Rename` - Rename a file.
- `6`: `Copy` - Copy a file.
- `7`: `Move` - Move a file.
- `8`: `Restore` - Restore a file.
- `9`: `Preview` - Preview a file.
- `10`: `Lock` - Lock a file.
- `11`: `Unlock` - Unlock a file.
- `12`: `Share` - Share a file.
- `13`: `Unshare` - Unshare a file.
- `14`: `Open` - Open a file.
- `15`: `Sync` - Mark a file or folder to sync with a computer.
- `16`: `Unsync` - Mark a file or folder to not sync with a computer.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: required
- **Group**: primary

The actor that performed the activity on the target file.

### `connection_info`

- **Type**: [`network_connection_info`](../objects/network_connection_info.md)
- **Requirement**: optional
- **Group**: context

The network connection information.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended

The endpoint that received the activity on the target file.

### `expiration_time`

- **Type**: `timestamp_t`
- **Requirement**: optional
- **Group**: context

The share expiration time.

### `file`

- **Type**: [`file`](../objects/file.md)
- **Requirement**: required
- **Group**: primary

The file that is the target of the activity.

### `file_result`

- **Type**: [`file`](../objects/file.md)
- **Requirement**: optional
- **Group**: context

The resulting file object when the activity was allowed and successful.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: required
- **Group**: primary

The endpoint that performed the activity on the target file.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `6006`: `File Hosting Activity` - File Hosting Activity events report the actions taken by file management applications, including file sharing servers like Sharepoint and services such as Box, MS OneDrive, or Google Drive.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `600600`: `File Hosting Activity: Unknown`
- `600601`: `File Hosting Activity: Upload` - Upload a file.
- `600602`: `File Hosting Activity: Download` - Download a file.
- `600603`: `File Hosting Activity: Update` - Update a file.
- `600604`: `File Hosting Activity: Delete` - Delete a file.
- `600605`: `File Hosting Activity: Rename` - Rename a file.
- `600606`: `File Hosting Activity: Copy` - Copy a file.
- `600607`: `File Hosting Activity: Move` - Move a file.
- `600608`: `File Hosting Activity: Restore` - Restore a file.
- `600609`: `File Hosting Activity: Preview` - Preview a file.
- `600610`: `File Hosting Activity: Lock` - Lock a file.
- `600611`: `File Hosting Activity: Unlock` - Unlock a file.
- `600612`: `File Hosting Activity: Share` - Share a file.
- `600613`: `File Hosting Activity: Unshare` - Unshare a file.
- `600614`: `File Hosting Activity: Open` - Open a file.
- `600615`: `File Hosting Activity: Sync` - Mark a file or folder to sync with a computer.
- `600616`: `File Hosting Activity: Unsync` - Mark a file or folder to not sync with a computer.
- `600699`: `File Hosting Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
