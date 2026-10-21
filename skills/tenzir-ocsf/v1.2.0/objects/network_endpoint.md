# Network Endpoint (network_endpoint)

The Network Endpoint object describes characteristics of a network endpoint. These can be a source or destination of a network connection.

- **Extends**: [Endpoint (endpoint)](endpoint.md)
- **Profiles**: [Container](../profiles/container.md)
- **Observable**: `20`

## Constraints

- **At least one of**: `ip`, `uid`, `name`, `hostname`, `svc_name`, `instance_uid`, `interface_uid`, `interface_name`

## Inherited attributes

**From Endpoint:**
- `hostname` (recommended)
- `instance_uid` (recommended)
- `interface_name` (recommended)
- `interface_uid` (recommended)
- `ip` (recommended)
- `name` (recommended)
- `owner` (recommended)
- `uid` (recommended)

## Attributes

### `autonomous_system`

- **Type**: [`autonomous_system`](autonomous_system.md)
- **Requirement**: optional

The Autonomous System details associated with an IP address.

### `intermediate_ips`

- **Type**: `ip_t`
- **Requirement**: optional

The intermediate IP Addresses. For example, the IP addresses in the HTTP X-Forwarded-For header.

### `proxy_endpoint`

- **Type**: [`network_proxy`](network_proxy.md)
- **Requirement**: optional

The network proxy information pertaining to a specific endpoint. This can be used to describe information pertaining to network address translation (NAT).

### `port`

- **Type**: `port_t`
- **Requirement**: recommended

The port used for communication within the network connection.

### `svc_name`

- **Type**: `string_t`
- **Requirement**: recommended

The service name in service-to-service connections. For example, AWS VPC logs the pkt-src-aws-service and pkt-dst-aws-service fields identify the connection is coming from or going to an AWS service.

### `type`

- **Type**: `string_t`
- **Requirement**: optional

The network endpoint type. For example: `unknown`, `server`, `desktop`, `laptop`, `tablet`, `mobile`, `virtual`, `browser`, or `other`.

### `type_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Sibling**: `type`

#### Enum values

- `0`: `Unknown` - The type is unknown.
- `1`: `Server` - A [server](https://d3fend.mitre.org/dao/artifact/d3f:Server/).
- `2`: `Desktop` - A [desktop computer](https://d3fend.mitre.org/dao/artifact/d3f:DesktopComputer/).
- `3`: `Laptop` - A [laptop computer](https://d3fend.mitre.org/dao/artifact/d3f:LaptopComputer/).
- `4`: `Tablet` - A [tablet computer](https://d3fend.mitre.org/dao/artifact/d3f:TabletComputer/).
- `5`: `Mobile` - A [mobile phone](https://d3fend.mitre.org/dao/artifact/d3f:MobilePhone/).
- `6`: `Virtual` - A [virtual machine](https://d3fend.mitre.org/dao/artifact/d3f:VirtualizationSoftware/).
- `7`: `IOT` - A [IOT (Internet of Things) device](https://www.techtarget.com/iotagenda/definition/IoT-device).
- `8`: `Browser` - A [web browser](https://d3fend.mitre.org/dao/artifact/d3f:Browser/).
- `9`: `Firewall` - A [networking firewall](https://d3fend.mitre.org/dao/artifact/d3f:Firewall/).
- `10`: `Switch` - A [networking switch](https://d3fend.mitre.org/dao/artifact/d3f:Switch/).
- `11`: `Hub` - A [networking hub](https://en.wikipedia.org/wiki/Ethernet_hub).
- `99`: `Other` - The type is not mapped. See the `type` attribute, which contains a data source specific value.

The network endpoint type ID.
