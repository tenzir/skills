---
title: Performance
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/performance
last_modified: 2026-04-01T20:48:25.223Z
version: 8.5
---

# Performance

The fields in the Performance data model describe performance tracking data.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with Performance event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| All_Performance | performance |
| cpu OR facilities OR memory OR storage OR network OR (os, (uptime OR (time, synchronize))) |

| \|____CPU | cpu |

| \|____Facilities | facilities |

| \|____Memory | memory |

| \|____Storage | storage |

| \|____Network | network |

| \|____OS | os |

| \|____Uptime | uptime |

| \|____Timesync | time |
| synchronize |

## Fields for Performance event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Object name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| All_Performance | ` dest ` | string | The system where the event occurred, usually a facilities resource such as a rack or room. You can alias this from more specific fields in your event data, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . | recommended |

| All_Performance | ` dest_bunit ` | string | The business unit of the system where the event occurred. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Performance | ` dest_category ` | string | The category of the system where the event occurred. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Performance | ` dest_priority ` | string | The priority of the system where the performance event occurred. |  |

| All_Performance | ` dest_should_timesync ` | boolean | Indicates whether or not the system where the performance event occurred should time sync. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Performance | ` dest_should_update ` | boolean | Indicates whether or not the system where the performance event occurred should update. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Performance | ` hypervisor_id ` | string | The ID of the virtualization hypervisor. |  |
| All_Performance | ` resource_type ` | string | The type of facilities resource involved in the performance event, such as a ` rack ` , ` room ` , or ` system ` . |  |
| All_Performance | ` tag ` | string | This automatically generated field is used to access tags from within data models. Do not define extractions for this field when writing add-ons. |  |
| CPU | ` cpu_load_mhz ` | number | The amount of CPU load reported by the controller in megahertz. |  |
| CPU | ` cpu_load_percent ` | number | The amount of CPU load reported by the controller in percentage points. | recommended |
| CPU | ` cpu_time ` | number | The number of CPU seconds consumed by processes. |  |
| CPU | ` cpu_user_percent ` | number | Percentage of CPU user time consumed by processes. |  |
| Facilities | ` fan_speed ` | number | The speed of the cooling fan in the facilities resource, in rotations per second. |  |
| Facilities | ` power ` | number | Rate at which power is consumed by the facilities resource, in kW. |
| Facilities | ` temperature ` | number | Average temperature of the facilities resource, in °C. | recommended |
| Memory | ` mem ` | number | The total amount of memory capacity reported by the resource, in megabytes. | recommended |
| Memory | ` mem_committed ` | number | The committed amount of memory reported by the resource, in megabytes. |  |
| Memory | ` mem_free ` | number | The free amount of memory reported by the resource, in megabytes. | recommended |
| Memory | ` mem_used ` | number | The used amount of memory reported by the resource, in megabytes. | recommended |
| Memory | ` swap ` | number | The total swap space size, in megabytes, if applicable. |  |
| Memory | ` swap_free ` | number | The free swap space size, in megabytes, if applicable. |  |
| Memory | ` swap_used ` | number | The used swap space size, in megabytes, if applicable. |  |
| Storage | ` array ` | number | The array that the resource is a member of, if applicable. |  |
| Storage | ` blocksize ` | number | Block size used by the storage resource, in kilobytes. |  |
| Storage | ` cluster ` | string | The cluster that the resource is a member of, if applicable. |  |
| Storage | ` fd_max ` | number | The maximum number of available file descriptors. |  |
| Storage | ` fd_used ` | number | The current number of open file descriptors. |  |
| Storage | ` latency ` | number | The latency reported by the resource, in milliseconds. |  |
| Storage | ` mount ` | string | The mount point of a storage resource. |  |
| Storage | ` parent ` | string | A generic indicator of hierarchy. For instance, a disk event might include the array ID here. |  |
| Storage | ` read_blocks ` | number | Number of blocks read. |  |
| Storage | ` read_latency ` | number | The latency of read operations, in milliseconds. |  |
| Storage | ` read_ops ` | number | Number of read operations. |  |
| Storage | ` storage ` | number | The total amount of storage capacity reported by the resource, in megabytes. |  |
| Storage | ` storage_free ` | number | The free amount of storage capacity reported by the resource, in megabytes. | recommended |
| Storage | ` storage_free_percent ` | number | The percentage of storage capacity reported by the resource that is free. | recommended |
| Storage | ` storage_used ` | number | The used amount of storage capacity reported by the resource, in megabytes. | recommended |
| Storage | ` storage_used_percent ` | number | The percentage of storage capacity reported by the resource that is used. | recommended |
| Storage | ` write_blocks ` | number | The number of blocks written by the resource. |  |
| Storage | ` write_latency ` | number | The latency of write operations, in milliseconds. |  |
| Storage | ` write_ops ` | number | The total number of write operations processed by the resource. |  |
| Network | ` thruput ` | number | The current throughput reported by the service, in bytes. | recommended |
| Network | ` thruput_max ` | number | The maximum possible throughput reported by the service, in bytes. |  |
| OS | ` signature ` | string | The event description signature, if available. | recommended |
| OS | ` signature_id ` | string | The unique identifier or event code of the event signature. |  |

-
-

| Timesync | ` action ` | string | The result of a time sync event. | recommended prescribed values: ` success ` , ` failure ` |
| Uptime | ` uptime ` | number | The uptime of the compute resource, in seconds. | recommended |
