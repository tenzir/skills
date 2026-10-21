# Startup Item Query (startup_item_query)

Startup Item Query events report information about discovered items, e.g., application components that are generally configured to run automatically.

> **Deprecated since v1.5.0.** Use the `Live Evidence Info` class.

- **Class UID**: `5022`
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

### `startup_item`

- **Type**: [`startup_item`](../objects/startup_item.md)
- **Requirement**: required
- **Group**: primary

The startup item object describes an application component that has associated startup criteria and configurations.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5022`: `Startup Item Query` - Startup Item Query events report information about discovered items, e.g., application components that are generally configured to run automatically.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `502200`: `Startup Item Query: Unknown`
- `502201`: `Startup Item Query: Query` - The discovered results are via a query request.
- `502299`: `Startup Item Query: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
