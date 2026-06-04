# Event Types

An event type. Choose event type not based on the product that generated the event but the one that logged the event itself. So, for example, an antivirus (AV) scanning email on a client would generate an SMTP_PROXY event, not an AV event. A DLP device scanning a web upload would generate an HTTP_PROXY event and not a DLP or process activity event. Note: In the case of a HTTP_PROXY event, you might also include process details if this occurred on an endpoint. That would be optional, but there are a certain set of required fields and banned fields due to its status as an HTTP_PROXY event.

## Values

- `EVENTTYPE_UNSPECIFIED` (0): Default event type
- `PROCESS_UNCATEGORIZED` (10000): Activity related to a process which does not match any other event types.
- `PROCESS_LAUNCH` (10001): Process launch.
- `PROCESS_INJECTION` (10002): Process injecting into another process.
- `PROCESS_PRIVILEGE_ESCALATION` (10003): Process privilege escalation.
- `PROCESS_TERMINATION` (10004): Process termination.
- `PROCESS_OPEN` (10005): Process being opened.
- `PROCESS_MODULE_LOAD` (10006): Process loading a module.
- `REGISTRY_UNCATEGORIZED` (11000): Registry event which does not match any of the other event types.
- `REGISTRY_CREATION` (11001): Registry creation.
- `REGISTRY_MODIFICATION` (11002): Registry modification.
- `REGISTRY_DELETION` (11003): Registry deletion.
- `SETTING_UNCATEGORIZED` (12000): Settings-related event which does not match any of the other event types.
- `SETTING_CREATION` (12001): Setting creation.
- `SETTING_MODIFICATION` (12002): Setting modification.
- `SETTING_DELETION` (12003): Setting deletion.
- `MUTEX_UNCATEGORIZED` (13000): Any mutex event other than creation.
- `MUTEX_CREATION` (13001): Mutex creation.
- `FILE_UNCATEGORIZED` (14000): File event which does not match any of the other event types.
- `FILE_CREATION` (14001): File created.
- `FILE_DELETION` (14002): File deleted.
- `FILE_MODIFICATION` (14003): File modified.
- `FILE_READ` (14004): File read.
- `FILE_COPY` (14005): File copied. Used for file copies, for example, to a thumb drive.
- `FILE_OPEN` (14006): File opened.
- `FILE_MOVE` (14007): File moved or renamed.
- `FILE_SYNC` (14008): File synced (for example, Google Drive, Dropbox, backup).
- `USER_UNCATEGORIZED` (15000): User activity which does not match any of the other event types.
- `USER_LOGIN` (15001): User login.
- `USER_LOGOUT` (15002): User logout.
- `USER_CREATION` (15003): User creation.
- `USER_CHANGE_PASSWORD` (15004): User password change event.
- `USER_CHANGE_PERMISSIONS` (15005): Change in user permissions.
- `USER_STATS` (15006, deprecated): Deprecated. Used to update user info for an LDAP dump.
- `USER_BADGE_IN` (15007): User physically badging into a location.
- `USER_DELETION` (15008): User deletion.
- `USER_RESOURCE_CREATION` (15009): User creating a virtual resource. This is equivalent to RESOURCE_CREATION.
- `USER_RESOURCE_UPDATE_CONTENT` (15010): User updating content of a virtual resource. This is equivalent to RESOURCE_WRITTEN.
- `USER_RESOURCE_UPDATE_PERMISSIONS` (15011): User updating permissions of a virtual resource. This is equivalent to RESOURCE_PERMISSIONS_CHANGE.
- `USER_COMMUNICATION` (15012): User initiating communication through a medium (for example, video).
- `USER_RESOURCE_ACCESS` (15013): User accessing a virtual resource. This is equivalent to RESOURCE_READ.
- `USER_RESOURCE_DELETION` (15014): User deleting a virtual resource. This is equivalent to RESOURCE_DELETION.
- `GROUP_UNCATEGORIZED` (23000): A group activity that does not fall into one of the other event types.
- `GROUP_CREATION` (23001): A group creation.
- `GROUP_DELETION` (23002): A group deletion.
- `GROUP_MODIFICATION` (23003): A group modification.
- `EMAIL_UNCATEGORIZED` (19000): Email messages
- `EMAIL_TRANSACTION` (19001): An email transaction.
- `EMAIL_URL_CLICK` (19002, deprecated): Deprecated: use NETWORK_HTTP instead. An email URL click event.
- `NETWORK_UNCATEGORIZED` (16000): A network event that does not fit into one of the other event types.
- `NETWORK_FLOW` (16001): Aggregated flow stats like netflow.
- `NETWORK_CONNECTION` (16002): Network connection details like from a FW.
- `NETWORK_FTP` (16003): FTP telemetry.
- `NETWORK_DHCP` (16004): DHCP payload.
- `NETWORK_DNS` (16005): DNS payload.
- `NETWORK_HTTP` (16006): HTTP telemetry.
- `NETWORK_SMTP` (16007): SMTP telemetry.
- `STATUS_UNCATEGORIZED` (17000): A status message that does not fit into one of the other event types.
- `STATUS_HEARTBEAT` (17001): Heartbeat indicating product is alive.
- `STATUS_STARTUP` (17002): An agent startup.
- `STATUS_SHUTDOWN` (17003): An agent shutdown.
- `STATUS_UPDATE` (17004): A software or fingerprint update.
- `SCAN_UNCATEGORIZED` (18000): Scan item that does not fit into one of the other event types.
- `SCAN_FILE` (18001): A file scan.
- `SCAN_PROCESS_BEHAVIORS` (18002, deprecated): Scan process behaviors. Please use SCAN_PROCESS instead.
- `SCAN_PROCESS` (18003): Scan process.
- `SCAN_HOST` (18004): Scan results from scanning an entire host device for threats/sensitive documents.
- `SCAN_VULN_HOST` (18005): Vulnerability scan logs about host vulnerabilities (e.g., out of date software) and network vulnerabilities (e.g., unprotected service detected via a network scan).
- `SCAN_VULN_NETWORK` (18006): Vulnerability scan logs about network vulnerabilities.
- `SCAN_NETWORK` (18007): Scan network for suspicious activity
- `SCHEDULED_TASK_UNCATEGORIZED` (20000): Scheduled task event that does not fall into one of the other event types.
- `SCHEDULED_TASK_CREATION` (20001): Scheduled task creation.
- `SCHEDULED_TASK_DELETION` (20002): Scheduled task deletion.
- `SCHEDULED_TASK_ENABLE` (20003): Scheduled task being enabled.
- `SCHEDULED_TASK_DISABLE` (20004): Scheduled task being disabled.
- `SCHEDULED_TASK_MODIFICATION` (20005): Scheduled task being modified.
- `SYSTEM_AUDIT_LOG_UNCATEGORIZED` (21000): A system audit log event that is not a wipe.
- `SYSTEM_AUDIT_LOG_WIPE` (21001): A system audit log wipe.
- `SERVICE_UNSPECIFIED` (22000): Service event that does not fit into one of the other event types.
- `SERVICE_CREATION` (22001): A service creation.
- `SERVICE_DELETION` (22002): A service deletion.
- `SERVICE_START` (22003): A service start.
- `SERVICE_STOP` (22004): A service stop.
- `SERVICE_MODIFICATION` (22005): A service modification.
- `GENERIC_EVENT` (100000): Operating system events that are not described by any of the other event types. Might include uncategorized Microsoft Windows event logs.
- `RESOURCE_CREATION` (1): The resource was created/provisioned. This is equivalent to USER_RESOURCE_CREATION.
- `RESOURCE_DELETION` (2): The resource was deleted/deprovisioned. This is equivalent to USER_RESOURCE_DELETION.
- `RESOURCE_PERMISSIONS_CHANGE` (3): The resource had it's permissions or ACLs updated. This is equivalent to USER_RESOURCE_UPDATE_PERMISSIONS.
- `RESOURCE_READ` (4): The resource was read. This is equivalent to USER_RESOURCE_ACCESS.
- `RESOURCE_WRITTEN` (5): The resource was written to. This is equivalent to USER_RESOURCE_UPDATE_CONTENT.
- `DEVICE_FIRMWARE_UPDATE` (25000): Firmware update.
- `DEVICE_CONFIG_UPDATE` (25001): Configuration update.
- `DEVICE_PROGRAM_UPLOAD` (25002): A program or application uploaded to a device.
- `DEVICE_PROGRAM_DOWNLOAD` (25003): A program or application downloaded to a device.
- `ANALYST_UPDATE_VERDICT` (24000): Analyst update about the Verdict (such as true positive, false positive, or disregard) of a finding.
- `ANALYST_UPDATE_REPUTATION` (24001): Analyst update about the Reputation (such as useful or not useful) of a finding.
- `ANALYST_UPDATE_SEVERITY_SCORE` (24002): Analyst update about the Severity score (0-100) of a finding.
- `ANALYST_UPDATE_STATUS` (24007): Analyst update about the finding status.
- `ANALYST_ADD_COMMENT` (24008): Analyst addition of a comment for a finding.
- `ANALYST_UPDATE_PRIORITY` (24009): Analyst update about the priority (such as low, medium, or high) for a finding.
- `ANALYST_UPDATE_ROOT_CAUSE` (24010): Analyst update about the root cause for a finding.
- `ANALYST_UPDATE_REASON` (24011): Analyst update about the reason (such as malicious or not malicious) for a finding.
- `ANALYST_UPDATE_RISK_SCORE` (24012): Analyst update about the risk score (0-100) of a finding.
- `ENTITY_RISK_CHANGE` (26000): An update to an entity risk score. This event type is restricted to events published by Google Securit Operations Risk Analytics.
- `TRIAGE_AGENT_UPDATE_INVESTIGATION` (27000): Triage Agent has investigated the finding.

