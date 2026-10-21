# Observable (observable)

The observable object is a pivot element that contains related information found in many places in the event.

- **Extends**: [Object (object)](object.md)

## Attributes

### `name`

- **Type**: `string_t`
- **Requirement**: required

The full name of the observable attribute. The `name` is a pointer/reference to an attribute within the event data. For example: `file.name`.

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
- `1`: `Hostname` - Observable by Dictionary Type. Unique name assigned to a device connected to a computer network. A domain name in general is an Internet address that can be resolved through the Domain Name System (DNS). For example: `r2-d2.example.com`.
- `2`: `IP Address` - Observable by Dictionary Type. Internet Protocol address (IP address), in either IPv4 or IPv6 format. For example, `192.168.200.24` or `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.
- `3`: `MAC Address` - Observable by Dictionary Type. Media Access Control (MAC) address. For example: `18:36:F3:98:4F:9A`.
- `4`: `User Name` - Observable by Dictionary Type. User name. For example: `john_doe`.
- `5`: `Email Address` - Observable by Dictionary Type. Email address. For example: `john_doe@example.com`.
- `6`: `URL String` - Observable by Dictionary Type. Uniform Resource Locator (URL) string. For example: `http://www.example.com/download/trouble.exe`.
- `7`: `File Name` - Observable by Dictionary Type. File name. For example: `text-file.txt`.
- `8`: `Hash` - Observable by Dictionary Type. Hash. A unique value that corresponds to the content of the file, image, ja3_hash or hassh found in the schema. For example MD5: `3172ac7e2b55cbb81f04a6e65855a628`.
- `9`: `Process Name` - Observable by Dictionary Type. Process name. For example: `Notepad`.
- `10`: `Resource UID` - Observable by Dictionary Type. Resource unique identifier. For example, S3 Bucket name or EC2 Instance ID.
- `20`: `Endpoint` - Observable by Object. The Endpoint object describes a physical or virtual device that connects to and exchanges information with a computer network. Some examples of endpoints are mobile devices, desktop computers, virtual machines, embedded devices, and servers. Internet-of-Things devices—like cameras, lighting, refrigerators, security systems, smart speakers, and thermostats—are also endpoints.
- `21`: `User` - Observable by Object. The User object describes the characteristics of a user/person or a security principal. Defined by D3FEND [d3f:UserAccount](https://d3fend.mitre.org/dao/artifact/d3f:UserAccount/).
- `22`: `Email` - Observable by Object. The Email object describes the email metadata such as sender, recipients, and direction. Defined by D3FEND [d3f:Email](https://d3fend.mitre.org/dao/artifact/d3f:Email/).
- `23`: `Uniform Resource Locator` - Observable by Object. The Uniform Resource Locator(URL) object describes the characteristics of a URL. Defined in [RFC 1738](https://datatracker.ietf.org/doc/html/rfc1738) and by D3FEND [d3f:URL](https://d3fend.mitre.org/dao/artifact/d3f:URL/).
- `24`: `File` - Observable by Object. The File object represents the metadata associated with a file stored in a computer system. It encompasses information about the file itself, including its attributes, properties, and organizational details. Defined by D3FEND [d3f:File](https://next.d3fend.mitre.org/dao/artifact/d3f:File/).
- `25`: `Process` - Observable by Object. The Process object describes a running instance of a launched program. Defined by D3FEND [d3f:Process](https://d3fend.mitre.org/dao/artifact/d3f:Process/).
- `26`: `Geo Location` - Observable by Object. The Geo Location object describes a geographical location, usually associated with an IP address. Defined by D3FEND [d3f:PhysicalLocation](https://d3fend.mitre.org/dao/artifact/d3f:PhysicalLocation/).
- `27`: `Container` - Observable by Object. The Container object describes an instance of a specific container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.
- `30`: `Fingerprint` - Observable by Object. The Fingerprint object provides detailed information about a digital fingerprint, which is a compact representation of data used to identify a longer piece of information, such as a public key or file content. It contains the algorithm and value of the fingerprint, enabling efficient and reliable identification of the associated data.
- `99`: `Other` - The observable data type is not mapped. See the `type` attribute, which may contain data source specific value.

The observable value type identifier.

### `value`

- **Type**: `string_t`
- **Requirement**: optional

The value associated with the observable attribute. The meaning of the value depends on the observable type.
If the `name` refers to a scalar attribute, then the `value` is the value of the attribute.
If the `name` refers to an object attribute, then the `value` is not populated.
