# SMB Activity (4006)

> Server Message Block (SMB) Protocol Activity events report client/server connections sharing resources within the network.


Server Message Block (SMB) Protocol Activity events report client/server connections sharing resources within the network.

* **Category**: Network Activity
* **Extends**: `network_activity`
* **UID**: `4006`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `File Supersede`: The event pertains to file superseded activity (overwritten if it exists and created if not).
  * `2` - `File Open`: The event pertains to file open activity (the file is opened if it exists and fails to open if it doesn’t).
  * `3` - `File Create`: The event pertains to file creation activity (a file is created if it does not exist and fails if it does).
  * `4` - `File Open If`: The event pertains to file open activity (the file is opened if it exists and is created if it doesn’t).
  * `5` - `File Overwrite`: The event pertains to file overwrite activity (the file is opened in a truncated form if it exists and fails if it doesn’t).
  * `6` - `File Overwrite If`: The event pertains to file overwrite activity (the file is opened in a truncated form if it exists and created otherwise)
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
  * `4006` - `SMB Activity`: Server Message Block (SMB) Protocol Activity events report client/server connections sharing resources within the network.

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

  * `400600` - `SMB Activity: Unknown`
  * `400601` - `SMB Activity: File Supersede`: The event pertains to file superseded activity (overwritten if it exists and created if not).
  * `400602` - `SMB Activity: File Open`: The event pertains to file open activity (the file is opened if it exists and fails to open if it doesn’t).
  * `400603` - `SMB Activity: File Create`: The event pertains to file creation activity (a file is created if it does not exist and fails if it does).
  * `400604` - `SMB Activity: File Open If`: The event pertains to file open activity (the file is opened if it exists and is created if it doesn’t).
  * `400605` - `SMB Activity: File Overwrite`: The event pertains to file overwrite activity (the file is opened in a truncated form if it exists and fails if it doesn’t).
  * `400606` - `SMB Activity: File Overwrite If`: The event pertains to file overwrite activity (the file is opened in a truncated form if it exists and created otherwise)
  * `400699` - `SMB Activity: Other`

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

The event class name, as defined by class\_uid value: `SMB Activity`.

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

**`client_dialects`**

* **Type**: `string_t`
* **Requirement**: recommended

The list of SMB dialects that the client speaks.

**`dialect`**

* **Type**: `string_t`
* **Requirement**: recommended

The negotiated protocol dialect.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`app_name`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the application that is associated with the event or object.

**`dce_rpc`**

* **Type**: [`dce_rpc`](../objects/dce_rpc.md)
* **Requirement**: optional

The DCE/RPC object describes the remote procedure call system for distributed computing environments.

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

**`command`**

* **Type**: `string_t`
* **Requirement**: recommended

The command name (e.g. SMB2\_COMMAND\_CREATE, SMB1\_COMMAND\_WRITE\_ANDX).

**`connection_info`**

* **Type**: [`network_connection_info`](../objects/network_connection_info.md)
* **Requirement**: recommended

The network connection information.

**`device`** [host](../profiles/host.md)

* **Type**: [`device`](../objects/device.md)
* **Requirement**: recommended

An addressable device, computer system or host.

**`file`**

* **Type**: [`file`](../objects/file.md)
* **Requirement**: recommended

The file that is the target of the SMB activity.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event, as defined by the event source.

**`open_type`**

* **Type**: `string_t`
* **Requirement**: recommended

Indicates how the file was opened (e.g. normal, delete on close).

**`response`**

* **Type**: [`response`](../objects/response.md)
* **Requirement**: recommended

The server response in an SMB network connection.

**`share_type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The share type is not known.
  * `1` - `File`
  * `2` - `Pipe`
  * `3` - `Print`
  * `99` - `Other`: The share type is not mapped.

The normalized identifier of the SMB share type.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`
  * `1` - `Success`
  * `2` - `Failure`
  * `99` - `Other`: The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

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

**`share`**

* **Type**: `string_t`
* **Requirement**: optional

The SMB share name.

**`share_type`**

* **Type**: `string_t`
* **Requirement**: optional

The SMB share type, normalized to the caption of the share\_type\_id value. In the case of ‘Other’, it is defined by the event source.

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

**`tree_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The tree id is a unique SMB identifier which represents an open connection to a share.

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`attack`](../objects/attack.md)
* [`cloud`](../objects/cloud.md)
* [`dce_rpc`](../objects/dce_rpc.md)
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`file`](../objects/file.md)
* [`malware`](../objects/malware.md)
* [`metadata`](../objects/metadata.md)
* [`network_connection_info`](../objects/network_connection_info.md)
* [`network_endpoint`](../objects/network_endpoint.md)
* [`network_proxy`](../objects/network_proxy.md)
* [`network_traffic`](../objects/network_traffic.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`response`](../objects/response.md)
* [`tls`](../objects/tls.md)