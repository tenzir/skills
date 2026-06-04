# Noun

The Noun type is used to represent the different entities in an event: principal, src, target, observer, intermediary, and about. It stores attributes known about the entity. For example, if the entity is a device with multiple IP or MAC addresses, it stores the IP and MAC addresses that are relevant to the event.

- **Full name**: `google.backstory.Noun`
- **Fields**: `38`
- **Nested enums**: `1`

## Nested enums

- [Noun.Platform](../enums/noun_platform.md)

## Fields

### `hostname`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `hostname`

Client hostname or domain name field. Hostname also doubles as the domain for remote entities. This field can be used as an entity indicator for asset entities.

### `domain`

- **Number**: `30`
- **Cardinality**: `singular`
- **Type**: [`Domain`](domain.md)
- **JSON name**: `domain`

Information about the domain.

### `artifact`

- **Number**: `32`
- **Cardinality**: `singular`
- **Type**: [`Artifact`](artifact.md)
- **JSON name**: `artifact`

Information about an artifact.

### `url_metadata`

- **Number**: `37`
- **Cardinality**: `singular`
- **Type**: [`Url`](url.md)
- **JSON name**: `urlMetadata`

Information about the URL.

### `browser`

- **Number**: `38`
- **Cardinality**: `singular`
- **Type**: [`Browser`](browser.md)
- **JSON name**: `browser`

Information about an entry in the web browser's local history database.

### `asset_id`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `assetId`

The asset ID. This field can be used as an entity indicator for asset entities.

### `user`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`User`](user.md)
- **JSON name**: `user`

Information about the user.

### `user_management_chain`

- **Number**: `29`
- **Cardinality**: `repeated`
- **Type**: [`User`](user.md)
- **JSON name**: `userManagementChain`

Information about the user's management chain (reporting hierarchy). Note: user_management_chain is only populated when data is exported to BigQuery since recursive fields (e.g. user.managers) are not supported by BigQuery.

### `group`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: [`Group`](group.md)
- **JSON name**: `group`

Information about the group.

### `process`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`Process`](process.md)
- **JSON name**: `process`

Information about the process.

### `process_ancestors`

- **Number**: `28`
- **Cardinality**: `repeated`
- **Type**: [`Process`](process.md)
- **JSON name**: `processAncestors`

Information about the process's ancestors ordered from immediate ancestor (parent process) to root. Note: process_ancestors is only populated when data is exported to BigQuery since recursive fields (e.g. process.parent_process) are not supported by BigQuery.

### `asset`

- **Number**: `27`
- **Cardinality**: `singular`
- **Type**: [`Asset`](asset.md)
- **JSON name**: `asset`

Information about the asset.

### `ip`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `ip`

A list of IP addresses associated with a network connection. This field can be used as an entity indicator for asset entities.

### `nat_ip`

- **Number**: `21`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `natIp`

A list of NAT translated IP addresses associated with a network connection.

### `port`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `port`

Source or destination network port number when a specific network connection is described within an event.

### `nat_port`

- **Number**: `22`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `natPort`

NAT external network port number when a specific network connection is described within an event.

### `mac`

- **Number**: `8`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `mac`

List of MAC addresses associated with a device. This field can be used as an entity indicator for asset entities.

### `administrative_domain`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `administrativeDomain`

Domain which the device belongs to (for example, the Microsoft Windows domain).

### `namespace`

- **Number**: `19`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `namespace`

Namespace which the device belongs to, such as "AD forest". Uses for this field include Microsoft Windows AD forest, the name of subsidiary, or the name of acquisition. This field can be used along with an asset indicator to identify an asset.

### `url`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `url`

The URL.

### `file`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: [`File`](file.md)
- **JSON name**: `file`

Information about the file.

### `email`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `email`

Email address. Only filled in for security_result.about

### `registry`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: [`Registry`](registry.md)
- **JSON name**: `registry`

Registry information.

### `application`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `application`

The name of an application or service. Some SSO solutions only capture the name of a target application such as "Atlassian" or "Chronicle".

### `platform`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`Noun.Platform`](../enums/noun_platform.md)
- **JSON name**: `platform`

Platform.

### `platform_version`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `platformVersion`

Platform version. For example, "Microsoft Windows 1803".

### `platform_patch_level`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `platformPatchLevel`

Platform patch level. For example, "Build 17134.48"

### `cloud`

- **Number**: `24`
- **Cardinality**: `singular`
- **Type**: [`Cloud`](cloud.md)
- **JSON name**: `cloud`
- **Deprecated**: `true`

Cloud metadata. Deprecated: cloud should be populated in entity Attribute as generic metadata (e.g. asset.attribute.cloud).

### `location`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: [`Location`](location.md)
- **JSON name**: `location`

Physical location. For cloud environments, set the region in location.name.

### `ip_location`

- **Number**: `34`
- **Cardinality**: `repeated`
- **Type**: [`Location`](location.md)
- **JSON name**: `ipLocation`
- **Deprecated**: `true`

Deprecated: use ip_geo_artifact.location instead.

### `ip_geo_artifact`

- **Number**: `35`
- **Cardinality**: `repeated`
- **Type**: [`Artifact`](artifact.md)
- **JSON name**: `ipGeoArtifact`

Enriched geographic information corresponding to an IP address. Specifically, location and network data.

### `resource`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: [`Resource`](resource.md)
- **JSON name**: `resource`

Information about the resource (e.g. scheduled task, calendar entry). This field should not be used for files, registry, or processes because these objects are already part of Noun.

### `resource_ancestors`

