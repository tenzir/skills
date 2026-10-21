# DNS Activity (dns_activity)

DNS Activity events report DNS queries and answers as seen on the network.

- **Class UID**: `4003`
- **Category**: Network Activity
- **Extends**: [Network (network)](network.md)
- **Profiles**: [Host](../profiles/host.md), [Network Proxy](../profiles/network_proxy.md), [Security Control](../profiles/security_control.md), [Load Balancer](../profiles/load_balancer.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

**From Network:**
- `src_endpoint` (required)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
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
- `1`: `Query` - The DNS query request.
- `2`: `Response` - The DNS query response.
- `6`: `Traffic` - Bidirectional DNS request and response traffic.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `answers`

- **Type**: [`dns_answer`](../objects/dns_answer.md)
- **Requirement**: recommended
- **Group**: primary

The Domain Name System (DNS) answers.

### `connection_info`

- **Type**: [`network_connection_info`](../objects/network_connection_info.md)
- **Requirement**: optional
- **Group**: context

The network connection information.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

The responder (server) in a network connection.

### `query`

- **Type**: [`dns_query`](../objects/dns_query.md)
- **Requirement**: recommended
- **Group**: primary

The Domain Name System (DNS) query.

### `query_time`

- **Type**: `timestamp_t`
- **Requirement**: recommended
- **Group**: occurrence

The Domain Name System (DNS) query time.

### `rcode`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The DNS server response code, normalized to the caption of the rcode_id value. In the case of 'Other', it is defined by the event source.

### `rcode_id`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: primary
- **Sibling**: `rcode`

#### Enum values

- `0`: `NoError` - No Error.
- `1`: `FormError` - Format Error.
- `2`: `ServError` - Server Failure.
- `3`: `NXDomain` - Non-Existent Domain.
- `4`: `NotImp` - Not Implemented.
- `5`: `Refused` - Query Refused.
- `6`: `YXDomain` - Name Exists when it should not.
- `7`: `YXRRSet` - RR Set Exists when it should not.
- `8`: `NXRRSet` - RR Set that should exist does not.
- `9`: `NotAuth` - Not Authorized or Server Not Authoritative for zone.
- `10`: `NotZone` - Name not contained in zone.
- `11`: `DSOTYPENI` - DSO-TYPE Not Implemented.
- `16`: `BADSIG_VERS` - TSIG Signature Failure or Bad OPT Version.
- `17`: `BADKEY` - Key not recognized.
- `18`: `BADTIME` - Signature out of time window.
- `19`: `BADMODE` - Bad TKEY Mode.
- `20`: `BADNAME` - Duplicate key name.
- `21`: `BADALG` - Algorithm not supported.
- `22`: `BADTRUNC` - Bad Truncation.
- `23`: `BADCOOKIE` - Bad/missing Server Cookie.
- `24`: `Unassigned` - The codes deemed to be unassigned by the RFC (unassigned codes: 12-15, 24-3840, 4096-65534).
- `25`: `Reserved` - The codes deemed to be reserved by the RFC (codes: 3841-4095, 65535).
- `99`: `Other` - The dns response code is not defined by the RFC.

The normalized identifier of the DNS server response code. See [RFC-6895](https://datatracker.ietf.org/doc/html/rfc6895).

### `response_time`

- **Type**: `timestamp_t`
- **Requirement**: recommended
- **Group**: occurrence

The Domain Name System (DNS) response time.

### `traffic`

- **Type**: [`network_traffic`](../objects/network_traffic.md)
- **Requirement**: optional
- **Group**: context

The network traffic refers to the amount of data moving across a network at a given point of time. Intended to be used alongside Network Connection.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4003`: `DNS Activity` - DNS Activity events report DNS queries and answers as seen on the network.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `400300`: `DNS Activity: Unknown`
- `400301`: `DNS Activity: Query` - The DNS query request.
- `400302`: `DNS Activity: Response` - The DNS query response.
- `400306`: `DNS Activity: Traffic` - Bidirectional DNS request and response traffic.
- `400399`: `DNS Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
