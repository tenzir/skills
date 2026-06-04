# Event Type Categories

Usage-guide grouping for choosing `metadata.event_type`.

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

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
- [EMAIL_TRANSACTION](event-guidance/email_transaction.md)
- EMAIL_URL_CLICK

## Events that are unspecified

- EVENTTYPE_UNSPECIFIED

## File events performed on an endpoint

- FILE_UNCATEGORIZED
- [FILE_COPY (for example, copying a file to a thumb drive)](event-guidance/file_copy.md)
- [FILE_CREATION](event-guidance/file_creation.md)
- [FILE_DELETION](event-guidance/file_deletion.md)
- [FILE_MODIFICATION](event-guidance/file_modification.md)
- FILE_MOVE
- [FILE_OPEN (for example, opening a file might indicate a security breach)](event-guidance/file_open.md)
- [FILE_READ (for example, reading a password file)](event-guidance/file_read.md)
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
- [MUTEX_CREATION](event-guidance/mutex_creation.md)

## Network telemetry events

Network telemetry events, which include raw protocol payloads, such as DHCP and DNS, as well as protocol summaries for protocols such as HTTP, SMTP, and FTP and flow and connection events from NetFlow and firewalls:

- NETWORK_UNCATEGORIZED
- [NETWORK_CONNECTION (for example, network connection details from a firewall)](event-guidance/network_connection.md)
- NETWORK_DHCP
- NETWORK_DNS
- NETWORK_FLOW (for example, aggregated flow statistics from Netflow)
- NETWORK_FTP
- [NETWORK_HTTP](event-guidance/network_http.md)
- NETWORK_SMTP

## Process events

Any events pertaining to a process such as a process launch, a process creating something malicious, a process injecting into another process, a change of a registry key, or creating a malicious file on disk:

- [PROCESS_UNCATEGORIZED](event-guidance/process_uncategorized.md)
- [PROCESS_INJECTION](event-guidance/process_injection.md)
- [PROCESS_LAUNCH](event-guidance/process_launch.md)
- [PROCESS_MODULE_LOAD](event-guidance/process_module_load.md)
- [PROCESS_OPEN](event-guidance/process_open.md)
- [PROCESS_PRIVILEGE_ESCALATION](event-guidance/process_privilege_escalation.md)
- [PROCESS_TERMINATION](event-guidance/process_termination.md)

## Registry events

Use the following REGISTRY events rather than the SETTING events when dealing with Microsoft Windows-specific registry events:

- REGISTRY_UNCATEGORIZED
- [REGISTRY_CREATION](event-guidance/registry_creation.md)
- [REGISTRY_MODIFICATION](event-guidance/registry_modification.md)
- [REGISTRY_DELETION](event-guidance/registry_deletion.md)

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
- [SCAN_FILE](event-guidance/scan_file.md)
- [SCAN_HOST](event-guidance/scan_host.md)
- SCAN_NETWORK
- [SCAN_PROCESS](event-guidance/scan_process.md)
- SCAN_PROCESS_BEHAVIORS
- [SCAN_VULN_HOST](event-guidance/scan_vuln_host.md)
- [SCAN_VULN_NETWORK](event-guidance/scan_vuln_network.md)

## Scheduled tasks events (Windows Task Scheduler, cron, etc.)

- [SCHEDULED_TASK_UNCATEGORIZED](event-guidance/scheduled_task_uncategorized.md)
- [SCHEDULED_TASK_CREATION](event-guidance/scheduled_task_creation.md)
- [SCHEDULED_TASK_DELETION](event-guidance/scheduled_task_deletion.md)
- [SCHEDULED_TASK_DISABLE](event-guidance/scheduled_task_disable.md)
- [SCHEDULED_TASK_ENABLE](event-guidance/scheduled_task_enable.md)
- [SCHEDULED_TASK_MODIFICATION](event-guidance/scheduled_task_modification.md)

## Service events

- [SERVICE_UNSPECIFIED](event-guidance/service_unspecified.md)
- [SERVICE_CREATION](event-guidance/service_creation.md)
- [SERVICE_DELETION](event-guidance/service_deletion.md)
- SERVICE_MODIFICATION
- [SERVICE_START](event-guidance/service_start.md)
- [SERVICE_STOP](event-guidance/service_stop.md)

## Setting events

For setting event requirements, see Settings - required fields.

Setting events, including when a system setting is changed on an endpoint:

- [SETTING_UNCATEGORIZED](event-guidance/setting_uncategorized.md)
- [SETTING_CREATION](event-guidance/setting_creation.md)
- [SETTING_DELETION](event-guidance/setting_deletion.md)
- [SETTING_MODIFICATION](event-guidance/setting_modification.md)

## Status messages from security products

Status messages from security products to indicate that agents are alive and to send version, fingerprint, or other types of data:

- STATUS_UNCATEGORIZED
- [STATUS_HEARTBEAT (indicates product is alive)](event-guidance/status_heartbeat.md)
- [STATUS_STARTUP](event-guidance/status_startup.md)
- [STATUS_SHUTDOWN](event-guidance/status_shutdown.md)
- [STATUS_UPDATE (software or fingerprint update)](event-guidance/status_update.md)

## System audit log events

- [SYSTEM_AUDIT_LOG_UNCATEGORIZED](event-guidance/system_audit_log_uncategorized.md)
- [SYSTEM_AUDIT_LOG_WIPE](event-guidance/system_audit_log_wipe.md)

## User authentication activity events

- [USER_UNCATEGORIZED](event-guidance/user_uncategorized.md)
- USER_BADGE_IN (for example, when a user physically badges in to a site)
- [USER_CHANGE_PASSWORD](event-guidance/user_change_password.md)
- [USER_CHANGE_PERMISSIONS](event-guidance/user_change_permissions.md)
- [USER_COMMUNICATION](event-guidance/user_communication.md)
- [USER_CREATION](event-guidance/user_creation.md)
- [USER_DELETION](event-guidance/user_deletion.md)
- [USER_LOGIN](event-guidance/user_login.md)
- [USER_LOGOUT](event-guidance/user_logout.md)
- [USER_RESOURCE_ACCESS](event-guidance/user_resource_access.md)
- [USER_RESOURCE_CREATION](event-guidance/user_resource_creation.md)
- [USER_RESOURCE_DELETION](event-guidance/user_resource_deletion.md)
- [USER_RESOURCE_UPDATE_CONTENT](event-guidance/user_resource_update_content.md)
- [USER_RESOURCE_UPDATE_PERMISSIONS](event-guidance/user_resource_update_permissions.md)
- USER_STATS
