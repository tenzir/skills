# Peripheral Device Query (peripheral_device_query)

Peripheral Device Query events report information about peripheral devices.

- **Class UID**: `5014`
- **Category**: Discovery
- **Extends**: [Discovery Result (discovery_result)](discovery_result.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

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

### `peripheral_device`

- **Type**: [`peripheral_device`](../objects/peripheral_device.md)
- **Requirement**: required
- **Group**: primary

The peripheral device that triggered the event.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5014`: `Peripheral Device Query` - Peripheral Device Query events report information about peripheral devices.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `501400`: `Peripheral Device Query: Unknown`
- `501401`: `Peripheral Device Query: Query` - The discovered results are via a query request.
- `501499`: `Peripheral Device Query: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
