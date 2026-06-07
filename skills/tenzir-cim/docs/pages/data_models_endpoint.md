---
title: Endpoint
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/endpoint
last_modified: 2026-04-01T20:48:24.609Z
version: 8.5
---

# Endpoint

The Endpoint data model replaces the Application State data model, which is deprecated as of software version 4.12.0. The architecture of this data model is different than the data model it replaces. Each data set is directly searchable as `DataModel.DataSet `rather than by node name.

The Endpoint data model is for monitoring endpoint clients including, but not limited to, end user machines, laptops, and bring your own devices (BYOD). If an event is about an endpoint process, service, file, port, and so on, then it relates to the Endpoint data model. For administrative and policy types of changes to infrastructure security devices, servers, and endpoint detection and response (EDR) systems, see Change.Endpoint in the Change data model.

The datasets for Processes and Services are for the launch of processes and services and not to observe a running process or service.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

| Dataset name | Tag name |
| --- | --- |
| Endpoint |  |
| \|____ Ports | listening |
| port |
| \|____ Processes | process |
| report |
| \|____ Services | service |
| report |
| \|____ Filesystem | endpoint |
| filesystem |
| \|____ Registry | endpoint |
| registry |

## Difference between the Endpoint and Change data models

The Endpoint data model monitors endpoint clients including, but not limited to, end user physical or virtual machines, laptops, bring your own devices (BYOD), and so on. If an event is about an endpoint process, service, file, or port, it relates to the Endpoint data model because such events typically pertain to regular user activities.

For administrative changes that include changes to infrastructure security devices, servers, Cloud environments, endpoint detection and response (EDR) systems, see the Change data model. Administrative changes in EDR systems are mapped to the Endpoint dataset of the Change data model, but not mapped to the Endpoint data model since they do not pertain to endpoints clients.

Note: The structure "Change.Endpoint" represents "DataModel.DataSet".

## Fields for the Endpoint event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. Note that it does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

