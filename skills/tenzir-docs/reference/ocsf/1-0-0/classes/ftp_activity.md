# FTP Activity (4008)

> File Transfer Protocol (FTP) Activity events report file transfers between a server and a client as seen on the network.


File Transfer Protocol (FTP) Activity events report file transfers between a server and a client as seen on the network.

* **Category**: Network Activity
* **Extends**: `network_activity`
* **UID**: `4008`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Put`: File upload to the FTP or SFTP site.
  * `2` - `Get`: File download from the FTP or SFTP site.
  * `3` - `Poll`: Poll directory for specific file(s) or folder(s) at the FTP or SFTP site location.
  * `4` - `Delete`: Delete file(s) from the FTP or SFTP site.
  * `5` - `Rename`: Rename the file(s) in the FTP or SFTP site.
  * `6` - `List`: List files in a specified directory.
  * `99` - `Other`: The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

**`category_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `4` - `Network Activity`: Network Activity events.

The category unique identifier of the event.

**`class_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `4008` - `FTP Activity`: File Transfer Protocol (FTP) Activity events report file transfers between a server and a client as seen on the network.

The unique identifier of a class. A Class describes the attributes available in an event.

**`severity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event severity is not known.
  * `1` - `Informational`: Informational message. No action required.
  * `2` - `Low`: The user decides if action is needed.
  * `3` - `Medium`: Action is required but the situation is not serious at this time.
  * `4` - `High`: Action is required immediately.
  * `5` - `Critical`: Action is required immediately and the scope is broad.
  * `6` - `Fatal`: An error occurred but it is too late to take remedial action.
  * `99` - `Other`: The event severity is not mapped. See the `severity` attribute, which contains a data source specific value.

The normalized identifier of the event severity.The normalized severity is a measurement the effort and expense required to manage and resolve an event or incident. Smaller numerical values represent lower impact events, and larger numerical values represent higher impact events.

**`type_uid`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `400800` - `FTP Activity: Unknown`
  * `400801` - `FTP Activity: Put`: File upload to the FTP or SFTP site.
  * `400802` - `FTP Activity: Get`: File download from the FTP or SFTP site.
  * `400803` - `FTP Activity: Poll`: Poll directory for specific file(s) or folder(s) at the FTP or SFTP site location.
  * `400804` - `FTP Activity: Delete`: Delete file(s) from the FTP or SFTP site.
  * `400805` - `FTP Activity: Rename`: Rename the file(s) in the FTP or SFTP site.
  * `400806` - `FTP Activity: List`: List files in a specified directory.
  * `400899` - `FTP Activity: Other`

The event type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

**`activity_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event activity name, as defined by the activity\_id.

**`category_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event category name, as defined by category\_uid value: `Network Activity`.

**`class_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event class name, as defined by class\_uid value: `FTP Activity`.

**`severity`**

* **Type**: `string_t`
* **Requirement**: optional

The event severity, normalized to the caption of the severity\_id value. In the case of ‘Other’, it is defined by the event source.

**`type_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event type name, as defined by the type\_uid.

### Context

**`metadata`**

* **Type**: [`metadata`](../objects/metadata.md)
* **Requirement**: required

The metadata associated with the event.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`app_name`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the application that is associated with the event or object.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`raw_data`**

* **Type**: `string_t`
* **Requirement**: optional

The event data as received from the event source.

**`unmapped`**

* **Type**: [`object`](../objects/object.md)
* **Requirement**: optional

The attributes that are not mapped to the event schema. The names and values of those attributes are specific to the event source.

### Occurrence

**`time`**

* **Type**: `timestamp_t`
* **Requirement**: required

The normalized event occurrence time.

**`timezone_offset`**

* **Type**: `integer_t`
* **Requirement**: recommended

The number of minutes that the reported event `time` is ahead or behind UTC, in the range -1,080 to +1,080.

**`count`**

* **Type**: `integer_t`
* **Requirement**: optional

The number of times that events in the same logical group occurred during the event Start Time to End Time period.

**`duration`**

* **Type**: `integer_t`
* **Requirement**: optional

The event duration or aggregate time, the amount of time the event covers from `start_time` to `end_time` in milliseconds.

**`end_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The end time of a time period, or the time of the most recent event included in the aggregate event.

**`end_time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The end time of a time period, or the time of the most recent event included in the aggregate event.

**`start_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The start time of a time period, or the time of the least recent event included in the aggregate event.

**`start_time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The start time of a time period, or the time of the least recent event included in the aggregate event.

