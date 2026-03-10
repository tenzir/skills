# HTTP Activity (4002)

> HTTP Activity events report HTTP connection and traffic information.


HTTP Activity events report HTTP connection and traffic information.

* **Category**: Network Activity
* **Extends**: `network`
* **UID**: `4002`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Connect`: The CONNECT method establishes a tunnel to the server identified by the target resource.
  * `2` - `Delete`: The DELETE method deletes the specified resource.
  * `3` - `Get`: The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
  * `4` - `Head`: The HEAD method asks for a response identical to a GET request, but without the response body.
  * `5` - `Options`: The OPTIONS method describes the communication options for the target resource.
  * `6` - `Post`: The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.
  * `7` - `Put`: The PUT method replaces all current representations of the target resource with the request payload.
  * `8` - `Trace`: The TRACE method performs a message loop-back test along the path to the target resource.
  * `9` - `Patch`: The PATCH method applies partial modifications to a resource.
  * `99` - `Other`: The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

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
  * `4002` - `HTTP Activity`: HTTP Activity events report HTTP connection and traffic information.

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

  * `400200` - `HTTP Activity: Unknown`
  * `400201` - `HTTP Activity: Connect`: The CONNECT method establishes a tunnel to the server identified by the target resource.
  * `400202` - `HTTP Activity: Delete`: The DELETE method deletes the specified resource.
  * `400203` - `HTTP Activity: Get`: The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
  * `400204` - `HTTP Activity: Head`: The HEAD method asks for a response identical to a GET request, but without the response body.
  * `400205` - `HTTP Activity: Options`: The OPTIONS method describes the communication options for the target resource.
  * `400206` - `HTTP Activity: Post`: The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.
  * `400207` - `HTTP Activity: Put`: The PUT method replaces all current representations of the target resource with the request payload.
  * `400208` - `HTTP Activity: Trace`: The TRACE method performs a message loop-back test along the path to the target resource.
  * `400209` - `HTTP Activity: Patch`: The PATCH method applies partial modifications to a resource.
  * `400299` - `HTTP Activity: Other`

The event/finding type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

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

The event class name, as defined by class\_uid value: `HTTP Activity`.

**`severity`**

* **Type**: `string_t`
* **Requirement**: optional

The event/finding severity, normalized to the caption of the `severity_id` value. In the case of ‘Other’, it is defined by the source.

**`type_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event/finding type name, as defined by the type\_uid.

### Context

**`metadata`**

* **Type**: [`metadata`](../objects/metadata.md)
* **Requirement**: required

The metadata associated with the event or a finding.

**`confidence_id`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The normalized confidence is unknown.
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `99` - `Other`: The confidence is not mapped to the defined enum values. See the `confidence` attribute, which contains a data source specific value.

The normalized confidence refers to the accuracy of the rule that created the finding. A rule with a low confidence means that the finding scope is wide and may create finding reports that may not be malicious in nature.

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

**`app_name`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the application associated with the event or object.

**`confidence`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

The confidence, normalized to the caption of the confidence\_id value. In the case of ‘Other’, it is defined by the event source.

**`confidence_score`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`
* **Requirement**: optional

The confidence score as reported by the event source.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event or a finding. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`file`**

* **Type**: [`file`](../objects/file.md)
* **Requirement**: optional

The file that is the target of the HTTP activity.

**`ja4_fingerprint_list`**

* **Type**: [`ja4_fingerprint`](../objects/ja4_fingerprint.md)
* **Requirement**: optional

A list of the JA4+ network fingerprints.

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

**`raw_data_hash`**

* **Type**: [`fingerprint`](../objects/fingerprint.md)
* **Requirement**: optional

The hash, which describes the content of the raw\_data field.

**`raw_data_size`**

* **Type**: `long_t`
* **Requirement**: optional

The size of the raw data which was transformed into an OCSF event, in bytes.

**`risk_details`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

Describes the risk associated with the finding.

**`risk_level`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

The risk level, normalized to the caption of the risk\_level\_id value.

**`risk_level_id`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Info`
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `4` - `Critical`
  * `99` - `Other`: The risk level is not mapped. See the `risk_level` attribute, which contains a data source specific value.

The normalized risk level id.

