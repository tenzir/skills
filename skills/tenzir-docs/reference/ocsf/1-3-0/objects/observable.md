# Observable

> The observable object is a pivot element that contains related information found in many places in the event.


The observable object is a pivot element that contains related information found in many places in the event.

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: required

The full name of the observable attribute. The `name` is a pointer/reference to an attribute within the event data. For example: `file.name`.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: Unknown observable data type.
  * `1` - `Hostname`: Observable by Dictionary Type. Unique name assigned to a device connected to a computer network. A domain name in general is an Internet address that can be resolved through the Domain Name System (DNS). For example: `r2-d2.example.com`.
  * `2` - `IP Address`: Observable by Dictionary Type. Internet Protocol address (IP address), in either IPv4 or IPv6 format. For example, `192.168.200.24` or `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.
  * `3` - `MAC Address`: Observable by Dictionary Type. Media Access Control (MAC) address. For example: `18:36:F3:98:4F:9A`.
  * `4` - `User Name`: Observable by Dictionary Type. User name. For example: `john_doe`.
  * `5` - `Email Address`: Observable by Dictionary Type. Email address. For example: `john_doe@example.com`.
  * `6` - `URL String`: Observable by Dictionary Type. Uniform Resource Locator (URL) string. For example: `http://www.example.com/download/trouble.exe`.
  * `7` - `File Name`: Observable by Dictionary Type. File name. For example: `text-file.txt`.
  * `8` - `Hash`: Observable by Dictionary Type. Hash. A unique value that corresponds to the content of the file, image, ja3\_hash or hassh found in the schema. For example MD5: `3172ac7e2b55cbb81f04a6e65855a628`.
  * `9` - `Process Name`: Observable by Dictionary Type. Process name. For example: `Notepad`.
  * `10` - `Resource UID`: Observable by Dictionary Type. Resource unique identifier. For example, S3 Bucket name or EC2 Instance ID.
  * `11` - `Port`: Observable by Dictionary Type. The TCP/UDP port number. For example: `80` or `22`.
  * `12` - `Subnet`: Observable by Dictionary Type. The subnet represented in a CIDR notation, using the format network\_address/prefix\_length. The network\_address can be in either IPv4 or IPv6 format. The prefix length indicates the number of bits used for the network portion, and the remaining bits are available for host addresses within that subnet. For example:

* 192.168.1.0/24

* 2001:0db8:85a3:0000::/64

  * `13` - `Command Line`: Observable by Dictionary Attribute. The full command line used to launch an application, service, process, or job. For example: `ssh user@10.0.0.10`. If the command line is unavailable or missing, the empty string `''` is to be used.
  * `14` - `Country`: Observable by Dictionary Attribute. The ISO 3166-1 Alpha-2 country code. For the complete list of country codes see [ISO 3166-1 alpha-2 codes](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en).

Note: The two letter country code should be capitalized. For example: `US` or `CA`.

