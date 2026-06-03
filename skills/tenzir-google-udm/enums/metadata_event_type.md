# Metadata.EventType

An event type. Choose event type not based on the product that generated the event but the one that logged the event itself. So, for example, an antivirus (AV) scanning email on a client would generate an SMTP_PROXY event, not an AV event. A DLP device scanning a web upload would generate an HTTP_PROXY event and not a DLP or process activity event. Note: In the case of a HTTP_PROXY event, you might also include process details if this occurred on an endpoint. That would be optional, but there are a certain set of required fields and banned fields due to its status as an HTTP_PROXY event.

- **Full name**: `google.backstory.Metadata.EventType`
- **Values**: `105`

## Values

### `EVENTTYPE_UNSPECIFIED`

- **Number**: `0`

Default event type

### `PROCESS_UNCATEGORIZED`

- **Number**: `10000`

Activity related to a process which does not match any other event types.

### `PROCESS_LAUNCH`

- **Number**: `10001`

Process launch.

### `PROCESS_INJECTION`

- **Number**: `10002`

Process injecting into another process.

### `PROCESS_PRIVILEGE_ESCALATION`

- **Number**: `10003`

Process privilege escalation.

### `PROCESS_TERMINATION`

- **Number**: `10004`

Process termination.

### `PROCESS_OPEN`

- **Number**: `10005`

Process being opened.

### `PROCESS_MODULE_LOAD`

- **Number**: `10006`

Process loading a module.

### `REGISTRY_UNCATEGORIZED`

- **Number**: `11000`

Registry event which does not match any of the other event types.

### `REGISTRY_CREATION`

- **Number**: `11001`

Registry creation.

### `REGISTRY_MODIFICATION`

- **Number**: `11002`

Registry modification.

### `REGISTRY_DELETION`

- **Number**: `11003`

Registry deletion.

### `SETTING_UNCATEGORIZED`

- **Number**: `12000`

Settings-related event which does not match any of the other event types.

### `SETTING_CREATION`

- **Number**: `12001`

Setting creation.

### `SETTING_MODIFICATION`

- **Number**: `12002`

Setting modification.

### `SETTING_DELETION`

- **Number**: `12003`

Setting deletion.

### `MUTEX_UNCATEGORIZED`

- **Number**: `13000`

Any mutex event other than creation.

### `MUTEX_CREATION`

- **Number**: `13001`

Mutex creation.

### `FILE_UNCATEGORIZED`

- **Number**: `14000`

File event which does not match any of the other event types.

### `FILE_CREATION`

- **Number**: `14001`

File created.

### `FILE_DELETION`

- **Number**: `14002`

File deleted.

### `FILE_MODIFICATION`

- **Number**: `14003`

File modified.

### `FILE_READ`

- **Number**: `14004`

File read.

### `FILE_COPY`

- **Number**: `14005`

File copied. Used for file copies, for example, to a thumb drive.

### `FILE_OPEN`

- **Number**: `14006`

File opened.

### `FILE_MOVE`

- **Number**: `14007`

File moved or renamed.

### `FILE_SYNC`

- **Number**: `14008`

File synced (for example, Google Drive, Dropbox, backup).

### `USER_UNCATEGORIZED`

- **Number**: `15000`

User activity which does not match any of the other event types.

### `USER_LOGIN`

- **Number**: `15001`

User login.

### `USER_LOGOUT`

- **Number**: `15002`

User logout.

### `USER_CREATION`

- **Number**: `15003`

User creation.

### `USER_CHANGE_PASSWORD`

- **Number**: `15004`

User password change event.

### `USER_CHANGE_PERMISSIONS`

- **Number**: `15005`

Change in user permissions.

### `USER_STATS`

- **Number**: `15006`
- **Deprecated**: `true`

Deprecated. Used to update user info for an LDAP dump.

### `USER_BADGE_IN`

- **Number**: `15007`

User physically badging into a location.

### `USER_DELETION`

- **Number**: `15008`

User deletion.

### `USER_RESOURCE_CREATION`

- **Number**: `15009`

User creating a virtual resource. This is equivalent to RESOURCE_CREATION.

