# DNS Activity (4003)

> DNS Activity events report DNS queries and answers as seen on the network.


DNS Activity events report DNS queries and answers as seen on the network.

* **Category**: Network Activity
* **Extends**: `network_activity`
* **UID**: `4003`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Query`: The DNS query request.
  * `2` - `Response`: The DNS query response.
  * `3` - `Reset`: The network connection was abnormally terminated or closed by a middle device like firewalls.
  * `4` - `Fail`: The network connection failed. For example a connection timeout or no route to host.
  * `5` - `Refuse`: The network connection was refused. For example an attempt to connect to a server port which is not open.
  * `6` - `Traffic`: Network traffic report.
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
  * `4003` - `DNS Activity`: DNS Activity events report DNS queries and answers as seen on the network.

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

  * `400300` - `DNS Activity: Unknown`
  * `400301` - `DNS Activity: Query`: The DNS query request.
  * `400302` - `DNS Activity: Response`: The DNS query response.
  * `400303` - `DNS Activity: Reset`: The network connection was abnormally terminated or closed by a middle device like firewalls.
  * `400304` - `DNS Activity: Fail`: The network connection failed. For example a connection timeout or no route to host.
  * `400305` - `DNS Activity: Refuse`: The network connection was refused. For example an attempt to connect to a server port which is not open.
  * `400306` - `DNS Activity: Traffic`: Network traffic report.
  * `400399` - `DNS Activity: Other`

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

The event class name, as defined by class\_uid value: `DNS Activity`.

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

**`connection_info`**

* **Type**: [`network_connection_info`](../objects/network_connection_info.md)
* **Requirement**: optional

The network connection information.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`raw_data`**

* **Type**: `string_t`
* **Requirement**: optional

The event data as received from the event source.

**`traffic`**

* **Type**: [`network_traffic`](../objects/network_traffic.md)
* **Requirement**: optional

The network traffic refers to the amount of data moving across a network at a given point of time. Intended to be used alongside Network Connection.

**`unmapped`**

* **Type**: [`object`](../objects/object.md)
* **Requirement**: optional

The attributes that are not mapped to the event schema. The names and values of those attributes are specific to the event source.

### Occurrence

**`time`**

* **Type**: `timestamp_t`
* **Requirement**: required

The normalized event occurrence time.

**`query_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The Domain Name System (DNS) query time.

**`response_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The Domain Name System (DNS) response time.

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

**`query_time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The Domain Name System (DNS) query time.

**`response_time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The Domain Name System (DNS) response time.

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

**`answers`**

* **Type**: [`dns_answer`](../objects/dns_answer.md)
* **Requirement**: recommended

The Domain Name System (DNS) answers.

**`attacks`** [security\_control](../profiles/security_control.md)

* **Type**: [`attack`](../objects/attack.md)
* **Requirement**: recommended

An array of attacks associated with an event.

**`device`** [host](../profiles/host.md)

* **Type**: [`device`](../objects/device.md)
* **Requirement**: recommended

An addressable device, computer system or host.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event, as defined by the event source.

**`query`**

* **Type**: [`dns_query`](../objects/dns_query.md)
* **Requirement**: recommended

The Domain Name System (DNS) query.

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

**`rcode`**

* **Type**: `string_t`
* **Requirement**: optional

The DNS server response code, normalized to the caption of the rcode\_id value. In the case of ‘Other’, it is defined by the event source.

**`rcode_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `NoError`: No Error.
  * `1` - `FormError`: Format Error.
  * `2` - `ServError`: Server Failure.
  * `3` - `NXDomain`: Non-Existent Domain.
  * `4` - `NotImp`: Not Implemented.
  * `5` - `Refused`: Query Refused.
  * `6` - `YXDomain`: Name Exists when it should not.
  * `7` - `YXRRSet`: RR Set Exists when it should not.
  * `8` - `NXRRSet`: RR Set that should exist does not.
  * `9` - `NotAuth`: Not Authorized or Server Not Authoritative for zone.
  * `10` - `NotZone`: Name not contained in zone.
  * `11` - `DSOTYPENI`: DSO-TYPE Not Implemented.
  * `16` - `BADSIG_VERS`: TSIG Signature Failure or Bad OPT Version.
  * `17` - `BADKEY`: Key not recognized.
  * `18` - `BADTIME`: Signature out of time window.
  * `19` - `BADMODE`: Bad TKEY Mode.
  * `20` - `BADNAME`: Duplicate key name.
  * `21` - `BADALG`: Algorithm not supported.
  * `22` - `BADTRUNC`: Bad Truncation.
  * `23` - `BADCOOKIE`: Bad/missing Server Cookie.
  * `24` - `Unassigned`: The codes deemed to be unassigned by the RFC (unassigned codes: 12-15, 24-3840, 4096-65534).
  * `25` - `Reserved`: The codes deemed to be reserved by the RFC (codes: 3841-4095, 65535).
  * `99` - `Other`: The dns response code is not defined by the RFC.

The normalized identifier of the DNS server response code. See [RFC-6895](https://datatracker.ietf.org/doc/html/rfc6895).

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

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`attack`](../objects/attack.md)
* [`cloud`](../objects/cloud.md)
* [`device`](../objects/device.md)
* [`dns_answer`](../objects/dns_answer.md)
* [`dns_query`](../objects/dns_query.md)
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