**`risk_score`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`
* **Requirement**: optional

The risk score as reported by the event source.

**`tls`**

* **Type**: [`tls`](../objects/tls.md)
* **Requirement**: optional

The Transport Layer Security (TLS) attributes.

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

**`osint`** [osint](../profiles/osint.md)

* **Type**: [`osint`](../objects/osint.md)
* **Requirement**: required

The OSINT (Open Source Intelligence) object contains details related to an indicator such as the indicator itself, related indicators, geolocation, registrar information, subdomains, analyst commentary, and other contextual information. This information can be used to further enrich a detection or finding by providing decisioning support to other analysts and engineers.

**`action_id`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The action was unknown. The `disposition_id` attribute may still be set to a non-unknown value, for example ‘Custom Action’, ‘Challenge’.
  * `1` - `Allowed`: The activity was allowed. The `disposition_id` attribute should be set to a value that conforms to this action, for example ‘Allowed’, ‘Approved’, ‘Delayed’, ‘No Action’, ‘Count’ etc.
  * `2` - `Denied`: The attempted activity was denied. The `disposition_id` attribute should be set to a value that conforms to this action, for example ‘Blocked’, ‘Rejected’, ‘Quarantined’, ‘Isolated’, ‘Dropped’, ‘Access Revoked, etc.
  * `3` - `Observed`: The activity was observed, but neither explicitly allowed nor denied. This is common with IDS and EDR controls that report additional information on observed behavior such as TTPs. The `disposition_id` attribute should be set to a value that conforms to this action, for example ‘Logged’, ‘Alert’, ‘Detected’, ‘Count’, etc.
  * `4` - `Modified`: The activity was modified, adjusted, or corrected. The `disposition_id` attribute should be set appropriately, for example ‘Restored’, ‘Corrected’, ‘Delayed’, ‘Captcha’, ‘Tagged’.
  * `99` - `Other`: The action is not mapped. See the `action` attribute which contains a data source specific value.

The action taken by a control or other policy-based system leading to an outcome or disposition. An unknown action may still correspond to a known disposition. Refer to `disposition_id` for the outcome of the action.

**`connection_info`**

* **Type**: [`network_connection_info`](../objects/network_connection_info.md)
* **Requirement**: recommended

The network connection information.

**`device`** [host](../profiles/host.md)

* **Type**: [`device`](../objects/device.md)
* **Requirement**: recommended

An addressable device, computer system or host.

**`disposition_id`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The disposition is unknown.
  * `1` - `Allowed`: Granted access or allowed the action to the protected resource.
  * `2` - `Blocked`: Denied access or blocked the action to the protected resource.
  * `3` - `Quarantined`: A suspicious file or other content was moved to a benign location.
  * `4` - `Isolated`: A session was isolated on the network or within a browser.
  * `5` - `Deleted`: A file or other content was deleted.
  * `6` - `Dropped`: The request was detected as a threat and resulted in the connection being dropped.
  * `7` - `Custom Action`: A custom action was executed such as running of a command script. Use the `message` attribute of the base class for details.
  * `8` - `Approved`: A request or submission was approved. For example, when a form was properly filled out and submitted. This is distinct from `1` ‘Allowed’.
  * `9` - `Restored`: A quarantined file or other content was restored to its original location.
  * `10` - `Exonerated`: A suspicious or risky entity was deemed to no longer be suspicious (re-scored).
  * `11` - `Corrected`: A corrupt file or configuration was corrected.
  * `12` - `Partially Corrected`: A corrupt file or configuration was partially corrected.
  * `13` - `Uncorrected`: A corrupt file or configuration was not corrected.
  * `14` - `Delayed`: An operation was delayed, for example if a restart was required to finish the operation.
  * `15` - `Detected`: Suspicious activity or a policy violation was detected without further action.
  * `16` - `No Action`: The outcome of an operation had no action taken.
  * `17` - `Logged`: The operation or action was logged without further action.
  * `18` - `Tagged`: A file or other entity was marked with extended attributes.
  * `19` - `Alert`: The request or activity was detected as a threat and resulted in a notification but request was not blocked.
  * `20` - `Count`: Counted the request or activity but did not determine whether to allow it or block it.
  * `21` - `Reset`: The request was detected as a threat and resulted in the connection being reset.
  * `22` - `Captcha`: Required the end user to solve a CAPTCHA puzzle to prove that a human being is sending the request.
  * `23` - `Challenge`: Ran a silent challenge that required the client session to verify that it’s a browser, and not a bot.
  * `24` - `Access Revoked`: The requestor’s access has been revoked due to security policy enforcements. Note: use the `Host` profile if the `User` or `Actor` requestor is not present in the event class.
  * `25` - `Rejected`: A request or submission was rejected. For example, when a form was improperly filled out and submitted. This is distinct from `2` ‘Blocked’.
  * `26` - `Unauthorized`: An attempt to access a resource was denied due to an authorization check that failed. This is a more specific disposition than `2` ‘Blocked’ and can be complemented with the `authorizations` attribute for more detail.
  * `27` - `Error`: An error occurred during the processing of the activity or request. Use the `message` attribute of the base class for details.
  * `99` - `Other`: The disposition is not mapped. See the `disposition` attribute, which contains a data source specific value.

Describes the outcome or action taken by a security control, such as access control checks, malware detections or various types of policy violations.

**`dst_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: recommended

The responder (server) in a network connection.

**`http_cookies`**

* **Type**: [`http_cookie`](../objects/http_cookie.md)
* **Requirement**: recommended

The cookies object describes details about HTTP cookies

**`http_request`**

* **Type**: [`http_request`](../objects/http_request.md)
* **Requirement**: recommended

