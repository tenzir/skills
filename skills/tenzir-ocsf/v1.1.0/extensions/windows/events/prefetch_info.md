# Prefetch Info (prefetch_info)

Prefetch Info events report information about Windows prefetch files.

- **Class UID**: `205019`
- **Category**: Discovery
- **Extends**: [Discovery Result (discovery_result)](../../../classes/discovery_result.md)
- **Profiles**: [Host](../../../profiles/host.md), [Cloud](../../../profiles/cloud.md), [Date/Time](../../../profiles/datetime.md)

## Inherited attributes

**From Discovery Result:**
- `activity_id` (required)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `last_run_time`

- **Type**: `timestamp_t`
- **Requirement**: recommended
- **Group**: occurrence

The prefetch file last run time.

### `name`

- **Type**: `string_t`
- **Requirement**: required
- **Group**: primary

The name of the prefetch file that is the target of the query.

### `run_count`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The prefetch file run count.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `205019`: `Prefetch Info` - Prefetch Info events report information about Windows prefetch files.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `20501900`: `Prefetch Info: Unknown`
- `20501901`: `Prefetch Info: Exists` - The target was found.
- `20501902`: `Prefetch Info: Partial` - The target was partially found.
- `20501903`: `Prefetch Info: Does not exist` - The target was not found.
- `20501904`: `Prefetch Info: Error` - The discovery attempt failed.
- `20501905`: `Prefetch Info: Unsupported` - Discovery of the target was not supported.
- `20501999`: `Prefetch Info: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
