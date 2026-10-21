# Network Activity (network_activity)

Network Activity events report network connection and traffic activity.

- **Class UID**: `4001`
- **Category**: Network Activity
- **Extends**: [Network (network)](network.md)
- **Profiles**: [Network Proxy](../profiles/network_proxy.md), [Load Balancer](../profiles/load_balancer.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

## Constraints

- **At least one of**: `dst_endpoint`, `src_endpoint`

## Inherited attributes

**From Network:**
- `connection_info` (recommended)
- `proxy` (recommended)
- `traffic` (recommended)

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

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Open` - A new network connection was opened.
- `2`: `Close` - The network connection was closed.
- `3`: `Reset` - The network connection was abnormally terminated or closed by a middle device like firewalls.
- `4`: `Fail` - The network connection failed. For example a connection timeout or no route to host.
- `5`: `Refuse` - The network connection was refused. For example an attempt to connect to a server port which is not open.
- `6`: `Traffic` - Network traffic report.
- `7`: `Listen` - A network endpoint began listening for new network connections.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

The responder of the network connection. In some contexts an event source cannot correctly identify the responder. Refer to `is_src_dst_assignment_known` for certainty.

### `is_src_dst_assignment_known`

- **Type**: `boolean_t`
- **Requirement**: recommended
- **Group**: primary

`true` denotes that `src_endpoint` and `dst_endpoint` correctly identify the initiator and responder respectively. `false` denotes that the event source has arbitrarily assigned one peer to `src_endpoint` and the other to `dst_endpoint`, in other words that initiator and responder are not being asserted. This can occur, for example, when the event source is a network appliance that has not observed the initiation of a given connection. In the absence of this attribute, interpretation of the initiator and responder is implementation-specific.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

The initiator of the network connection. In some contexts an event source cannot correctly identify the initiator. Refer to `is_src_dst_assignment_known` for certainty.

### `url`

- **Type**: [`url`](../objects/url.md)
- **Requirement**: recommended
- **Group**: primary

The URL details relevant to the network traffic.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4001`: `Network Activity` - Network Activity events report network connection and traffic activity.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `400100`: `Network Activity: Unknown`
- `400101`: `Network Activity: Open` - A new network connection was opened.
- `400102`: `Network Activity: Close` - The network connection was closed.
- `400103`: `Network Activity: Reset` - The network connection was abnormally terminated or closed by a middle device like firewalls.
- `400104`: `Network Activity: Fail` - The network connection failed. For example a connection timeout or no route to host.
- `400105`: `Network Activity: Refuse` - The network connection was refused. For example an attempt to connect to a server port which is not open.
- `400106`: `Network Activity: Traffic` - Network traffic report.
- `400107`: `Network Activity: Listen` - A network endpoint began listening for new network connections.
- `400199`: `Network Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