## Guidance

Population guidance for choosing event types and required fields.

### EMAIL_TRANSACTION

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: Populate with information about the machine that the email message originated from (for example, the IP address of the sender).
- `network.email`: Email sender or recipient information.

#### Optional Fields

- `about`: URLs, IPs, domains, and any file attachments embedded in the email body.
- `securityResult.about`: Bad URLs, IPs, and files embedded within the email body.
- `principal`: If there is client machine data on who sent the email, populate the server details in principal (for example, the client process, port numbers, username, etc.).
- `target`: If there is destination email server data, populate the server details in target (for example, the IP address).
- `intermediary`: If there is mail server data or mail proxy data, populate the server details in intermediary.

#### Notes

- Never populate `principal.email` or `target.email`.
- Only populate the `email` field in `security_result.about` or `network.email`.
- Top level security results generally have a noun set (optional for spam).

### File Creation / Deletion / Modification / Read / Open Events

Applies to: `FILE_CREATION`, `FILE_DELETION`, `FILE_MODIFICATION`, `FILE_READ`, `FILE_OPEN`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. (Optional) Populate `principal.process` with information about the process accessing the file.
- `target`: If the file is remote (for example SMB share), the target must include at least one machine identifier for the target machine, otherwise all machine identifiers must be blank. Populate `target.file` with information about the file.