### `USER_RESOURCE_UPDATE_CONTENT`

- **Number**: `15010`

User updating content of a virtual resource. This is equivalent to RESOURCE_WRITTEN.

### `USER_RESOURCE_UPDATE_PERMISSIONS`

- **Number**: `15011`

User updating permissions of a virtual resource. This is equivalent to RESOURCE_PERMISSIONS_CHANGE.

### `USER_COMMUNICATION`

- **Number**: `15012`

User initiating communication through a medium (for example, video).

### `USER_RESOURCE_ACCESS`

- **Number**: `15013`

User accessing a virtual resource. This is equivalent to RESOURCE_READ.

### `USER_RESOURCE_DELETION`

- **Number**: `15014`

User deleting a virtual resource. This is equivalent to RESOURCE_DELETION.

### `GROUP_UNCATEGORIZED`

- **Number**: `23000`

A group activity that does not fall into one of the other event types.

### `GROUP_CREATION`

- **Number**: `23001`

A group creation.

### `GROUP_DELETION`

- **Number**: `23002`

A group deletion.

### `GROUP_MODIFICATION`

- **Number**: `23003`

A group modification.

### `EMAIL_UNCATEGORIZED`

- **Number**: `19000`

Email messages

### `EMAIL_TRANSACTION`

- **Number**: `19001`

An email transaction.

### `EMAIL_URL_CLICK`

- **Number**: `19002`
- **Deprecated**: `true`

Deprecated: use NETWORK_HTTP instead. An email URL click event.

### `NETWORK_UNCATEGORIZED`

- **Number**: `16000`

A network event that does not fit into one of the other event types.

### `NETWORK_FLOW`

- **Number**: `16001`

Aggregated flow stats like netflow.

### `NETWORK_CONNECTION`

- **Number**: `16002`

Network connection details like from a FW.

### `NETWORK_FTP`

- **Number**: `16003`

FTP telemetry.

### `NETWORK_DHCP`

- **Number**: `16004`

DHCP payload.

### `NETWORK_DNS`

- **Number**: `16005`

DNS payload.

### `NETWORK_HTTP`

- **Number**: `16006`

HTTP telemetry.

### `NETWORK_SMTP`

- **Number**: `16007`

SMTP telemetry.

### `STATUS_UNCATEGORIZED`

- **Number**: `17000`

A status message that does not fit into one of the other event types.

### `STATUS_HEARTBEAT`

- **Number**: `17001`

Heartbeat indicating product is alive.

### `STATUS_STARTUP`

- **Number**: `17002`

An agent startup.

### `STATUS_SHUTDOWN`

- **Number**: `17003`

An agent shutdown.

### `STATUS_UPDATE`

- **Number**: `17004`

A software or fingerprint update.

### `SCAN_UNCATEGORIZED`

- **Number**: `18000`

Scan item that does not fit into one of the other event types.

### `SCAN_FILE`

- **Number**: `18001`

A file scan.

### `SCAN_PROCESS_BEHAVIORS`

- **Number**: `18002`
- **Deprecated**: `true`

Scan process behaviors. Please use SCAN_PROCESS instead.

### `SCAN_PROCESS`

- **Number**: `18003`

Scan process.

### `SCAN_HOST`

- **Number**: `18004`

Scan results from scanning an entire host device for threats/sensitive documents.

### `SCAN_VULN_HOST`

- **Number**: `18005`

Vulnerability scan logs about host vulnerabilities (e.g., out of date software) and network vulnerabilities (e.g., unprotected service detected via a network scan).

### `SCAN_VULN_NETWORK`

- **Number**: `18006`

Vulnerability scan logs about network vulnerabilities.

### `SCAN_NETWORK`

- **Number**: `18007`

Scan network for suspicious activity

### `SCHEDULED_TASK_UNCATEGORIZED`

- **Number**: `20000`

Scheduled task event that does not fall into one of the other event types.

### `SCHEDULED_TASK_CREATION`

- **Number**: `20001`

Scheduled task creation.

### `SCHEDULED_TASK_DELETION`

- **Number**: `20002`

Scheduled task deletion.

