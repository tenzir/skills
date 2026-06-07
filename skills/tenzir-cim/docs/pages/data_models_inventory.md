---
title: Inventory
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/inventory
last_modified: 2026-04-01T20:48:25.635Z
version: 8.5
---

# Inventory

The fields and tags in the Inventory data model describe common computer infrastructure components from any data source, along with network infrastructure inventory and topology. This model was formerly labeled and documented as "Compute Inventory." The internal name of the datamodel has not changed, to support backward compatibility.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with Inventory event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| All_Inventory | inventory |
| cpu OR memory OR network OR storage OR (system, version) OR user OR virtual |

| \|____ CPU | cpu |

| \|____ Memory | memory |

| \|____ Network | network |

| \|____ Storage | storage |

| \|____ OS | system |
| version |

| \|____ User | user |

| \|____ Default_Accounts | default |

| \|____ Virtual_OS | virtual |

| \|____ Snapshot | snapshot |

| \|____ Tools | tools |

## Fields for Inventory event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| All_Inventory | ` description ` | string | The description of the inventory system. |  |
| All_Inventory | ` dest ` | string | The system where the data originated, the source of the event. You can alias ' this from more specific fields, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . |  |

| All_Inventory | ` dest_bunit ` | string | The business unit of the system where the data is going. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Inventory | ` dest_category ` | string | The category of the system where the data is going, such as ` email_server ` or ` SOX-compliant ` . This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Inventory | ` dest_priority ` | string | The priority of the system where the data is going. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Inventory | ` enabled ` | boolean | Indicates whether the resource is enabled or disabled. |  |
| All_Inventory | ` family ` | string | The product family of the resource, such as ` 686_64 ` or ` RISC ` . |  |
| All_Inventory | ` hypervisor_id ` | string | The hypervisor identifier, if applicable. |  |
| All_Inventory | ` serial ` | string | The serial number of the resource. |  |
| All_Inventory | ` status ` | string | The current reported state of the resource. |  |
| All_Inventory | ` tag ` | string | Splunk uses this automatically generated field to access tags from within data models. You do not need to populate it. |  |
| All_Inventory | ` vendor_product ` | string | The vendor and product name of the resource, such as ` Cisco Catalyst 3850 ` . This field can be automatically populated by ` vendor ` and ` product ` fields in your data. |  |
| All_Inventory | ` version ` | string | The version of a computer resource, such as ` 2008r2 ` or ` 3.0.0 ` . |  |
| CPU | ` cpu_cores ` | number | The number of CPU cores reported by the resource (total, not per CPU). |  |
| CPU | ` cpu_count ` | number | The number of CPUs reported by the resource. |  |
| CPU | ` cpu_mhz ` | number | The maximum speed of the CPU reported by the resource (in megahertz). |  |
| Memory | ` mem ` | number | The total amount of memory installed in or allocated to the resource, in megabytes. |  |
| Network | ` dest_ip ` | string | The IP address for the system that the data is going to. |  |
| Network | ` dns ` | string | The domain name server for the resource. |  |
| Network | ` inline_nat ` | string | Identifies whether the resource is a network address translation pool. |  |
| Network | ` interface ` | string | The network interfaces of the computing resource, such as ` eth0, eth1 ` or ` Wired Ethernet Connection, Teredo Tunneling Pseudo-Interface ` . |  |
| Network | ` ip ` | string | The network address of the computing resource, such as ` 192.168.1.1 ` or ` E80:0000:0000:0000:0202:B3FF:FE1E:8329 ` . |  |
| Network | ` lb_method ` | string | The load balancing method used by the computing resource such as ` method ` , ` round robin ` , or ` least weight ` . |  |
| Network | ` mac ` | string | A MAC (media access control) address associated with the resource, such as ` 06:10:9f:eb:8f:14 ` . Note: Always force lower case on this field. Note: Always use colons instead of dashes, spaces, or no separator. |  |
| Network | ` name ` | string | A name field provided in some data sources. |  |
| Network | ` node ` | string | Represents a node hit. |  |
| Network | ` node_port ` | number | The number of the destination port on the server that you requested from. |  |
| Network | ` src_ip ` | string | The IP address for the system from which the data originates. |  |
| Network | ` vip_port ` | number | The port number for the virtual IP address (VIP). A VIP allows multiple MACs to use one IP address. VIPs are often used by load balancers. |  |
| OS | ` os ` | string | The operating system of the resource, such as ` Microsoft Windows Server 2008r2 ` . This field is constructed from ` vendor_product ` and ` version ` fields. |  |
| Storage | ` array ` | string | The array that the storage resource is a member of, if applicable |  |
| Storage | ` blocksize ` | number | The block size used by the storage resource, in kilobytes. |  |
| Storage | ` cluster ` | string | The index cluster that the resource is a member of, if applicable. |  |
| Storage | ` fd_max ` | number | The maximum number of file descriptors available. |  |
| Storage | ` latency ` | number | The latency reported by the resource, in milliseconds. |  |
| Storage | ` mount ` | string | The path at which a storage resource is mounted. |  |
| Storage | ` parent ` | string | A higher level object that this resource is owned by, if applicable. |  |
| Storage | ` read_blocks ` | number | The maximum possible number of blocks read per second during a polling period . |  |
| Storage | ` read_latency ` | number | For a polling period, the average amount of time elapsed until a read request is filled by the host disks (in ms). |  |
| Storage | ` read_ops ` | number | The total number of read operations in the polling period. |  |
| Storage | ` storage ` | number | The amount of storage capacity allocated to the resource, in megabytes. |  |
| Storage | ` write_blocks ` | number | The maximum possible number of blocks written per second during a polling period. |  |
| Storage | ` write_latency ` | number | For a polling period, the average amount of time elapsed until a write request is filled by the host disks (in ms). |  |
| Storage | ` write_ops ` | number | The total number of write operations in the polling period. |  |
| User | ` interactive ` | boolean | Indicates whether a locally defined account on a resource can be interactively logged in. |  |
| User | ` password ` | string | Displays the stored password(s) for a locally defined account, if it has any. For instance, an add-on may report the password column from ` /etc/passwd ` in this field. |  |
| User | ` shell ` | string | Indicates the shell program used by a locally defined account. |  |
| User | ` user ` | string | The full name of a locally defined account. |  |

| User | ` user_bunit ` | string | The business unit of the locally-defined user account. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| User | ` user_category ` | string | The category of the system where the data originated, such as ` email_server ` or ` SOX-compliant ` . This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| User | ` user_id ` | number | The user identification for a locally defined account. |  |

| User | ` user_priority ` | string | The priority of a locally-defined account. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Virtual_OS | ` hypervisor ` | string | The hypervisor parent of a virtual guest OS. |  |
| Snapshot | ` size ` | number | The snapshot file size, in megabytes. |  |
| Snapshot | ` snapshot ` | string | The name of a snapshot file. |  |
| Snapshot | ` time ` | time | The time at which the snapshot was taken. |  |
