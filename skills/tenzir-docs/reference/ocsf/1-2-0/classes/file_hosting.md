# File Hosting Activity (6006)

> File Hosting Activity events report the actions taken by file management applications, including file sharing servers like Sharepoint and services such as Box, MS OneDrive, or Google Drive.


File Hosting Activity events report the actions taken by file management applications, including file sharing servers like Sharepoint and services such as Box, MS OneDrive, or Google Drive.

* **Category**: Application Activity
* **Extends**: `application`
* **UID**: `6006`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Upload`: Upload a file.
  * `2` - `Download`: Download a file.
  * `3` - `Update`: Update a file.
  * `4` - `Delete`: Delete a file.
  * `5` - `Rename`: Rename a file.
  * `6` - `Copy`: Copy a file.
  * `7` - `Move`: Move a file.
  * `8` - `Restore`: Restore a file.
  * `9` - `Preview`: Preview a file.
  * `10` - `Lock`: Lock a file.
  * `11` - `Unlock`: Unlock a file.
  * `12` - `Share`: Share a file.
  * `13` - `Unshare`: Unshare a file.
  * `14` - `Open`: Open a file.
  * `15` - `Sync`: Mark a file or folder to sync with a computer.
  * `16` - `Unsync`: Mark a file or folder to not sync with a computer.
  * `99` - `Other`: The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

**`category_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `6` - `Application Activity`: Application Activity events report detailed information about the behavior of applications and services.

The category unique identifier of the event.

**`class_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `6006` - `File Hosting Activity`: File Hosting Activity events report the actions taken by file management applications, including file sharing servers like Sharepoint and services such as Box, MS OneDrive, or Google Drive.

The unique identifier of a class. A class describes the attributes available in an event.

**`severity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event/finding severity is unknown.
  * `1` - `Informational`: Informational message. No action required.
  * `2` - `Low`: The user decides if action is needed.
  * `3` - `Medium`: Action is required but the situation is not serious at this time.
  * `4` - `High`: Action is required immediately.
  * `5` - `Critical`: Action is required immediately and the scope is broad.
  * `6` - `Fatal`: An error occurred but it is too late to take remedial action.
  * `99` - `Other`: The event/finding severity is not mapped. See the `severity` attribute, which contains a data source specific value.

The normalized identifier of the event/finding severity.The normalized severity is a measurement the effort and expense required to manage and resolve an event or incident. Smaller numerical values represent lower impact events, and larger numerical values represent higher impact events.

**`type_uid`**

* **Type**: `long_t`

* **Requirement**: required

* **Values**:

  * `600600` - `File Hosting Activity: Unknown`
  * `600601` - `File Hosting Activity: Upload`: Upload a file.
  * `600602` - `File Hosting Activity: Download`: Download a file.
  * `600603` - `File Hosting Activity: Update`: Update a file.
  * `600604` - `File Hosting Activity: Delete`: Delete a file.
  * `600605` - `File Hosting Activity: Rename`: Rename a file.
  * `600606` - `File Hosting Activity: Copy`: Copy a file.
  * `600607` - `File Hosting Activity: Move`: Move a file.
  * `600608` - `File Hosting Activity: Restore`: Restore a file.
  * `600609` - `File Hosting Activity: Preview`: Preview a file.
  * `600610` - `File Hosting Activity: Lock`: Lock a file.
  * `600611` - `File Hosting Activity: Unlock`: Unlock a file.
  * `600612` - `File Hosting Activity: Share`: Share a file.
  * `600613` - `File Hosting Activity: Unshare`: Unshare a file.
  * `600614` - `File Hosting Activity: Open`: Open a file.
  * `600615` - `File Hosting Activity: Sync`: Mark a file or folder to sync with a computer.
  * `600616` - `File Hosting Activity: Unsync`: Mark a file or folder to not sync with a computer.
  * `600699` - `File Hosting Activity: Other`

The event/finding type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

**`activity_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event activity name, as defined by the activity\_id.

**`category_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event category name, as defined by category\_uid value: `Application Activity`.

**`class_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event class name, as defined by class\_uid value: `File Hosting Activity`.

**`severity`**

* **Type**: `string_t`
* **Requirement**: optional

The event/finding severity, normalized to the caption of the severity\_id value. In the case of ‘Other’, it is defined by the source.

**`type_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event/finding type name, as defined by the type\_uid.

### Context

**`metadata`**

* **Type**: [`metadata`](../objects/metadata.md)
* **Requirement**: required

The metadata associated with the event or a finding.

**`dst_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: recommended

The endpoint that received the activity on the target file.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`connection_info`**

* **Type**: [`network_connection_info`](../objects/network_connection_info.md)
* **Requirement**: optional

The network connection information.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event or a finding. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`expiration_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The share expiration time.

**`expiration_time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The share expiration time.

**`raw_data`**

* **Type**: `string_t`
* **Requirement**: optional

The raw event/finding data as received from the source.

**`unmapped`**

* **Type**: [`object`](../objects/object.md)
* **Requirement**: optional

The attributes that are not mapped to the event schema. The names and values of those attributes are specific to the event source.

### Occurrence

**`time`**

* **Type**: `timestamp_t`
* **Requirement**: required

The normalized event occurrence time or the finding creation time.

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

The normalized event occurrence time or the finding creation time.

### Primary

**`actor`**

* **Type**: [`actor`](../objects/actor.md)
* **Requirement**: required

The actor that performed the activity on the target file.

**`cloud`** [cloud](../profiles/cloud.md)

* **Type**: [`cloud`](../objects/cloud.md)
* **Requirement**: required

Describes details about the Cloud environment where the event was originally created or logged.

**`file`**

* **Type**: [`file`](../objects/file.md)
* **Requirement**: required

The file that is the target of the activity.

**`src_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: required

The endpoint that performed the activity on the target file.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event/finding, as defined by the source.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: recommended

The observables associated with the event or a finding.

**`status`**

* **Type**: `string_t`
* **Requirement**: recommended

The event status, normalized to the caption of the status\_id value. In the case of ‘Other’, it is defined by the event source.

**`status_code`**

* **Type**: `string_t`
* **Requirement**: recommended

The event status code, as reported by the event source.

For example, in a Windows Failed Authentication event, this would be the value of ‘Failure Code’, e.g. 0x18.

**`status_detail`**

* **Type**: `string_t`
* **Requirement**: recommended

The status details contains additional information about the event/finding outcome.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The status is unknown.
  * `1` - `Success`
  * `2` - `Failure`
  * `99` - `Other`: The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`cloud`](../objects/cloud.md)
* [`enrichment`](../objects/enrichment.md)
* [`file`](../objects/file.md)
* [`metadata`](../objects/metadata.md)
* [`network_connection_info`](../objects/network_connection_info.md)
* [`network_endpoint`](../objects/network_endpoint.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)