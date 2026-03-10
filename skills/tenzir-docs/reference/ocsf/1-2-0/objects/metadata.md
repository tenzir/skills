# Metadata

> The Metadata object describes the metadata associated with the event.


The Metadata object describes the metadata associated with the event. Defined by D3FEND [d3f:Metadata](https://d3fend.mitre.org/dao/artifact/d3f:Metadata/).

## Attributes

**`product`**

* **Type**: [`product`](product.md)
* **Requirement**: required

The product that reported the event.

**`version`**

* **Type**: `string_t`
* **Requirement**: required

The version of the OCSF schema, using Semantic Versioning Specification ([SemVer](https://semver.org)). For example: 1.0.0. Event consumers use the version to determine the available event attributes.

**`data_classification`**

* **Type**: [`data_classification`](data_classification.md)
* **Requirement**: recommended

The Data Classification object includes information about data classification levels and data category types.

**`log_name`**

* **Type**: `string_t`
* **Requirement**: recommended

The event log name. For example, syslog file name or Windows logging subsystem: Security.

**`log_provider`**

* **Type**: `string_t`
* **Requirement**: recommended

The logging provider or logging service that logged the event. For example, Microsoft-Windows-Security-Auditing.

**`original_time`**

* **Type**: `string_t`
* **Requirement**: recommended

The original event time as reported by the event source. For example, the time in the original format from system event log such as Syslog on Unix/Linux and the System event file on Windows. Omit if event is generated instead of collected via logs.

**`tenant_uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique tenant identifier.

**`correlation_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier used to correlate events.

**`event_code`**

* **Type**: `string_t`
* **Requirement**: optional

The Event ID or Code that the product uses to describe the event.

**`extension`**

* **Type**: [`extension`](extension.md)
* **Requirement**: optional

The schema extension used to create the event.

**`extensions`**

* **Type**: [`extension`](extension.md)
* **Requirement**: optional

The schema extensions used to create the event.

**`labels`**

* **Type**: `string_t`
* **Requirement**: optional

The list of category labels attached to the event or specific attributes. Labels are user defined tags or aliases added at normalization time.For example: `["network", "connection.ip:destination", "device.ip:source"]`

**`log_level`**

* **Type**: `string_t`
* **Requirement**: optional

The audit level at which an event was generated.

**`log_version`**

* **Type**: `string_t`
* **Requirement**: optional

The event log schema version that specifies the format of the original event. For example syslog version or Cisco Log Schema Version.

**`logged_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the logging system collected and logged the event.This attribute is distinct from the event time in that event time typically contain the time extracted from the original event. Most of the time, these two times will be different.

**`logged_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the logging system collected and logged the event.This attribute is distinct from the event time in that event time typically contain the time extracted from the original event. Most of the time, these two times will be different.

**`loggers`**

* **Type**: [`logger`](logger.md)
* **Requirement**: optional

An array of Logger objects that describe the devices and logging products between the event source and its eventual destination. Note, this attribute can be used when there is a complex end-to-end path of event flow.

**`modified_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the event was last modified or enriched.

**`modified_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the event was last modified or enriched.

**`processed_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The event processed time, such as an ETL operation.

**`processed_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The event processed time, such as an ETL operation.

**`profiles`**

* **Type**: `string_t`
* **Requirement**: optional

The list of profiles used to create the event.

**`sequence`**

* **Type**: `integer_t`
* **Requirement**: optional

Sequence number of the event. The sequence number is a value available in some events, to make the exact ordering of events unambiguous, regardless of the event time precision.

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

The logging system-assigned unique identifier of an event instance.

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
* [`file_activity`](../classes/file_activity.md)
* [`file_hosting`](../classes/file_hosting.md)
* [`file_query`](../classes/file_query.md)
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
* [`networks_query`](../classes/networks_query.md)
* [`ntp_activity`](../classes/ntp_activity.md)
* [`patch_state`](../classes/patch_state.md)
* [`peripheral_device_query`](../classes/peripheral_device_query.md)
* [`process_activity`](../classes/process_activity.md)
* [`process_query`](../classes/process_query.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`scan_activity`](../classes/scan_activity.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)
* [`security_finding`](../classes/security_finding.md)
* [`service_query`](../classes/service_query.md)
* [`session_query`](../classes/session_query.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`user_access`](../classes/user_access.md)
* [`user_inventory`](../classes/user_inventory.md)
* [`user_query`](../classes/user_query.md)
* [`vulnerability_finding`](../classes/vulnerability_finding.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)