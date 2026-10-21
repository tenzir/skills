# Prefetch Query (prefetch_query)

Prefetch Query events report information about Windows prefetch files.

- **Class UID**: `205019`
- **Category**: Discovery
- **Extends**: [Discovery Result (discovery_result)](../../../classes/discovery_result.md)
- **Profiles**: [Host](../../../profiles/host.md), [Cloud](../../../profiles/cloud.md), [Date/Time](../../../profiles/datetime.md), [OSINT](../../../profiles/osint.md)

## Inherited attributes

**From Discovery Result:**
- `activity_id` (required)
- `query_result_id` (required)
- `query_info` (recommended)
- `query_result` (recommended)

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

- `205019`: `Prefetch Query` - Prefetch Query events report information about Windows prefetch files.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `20501900`: `Prefetch Query: Unknown`
- `20501901`: `Prefetch Query: Query` - The discovered results are via a query request.
- `20501999`: `Prefetch Query: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
