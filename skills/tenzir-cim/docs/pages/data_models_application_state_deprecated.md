---
title: Application State (deprecated)
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/application-state-deprecated
last_modified: 2026-04-01T20:48:30.176Z
version: 8.5
---

# Application State (deprecated)

Note: This data model is deprecated as of software version 4.12.0. Use the Endpoint data model instead.

The fields and tags in the Application State data model describe service or process inventory and state, such as Unix daemons, Windows services, running processes on any OS, or similar systems.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with Application State event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| All_Application_State | (listening, port) OR (process, report) OR (service, report) |
| \|____ Ports | listening |
| port |
| \|____ Processes | process |
| report |
| \|____ Services | service |
| report |

## Fields for Application State event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. Note that it does not include any inherited fields. For more information, see How to use these reference tables .

| Dataset name | Field name | Data type | Description | Notes |
| --- | --- | --- | --- | --- |
| All_Application_State | ` dest ` | string | The compute resource where the service is installed. You can alias this from more specific fields, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . | recommended |
| All_Application_State | ` dest_bunit ` | string |  | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| All_Application_State | ` dest_category ` | string |  |  |
| All_Application_State | ` dest_priority ` | string |  |  |
| All_Application_State | ` dest_requires_av ` | boolean |  |  |
| All_Application_State | ` dest_should_timesync ` | boolean |  |  |
| All_Application_State | ` dest_should_update ` | boolean |  |  |
| All_Application_State | ` process ` | string | The name of a process or service file, such as ` sqlsrvr.exe ` or ` httpd ` . Note: This field is not appropriate for service or daemon names, such as ` SQL Server ` or ` Apache Web Server ` . Service or daemon names belong to the ` service ` field (see below). | recommended |
| All_Application_State | ` process_name ` | string | The name of a process. |  |
| All_Application_State | ` tag ` | string | This automatically generated field is used to access tags from within data models. Do not define extractions for this field when writing add-ons. |  |
| All_Application_State | ` user ` | string | The user account the service is running as, such as ` System ` or ` httpdsvc ` . |  |
| All_Application_State | ` user_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| All_Application_State | ` user_category ` | string |
| All_Application_State | ` user_priority ` | string |
| Ports | ` dest_port ` | number | Network ports communicated to by the process, such as 53. | recommended |
| Ports | ` transport ` | string | The network ports listened to by the application process, such as tcp, udp, etc. | recommended |
| Ports | ` transport_dest_port ` | string | Calculated as transport/dest_port, such as tcp/53. |  |
| Processes | ` cpu_load_mhz ` | number | CPU Load in megahertz |  |
| Processes | ` cpu_load_percent ` | number | CPU Load in percent |  |
| Processes | ` cpu_time ` | string | CPU Time |  |
| Processes | ` mem_used ` | number | Memory used in bytes |  |
| Services | ` service ` | string | The name of the service, such as ` SQL Server ` or ` Apache Web Server ` . Note: This field is not appropriate for filenames, such as ` sqlsrvr.exe ` or ` httpd ` . Filenames should belong to the ` process ` field instead. Also, note that field is a string. Use the ` service_id ` field for service ID fields that are integer data types. | recommended |
| Services | ` service_id ` | string | A numeric indicator for a service. | recommended |
| Services | ` start_mode ` | string | The start mode for the service. | ` disabled ` , ` manual ` , ` auto ` . recommended |
| Services | ` status ` | string | The status of the service. | ` critical ` , ` started ` , ` stopped ` , ` warning ` recommended |