#### Optional Fields

- `security_result`: Describe the malicious activity detected.
- `principal.user`: Populate if user information is available about the process.

### FILE_COPY

#### Required Fields

- `metadata`: Include the required fields as described.
- `principal`: At least one machine identifier. (Optional) Populate `principal.process` with information about the process performing the file copy operation.
- `src`: Populate `src.file` with information about the source file. If the file is remote (for example SMB share), src must include at least one machine identifier for the source machine storing the source file.
- `target`: Populate `target.file` with information about the target file. If the file is remote (for example SMB share), the `target` field must include at least one machine identifier for the target machine that holds the target file.

#### Optional Fields

- `security_result`: Describe the malicious activity detected.
- `principal.user`: Populate if user information is available about the process.

### MUTEX_CREATION

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. Populate `principal.process` with information about the process creating the mutex.
- `target`: Populate `target.resource`. Populate `target.resource.type` with MUTEX. Populate `target.resource.name` with the name of the mutex created.

#### Optional Fields

- `security_result`: Describe the malicious activity detected.
- `principal.user`: Populate if user information is available about the process.

### NETWORK_CONNECTION

#### Required Fields

- `metadata`: `event_timestamp`
- `principal`: Include detail about the machine that initiated the network connection (for example, source).
- `target`: Include details about the target machine if different from the principal machine.
- `network`: Capture details about the network connection (ports, protocol, etc.).

