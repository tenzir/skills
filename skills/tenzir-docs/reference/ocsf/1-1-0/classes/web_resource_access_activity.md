# Web Resource Access Activity (6004)

> Web Resource Access Activity events describe successful/failed attempts to access a web resource over HTTP.


Web Resource Access Activity events describe successful/failed attempts to access a web resource over HTTP.

* **Category**: Application Activity
* **Extends**: `application`
* **UID**: `6004`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Access Grant`: The incoming request has permission to the web resource.
  * `2` - `Access Deny`: The incoming request does not have permission to the web resource.
  * `3` - `Access Revoke`: The incoming request’s access has been revoked due to security policy enforcements.
  * `4` - `Access Error`: An error occurred during processing the request.
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
  * `6004` - `Web Resource Access Activity`: Web Resource Access Activity events describe successful/failed attempts to access a web resource over HTTP.

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

  * `600400` - `Web Resource Access Activity: Unknown`
  * `600401` - `Web Resource Access Activity: Access Grant`: The incoming request has permission to the web resource.
  * `600402` - `Web Resource Access Activity: Access Deny`: The incoming request does not have permission to the web resource.
  * `600403` - `Web Resource Access Activity: Access Revoke`: The incoming request’s access has been revoked due to security policy enforcements.
  * `600404` - `Web Resource Access Activity: Access Error`: An error occurred during processing the request.
  * `600499` - `Web Resource Access Activity: Other`

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

The event class name, as defined by class\_uid value: `Web Resource Access Activity`.

**`severity`**

* **Type**: `string_t`
* **Requirement**: optional

The event/finding severity, normalized to the caption of the severity\_id value. In the case of ‘Other’, it is defined by the source.

**`type_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event/finding type name, as defined by the type\_uid.

### Context

**`http_request`**

* **Type**: [`http_request`](../objects/http_request.md)
* **Requirement**: required

Details about the underlying HTTP request.

**`metadata`**

* **Type**: [`metadata`](../objects/metadata.md)
* **Requirement**: required

The metadata associated with the event or a finding.

**`proxy_connection_info`** [network\_proxy](../profiles/network_proxy.md)

* **Type**: [`network_connection_info`](../objects/network_connection_info.md)
* **Requirement**: recommended

The connection information from the proxy server to the remote server.

**`proxy_tls`** [network\_proxy](../profiles/network_proxy.md)

* **Type**: [`tls`](../objects/tls.md)
* **Requirement**: recommended

The TLS protocol negotiated between the proxy server and the remote server.

**`proxy_traffic`** [network\_proxy](../profiles/network_proxy.md)

* **Type**: [`network_traffic`](../objects/network_traffic.md)
* **Requirement**: recommended

The network traffic refers to the amount of data moving across a network, from proxy to remote server at a given point of time.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event or a finding. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`http_response`**

* **Type**: [`http_response`](../objects/http_response.md)
* **Requirement**: optional

Details about the HTTP response, if available.

**`proxy`**

* **Type**: [`network_proxy`](../objects/network_proxy.md)
* **Requirement**: optional

Details about the proxy service, if available.

**`proxy_endpoint`** [network\_proxy](../profiles/network_proxy.md)

* **Type**: [`network_proxy`](../objects/network_proxy.md)
* **Requirement**: optional

The proxy (server) in a network connection.

**`proxy_http_request`** [network\_proxy](../profiles/network_proxy.md)

* **Type**: [`http_request`](../objects/http_request.md)
* **Requirement**: optional

The HTTP Request from the proxy server to the remote server.

**`proxy_http_response`** [network\_proxy](../profiles/network_proxy.md)

* **Type**: [`http_response`](../objects/http_response.md)
* **Requirement**: optional

The HTTP Response from the remote server to the proxy server.

**`raw_data`**

* **Type**: `string_t`
* **Requirement**: optional

The raw event/finding data as received from the source.

**`tls`**

* **Type**: [`tls`](../objects/tls.md)
* **Requirement**: optional

The Transport Layer Security (TLS) attributes, if available.

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

**`cloud`** [cloud](../profiles/cloud.md)

* **Type**: [`cloud`](../objects/cloud.md)
* **Requirement**: required

Describes details about the Cloud environment where the event was originally created or logged.

**`web_resources`**

* **Type**: [`web_resource`](../objects/web_resource.md)
* **Requirement**: required

Details about the resource that is the target of the activity.

**`device`** [host](../profiles/host.md)

* **Type**: [`device`](../objects/device.md)
* **Requirement**: recommended

An addressable device, computer system or host.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event/finding, as defined by the source.

**`src_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: recommended

Details about the source endpoint of the request.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The status is unknown.
  * `1` - `Success`
  * `2` - `Failure`
  * `99` - `Other`: The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

**`actor`** [host](../profiles/host.md)

* **Type**: [`actor`](../objects/actor.md)
* **Requirement**: optional

The actor object describes details about the user/role/process that was the source of the activity.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: optional

The observables associated with the event or a finding.

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

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`cloud`](../objects/cloud.md)
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`http_request`](../objects/http_request.md)
* [`http_response`](../objects/http_response.md)
* [`metadata`](../objects/metadata.md)
* [`network_connection_info`](../objects/network_connection_info.md)
* [`network_endpoint`](../objects/network_endpoint.md)
* [`network_proxy`](../objects/network_proxy.md)
* [`network_traffic`](../objects/network_traffic.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`tls`](../objects/tls.md)
* [`web_resource`](../objects/web_resource.md)