# Event Type Categories

Usage-guide grouping for choosing `metadata.event_type`.

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Analyst events

- ANALYST_ADD_COMMENT
- ANALYST_UPDATE_PRIORITY
- ANALYST_UPDATE_REASON
- ANALYST_UPDATE_REPUTATION
- ANALYST_UPDATE_RISK_SCORE
- ANALYST_UPDATE_ROOT_CAUSE
- ANALYST_UPDATE_SEVERITY_SCORE
- ANALYST_UPDATE_STATUS
- ANALYST_UPDATE_VERDICT

## Device events

- DEVICE_CONFIG_UPDATE
- DEVICE_FIRMWARE_UPDATE
- DEVICE_PROGRAM_DOWNLOAD
- DEVICE_PROGRAM_UPLOAD

## Email events

- EMAIL_UNCATEGORIZED
- [EMAIL_TRANSACTION](event-types.md#email_transaction)
- EMAIL_URL_CLICK

## Events that are unspecified

- EVENTTYPE_UNSPECIFIED

## File events performed on an endpoint

- FILE_UNCATEGORIZED
- [FILE_COPY (for example, copying a file to a thumb drive)](event-types.md#file_copy)
- [FILE_CREATION](event-types.md#file_creation)
- [FILE_DELETION](event-types.md#file_deletion)
- [FILE_MODIFICATION](event-types.md#file_modification)
- FILE_MOVE
- [FILE_OPEN (for example, opening a file might indicate a security breach)](event-types.md#file_open)
- [FILE_READ (for example, reading a password file)](event-types.md#file_read)
- FILE_SYNC

## Events that don't fall into any other category

Events that don't fall into any other category, including uncategorized Windows events:

- GENERIC_EVENT

## Group activity events

- GROUP_UNCATEGORIZED
- GROUP_CREATION
- GROUP_DELETION
- GROUP_MODIFICATION

## Mutex events

- MUTEX_UNCATEGORIZED
- [MUTEX_CREATION](event-types.md#mutex_creation)

## Network telemetry events

Network telemetry events, which include raw protocol payloads, such as DHCP and DNS, as well as protocol summaries for protocols such as HTTP, SMTP, and FTP and flow and connection events from NetFlow and firewalls:

- NETWORK_UNCATEGORIZED
- [NETWORK_CONNECTION (for example, network connection details from a firewall)](event-types.md#network_connection)
- NETWORK_DHCP
- NETWORK_DNS
- NETWORK_FLOW (for example, aggregated flow statistics from Netflow)
- NETWORK_FTP
- [NETWORK_HTTP](event-types.md#network_http)
- NETWORK_SMTP

## Process events

Any events pertaining to a process such as a process launch, a process creating something malicious, a process injecting into another process, a change of a registry key, or creating a malicious file on disk:

- [PROCESS_UNCATEGORIZED](event-types.md#process_uncategorized)
- [PROCESS_INJECTION](event-types.md#process_injection)
- [PROCESS_LAUNCH](event-types.md#process_launch)
- [PROCESS_MODULE_LOAD](event-types.md#process_module_load)
- [PROCESS_OPEN](event-types.md#process_open)
- [PROCESS_PRIVILEGE_ESCALATION](event-types.md#process_privilege_escalation)
- [PROCESS_TERMINATION](event-types.md#process_termination)

## Registry events

Use the following REGISTRY events rather than the SETTING events when dealing with Microsoft Windows-specific registry events:

- REGISTRY_UNCATEGORIZED
- [REGISTRY_CREATION](event-types.md#registry_creation)
- [REGISTRY_MODIFICATION](event-types.md#registry_modification)
- [REGISTRY_DELETION](event-types.md#registry_deletion)

## Resource events

- RESOURCE_CREATION
- RESOURCE_DELETION
- RESOURCE_PERMISSIONS_CHANGE
- RESOURCE_READ
- RESOURCE_WRITTEN

## Scan-oriented events

Scan-oriented events includes on-demand scans and behavioral detections performed by endpoint security products (EDR, AV, DLP). They are used only when attaching a SecurityResult to another event type (such as PROCESS_LAUNCH).

Scan-oriented events:

- SCAN_UNCATEGORIZED
- [SCAN_FILE](event-types.md#scan_file)
- [SCAN_HOST](event-types.md#scan_host)
- SCAN_NETWORK
- [SCAN_PROCESS](event-types.md#scan_process)
- SCAN_PROCESS_BEHAVIORS
- [SCAN_VULN_HOST](event-types.md#scan_vuln_host)
- [SCAN_VULN_NETWORK](event-types.md#scan_vuln_network)

## Scheduled tasks events (Windows Task Scheduler, cron, etc.)

- [SCHEDULED_TASK_UNCATEGORIZED](event-types.md#scheduled_task_uncategorized)
- [SCHEDULED_TASK_CREATION](event-types.md#scheduled_task_creation)
- [SCHEDULED_TASK_DELETION](event-types.md#scheduled_task_deletion)
- [SCHEDULED_TASK_DISABLE](event-types.md#scheduled_task_disable)
- [SCHEDULED_TASK_ENABLE](event-types.md#scheduled_task_enable)
- [SCHEDULED_TASK_MODIFICATION](event-types.md#scheduled_task_modification)

## Service events

- [SERVICE_UNSPECIFIED](event-types.md#service_unspecified)
- [SERVICE_CREATION](event-types.md#service_creation)
- [SERVICE_DELETION](event-types.md#service_deletion)
- SERVICE_MODIFICATION
- [SERVICE_START](event-types.md#service_start)
- [SERVICE_STOP](event-types.md#service_stop)

## Setting events

For setting event requirements, see Settings - required fields.

Setting events, including when a system setting is changed on an endpoint:

- [SETTING_UNCATEGORIZED](event-types.md#setting_uncategorized)
- [SETTING_CREATION](event-types.md#setting_creation)
- [SETTING_DELETION](event-types.md#setting_deletion)
- [SETTING_MODIFICATION](event-types.md#setting_modification)

## Status messages from security products

Status messages from security products to indicate that agents are alive and to send version, fingerprint, or other types of data:

- STATUS_UNCATEGORIZED
- [STATUS_HEARTBEAT (indicates product is alive)](event-types.md#status_heartbeat)
- [STATUS_STARTUP](event-types.md#status_startup)
- [STATUS_SHUTDOWN](event-types.md#status_shutdown)
- [STATUS_UPDATE (software or fingerprint update)](event-types.md#status_update)

## System audit log events

- [SYSTEM_AUDIT_LOG_UNCATEGORIZED](event-types.md#system_audit_log_uncategorized)
- [SYSTEM_AUDIT_LOG_WIPE](event-types.md#system_audit_log_wipe)

## User authentication activity events

- [USER_UNCATEGORIZED](event-types.md#user_uncategorized)
- USER_BADGE_IN (for example, when a user physically badges in to a site)
- [USER_CHANGE_PASSWORD](event-types.md#user_change_password)
- [USER_CHANGE_PERMISSIONS](event-types.md#user_change_permissions)
- [USER_COMMUNICATION](event-types.md#user_communication)
- [USER_CREATION](event-types.md#user_creation)
- [USER_DELETION](event-types.md#user_deletion)
- [USER_LOGIN](event-types.md#user_login)
- [USER_LOGOUT](event-types.md#user_logout)
- [USER_RESOURCE_ACCESS](event-types.md#user_resource_access)
- [USER_RESOURCE_CREATION](event-types.md#user_resource_creation)
- [USER_RESOURCE_DELETION](event-types.md#user_resource_deletion)
- [USER_RESOURCE_UPDATE_CONTENT](event-types.md#user_resource_update_content)
- [USER_RESOURCE_UPDATE_PERMISSIONS](event-types.md#user_resource_update_permissions)
- USER_STATS
