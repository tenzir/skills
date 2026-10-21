# Kernel Object Query (kernel_object_query)

Kernel Object Query events report information about discovered kernel resources.

- **Class UID**: `5006`
- **Category**: Discovery
- **Extends**: [Discovery Result (discovery_result)](discovery_result.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

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

### `kernel`

- **Type**: [`kernel`](../objects/kernel.md)
- **Requirement**: required
- **Group**: primary

The kernel object that pertains to the event.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5006`: `Kernel Object Query` - Kernel Object Query events report information about discovered kernel resources.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `500600`: `Kernel Object Query: Unknown`
- `500601`: `Kernel Object Query: Query` - The discovered results are via a query request.
- `500699`: `Kernel Object Query: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
