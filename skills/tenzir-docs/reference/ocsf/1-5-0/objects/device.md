# Device

> The Device object represents an addressable computer system or host, which is typically connected to a computer network and participates in the transmission or processing of data within the computer network.


The Device object represents an addressable computer system or host, which is typically connected to a computer network and participates in the transmission or processing of data within the computer network.

* **Extends**: `endpoint`

## Attributes

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Server`: A [server](https://d3fend.mitre.org/dao/artifact/d3f:Server/).
  * `2` - `Desktop`: A [desktop computer](https://d3fend.mitre.org/dao/artifact/d3f:DesktopComputer/).
  * `3` - `Laptop`: A [laptop computer](https://d3fend.mitre.org/dao/artifact/d3f:LaptopComputer/).
  * `4` - `Tablet`: A [tablet computer](https://d3fend.mitre.org/dao/artifact/d3f:TabletComputer/).
  * `5` - `Mobile`: A [mobile phone](https://d3fend.mitre.org/dao/artifact/d3f:MobilePhone/).
  * `6` - `Virtual`: A [virtual machine](https://d3fend.mitre.org/dao/artifact/d3f:VirtualizationSoftware/).
  * `7` - `IOT`: An [IOT (Internet of Things) device](https://www.techtarget.com/iotagenda/definition/IoT-device).
  * `8` - `Browser`: A [web browser](https://d3fend.mitre.org/dao/artifact/d3f:Browser/).
  * `9` - `Firewall`: A [networking firewall](https://d3fend.mitre.org/dao/artifact/d3f:Firewall/).
  * `10` - `Switch`: A [networking switch](https://d3fend.mitre.org/dao/artifact/d3f:Switch/).
  * `11` - `Hub`: A [networking hub](https://en.wikipedia.org/wiki/Ethernet_hub).
  * `12` - `Router`: A [networking router](https://d3fend.mitre.org/dao/artifact/d3f:Router/).
  * `13` - `IDS`: An [intrusion detection system](https://d3fend.mitre.org/dao/artifact/d3f:IntrusionDetectionSystem/).
  * `14` - `IPS`: An [intrusion prevention system](https://d3fend.mitre.org/dao/artifact/d3f:IntrusionPreventionSystem/).
  * `15` - `Load Balancer`: A [Load Balancer device.](https://en.wikipedia.org/wiki/Load_balancing_\(computing\))
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The device type ID.

**`container`**

* **Type**: [`container`](container.md)
* **Requirement**: recommended

The information describing an instance of a container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.

**`hostname`**

* **Type**: `hostname_t`
* **Requirement**: recommended

The device hostname.

**`instance_uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of a VM instance.

**`interface_name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the network interface (e.g. eth2).

**`interface_uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the network interface.

**`namespace_pid`**

* **Type**: `integer_t`
* **Requirement**: recommended

If running under a process namespace (such as in a container), the process identifier within that process namespace.

**`owner`**

* **Type**: [`user`](user.md)
* **Requirement**: recommended

The identity of the service or user account that owns the endpoint or was last logged into it.

**`region`**

* **Type**: `string_t`
* **Requirement**: recommended

The region where the virtual machine is located. For example, an AWS Region.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The device type. For example: `unknown`, `server`, `desktop`, `laptop`, `tablet`, `mobile`, `virtual`, `browser`, or `other`.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the device. For example the Windows TargetSID or AWS EC2 ARN.

**`vendor_name`**

* **Type**: `string_t`
* **Requirement**: recommended

The vendor for the device. For example `Dell` or `Lenovo`.

**`agent_list`**

* **Type**: [`agent`](agent.md)
* **Requirement**: optional

A list of `agent` objects associated with a device, endpoint, or resource.

**`autoscale_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the cloud autoscale configuration.

**`boot_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time the system was booted.

**`boot_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time the system was booted.

**`boot_uid`**

* **Type**: `string_t`
* **Requirement**: optional

A unique identifier of the device that changes after every reboot. For example, the value of `/proc/sys/kernel/random/boot_id` from Linux’s procfs.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the device was known to have been created.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the device was known to have been created.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the device, ordinarily as reported by the operating system.

**`domain`**

* **Type**: `string_t`
* **Requirement**: optional

The network domain where the device resides. For example: `work.example.com`.

**`eid`**

* **Type**: `string_t`
* **Requirement**: optional

An Embedded Identity Document, is a unique serial number that identifies an eSIM-enabled device.

**`first_seen_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The initial discovery time of the device.

