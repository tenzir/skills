# Registry Value Info (registry_value_info)

Registry Value Info events report information about discovered Windows registry values.

- **Class UID**: `205005`
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

### `reg_value`

- **Type**: `win/reg_value`
- **Requirement**: required
- **Group**: primary

The registry value that pertains to the event.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `205005`: `Registry Value Info` - Registry Value Info events report information about discovered Windows registry values.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `20500500`: `Registry Value Info: Unknown`
- `20500501`: `Registry Value Info: Exists` - The target was found.
- `20500502`: `Registry Value Info: Partial` - The target was partially found.
- `20500503`: `Registry Value Info: Does not exist` - The target was not found.
- `20500504`: `Registry Value Info: Error` - The discovery attempt failed.
- `20500505`: `Registry Value Info: Unsupported` - Discovery of the target was not supported.
- `20500599`: `Registry Value Info: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
