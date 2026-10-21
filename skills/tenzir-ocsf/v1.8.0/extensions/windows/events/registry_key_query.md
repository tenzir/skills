# Registry Key Query (registry_key_query)

Registry Key Query events report information about discovered Windows registry keys.

> **Deprecated since v1.5.0.** Use the `Evidence Info` class with the `Query Evidence` object populated with `Registry Key` instead.

- **Class UID**: `205004`
- **Category**: Discovery
- **Extends**: [Discovery Result (discovery_result)](../../../classes/discovery_result.md)
- **Profiles**: [Cloud](../../../profiles/cloud.md), [Date/Time](../../../profiles/datetime.md), [Host](../../../profiles/host.md), [OSINT](../../../profiles/osint.md), [Security Control](../../../profiles/security_control.md)

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

- `205004`: `Registry Key Query` - Registry Key Query events report information about discovered Windows registry keys.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `20500400`: `Registry Key Query: Unknown`
- `20500401`: `Registry Key Query: Query` - The discovered results are via a query request.
- `20500499`: `Registry Key Query: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
