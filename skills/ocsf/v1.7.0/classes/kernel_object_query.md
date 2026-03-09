# Kernel Object Query (kernel_object_query)

Kernel Object Query events report information about discovered kernel resources.

- **Class UID**: `5006`
- **Category**: Discovery
- **Extends**: [Discovery Result (discovery_result)](discovery_result.md)
- **Profiles**: `cloud`, `datetime`, `host`, `osint`, `security_control`

## Inherited attributes

**From Discovery Result:**
- `query_result_id` (required)
- `query_info` (recommended)
- `query_result` (recommended)

**From Base Event:**
- `category_uid` (required)
- `class_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `type_uid` (required)
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
