# Device

> The Device object represents an addressable computer system or host, which is typically connected to a computer network and participates in the transmission or processing of data within the computer network.


The Device object represents an addressable computer system or host, which is typically connected to a computer network and participates in the transmission or processing of data within the computer network. Defined by D3FEND [d3f:Host](https://d3fend.mitre.org/dao/artifact/d3f:Host/).

* **Extends**: `endpoint`

## Attributes

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Server`
  * `2` - `Desktop`
  * `3` - `Laptop`
  * `4` - `Tablet`
  * `5` - `Mobile`
  * `6` - `Virtual`
  * `7` - `IOT`
  * `8` - `Browser`
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which may contain a data source specific value.

The device type ID.

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

**`ip`**

* **Type**: `ip_t`
* **Requirement**: recommended

The device IP address, in either IPv4 or IPv6 format.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The alternate device name, ordinarily as assigned by an administrator.

Note: The Name could be any other string that helps to identify the device, such as a phone number; for example `310-555-1234`.

**`region`**

* **Type**: `string_t`
* **Requirement**: recommended

The region where the virtual machine is located. For example, an AWS Region.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the device. For example the Windows TargetSID or AWS EC2 ARN.

**`autoscale_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the cloud autoscale configuration.

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

The group names to which the device belongs. For example: \`\[“Windows Laptops”, “Engineering”].

**`hw_info`**

* **Type**: [`device_hw_info`](device_hw_info.md)
* **Requirement**: optional

The device hardware information.

**`hypervisor`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the hypervisor running on the device. For example, `Xen`, `VMware`, `Hyper-V`, `VirtualBox`, etc.

**`image`**

* **Type**: [`image`](image.md)
* **Requirement**: optional

The image used as a template to run the virtual machine.

**`imei`**

* **Type**: `string_t`
* **Requirement**: optional

The International Mobile Station Equipment Identifier that is associated with the device.

**`is_compliant`**

* **Type**: `boolean_t`
* **Requirement**: optional

The event occurred on a compliant device.

**`is_managed`**

* **Type**: `boolean_t`
* **Requirement**: optional

The event occurred on a managed device.

**`is_personal`**

* **Type**: `boolean_t`
* **Requirement**: optional

The event occurred on a personal device.

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

The device Media Access Control (MAC) address.

**`modified_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the device was last known to have been modified.

**`modified_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the device was last known to have been modified.

**`network_interfaces`**

* **Type**: [`network_interface`](network_interface.md)
* **Requirement**: optional

The network interfaces that are associated with the device, one for each unique MAC address/IP address/hostname/name combination.

Note: The first element of the array is the network information that pertains to the event.

**`org`**

* **Type**: [`organization`](organization.md)
* **Requirement**: optional

Organization and org unit related to the device.

**`os`**

* **Type**: [`os`](os.md)
* **Requirement**: optional

The device operating system.

**`risk_level`**

* **Type**: `string_t`
* **Requirement**: optional

The risk level, normalized to the caption of the risk\_level\_id value. In the case of ‘Other’, it is defined by the event source.

**`risk_level_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Info`
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `4` - `Critical`

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

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The device type. For example: `unknown`, `server`, `desktop`, `laptop`, `tablet`, `mobile`, `virtual`, `browser`, or `other`.

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

## Constraints

At least one of: `ip`, `uid`, `name`, `hostname`, `instance_uid`, `interface_uid`, `interface_name`

## Used By

* [`account_change`](../classes/account_change.md)
* [`application_lifecycle`](../classes/application_lifecycle.md)
* [`authentication`](../classes/authentication.md)
* [`authorize_session`](../classes/authorize_session.md)
* [`config_state`](../classes/config_state.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`email_activity`](../classes/email_activity.md)
* [`email_file_activity`](../classes/email_file_activity.md)
* [`email_url_activity`](../classes/email_url_activity.md)
* [`entity_management`](../classes/entity_management.md)
* [`file_activity`](../classes/file_activity.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`group_management`](../classes/group_management.md)
* [`http_activity`](../classes/http_activity.md)
* [`inventory_info`](../classes/inventory_info.md)
* [`kernel_activity`](../classes/kernel_activity.md)
* [`kernel_extension`](../classes/kernel_extension.md)
* [`memory_activity`](../classes/memory_activity.md)
* [`module_activity`](../classes/module_activity.md)
* [`network_activity`](../classes/network_activity.md)
* [`process_activity`](../classes/process_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`user_access`](../classes/user_access.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)