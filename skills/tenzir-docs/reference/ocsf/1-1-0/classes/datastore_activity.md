# Datastore Activity (6005)

> Datastore events describe general activities (Read, Update, Query, Delete, etc.) which affect datastores or data within those datastores, e.g. (AWS RDS, AWS S3).


Datastore events describe general activities (Read, Update, Query, Delete, etc.) which affect datastores or data within those datastores, e.g. (AWS RDS, AWS S3).

* **Category**: Application Activity
* **Extends**: `application`
* **UID**: `6005`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Read`: The datastore activity in the event pertains to a ‘Read’ operation.
  * `2` - `Update`: The datastore activity in the event pertains to a ‘Update’ operation.
  * `3` - `Connect`: The datastore activity in the event pertains to a ‘Connect’ operation.
  * `4` - `Query`: The datastore activity in the event pertains to a ‘Query’ operation.
  * `5` - `Write`: The datastore activity in the event pertains to a ‘Write’ operation.
  * `6` - `Create`: The datastore activity in the event pertains to a ‘Create’ operation.
  * `7` - `Delete`: The datastore activity in the event pertains to a ‘Delete’ operation.
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
  * `6005` - `Datastore Activity`: Datastore events describe general activities (Read, Update, Query, Delete, etc.) which affect datastores or data within those datastores, e.g. (AWS RDS, AWS S3).

The unique identifier of a class. A Class describes the attributes available in an event.

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

  * `600500` - `Datastore Activity: Unknown`
  * `600501` - `Datastore Activity: Read`: The datastore activity in the event pertains to a ‘Read’ operation.
  * `600502` - `Datastore Activity: Update`: The datastore activity in the event pertains to a ‘Update’ operation.
  * `600503` - `Datastore Activity: Connect`: The datastore activity in the event pertains to a ‘Connect’ operation.
  * `600504` - `Datastore Activity: Query`: The datastore activity in the event pertains to a ‘Query’ operation.
  * `600505` - `Datastore Activity: Write`: The datastore activity in the event pertains to a ‘Write’ operation.
  * `600506` - `Datastore Activity: Create`: The datastore activity in the event pertains to a ‘Create’ operation.
  * `600507` - `Datastore Activity: Delete`: The datastore activity in the event pertains to a ‘Delete’ operation.
  * `600599` - `Datastore Activity: Other`

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

The event class name, as defined by class\_uid value: `Datastore Activity`.

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

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The datastore resource type is unknown.
  * `1` - `Database`
  * `2` - `Databucket`
  * `3` - `Table`
  * `99` - `Other`: The datastore resource type is not mapped.

The normalized datastore resource type identifier.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event or a finding. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`raw_data`**

* **Type**: `string_t`
* **Requirement**: optional

The raw event/finding data as received from the source.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The datastore resource type (e.g. database, datastore, or table).

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

The actor object describes details about the user/role/process that was the source of the activity.

**`cloud`** [cloud](../profiles/cloud.md)

* **Type**: [`cloud`](../objects/cloud.md)
* **Requirement**: required

Describes details about the Cloud environment where the event was originally created or logged.

**`src_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: required

Details about the source of the activity.

**`database`**

* **Type**: [`database`](../objects/database.md)
* **Requirement**: recommended

The database object is used for databases which are typically datastore services that contain an organized collection of structured and unstructured data or a types of data.

**`databucket`**

* **Type**: [`databucket`](../objects/databucket.md)
* **Requirement**: recommended

The data bucket object is a basic container that holds data, typically organized through the use of data partitions.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event/finding, as defined by the source.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The status is unknown.
  * `1` - `Success`
  * `2` - `Failure`
  * `99` - `Other`: The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

**`dst_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: optional

Details about the endpoint hosting the datastore application or service.

**`http_request`**

* **Type**: [`http_request`](../objects/http_request.md)
* **Requirement**: optional

Details about the underlying http request.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: optional

The observables associated with the event or a finding.

**`query_info`**

* **Type**: [`query_info`](../objects/query_info.md)
* **Requirement**: optional

The query info object holds information related to data access within a datastore. To access, manipulate, delete, or retrieve data from a datastore, a database query must be written using a specific syntax.

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

The status details contains additional information about the event/finding outcome.

**`table`**

* **Type**: [`table`](../objects/table.md)
* **Requirement**: optional

The table object represents a table within a structured relational database or datastore, which contains columns and rows of data that are able to be create, updated, deleted and queried.

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`cloud`](../objects/cloud.md)
* [`database`](../objects/database.md)
* [`databucket`](../objects/databucket.md)
* [`enrichment`](../objects/enrichment.md)
* [`http_request`](../objects/http_request.md)
* [`metadata`](../objects/metadata.md)
* [`network_endpoint`](../objects/network_endpoint.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`query_info`](../objects/query_info.md)
* [`table`](../objects/table.md)