### `SCHEDULED_TASK_ENABLE`

- **Number**: `20003`

Scheduled task being enabled.

### `SCHEDULED_TASK_DISABLE`

- **Number**: `20004`

Scheduled task being disabled.

### `SCHEDULED_TASK_MODIFICATION`

- **Number**: `20005`

Scheduled task being modified.

### `SYSTEM_AUDIT_LOG_UNCATEGORIZED`

- **Number**: `21000`

A system audit log event that is not a wipe.

### `SYSTEM_AUDIT_LOG_WIPE`

- **Number**: `21001`

A system audit log wipe.

### `SERVICE_UNSPECIFIED`

- **Number**: `22000`

Service event that does not fit into one of the other event types.

### `SERVICE_CREATION`

- **Number**: `22001`

A service creation.

### `SERVICE_DELETION`

- **Number**: `22002`

A service deletion.

### `SERVICE_START`

- **Number**: `22003`

A service start.

### `SERVICE_STOP`

- **Number**: `22004`

A service stop.

### `SERVICE_MODIFICATION`

- **Number**: `22005`

A service modification.

### `GENERIC_EVENT`

- **Number**: `100000`

Operating system events that are not described by any of the other event types. Might include uncategorized Microsoft Windows event logs.

### `RESOURCE_CREATION`

- **Number**: `1`

The resource was created/provisioned. This is equivalent to USER_RESOURCE_CREATION.

### `RESOURCE_DELETION`

- **Number**: `2`

The resource was deleted/deprovisioned. This is equivalent to USER_RESOURCE_DELETION.

### `RESOURCE_PERMISSIONS_CHANGE`

- **Number**: `3`

The resource had it's permissions or ACLs updated. This is equivalent to USER_RESOURCE_UPDATE_PERMISSIONS.

### `RESOURCE_READ`

- **Number**: `4`

The resource was read. This is equivalent to USER_RESOURCE_ACCESS.

### `RESOURCE_WRITTEN`

- **Number**: `5`

The resource was written to. This is equivalent to USER_RESOURCE_UPDATE_CONTENT.

### `DEVICE_FIRMWARE_UPDATE`

- **Number**: `25000`

Firmware update.

### `DEVICE_CONFIG_UPDATE`

- **Number**: `25001`

Configuration update.

### `DEVICE_PROGRAM_UPLOAD`

- **Number**: `25002`

A program or application uploaded to a device.

### `DEVICE_PROGRAM_DOWNLOAD`

- **Number**: `25003`

A program or application downloaded to a device.

### `ANALYST_UPDATE_VERDICT`

- **Number**: `24000`

Analyst update about the Verdict (such as true positive, false positive, or disregard) of a finding.

### `ANALYST_UPDATE_REPUTATION`

- **Number**: `24001`

Analyst update about the Reputation (such as useful or not useful) of a finding.

### `ANALYST_UPDATE_SEVERITY_SCORE`

- **Number**: `24002`

Analyst update about the Severity score (0-100) of a finding.

### `ANALYST_UPDATE_STATUS`

- **Number**: `24007`

Analyst update about the finding status.

### `ANALYST_ADD_COMMENT`

- **Number**: `24008`

Analyst addition of a comment for a finding.

### `ANALYST_UPDATE_PRIORITY`

- **Number**: `24009`

Analyst update about the priority (such as low, medium, or high) for a finding.

### `ANALYST_UPDATE_ROOT_CAUSE`

- **Number**: `24010`

Analyst update about the root cause for a finding.

### `ANALYST_UPDATE_REASON`

- **Number**: `24011`

Analyst update about the reason (such as malicious or not malicious) for a finding.

### `ANALYST_UPDATE_RISK_SCORE`

- **Number**: `24012`

Analyst update about the risk score (0-100) of a finding.

### `ENTITY_RISK_CHANGE`

- **Number**: `26000`

An update to an entity risk score. This event type is restricted to events published by Google Securit Operations Risk Analytics.

### `TRIAGE_AGENT_UPDATE_INVESTIGATION`

- **Number**: `27000`

Triage Agent has investigated the finding.
