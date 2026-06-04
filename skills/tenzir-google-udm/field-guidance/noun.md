# Noun Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- [Noun](../messages/noun.md)

## Fields

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
- **Examples**: userwin10 www.altostrat.com

#### Examples

- userwin10
- www.altostrat.com

### `Noun.ip`

- **Purpose**: Single IP address associated with a network connection. One or more IP addresses associated with a participant device at the time of the event (for example, if an EDR product knows all of the IP addresses associated with a device, it can encode all of these within IP fields).
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.
- **Repeatability**: If an event is describing a specific network connection (for example, srcip:srcport > dstip:dstport), the vendor must provide only a single IP address. If an event is describing general activity occurring on a participant device but not a specific network connection, the vendor might provide all of the associated IP addresses for the device at the time of the event.
- **Examples**: 192.168.1.2 2001:db8:1:3::1

#### Examples

- 192.168.1.2
- 2001:db8:1:3::1

### `Noun.mac`

- **Purpose**: One or more MAC addresses associated with a device.
- **Encoding**: Valid MAC address (EUI-48) in ASCII.
- **Repeatability**: Vendor might provide all of the associated MAC addresses for the device at the time of the event.
- **Examples**: fedc:ba98:7654:3210:fedc:ba98:7654:3210 1080:0:0:0:8:800:200c:417a 00:a0:0:0:c9:14:c8:29

#### Examples

- fedc:ba98:7654:3210:fedc:ba98:7654:3210
- 1080:0:0:0:8:800:200c:417a
- 00:a0:0:0:c9:14:c8:29

### `Noun.platform`

- **Purpose**: Platform operating system.
- **Encoding**: Enum
- **Possible values**: LINUX MAC WINDOWS UNKNOWN_PLATFORM

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
- **Examples**: 80 443 Note: If a port number is specified, there must be one and only one IP address specified in the same Noun.

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
