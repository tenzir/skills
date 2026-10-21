# Network File Activity (network_file_activity)

Network File Activity events report file activities traversing the network, including file storage services such as Box, MS OneDrive, or Google Drive.

> **Deprecated since v1.1.0.** Use the new class: `'File Hosting Activity' in the 'Application' category.`

- **Class UID**: `4010`
- **Category**: Network Activity
- **Extends**: [Network (network)](network.md)
- **Profiles**: [Host](../profiles/host.md), [Network Proxy](../profiles/network_proxy.md), [Security Control](../profiles/security_control.md), [Load Balancer](../profiles/load_balancer.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

**From Network:**
- `proxy` (recommended)
- `traffic` (recommended)

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
- **Group**: primary

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

- `4010`: `Network File Activity` - Network File Activity events report file activities traversing the network, including file storage services such as Box, MS OneDrive, or Google Drive.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `401000`: `Network File Activity: Unknown`
- `401001`: `Network File Activity: Upload` - Upload a file.
- `401002`: `Network File Activity: Download` - Download a file.
- `401003`: `Network File Activity: Update` - Update a file.
- `401004`: `Network File Activity: Delete` - Delete a file.
- `401005`: `Network File Activity: Rename` - Rename a file.
- `401006`: `Network File Activity: Copy` - Copy a file.
- `401007`: `Network File Activity: Move` - Move a file.
- `401008`: `Network File Activity: Restore` - Restore a file.
- `401009`: `Network File Activity: Preview` - Preview a file.
- `401010`: `Network File Activity: Lock` - Lock a file.
- `401011`: `Network File Activity: Unlock` - Unlock a file.
- `401012`: `Network File Activity: Share` - Share a file.
- `401013`: `Network File Activity: Unshare` - Unshare a file.
- `401014`: `Network File Activity: Open` - Open a file.
- `401015`: `Network File Activity: Sync` - Mark a file or folder to sync with a computer.
- `401016`: `Network File Activity: Unsync` - Mark a file or folder to not sync with a computer.
- `401099`: `Network File Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
