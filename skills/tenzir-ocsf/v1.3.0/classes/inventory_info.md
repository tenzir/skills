# Device Inventory Info (inventory_info)

Device Inventory Info events report device inventory data that is either logged or proactively collected. For example, when collecting device information from a CMDB or running a network sweep of connected devices.

- **Class UID**: `5001`
- **Category**: Discovery
- **Extends**: [Discovery (discovery)](discovery.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [OSINT](../profiles/osint.md)

## Inherited attributes

**From Discovery:**
- `activity_id` (required)

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

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: optional
- **Group**: context

The actor object describes details about the user/role/process that was the source of the activity.

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: required
- **Group**: primary

The device that is being discovered by an inventory process.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5001`: `Device Inventory Info` - Device Inventory Info events report device inventory data that is either logged or proactively collected. For example, when collecting device information from a CMDB or running a network sweep of connected devices.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `500100`: `Device Inventory Info: Unknown`
- `500101`: `Device Inventory Info: Log` - The discovered information is via a log.
- `500102`: `Device Inventory Info: Collect` - The discovered information is via a collection process.
- `500199`: `Device Inventory Info: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