- **Number**: `31`
- **Cardinality**: `repeated`
- **Type**: [`Resource`](resource.md)
- **JSON name**: `resourceAncestors`

Information about the resource's ancestors ordered from immediate ancestor (starting with parent resource).

### `labels`

- **Number**: `23`
- **Cardinality**: `repeated`
- **Type**: [`Label`](label.md)
- **JSON name**: `labels`
- **Deprecated**: `true`

Labels are key-value pairs. For example: key = "env", value = "prod". Deprecated: labels should be populated in entity Attribute as generic metadata (e.g. user.attribute.labels).

### `object_reference`

- **Number**: `25`
- **Cardinality**: `singular`
- **Type**: [`Id`](id.md)
- **JSON name**: `objectReference`

Finding to which the Analyst updated the feedback.

### `investigation`

- **Number**: `26`
- **Cardinality**: `singular`
- **Type**: [`Investigation`](investigation.md)
- **JSON name**: `investigation`

Analyst feedback/investigation for alerts.

### `network`

- **Number**: `33`
- **Cardinality**: `singular`
- **Type**: [`Network`](network.md)
- **JSON name**: `network`

Network details, including sub-messages with details on each protocol (for example, DHCP, DNS, or HTTP).

### `security_result`

- **Number**: `36`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult`](security_result.md)
- **JSON name**: `securityResult`

A list of security results.

## Guidance

Population guidance from the Google UDM usage guide.

### `Noun.administrative_domain`

- **Purpose**: Domain that the device belongs to (for example, the Windows domain).
- **Encoding**: Valid domain name string (128 characters maximum).
- **Example**: corp.altostrat.com

#### Examples

- corp.altostrat.com

### `Noun.asset_id`

- **Purpose**: Vendor-specific unique device identifier (for example, a GUID that is generated when installing endpoint security software on a new device that is used to track that unique device over time).
- **Encoding**: (VendorName or VendorAbbreviation):ID where the VendorName or VendorAbbreviation is a case insensitive vendor name like `Carbon Black` or `CB` and ID is a vendor-specific customer identifier that is globally unique within their customer's environment (for example, a GUID or unique value identifying a unique device). VendorName is alphanumeric and no more than 32 characters long. ID can be a maximum of 128 characters in length and can include alphanumeric characters, dashes, and periods.
- **Example**: `CrowdStrike:0bce4259-4ada-48f3-a904-9a526b01311f`
- **Example**: `CS:0bce4259-4ada-48f3-a904-9a526b01311f`

#### Examples

- `CrowdStrike:0bce4259-4ada-48f3-a904-9a526b01311f`
- `CS:0bce4259-4ada-48f3-a904-9a526b01311f`

### `Noun.email`

- **Purpose**: Email address
- **Encoding**: Standard email address format.
- **Example**: johns@test.altostrat.com

#### Examples

- johns@test.altostrat.com

### `Noun.file`

- **Purpose**: Detailed file metadata.
- **Type**: Object
- **Note**: See Population of File metadata.

### `Noun.hostname`

- **Purpose**: Client hostname or domain name field. Do not include if a URL is present.
- **Encoding**: Valid RFC 1123 hostname.

#### Examples

- userwin10
- www.altostrat.com

### `Noun.ip`

- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

#### Examples

- 192.168.1.2
- 2001:db8:1:3::1

### `Noun.mac`

- **Purpose**: One or more MAC addresses associated with a device.
- **Encoding**: Valid MAC address (EUI-48) in ASCII.
- **Repeatability**: Vendor might provide all of the associated MAC addresses for the device at the time of the event.

#### Examples

- fedc:ba98:7654:3210:fedc:ba98:7654:3210
- 1080:0:0:0:8:800:200c:417a
- 00:a0:0:0:c9:14:c8:29

### `Noun.platform`

- **Purpose**: Platform operating system.
- **Encoding**: Enum
- **Possible values**:
  - `LINUX`
  - `MAC`
  - `WINDOWS`
  - `UNKNOWN_PLATFORM`

### `Noun.platform_patch_level`

- **Purpose**: Platform operating system patch level.
- **Encoding**: Alphanumeric string with punctuation, 64 characters maximum.
- **Example**: Build 17134.48

#### Examples

- Build 17134.48

### `Noun.platform_version`

- **Purpose**: Platform operating system version.
- **Encoding**: Alphanumeric string with punctuation, 64 characters maximum.
- **Example**: Microsoft Windows 10 version 1803

#### Examples

- Microsoft Windows 10 version 1803

### `Noun.port`

- **Purpose**: Source or destination network port number when a specific network connection is described within an event.
- **Encoding**: Valid TCP/IP port number from 1 through 65,535.
- **Examples**: Note: If a port number is specified, there must be one and only one IP address specified in the same Noun.

#### Examples

- 80
- 443

### `Noun.process`

- **Purpose**: Detailed process metadata.
- **Type**: Object
- **Note**: See Population of Process metadata.

### `Noun.registry`

- **Purpose**: Detailed registry metadata.
- **Type**: Object
- **Note**: See Population of Registry metadata

### `Noun.url`

- **Purpose**: Standard URL
- **Encoding**: URL (RFC 3986). Must have a valid protocol prefix (for example, https:// or ftp://). Must include the full domain and path. Might include the URL's parameters.
- **Example**: https://foo.altostrat.com/bletch?a=b;c=d

#### Examples

- https://foo.altostrat.com/bletch?a=b;c=d

### `Noun.user`

- **Purpose**: Detailed user metadata.
- **Type**: Object
- **Note**: See Population of User metadata.