The HTTP Request Object documents attributes of a request made to a web server.

**`http_response`**

* **Type**: [`http_response`](../objects/http_response.md)
* **Requirement**: recommended

The HTTP Response from a web server to a requester.

**`http_status`**

* **Type**: `integer_t`
* **Requirement**: recommended

The Hypertext Transfer Protocol (HTTP) [status code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) returned to the client.

**`is_alert`** [security\_control](../profiles/security_control.md)

* **Type**: `boolean_t`
* **Requirement**: recommended

Indicates that the event is considered to be an alertable signal. Should be set to `true` if `disposition_id = Alert` among other dispositions, and/or `risk_level_id` or `severity_id` of the event is elevated. Not all control events will be alertable, for example if `disposition_id = Exonerated` or `disposition_id = Allowed`.

**`load_balancer`** [load\_balancer](../profiles/load_balancer.md)

* **Type**: [`load_balancer`](../objects/load_balancer.md)
* **Requirement**: recommended

The Load Balancer object contains information related to the device that is distributing incoming traffic to specified destinations.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event/finding, as defined by the source.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: recommended

The observables associated with the event or a finding.

**`proxy`**

* **Type**: [`network_proxy`](../objects/network_proxy.md)
* **Requirement**: recommended

The proxy (server) in a network connection.

**`src_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: recommended

The initiator (client) of the network connection.

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
  * `99` - `Other`: The status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

**`trace`** [trace](../profiles/trace.md)

* **Type**: [`trace`](../objects/trace.md)
* **Requirement**: recommended

The trace object contains information about distributed traces which are critical to observability and describe how requests move through a system, capturing each step’s timing and status.

**`traffic`**

* **Type**: [`network_traffic`](../objects/network_traffic.md)
* **Requirement**: recommended

The network traffic refers to the amount of data moving across a network at a given point of time. Intended to be used alongside Network Connection.

**`action`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

The normalized caption of `action_id`.

**`actor`** [host](../profiles/host.md)

* **Type**: [`actor`](../objects/actor.md)
* **Requirement**: optional

The actor object describes details about the user/role/process that was the source of the activity. Note that this is not the threat actor of a campaign but may be part of a campaign.

**`attacks`** [security\_control](../profiles/security_control.md)

* **Type**: [`attack`](../objects/attack.md)
* **Requirement**: optional

An array of MITRE ATT\&CK® objects describing identified tactics, techniques & sub-techniques. The objects are compatible with MITRE ATLAS™ tactics, techniques & sub-techniques.

**`authorizations`** [security\_control](../profiles/security_control.md)

* **Type**: [`authorization`](../objects/authorization.md)
* **Requirement**: optional

Provides details about an authorization, such as authorization outcome, and any associated policies related to the activity/event.

**`disposition`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

The disposition name, normalized to the caption of the disposition\_id value. In the case of ‘Other’, it is defined by the event source.

**`firewall_rule`** [security\_control](../profiles/security_control.md)

* **Type**: [`firewall_rule`](../objects/firewall_rule.md)
* **Requirement**: optional

The firewall rule that pertains to the control that triggered the event, if applicable.

**`malware`** [security\_control](../profiles/security_control.md)

* **Type**: [`malware`](../objects/malware.md)
* **Requirement**: optional

A list of Malware objects, describing details about the identified malware.

**`malware_scan_info`** [security\_control](../profiles/security_control.md)

* **Type**: [`malware_scan_info`](../objects/malware_scan_info.md)
* **Requirement**: optional

Describes details about the scan job that identified malware on the target system.

**`policy`** [security\_control](../profiles/security_control.md)

* **Type**: [`policy`](../objects/policy.md)
* **Requirement**: optional

The policy that pertains to the control that triggered the event, if applicable. For example the name of an anti-malware policy or an access control policy.

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`attack`](../objects/attack.md)
* [`authorization`](../objects/authorization.md)
* [`cloud`](../objects/cloud.md)
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`file`](../objects/file.md)
* [`fingerprint`](../objects/fingerprint.md)
* [`firewall_rule`](../objects/firewall_rule.md)
* [`http_cookie`](../objects/http_cookie.md)
* [`http_request`](../objects/http_request.md)
* [`http_response`](../objects/http_response.md)
* [`ja4_fingerprint`](../objects/ja4_fingerprint.md)
* [`load_balancer`](../objects/load_balancer.md)
* [`malware`](../objects/malware.md)
* [`malware_scan_info`](../objects/malware_scan_info.md)
* [`metadata`](../objects/metadata.md)
* [`network_connection_info`](../objects/network_connection_info.md)
* [`network_endpoint`](../objects/network_endpoint.md)
* [`network_proxy`](../objects/network_proxy.md)
* [`network_traffic`](../objects/network_traffic.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`osint`](../objects/osint.md)
* [`policy`](../objects/policy.md)
* [`tls`](../objects/tls.md)
* [`trace`](../objects/trace.md)