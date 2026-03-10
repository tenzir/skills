# File System Activity (1001)

> File System Activity events report when a process performs an action on a file or folder.


File System Activity events report when a process performs an action on a file or folder.

* **Category**: System Activity
* **Extends**: `system`
* **UID**: `1001`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Create`: A request to create a new file on a file system.
  * `2` - `Read`: A request to read data from a file on a file system.
  * `3` - `Update`: A request to write data to a file on a file system.
  * `4` - `Delete`: A request to delete a file on a file system.
  * `5` - `Rename`: A request to rename a file on a file system.
  * `6` - `Set Attributes`: A request to set attributes for a file on a file system.
  * `7` - `Set Security`: A request to set security for a file on a file system.
  * `8` - `Get Attributes`: A request to get attributes for a file on a file system.
  * `9` - `Get Security`: A request to get security for a file on a file system.
  * `10` - `Encrypt`: A request to encrypt a file on a file system.
  * `11` - `Decrypt`: A request to decrypt a file on a file system.
  * `12` - `Mount`: A request to mount a file on a file system.
  * `13` - `Unmount`: A request to unmount a file from a file system.
  * `14` - `Open`: A request to create a file handle.
  * `99` - `Other`: The event activity is not mapped.

The activity ID of the event.

**`category_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `1` - `System Activity`: System Activity events.

The category unique identifier of the event.

**`class_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `1001` - `File System Activity`: File System Activity events report when a process performs an action on a file or folder.

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

  * `100100` - `File System Activity: Unknown`
  * `100101` - `File System Activity: Create`: A request to create a new file on a file system.
  * `100102` - `File System Activity: Read`: A request to read data from a file on a file system.
  * `100103` - `File System Activity: Update`: A request to write data to a file on a file system.
  * `100104` - `File System Activity: Delete`: A request to delete a file on a file system.
  * `100105` - `File System Activity: Rename`: A request to rename a file on a file system.
  * `100106` - `File System Activity: Set Attributes`: A request to set attributes for a file on a file system.
  * `100107` - `File System Activity: Set Security`: A request to set security for a file on a file system.
  * `100108` - `File System Activity: Get Attributes`: A request to get attributes for a file on a file system.
  * `100109` - `File System Activity: Get Security`: A request to get security for a file on a file system.
  * `100110` - `File System Activity: Encrypt`: A request to encrypt a file on a file system.
  * `100111` - `File System Activity: Decrypt`: A request to decrypt a file on a file system.
  * `100112` - `File System Activity: Mount`: A request to mount a file on a file system.
  * `100113` - `File System Activity: Unmount`: A request to unmount a file from a file system.
  * `100114` - `File System Activity: Open`: A request to create a file handle.
  * `100199` - `File System Activity: Other`

The event type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

**`activity_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event activity name, as defined by the activity\_id.

**`category_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event category name, as defined by category\_uid value: `System Activity`.

**`class_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event class name, as defined by class\_uid value: `File System Activity`.

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

**`access_mask`**

* **Type**: `integer_t`
* **Requirement**: optional

The access mask in a platform-native format.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`connection_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The network connection identifier.

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

**`actor`**

* **Type**: [`actor`](../objects/actor.md)
* **Requirement**: required

The actor that performed the activity on the `file` object

**`cloud`** [cloud](../profiles/cloud.md)

* **Type**: [`cloud`](../objects/cloud.md)
* **Requirement**: required

Describes details about the Cloud environment where the event was originally created or logged.

**`device`**

* **Type**: [`device`](../objects/device.md)
* **Requirement**: required

An addressable device, computer system or host.

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

**`file`**

* **Type**: [`file`](../objects/file.md)
* **Requirement**: required

The file that is the target of the activity.

**`attacks`** [security\_control](../profiles/security_control.md)

* **Type**: [`attack`](../objects/attack.md)
* **Requirement**: recommended

An array of attacks associated with an event.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event, as defined by the event source.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`
  * `1` - `Success`
  * `2` - `Failure`
  * `99` - `Other`: The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

**`component`**

* **Type**: `string_t`
* **Requirement**: optional

The name or relative pathname of a sub-component of the data object, if applicable. For example: `attachment.doc`, `attachment.zip/bad.doc`, or `part.mime/part.cab/part.uue/part.doc`.

**`create_mask`**

* **Type**: `string_t`
* **Requirement**: optional

The original Windows mask that is required to create the object.

**`disposition`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

The event disposition name, normalized to the caption of the disposition\_id value. In the case of ‘Other’, it is defined by the event source.

**`file_diff`**

* **Type**: `string_t`
* **Requirement**: optional

File content differences used for change detection. For example, a common use case is to identify itemized changes within INI or configuration/property setting values.

**`file_result`**

* **Type**: [`file`](../objects/file.md)
* **Requirement**: optional

The resulting file object when the activity was allowed and successful.

**`malware`** [security\_control](../profiles/security_control.md)

* **Type**: [`malware`](../objects/malware.md)
* **Requirement**: optional

The list of malware identified by a finding.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: optional

The observables associated with the event.

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

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`attack`](../objects/attack.md)
* [`cloud`](../objects/cloud.md)
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`file`](../objects/file.md)
* [`malware`](../objects/malware.md)
* [`metadata`](../objects/metadata.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)