---
title: Java Virtual Machines (JVM)
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/java-virtual-machines-jvm
last_modified: 2026-04-01T20:48:25.867Z
version: 8.5
---

# Java Virtual Machines (JVM)

The fields in the JVM data model describe generic Java server platforms.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with JVM event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| JVM | jvm |

| \|____ Threading | threading |

| \|____ Runtime | runtime |

| \|____ OS | os |

| \|____ Compilation | compilation |

| \|____ Classloading | classloading |

| \|____ Memory | memory |

## Fields for JVM event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. Note that it does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| JVM | ` jvm_description ` | string | A description field provided in some data sources. |  |
| JVM | ` tag ` | string | This automatically generated field is used to access tags from within datamodels. Add-on builders do not need to populate it. |  |

| Threading | ` cm_enabled ` | boolean | Indicates whether thread contention monitoring is enabled. | prescribed values: ` true ` , ` false ` , ` 1 ` , ` 0 ` |

| Threading | ` cm_supported ` | boolean | Indicates whether the JVM supports thread contention monitoring. | prescribed values: ` true ` , ` false ` , ` 1 ` , ` 0 ` |

| Threading | ` cpu_time_enabled ` | boolean | Indicates whether thread CPU time measurement is enabled. | prescribed values: ` true ` , ` false ` , ` 1 ` , ` 0 ` |

| Threading | ` cpu_time_supported ` | boolean | Indicates whether the Java virtual machine supports CPU time measurement for the current thread. | prescribed values: ` true ` , ` false ` , ` 1 ` , ` 0 ` |
| Threading | ` current_cpu_time ` | number | CPU-space time taken by the JVM, in seconds. |  |
| Threading | ` current_user_time ` | number | User-space time taken by the JVM, in seconds. |  |
| Threading | ` daemon_thread_count ` | number | The JVM's current daemon count. |  |

| Threading | ` omu_supported ` | boolean | Indicates whether the JVM supports monitoring of object monitor usage. | prescribed values: ` true ` , ` false ` , ` 1 ` , ` 0 ` |
| Threading | ` peak_thread_count ` | number | The JVM's peak thread count. |  |

| Threading | ` synch_supported ` | boolean | Indicates whether the JVM supports monitoring of ownable synchronizer usage. | prescribed values: ` true ` , ` false ` , ` 1 ` , ` 0 ` |
| Threading | ` thread_count ` | number | The JVM's current thread count. |  |
| Threading | ` threads_started ` | number | The total number of threads started in the JVM. |  |
| Runtime | ` process_name ` | string | Process name of the JVM process. |  |
| Runtime | ` start_time ` | timestamp | Start time of the JVM process. |  |
| Runtime | ` uptime ` | number | Uptime of the JVM process, in seconds. |  |
| Runtime | ` vendor_product ` | string | The JVM product or service. This field can be automatically populated by the the ` vendor ` and ` product ` fields in your raw data. |  |
| Runtime | ` version ` | string | Version of the JVM. |  |
| OS | ` committed_memory ` | number | Amount of memory committed to the JVM, in bytes. |  |
| OS | ` cpu_time ` | number | Amount of CPU time taken by the JVM, in seconds. |  |
| OS | ` free_physical_memory ` | number | Amount of free physical memory remaining to the JVM, in bytes. |  |
| OS | ` free_swap ` | number | Amount of free swap memory remaining to the JVM, in bytes. |  |
| OS | ` max_file_descriptors ` | number | Maximum file descriptors available to the JVM. |  |
| OS | ` open_file_descriptors ` | number | Number of file descriptors opened by the JVM. |  |
| OS | ` os ` | string | OS that the JVM is running on. |  |
| OS | ` os_architecture ` | string | OS architecture that the JVM is running on. |  |
| OS | ` os_version ` | string | OS version that the JVM is running on. |  |
| OS | ` physical_memory ` | number | Physical memory available to the OS that the JVM is running on, in bytes. |  |
| OS | ` swap_space ` | number | Swap memory space available to the OS that the JVM is running on, in bytes. |  |
| OS | ` system_load ` | number | System load of the OS that the JVM is running on. |  |
| OS | ` total_processors ` | number | Total processor cores available to the OS that the JVM is running on. |  |
| Compilation | ` compilation_time ` | number | Time taken by JIT compilation , in seconds. |  |
| Classloading | ` current_loaded ` | number | The current count of classes loaded in the JVM. |  |
| Classloading | ` total_loaded ` | number | The total count of classes loaded in the JVM. |  |
| Classloading | ` total_unloaded ` | number | The total count of classes unloaded from the JVM. |  |
| Memory | ` heap_committed ` | number | Committed amount of heap memory used by the JVM, in bytes. |  |
| Memory | ` heap_initial ` | number | Initial amount of heap memory used by the JVM, in bytes. |  |
| Memory | ` heap_max ` | number | Maximum amount of heap memory used by the JVM, in bytes. |  |
| Memory | ` heap_used ` | number | Heap memory used by the JVM, in bytes. |  |
| Memory | ` non_heap_committed ` | number | Committed amount of non-heap memory used by the JVM, in bytes. |  |
| Memory | ` non_heap_initial ` | number | Initial amount of non-heap memory used by the JVM, in bytes. |  |
| Memory | ` non_heap_max ` | number | Maximum amount of non-heap memory used by the JVM, in bytes. |  |
| Memory | ` non_heap_used ` | number | Non-heap memory used by the JVM, in bytes. |  |
| Memory | ` objects_pending ` | number | Number of objects pending in the JVM, in bytes. |  |