**`first_seen_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The initial discovery time of the device.

**`groups`**

* **Type**: [`group`](group.md)
* **Requirement**: optional

The group names to which the device belongs. For example: `["Windows Laptops", "Engineering"]`.

**`hw_info`**

* **Type**: [`device_hw_info`](device_hw_info.md)
* **Requirement**: optional

The endpoint hardware information.

**`hypervisor`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the hypervisor running on the device. For example, `Xen`, `VMware`, `Hyper-V`, `VirtualBox`, etc.

**`iccid`**

* **Type**: `string_t`
* **Requirement**: optional

The Integrated Circuit Card Identification of a mobile device. Typically it is a unique 18 to 22 digit number that identifies a SIM card.

**`image`**

* **Type**: [`image`](image.md)
* **Requirement**: optional

The image used as a template to run the virtual machine.

**`imei`**

* **Type**: `string_t`
* **Requirement**: optional

The International Mobile Equipment Identity that is associated with the device.

**`imei_list`**

* **Type**: `string_t`
* **Requirement**: optional

The International Mobile Equipment Identity values that are associated with the device.

**`ip`**

* **Type**: `ip_t`
* **Requirement**: optional

The device IP address, in either IPv4 or IPv6 format.

**`is_backed_up`**

* **Type**: `boolean_t`
* **Requirement**: optional

Indicates whether the device or resource has a backup enabled, such as an automated snapshot or a cloud backup. For example, this is indicated by the `cloudBackupEnabled` value within JAMF Pro mobile devices or the registration of an AWS ARN with the AWS Backup service.

**`is_compliant`**

* **Type**: `boolean_t`
* **Requirement**: optional

The event occurred on a compliant device.

**`is_managed`**

* **Type**: `boolean_t`
* **Requirement**: optional

The event occurred on a managed device.

**`is_mobile_account_active`**

* **Type**: `boolean_t`
* **Requirement**: optional

Indicates whether the device has an active mobile account. For example, this is indicated by the `itunesStoreAccountActive` value within JAMF Pro mobile devices.

**`is_personal`**

* **Type**: `boolean_t`
* **Requirement**: optional

The event occurred on a personal device.

**`is_shared`**

* **Type**: `boolean_t`
* **Requirement**: optional

The event occurred on a shared device.

**`is_supervised`**

* **Type**: `boolean_t`
* **Requirement**: optional

The event occurred on a supervised device. Devices that are supervised are typically mobile devices managed by a Mobile Device Management solution and are restricted from specific behaviors such as Apple AirDrop.

**`is_trusted`**

* **Type**: `boolean_t`
* **Requirement**: optional

The event occurred on a trusted device.

**`last_seen_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The most recent discovery time of the device.

**`last_seen_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The most recent discovery time of the device.

**`location`**

* **Type**: [`location`](location.md)
* **Requirement**: optional

The geographical location of the device.

**`mac`**

* **Type**: `mac_t`
* **Requirement**: optional

The Media Access Control (MAC) address of the endpoint.

**`meid`**

* **Type**: `string_t`
* **Requirement**: optional

The Mobile Equipment Identifier. It’s a unique number that identifies a Code Division Multiple Access (CDMA) mobile device.

**`model`**

* **Type**: `string_t`
* **Requirement**: optional

The model of the device. For example `ThinkPad X1 Carbon`.

**`modified_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the device was last known to have been modified.

**`modified_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the device was last known to have been modified.

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The alternate device name, ordinarily as assigned by an administrator.

Note: The Name could be any other string that helps to identify the device, such as a phone number; for example `310-555-1234`.

**`network_interfaces`**

* **Type**: [`network_interface`](network_interface.md)
* **Requirement**: optional

The physical or virtual network interfaces that are associated with the device, one for each unique MAC address/IP address/hostname/name combination.

Note: The first element of the array is the network information that pertains to the event.

**`org`**

* **Type**: [`organization`](organization.md)
* **Requirement**: optional

Organization and org unit related to the device.

**`os`**

* **Type**: [`os`](os.md)
* **Requirement**: optional

The endpoint operating system.

**`os_machine_uuid`**

* **Type**: `uuid_t`
* **Requirement**: optional

The operating system assigned Machine ID. In Windows, this is the value stored at the registry path: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\MachineGuid`. In Linux, this is stored in the file: `/etc/machine-id`.

