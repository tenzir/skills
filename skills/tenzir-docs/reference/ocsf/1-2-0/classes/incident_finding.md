# Incident Finding (2005)

> An Incident Finding reports the creation, update, or closure of security incidents as a result of detections and/or analytics.


An Incident Finding reports the creation, update, or closure of security incidents as a result of detections and/or analytics.

* **Category**: Findings
* **Extends**: `base_event`
* **UID**: `2005`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Create`: Reports the creation of an Incident.
  * `2` - `Update`: Reports updates to an Incident.
  * `3` - `Close`: Reports closure of an Incident .
  * `99` - `Other`: The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the Incident activity.

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
  * `2005` - `Incident Finding`: An Incident Finding reports the creation, update, or closure of security incidents as a result of detections and/or analytics.

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

  * `200500` - `Incident Finding: Unknown`
  * `200501` - `Incident Finding: Create`: Reports the creation of an Incident.
  * `200502` - `Incident Finding: Update`: Reports updates to an Incident.
  * `200503` - `Incident Finding: Close`: Reports closure of an Incident .
  * `200599` - `Incident Finding: Other`

The event/finding type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

**`activity_name`**

* **Type**: `string_t`
* **Requirement**: optional

The Incident activity name, as defined by the `activity_id`.

**`category_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event category name, as defined by category\_uid value: `Findings`.

**`class_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event class name, as defined by class\_uid value: `Incident Finding`.

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

**`confidence_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The normalized confidence is unknown.
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `99` - `Other`: The confidence is not mapped to the defined enum values. See the `confidence` attribute, which contains a data source specific value.

The normalized confidence refers to the accuracy of the rule that created the finding. A rule with a low confidence means that the finding scope is wide and may create finding reports that may not be malicious in nature.

**`priority_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: No priority is assigned.
  * `1` - `Low`: Application or personal procedure is unusable, where a workaround is available or a repair is possible.
  * `2` - `Medium`: Non-critical function or procedure is unusable or hard to use causing operational disruptions with no direct impact on a service’s availability. A workaround is available.
  * `3` - `High`: Critical functionality or network access is interrupted, degraded or unusable, having a severe impact on services availability. No acceptable alternative is possible.
  * `4` - `Critical`: Interruption making a critical functionality inaccessible or a complete network interruption causing a severe impact on services availability. There is no possible alternative.
  * `99` - `Other`: The priority is not normalized.

The normalized priority. Priority identifies the relative importance of the finding. It is a measurement of urgency.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`assignee`**

* **Type**: [`user`](../objects/user.md)
* **Requirement**: optional

The details of the user assigned to an Incident.

**`assignee_group`**

* **Type**: [`group`](../objects/group.md)
* **Requirement**: optional

The details of the group assigned to an Incident.

**`attacks`**

* **Type**: [`attack`](../objects/attack.md)
* **Requirement**: optional

An array of [MITRE ATT\&CK®](https://attack.mitre.org) objects describing the tactics, techniques & sub-techniques associated to the Incident.

**`comment`**

* **Type**: `string_t`
* **Requirement**: optional

Additional user supplied details for updating or closing the incident.

**`confidence`**

* **Type**: `string_t`
* **Requirement**: optional

The confidence, normalized to the caption of the confidence\_id value. In the case of ‘Other’, it is defined by the event source.

**`confidence_score`**

* **Type**: `integer_t`
* **Requirement**: optional

The confidence score as reported by the event source.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event or a finding. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`is_suspected_breach`**

* **Type**: `boolean_t`
* **Requirement**: optional

A determination based on analytics as to whether a potential breach was found.

**`priority`**

* **Type**: `string_t`
* **Requirement**: optional

The priority, normalized to the caption of the priority\_id value. In the case of ‘Other’, it is defined by the event source.

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

The time of the most recent event included in the incident.

**`end_time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The time of the most recent event included in the incident.

**`start_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time of the least recent event included in the incident.

**`start_time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The time of the least recent event included in the incident.

**`time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The normalized event occurrence time or the finding creation time.

### Primary

**`cloud`** [cloud](../profiles/cloud.md)

* **Type**: [`cloud`](../objects/cloud.md)
* **Requirement**: required

Describes details about the Cloud environment where the event was originally created or logged.

**`finding_info_list`**

* **Type**: [`finding_info`](../objects/finding_info.md)
* **Requirement**: required

A list of `finding_info` objects associated to an incident.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The status is unknown.
  * `1` - `New`: The service desk has received the incident but has not assigned it to an agent.
  * `2` - `In Progress`: The incident has been assigned to an agent but has not been resolved. The agent is actively working with the user to diagnose and resolve the incident.
  * `3` - `On Hold`: The incident requires some information or response from the user or from a third party.
  * `4` - `Resolved`: The service desk has confirmed that the incident is resolved.
  * `5` - `Closed`: The incident is resolved and no further action is necessary.
  * `99` - `Other`: The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized status identifier of the Incident.

**`desc`**

* **Type**: `string_t`
* **Requirement**: recommended

The short description of the Incident.

**`impact`**

* **Type**: `string_t`
* **Requirement**: recommended

The impact , normalized to the caption of the impact\_id value. In the case of ‘Other’, it is defined by the event source.

**`impact_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The normalized impact is unknown.
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `4` - `Critical`
  * `99` - `Other`: The impact is not mapped. See the `impact` attribute, which contains a data source specific value.

The normalized impact of the finding.

**`impact_score`**

* **Type**: `integer_t`
* **Requirement**: recommended

The impact of the finding, valid range 0-100.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event/finding, as defined by the source.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: recommended

The observables associated with the event or a finding.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: recommended

A Url link used to access the original incident.

**`status`**

* **Type**: `string_t`
* **Requirement**: recommended

The normalized status of the Incident normalized to the caption of the status\_id value. In the case of ‘Other’, it is defined by the source.

**`status_code`**

* **Type**: `string_t`
* **Requirement**: recommended

The event status code, as reported by the event source.

For example, in a Windows Failed Authentication event, this would be the value of ‘Failure Code’, e.g. 0x18.

**`status_detail`**

* **Type**: `string_t`
* **Requirement**: recommended

The status details contains additional information about the event/finding outcome.

**`verdict`**

* **Type**: `string_t`
* **Requirement**: recommended

The verdict assigned to an Incident finding.

**`verdict_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `False Positive`: The incident is a false positive.
  * `2` - `True Positive`: The incident is a true positive.
  * `3` - `Disregard`: The incident can be disregarded as it is unimportant, an error or accident.
  * `4` - `Suspicious`: The incident is suspicious.
  * `5` - `Benign`: The incident is benign.
  * `6` - `Test`: The incident is a test.
  * `7` - `Insufficient Data`: The incident has insufficient data to make a verdict.
  * `8` - `Security Risk`: The incident is a security risk.
  * `9` - `Managed Externally`: The incident remediation or required actions are managed externally.
  * `10` - `Duplicate`: The incident is a duplicate.
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The normalized verdict of an Incident.

## Objects Used

* [`api`](../objects/api.md)
* [`attack`](../objects/attack.md)
* [`cloud`](../objects/cloud.md)
* [`enrichment`](../objects/enrichment.md)
* [`finding_info`](../objects/finding_info.md)
* [`group`](../objects/group.md)
* [`metadata`](../objects/metadata.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`user`](../objects/user.md)