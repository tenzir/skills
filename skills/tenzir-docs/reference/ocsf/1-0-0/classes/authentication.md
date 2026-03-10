# Authentication (3002)

> Authentication events report authentication session activities such as user attempts a logon or logoff, successfully or otherwise.


Authentication events report authentication session activities such as user attempts a logon or logoff, successfully or otherwise.

* **Category**: Identity & Access Management
* **Extends**: `iam`
* **UID**: `3002`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Logon`: A new logon session was requested.
  * `2` - `Logoff`: A logon session was terminated and no longer exists.
  * `3` - `Authentication Ticket`: A Kerberos authentication ticket (TGT) was requested.
  * `4` - `Service Ticket`: A Kerberos service ticket was requested.
  * `99` - `Other`: The event activity is not mapped.

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
  * `3002` - `Authentication`: Authentication events report authentication session activities such as user attempts a logon or logoff, successfully or otherwise.

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

  * `300200` - `Authentication: Unknown`
  * `300201` - `Authentication: Logon`: A new logon session was requested.
  * `300202` - `Authentication: Logoff`: A logon session was terminated and no longer exists.
  * `300203` - `Authentication: Authentication Ticket`: A Kerberos authentication ticket (TGT) was requested.
  * `300204` - `Authentication: Service Ticket`: A Kerberos service ticket was requested.
  * `300299` - `Authentication: Other`

The event type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

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

The event class name, as defined by class\_uid value: `Authentication`.

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

The actor that requested the authentication.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`http_request`**

* **Type**: [`http_request`](../objects/http_request.md)
* **Requirement**: optional

Details about the underlying http request.

**`is_cleartext`**

* **Type**: `boolean_t`
* **Requirement**: optional

Indicates whether the credentials were passed in clear text.

Note: True if the credentials were passed in a clear text protocol such as FTP or TELNET, or if Windows detected that a user’s logon password was passed to the authentication package in clear text.

**`is_new_logon`**

* **Type**: `boolean_t`
* **Requirement**: optional

Indicates logon is from a device not seen before or a first time account logon.

**`logon_process`**

* **Type**: [`process`](../objects/process.md)
* **Requirement**: optional

The trusted process that validated the authentication credentials.

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

**`user`**

* **Type**: [`user`](../objects/user.md)
* **Requirement**: required

The subject (user/role or account) to authenticate.

**`auth_protocol_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`
  * `1` - `NTLM`
  * `2` - `Kerberos`
  * `3` - `Digest`
  * `4` - `OpenID`
  * `5` - `SAML`
  * `6` - `OAUTH 2.0`
  * `7` - `PAP`
  * `8` - `CHAP`
  * `9` - `EAP`
  * `10` - `RADIUS`
  * `99` - `Other`

The normalized identifier of the authentication protocol used to create the user session.

**`device`** [host](../profiles/host.md)

* **Type**: [`device`](../objects/device.md)
* **Requirement**: recommended

An addressable device, computer system or host.

**`dst_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: recommended

The endpoint to which the authentication was targeted.

**`is_remote`**

* **Type**: `boolean_t`
* **Requirement**: recommended

The attempted authentication is over a remote connection.

**`logon_type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `System`: Used only by the System account, for example at system startup.
  * `2` - `Interactive`: A local logon to device console.
  * `3` - `Network`: A user or device logged onto this device from the network.
  * `4` - `Batch`: A batch server logon, where processes may be executing on behalf of a user without their direct intervention.
  * `5` - `OS Service`: A logon by a service or daemon that was started by the OS.
  * `7` - `Unlock`: A user unlocked the device.
  * `8` - `Network Cleartext`: A user logged on to this device from the network. The user’s password in the authentication package was not hashed.
  * `9` - `New Credentials`: A caller cloned its current token and specified new credentials for outbound connections. The new logon session has the same local identity, but uses different credentials for other network connections.
  * `10` - `Remote Interactive`: A remote logon using Terminal Services or remote desktop application.
  * `11` - `Cached Interactive`: A user logged on to this device with network credentials that were stored locally on the device and the domain controller was not contacted to verify the credentials.
  * `12` - `Cached Remote Interactive`: Same as Remote Interactive. This is used for internal auditing.
  * `13` - `Cached Unlock`: Workstation logon.
  * `99` - `Other`: Other logon type.

The normalized logon type identifier.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event, as defined by the event source.

**`service`**

* **Type**: [`service`](../objects/service.md)
* **Requirement**: recommended

The service or gateway to which the user or process is being authenticated

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`
  * `1` - `Success`
  * `2` - `Failure`
  * `99` - `Other`: The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

**`auth_protocol`**

* **Type**: `string_t`
* **Requirement**: optional

The authentication protocol as defined by the caption of ‘auth\_protocol\_id’. In the case of ‘Other’, it is defined by the event source.

**`certificate`**

* **Type**: [`certificate`](../objects/certificate.md)
* **Requirement**: optional

The certificate associated with the authentication or pre-authentication (Kerberos).

**`is_mfa`**

* **Type**: `boolean_t`
* **Requirement**: optional

Indicates whether Multi Factor Authentication was used during authentication.

**`logon_type`**

* **Type**: `string_t`
* **Requirement**: optional

The logon type, normalized to the caption of the logon\_type\_id value. In the case of ‘Other’, it is defined by the event source.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: optional

The observables associated with the event.

**`session`**

* **Type**: [`session`](../objects/session.md)
* **Requirement**: optional

The authenticated user or service session.

**`src_endpoint`**

* **Type**: [`network_endpoint`](../objects/network_endpoint.md)
* **Requirement**: optional

The Endpoint from which the authentication was requested.

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

The details about the authentication request. For example, possible details for Windows logon or logoff events are:

* Success
* LOGOFF\_USER\_INITIATED
* LOGOFF\_OTHER
* Failure
* USER\_DOES\_NOT\_EXIST
* INVALID\_CREDENTIALS
* ACCOUNT\_DISABLED
* ACCOUNT\_LOCKED\_OUT
* PASSWORD\_EXPIRED

## Objects Used

* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`certificate`](../objects/certificate.md)
* [`cloud`](../objects/cloud.md)
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`http_request`](../objects/http_request.md)
* [`metadata`](../objects/metadata.md)
* [`network_endpoint`](../objects/network_endpoint.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`process`](../objects/process.md)
* [`service`](../objects/service.md)
* [`session`](../objects/session.md)
* [`user`](../objects/user.md)