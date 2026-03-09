# Software Inventory Info (software_info)

Software Inventory Info events report device software inventory data that is either logged or proactively collected. For example, when collecting device information from a CMDB or running a network sweep of connected devices.

- **UID**: `20`
- **Category**: Discovery
- **Extends**: `discovery`

## Attributes

### `actor`

- **Type**: `actor`
- **Requirement**: optional
- **Group**: context

The actor object describes details about the user/role/process that was the source of the activity. Note that this is not the threat actor of a campaign but may be part of a campaign.

### `device`

- **Type**: `device`
- **Requirement**: required
- **Group**: primary

The device that is being discovered by an inventory process.

### `package`

- **Type**: `package`
- **Requirement**: recommended
- **Group**: primary

The device software that is being discovered by an inventory process.

### `product`

- **Type**: `product`
- **Requirement**: optional
- **Group**: context

Additional product attributes that have been discovered or enriched from a catalog or other external source.

### `sbom`

- **Type**: `sbom`
- **Requirement**: recommended
- **Group**: primary

The Software Bill of Materials (SBOM) of the device software that is being discovered by an inventory process.
