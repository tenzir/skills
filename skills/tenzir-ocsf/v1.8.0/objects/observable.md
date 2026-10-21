# Observable (observable)

The observable object is a pivot element that contains related information found in many places in the event.

- **Extends**: [Object (object)](object.md)

## Attributes

### `event_uid`

- **Type**: `string_t`
- **Requirement**: optional

The unique identifier (`metadata.uid`) of the source OCSF event from which this observable was extracted. This field enables linking observables back to their originating event data when observables are stored in a separate location or system.

### `name`

- **Type**: `string_t`
- **Requirement**: recommended

The full name of the observable attribute. The `name` is a pointer/reference to an attribute within the OCSF event data. For example: `file.name`. Array attributes may be represented in one of three ways. For example: `resources.uid`, `resources[].uid`, `resources[0].uid`.

### `reputation`

- **Type**: [`reputation`](reputation.md)
- **Requirement**: optional

Contains the original and normalized reputation scores.

### `type`

- **Type**: `string_t`
- **Requirement**: optional

The observable value type name.

### `type_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Sibling**: `type`

#### Enum values

- `0`: `Unknown` - Unknown observable data type.
- `1`: `Hostname` - Observable by Dictionary Type. Unique name assigned to a device connected to a computer network. It may be a fully qualified domain name (FQDN). For example: `r2-d2.example.com.`, `mx.example.com`
- `2`: `IP Address` - Observable by Dictionary Type. Internet Protocol address (IP address), in either IPv4 or IPv6 format. For example: `192.168.200.24`, `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.
- `3`: `MAC Address` - Observable by Dictionary Type. Media Access Control (MAC) address. For example: `18:36:F3:98:4F:9A`.
- `4`: `User Name` - Observable by Dictionary Type. User name. For example: `john_doe`.
- `5`: `Email Address` - Observable by Dictionary Type. Email address. For example: `john_doe@example.com`.
- `6`: `URL String` - Observable by Dictionary Type. Uniform Resource Locator (URL) string. For example: `http://www.example.com/download/trouble.exe`.
- `7`: `File Name` - Observable by Dictionary Type. File name. For example: `text-file.txt`.
- `8`: `Hash` - Observable by Dictionary Type. Fingerprint. A value, in any format, that maps an arbitrarily large data item to a much shorter string that uniquely identifies the original data. Examples include cryptographic hashing of a file, code signing, and Network Protocol Fingerprinting (NPF). Note about name. The type name `file_hast_t` and the caption "Hash" are used for legacy reasons. This type has been generalized from a file hash to a general fingerprint. The existing type name and caption were retained for backwards compatibility.
- `9`: `Process Name` - Observable by Dictionary Type. Process name. For example: `Notepad`.
- `10`: `Resource UID` - Observable by Dictionary Type. Resource unique identifier. For example, S3 Bucket name or EC2 Instance ID.
- `11`: `Port` - Observable by Dictionary Type. The TCP/UDP port number. For example: `80`, `22`.
- `12`: `Subnet` - Observable by Dictionary Type. The subnet represented in a CIDR notation, using the format network_address/prefix_length. The network_address can be in either IPv4 or IPv6 format. The prefix length indicates the number of bits used for the network portion, and the remaining bits are available for host addresses within that subnet. For example: `192.168.1.0/24`, `2001:0db8:85a3:0000::/64`
- `13`: `Command Line` - Observable by Dictionary Attribute. The full command line used to launch an application, service, process, or job. For example: `ssh user@10.0.0.10`. If the command line is unavailable or missing, the empty string `''` is to be used.
- `14`: `Country` - Observable by Dictionary Attribute. The ISO 3166-1 Alpha-2 country code. Note: The two letter country code should be capitalized. For example: `US` or `CA`.
- `15`: `Process ID` - Observable by Dictionary Attribute. The process identifier, as reported by the operating system. Process ID (PID) is a number used by the operating system to uniquely identify an active process.
- `16`: `HTTP User-Agent` - Observable by Dictionary Attribute. The request header that identifies the operating system and web browser.
- `17`: `CWE Object: uid` - Observable by Object-Specific Attribute. Object-specific attribute "uid" for the CWE Object.
- `18`: `CVE Object: uid` - Observable by Object-Specific Attribute. Object-specific attribute "uid" for the CVE Object.
- `19`: `User Credential ID` - Observable by Dictionary Attribute. The unique identifier of the user's credential. For example, AWS Access Key ID.
- `20`: `Endpoint` - Observable by Object. The Endpoint object describes a physical or virtual device that connects to and exchanges information with a computer network. Some examples of endpoints are mobile devices, desktop computers, virtual machines, embedded devices, and servers. Internet-of-Things devices—like cameras, lighting, refrigerators, security systems, smart speakers, and thermostats—are also endpoints.
- `21`: `User` - Observable by Object. The User object describes the characteristics of a user/person or a security principal.
- `22`: `Email` - Observable by Object. The Email object describes the email metadata such as sender, recipients, and direction, and can include embedded URLs and files.
- `23`: `Uniform Resource Locator` - Observable by Object. The Uniform Resource Locator (URL) object describes the characteristics of a URL.
- `24`: `File` - Observable by Object. The File object represents the metadata associated with a file stored in a computer system. It encompasses information about the file itself, including its attributes, properties, and organizational details.
- `25`: `Process` - Observable by Object. The Process object describes a running instance of a launched program.
- `26`: `Geo Location` - Observable by Object. The Geo Location object describes a geographical location, usually associated with an IP address.
- `27`: `Container` - Observable by Object. The Container object describes an instance of a specific container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.
- `30`: `Fingerprint` - Observable by Object. The Fingerprint object provides detailed information about a fingerprint, which is a compact representation of data used to identify a longer piece of information, such as a public key, file content, or application implementation. It contains the algorithm or scheme and value of the fingerprint, enabling efficient and reliable identification of the associated data.
- `31`: `User Object: uid` - Observable by Object-Specific Attribute. Object-specific attribute "uid" for the User Object.
- `32`: `Group Object: name` - Observable by Object-Specific Attribute. Object-specific attribute "name" for the Group Object.
- `33`: `Group Object: uid` - Observable by Object-Specific Attribute. Object-specific attribute "uid" for the Group Object.
- `34`: `Account Object: name` - Observable by Object-Specific Attribute. Object-specific attribute "name" for the Account Object.
- `35`: `Account Object: uid` - Observable by Object-Specific Attribute. Object-specific attribute "uid" for the Account Object.
- `36`: `Script Content` - Observable by Dictionary Attribute. The script content, normalized to UTF-8 encoding irrespective of its original encoding. When emitting this attribute, it may be appropriate to truncate large scripts. When consuming this attribute, large scripts should be anticipated.
- `37`: `Serial Number` - Observable by Dictionary Attribute. The serial number that pertains to the object. See specific usage.
- `38`: `Resource Details Object: name` - Observable by Object-Specific Attribute. Object-specific attribute "name" for the Resource Details Object.
- `39`: `Process Entity Object: uid` - Observable by Object-Specific Attribute. Object-specific attribute "uid" for the Process Entity Object.
- `40`: `Email Object: subject` - Observable by Object-Specific Attribute. Object-specific attribute "subject" for the Email Object.
- `41`: `Email Object: uid` - Observable by Object-Specific Attribute. Object-specific attribute "uid" for the Email Object.
- `42`: `Message UID` - Observable by Dictionary Attribute. The email header Message-ID value, as defined by RFC 5322.
- `44`: `Advisory Object: uid` - Observable by Object-Specific Attribute. Object-specific attribute "uid" for the Advisory Object.
- `45`: `File Path` - Observable by Dictionary Type. The full path to the file. For example: For example: `c:\windows\system32\svchost.exe`.
- `47`: `Device Object: uid` - Observable by Object-Specific Attribute. Object-specific attribute "uid" for the Device Object.
- `48`: `Network Endpoint Object: uid` - Observable by Object-Specific Attribute. Object-specific attribute "uid" for the Network Endpoint Object.
- `99`: `Other` - The observable data type is not mapped. See the `type` attribute, which may contain data source specific value.

The observable value type identifier.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: optional
- **Sibling**: `type_name`

The OCSF event type UID (`type_uid`) of the source event that this observable was extracted from. This field enables filtering and categorizing observables by their originating event type. For example: `300101` for Network Activity (class_uid 3001) with activity_id 1.

### `value`

- **Type**: `string_t`
- **Requirement**: optional

The value associated with the observable attribute. The meaning of the value depends on the observable type.
If the `name` refers to a scalar attribute, then the `value` is the value of the attribute.
If the `name` refers to an object attribute, then the `value` is not populated.
