# DHCP Activity (4004)

> DHCP Activity events report MAC to IP assignment via DHCP from a client or server.


DHCP Activity events report MAC to IP assignment via DHCP from a client or server.

* **Category**: Network Activity
* **Extends**: `network`
* **UID**: `4004`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Discover`: DHCPDISCOVER
  * `2` - `Offer`: DHCPOFFER
  * `3` - `Request`: DHCPREQUEST
  * `4` - `Decline`: DHCPDECLINE
  * `5` - `Ack`: DHCPACK: The server accepts the request by sending the client a DHCP Acknowledgment message.
  * `6` - `Nak`: DHCPNAK
  * `7` - `Release`: DHCPRELEASE: A DHCP client sends a DHCPRELEASE packet to the server to release the IP address and cancel any remaining lease.
  * `8` - `Inform`: DHCPINFORM
  * `9` - `Expire`: DHCPEXPIRE: A DHCP lease expired.
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
  * `4004` - `DHCP Activity`: DHCP Activity events report MAC to IP assignment via DHCP from a client or server.

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

  * `400400` - `DHCP Activity: Unknown`
  * `400401` - `DHCP Activity: Discover`: DHCPDISCOVER
  * `400402` - `DHCP Activity: Offer`: DHCPOFFER
  * `400403` - `DHCP Activity: Request`: DHCPREQUEST
  * `400404` - `DHCP Activity: Decline`: DHCPDECLINE
  * `400405` - `DHCP Activity: Ack`: DHCPACK: The server accepts the request by sending the client a DHCP Acknowledgment message.
  * `400406` - `DHCP Activity: Nak`: DHCPNAK
  * `400407` - `DHCP Activity: Release`: DHCPRELEASE: A DHCP client sends a DHCPRELEASE packet to the server to release the IP address and cancel any remaining lease.
  * `400408` - `DHCP Activity: Inform`: DHCPINFORM
  * `400409` - `DHCP Activity: Expire`: DHCPEXPIRE: A DHCP lease expired.
  * `400499` - `DHCP Activity: Other`

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

The event class name, as defined by class\_uid value: `DHCP Activity`.

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

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event or a finding. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

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

**`action_id`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The action was unknown. The `disposition_id` attribute may still be set to a non-unknown value, for example ‘Count’, ‘Uncorrected’, ‘Isolated’, ‘Quarantined’ or ‘Exonerated’.
  * `1` - `Allowed`: The activity was allowed. The `disposition_id` attribute should be set to a value that conforms to this action, for example ‘Allowed’, ‘Approved’, ‘Delayed’, ‘No Action’, ‘Count’ etc.
  * `2` - `Denied`: The attempted activity was denied. The `disposition_id` attribute should be set to a value that conforms to this action, for example ‘Blocked’, ‘Rejected’, ‘Quarantined’, ‘Isolated’, ‘Dropped’, ‘Access Revoked, etc.
  * `99` - `Other`: The action was not mapped. See the `action` attribute, which contains a data source specific value.

The action taken by a control or other policy-based system leading to an outcome or disposition. Dispositions conform to an action of `1` ‘Allowed’ or `2` ‘Denied’ in most cases. Note that `99` ‘Other’ is not an option. No action would equate to `1` ‘Allowed’. An unknown action may still correspond to a known disposition. Refer to `disposition_id` for the outcome of the action.

**`cloud`** [cloud](../profiles/cloud.md)

* **Type**: [`cloud`](../objects/cloud.md)
* **Requirement**: required

Describes details about the Cloud environment where the event was originally created or logged.

**`osint`** [osint](../profiles/osint.md)

* **Type**: [`osint`](../objects/osint.md)
* **Requirement**: required

The OSINT (Open Source Intelligence) object contains details related to an indicator such as the indicator itself, related indicators, geolocation, registrar information, subdomains, analyst commentary, and other contextual information. This information can be used to further enrich a detection or finding by providing decisioning support to other analysts and engineers.

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

The responder (server) of the DHCP connection.

**`is_renewal`**

* **Type**: `boolean_t`
* **Requirement**: recommended

The indication of whether this is a lease/session renewal event.

**`lease_dur`**

* **Type**: `integer_t`
* **Requirement**: recommended

This represents the length of the DHCP lease in seconds. This is present in DHCP Ack events.

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

**`relay`**

* **Type**: [`network_interface`](../objects/network_interface.md)
* **Requirement**: recommended

The network relay that is associated with the event.

**`src_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: recommended

The initiator (client) of the DHCP connection.

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

**`traffic`**

* **Type**: [`network_traffic`](../objects/network_traffic.md)
* **Requirement**: recommended

The network traffic refers to the amount of data moving across a network at a given point of time. Intended to be used alongside Network Connection.

**`transaction_uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the transaction. This is typically a random number generated from the client to associate a dhcp request/response pair.

**`action`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

The normalized caption of `action_id`.

**`actor`** [host](../profiles/host.md)

* **Type**: [`actor`](../objects/actor.md)
* **Requirement**: optional

The actor object describes details about the user/role/process that was the source of the activity.

**`attacks`** [security\_control](../profiles/security_control.md)

* **Type**: [`attack`](../objects/attack.md)
* **Requirement**: optional

An array of [MITRE ATT\&CK®](https://attack.mitre.org) objects describing the tactics, techniques & sub-techniques identified by a security control or finding.

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

The firewall rule that triggered the event.

**`malware`** [security\_control](../profiles/security_control.md)

* **Type**: [`malware`](../objects/malware.md)
* **Requirement**: optional

A list of Malware objects, describing details about the identified malware.

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`attack`](../objects/attack.md)
* [`authorization`](../objects/authorization.md)
* [`cloud`](../objects/cloud.md)
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`firewall_rule`](../objects/firewall_rule.md)
* [`http_request`](../objects/http_request.md)
* [`http_response`](../objects/http_response.md)
* [`ja4_fingerprint`](../objects/ja4_fingerprint.md)
* [`load_balancer`](../objects/load_balancer.md)
* [`malware`](../objects/malware.md)
* [`metadata`](../objects/metadata.md)
* [`network_connection_info`](../objects/network_connection_info.md)
* [`network_endpoint`](../objects/network_endpoint.md)
* [`network_interface`](../objects/network_interface.md)
* [`network_proxy`](../objects/network_proxy.md)
* [`network_traffic`](../objects/network_traffic.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`osint`](../objects/osint.md)
* [`tls`](../objects/tls.md)