#### Optional Fields

- `principal.process` and `target.process`: Include process information associated with the principal and target of the network connection (if available).
- `principal.user` and `target.user`: Include user information associated with the principal and target of the network connection (if available).

#### Notes

- Note: For all network events, if the principal or target has a port specified, the `ip` and `mac` fields must include only one value each (if available), that is the IP address and MAC associated with the port. Otherwise, if no port is specified, you can specify any number of IP and MAC addresses associated with the device at the time of the event (no particular order is required).

### NETWORK_HTTP

#### Required Fields

- `metadata`: Include the required fields.
- `target`: Represents the web server. Include device information and an optional port number. If a target port number is available, specify only one IP address in addition to the port number associated with that network connection (although multiple other machine identifiers could be provided for the target). For `target.url`, populate with the URL accessed.

#### Optional Fields

- `principal`: Represents the client initiating the web request. Include at least one machine identifier (for example, hostname, IP, MAC, proprietary asset identifier) or a user identifier (for example, username). If a specific network connection is described and a client port number is available, specify only one IP address along with the port number associated with that network connection (although other machine identifiers could be provided to better describe the participant device). If no source port is available, you could specify any and all IP and MAC addresses, asset identifiers, and hostname values describing the principal device.
- `network`: Include details of the network connection. You must populate the following fields: `network.ip_protocol` `network.application_protocol`
- `about`: Represents other entities found in the HTTP transaction (for example, an uploaded or downloaded file).
- `intermediary`: Represents a proxy server (if different from the principal or target).
- `metadata`: Populate the other `metadata` fields.
- `network`: Populate other `network` fields.
- `network.email`: If the HTTP network connection originated from a URL that appeared in an email message, populate `network.email` with the details.
- `network.http`: If the HTTP network connection method is present, populate `network.http.method`.
- `observer`: Represents a passive sniffer (if present).
- `security_result`: Add one or more items to the `security_result` field to represent the malicious activity detected.

#### Notes

- The NETWORK_HTTP event type represents an HTTP network connection from a principal to a target web server.

### Process Injection / Launch / Open / Termination / Uncategorized Events

Applies to: `PROCESS_INJECTION`, `PROCESS_LAUNCH`, `PROCESS_OPEN`, `PROCESS_TERMINATION`, `PROCESS_UNCATEGORIZED`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. For process injection and process termination events, if available, `principal.process` must include information about the process initiating the action (for example, for a process launch event, `principal.process` must include details about the parent process if available).
- `target`: `target.process`: Includes information about the process that is being injected, opened, launched, or terminated. If the target process is remote, target must include at least one machine identifier for the target machine (for example, an IP address, MAC, hostname, or third-party asset identifier).

#### Optional Fields

- `security_result`: Describe the malicious activity detected.
- `principal.user` and `target.user`: Populate the initiating process (principal) and the target process if the user information is available.

### PROCESS_MODULE_LOAD

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. `principal.process`: Process loading the module.
- `target`: `target.process`: Includes information about the process. `target.process.file`: Module loaded (for example, the DLL or shared object).

#### Optional Fields

- `security_result`: Describe the malicious activity detected.
- `principal.user`: Populate if user information is available about the process.

### PROCESS_PRIVILEGE_ESCALATION

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. `principal.process`: Process loading the module. `principal.user`: User loading the module.

#### Optional Fields

- `security_result`: Describe the malicious activity detected.

### Registry Creation / Modification / Deletion Events

Applies to: `REGISTRY_CREATION`, `REGISTRY_MODIFICATION`, `REGISTRY_DELETION`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. If a user-mode process performs the registry modification, `principal.process` must include information about the process modifying the registry. If a kernel process performs the registry modification, the principal must not include process information.
- `target`: `target.registry`: If the target registry is remote, target must include at least one identifier for the target machine (for example, an IP address, MAC, hostname, or third party asset identifier). `target.registry.registry_key`: All registry events must include the affected registry key.

