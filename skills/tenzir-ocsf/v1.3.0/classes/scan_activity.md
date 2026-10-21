# Scan Activity (scan_activity)

Scan events report the start, completion, and results of a scan job. The scan event includes the number of items that were scanned and the number of detections that were resolved.

- **Class UID**: `6007`
- **Category**: Application Activity
- **Extends**: [Base Event (base_event)](base_event.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [OSINT](../profiles/osint.md)

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

### `command_uid`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The command identifier that is associated with this scan event.  This ID uniquely identifies the proactive scan command, e.g., if remotely initiated.

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Started` - The scan was started.
- `2`: `Completed` - The scan was completed.
- `3`: `Cancelled` - The scan was cancelled.
- `4`: `Duration Violation` - The allocated scan time was insufficient to complete the requested scan.
- `5`: `Pause Violation` - The scan was paused, either by the user or by program constraints (e.g. scans that are suspended during certain time intervals), and not resumed within the allotted time.
- `6`: `Error` - The scan could not be completed due to an internal error.
- `7`: `Paused` - The scan was paused.
- `8`: `Resumed` - The scan was resumed from the pause point.
- `9`: `Restarted` - The scan restarted from the beginning of the file enumeration.
- `10`: `Delayed` - The user delayed the scan.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `duration`

- **Type**: `long_t`
- **Requirement**: recommended
- **Group**: occurrence

The duration of the scan

### `end_time`

- **Type**: `timestamp_t`
- **Requirement**: recommended
- **Group**: occurrence

The end time of the scan job.

### `num_detections`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The number of detections.

### `num_files`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The number of files scanned.

### `num_folders`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The number of folders scanned.

### `num_network_items`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The number of network items scanned.

### `num_processes`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The number of processes scanned.

### `num_registry_items`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The number of registry items scanned.

### `num_resolutions`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The number of items that were resolved.

### `num_skipped_items`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The number of skipped items.

### `num_trusted_items`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The number of trusted items.

### `policy`

- **Type**: [`policy`](../objects/policy.md)
- **Requirement**: recommended
- **Group**: primary

The policy associated with this Scan event; required if the scan was initiated by a policy.

### `scan`

- **Type**: [`scan`](../objects/scan.md)
- **Requirement**: required
- **Group**: primary

The Scan object describes characteristics of the scan job.

### `schedule_uid`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The unique identifier of the schedule associated with a scan job.

### `start_time`

- **Type**: `timestamp_t`
- **Requirement**: recommended
- **Group**: occurrence

The start time of the scan job.

### `total`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The total number of items that were scanned; zero if no items were scanned.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `6007`: `Scan Activity` - Scan events report the start, completion, and results of a scan job. The scan event includes the number of items that were scanned and the number of detections that were resolved.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `600700`: `Scan Activity: Unknown`
- `600701`: `Scan Activity: Started` - The scan was started.
- `600702`: `Scan Activity: Completed` - The scan was completed.
- `600703`: `Scan Activity: Cancelled` - The scan was cancelled.
- `600704`: `Scan Activity: Duration Violation` - The allocated scan time was insufficient to complete the requested scan.
- `600705`: `Scan Activity: Pause Violation` - The scan was paused, either by the user or by program constraints (e.g. scans that are suspended during certain time intervals), and not resumed within the allotted time.
- `600706`: `Scan Activity: Error` - The scan could not be completed due to an internal error.
- `600707`: `Scan Activity: Paused` - The scan was paused.
- `600708`: `Scan Activity: Resumed` - The scan was resumed from the pause point.
- `600709`: `Scan Activity: Restarted` - The scan restarted from the beginning of the file enumeration.
- `600710`: `Scan Activity: Delayed` - The user delayed the scan.
- `600799`: `Scan Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
