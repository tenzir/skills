# Startup Item Query (startup_item_query)

Startup Item Query events report information about discovered items, e.g., application components that are generally configured to run automatically.

- **Class UID**: `5022`
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

### `startup_item`

- **Type**: [`startup_item`](../objects/startup_item.md)
- **Requirement**: required
- **Group**: primary

The startup item object describes an application component that has associated startup criteria and configurations.