#### Optional Fields

- `security_result`: Describe the malicious activity detected. For example, a bad registry key.
- `principal.user`: Populate if user information is available about the process.

### Scan File / Host / Process / Vuln Host / Vuln Network Events

Applies to: `SCAN_FILE`, `SCAN_HOST`, `SCAN_PROCESS`, `SCAN_VULN_HOST`, `SCAN_VULN_NETWORK`

#### Required Fields

- `metadata`: `event_timestamp` and background information about the event.
- `observer`: Capture information about the scanner itself. If the scanner is remote, the machine details must be captured by the `observer` field. For a local scanner, leave empty.
- `target`: Capture information about the machine that holds the object being scanned. If a file is being scanned, `target.file` must capture information about the scanned file. If a process is being scanned, `target.process` must capture information about the scanned process.
- `extensions`: For SCAN_VULN_HOST and SCAN_VULN_NETWORK, define the vulnerability using the `extensions.vuln` field.

#### Optional Fields

- `principal`: Represents the device initiating the connection and includes at least one machine identifier (for example, hostname, IP address, MAC address, proprietary asset identifier) or a user identifier.
- `target`: User detail about the target object (for example, file creator or process owner) should be captured in `target.user`.
- `security_result`: Describe the malicious activity detected.

### Scheduled Task Creation / Deletion / Disable / Enable / Modification / Uncategorized Events

Applies to: `SCHEDULED_TASK_CREATION`, `SCHEDULED_TASK_DELETION`, `SCHEDULED_TASK_DISABLE`, `SCHEDULED_TASK_ENABLE`, `SCHEDULED_TASK_MODIFICATION`, `SCHEDULED_TASK_UNCATEGORIZED`

#### Required Fields

- `principal`: For all SCHEDULED_TASK events, principal must include a machine identifier and a user identifier.
- `target`: Target must include a valid resource and a resource type defined as "TASK".

#### Optional Fields

- `security_result`: Describe the malicious activity detected.

### Setting Uncategorized / Creation / Modification / Deletion Events

Applies to: `SETTING_UNCATEGORIZED`, `SETTING_CREATION`, `SETTING_MODIFICATION`, `SETTING_DELETION`

#### Required Fields

- `principal`: Must be present, non-empty, and include a machine identifier.
- `target`: Must be present, non-empty, and include a resource with its type specified as SETTING

### Service Unspecified / Creation / Deletion / Start / Stop Events

Applies to: `SERVICE_UNSPECIFIED`, `SERVICE_CREATION`, `SERVICE_DELETION`, `SERVICE_START`, `SERVICE_STOP`

#### Required Fields

- `target`: Include the user identifier and specify either process or application.
- `principal`: Include at least one machine identifier (IP or MAC ADDRESS, hostname, or asset identifier).

### Status Heartbeat / Startup / Shutdown / Update Events

Applies to: `STATUS_HEARTBEAT`, `STATUS_STARTUP`, `STATUS_SHUTDOWN`, `STATUS_UPDATE`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier (IP or MAC ADDRESS, hostname, or asset identifier).

### System Audit Log Uncategorized / Wipe Events

Applies to: `SYSTEM_AUDIT_LOG_UNCATEGORIZED`, `SYSTEM_AUDIT_LOG_WIPE`

#### Required Fields

- `principal`: Include a user identifier for the user who performed the operation on the log and a machine identifier for the machine where the log is or was (in the case of wiping) stored.

### User Change Password / Permissions Events

Applies to: `USER_CHANGE_PASSWORD`, `USER_CHANGE_PERMISSIONS`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: If the user account is modified from a remote location, populate principal with information about the machine from where the user modification originated.
- `target`: Populate `target.user` with information about the user that has been modified.
- `intermediary`: For SSO logins, intermediary must include at least one machine identifier for the SSO server if available.

### USER_COMMUNICATION

#### Required Fields

- `principal`: Populate the `principal.user` field with details associated with user-initiated (sender) communication, such as a chat message in Google Chat or Slack, a video or voice conference in Zoom or Google Meet, or a VoIP connection.

