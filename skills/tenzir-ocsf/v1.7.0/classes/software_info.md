# Software Inventory Info (software_info)

Software Inventory Info events report device software inventory data that is either logged or proactively collected. For example, when collecting device information from a CMDB or running a network sweep of connected devices.

- **Class UID**: `5020`
- **Category**: Discovery
- **Extends**: [Discovery (discovery)](discovery.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

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

The actor object describes details about the user/role/process that was the source of the activity. Note that this is not the threat actor of a campaign but may be part of a campaign.

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: required
- **Group**: primary

The device that is being discovered by an inventory process.

### `package`

- **Type**: [`package`](../objects/package.md)
- **Requirement**: recommended
- **Group**: primary

> **Deprecated since v1.4.0.** Use the `sbom` attribute instead.

The device software that is being discovered by an inventory process.

### `product`

- **Type**: [`product`](../objects/product.md)
- **Requirement**: optional
- **Group**: context

Additional product attributes that have been discovered or enriched from a catalog or other external source.

### `sbom`

- **Type**: [`sbom`](../objects/sbom.md)
- **Requirement**: recommended
- **Group**: primary

The Software Bill of Materials (SBOM) of the device software that is being discovered by an inventory process.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5020`: `Software Inventory Info` - Software Inventory Info events report device software inventory data that is either logged or proactively collected. For example, when collecting device information from a CMDB or running a network sweep of connected devices.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `502000`: `Software Inventory Info: Unknown`
- `502001`: `Software Inventory Info: Log` - The discovered information is via a log.
- `502002`: `Software Inventory Info: Collect` - The discovered information is via a collection process.
- `502099`: `Software Inventory Info: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
