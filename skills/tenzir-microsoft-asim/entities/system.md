# ASimSystem

- **Source**: [`ASIM/schemas/entities/ASimSystem.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/entities/ASimSystem.yaml)
- **Fields**: `22`

## Included by

- [AuditEvent](../schemas/audit_event.md) as `Src`
- [AuditEvent](../schemas/audit_event.md) as `Target`
- [Authentication](../schemas/authentication.md) as `Src`
- [Authentication](../schemas/authentication.md) as `Target`
- [Dhcp](../schemas/dhcp.md) as `Src`
- [Dns](../schemas/dns.md) as `Src`
- [Dns](../schemas/dns.md) as `Dst`
- [FileEvent](../schemas/file_event.md) as `Src`
- [User Management](../schemas/user_management.md) as `Src`

## Raw fields

### `<<Role>>Description`

- **Class**: `Optional`
- **Type**: `string`

A descriptive text associated with the device.

### `<<Role>>DeviceType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DeviceType](../enumerations/device_type.md)

The type of the device.

### `<<Role>>Domain`

- **Class**: `Optional`
- **Type**: `string`

The domain of the device.

### `<<Role>>DomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`<<Role>>Domain`](../fields/role_domain.md)

The type of the domain.

### `<<Role>>DvcId`

- **Class**: `Optional`
- **Type**: `string`

The ID of the device.

### `<<Role>>DvcIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DvcIdType](../enumerations/dvc_id_type.md)
- **Follows**: [`<<Role>>DvcId`](../fields/role_dvc_id.md)

The type of the DvcId.

### `<<Role>>DvcScope`

- **Class**: `Optional`
- **Type**: `string`

The cloud platform scope the device belongs to. TargetDvcScope map to a subscription ID on Azure and to an account ID on AWS.

### `<<Role>>DvcScopeId`

- **Class**: `Optional`
- **Type**: `string`

The cloud platform scope ID the device belongs to. DvcScopeId maps to a subscription ID on Azure and to an account ID on AWS.

### `<<Role>>FQDN`

- **Class**: `Optional`
- **Type**: `string`

The device hostname, including domain information when available.

### `<<Role>>GeoCity`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `City`

The city associated with the IP address.

### `<<Role>>GeoCountry`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Country`

The country associated with the IP address.

### `<<Role>>GeoLatitude`

- **Class**: `Optional`
- **Type**: `Double`

The latitude of the geographical coordinate associated with the IP address.

### `<<Role>>GeoLongitude`

- **Class**: `Optional`
- **Type**: `Double`

The longitude of the geographical coordinate associated with the IP address.

### `<<Role>>GeoRegion`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Region`

The region within a country associated with the IP address.

### `<<Role>>Hostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### `<<Role>>IpAddr`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `IP Address`

The IP address of the device.

### `<<Role>>MacAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `MAC address`

The MAC address of the device.

### `<<Role>>OriginalRiskLevel`

- **Class**: `Optional`
- **Type**: `string`

The risk level associated with the source. As reported by the reporting device or enriched.

### `<<Role>>PortNumber`

- **Class**: `Optional`
- **Type**: `int`

The IP port on which the device communicated, if applicable.

### `<<Role>>RiskLevel`

- **Class**: `Optional`
- **Type**: `int`

The risk level associated with the source. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk. User the OriginalRiskLevel field for the value as reported or enriched.

### `Dst`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: `<<role>>FQDN`, `<<role>>DvcId`, `<<role>>Hostname`, `<<role>>IpAddr`, `<<role>>MacAddr`, `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Target`, `Dst`

A unique identifier of the destination device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### `Src`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: `<<role>>FQDN`, `<<role>>DvcId`, `<<role>>Hostname`, `<<role>>IpAddr`, `<<role>>MacAddr`, `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Acting`, `Src`

A unique identifier of the source device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.
