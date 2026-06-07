# Record Field Guidance

Population guidance from the Google UDM usage guide for specific record fields.
Use this page for prose guidance and the linked YAML leaves for exact
record fields.

## Metadata

Record: [records/metadata.yaml](records/metadata.yaml)

### `collected_timestamp` / `collectedTimestamp`

- **Purpose**: Encodes the GMT timestamp when the event was collected by the vendor's local collection infrastructure.
- **Encoding**: RFC 3339 timestamp.

#### Examples

- RFC 3339: '2019-09-10T20:32:31-08:00'
- timestamp: '2012-04-23T18:25:43.511Z'

### `description`

- **Purpose**: Human-readable description of the event.
- **Encoding**: Alpha-numeric string, punctuation allowed, 1024 bytes maximum
- **Example**: File c:\bar\foo.exe blocked from accessing sensitive document c:\documents\earnings.docx.

#### Examples

- File c:\bar\foo.exe blocked from accessing sensitive document c:\documents\earnings.docx.

### `event_timestamp` / `eventTimestamp`

- **Purpose**: Encodes the GMT timestamp when the event was generated.
- **Required**: Yes
- **Encoding**: RFC 3339 timestamp.

#### Examples

- RFC 3339: 2019-09-10T20:32:31-08:00
- timestamp: 2012-04-23T18:25:43.511Z

### `event_type` / `eventType`

- **Purpose**: Specifies the type of the event. If an event has multiple possible types, this value must specify the most specific type.
- **Required**: Yes.
- **Encoding**: Must be one of the predefined UDM `event_type` enumerated types.
- **Possible values**: The following lists all of the possible values for `event_type` within the UDM.

### `product_event_type` / `productEventType`

- **Purpose**: Short, descriptive, human-readable, and product-specific event name or type.
- **Encoding**: Alpha-numeric string, punctuation allowed, 64 bytes maximum.

#### Examples

- Registry Creation Event
- ProcessRollUp
- Privilege Escalation Detected
- Malware blocked

### `product_log_id` / `productLogId`

- **Purpose**: Encodes a vendor-specific event identifier to uniquely identify the event (a GUID). Users might use this identifier to search the vendor's proprietary console for the event in question.
- **Encoding**: Case-sensitive, alphanumeric string, punctuation allowed, 256 bytes maximum.
- **Example**: ABcd1234-98766

#### Examples

- ABcd1234-98766

### `product_name` / `productName`

- **Purpose**: Specifies the name of the product.
- **Encoding**: Case-sensitive, alphanumeric string, punctuation allowed, 256 bytes maximum.

#### Examples

- Falcon
- Symantec Endpoint Protection

### `product_version` / `productVersion`

- **Purpose**: Specifies the version of the product.
- **Encoding**: Alphanumeric string, periods and dashes allowed, 32 bytes maximum

#### Examples

- 1.2.3b
- 10.3:rev1

### `url_back_to_product` / `urlBackToProduct`