* `15` - `Process ID`: Observable by Dictionary Attribute. The process identifier, as reported by the operating system. Process ID (PID) is a number used by the operating system to uniquely identify an active process.
* `16` - `HTTP User-Agent`: Observable by Dictionary Attribute. The request header that identifies the operating system and web browser.
* `17` - `CWE Object: uid`: Observable by Object-Specific Attribute. Object-specific attribute “uid” for the CWE Object.
* `18` - `CVE Object: uid`: Observable by Object-Specific Attribute. Object-specific attribute “uid” for the CVE Object.
* `19` - `User Credential ID`: Observable by Dictionary Attribute. The unique identifier of the user’s credential. For example, AWS Access Key ID.
* `20` - `Endpoint`: Observable by Object. The Endpoint object describes a physical or virtual device that connects to and exchanges information with a computer network. Some examples of endpoints are mobile devices, desktop computers, virtual machines, embedded devices, and servers. Internet-of-Things devices—like cameras, lighting, refrigerators, security systems, smart speakers, and thermostats—are also endpoints.
* `21` - `User`: Observable by Object. The User object describes the characteristics of a user/person or a security principal. Defined by D3FEND [d3f:UserAccount](https://d3fend.mitre.org/dao/artifact/d3f:UserAccount/).
* `22` - `Email`: Observable by Object. The Email object describes the email metadata such as sender, recipients, and direction. Defined by D3FEND [d3f:Email](https://d3fend.mitre.org/dao/artifact/d3f:Email/).
* `23` - `Uniform Resource Locator`: Observable by Object. The Uniform Resource Locator(URL) object describes the characteristics of a URL. Defined in [RFC 1738](https://datatracker.ietf.org/doc/html/rfc1738) and by D3FEND [d3f:URL](https://d3fend.mitre.org/dao/artifact/d3f:URL/).
* `24` - `File`: Observable by Object. The File object represents the metadata associated with a file stored in a computer system. It encompasses information about the file itself, including its attributes, properties, and organizational details. Defined by D3FEND [d3f:File](https://next.d3fend.mitre.org/dao/artifact/d3f:File/).
* `25` - `Process`: Observable by Object. The Process object describes a running instance of a launched program. Defined by D3FEND [d3f:Process](https://d3fend.mitre.org/dao/artifact/d3f:Process/).
* `26` - `Geo Location`: Observable by Object. The Geo Location object describes a geographical location, usually associated with an IP address. Defined by D3FEND [d3f:PhysicalLocation](https://d3fend.mitre.org/dao/artifact/d3f:PhysicalLocation/).
* `27` - `Container`: Observable by Object. The Container object describes an instance of a specific container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.
* `30` - `Fingerprint`: Observable by Object. The Fingerprint object provides detailed information about a digital fingerprint, which is a compact representation of data used to identify a longer piece of information, such as a public key or file content. It contains the algorithm and value of the fingerprint, enabling efficient and reliable identification of the associated data.
* `99` - `Other`: The observable data type is not mapped. See the `type` attribute, which may contain data source specific value.

The observable value type identifier.

**`reputation`**

* **Type**: [`reputation`](reputation.md)
* **Requirement**: optional

Contains the original and normalized reputation scores.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The observable value type name.

**`value`**

* **Type**: `string_t`
* **Requirement**: optional

The value associated with the observable attribute. The meaning of the value depends on the observable type. If the `name` refers to a scalar attribute, then the `value` is the value of the attribute. If the `name` refers to an object attribute, then the `value` is not populated.

## Used By

* [`account_change`](../classes/account_change.md)
* [`admin_group_query`](../classes/admin_group_query.md)
* [`api_activity`](../classes/api_activity.md)
* [`application_lifecycle`](../classes/application_lifecycle.md)
* [`authentication`](../classes/authentication.md)
* [`authorize_session`](../classes/authorize_session.md)
* [`base_event`](../classes/base_event.md)
* [`compliance_finding`](../classes/compliance_finding.md)
* [`config_state`](../classes/config_state.md)
* [`data_security_finding`](../classes/data_security_finding.md)
* [`datastore_activity`](../classes/datastore_activity.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`device_config_state_change`](../classes/device_config_state_change.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`email_activity`](../classes/email_activity.md)
* [`email_file_activity`](../classes/email_file_activity.md)
* [`email_url_activity`](../classes/email_url_activity.md)
* [`entity_management`](../classes/entity_management.md)
* [`event_log`](../classes/event_log.md)
* [`file_activity`](../classes/file_activity.md)
* [`file_hosting`](../classes/file_hosting.md)
* [`file_query`](../classes/file_query.md)
* [`file_remediation_activity`](../classes/file_remediation_activity.md)
* [`folder_query`](../classes/folder_query.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`group_management`](../classes/group_management.md)
* [`http_activity`](../classes/http_activity.md)
* [`incident_finding`](../classes/incident_finding.md)
* [`inventory_info`](../classes/inventory_info.md)
* [`job_query`](../classes/job_query.md)
* [`kernel_activity`](../classes/kernel_activity.md)
* [`kernel_extension`](../classes/kernel_extension.md)
* [`kernel_object_query`](../classes/kernel_object_query.md)
* [`memory_activity`](../classes/memory_activity.md)
* [`module_activity`](../classes/module_activity.md)
* [`module_query`](../classes/module_query.md)
* [`network_activity`](../classes/network_activity.md)
* [`network_connection_query`](../classes/network_connection_query.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`network_remediation_activity`](../classes/network_remediation_activity.md)
* [`networks_query`](../classes/networks_query.md)
* [`ntp_activity`](../classes/ntp_activity.md)
* [`patch_state`](../classes/patch_state.md)
* [`peripheral_device_query`](../classes/peripheral_device_query.md)
* [`process_activity`](../classes/process_activity.md)
* [`process_query`](../classes/process_query.md)
* [`process_remediation_activity`](../classes/process_remediation_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`remediation_activity`](../classes/remediation_activity.md)
* [`scan_activity`](../classes/scan_activity.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)
* [`security_finding`](../classes/security_finding.md)
* [`service_query`](../classes/service_query.md)
* [`session_query`](../classes/session_query.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`software_info`](../classes/software_info.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`user_access`](../classes/user_access.md)
* [`user_inventory`](../classes/user_inventory.md)
* [`user_query`](../classes/user_query.md)
* [`vulnerability_finding`](../classes/vulnerability_finding.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)