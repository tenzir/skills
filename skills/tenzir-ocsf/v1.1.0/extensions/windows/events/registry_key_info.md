# Registry Key Info (registry_key_info)

Registry Key Info events report information about discovered Windows registry keys.

- **Class UID**: `205004`
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

### `reg_key`

- **Type**: `win/reg_key`
- **Requirement**: required
- **Group**: primary

The registry key that pertains to the event.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `205004`: `Registry Key Info` - Registry Key Info events report information about discovered Windows registry keys.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `20500400`: `Registry Key Info: Unknown`
- `20500401`: `Registry Key Info: Exists` - The target was found.
- `20500402`: `Registry Key Info: Partial` - The target was partially found.
- `20500403`: `Registry Key Info: Does not exist` - The target was not found.
- `20500404`: `Registry Key Info: Error` - The discovery attempt failed.
- `20500405`: `Registry Key Info: Unsupported` - Discovery of the target was not supported.
- `20500499`: `Registry Key Info: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
