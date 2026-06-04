# Asset

Information about a compute asset such as a workstation, laptop, phone, virtual desktop, or VM.

## Fields

### `productObjectId`

- Type: `string` (singular)

A vendor-specific identifier to uniquely identify the entity (a GUID or similar). This field can be used as an entity indicator for asset entities.

### `hostname`

- Type: `string` (singular)

Asset hostname or domain name field. This field can be used as an entity indicator for asset entities.

### `assetId`

- Type: `string` (singular)

The asset ID. Value must contain the ':' character. For example, cs:abcdd23434. This field can be used as an entity indicator for asset entities.

### `ip`

- Type: `string` (repeated)

A list of IP addresses associated with an asset. This field can be used as an entity indicator for asset entities.

### `mac`

- Type: `string` (repeated)

List of MAC addresses associated with an asset. This field can be used as an entity indicator for asset entities.

### `natIp`

- Type: `string` (repeated)

List of NAT IP addresses associated with an asset.

### `firstSeenTime`

- Type: `timestamp` (singular)

The first observed time for an asset. The value is calculated on the basis of the first time the identifier was observed.

### `hardware`

- Type: [`Hardware`](hardware.md) (repeated)

The asset hardware specifications.

### `platformSoftware`

- Type: [`PlatformSoftware`](platform_software.md) (singular)

The asset operating system platform software.

### `software`

- Type: [`Software`](software.md) (repeated)

The asset software details.

### `location`

- Type: [`Location`](location.md) (singular)

Location of the asset.

### `category`

- Type: `string` (singular)

The category of the asset (e.g. "End User Asset", "Workstation", "Server").

### `type`

- Type: [`AssetType`](../enums/asset_asset_type.md) (singular)

The type of the asset (e.g. workstation or laptop or server).

### `networkDomain`

- Type: `string` (singular)

The network domain of the asset (e.g. "corp.acme.com")

### `creationTime`

- Type: `timestamp` (singular)
- Deprecated: `true`

Time the asset was created or provisioned. Deprecate: creationTime should be populated in Attribute as generic metadata.

### `firstDiscoverTime`

- Type: `timestamp` (singular)

Time the asset was first discovered (by asset management/discoverability software).

### `lastDiscoverTime`

- Type: `timestamp` (singular)

Time the asset was last discovered (by asset management/discoverability software).

### `systemLastUpdateTime`

- Type: `timestamp` (singular)

Time the asset system or OS was last updated. For all other operations that are not system updates (such as resizing a VM), use Attribute.lastUpdateTime.

### `lastBootTime`

- Type: `timestamp` (singular)

Time the asset was last boot started.

### `labels`

- Type: [`Label`](label.md) (repeated)
- Deprecated: `true`

Metadata labels for the asset. Deprecated: labels should be populated in Attribute as generic metadata.

### `deploymentStatus`

- Type: [`DeploymentStatus`](../enums/asset_deployment_status.md) (singular)

The deployment status of the asset for device lifecycle purposes.

### `vulnerabilities`

- Type: [`Vulnerability`](vulnerability.md) (repeated)

Vulnerabilities discovered on asset.

### `attribute`

- Type: [`Attribute`](attribute.md) (singular)

Generic entity metadata attributes of the asset.

### `wmiPersistenceItem`

- Type: [`WmiPersistenceItem`](wmi_persistence_item.md) (singular)

Information about a WMI persistence item.