**`time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The normalized event occurrence time.

### Primary

**`cloud`** [cloud](../profiles/cloud.md)

* **Type**: [`cloud`](../objects/cloud.md)
* **Requirement**: required

Describes details about the Cloud environment where the event was originally created or logged.

**`disposition_id`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`
  * `1` - `Allowed`
  * `2` - `Blocked`
  * `3` - `Quarantined`
  * `4` - `Isolated`
  * `5` - `Deleted`
  * `6` - `Dropped`
  * `7` - `Custom Action`: Executed custom action such as run a command script.
  * `8` - `Approved`
  * `9` - `Restored`
  * `10` - `Exonerated`: No longer suspicious (re-scored).
  * `11` - `Corrected`
  * `12` - `Partially Corrected`
  * `13` - `Uncorrected`
  * `14` - `Delayed`: Requires reboot to finish the operation.
  * `15` - `Detected`
  * `16` - `No Action`
  * `17` - `Logged`
  * `18` - `Tagged`: Marked with extended attributes.
  * `99` - `Other`

When security issues, such as malware or policy violations, are detected and possibly corrected, then `disposition_id` describes the action taken by the security product.

**`dst_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: required

The responder (server) in a network connection.

**`src_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: required

The initiator (client) of the network connection.

**`attacks`** [security\_control](../profiles/security_control.md)

* **Type**: [`attack`](../objects/attack.md)
* **Requirement**: recommended

An array of attacks associated with an event.

**`codes`**

* **Type**: `integer_t`
* **Requirement**: recommended

The list of return codes to the FTP command.

**`command`**

* **Type**: `string_t`
* **Requirement**: recommended

The FTP command.

**`command_responses`**

* **Type**: `string_t`
* **Requirement**: recommended

The list of responses to the FTP command.

**`connection_info`**

* **Type**: [`network_connection_info`](../objects/network_connection_info.md)
* **Requirement**: recommended

The network connection information.

**`device`** [host](../profiles/host.md)

* **Type**: [`device`](../objects/device.md)
* **Requirement**: recommended

An addressable device, computer system or host.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event, as defined by the event source.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the data affiliated with the command.

**`port`**

* **Type**: `port_t`
* **Requirement**: recommended

The dynamic port established for impending data transfers.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`
  * `1` - `Success`
  * `2` - `Failure`
  * `99` - `Other`: The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The type of FTP network connection (e.g. active, passive).

**`actor`** [host](../profiles/host.md)

* **Type**: [`actor`](../objects/actor.md)
* **Requirement**: optional

The actor object describes details about the user/role/process that was the source of the activity.

**`disposition`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

The event disposition name, normalized to the caption of the disposition\_id value. In the case of ‘Other’, it is defined by the event source.

**`malware`** [security\_control](../profiles/security_control.md)

* **Type**: [`malware`](../objects/malware.md)
* **Requirement**: optional

The list of malware identified by a finding.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: optional

The observables associated with the event.

**`proxy`**

* **Type**: [`network_proxy`](../objects/network_proxy.md)
* **Requirement**: optional

If a proxy connection is present, the connection from the client to the proxy server.

**`status`**

* **Type**: `string_t`
* **Requirement**: optional

The event status, normalized to the caption of the status\_id value. In the case of ‘Other’, it is defined by the event source.

**`status_code`**

* **Type**: `string_t`
* **Requirement**: optional

The event status code, as reported by the event source.

For example, in a Windows Failed Authentication event, this would be the value of ‘Failure Code’, e.g. 0x18.

**`status_detail`**

* **Type**: `string_t`
* **Requirement**: optional

The status details contains additional information about the event outcome.

**`tls`**

* **Type**: [`tls`](../objects/tls.md)
* **Requirement**: optional

The Transport Layer Security (TLS) attributes.

**`traffic`**

* **Type**: [`network_traffic`](../objects/network_traffic.md)
* **Requirement**: optional

The network traffic refers to the amount of data moving across a network at a given point of time. Intended to be used alongside Network Connection.

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`attack`](../objects/attack.md)
* [`cloud`](../objects/cloud.md)
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`malware`](../objects/malware.md)
* [`metadata`](../objects/metadata.md)
* [`network_connection_info`](../objects/network_connection_info.md)
* [`network_endpoint`](../objects/network_endpoint.md)
* [`network_proxy`](../objects/network_proxy.md)
* [`network_traffic`](../objects/network_traffic.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`tls`](../objects/tls.md)