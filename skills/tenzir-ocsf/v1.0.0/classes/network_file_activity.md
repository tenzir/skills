# Network File Activity (network_file_activity)

Network File Activity events report activities on a cloud file storage service such as Box, MS OneDrive, or Google Drive.

- **Class UID**: `4010`
- **Category**: Network Activity
- **Extends**: [Base Event (base_event)](base_event.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

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
- `1`: `Upload`
- `2`: `Download`
- `3`: `Update`
- `4`: `Delete`
- `5`: `Rename`
- `6`: `Copy`
- `7`: `Move`
- `8`: `Restore`
- `9`: `Preview`
- `10`: `Lock`
- `11`: `Unlock`
- `12`: `Share`
- `13`: `Unshare`
- `14`: `Open`
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: required
- **Group**: primary

The actor that performed the activity on the target file.

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

- `4010`: `Network File Activity` - Network File Activity events report activities on a cloud file storage service such as Box, MS OneDrive, or Google Drive.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `401000`: `Network File Activity: Unknown`
- `401001`: `Network File Activity: Upload`
- `401002`: `Network File Activity: Download`
- `401003`: `Network File Activity: Update`
- `401004`: `Network File Activity: Delete`
- `401005`: `Network File Activity: Rename`
- `401006`: `Network File Activity: Copy`
- `401007`: `Network File Activity: Move`
- `401008`: `Network File Activity: Restore`
- `401009`: `Network File Activity: Preview`
- `401010`: `Network File Activity: Lock`
- `401011`: `Network File Activity: Unlock`
- `401012`: `Network File Activity: Share`
- `401013`: `Network File Activity: Unshare`
- `401014`: `Network File Activity: Open`
- `401099`: `Network File Activity: Other`

The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
