# Dns

- **Version**: `0.1.7`
- **Last updated**: Jan 01 2023
- **Source**: [`ASIM/schemas/ASimDns.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/ASimDns.yaml)
- **Fields**: `148`

## References

- [ASIM Dns Schema](https://aka.ms/ASimDnsDoc)
- [ASIM](https://aka.ms/AboutASIM)

## Includes

| Include | File | Role |
| --- | --- | --- |
| Enumerations | `ASIM/schemas/common/ASimEnumerations.yaml` |  |
| Event Fields | `ASIM/schemas/common/ASimEventFields.yaml` |  |
| Inspection fields | `ASIM/schemas/common/ASimInspectionFields.yaml` |  |
| Dvc | `ASIM/schemas/entities/ASimDvc.yaml` |  |
| Source user entity | `ASIM/schemas/entities/ASimUser.yaml` | `Src` |
| Source process entity | `ASIM/schemas/entities/ASimProcess.yaml` | `Src` |
| Source system entity | `ASIM/schemas/entities/ASimSystem.yaml` | `Src` |
| Destination system entity | `ASIM/schemas/entities/ASimSystem.yaml` | `Dst` |

## Resolved fields

| Field | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [`AdditionalFields`](../fields/additional_fields.md) | `Recommended` | `dynamic` |  |  | inherited from Event Fields |
| [`DnsFlags`](../fields/dns_flags.md) | `Optional` | `string` |  |  | local |
| [`DnsFlagsAuthenticated`](../fields/dns_flags_authenticated.md) | `Optional` | `bool` |  |  | local |
| [`DnsFlagsAuthoritative`](../fields/dns_flags_authoritative.md) | `Optional` | `bool` |  |  | local |
| [`DnsFlagsCheckingDisabled`](../fields/dns_flags_checking_disabled.md) | `Optional` | `bool` |  |  | local |
| [`DnsFlagsRecursionAvailable`](../fields/dns_flags_recursion_available.md) | `Optional` | `bool` |  |  | local |
| [`DnsFlagsRecursionDesired`](../fields/dns_flags_recursion_desired.md) | `Optional` | `bool` |  |  | local |
| [`DnsFlagsTruncated`](../fields/dns_flags_truncated.md) | `Optional` | `bool` |  |  | local |
| [`DnsFlagsZ`](../fields/dns_flags_z.md) | `Optional` | `bool` |  |  | local |
| [`DnsNetworkDuration`](../fields/dns_network_duration.md) | `Optional` | `integer` |  |  | local |
| [`DnsQuery`](../fields/dns_query.md) | `Mandatory` | `string` |  |  | local |
| [`DnsQueryClass`](../fields/dns_query_class.md) | `Optional` | `integer` |  |  | local |
| [`DnsQueryClassName`](../fields/dns_query_class_name.md) | `Optional` | `string` | `Enumerated` | `TBD` | local |
| [`DnsQueryType`](../fields/dns_query_type.md) | `Optional` | `integer` |  |  | local |
| [`DnsQueryTypeName`](../fields/dns_query_type_name.md) | `Recommended` | `string` | `Enumerated` | `TBD` | local |
| [`DnsResponseCode`](../fields/dns_response_code.md) | `Optional` | `integer` |  |  | local |
| [`DnsResponseCodeName`](../fields/dns_response_code_name.md) | `Alias` | `string` |  |  | local |
| [`DnsResponseIpCity`](../fields/dns_response_ip_city.md) | `Optional` | `string` | `City` |  | local |
| [`DnsResponseIpCountry`](../fields/dns_response_ip_country.md) | `Optional` | `string` | `Country` |  | local |
| [`DnsResponseIpLatitude`](../fields/dns_response_ip_latitude.md) | `Optional` | `float` | `Latitude` |  | local |
| [`DnsResponseIpLongitude`](../fields/dns_response_ip_longitude.md) | `Optional` | `float` | `Longitude` |  | local |
| [`DnsResponseIpRegion`](../fields/dns_response_ip_region.md) | `Optional` | `string` | `Region` |  | local |
| [`DnsResponseName`](../fields/dns_response_name.md) | `Optional` | `string` |  |  | local |
| [`DnsSessionId`](../fields/dns_session_id.md) | `Optional` | `string` |  |  | local |
| [`Domain`](../fields/domain.md) | `Alias` | `string` |  |  | local |
| [`DomainCategory`](../fields/domain_category.md) | `Alias` | `string` |  |  | local |
| [`Dst`](../fields/dst.md) | `Alias` | `string` |  |  | inherited from Destination system entity as Dst |
| [`DstDescription`](../fields/dst_description.md) | `Optional` | `string` |  |  | inherited from Destination system entity as Dst |
| [`DstDeviceType`](../fields/dst_device_type.md) | `Optional` | `string` | `Enumerated` | [DeviceType](../enumerations/device_type.md) | inherited from Destination system entity as Dst |
| [`DstDomain`](../fields/dst_domain.md) | `Optional` | `string` |  |  | inherited from Destination system entity as Dst |
| [`DstDomainType`](../fields/dst_domain_type.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Destination system entity as Dst |
| [`DstDvcId`](../fields/dst_dvc_id.md) | `Optional` | `string` |  |  | inherited from Destination system entity as Dst |
| [`DstDvcIdType`](../fields/dst_dvc_id_type.md) | `Conditional` | `string` | `Enumerated` | [DvcIdType](../enumerations/dvc_id_type.md) | inherited from Destination system entity as Dst |
| [`DstDvcScope`](../fields/dst_dvc_scope.md) | `Optional` | `string` |  |  | inherited from Destination system entity as Dst |
| [`DstDvcScopeId`](../fields/dst_dvc_scope_id.md) | `Optional` | `string` |  |  | inherited from Destination system entity as Dst |
| [`DstFQDN`](../fields/dst_fqdn.md) | `Optional` | `string` |  |  | inherited from Destination system entity as Dst |
| [`DstGeoCity`](../fields/dst_geo_city.md) | `Optional` | `string` | `City` |  | inherited from Destination system entity as Dst |
| [`DstGeoCountry`](../fields/dst_geo_country.md) | `Optional` | `string` | `Country` |  | inherited from Destination system entity as Dst |
| [`DstGeoLatitude`](../fields/dst_geo_latitude.md) | `Optional` | `Double` |  |  | inherited from Destination system entity as Dst |
| [`DstGeoLongitude`](../fields/dst_geo_longitude.md) | `Optional` | `Double` |  |  | inherited from Destination system entity as Dst |
| [`DstGeoRegion`](../fields/dst_geo_region.md) | `Optional` | `string` | `Region` |  | inherited from Destination system entity as Dst |
| [`DstHostname`](../fields/dst_hostname.md) | `Optional` | `string` | `Hostname` |  | inherited from Destination system entity as Dst |
| [`DstIpAddr`](../fields/dst_ip_addr.md) | `Recommended` | `string` | `IP Address` |  | inherited from Destination system entity as Dst |
| [`DstMacAddr`](../fields/dst_mac_addr.md) | `Optional` | `string` | `MAC address` |  | inherited from Destination system entity as Dst |
| [`DstOriginalRiskLevel`](../fields/dst_original_risk_level.md) | `Optional` | `string` |  |  | inherited from Destination system entity as Dst |
| [`DstPortNumber`](../fields/dst_port_number.md) | `Optional` | `int` |  |  | inherited from Destination system entity as Dst |
| [`DstRiskLevel`](../fields/dst_risk_level.md) | `Optional` | `int` |  |  | inherited from Destination system entity as Dst |
| [`Duration`](../fields/duration.md) | `Alias` | `integer` |  |  | local |
| [`Dvc`](../fields/dvc.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [`DvcAction`](../fields/dvc_action.md) | `Recommended` | `string` |  |  | inherited from Dvc |
| [`DvcDescription`](../fields/dvc_description.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcDomain`](../fields/dvc_domain.md) | `Recommended` | `string` |  |  | inherited from Dvc |
| [`DvcDomainType`](../fields/dvc_domain_type.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Dvc |
| [`DvcFQDN`](../fields/dvc_fqdn.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcHostname`](../fields/dvc_hostname.md) | `Recommended` | `string` | `Hostname` |  | inherited from Dvc |
| [`DvcId`](../fields/dvc_id.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcIdType`](../fields/dvc_id_type.md) | `Conditional` | `string` | `Enumerated` | [DvcIdType](../enumerations/dvc_id_type.md) | inherited from Dvc |
| [`DvcInterface`](../fields/dvc_interface.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcIpAddr`](../fields/dvc_ip_addr.md) | `Recommended` | `string` | `IP Address` |  | inherited from Dvc |
| [`DvcMacAddr`](../fields/dvc_mac_addr.md) | `Optional` | `string` | `MAC address` |  | inherited from Dvc |
| [`DvcOriginalAction`](../fields/dvc_original_action.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcOs`](../fields/dvc_os.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcOsVersion`](../fields/dvc_os_version.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcScope`](../fields/dvc_scope.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcScopeId`](../fields/dvc_scope_id.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcZone`](../fields/dvc_zone.md) | `Optional` | `string` | `MAC address` |  | inherited from Dvc |
| [`EventCount`](../fields/event_count.md) | `Optional` | `int` |  |  | inherited from Event Fields |
| [`EventEndTime`](../fields/event_end_time.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`EventMessage`](../fields/event_message.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOriginalResultDetails`](../fields/event_original_result_details.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOriginalSeverity`](../fields/event_original_severity.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOriginalSubType`](../fields/event_original_sub_type.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOriginalType`](../fields/event_original_type.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOriginalUid`](../fields/event_original_uid.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOwner`](../fields/event_owner.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [`EventProduct`](../fields/event_product.md) | `Mandatory` | `string` | `Enumerated` | [EventProduct](../enumerations/event_product.md) | inherited from Event Fields |
| [`EventProductVersion`](../fields/event_product_version.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventReportUrl`](../fields/event_report_url.md) | `Optional` | `string` | `URL` |  | inherited from Event Fields |
| [`EventResult`](../fields/event_result.md) | `Mandatory` | `string` | `Enumerated` | `Success`, `Failure`, `Partial`, `NA` | inherited from Event Fields |
| [`EventResultDetails`](../fields/event_result_details.md) | `Mandatory` | `string` | `Enumerated` | `TBD` | local override |
| [`EventSchema`](../fields/event_schema.md) | `Mandatory` | `string` | `Enumerated` | [Dns](../schemas/dns.md) | local override |
| [`EventSchemaVersion`](../fields/event_schema_version.md) | `Mandatory` | `string` | `SchemaVersion` |  | inherited from Event Fields |
| [`EventSeverity`](../fields/event_severity.md) | `Recommended` | `string` | `Enumerated` | `Informational`, `Low`, `Medium`, `High` | inherited from Event Fields |
| [`EventStartTime`](../fields/event_start_time.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`EventSubType`](../fields/event_sub_type.md) | `Mandatory` | `string` | `Enumerated` | `request`, `response` | local override |
| [`EventType`](../fields/event_type.md) | `Mandatory` | `string` | `Enumerated` | `TBD` | local override |
| [`EventVendor`](../fields/event_vendor.md) | `Mandatory` | `string` | `Enumerated` | [EventVendor](../enumerations/event_vendor.md) | inherited from Event Fields |
| [`Hostname`](../fields/hostname.md) | `Alias` | `string` |  |  | local |
| [`IpAddr`](../fields/ip_addr.md) | `Alias` | `string` | `IP Address` |  | local |
| [`NetworkProtocol`](../fields/network_protocol.md) | `Optional` | `string` | `Enumerated` | `TCP`, `UDP` | local |
| [`NetworkProtocolVersion`](../fields/network_protocol_version.md) | `Optional` | `string` | `Enumerated` | `TBD` | local |
| [`Process`](../fields/process.md) | `Alias` | `string` |  |  | local |
| [`Rule`](../fields/rule.md) | `Alias` | `string` |  |  | inherited from Inspection fields |
| [`RuleName`](../fields/rule_name.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`RuleNumber`](../fields/rule_number.md) | `Optional` | `int` |  |  | inherited from Inspection fields |
| [`SessionId`](../fields/session_id.md) | `Alias` | `string` |  |  | local |
| [`Src`](../fields/src.md) | `Alias` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDescription`](../fields/src_description.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDeviceType`](../fields/src_device_type.md) | `Optional` | `string` | `Enumerated` | [DeviceType](../enumerations/device_type.md) | inherited from Source system entity as Src |
| [`SrcDomain`](../fields/src_domain.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDomainType`](../fields/src_domain_type.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Source system entity as Src |
| [`SrcDvcId`](../fields/src_dvc_id.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDvcIdType`](../fields/src_dvc_id_type.md) | `Conditional` | `string` | `Enumerated` | [DvcIdType](../enumerations/dvc_id_type.md) | inherited from Source system entity as Src |
| [`SrcDvcScope`](../fields/src_dvc_scope.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDvcScopeId`](../fields/src_dvc_scope_id.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcFQDN`](../fields/src_fqdn.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcGeoCity`](../fields/src_geo_city.md) | `Optional` | `string` | `City` |  | inherited from Source system entity as Src |
| [`SrcGeoCountry`](../fields/src_geo_country.md) | `Optional` | `string` | `Country` |  | inherited from Source system entity as Src |
| [`SrcGeoLatitude`](../fields/src_geo_latitude.md) | `Optional` | `Double` |  |  | inherited from Source system entity as Src |
| [`SrcGeoLongitude`](../fields/src_geo_longitude.md) | `Optional` | `Double` |  |  | inherited from Source system entity as Src |
| [`SrcGeoRegion`](../fields/src_geo_region.md) | `Optional` | `string` | `Region` |  | inherited from Source system entity as Src |
| [`SrcHostname`](../fields/src_hostname.md) | `Optional` | `string` | `Hostname` |  | inherited from Source system entity as Src |
| [`SrcIpAddr`](../fields/src_ip_addr.md) | `Recommended` | `string` | `IP Address` |  | inherited from Source system entity as Src |
| [`SrcMacAddr`](../fields/src_mac_addr.md) | `Optional` | `string` | `MAC address` |  | inherited from Source system entity as Src |
| [`SrcOriginalRiskLevel`](../fields/src_original_risk_level.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcOriginalUserType`](../fields/src_original_user_type.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`SrcPortNumber`](../fields/src_port_number.md) | `Optional` | `int` |  |  | inherited from Source system entity as Src |
| [`SrcProcessCommandLine`](../fields/src_process_command_line.md) | `Optional` | `string` |  |  | inherited from Source process entity as Src |
| [`SrcProcessGuid`](../fields/src_process_guid.md) | `Optional` | `string` |  |  | inherited from Source process entity as Src |
| [`SrcProcessId`](../fields/src_process_id.md) | `Optional` | `string` |  |  | inherited from Source process entity as Src |
| [`SrcProcessName`](../fields/src_process_name.md) | `Optional` | `string` |  |  | inherited from Source process entity as Src |
| [`SrcRiskLevel`](../fields/src_risk_level.md) | `Optional` | `int` |  |  | inherited from Source system entity as Src |
| [`SrcUserId`](../fields/src_user_id.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`SrcUserIdType`](../fields/src_user_id_type.md) | `Conditional` | `string` | `Enumerated` | [UserIdType](../enumerations/user_id_type.md) | inherited from Source user entity as Src |
| [`SrcUsername`](../fields/src_username.md) | `Recommended` | `string` | `Username` |  | inherited from Source user entity as Src |
| [`SrcUsernameType`](../fields/src_username_type.md) | `Conditional` | `string` | `Enumerated` | [UsernameType](../enumerations/username_type.md) | inherited from Source user entity as Src |
| [`SrcUserScope`](../fields/src_user_scope.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`SrcUserScopeId`](../fields/src_user_scope_id.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`SrcUserSessionId`](../fields/src_user_session_id.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`SrcUserType`](../fields/src_user_type.md) | `Optional` | `string` | `Enumerated` | [UserType](../enumerations/user_type.md) | inherited from Source user entity as Src |
| [`SrcUserUid`](../fields/src_user_uid.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`ThreatCategory`](../fields/threat_category.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatConfidence`](../fields/threat_confidence.md) | `Optional` | `int` | `ConfidenceLevel` |  | inherited from Inspection fields |
| [`ThreatField`](../fields/threat_field.md) | `Conditional` | `string` | `Enumerated` | `SrcIpAddr`, `DstIpAddr`, `Domain`, `DnsResponseName` | local override |
| [`ThreatFirstReportedTime`](../fields/threat_first_reported_time.md) | `Optional` | `datetime` |  |  | inherited from Inspection fields |
| [`ThreatId`](../fields/threat_id.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatIpAddr`](../fields/threat_ip_addr.md) | `Optional` | `string` | `IP Address` |  | local |
| [`ThreatIsActive`](../fields/threat_is_active.md) | `Optional` | `bool` |  |  | inherited from Inspection fields |
| [`ThreatLastReportedTime`](../fields/threat_last_reported_time.md) | `Optional` | `datetime` |  |  | inherited from Inspection fields |
| [`ThreatName`](../fields/threat_name.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatOriginalConfidence`](../fields/threat_original_confidence.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatOriginalRiskLevel`](../fields/threat_original_risk_level.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatRiskLevel`](../fields/threat_risk_level.md) | `Optional` | `int` | `RiskLevel` |  | inherited from Inspection fields |
| [`TimeGenerated`](../fields/time_generated.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`TransactionIdHex`](../fields/transaction_id_hex.md) | `Recommended` | `string` |  |  | local |
| [`Type`](../fields/type.md) | `Mandatory` | `string` |  |  | inherited from Event Fields |
| [`UrlCategory`](../fields/url_category.md) | `Optional` | `string` |  |  | local |
| [`User`](../fields/user.md) | `Alias` | `string` | `Username` |  | local |

## Fields

### `AdditionalFields`

- **Class**: `Recommended`
- **Type**: `dynamic`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

### `DnsFlags`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

List of strings  The flags field, as provided by the reporting device. If flag information is provided in multiple fields, concatenate them with comma as a separator.

#### Notes

Since DNS flags are complex to parse and are less often used by analytics, parsing, and normalization aren't required. Microsoft Sentinel can use an auxiliary function to provide flags information. For more information, see Handling DNS response.

#### Examples

- `DR`

### `DnsFlagsAuthenticated`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS AD flag, which is related to DNSSEC, indicates in a response that all data included in the answer and authority sections of the response have been verified by the server according to the policies of that server. For more information, see RFC 3655 Section 6.1 for more information.

### `DnsFlagsAuthoritative`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS AA flag indicates whether the response from the server was authoritative

### `DnsFlagsCheckingDisabled`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS CD flag, which is related to DNSSEC, indicates in a query that non-verified data is acceptable to the system sending the query. For more information, see RFC 3655 Section 6.1 for more information.

### `DnsFlagsRecursionAvailable`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS RA flag indicates in a response that that server supports recursive queries.

### `DnsFlagsRecursionDesired`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS RD flag indicates in a request that that client would like the server to use recursive queries.

### `DnsFlagsTruncated`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS TC flag indicates that a response was truncated as it exceeded the maximum response size.

### `DnsFlagsZ`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS Z flag is a deprecated DNS flag, which might be reported by older DNS systems.

### `DnsNetworkDuration`

- **Class**: `Optional`
- **Type**: `integer`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The amount of time, in milliseconds, for the completion of DNS request.

#### Examples

- `1500`

### `DnsQuery`

- **Class**: `Mandatory`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The domain that the request tries to resolve.

#### Notes

- Some sources send valid FQDN queries in a different format. For example, in the DNS protocol itself, the query includes a dot (.) at the end, which must be removed.
- While the DNS protocol limits the type of value in this field to an FQDN, most DNS servers allow any value, and this field is therefore not limited to FQDN values only. Most notably, DNS tunneling attacks may use invalid FQDN values in the query field.
- While the DNS protocol allows for multiple queries in a single request, this scenario is rare, if it's found at all. If the request has multiple queries, store the first one in this field, and then and optionally keep the rest in the AdditionalFields field.

#### Examples

- `www.malicious.com`

### `DnsQueryClass`

- **Class**: `Optional`
- **Type**: `integer`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS class ID. In practice, only the IN class (ID 1) is used, and therefore this field is less valuable.

### `DnsQueryClassName`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TBD`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS class name. In practice, only the IN class (ID 1) is used, and therefore this field is less valuable.

#### Examples

- `IN`

### `DnsQueryType`

- **Class**: `Optional`
- **Type**: `integer`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS Resource Record Type codes.

#### Examples

- `28`

### `DnsQueryTypeName`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TBD`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS Resource Record Type names.

#### Notes

- IANA doesn't define the case for the values, so analytics must normalize the case as needed.
- The value ANY is supported for the response code 255.
- The value TYPExxxx is supported for unmapped response codes, where xxxx is the numerical value of the response code, as reported by the BIND DNS server.
- If the source provides only a numerical query type code and not a query type name, the parser must include a lookup table to enrich with this value.

#### Examples

- `AAAA`

### `DnsResponseCode`

- **Class**: `Optional`
- **Type**: `integer`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS numerical response code.

#### Examples

- `3`

### `DnsResponseCodeName`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`EventResultDetails`](../fields/event_result_details.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to EventResultDetails

### `DnsResponseIpCity`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `City`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The city associated with one of the IP addresses in the DNS response. For more information, see Logical types.

#### Examples

- `Burlington`

### `DnsResponseIpCountry`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Country`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The country associated with one of the IP addresses in the DNS response. For more information, see Logical types.

#### Examples

- `USA`

### `DnsResponseIpLatitude`

- **Class**: `Optional`
- **Type**: `float`
- **Logical type**: `Latitude`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The latitude of the geographical coordinate associated with one of the IP addresses in the DNS response. For more information, see Logical types.

#### Examples

- `44.475833`

### `DnsResponseIpLongitude`

- **Class**: `Optional`
- **Type**: `float`
- **Logical type**: `Longitude`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The longitude of the geographical coordinate associated with one of the IP addresses in the DNS response. For more information, see Logical types.

#### Examples

- `73.211944`

### `DnsResponseIpRegion`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Region`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The region, or state, within a country associated with one of the IP addresses in the DNS response. For more information, see Logical types.

#### Examples

- `Vermont`

### `DnsResponseName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The content of the response, as included in the record.

#### Notes

The DNS response data is inconsistent across reporting devices, is complex to parse, and has less value for source-agnostic analytics. Therefore the information model doesn't require parsing and normalization, and Microsoft Sentinel uses an auxiliary function to provide response information. For more information, see Handling DNS response.

### `DnsSessionId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS session identifier as reported by the reporting device. This value is different from TransactionIdHex, the DNS query unique ID as assigned by the DNS client.

#### Examples

- `EB4BFA28-2EAD-4EF7-BC8A-51DF4FDF5B55`

### `Domain`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DnsQuery`](../fields/dns_query.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to DnsQuery.

### `DomainCategory`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`UrlCategory`](../fields/url_category.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to UrlCategory. DomainCategory is added as an alias that's fitting to DNS.

### `Dst`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DstFQDN`](../fields/dst_fqdn.md), [`DstDvcId`](../fields/dst_dvc_id.md), [`DstHostname`](../fields/dst_hostname.md), [`DstIpAddr`](../fields/dst_ip_addr.md), [`DstMacAddr`](../fields/dst_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Target`, `Dst`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

A unique identifier of the destination device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### `DstDescription`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

A descriptive text associated with the device.

### `DstDeviceType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DeviceType](../enumerations/device_type.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The type of the device.

### `DstDomain`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The domain of the device.

### `DstDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`DstDomain`](../fields/dst_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The type of the domain.

### `DstDvcId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The ID of the device.

### `DstDvcIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DvcIdType](../enumerations/dvc_id_type.md)
- **Follows**: [`DstDvcId`](../fields/dst_dvc_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The type of the DvcId.

### `DstDvcScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The cloud platform scope the device belongs to. TargetDvcScope map to a subscription ID on Azure and to an account ID on AWS.

### `DstDvcScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The cloud platform scope ID the device belongs to. DvcScopeId maps to a subscription ID on Azure and to an account ID on AWS.

### `DstFQDN`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The device hostname, including domain information when available.

### `DstGeoCity`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `City`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The city associated with the IP address.

### `DstGeoCountry`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Country`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The country associated with the IP address.

### `DstGeoLatitude`

- **Class**: `Optional`
- **Type**: `Double`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The latitude of the geographical coordinate associated with the IP address.

### `DstGeoLongitude`

- **Class**: `Optional`
- **Type**: `Double`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The longitude of the geographical coordinate associated with the IP address.

### `DstGeoRegion`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Region`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The region within a country associated with the IP address.

### `DstHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### `DstIpAddr`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `IP Address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The IP address of the device.

### `DstMacAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `MAC address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The MAC address of the device.

### `DstOriginalRiskLevel`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The risk level associated with the source. As reported by the reporting device or enriched.

### `DstPortNumber`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The IP port on which the device communicated, if applicable.

### `DstRiskLevel`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The risk level associated with the source. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk. User the OriginalRiskLevel field for the value as reported or enriched.

### `Duration`

- **Class**: `Alias`
- **Type**: `integer`
- **Aliases**: [`DnsNetworkDuration`](../fields/dns_network_duration.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to DnsNetworkDuration

### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### `DvcAction`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

For reporting security systems, the action taken by the system, if applicable.

### `DvcDescription`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A descriptive text associated with the device.

### `DvcDomain`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The domain of the device on which the event occurred or which reported the event, depending on the schema.

### `DvcDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`DvcDomain`](../fields/dvc_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

TThe type of DvcDomain.

### `DvcFQDN`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The hostname of the device on which the event occurred or which reported the event, depending on the schema.

### `DvcHostname`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The hostname of the device on which the event occurred or which reported the event, depending on the schema.

### `DvcId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The unique ID of the device on which the event occurred or which reported the event, depending on the schema.

### `DvcIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DvcIdType](../enumerations/dvc_id_type.md)
- **Follows**: [`SrcDvcId`](../fields/src_dvc_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The type of DvcId.

### `DvcInterface`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The network interface on which data was captured. This field is typically relevant to network related activity which is captured by an intermediate or tap device.

### `DvcIpAddr`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `IP Address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The IP address of the device on which the event occurred or which reported the event, depending on the schema.

### `DvcMacAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `MAC address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The MAC address of the device on which the event occurred or which reported the event.

### `DvcOriginalAction`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The original DvcAction as provided by the reporting device.

### `DvcOs`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The operating system running on the device on which the event occurred or which reported the event.

### `DvcOsVersion`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The version of the operating system on the device on which the event occurred or which reported the event.

### `DvcScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The cloud platform scope the device belongs to. DvcScope map to a subscription ID on Azure and to an account ID on AWS.

### `DvcScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The cloud platform scope ID the device belongs to. DvcScopeId map to a subscription ID on Azure and to an account ID on AWS.

### `DvcZone`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `MAC address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The network on which the event occurred or which reported the event, depending on the schema. The zone is defined by the reporting device.

### `EventCount`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The number of events described by the record. This value is used when the source supports aggregation, and a single record might represent multiple events.

### `EventEndTime`

- **Class**: `Mandatory`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The time in which the event ended. If the source supports aggregation and the record represents multiple events, the time that the last event was generated. If not provided by the source record, this field aliases the TimeGenerated field.

### `EventMessage`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A general message or description, either included in or generated from the record.

### `EventOriginalResultDetails`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original result details provided by the source. This value is used to derive EventResultDetails, which should have only one of the values documented for each schema.

### `EventOriginalSeverity`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original severity as provided by the reporting device. This value is used to derive EventSeverity.

### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### `EventOriginalType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event type or ID, if provided by the source. For example, this field will be used to store the original Windows event ID. This value is used to derive EventType, which should have only one of the values documented for each schema.

### `EventOriginalUid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique ID of the original record, if provided by the source.

### `EventOwner`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The owner of the event, which is usually the department or subsidiary in which it was generated.

### `EventProduct`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [EventProduct](../enumerations/event_product.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The product generating the event. The value should be one of the values listed in Vendors and Products.

### `EventProductVersion`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The version of the product generating the event.

### `EventReportUrl`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `URL`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A URL provided in the event for a resource that provides more information about the event.

### `EventResult`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Success`, `Failure`, `Partial`, `NA`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

### `EventResultDetails`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TBD`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDns.yaml`

For DNS events, this field provides the DNS response code.

#### References

- [https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml)

### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [Dns](../schemas/dns.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDns.yaml`

The schema the event is normalized to. Each schema documents its schema name.

### `EventSchemaVersion`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `SchemaVersion`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The version of the schema. Each schema documents its current version.

### `EventSeverity`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Informational`, `Low`, `Medium`, `High`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The severity of the event.

### `EventStartTime`

- **Class**: `Mandatory`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The time in which the event started. If the source supports aggregation and the record represents multiple events, the time that the first event was generated. If not provided by the source record, this field aliases the TimeGenerated field.

### `EventSubType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `request`, `response`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDns.yaml`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

#### Notes

For most sources, only the responses are logged, and therefore the value is often response.

### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TBD`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDns.yaml`

For DNS records, this value would be the DNS op code.

#### References

- [https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml)

### `EventVendor`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [EventVendor](../enumerations/event_vendor.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The vendor of the product generating the event. The value should be one of the values listed in Vendors and Products.

### `Hostname`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcHostname`](../fields/src_hostname.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to SrcHostname

### `IpAddr`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `IP Address`
- **Aliases**: [`SrcIpAddr`](../fields/src_ip_addr.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to SrcIpAddr

### `NetworkProtocol`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TCP`, `UDP`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The transport protocol used by the network resolution event. The value can be UDP or TCP, and is most commonly set to UDP for DNS.

#### Examples

- `UDP`

### `NetworkProtocolVersion`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TBD`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

### `Process`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcProcessName`](../fields/src_process_name.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to SrcProcessName

### `Rule`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`RuleName`](../fields/rule_name.md), [`RuleNumber`](../fields/rule_number.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

Either the value of RuleName or the value of RuleNumber. If the value of RuleNumber is used, the type should be converted to string.

### `RuleName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The name or ID of the rule by associated with the inspection results.

### `RuleNumber`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The number of the rule associated with the inspection results.

### `SessionId`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DnsSessionId`](../fields/dns_session_id.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to DnsSessionId

### `Src`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcFQDN`](../fields/src_fqdn.md), [`SrcDvcId`](../fields/src_dvc_id.md), [`SrcHostname`](../fields/src_hostname.md), [`SrcIpAddr`](../fields/src_ip_addr.md), [`SrcMacAddr`](../fields/src_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Acting`, `Src`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

A unique identifier of the source device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### `SrcDescription`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

A descriptive text associated with the device.

### `SrcDeviceType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DeviceType](../enumerations/device_type.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the device.

### `SrcDomain`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The domain of the device.

### `SrcDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`SrcDomain`](../fields/src_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the domain.

### `SrcDvcId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The ID of the device.

### `SrcDvcIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DvcIdType](../enumerations/dvc_id_type.md)
- **Follows**: [`SrcDvcId`](../fields/src_dvc_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the DvcId.

### `SrcDvcScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The cloud platform scope the device belongs to. TargetDvcScope map to a subscription ID on Azure and to an account ID on AWS.

### `SrcDvcScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The cloud platform scope ID the device belongs to. DvcScopeId maps to a subscription ID on Azure and to an account ID on AWS.

### `SrcFQDN`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The device hostname, including domain information when available.

### `SrcGeoCity`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `City`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The city associated with the IP address.

### `SrcGeoCountry`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Country`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The country associated with the IP address.

### `SrcGeoLatitude`

- **Class**: `Optional`
- **Type**: `Double`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The latitude of the geographical coordinate associated with the IP address.

### `SrcGeoLongitude`

- **Class**: `Optional`
- **Type**: `Double`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The longitude of the geographical coordinate associated with the IP address.

### `SrcGeoRegion`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Region`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The region within a country associated with the IP address.

### `SrcHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### `SrcIpAddr`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `IP Address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The IP address of the device.

### `SrcMacAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `MAC address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The MAC address of the device.

### `SrcOriginalRiskLevel`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The risk level associated with the source. As reported by the reporting device or enriched.

### `SrcOriginalUserType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

TBD

### `SrcPortNumber`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The IP port on which the device communicated, if applicable.

### `SrcProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Source process entity`; role `Src`

The command line used to run the process.

#### Examples

- `choco.exe -v`

### `SrcProcessGuid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Source process entity`; role `Src`

A generated unique identifier (GUID) of the process. Enables identifying the process across systems.

#### Examples

- `EF3BD0BD-2B74-60C5-AF5C-010000001E00`

### `SrcProcessId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Source process entity`; role `Src`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`

### `SrcProcessName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Source process entity`; role `Src`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`

### `SrcRiskLevel`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The risk level associated with the source. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk. User the OriginalRiskLevel field for the value as reported or enriched.

### `SrcUserId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

A machine-readable, alphanumeric, unique representation of the user.

#### Examples

- `S-1-12-1-4141952679-1282074057-627758481-2916039507`

### `SrcUserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations/user_id_type.md)
- **Follows**: [`SrcUserId`](../fields/src_user_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

### `SrcUsername`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Username`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The user's username, including domain information when available.

### `SrcUsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations/username_type.md)
- **Follows**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

### `SrcUserScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The scope, such as Azure AD tenant, in which UserId and Username are defined.

### `SrcUserScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The scope ID, such as Azure AD tenant ID, in which UserId and Username are defined.

### `SrcUserSessionId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The unique ID of the sign-in session of the user.

#### Examples

- `102pTUgC3p8RIqHvzxLCHnFlg`

### `SrcUserType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserType](../enumerations/user_type.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

### `SrcUserUid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The Unix or Linux user ID of the user.

### `ThreatCategory`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The category of the threat or malware identified in activity.

### `ThreatConfidence`

- **Class**: `Optional`
- **Type**: `int`
- **Logical type**: `ConfidenceLevel`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The confidence level of the threat identified, normalized to a value between 0 and a 100.

### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `SrcIpAddr`, `DstIpAddr`, `Domain`, `DnsResponseName`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`
- Local: `ASIM/schemas/ASimDns.yaml`

The field for which a threat was identified. The value is either SrcIpAddr, DstIpAddr, Domain, or DnsResponseName..

### `ThreatFirstReportedTime`

- **Class**: `Optional`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The first time the relevant IoC was identified as a threat.

### `ThreatId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The ID of the threat or malware identified in the activity.

### `ThreatIpAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `IP Address`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

An IP address for which a threat was identified. The field ThreatField contains the name of the field ThreatFilePath represents.

### `ThreatIsActive`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

True ID the threat identified is considered an active threat.

### `ThreatLastReportedTime`

- **Class**: `Optional`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The last time the relevant IoC was identified as a threat.

### `ThreatName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The name of the threat or malware identified in the activity.

### `ThreatOriginalConfidence`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The original confidence level of the threat identified, as reported by the reporting device.

### `ThreatOriginalRiskLevel`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The risk level as reported by the reporting device.

### `ThreatRiskLevel`

- **Class**: `Optional`
- **Type**: `int`
- **Logical type**: `RiskLevel`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The risk level associated with the identified threat. The level should be a number between 0 and 100.

### `TimeGenerated`

- **Class**: `Mandatory`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

### `TransactionIdHex`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS query unique ID as assigned by the DNS client, in hexadecimal format. Note that this value is part of the DNS protocol and different from DnsSessionId, the network layer session ID, typically assigned by the reporting device.

### `Type`

- **Class**: `Mandatory`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

### `UrlCategory`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

A DNS event source may also look up the category of the requested Domains. The field is called UrlCategory to align with the Microsoft Sentinel network schema.

#### Examples

- `Educational \\ Phishing`

### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `Username`
- **Aliases**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`
