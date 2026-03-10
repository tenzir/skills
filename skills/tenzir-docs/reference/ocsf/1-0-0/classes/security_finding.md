# Security Finding (2001)

> Security Finding events describe findings, detections, anomalies, alerts and/or actions performed by security products


Security Finding events describe findings, detections, anomalies, alerts and/or actions performed by security products

* **Category**: Findings
* **Extends**: `findings`
* **UID**: `2001`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Create`: A security finding is created.
  * `2` - `Update`: A security finding is updated.
  * `99` - `Other`: The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

**`category_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `2` - `Findings`: Findings events report findings, detections, and possible resolutions of malware, anomalies, or other actions performed by security products.

The category unique identifier of the event.

**`class_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `2001` - `Security Finding`: Security Finding events describe findings, detections, anomalies, alerts and/or actions performed by security products

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

  * `200100` - `Security Finding: Unknown`
  * `200101` - `Security Finding: Create`: A security finding is created.
  * `200102` - `Security Finding: Update`: A security finding is updated.
  * `200199` - `Security Finding: Other`

The event type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

**`activity_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event activity name, as defined by the activity\_id.

**`category_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event category name, as defined by category\_uid value: `Findings`.

**`class_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event class name, as defined by class\_uid value: `Security Finding`.

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

**`state_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`
  * `1` - `New`: The finding is new and yet to be reviewed.
  * `2` - `In Progress`: The finding is under review.
  * `3` - `Suppressed`: The finding was reviewed, considered as a false positive and is now suppressed.
  * `4` - `Resolved`: The finding was reviewed and remediated and is now considered resolved.
  * `99` - `Other`: The state is not mapped. See the `state` attribute, which contains a data source specific value.

The normalized state identifier of a security finding.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`attacks`**

* **Type**: [`attack`](../objects/attack.md)
* **Requirement**: optional

The attack object describes the technique and associated tactics as defined by ATT\&CK MatrixTM.

**`cis_csc`**

* **Type**: [`cis_control`](../objects/cis_control.md)
* **Requirement**: optional

The CIS Critical Security Controls is a list of top 20 actions and practices an organization’s security team can take on such that cyber attacks or malware, are minimized and prevented.

**`compliance`**

* **Type**: [`compliance`](../objects/compliance.md)
* **Requirement**: optional

The compliance object provides context to compliance findings (e.g., a check against a specific regulatory or best practice framework such as CIS or NIST) and contains compliance related details.

**`data_sources`**

* **Type**: `string_t`
* **Requirement**: optional

The data sources for the finding.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`evidence`**

* **Type**: `json_t`
* **Requirement**: optional

The data the finding exposes to the analyst.

**`kill_chain`**

* **Type**: [`kill_chain`](../objects/kill_chain.md)
* **Requirement**: optional

The [Cyber Kill Chain®](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html).

**`malware`**

* **Type**: [`malware`](../objects/malware.md)
* **Requirement**: optional

The list of malware identified by a finding.

**`nist`**

* **Type**: `string_t`
* **Requirement**: optional

The NIST Cybersecurity Framework recommendations for managing the cybersecurity risk.

**`process`**

* **Type**: [`process`](../objects/process.md)
* **Requirement**: optional

The process object.

**`raw_data`**

* **Type**: `string_t`
* **Requirement**: optional

The event data as received from the event source.

**`state`**

* **Type**: `string_t`
* **Requirement**: optional

The normalized state of a security finding.

**`unmapped`**

* **Type**: [`object`](../objects/object.md)
* **Requirement**: optional

The attributes that are not mapped to the event schema. The names and values of those attributes are specific to the event source.

**`vulnerabilities`**

* **Type**: [`vulnerability`](../objects/vulnerability.md)
* **Requirement**: optional

This object describes vulnerabilities reported in a security finding.

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

**`finding`**

* **Type**: [`finding`](../objects/finding.md)
* **Requirement**: required

Finding object provides details related to a finding generated by security tool

**`analytic`**

* **Type**: [`analytic`](../objects/analytic.md)
* **Requirement**: recommended

The analytic technique used to create the finding or detection

**`confidence_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: No confidence is assigned.
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `99` - `Other`: The confidence is not mapped to the defined enum values. See the `confidence` attribute, which contains a data source specific value.

The normalized confidence refers to the accuracy of the rule that created the finding. A rule with a low confidence means that the finding scope is wide and may create finding reports that may not be malicious in nature.

**`impact_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `4` - `Critical`
  * `99` - `Other`: The detection impact is not mapped. See the `impact` attribute, which contains a data source specific value.

The normalized impact of the finding.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event, as defined by the event source.

**`resources`**

* **Type**: [`resource_details`](../objects/resource_details.md)
* **Requirement**: recommended

Describes details about resources that were affected by the activity/event.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`
  * `1` - `Success`
  * `2` - `Failure`
  * `99` - `Other`: The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

**`confidence`**

* **Type**: `string_t`
* **Requirement**: optional

The confidence, normalized to the caption of the confidence\_id value. In the case of ‘Other’, it is defined by the event source.

**`confidence_score`**

* **Type**: `integer_t`
* **Requirement**: optional

The confidence score as reported by the event source.

**`impact`**

* **Type**: `string_t`
* **Requirement**: optional

The impact , normalized to the caption of the impact\_id value. In the case of ‘Other’, it is defined by the event source.

**`impact_score`**

* **Type**: `integer_t`
* **Requirement**: optional

The impact of the finding, valid range 0-100.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: optional

The observables associated with the event.

**`risk_level`**

* **Type**: `string_t`
* **Requirement**: optional

The risk level, normalized to the caption of the risk\_level\_id value. In the case of ‘Other’, it is defined by the event source.

**`risk_level_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Info`
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `4` - `Critical`

The normalized risk level id.

**`risk_score`**

* **Type**: `integer_t`
* **Requirement**: optional

The risk score as reported by the event source.

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

* [`analytic`](../objects/analytic.md)
* [`api`](../objects/api.md)
* [`attack`](../objects/attack.md)
* [`cis_control`](../objects/cis_control.md)
* [`cloud`](../objects/cloud.md)
* [`compliance`](../objects/compliance.md)
* [`enrichment`](../objects/enrichment.md)
* [`finding`](../objects/finding.md)
* [`kill_chain`](../objects/kill_chain.md)
* [`malware`](../objects/malware.md)
* [`metadata`](../objects/metadata.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`process`](../objects/process.md)
* [`resource_details`](../objects/resource_details.md)
* [`vulnerability`](../objects/vulnerability.md)