#### Optional Fields

- `target`: (Recommended) Populate the `target.user` field with information about the target user (receiver) of the cloud communication resource. Populate the `target.application` field with information about the target cloud communication application.

### User Creation / Deletion Events

Applies to: `USER_CREATION`, `USER_DELETION`

#### Required Fields

- `metadata`: `event_timestamp`.
- `principal`: Include information about the machine where the request to create or delete the user originated from. For a local user creation or deletion, principal must include at least one machine identifier for the originating machine.
- `target`: Location where the user is being created. Must also include user information (for example, `target.user`).

#### Optional Fields

- `principal`: User and process details for the machine where the user creation or deletion request was initiated.
- `target`: Information about the target machine (if different than the principal machine).

### User Login / Logout Events

Applies to: `USER_LOGIN`, `USER_LOGOUT`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: For remote user activity (for example, remote login), populate principal with information about the machine originating the user activity. For local user activity (for example, local login), don't set principal.
- `target`: Populate `target.user` with information about the user that has logged on or logged off. If principal is not set (for example, local login), target must also include at least one machine identifier identifying the target machine. For machine to machine user activity (for example, remote login, SSO, Cloud Service, VPN), target must include information on either the target application, target machine, or target VPN server.
- `intermediary`: For SSO logins, intermediary must include at least one machine identifier for the SSO server if available.
- `network` and `network.http`: If the login occurs over HTTP, you must place all available details in `network.ip_protocol`, `network.application_protocol`, and `network.http`.
- authentication extension: Must identify the type of authentication system that the event is related to (for example, machine, SSO, or VPN) and the mechanism employed (username and password, OTP, etc.).
- `security_result`: Add a `security_result` field to represent the login status if it fails. Specify `security_result.category` with the AUTH_VIOLATION value if authentication fails.

### USER_RESOURCE_ACCESS

#### Required Fields

- `principal`: Populate the `principal.user` field with details about attempts to access a cloud resource (for example, a Salesforce case, Office365 calendar, Google Doc, or ServiceNow ticket).
- `target`: Populate the `target.resource` field with information about the target cloud resource.

#### Optional Fields

- `target.application`: (Recommended) Populate the `target.application` field with information about the target cloud application.

### User Resource Creation / Deletion Events

Applies to: `USER_RESOURCE_CREATION`, `USER_RESOURCE_DELETION`

#### Required Fields

- `principal`: Populate the `principal.user` field with details associated with the user created within a cloud resource (for example, a Salesforce case, Office 365 calendar, Google Doc, or ServiceNow ticket).
- `target`: Populate the `target.resource` field with information about the target cloud resource.

#### Optional Fields

- `target.application`: (Recommended) Populate the `target.application` field with information about the target cloud application.

### USER_RESOURCE_UPDATE_CONTENT

#### Required Fields

- `principal`: Populate the `principal.user` field with details associated with the user whose content was updated within a cloud resource (for example, a Salesforce case, Office365 calendar, Google Doc, or ServiceNow ticket).
- `target`: Populate the `target.resource` field with information about the target cloud resource.

#### Optional Fields

- `target.application`: (Recommended) Populate the `target.application` field with information about the target cloud application.

### USER_RESOURCE_UPDATE_PERMISSIONS

#### Required Fields

- `principal`: Populate the `principal.user` field with details associated with the user whose permissions were updated within a cloud resource (for example, a Salesforce case, Office 365 calendar, Google Doc, or ServiceNow ticket).
- `target`: Populate the `target.resource` field with information about the target cloud resource.

#### Optional Fields

- `target.application`: (Recommended) Populate the `target.application` field with information about the target cloud application.

### USER_UNCATEGORIZED

#### Required Fields

- `metadata`: `event_timestamp`
- `principal`: Include information about the machine where the request to create or delete the user originated from. For a local user creation or deletion, principal must include at least one machine identifier for the originating machine.
- `target`: Location where the user is being created. Must also include user information (for example, `target.user`).

#### Optional Fields

- `principal`: User and process details for the machine where the user creation or deletion request was initiated.
- `target`: Information about the target machine (if different than the principal machine).
