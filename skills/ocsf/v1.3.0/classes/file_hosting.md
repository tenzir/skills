# File Hosting Activity (file_hosting)

File Hosting Activity events report the actions taken by file management applications, including file sharing servers like Sharepoint and services such as Box, MS OneDrive, or Google Drive.

- **UID**: `6`
- **Category**: Application Activity
- **Extends**: `application`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

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

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: `actor`
- **Requirement**: required
- **Group**: primary

The actor that performed the activity on the target file.

### `connection_info`

- **Type**: `network_connection_info`
- **Requirement**: optional
- **Group**: context

The network connection information.

### `dst_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: recommended

The endpoint that received the activity on the target file.

### `expiration_time`

- **Type**: `timestamp_t`
- **Requirement**: optional
- **Group**: context

The share expiration time.

### `file`

- **Type**: `file`
- **Requirement**: required
- **Group**: primary

The file that is the target of the activity.

### `file_result`

- **Type**: `file`
- **Requirement**: optional
- **Group**: context

The resulting file object when the activity was allowed and successful.

### `src_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: required
- **Group**: primary

The endpoint that performed the activity on the target file.