**`risk_level`**

* **Type**: `string_t`
* **Requirement**: optional

The risk level, normalized to the caption of the risk\_level\_id value.

**`risk_level_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Info`
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `4` - `Critical`
  * `99` - `Other`: The risk level is not mapped. See the `risk_level` attribute, which contains a data source specific value.

The normalized risk level id.

**`risk_score`**

* **Type**: `integer_t`
* **Requirement**: optional

The risk score as reported by the event source.

**`subnet`**

* **Type**: `subnet_t`
* **Requirement**: optional

The subnet mask.

**`subnet_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of a virtual subnet.

**`udid`**

* **Type**: `string_t`
* **Requirement**: optional

The Apple assigned Unique Device Identifier (UDID). For iOS, iPadOS, tvOS, watchOS and visionOS devices, this is the UDID. For macOS devices, it is the Provisioning UDID. For example: `00008020-008D4548007B4F26`

**`uid_alt`**

* **Type**: `string_t`
* **Requirement**: optional

An alternate unique identifier of the device if any. For example the ActiveDirectory DN.

**`vlan_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The Virtual LAN identifier.

**`vpc_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the Virtual Private Cloud (VPC).

**`zone`**

* **Type**: `string_t`
* **Requirement**: optional

The network zone or LAN segment.

## Constraints

At least one of: `ip`, `uid`, `name`, `hostname`, `instance_uid`, `interface_uid`, `interface_name`

## Used By

* [`account_change`](../classes/account_change.md)
* [`admin_group_query`](../classes/admin_group_query.md)
* [`airborne_broadcast_activity`](../classes/airborne_broadcast_activity.md)
* [`api_activity`](../classes/api_activity.md)
* [`application_error`](../classes/application_error.md)
* [`application_lifecycle`](../classes/application_lifecycle.md)
* [`application_security_posture_finding`](../classes/application_security_posture_finding.md)
* [`authentication`](../classes/authentication.md)
* [`authorize_session`](../classes/authorize_session.md)
* [`base_event`](../classes/base_event.md)
* [`cloud_resources_inventory_info`](../classes/cloud_resources_inventory_info.md)
* [`compliance_finding`](../classes/compliance_finding.md)
* [`config_state`](../classes/config_state.md)
* [`data_security_finding`](../classes/data_security_finding.md)
* [`datastore_activity`](../classes/datastore_activity.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`device_config_state_change`](../classes/device_config_state_change.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`drone_flights_activity`](../classes/drone_flights_activity.md)
* [`email_activity`](../classes/email_activity.md)
* [`email_file_activity`](../classes/email_file_activity.md)
* [`email_url_activity`](../classes/email_url_activity.md)
* [`entity_management`](../classes/entity_management.md)
* [`event_log_actvity`](../classes/event_log_actvity.md)
* [`evidence_info`](../classes/evidence_info.md)
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
* [`kernel_extension_activity`](../classes/kernel_extension_activity.md)
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
* [`osint_inventory_info`](../classes/osint_inventory_info.md)
* [`patch_state`](../classes/patch_state.md)
* [`peripheral_device_query`](../classes/peripheral_device_query.md)
* [`process_activity`](../classes/process_activity.md)
* [`process_query`](../classes/process_query.md)
* [`process_remediation_activity`](../classes/process_remediation_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`remediation_activity`](../classes/remediation_activity.md)
* [`scan_activity`](../classes/scan_activity.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)
* [`script_activity`](../classes/script_activity.md)
* [`security_finding`](../classes/security_finding.md)
* [`service_query`](../classes/service_query.md)
* [`session_query`](../classes/session_query.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`software_info`](../classes/software_info.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`startup_item_query`](../classes/startup_item_query.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`user_access`](../classes/user_access.md)
* [`user_inventory`](../classes/user_inventory.md)
* [`user_query`](../classes/user_query.md)
* [`vulnerability_finding`](../classes/vulnerability_finding.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)