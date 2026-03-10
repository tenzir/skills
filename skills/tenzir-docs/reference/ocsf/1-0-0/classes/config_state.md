# Device Config State (5002)

> Device Config State events report device configuration data.


Device Config State events report device configuration data.

* **Category**: Discovery
* **Extends**: `discovery`
* **UID**: `5002`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Log`: The discovered information is via a log.
  * `2` - `Collect`: The discovered information is via a collection process.
  * `99` - `Other`: The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

**`category_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `5` - `Discovery`: Discovery events report the existence and state of devices, files, configurations, processes, registry keys, and other objects.

The category unique identifier of the event.

**`class_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `5002` - `Device Config State`: Device Config State events report device configuration data.

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

  * `500200` - `Device Config State: Unknown`
  * `500201` - `Device Config State: Log`: The discovered information is via a log.
  * `500202` - `Device Config State: Collect`: The discovered information is via a collection process.
  * `500299` - `Device Config State: Other`

The event type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

**`activity_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event activity name, as defined by the activity\_id.

**`category_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event category name, as defined by category\_uid value: `Discovery`.

**`class_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event class name, as defined by class\_uid value: `Device Config State`.

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

**`actor`**

* **Type**: [`actor`](../objects/actor.md)
* **Requirement**: optional

The actor object describes details about the user/role/process that was the source of the activity.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

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

**`device`**

* **Type**: [`device`](../objects/device.md)
* **Requirement**: required

The device that is being discovered by an inventory process.

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

**`cis_benchmark_result`**

* **Type**: [`cis_benchmark_result`](../objects/cis_benchmark_result.md)
* **Requirement**: optional

The CIS benchmark result.

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
* [`cis_benchmark_result`](../objects/cis_benchmark_result.md)
* [`cloud`](../objects/cloud.md)
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`metadata`](../objects/metadata.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)