- **Purpose**: URL linking to a relevant website where you can view more information about this specific event (or the general event category).
- **Encoding**: Valid RFC 3986 URL with optional parameters such as port information, etc. Must have a protocol prefix before the URL (for example, https:// or http://).
- **Example**: https://newco.altostrat.com:8080/event_info?event_id=12345

#### Examples

- https://newco.altostrat.com:8080/event_info?event_id=12345

### `vendor_name` / `vendorName`

- **Purpose**: Specifies the product vendor's name.
- **Encoding**: Case-sensitive, alphanumeric string, punctuation allowed, 256 bytes maximum

#### Examples

- CrowdStrike
- Symantec

## Network

Record: [records/network.yaml](records/network.yaml)

### `application_protocol` / `applicationProtocol`

- **Purpose**: Indicates the network application protocol.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_APPLICATION_PROTOCOL`
  - `AFP`
  - `APPC`
  - `AMQP`
  - `ATOM`
  - `BEEP`
  - `BITCOIN`
  - `BIT_TORRENT`
  - `CFDP`
  - `CIP`
  - `COAP`
  - `COTP`
  - `DCERPC`
  - `DDS`
  - `DEVICE_NET`
  - `DHCP`
  - `DICOM`
  - `DNP3`
  - `DNS`
  - `E_DONKEY`
  - `ENRP`
  - `FAST_TRACK`
  - `FINGER`
  - `FREENET`
  - `FTAM`
  - `GOOSE`
  - `GOPHER`
  - `GRPC`
  - `HL7`
  - `H323`
  - `HTTP`
  - `HTTPS`
  - `IEC104`
  - `IRCP`
  - `KADEMLIA`
  - `KRB5`
  - `LDAP`
  - `LPD`
  - `MIME`
  - `MMS`
  - `MODBUS`
  - `MQTT`
  - `NETCONF`
  - `NFS`
  - `NIS`
  - `NNTP`
  - `NTCIP`
  - `NTP`
  - `OSCAR`
  - `PNRP`
  - `PTP`
  - `QUIC`
  - `RDP`
  - `RELP`
  - `RIP`
  - `RLOGIN`
  - `RPC`
  - `RTMP`
  - `RTP`
  - `RTPS`
  - `RTSP`
  - `SAP`
  - `SDP`
  - `SIP`
  - `SLP`
  - `SMB`
  - `SMTP`
  - `SNMP`
  - `SNTP`
  - `SSH`
  - `SSMS`
  - `STYX`
  - `SV`
  - `TCAP`
  - `TDS`
  - `TOR`
  - `TSP`
  - `VTP`
  - `WHOIS`
  - `WEB_DAV`
  - `X400`
  - `X500`
  - `XMPP`

### `direction`

- **Purpose**: Indicates the direction of network traffic.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_DIRECTION`
  - `INBOUND`
  - `OUTBOUND`
  - `BROADCAST`

### `email`

- **Purpose**: Specifies the email address for the sender/recipient.
- **Encoding**: String.
- **Example**: jcheng@company.example.com

#### Examples

- jcheng@company.example.com

### `ip_protocol` / `ipProtocol`

- **Purpose**: Indicates the IP protocol.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_IP_PROTOCOL`
  - `EIGRP`: Enhanced Interior Gateway Routing Protocol
  - `ESP`: Encapsulating Security Payload
  - `ETHERIP`: Ethernet-within-IP Encapsulation
  - `GRE`: Generic Routing Encapsulation
  - `ICMP`: Internet Control Message Protocol
  - `IGMP`: Internet Group Management Protocol
  - `IP6IN4`: IPv6 Encapsulation
  - `PIM`: Protocol Independent Multicast
  - `TCP`: Transmission Control Protocol
  - `UDP`: User Datagram Protocol
  - `VRRP`: Virtual Router Redundancy Protocol

### `received_bytes` / `receivedBytes`

- **Purpose**: Specifies the number of bytes received.
- **Encoding**: 64-bit unsigned integer.
- **Example**: 12,453,654,768

#### Examples

- 12,453,654,768

### `sent_bytes` / `sentBytes`

- **Purpose**: Specifies the number of bytes sent.
- **Encoding**: 64-bit unsigned integer.
- **Example**: 7,654,876

#### Examples

- 7,654,876

### `session_duration` / `sessionDuration`

- **Purpose**: Stores the network session duration, typically returned in a drop event for the session. To set the duration you can set either `network.session_duration.seconds` = 1, (type int64) or `network.session_duration.nanos` = 1 (type int32).

### `session_id` / `sessionId`

- **Purpose**: Stores the network session identifier.
- **Encoding**: String.
- **Example**: SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34

#### Examples

- SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34

## Extensions

Record: [records/extensions.yaml](records/extensions.yaml)

### `auth`

- **Purpose**: Extension to the authentication metadata.
- **Encoding**: String.

#### Examples

- Sandbox metadata (all behaviors exhibited by a file, for example, FireEye).
- Network Access Control (NAC) data.
- LDAP details about a user (for example, role, organization, etc.).

### `auth.auth_details` / `auth.authDetails`

- **Purpose**: Specify the vendor specific details for the authentication type or mechanism. Authentication providers often define types such as via_mfa or via_ad that provide useful information on the authentication type. These types can still be generalized in auth.type or auth.mechanism for usability and cross dataset rule compatibility.
- **Encoding**: String.
- **Examples**: via_mfa, via_ad.

#### Examples

- via_mfa, via_ad.

### `vulns`

- **Purpose**: Extension to the vulnerability metadata.
- **Encoding**: String.
- **Example**: Host vulnerability scan data.

#### Examples

- Host vulnerability scan data.

## Authentication

Record: [records/authentication.yaml](records/authentication.yaml)

### `auth_details` / `authDetails`

- **Purpose**: Vendor-defined authentication details.
- **Encoding**: String.

### `Authentication_Status`

- **Purpose**: Describes the authentication status of a user or specific credential.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_AUTHENTICATION_STATUS`: Default authentication status
  - `ACTIVE`: Authentication method is in an active state
  - `SUSPENDED`: Authentication method is in a suspended or disabled state
  - `DELETED`: Authentication method has been deleted
  - `NO_ACTIVE_CREDENTIALS`: Authentication method has no active credentials.

### `AuthType`

- **Purpose**: Type of system an authentication event is associated with (Google Security Operations UDM).
- **Encoding**: Enumerated type.
- **Possible values**:
  - `AUTHTYPE_UNSPECIFIED`
  - `MACHINE`: Machine authentication
  - `PHYSICAL`: Physical authentication (for example, a badge reader)
  - `SSO`
  - `TACACS`: TACACS family protocol for authentication of networked systems (for example, TACACS or TACACS+)
  - `VPN`

### `Mechanism`

- **Purpose**: Mechanism(s) used for authentication.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `MECHANISM_UNSPECIFIED`: Default authentication mechanism.
  - `BADGE_READER`
  - `BATCH`: Batch authentication.
  - `CACHED_INTERACTIVE`: Interactive authentication using cached credentials.
  - `HARDWARE_KEY`
  - `LOCAL`
  - `MECHANISM_OTHER`: Some other mechanism that is not defined here.
  - `NETWORK`: Network authentication.
  - `NETWORK_CLEAR_TEXT`: Network clear text authentication.
  - `NEW_CREDENTIALS`: Authentication with new credentials.
  - `OTP`
  - `REMOTE`: Remote authentication
  - `REMOTE_INTERACTIVE`: RDP, terminal services, Virtual Network Computing (VNC), etc.
  - `SERVICE`: Service authentication.
  - `UNLOCK`: Direct human-interactive unlock authentication.
  - `USERNAME_PASSWORD`

## Vulnerability

Record: [records/vulnerability.yaml](records/vulnerability.yaml)

### `about`

- **Purpose**: If the vulnerability is about a specific noun (for example, executable), add it here.
- **Encoding**: Noun. See Population of Noun metadata
- **Example**: executable.

#### Examples

- executable.

### `cvss_base_score` / `cvssBaseScore`

- **Purpose**: Base score for Common Vulnerability Scoring System (CVSS).
- **Encoding**: Floating-point.
- **Range**: 0.0 through 10.0
- **Example**: 8.5

#### Examples

- 8.5

### `cvss_vector` / `cvssVector`

- **Purpose**: Vector for the CVSS properties of the vulnerability. A CVSS score is composed of the following metrics: For more information, see https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator.
- **Encoding**: String.
- **Example**: AV:L/AC:H/Au:N/C:N/I:P/A:C

#### Examples

- AV:L/AC:H/Au:N/C:N/I:P/A:C

### `cvss_version` / `cvssVersion`

- **Purpose**: CVSS version for the vulnerability score or vector.
- **Encoding**: String.
- **Example**: 3.1

#### Examples

- 3.1

### `description`

- **Purpose**: Description of the vulnerability.
- **Encoding**: String.

### `first_found` / `firstFound`

- **Purpose**: Products that maintain a history of vulnerability scans should populate first_found with the time the vulnerability for this asset was first detected.
- **Encoding**: String.

### `last_found` / `lastFound`

- **Purpose**: Products that maintain a history of vulnerability scans should populate last_found with the time the vulnerability for this asset was most recently detected.
- **Encoding**: String.

### `name`

- **Purpose**: Name of the vulnerability.
- **Encoding**: String.
- **Example**: Unsupported OS Version detected.

#### Examples

- Unsupported OS Version detected.

### `scan_end_time` / `scanEndTime`

- **Purpose**: If the vulnerability was discovered during an asset scan, populate this field with the time the scan ended. Leave this field empty if the end time is not available or not applicable.
- **Encoding**: String.

### `scan_start_time` / `scanStartTime`

- **Purpose**: If the vulnerability was discovered during an asset scan, populate this field with the time the scan started. Leave this field empty if the start time is not available or not applicable.
- **Encoding**: String.

### `severity`

- **Purpose**: Severity of the vulnerability.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_SEVERITY`
  - `LOW`
  - `MEDIUM`
  - `HIGH`

### `severity_details` / `severityDetails`

- **Purpose**: Vendor specific severity details.
- **Encoding**: String.

## Ftp

Record: [records/ftp.yaml](records/ftp.yaml)

### `command`

- **Purpose**: Stores the FTP command.
- **Encoding**: String.

#### Examples

- binary
- delete
- get
- put

## Email

Record: [records/email.yaml](records/email.yaml)

### `bcc`

- **Purpose**: Stores the bcc email addresses.
- **Encoding**: String.

### `cc`

- **Purpose**: Stores the cc email addresses.
- **Encoding**: String.

### `from`

- **Purpose**: Stores the from email address.
- **Encoding**: String.

### `mail_id` / `mailId`

- **Purpose**: Stores the mail (or message) id.
- **Encoding**: String.
- **Example**: 192544.132632@email.example.com

#### Examples

- 192544.132632@email.example.com

### `reply_to` / `replyTo`

- **Purpose**: Stores the reply_to email address.
- **Encoding**: String.

### `subject`

- **Purpose**: Stores the email subject line.
- **Encoding**: String.
- **Example**: "Please read this message."

#### Examples

- "Please read this message."

### `to`

- **Purpose**: Stores the to email addresses.
- **Encoding**: String.

## Process

Record: [records/process.yaml](records/process.yaml)

### `command_line` / `commandLine`

- **Purpose**: Stores the command line string for the process.
- **Encoding**: String.
- **Example**: `c:\windows\system32\net.exe` group.

#### Examples

- `c:\windows\system32\net.exe` group.

### `file`

- **Purpose**: Stores the filename of the file in use by the process.
- **Encoding**: String.
- **Example**: report.xls

#### Examples

- report.xls

### `parent_process` / `parentProcess`

- **Purpose**: Stores the details of the parent process.
- **Encoding**: Noun (Process)

### `parent_process.product_specific_process_id` / `parentProcess.productSpecificProcessId`

- **Purpose**: Stores the product specific process ID for the parent process.
- **Encoding**: String.
- **Examples**: `MySQL:78778` or `CS:90512`

#### Examples

- `MySQL:78778` or `CS:90512`

### `pid`

- **Purpose**: Stores the process ID.
- **Encoding**: String.

#### Examples

- 308
- 2002

### `product_specific_process_id` / `productSpecificProcessId`

- **Purpose**: Stores the product specific process ID.
- **Encoding**: String.
- **Examples**: `MySQL:78778` or `CS:90512`

#### Examples

- `MySQL:78778` or `CS:90512`

## SecurityResult

Record: [records/security_result.yaml](records/security_result.yaml)

### `about`

- **Purpose**: Provide a description of the security result.
- **Encoding**: Noun.

### `action`

- **Purpose**: Specify a security action.
- **Encoding**: Enumerated type.
- **Possible values**: Google SecOps UDM defines the following security actions:
  - `ALLOW`
  - `ALLOW_WITH_MODIFICATION`: File or email was disinfected or rewritten and still forwarded.
  - `BLOCK`
  - `QUARANTINE`: Store for later analysis (does not mean block).
  - `UNKNOWN_ACTION`

### `action_details` / `actionDetails`

- **Purpose**: Vendor-provided details of the action taken as a result of the security incident. Security actions often best translate into the more general `Security_Result.action` UDM field. However, you might need to write rules for the exact vendor-provided description of the action.
- **Encoding**: String.
- **Examples**: drop, block, decrypt, encrypt.

#### Examples

- drop, block, decrypt, encrypt.

### `category`

- **Purpose**: Specify a security category.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following security categories:
  - `ACL_VIOLATION`: Unauthorized access attempted, including attempted access to files, web services, processes, web objects, etc.
  - `AUTH_VIOLATION`: Authentication failed, such as a bad password or bad 2-factor authentication.
  - `DATA_AT_REST`: DLP: sensor data found at rest in a scan.
  - `DATA_DESTRUCTION`: Attempt to destroy/delete data.
  - `DATA_EXFILTRATION`: DLP: sensor data transmission, copy to thumb drive.
  - `EXPLOIT`: Attempted overflows, bad protocol encodings, ROP, SQL injection, etc, both network and host-based.
  - `MAIL_PHISHING`: Phishing email, chat messages, etc.
  - `MAIL_SPAM`: Spam email, message, etc.
  - `MAIL_SPOOFING`: Spoofed source email address, etc.
  - `NETWORK_CATEGORIZED_CONTENT`
  - `NETWORK_COMMAND_AND_CONTROL`: If the command and control channel is known.
  - `NETWORK_DENIAL_OF_SERVICE`
  - `NETWORK_MALICIOUS`: Command and control, network exploit, suspicious activity, potential reverse tunnel, etc.
  - `NETWORK_SUSPICIOUS`: Non-security related, for example, the URL is linked to gambling, etc.
  - `NETWORK_RECON`: Port scan detected by an IDS, probing by a web application.
  - `POLICY_VIOLATION`: Security policy violation, including firewall, proxy, and HIPS rule violations or NAC block actions.
  - `SOFTWARE_MALICIOUS`: Malware, spyware, rootkits, etc.
  - `SOFTWARE_PUA`: Potentially unwanted app, such as adware, etc.
  - `SOFTWARE_SUSPICIOUS`
  - `UNKNOWN_CATEGORY`

### `confidence`

- **Purpose**: Specify a confidence with regards to a security event as estimated by the product.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following product confidence categories:
  - `UNKNOWN_CONFIDENCE`
  - `LOW_CONFIDENCE`
  - `MEDIUM_CONFIDENCE`
  - `HIGH_CONFIDENCE`

### `confidence_details` / `confidenceDetails`

- **Purpose**: Additional detail with regards to the confidence of a security event as estimated by the product vendor.
- **Encoding**: String.

### `priority`

- **Purpose**: Specify a priority with regards to a security event as estimated by the product vendor.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following product priority categories:
  - `UNKNOWN_PRIORITY`
  - `LOW_PRIORITY`
  - `MEDIUM_PRIORITY`
  - `HIGH_PRIORITY`

### `priority_details` / `priorityDetails`

- **Purpose**: Vendor-specific information about the security result priority.
- **Encoding**: String.

### `rule_id` / `ruleId`

- **Purpose**: Identifier for the security rule.
- **Encoding**: String.

#### Examples

- 08123
- 5d2b44d0-5ef6-40f5-a704-47d61d3babbe

### `rule_name` / `ruleName`

- **Purpose**: Name of the security rule.
- **Encoding**: String.
- **Example**: BlockInboundToOracle.

#### Examples

- BlockInboundToOracle.

### `severity`

- **Purpose**: Severity of a security event as estimated by the product vendor using values defined by the Google SecOps UDM.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following product severities:
  - `UNKNOWN_SEVERITY`: Non-malicious
  - `INFORMATIONAL`: Non-malicious
  - `ERROR`: Non-malicious
  - `LOW`: Malicious
  - `MEDIUM`: Malicious
  - `HIGH`: Malicious

### `severity_details` / `severityDetails`

- **Purpose**: Severity for a security event as estimated by the product vendor.
- **Encoding**: String.

### `threat_name` / `threatName`

- **Purpose**: Name of the security threat.
- **Encoding**: String.

#### Examples

- W32/File-A
- Slammer

### `url_back_to_product` / `urlBackToProduct`

- **Purpose**: URL to direct you to the source product console for this security event.
- **Encoding**: String.

## File

Record: [records/file.yaml](records/file.yaml)

### `file_metadata` / `fileMetadata`

- **Purpose**: Metadata associated with the file.
- **Encoding**: String.

#### Examples

- Author
- Revision number
- Version number
- Date last saved

### `full_path` / `fullPath`

- **Purpose**: Full path identifying the location of the file on the system.
- **Encoding**: String.
- **Example**: \Program Files\Custom Utilities\`Test.exe`

#### Examples

- \Program Files\Custom Utilities\Test.exe

### `md5`

- **Purpose**: MD5 hash value for the file.
- **Encoding**: String, lower-case hexadecimal.
- **Example**: 35bf623e7db9bf0d68d0dda764fd9e8c

#### Examples

- 35bf623e7db9bf0d68d0dda764fd9e8c

### `mime_type` / `mimeType`

- **Purpose**: Multipurpose Internet Mail Extensions (MIME) type for the file.
- **Encoding**: String.

#### Examples

- PE
- PDF
- powershell script

### `sha1`

- **Purpose**: SHA-1 hash value for the file.
- **Encoding**: String, lower-case hexadecimal.
- **Example**: eb3520d53b45815912f2391b713011453ed8abcf

#### Examples

- eb3520d53b45815912f2391b713011453ed8abcf

### `sha256`

- **Purpose**: SHA-256 hash value for the file.
- **Encoding**: String, lower-case hexadecimal.
- **Example**: d7173c568b8985e61b4050f81b3fd8e75bc922d2a0843d7079c81ca4b6e36417

#### Examples

- d7173c568b8985e61b4050f81b3fd8e75bc922d2a0843d7079c81ca4b6e36417

### `size`

- **Purpose**: Size of the file.
- **Encoding**: 64-bit unsigned integer.
- **Example**: 342135

#### Examples

- 342135

## Dns

Record: [records/dns.yaml](records/dns.yaml)

### `additional`

- **Purpose**: Stores the additional domain name servers that can be used to verify the answer to the domain. See Population of DNS Resource Record metadata.

### `answers`

- **Purpose**: Stores the answer to the domain name query. See Population of DNS Resource Record metadata.

### `authoritative`

- **Purpose**: Set to true for authoritative DNS servers.
- **Encoding**: Boolean.

### `authority`

- **Purpose**: Stores the domain name servers that verified the answer to the domain name query. See Population of DNS Resource Record metadata.

### `id`

- **Purpose**: Stores the DNS query identifier.
- **Encoding**: 32-bit integer.

### `opcode`

- **Purpose**: Stores the DNS OpCode used to specify the type of DNS query (standard, inverse, server status, etc.).
- **Encoding**: 32-bit integer.

### `questions`

- **Purpose**: Stores the domain protocol message questions. See Population of DNS Question metadata.

### `recursion_available` / `recursionAvailable`

- **Purpose**: Set to true if a recursive DNS lookup is available.
- **Encoding**: Boolean.

### `recursion_desired` / `recursionDesired`

- **Purpose**: Set to true if a recursive DNS lookup is requested.
- **Encoding**: Boolean.

### `response`

- **Purpose**: Set to true if the event is a DNS response.
- **Encoding**: Boolean.

### `response_code` / `responseCode`

- **Purpose**: Stores the DNS response code as defined by RFC 1035, Domain Names - Implementation and Specification.
- **Encoding**: 32-bit integer.

### `truncated`

- **Purpose**: Set to true if this is a truncated DNS response.
- **Encoding**: Boolean.

## Question

Record: [records/dns_question.yaml](records/dns_question.yaml)

### `class`

- **Purpose**: Stores the code specifying the class of the query.
- **Encoding**: 32-bit integer.

### `name`

- **Purpose**: Stores the domain name.
- **Encoding**: String.

### `type`

- **Purpose**: Stores the code specifying the type of the query.
- **Encoding**: 32-bit integer.

## ResourceRecord

Record: [records/dns_resource_record.yaml](records/dns_resource_record.yaml)

### `binary_data` / `binaryData`

- **Purpose**: Stores the raw bytes of any non-UTF8 strings that might be included as part of a DNS response. This field must only be used if the response data returned by the DNS server contains non-UTF8 data. Otherwise, place the DNS response in the data field below. This type of information must be stored here rather than in `ResourceRecord.data`.
- **Encoding**: Bytes. Note: This field is not specified in RFC 1035 (unlike the other DNS resource record fields), but has been defined by Google SecOps for the UDM.

### `class`

- **Purpose**: Stores the code specifying the class of the resource record.
- **Encoding**: 32-bit integer.

### `data`

- **Purpose**: Stores the payload or response to the DNS question for all responses encoded in UTF-8 format. For example, the data field could return the IP address of the machine that the domain name refers to. If the resource record is for a different type or class, it might contain another domain name (when one domain name is redirected to another domain name). Data must be stored just as it is in the DNS response.
- **Encoding**: String.

### `name`

- **Purpose**: Stores the name of the owner of the resource record.
- **Encoding**: String.

### `ttl`

- **Purpose**: Stores the time interval for which the resource record can be cached before the source of the information should again be queried.
- **Encoding**: 32-bit integer.

### `type`

- **Purpose**: Stores the code specifying the type of the resource record.
- **Encoding**: 32-bit integer.

## Dhcp

Record: [records/dhcp.yaml](records/dhcp.yaml)

### `chaddr`

- **Purpose**: Hardware address for the client.
- **Encoding**: MAC address.

### `ciaddr`

- **Purpose**: IP address for the client.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `client_hostname` / `clientHostname`

- **Purpose**: Hostname for the client. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: String.

### `client_identifier` / `clientIdentifier`

- **Purpose**: Client identifier. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Bytes.

### `file`

- **Purpose**: Filename for the boot image.
- **Encoding**: String.

### `flags`

- **Purpose**: Value for the DHCP flags field.
- **Encoding**: 32-bit unsigned integer.

### `giaddr`

- **Purpose**: IP address for the relay agent.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `hlen`

- **Purpose**: Hardware address length.
- **Encoding**: 32-bit unsigned integer.

### `hops`

- **Purpose**: DHCP hop count.
- **Encoding**: 32-bit unsigned integer.

### `htype`

- **Purpose**: Hardware address type.
- **Encoding**: 32-bit unsigned integer.

### `lease_time_seconds` / `leaseTimeSeconds`

- **Purpose**: Client-requested lease time for an IP address in seconds. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: 32-bit unsigned integer.

### `opcode`

- **Purpose**: BOOTP op code (see section 3 of RFC 951).
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_OPCODE`
  - `BOOTREQUEST`
  - `BOOTREPLY`

### `requested_address` / `requestedAddress`

- **Purpose**: Client identifier. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `seconds`

- **Purpose**: Seconds elapsed since the client began the address acquisition/renewal process.
- **Encoding**: 32-bit unsigned integer.

### `siaddr`

- **Purpose**: IP address for the next bootstrap server.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `sname`

- **Purpose**: Name of the server that the client has requested to boot from.
- **Encoding**: String.

### `transaction_id` / `transactionId`

- **Purpose**: Client transaction ID.
- **Encoding**: 32-bit unsigned integer.

### `type`

- **Purpose**: DHCP message type. See RFC 1533 for more information.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_MESSAGE_TYPE`
  - `DISCOVER`
  - `OFFER`
  - `REQUEST`
  - `DECLINE`
  - `ACK`
  - `NAK`
  - `RELEASE`
  - `INFORM`
  - `WIN_DELECTED`
  - `WIN_EXPIRED`

### `yiaddr`

- **Purpose**: Your IP address.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

## Option

Record: [records/dhcp_option.yaml](records/dhcp_option.yaml)

### `code`

- **Purpose**: Stores the DHCP option code. See RFC 1533, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Unsigned 32-bit integer.

### `data`

- **Purpose**: Stores the DHCP option data. See RFC 1533, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Bytes.

## Http

Record: [records/http.yaml](records/http.yaml)

### `method`

- **Purpose**: Stores the HTTP request method.
- **Encoding**: String.

#### Examples

- GET
- HEAD
- POST

### `referral_url` / `referralUrl`

- **Purpose**: Stores the URL for the HTTP referer.
- **Encoding**: Valid RFC 3986 URL.
- **Example**: https://www.altostrat.com

#### Examples

- https://www.altostrat.com

### `response_code` / `responseCode`

- **Purpose**: Stores the HTTP response status code, which indicates whether a specific HTTP request has been successfully completed.
- **Encoding**: 32-bit integer.

#### Examples

- 400
- 404

### `user_agent` / `userAgent`

- **Purpose**: Stores the User-Agent request header that includes the application type, operating system, software vendor or software version of the requesting software user agent.
- **Encoding**: String.

#### Examples

- Mozilla/5.0 (X11; Linux x86_64)
- AppleWebKit/534.26 (KHTML, like Gecko)
- Chrome/41.0.2217.0
- Safari/527.33

## User

Record: [records/user.yaml](records/user.yaml)

### `email_addresses` / `emailAddresses`

- **Purpose**: Stores the email addresses for the user.
- **Encoding**: Repeated String.
- **Example**: johnlocke@company.example.com

#### Examples

- johnlocke@company.example.com

### `employee_id` / `employeeId`

- **Purpose**: Stores the human resources employee ID for the user.
- **Encoding**: String.
- **Example**: 11223344.

#### Examples

- 11223344.

### `first_name` / `firstName`

- **Purpose**: Stores the first name for the user.
- **Encoding**: String.
- **Example**: John.

#### Examples

- John.

### `group_identifiers` / `groupIdentifiers`

- **Purpose**: Stores the group ID(s) (a GUID, LDAP OID, or similar) associated with a user.
- **Encoding**: Repeated String.
- **Example**: admin-users.

#### Examples

- admin-users.

### `last_name` / `lastName`

- **Purpose**: Stores the last name for the user.
- **Encoding**: String.
- **Example**: Locke.

#### Examples

- Locke.

### `middle_name` / `middleName`

- **Purpose**: Stores the middle name for the user.
- **Encoding**: String.
- **Example**: Anthony.

#### Examples

- Anthony.

### `phone_numbers` / `phoneNumbers`

- **Purpose**: Stores the phone numbers for the user.
- **Encoding**: Repeated String.
- **Example**: 800-555-0101

#### Examples

- 800-555-0101

### `title`

- **Purpose**: Stores the job title for the user.
- **Encoding**: String.
- **Example**: Customer Relationship Manager.

#### Examples

- Customer Relationship Manager.

### `user_display_name` / `userDisplayName`

- **Purpose**: Stores the display name for the user.
- **Encoding**: String.
- **Example**: John Locke.

#### Examples

- John Locke.

### `userid`

- **Purpose**: Stores the user ID.
- **Encoding**: String.
- **Example**: jlocke.

#### Examples

- jlocke.

### `windows_sid` / `windowsSid`

- **Purpose**: Stores the Microsoft Windows security identifier (SID) associated with a user.
- **Encoding**: String.
- **Example**: S-1-5-21-1180649209-123456789-3582944384-1064

#### Examples

- S-1-5-21-1180649209-123456789-3582944384-1064

## Group

Record: [records/group.yaml](records/group.yaml)

### `creation_time` / `creationTime`

- **Purpose**: Group creation time.
- **Encoding**: RFC 3339 timestamp.

### `email_addresses` / `emailAddresses`

- **Purpose**: Group contact information.
- **Encoding**: Email.

### `group_display_name` / `groupDisplayName`

- **Purpose**: Group display name.
- **Encoding**: String.

#### Examples

- Finance
- HR
- Marketing

### `product_object_id` / `productObjectId`

- **Purpose**: Globally unique user object identifier for the product, such as an LDAP object identifier.
- **Encoding**: String.

### `windows_sid` / `windowsSid`

- **Purpose**: Microsoft Windows Security Identifier (SID) group attribute field.
- **Encoding**: String.

## Registry

Record: [records/registry.yaml](records/registry.yaml)

### `registry_key` / `registryKey`

- **Purpose**: Stores the registry key associated with an application or system component.
- **Encoding**: String.
- **Example**: HKEY_LOCAL_MACHINE/SYSTEM/DriverDatabase

#### Examples

- HKEY_LOCAL_MACHINE/SYSTEM/DriverDatabase

### `registry_value_data` / `registryValueData`

- **Purpose**: Stores the data associated with a registry value.
- **Encoding**: String.
- **Example**: %USERPROFILE%\Local Settings\Temp

#### Examples

- %USERPROFILE%\Local Settings\Temp

### `registry_value_name` / `registryValueName`

- **Purpose**: Stores the name of the registry value associated with an application or system component.
- **Encoding**: String.
- **Example**: TEMP

#### Examples

- TEMP

## Location

Record: [records/location.yaml](records/location.yaml)

### `city`

- **Purpose**: Stores the name of the city.
- **Encoding**: String.

#### Examples

- Sunnyvale
- Chicago
- Malaga

### `country_or_region` / `countryOrRegion`

- **Purpose**: Stores the name of the country or region of the world.
- **Encoding**: String.

#### Examples

- United States
- United Kingdom
- Spain

### `name`

- **Purpose**: Stores the name specific to the enterprise, such as a building or campus.
- **Encoding**: String.

#### Examples

- Campus 7B
- Building A2

### `state`

- **Purpose**: Stores the name of the state, province, or territory.
- **Encoding**: String.

#### Examples

- California
- Illinois
- Ontario

## Noun

Record: [records/noun.yaml](records/noun.yaml)

### `administrative_domain` / `administrativeDomain`

- **Purpose**: Domain that the device belongs to (for example, the Windows domain).
- **Encoding**: Valid domain name string (128 characters maximum).
- **Example**: corp.altostrat.com

#### Examples

- corp.altostrat.com

### `asset_id` / `assetId`

- **Purpose**: Vendor-specific unique device identifier (for example, a GUID that is generated when installing endpoint security software on a new device that is used to track that unique device over time).
- **Encoding**: (VendorName or VendorAbbreviation):ID where the VendorName or VendorAbbreviation is a case insensitive vendor name like `Carbon Black` or `CB` and ID is a vendor-specific customer identifier that is globally unique within their customer's environment (for example, a GUID or unique value identifying a unique device). VendorName is alphanumeric and no more than 32 characters long. ID can be a maximum of 128 characters in length and can include alphanumeric characters, dashes, and periods.
- **Example**: `CrowdStrike:0bce4259-4ada-48f3-a904-9a526b01311f`
- **Example**: `CS:0bce4259-4ada-48f3-a904-9a526b01311f`

#### Examples

- `CrowdStrike:0bce4259-4ada-48f3-a904-9a526b01311f`
- `CS:0bce4259-4ada-48f3-a904-9a526b01311f`

### `email`

- **Purpose**: Email address
- **Encoding**: Standard email address format.
- **Example**: johns@test.altostrat.com

#### Examples

- johns@test.altostrat.com

### `file`

- **Purpose**: Detailed file metadata.
- **Type**: Object
- **Note**: See Population of File metadata.

### `hostname`

- **Purpose**: Client hostname or domain name field. Do not include if a URL is present.
- **Encoding**: Valid RFC 1123 hostname.

#### Examples

- userwin10
- www.altostrat.com

### `ip`

- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

#### Examples

- 192.168.1.2
- 2001:db8:1:3::1

### `mac`

- **Purpose**: One or more MAC addresses associated with a device.
- **Encoding**: Valid MAC address (EUI-48) in ASCII.
- **Repeatability**: Vendor might provide all of the associated MAC addresses for the device at the time of the event.

#### Examples

- fedc:ba98:7654:3210:fedc:ba98:7654:3210
- 1080:0:0:0:8:800:200c:417a
- 00:a0:0:0:c9:14:c8:29

### `platform`

- **Purpose**: Platform operating system.
- **Encoding**: Enum
- **Possible values**:
  - `LINUX`
  - `MAC`
  - `WINDOWS`
  - `UNKNOWN_PLATFORM`

### `platform_patch_level` / `platformPatchLevel`

- **Purpose**: Platform operating system patch level.
- **Encoding**: Alphanumeric string with punctuation, 64 characters maximum.
- **Example**: Build 17134.48

#### Examples

- Build 17134.48

### `platform_version` / `platformVersion`

- **Purpose**: Platform operating system version.
- **Encoding**: Alphanumeric string with punctuation, 64 characters maximum.
- **Example**: Microsoft Windows 10 version 1803

#### Examples

- Microsoft Windows 10 version 1803

### `port`

- **Purpose**: Source or destination network port number when a specific network connection is described within an event.
- **Encoding**: Valid TCP/IP port number from 1 through 65,535.
- **Examples**: Note: If a port number is specified, there must be one and only one IP address specified in the same Noun.

#### Examples

- 80
- 443

### `process`

- **Purpose**: Detailed process metadata.
- **Type**: Object
- **Note**: See Population of Process metadata.

### `registry`

- **Purpose**: Detailed registry metadata.
- **Type**: Object
- **Note**: See Population of Registry metadata

### `url`

- **Purpose**: Standard URL
- **Encoding**: URL (RFC 3986). Must have a valid protocol prefix (for example, https:// or ftp://). Must include the full domain and path. Might include the URL's parameters.
- **Example**: https://foo.altostrat.com/bletch?a=b;c=d

#### Examples

- https://foo.altostrat.com/bletch?a=b;c=d

### `user`

- **Purpose**: Detailed user metadata.
- **Type**: Object
- **Note**: See Population of User metadata.

## Other Guidance

### `idm.is_alert`

- **Purpose**: Identifies whether the event is an alert.
- **Encoding**: Boolean.

### `idm.is_significant`

- **Purpose**: Specifies whether to display the alert in Enterprise Insights.
- **Encoding**: Boolean.
