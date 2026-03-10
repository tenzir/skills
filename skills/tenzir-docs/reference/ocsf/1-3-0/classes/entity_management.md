# Entity Management (3004)

> Entity Management events report activity by a managed client, a micro service, or a user at a management console.


Entity Management events report activity by a managed client, a micro service, or a user at a management console. The activity can be a create, read, update, and delete operation on a managed entity.

* **Category**: Identity & Access Management
* **Extends**: `iam`
* **UID**: `3004`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Create`: Create a new managed entity.
  * `2` - `Read`: Read an existing managed entity.
  * `3` - `Update`: Update an existing managed entity.
  * `4` - `Delete`: Delete a managed entity.
  * `5` - `Move`: Move or rename an existing managed entity.
  * `6` - `Enroll`: Enroll an existing managed entity.
  * `7` - `Unenroll`: Unenroll an existing managed entity.
  * `8` - `Enable`: Enable an existing managed entity. Note: This is typically regarded as a semi-permanent, editor visible, syncable change.
  * `9` - `Disable`: Disable an existing managed entity. Note: This is typically regarded as a semi-permanent, editor visible, syncable change.
  * `10` - `Activate`: Activate an existing managed entity. Note: This is a typically regarded as a transient change, a change of state of the engine.
  * `11` - `Deactivate`: Deactivate an existing managed entity. Note: This is a typically regarded as a transient change, a change of state of the engine.
  * `12` - `Suspend`: Suspend an existing managed entity.
  * `13` - `Resume`: Resume (unsuspend) an existing managed entity.
  * `99` - `Other`: The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

**`category_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `3` - `Identity & Access Management`: Identity & Access Management (IAM) events relate to the supervision of the system’s authentication and access control model. Examples of such events are the success or failure of authentication, granting of authority, password change, entity change, privileged use etc.

The category unique identifier of the event.

**`class_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `3004` - `Entity Management`: Entity Management events report activity by a managed client, a micro service, or a user at a management console. The activity can be a create, read, update, and delete operation on a managed entity.

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

  * `300400` - `Entity Management: Unknown`
  * `300401` - `Entity Management: Create`: Create a new managed entity.
  * `300402` - `Entity Management: Read`: Read an existing managed entity.
  * `300403` - `Entity Management: Update`: Update an existing managed entity.
  * `300404` - `Entity Management: Delete`: Delete a managed entity.
  * `300405` - `Entity Management: Move`: Move or rename an existing managed entity.
  * `300406` - `Entity Management: Enroll`: Enroll an existing managed entity.
  * `300407` - `Entity Management: Unenroll`: Unenroll an existing managed entity.
  * `300408` - `Entity Management: Enable`: Enable an existing managed entity. Note: This is typically regarded as a semi-permanent, editor visible, syncable change.
  * `300409` - `Entity Management: Disable`: Disable an existing managed entity. Note: This is typically regarded as a semi-permanent, editor visible, syncable change.
  * `300410` - `Entity Management: Activate`: Activate an existing managed entity. Note: This is a typically regarded as a transient change, a change of state of the engine.
  * `300411` - `Entity Management: Deactivate`: Deactivate an existing managed entity. Note: This is a typically regarded as a transient change, a change of state of the engine.
  * `300412` - `Entity Management: Suspend`: Suspend an existing managed entity.
  * `300413` - `Entity Management: Resume`: Resume (unsuspend) an existing managed entity.
  * `300499` - `Entity Management: Other`

The event/finding type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

**`activity_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event activity name, as defined by the activity\_id.

**`category_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event category name, as defined by category\_uid value: `Identity & Access Management`.

**`class_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event class name, as defined by class\_uid value: `Entity Management`.

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

**`access_list`**

* **Type**: `string_t`
* **Requirement**: optional

The list of requested access rights.

**`access_mask`**

* **Type**: `integer_t`
* **Requirement**: optional

The access mask in a platform-native format.

**`actor`** [host](../profiles/host.md)

* **Type**: [`actor`](../objects/actor.md)
* **Requirement**: optional

Used for when the entity acting upon another entity is a process or user.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event or a finding. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`http_request`**

* **Type**: [`http_request`](../objects/http_request.md)
* **Requirement**: optional

Details about the underlying HTTP request.

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

* **Type**: `long_t`
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

**`cloud`** [cloud](../profiles/cloud.md)

* **Type**: [`cloud`](../objects/cloud.md)
* **Requirement**: required

Describes details about the Cloud environment where the event was originally created or logged.

**`entity`**

* **Type**: [`managed_entity`](../objects/managed_entity.md)
* **Requirement**: required

The managed entity that is being acted upon.

**`osint`** [osint](../profiles/osint.md)

* **Type**: [`osint`](../objects/osint.md)
* **Requirement**: required

The OSINT (Open Source Intelligence) object contains details related to an indicator such as the indicator itself, related indicators, geolocation, registrar information, subdomains, analyst commentary, and other contextual information. This information can be used to further enrich a detection or finding by providing decisioning support to other analysts and engineers.

**`comment`**

* **Type**: `string_t`
* **Requirement**: recommended

The user provided comment about why the entity was changed.

**`device`** [host](../profiles/host.md)

* **Type**: [`device`](../objects/device.md)
* **Requirement**: recommended

An addressable device, computer system or host.

**`entity_result`**

* **Type**: [`managed_entity`](../objects/managed_entity.md)
* **Requirement**: recommended

The updated managed entity.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event/finding, as defined by the source.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: recommended

The observables associated with the event or a finding.

**`src_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: recommended

Details about the source of the IAM activity.

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

The status detail contains additional information about the event/finding outcome.

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
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`http_request`](../objects/http_request.md)
* [`managed_entity`](../objects/managed_entity.md)
* [`metadata`](../objects/metadata.md)
* [`network_endpoint`](../objects/network_endpoint.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`osint`](../objects/osint.md)