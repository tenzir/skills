# Device Inventory Info (inventory_info)

Device Inventory Info events report device inventory data.

- **UID**: `1`
- **Category**: Discovery
- **Extends**: `discovery`

## Attributes

### `actor`

- **Type**: `actor`
- **Requirement**: optional
- **Group**: context

The actor object describes details about the user/role/process that was the source of the activity.

### `device`

- **Type**: `device`
- **Requirement**: required
- **Group**: primary

The device that is being discovered by an inventory process.
