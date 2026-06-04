# Asset

Information about a compute asset such as a workstation, laptop, phone, virtual desktop, or VM.

- **Full name**: `google.backstory.Asset`
- **Fields**: `24`
- **Nested enums**: `2`

## Nested enums

- [Asset.AssetType](../enums/asset_asset_type.md)
- [Asset.DeploymentStatus](../enums/asset_deployment_status.md)

## Fields

### `product_object_id`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productObjectId`

A vendor-specific identifier to uniquely identify the entity (a GUID or similar). This field can be used as an entity indicator for asset entities.

### `hostname`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `hostname`

Asset hostname or domain name field. This field can be used as an entity indicator for asset entities.

### `asset_id`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `assetId`

The asset ID. Value must contain the ':' character. For example, cs:abcdd23434. This field can be used as an entity indicator for asset entities.

### `ip`

- **Number**: `4`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `ip`

A list of IP addresses associated with an asset. This field can be used as an entity indicator for asset entities.

### `mac`

- **Number**: `5`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `mac`

List of MAC addresses associated with an asset. This field can be used as an entity indicator for asset entities.

### `nat_ip`

- **Number**: `22`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `natIp`

List of NAT IP addresses associated with an asset.

### `first_seen_time`

- **Number**: `23`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `firstSeenTime`

The first observed time for an asset. The value is calculated on the basis of the first time the identifier was observed.

### `hardware`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: [`Hardware`](hardware.md)
- **JSON name**: `hardware`

The asset hardware specifications.

### `platform_software`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: [`PlatformSoftware`](platform_software.md)
- **JSON name**: `platformSoftware`

The asset operating system platform software.

### `software`

- **Number**: `17`
- **Cardinality**: `repeated`
- **Type**: [`Software`](software.md)
- **JSON name**: `software`

The asset software details.

### `location`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: [`Location`](location.md)
- **JSON name**: `location`

Location of the asset.

### `category`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `category`

The category of the asset (e.g. "End User Asset", "Workstation", "Server").

### `type`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: [`Asset.AssetType`](../enums/asset_asset_type.md)
- **JSON name**: `type`

The type of the asset (e.g. workstation or laptop or server).

### `network_domain`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `networkDomain`

The network domain of the asset (e.g. "corp.acme.com")

### `creation_time`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `creationTime`
- **Deprecated**: `true`

Time the asset was created or provisioned. Deprecate: creation_time should be populated in Attribute as generic metadata.

### `first_discover_time`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `firstDiscoverTime`

Time the asset was first discovered (by asset management/discoverability software).

### `last_discover_time`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `lastDiscoverTime`

Time the asset was last discovered (by asset management/discoverability software).

### `system_last_update_time`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `systemLastUpdateTime`

Time the asset system or OS was last updated. For all other operations that are not system updates (such as resizing a VM), use Attribute.last_update_time.

### `last_boot_time`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `lastBootTime`

Time the asset was last boot started.

### `labels`

- **Number**: `16`
- **Cardinality**: `repeated`
- **Type**: [`Label`](label.md)
- **JSON name**: `labels`
- **Deprecated**: `true`

Metadata labels for the asset. Deprecated: labels should be populated in Attribute as generic metadata.

### `deployment_status`

- **Number**: `19`
- **Cardinality**: `singular`
- **Type**: [`Asset.DeploymentStatus`](../enums/asset_deployment_status.md)
- **JSON name**: `deploymentStatus`

The deployment status of the asset for device lifecycle purposes.

### `vulnerabilities`

- **Number**: `21`
- **Cardinality**: `repeated`
- **Type**: [`Vulnerability`](vulnerability.md)
- **JSON name**: `vulnerabilities`

Vulnerabilities discovered on asset.

### `attribute`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: [`Attribute`](attribute.md)
- **JSON name**: `attribute`

Generic entity metadata attributes of the asset.

### `wmi_persistence_item`

- **Number**: `24`
- **Cardinality**: `singular`
- **Type**: [`WmiPersistenceItem`](wmi_persistence_item.md)
- **JSON name**: `wmiPersistenceItem`

Information about a WMI persistence item.
