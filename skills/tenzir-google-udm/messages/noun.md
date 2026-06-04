# Noun

The Noun type is used to represent the different entities in an event: principal, src, target, observer, intermediary, and about. It stores attributes known about the entity. For example, if the entity is a device with multiple IP or MAC addresses, it stores the IP and MAC addresses that are relevant to the event.

- **Full name**: `google.backstory.Noun`
- **Fields**: `38`
- **Nested enums**: `1`

## Nested enums

- [Noun.Platform](../enums/noun_platform.md)

## Fields

### `hostname`

- Type: `string` (singular)

Client hostname or domain name field. Hostname also doubles as the domain for remote entities. This field can be used as an entity indicator for asset entities.

### `domain`

- Type: [`Domain`](domain.md) (singular)

Information about the domain.

### `artifact`

- Type: [`Artifact`](artifact.md) (singular)

Information about an artifact.

### `urlMetadata`

- Type: [`Url`](url.md) (singular)

Information about the URL.

### `browser`

- Type: [`Browser`](browser.md) (singular)

Information about an entry in the web browser's local history database.

### `assetId`

- Type: `string` (singular)

The asset ID. This field can be used as an entity indicator for asset entities.

### `user`

- Type: [`User`](user.md) (singular)

Information about the user.

### `userManagementChain`

- Type: [`User`](user.md) (repeated)

Information about the user's management chain (reporting hierarchy). Note: userManagementChain is only populated when data is exported to BigQuery since recursive fields (e.g. user.managers) are not supported by BigQuery.

### `group`

- Type: [`Group`](group.md) (singular)

Information about the group.

### `process`

- Type: [`Process`](process.md) (singular)

Information about the process.

### `processAncestors`

- Type: [`Process`](process.md) (repeated)

Information about the process's ancestors ordered from immediate ancestor (parent process) to root. Note: processAncestors is only populated when data is exported to BigQuery since recursive fields (e.g. process.parentProcess) are not supported by BigQuery.

### `asset`

- Type: [`Asset`](asset.md) (singular)

Information about the asset.

### `ip`

- Type: `string` (repeated)

A list of IP addresses associated with a network connection. This field can be used as an entity indicator for asset entities.

### `natIp`

- Type: `string` (repeated)

A list of NAT translated IP addresses associated with a network connection.

### `port`

- Type: `int32` (singular)

Source or destination network port number when a specific network connection is described within an event.

### `natPort`

- Type: `int32` (singular)

NAT external network port number when a specific network connection is described within an event.

### `mac`

- Type: `string` (repeated)

List of MAC addresses associated with a device. This field can be used as an entity indicator for asset entities.

### `administrativeDomain`

- Type: `string` (singular)

Domain which the device belongs to (for example, the Microsoft Windows domain).

### `namespace`

- Type: `string` (singular)

Namespace which the device belongs to, such as "AD forest". Uses for this field include Microsoft Windows AD forest, the name of subsidiary, or the name of acquisition. This field can be used along with an asset indicator to identify an asset.

### `url`

- Type: `string` (singular)

The URL.

### `file`

- Type: [`File`](file.md) (singular)

Information about the file.

### `email`

- Type: `string` (singular)

Email address. Only filled in for securityResult.about

### `registry`

- Type: [`Registry`](registry.md) (singular)

Registry information.

### `application`

- Type: `string` (singular)

The name of an application or service. Some SSO solutions only capture the name of a target application such as "Atlassian" or "Chronicle".

### `platform`

- Type: [`Noun.Platform`](../enums/noun_platform.md) (singular)

Platform.

### `platformVersion`

- Type: `string` (singular)

Platform version. For example, "Microsoft Windows 1803".

### `platformPatchLevel`

- Type: `string` (singular)

Platform patch level. For example, "Build 17134.48"

### `cloud`

- Type: [`Cloud`](cloud.md) (singular)
- Deprecated: `true`

Cloud metadata. Deprecated: cloud should be populated in entity Attribute as generic metadata (e.g. asset.attribute.cloud).

### `location`

- Type: [`Location`](location.md) (singular)

Physical location. For cloud environments, set the region in location.name.

### `ipLocation`

- Type: [`Location`](location.md) (repeated)
- Deprecated: `true`

Deprecated: use ipGeoArtifact.location instead.

### `ipGeoArtifact`

- Type: [`Artifact`](artifact.md) (repeated)

Enriched geographic information corresponding to an IP address. Specifically, location and network data.

### `resource`

- Type: [`Resource`](resource.md) (singular)

Information about the resource (e.g. scheduled task, calendar entry). This field should not be used for files, registry, or processes because these objects are already part of Noun.

### `resourceAncestors`

- Type: [`Resource`](resource.md) (repeated)

Information about the resource's ancestors ordered from immediate ancestor (starting with parent resource).

### `labels`

- Type: [`Label`](label.md) (repeated)
- Deprecated: `true`

Labels are key-value pairs. For example: key = "env", value = "prod". Deprecated: labels should be populated in entity Attribute as generic metadata (e.g. user.attribute.labels).

### `objectReference`

- Type: [`Id`](id.md) (singular)

Finding to which the Analyst updated the feedback.

### `investigation`

- Type: [`Investigation`](investigation.md) (singular)

Analyst feedback/investigation for alerts.

### `network`

- Type: [`Network`](network.md) (singular)

Network details, including sub-messages with details on each protocol (for example, DHCP, DNS, or HTTP).

### `securityResult`

- Type: [`SecurityResult`](security_result.md) (repeated)

A list of security results.

## Guidance

Population guidance from the Google UDM usage guide.

### `Noun.administrativeDomain`

- **Purpose**: Domain that the device belongs to (for example, the Windows domain).
- **Encoding**: Valid domain name string (128 characters maximum).
- **Example**: corp.altostrat.com

#### Examples

- corp.altostrat.com

### `Noun.assetId`

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

### `Noun.platformPatchLevel`

- **Purpose**: Platform operating system patch level.
- **Encoding**: Alphanumeric string with punctuation, 64 characters maximum.
- **Example**: Build 17134.48

#### Examples

- Build 17134.48

### `Noun.platformVersion`

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