## Ports

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| Ports | ` creation_time ` | timestamp | The time at which the network port started listening on the endpoint. |  |
| Ports | ` dest ` | string | The endpoint on which the port is listening. Expression: ` if(isnull(dest) OR dest=\"\",\"unknown\",dest) ` | - recommended - required for pytest-splunk-addon |
| Ports | ` dest_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` dest_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` dest_port ` | number | Network port listening on the endpoint, such as 53. | - recommended - required for pytest-splunk-addon |
| Ports | ` dest_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` dest_requires_av ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` dest_should_timesync ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` dest_should_update ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` process_guid ` | string | The globally unique identifier of the process assigned by the vendor_product. |  |
| Ports | ` process_id ` | number | The numeric identifier of the process assigned by the operating system. |  |
| Ports | ` src ` | string | The "remote" system connected to the listening port (if applicable). Expression: ` if(isnull(src) OR src=\"\",\"unknown\",src) ` | - recommended - required for pytest-splunk-addon |
| Ports | ` src_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Ports | ` src_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` src_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` src_port ` | number | The "remote" port connected to the listening port (if applicable). Expression: ` if(isnum(src_port),src_port,0) ` | - recommended - required for pytest-splunk-addon |
| Ports | ` src_requires_av ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` src_should_timesync ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` src_should_update ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` state ` | string | The status of the listening port, such as established, listening, etc. | required for pytest-splunk-addon |
| Ports | ` tag ` | string | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Ports | ` transport ` | string | The network transport protocol associated with the listening port, such as tcp, udp, etc." | - recommended - required for pytest-splunk-addon |
| Ports | ` transport_dest_port ` | string | Calculated as transport/dest_port, such as tcp/53. |  |
| Ports | ` user ` | string | The user account associated with the listening port. Expression: ` if(isnull(user) OR user=\"\",\"unknown\",user) ` | recommended |
| Ports | ` user_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` user_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Ports | ` user_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |

## Processes

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| Processes | ` action ` | string | The action taken by the endpoint, such as allowed, blocked, deferred. | required for pytest-splunk-addon |
| Processes | ` cpu_load_percent ` | number | CPU load consumed by the process (in percent). |  |
| Processes | ` dest ` | string | The endpoint for which the process was spawned. Expression: ` if(isnull(dest) OR dest=\"\",\"unknown\",dest) ` | - recommended - required for pytest-splunk-addon |
| Processes | ` dest_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Processes | ` dest_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Processes | ` dest_is_expected ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Processes | ` dest_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Processes | ` dest_requires_av ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Processes | ` dest_should_timesync ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Processes | ` dest_should_update ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Processes | ` loaded_file ` | string | (optional)File that was loaded. |  |
| Processes | ` mem_used ` | number | Memory used by the process (in bytes). |  |
| Processes | ` original_file_name ` | string | Original name of the file, not including path. Sometimes this field is similar to process name but the two do not always match, such as ` process_name=pwsh ` and ` original_file_name=powershell.exe ` to detect renamed instances of any process executing. | recommended |
| Processes | ` os ` | string | The operating system of the resource, such as Microsoft Windows Server 2008r2. |  |
| Processes | ` parent_process ` | string | The full command string of the parent process. Expression: ` if(isnull(parent_process) OR parent_process=\"\",\"unknown\", parent_process) ` | recommended |
| Processes | ` parent_process_exec ` | string | The executable name of the parent process. |  |
| Processes | ` parent_process_hash ` | string | The digest(s) of the parent process (md5, sha1, etc.) |  |
| Processes | ` parent_process_id ` | number | The numeric identifier of the parent process assigned by the operating system. | required for pytest-splunk-addon |
| Processes | ` parent_process_guid ` | string | The globally unique identifier of the parent process assigned by the vendor_product. |  |
| Processes | ` parent_process_name ` | string | The friendly name of the parent process, such as notepad.exe. Expression: ` case(isnotnull(parent_process_name) AND parent_process_name!=\"\",parent_process_name, isnotnull(parent_process) AND parent_process!=\"\",replace(parent_process, \"^\\s*([^\\s]+).*\",\"\\1\"),1=1,\"unknown\")" ` | - recommended - required for pytest-splunk-addon |
| Processes | ` parent_process_path ` | string | The file path of the parent process, such as C:\Windows\System32\notepad.exe. | required for pytest-splunk-addon |
| Processes | ` process ` | string | The full command string of the spawned process. Such as C:\WINDOWS\system32\cmd.exe \/c \"\"C:\Program Files\SplunkUniversalForwarder\etc\system\bin\powershell.cmd\" --scheme\"". There is a limit of 2048 characters. Expression: ` if(isnull(process) OR process=\"\",\"unknown\",process) ` | - recommended - required for pytest-splunk-addon |
| Processes | ` process_current_directory ` | string | The current working directory used to spawn the process. |  |
| Processes | ` process_exec ` | string | The executable name of the process, such as notepad.exe. Sometimes this is similar to ` process_name ` , such as notepad. However in malicious scenarios, such as Fruitfly, the ` process_exec ` is Perl while the ` process_name ` is Java. | required for pytest-splunk-addon |
| Processes | ` process_hash ` | string | The digests of the parent process, such as <md5>, <sha1>, etc. |  |
| Processes | ` process_guid ` | string | The globally unique identifier of the process assigned by the vendor_product. |  |
| Processes | ` process_id ` | number | The numeric identifier of the process assigned by the operating system. | required for pytest-splunk-addon |
| Processes | ` process_integrity_level ` | string | The integrity level of the process. | prescribed values: ` system ` , ` high ` , ` medium ` , ` low ` , ` untrusted ` |
| Processes | ` process_name ` | string | The friendly name of the process, such as notepad.exe. Sometimes this is similar to ` process_exec ` , such as notepad.exe. However in malicious scenarios, such as Fruitfly, the ` process_exec ` is Perl while the ` process_name ` is Java. Expression: ` case(isnotnull(process_name) AND process_name!=\"\",process_name,isnotnull (process) AND process!=\"\",replace(process,\"^\\s*([^\\s]+).*\",\"\\1\"),1=1,\"unknown\") ` | - recommended - required for pytest-splunk-addon |
| Processes | ` process_path ` | string | The file path of the process, such as C:\Windows\System32\notepad.exe. | required for pytest-splunk-addon |
| Processes | ` tag ` | string | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Processes | ` user ` | string | The user account that spawned the process. Expression: ` if(isnull(user) OR user=\"\",\"unknown\",user) ` | - recommended - required for pytest-splunk-addon |
| Processes | ` user_id ` | string | The unique identifier of the user account which spawned the process. |  |
| Processes | ` user_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Processes | ` user_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Processes | ` user_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Processes | ` vendor_product ` | string | The vendor and product name of the Endpoint solution that reported the event, such as Carbon Black Cb Response. This field can be automatically populated by vendor and product fields in your data." Expression: ` case(isnotnull(vendor_product),vendor_product, isnotnull(vendor) AND vendor!=\"unknown\" AND isnotnull(product) AND product!=\"unknown\",vendor.\" \".product,isnotnull(vendor) AND vendor!=\"unknown\" AND (isnull(product) OR product=\"unknown\"),vendor.\" unknown\",(isnull(vendor) OR vendor=\"unknown\") AND isnotnull(product) AND product!=\"unknown\",\"unknown \".product,isnotnull(sourcetype),sourcetype, 1=1,\"unknown\") ` | recommended |

## Services

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| Services | ` description ` | string | The description of the service. |  |
| Services | ` dest ` | string | The endpoint for which the service is installed. Expression: ` if(isnull(dest) OR dest=\"\",\"unknown\",dest) ` | - recommended - required for pytest-splunk-addon |
| Services | ` dest_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Services | ` dest_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Services | ` dest_is_expected ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Services | ` dest_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Services | ` dest_requires_av ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Services | ` dest_should_timesync ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Services | ` dest_should_update ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Services | ` process_guid ` | string | The globally unique identifier of the process assigned by the vendor_product. |  |
| Services | ` process_id ` | number | The numeric identifier of the process assigned by the operating system. |  |
| Services | ` service ` | string | The full service name. Expression: ` if(isnull(service) OR service=\"\",\"unknown\",service) ` | - recommended - required for pytest-splunk-addon |
| Services | ` service_dll ` | string | The dynamic link library associated with the service. |  |
| Services | ` service_dll_path ` | string | The file path to the dynamic link library assocatied with the service, such as C:\Windows\System32\comdlg32.dll. |  |
| Services | ` service_dll_hash ` | string | The digests of the dynamic link library associated with the service, such as <md5>, <sha1>, etc. |  |
| Services | ` service_dll_signature_exists ` | boolean | Whether or not the dynamic link library associated with the service has a digitally signed signature. |  |
| Services | ` service_dll_signature_verified ` | boolean | Whether or not the dynamic link library associated with the service has had its digitally signed signature verified. |  |
| Services | ` service_exec ` | string | The executable name of the service. |  |
| Services | ` service_hash ` | string | The digest(s) of the service, such as <md5>, <sha1>, etc. |  |
| Services | ` service_id ` | string | The unique identifier of the service assigned by the operating system. Expression: ` if(isnull(service_id) OR service_id=\"\",\"unknown\",service_id) ` | recommended |
| Services | ` service_name ` | string | The friendly service name. Expression: ` if(isnull(service_name) OR service_name=\"\",\"unknown\",service_name) ` | - recommended - required for pytest-splunk-addon |
| Services | ` service_path ` | string | The file path of the service, such as C:\WINDOWS\system32\svchost.exe. | required for pytest-splunk-addon |
| Services | ` service_signature_exists ` | boolean | Whether or not the service has a digitally signed signature. |  |
| Services | ` service_signature_verified ` | boolean | Whether or not the service has had its digitally signed signature verified. |  |
| Services | ` start_mode ` | string | The start mode for the service. Expression: ` if(isnull(start_mode) OR start_mode=\"\",\"unknown\",start_mode) ` | - recommended - required for pytest-splunk-addon - prescribed values: ` disabled ` , ` manual ` , ` auto ` |
| Services | ` status ` | string | The status of the service. Expression: ` if(isnull(dest) OR dest=\"\",\"unknown\",dest) ` | - recommended - required for pytest-splunk-addon - prescribed values: ` critical ` , ` started ` , ` stopped ` , ` warning ` |
| Services | ` tag ` | string | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Services | ` user ` | string | The user account associated with the service. Expression: ` if(isnull(user) OR user=\"\",\"unknown\",user) ` | - recommended - required for pytest-splunk-addon |
| Services | ` user_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Services | ` user_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Services | ` user_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Services | ` vendor_product ` | string | The vendor and product name of the Endpoint solution that reported the event, such as Carbon Black Cb Response. This field can be automatically populated by vendor and product fields in your data. Expression: ` case(isnotnull(vendor_product),vendor_product, isnotnull(vendor) AND vendor!=\"unknown\" AND isnotnull(product) AND product!=\"unknown\",vendor.\" \".product,isnotnull(vendor) AND vendor!=\"unknown\" AND (isnull(product) OR product=\"unknown\"),vendor.\" unknown\",(isnull(vendor) OR vendor=\"unknown\") AND isnotnull(product) AND product!=\"unknown\",\"unknown \".product,isnotnull(sourcetype),sourcetype, 1=1,\"unknown\") ` | recommended |

## Filesystem

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| Filesystem | ` action ` | string | The action performed on the resource. Expression: ` if(isnull(action) OR action=\"\",\"unknown\",action) ` | - recommended - required for pytest-splunk-addon - prescribed values: ` acl_modified ` , ` created ` , ` deleted ` , ` modified ` , ` read ` |
| Filesystem | ` dest ` | string | The endpoint pertaining to the filesystem activity. Expression: ` if(isnull(dest) OR dest=\"\",\"unknown\",dest) ` | - recommended - required for pytest-splunk-addon |
| Filesystem | ` dest_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Filesystem | ` dest_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Filesystem | ` dest_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Filesystem | ` dest_requires_av ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Filesystem | ` dest_should_timesync ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Filesystem | ` dest_should_update ` | boolean | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Filesystem | ` file_access_time ` | timestamp | The time that the file (the object of the event) was accessed. | recommended |
| Filesystem | ` file_create_time ` | timestamp | The time that the file (the object of the event) was created. | recommended |
| Filesystem | ` file_hash ` | string | A cryptographic identifier assigned to the file object affected by the event. Expression: ` if(isnull(file_hash) OR file_hash=\"\",\"unknown\",file_hash) ` | recommended |
| Filesystem | ` file_modify_time ` | timestamp | The time that the file (the object of the event) was altered. | recommended |
| Filesystem | ` file_name ` | string | The name of the file, such as notepad.exe. Expression: ` if(isnull(file_name) OR file_name=\"\",\"unknown\",file_name ` | - recommended - required for pytest-splunk-addon |
| Filesystem | ` file_path ` | string | The path of the file, such as C:\Windows\System32\notepad.exe. Expression: ` if(isnull(file_path) OR file_path=\"\",\"unknown\",file_path) ` | - recommended - required for pytest-splunk-addon |
| Filesystem | ` file_acl ` | string | Access controls associated with the file affected by the event. Expression: ` if(isnull(file_acl) OR file_acl=\"\",\"unknown\",file_acl) ` | recommended |
| Filesystem | ` file_size ` | string | The size of the file that is the object of the event, in kilobytes. Expression: ` if(isnum(file_size),file_size,null()) ` | recommended |
| Filesystem | ` image ` | string | The binary file path or name that is tied to a process ID (PID) in events such as process creation or termination. | Optional |
| Filesystem | ` process_guid ` | string | The globally unique identifier of the process assigned by the vendor_product. |  |
| Filesystem | ` process_id ` | number | The numeric identifier of the process assigned by the operating system. |  |
| Filesystem | ` tag ` | string | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Filesystem | ` user ` | string | The user account associated with the filesystem access. Expression: ` if(isnull(user) OR user=\"\",\"unknown\",user) ` | - recommended - required for pytest-splunk-addon |
| Filesystem | ` user_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Filesystem | ` user_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Filesystem | ` user_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Filesystem | ` vendor_product ` | string | The vendor and product name of the Endpoint solution that reported the event, such as Carbon Black Cb Response. This field can be automatically populated by vendor and product fields in your data. Expression: ` case(isnotnull(vendor_product),vendor_product, isnotnull(vendor) AND vendor!=\"unknown\" AND isnotnull(product) AND product!=\"unknown\",vendor.\" \".product,isnotnull(vendor) AND vendor!=\"unknown\" AND (isnull(product) OR product=\"unknown\"),vendor.\" unknown\",(isnull(vendor) OR vendor=\"unknown\") AND isnotnull(product) AND product!=\"unknown\",\"unknown \".product,isnotnull(sourcetype),sourcetype, 1=1,\"unknown\") ` | recommended |

## Registry

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| Registry | ` action ` | string | The action performed on the resource. Expression: ` if(isnull(action) OR action=\"\",\"unknown\",action) ` | - recommended - required for pytest-splunk-addon - prescribed values: ` created ` , ` deleted ` , ` modified ` , ` read ` |
| Registry | ` dest ` | string | The endpoint pertaining to the registry events. Expression: ` if(isnull(dest) OR dest=\"\",\"unknown\",dest) ` | - recommended - required for pytest-splunk-addon |
| Registry | ` dest_bunit ` | string | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Registry | ` dest_category ` | string | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Registry | ` dest_priority ` | string | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Registry | ` dest_requires_av ` | boolean | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Registry | ` dest_should_timesync ` | boolean | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Registry | ` dest_should_update ` | boolean | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Registry | ` image ` | string | The binary file path or name that is tied to a process ID (PID) in events such as process creation or termination. | Optional |
| Registry | ` process_guid ` | string | The globally unique identifier of the process assigned by the vendor_product. |  |
| Registry | ` process_id ` | number | The numeric identifier of the process assigned by the operating system. |  |
| Registry | ` registry_hive ` | string | The logical grouping of registry keys, subkeys, and values. | - required for pytest-splunk-addon - prescribed values: ` HKEY_CURRENT_CONFIG ` , ` HKEY_CURRENT_USER ` , ` HKEY_LOCAL_MACHINE\\SAM ` , ` HKEY_LOCAL_MACHINE\\Security ` , ` HKEY_LOCAL_MACHINE\\Software ` , ` HKEY_LOCAL_MACHINE\\System ` , ` HKEY_USERS\\.DEFAULT ` |
| Registry | ` registry_path ` | string | The path to the registry value, such as \win\directory\directory2\{676235CD-B656-42D5-B737-49856E97D072}\PrinterDriverData. Expression: ` if(isnull(registry_path) OR registry_path=\"\",\"unknown\",registry_path) ` | - recommended - required for pytest-splunk-addon |
| Registry | ` registry_key_name ` | string | The name of the registry key, such as PrinterDriverData. Expression: ` if(isnull(registry_key_name) OR registry_key_name=\"\",\"unknown\", registry_key_name) ` | - recommended - required for pytest-splunk-addon |
| Registry | ` registry_value_data ` | string | The unaltered registry value. Expression: ` if(isnull(registry_value_data) OR registry_value_data=\"\",\"unknown\", registry_value_data) ` | - recommended - required for pytest-splunk-addon |
| Registry | ` registry_value_name ` | string | The name of the registry value. Expression: ` if(isnull(registry_value_name) OR registry_value_name=\"\",\"unknown\", registry_value_name) ` | - recommended - required for pytest-splunk-addon |
| Registry | ` registry_value_text ` | string | The textual representation of registry_value_data (if applicable). | required for pytest-splunk-addon |
| Registry | ` registry_value_type ` | string | The type of the registry value. Expression: ` if(isnull(registry_value_type) OR registry_value_type=\"\",\"unknown\", registry_value_type) ` | - recommended - required for pytest-splunk-addon - prescribed values: ` REG_BINARY ` , ` REG_DWORD ` , ` REG_DWORD_LITTLE_ENDIAN ` , ` REG_DWORD_BIG_ENDIAN ` , ` REG_EXPAND_SZ ` , ` REG_LINK, REG_MULTI_SZ ` , ` REG_NONE ` , ` REG_QWORD ` , ` REG_QWORD_LITTLE_ENDIAN ` , ` REG_SZ ` |
| Registry | ` status ` | string | The outcome of the registry action. | - required for pytest-splunk-addon - prescribed values: ` failure ` , ` success ` |
| Registry | ` tag ` | string | This automatically generated field is used to access tags from within data models. Add-on builders do not need to populate it. |  |
| Registry | ` user ` | string | The user account associated with the registry access. Expression: ` if(isnull(user) OR user=\"\",\"unknown\",user) ` | - recommended - required for pytest-splunk-addon |
| Registry | ` user_bunit ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Registry | ` user_category ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Registry | ` user_priority ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this fields when writing add-ons. |  |
| Registry | ` vendor_product ` | string | The vendor and product name of the Endpoint solution that reported the event, such as Carbon Black Cb Response. This field can be automatically populated by vendor and product fields in your data. Expression: ` case(isnotnull(vendor_product),vendor_product, isnotnull(vendor) AND vendor!=\"unknown\" AND isnotnull(product) AND product!=\"unknown\",vendor.\" \".product,isnotnull(vendor) AND vendor!=\"unknown\" AND (isnull(product) OR product=\"unknown\"),vendor.\" unknown\",(isnull(vendor) OR vendor=\"unknown\") AND isnotnull(product) AND product!=\"unknown\",\"unknown \".product,isnotnull(sourcetype),sourcetype, 1=1,\"unknown\") ` | recommended |

## Search Example

The Endpoint data model is not directly searchable. Searching the Endpoint data model directly may show the following error: "Error in 'DataModelCache': Invalid or unaccelerable root object for datamodel." Instead, search for one or more of the data sets within the Endpoint data model: Endpoint.Ports, Endpoint.Processes, Endpoint.Services, or Endpoint.Filesystem.

An example follows for the new versus old search for summary count of ports by destination port:

Endpoint

`| tstats `summariesonly` count from datamodel=Endpoint.Ports by Ports.dest `

Application State

`| tstats count from datamodel=Application_State.All_Application_State where nodename="All_Application_State.Ports" by All_Application_State.dest `
