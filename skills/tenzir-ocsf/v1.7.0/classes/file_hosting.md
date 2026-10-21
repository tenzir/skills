# File Hosting Activity (file_hosting)

File Hosting Activity events report the actions taken by file management applications, including file sharing servers like Sharepoint and services such as Box, MS OneDrive, Google Drive, or network file share services.

- **Class UID**: `6006`
- **Category**: Application Activity
- **Extends**: [Application Activity (application)](application.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

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

### `access_list`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The list of requested access rights.

### `access_mask`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: context

The sum of hexadecimal values of requested access rights.

### `access_result`

- **Type**: `json_t`
- **Requirement**: optional
- **Group**: context

The list of access check results.

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
- `17`: `Access Check` - Access check for a file. The `security_control` profile can be used to add the access check results.
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

### `http_request`

- **Type**: [`http_request`](../objects/http_request.md)
- **Requirement**: recommended
- **Group**: context

Details about the underlying HTTP request.

### `http_response`

- **Type**: [`http_response`](../objects/http_response.md)
- **Requirement**: optional
- **Group**: context

Details about the HTTP response, if available.

### `share`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The share name.

### `share_type`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The share type, normalized to the caption of the share_type_id value. In the case of 'Other', it is defined by the event source.

### `share_type_id`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: context
- **Sibling**: `share_type`

#### Enum values

- `0`: `Unknown` - The share type is unknown.
- `1`: `File`
- `2`: `Pipe`
- `3`: `Print`
- `99`: `Other` - The share type is not mapped. See the `share_type` attribute, which contains a data source specific value.

The normalized identifier of the share type.

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

- `6006`: `File Hosting Activity` - File Hosting Activity events report the actions taken by file management applications, including file sharing servers like Sharepoint and services such as Box, MS OneDrive, Google Drive, or network file share services.

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
- `600617`: `File Hosting Activity: Access Check` - Access check for a file. The `security_control` profile can be used to add the access check results.
- `600699`: `File Hosting Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
