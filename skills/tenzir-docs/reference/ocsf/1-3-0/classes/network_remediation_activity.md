# Network Remediation Activity (7004)

> Network Remediation Activity events report on attempts at remediating computer networks.


Network Remediation Activity events report on attempts at remediating computer networks. It follows the MITRE countermeasures defined by the D3FEND™ [Matrix](https://d3fend.mitre.org/). Techniques and Sub-techniques will include Network, such as Network Isolation or Network Traffic Filtering.

* **Category**: Remediation
* **Extends**: `remediation_activity`
* **UID**: `7004`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Isolate`: Creates logical or physical barriers in a system which reduces opportunities for adversaries to create further accesses. Defined by D3FEND™ [d3f:Isolate](https://d3fend.mitre.org/d3f:Isolate/).
  * `2` - `Evict`: Removes an adversary or malicious resource from a device or computer network. Defined by D3FEND™ [d3f:Evict](https://d3fend.mitre.org/d3f:Evict/).
  * `3` - `Restore`: Returns the system to a better state. Defined by D3FEND™ [d3f:Restore](https://d3fend.mitre.org/d3f:Restore/).
  * `4` - `Harden`: Increases the opportunity cost of computer network exploitation. Defined by D3FEND™ [d3f:Harden](https://d3fend.mitre.org/d3f:Harden/).
  * `99` - `Other`: The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

Matches the MITRE D3FEND™ Tactic. Note: the Model and Detect Tactics are not supported as remediations by the OCSF Remediation event class.

**`category_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `7` - `Remediation`: Remediation events report the results of remediation commands targeting files, processes, and other objects.

The category unique identifier of the event.

**`class_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `7004` - `Network Remediation Activity`: Network Remediation Activity events report on attempts at remediating computer networks. It follows the MITRE countermeasures defined by the D3FEND™ [Matrix](https://d3fend.mitre.org/). Techniques and Sub-techniques will include Network, such as Network Isolation or Network Traffic Filtering.

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

  * `700400` - `Network Remediation Activity: Unknown`
  * `700401` - `Network Remediation Activity: Isolate`: Creates logical or physical barriers in a system which reduces opportunities for adversaries to create further accesses. Defined by D3FEND™ [d3f:Isolate](https://d3fend.mitre.org/d3f:Isolate/).
  * `700402` - `Network Remediation Activity: Evict`: Removes an adversary or malicious resource from a device or computer network. Defined by D3FEND™ [d3f:Evict](https://d3fend.mitre.org/d3f:Evict/).
  * `700403` - `Network Remediation Activity: Restore`: Returns the system to a better state. Defined by D3FEND™ [d3f:Restore](https://d3fend.mitre.org/d3f:Restore/).
  * `700404` - `Network Remediation Activity: Harden`: Increases the opportunity cost of computer network exploitation. Defined by D3FEND™ [d3f:Harden](https://d3fend.mitre.org/d3f:Harden/).
  * `700499` - `Network Remediation Activity: Other`

The event/finding type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

**`activity_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event activity name, as defined by the activity\_id.

**`category_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event category name, as defined by category\_uid value: `Remediation`.

**`class_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event class name, as defined by class\_uid value: `Network Remediation Activity`.

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

**`remediation`**

* **Type**: [`remediation`](../objects/remediation.md)
* **Requirement**: optional

Describes the recommended remediation steps to address identified issue(s).

**`scan`**

* **Type**: [`scan`](../objects/scan.md)
* **Requirement**: optional

The remediation scan that pertains to this event.

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

**`command_uid`**

* **Type**: `string_t`
* **Requirement**: required

The unique identifier of the remediation command that pertains to this event.

**`connection_info`**

* **Type**: [`network_connection_info`](../objects/network_connection_info.md)
* **Requirement**: required

The network connection that pertains to the remediation event.

**`osint`** [osint](../profiles/osint.md)

* **Type**: [`osint`](../objects/osint.md)
* **Requirement**: required

The OSINT (Open Source Intelligence) object contains details related to an indicator such as the indicator itself, related indicators, geolocation, registrar information, subdomains, analyst commentary, and other contextual information. This information can be used to further enrich a detection or finding by providing decisioning support to other analysts and engineers.

**`countermeasures`**

* **Type**: [`d3fend`](../objects/d3fend.md)
* **Requirement**: recommended

The MITRE DEFEND™ Matrix Countermeasures associated with a remediation.

**`device`** [host](../profiles/host.md)

* **Type**: [`device`](../objects/device.md)
* **Requirement**: recommended

An addressable device, computer system or host.

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

The status detail contains additional information about the event/finding outcome.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The status is unknown.
  * `1` - `Success`
  * `2` - `Failure`
  * `3` - `Does Not Exist`: The target of the remediation does not exist.
  * `4` - `Partial`: The remediation was partially completed.
  * `5` - `Unsupported`: The remediation was not supported.
  * `6` - `Error`: There was an error during the remediation process.
  * `99` - `Other`: The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

**`actor`** [host](../profiles/host.md)

* **Type**: [`actor`](../objects/actor.md)
* **Requirement**: optional

The actor object describes details about the user/role/process that was the source of the activity.

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`cloud`](../objects/cloud.md)
* [`d3fend`](../objects/d3fend.md)
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`metadata`](../objects/metadata.md)
* [`network_connection_info`](../objects/network_connection_info.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`osint`](../objects/osint.md)
* [`remediation`](../objects/remediation.md)
* [`scan`](../objects/scan.md)