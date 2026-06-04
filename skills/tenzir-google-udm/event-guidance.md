# Event Guidance

Required fields, optional fields, notes, and examples by
`Metadata.EventType`. Grouped Google usage-guide sections are rendered as
one alias page for each event type.

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Event Types

- [`EMAIL_TRANSACTION`](event-guidance/email_transaction.md)
- [`FILE_COPY`](event-guidance/file_copy.md)
- [`FILE_CREATION`](event-guidance/file_creation.md) - section: FILE_CREATION, FILE_DELETION, FILE_MODIFICATION, FILE_READ, and FILE_OPEN
- [`FILE_DELETION`](event-guidance/file_deletion.md) - section: FILE_CREATION, FILE_DELETION, FILE_MODIFICATION, FILE_READ, and FILE_OPEN
- [`FILE_MODIFICATION`](event-guidance/file_modification.md) - section: FILE_CREATION, FILE_DELETION, FILE_MODIFICATION, FILE_READ, and FILE_OPEN
- [`FILE_OPEN`](event-guidance/file_open.md) - section: FILE_CREATION, FILE_DELETION, FILE_MODIFICATION, FILE_READ, and FILE_OPEN
- [`FILE_READ`](event-guidance/file_read.md) - section: FILE_CREATION, FILE_DELETION, FILE_MODIFICATION, FILE_READ, and FILE_OPEN
- [`MUTEX_CREATION`](event-guidance/mutex_creation.md)
- [`NETWORK_CONNECTION`](event-guidance/network_connection.md)
- [`NETWORK_HTTP`](event-guidance/network_http.md)
- [`PROCESS_INJECTION`](event-guidance/process_injection.md) - section: PROCESS_INJECTION, PROCESS_LAUNCH, PROCESS_OPEN, PROCESS_TERMINATION, PROCESS_UNCATEGORIZED
- [`PROCESS_LAUNCH`](event-guidance/process_launch.md) - section: PROCESS_INJECTION, PROCESS_LAUNCH, PROCESS_OPEN, PROCESS_TERMINATION, PROCESS_UNCATEGORIZED
- [`PROCESS_MODULE_LOAD`](event-guidance/process_module_load.md)
- [`PROCESS_OPEN`](event-guidance/process_open.md) - section: PROCESS_INJECTION, PROCESS_LAUNCH, PROCESS_OPEN, PROCESS_TERMINATION, PROCESS_UNCATEGORIZED
- [`PROCESS_PRIVILEGE_ESCALATION`](event-guidance/process_privilege_escalation.md)
- [`PROCESS_TERMINATION`](event-guidance/process_termination.md) - section: PROCESS_INJECTION, PROCESS_LAUNCH, PROCESS_OPEN, PROCESS_TERMINATION, PROCESS_UNCATEGORIZED
- [`PROCESS_UNCATEGORIZED`](event-guidance/process_uncategorized.md) - section: PROCESS_INJECTION, PROCESS_LAUNCH, PROCESS_OPEN, PROCESS_TERMINATION, PROCESS_UNCATEGORIZED
- [`REGISTRY_CREATION`](event-guidance/registry_creation.md) - section: REGISTRY_CREATION, REGISTRY_MODIFICATION, REGISTRY_DELETION
- [`REGISTRY_DELETION`](event-guidance/registry_deletion.md) - section: REGISTRY_CREATION, REGISTRY_MODIFICATION, REGISTRY_DELETION
- [`REGISTRY_MODIFICATION`](event-guidance/registry_modification.md) - section: REGISTRY_CREATION, REGISTRY_MODIFICATION, REGISTRY_DELETION
- [`SCAN_FILE`](event-guidance/scan_file.md) - section: SCAN_FILE, SCAN_HOST, SCAN_PROCESS, SCAN_VULN_HOST, SCAN_VULN_NETWORK
- [`SCAN_HOST`](event-guidance/scan_host.md) - section: SCAN_FILE, SCAN_HOST, SCAN_PROCESS, SCAN_VULN_HOST, SCAN_VULN_NETWORK
- [`SCAN_PROCESS`](event-guidance/scan_process.md) - section: SCAN_FILE, SCAN_HOST, SCAN_PROCESS, SCAN_VULN_HOST, SCAN_VULN_NETWORK
- [`SCAN_VULN_HOST`](event-guidance/scan_vuln_host.md) - section: SCAN_FILE, SCAN_HOST, SCAN_PROCESS, SCAN_VULN_HOST, SCAN_VULN_NETWORK
- [`SCAN_VULN_NETWORK`](event-guidance/scan_vuln_network.md) - section: SCAN_FILE, SCAN_HOST, SCAN_PROCESS, SCAN_VULN_HOST, SCAN_VULN_NETWORK
- [`SCHEDULED_TASK_CREATION`](event-guidance/scheduled_task_creation.md) - section: SCHEDULED_TASK_CREATION, SCHEDULED_TASK_DELETION, SCHEDULED_TASK_DISABLE, SCHEDULED_TASK_ENABLE, SCHEDULED_TASK_MODIFICATION, SCHEDULED_TASK_UNCATEGORIZED
- [`SCHEDULED_TASK_DELETION`](event-guidance/scheduled_task_deletion.md) - section: SCHEDULED_TASK_CREATION, SCHEDULED_TASK_DELETION, SCHEDULED_TASK_DISABLE, SCHEDULED_TASK_ENABLE, SCHEDULED_TASK_MODIFICATION, SCHEDULED_TASK_UNCATEGORIZED
- [`SCHEDULED_TASK_DISABLE`](event-guidance/scheduled_task_disable.md) - section: SCHEDULED_TASK_CREATION, SCHEDULED_TASK_DELETION, SCHEDULED_TASK_DISABLE, SCHEDULED_TASK_ENABLE, SCHEDULED_TASK_MODIFICATION, SCHEDULED_TASK_UNCATEGORIZED
- [`SCHEDULED_TASK_ENABLE`](event-guidance/scheduled_task_enable.md) - section: SCHEDULED_TASK_CREATION, SCHEDULED_TASK_DELETION, SCHEDULED_TASK_DISABLE, SCHEDULED_TASK_ENABLE, SCHEDULED_TASK_MODIFICATION, SCHEDULED_TASK_UNCATEGORIZED
- [`SCHEDULED_TASK_MODIFICATION`](event-guidance/scheduled_task_modification.md) - section: SCHEDULED_TASK_CREATION, SCHEDULED_TASK_DELETION, SCHEDULED_TASK_DISABLE, SCHEDULED_TASK_ENABLE, SCHEDULED_TASK_MODIFICATION, SCHEDULED_TASK_UNCATEGORIZED
- [`SCHEDULED_TASK_UNCATEGORIZED`](event-guidance/scheduled_task_uncategorized.md) - section: SCHEDULED_TASK_CREATION, SCHEDULED_TASK_DELETION, SCHEDULED_TASK_DISABLE, SCHEDULED_TASK_ENABLE, SCHEDULED_TASK_MODIFICATION, SCHEDULED_TASK_UNCATEGORIZED
- [`SERVICE_CREATION`](event-guidance/service_creation.md) - section: SERVICE_UNSPECIFIED, SERVICE_CREATION, SERVICE_DELETION, SERVICE_START, SERVICE_STOP
- [`SERVICE_DELETION`](event-guidance/service_deletion.md) - section: SERVICE_UNSPECIFIED, SERVICE_CREATION, SERVICE_DELETION, SERVICE_START, SERVICE_STOP
- [`SERVICE_START`](event-guidance/service_start.md) - section: SERVICE_UNSPECIFIED, SERVICE_CREATION, SERVICE_DELETION, SERVICE_START, SERVICE_STOP
- [`SERVICE_STOP`](event-guidance/service_stop.md) - section: SERVICE_UNSPECIFIED, SERVICE_CREATION, SERVICE_DELETION, SERVICE_START, SERVICE_STOP
- [`SERVICE_UNSPECIFIED`](event-guidance/service_unspecified.md) - section: SERVICE_UNSPECIFIED, SERVICE_CREATION, SERVICE_DELETION, SERVICE_START, SERVICE_STOP
- [`SETTING_CREATION`](event-guidance/setting_creation.md) - section: SETTING_UNCATEGORIZED, SETTING_CREATION, SETTING_MODIFICATION, SETTING_DELETION
- [`SETTING_DELETION`](event-guidance/setting_deletion.md) - section: SETTING_UNCATEGORIZED, SETTING_CREATION, SETTING_MODIFICATION, SETTING_DELETION
- [`SETTING_MODIFICATION`](event-guidance/setting_modification.md) - section: SETTING_UNCATEGORIZED, SETTING_CREATION, SETTING_MODIFICATION, SETTING_DELETION
- [`SETTING_UNCATEGORIZED`](event-guidance/setting_uncategorized.md) - section: SETTING_UNCATEGORIZED, SETTING_CREATION, SETTING_MODIFICATION, SETTING_DELETION
- [`STATUS_HEARTBEAT`](event-guidance/status_heartbeat.md) - section: STATUS_HEARTBEAT, STATUS_STARTUP, STATUS_SHUTDOWN, STATUS_UPDATE
- [`STATUS_SHUTDOWN`](event-guidance/status_shutdown.md) - section: STATUS_HEARTBEAT, STATUS_STARTUP, STATUS_SHUTDOWN, STATUS_UPDATE
- [`STATUS_STARTUP`](event-guidance/status_startup.md) - section: STATUS_HEARTBEAT, STATUS_STARTUP, STATUS_SHUTDOWN, STATUS_UPDATE
- [`STATUS_UPDATE`](event-guidance/status_update.md) - section: STATUS_HEARTBEAT, STATUS_STARTUP, STATUS_SHUTDOWN, STATUS_UPDATE
- [`SYSTEM_AUDIT_LOG_UNCATEGORIZED`](event-guidance/system_audit_log_uncategorized.md) - section: SYSTEM_AUDIT_LOG_UNCATEGORIZED, SYSTEM_AUDIT_LOG_WIPE
- [`SYSTEM_AUDIT_LOG_WIPE`](event-guidance/system_audit_log_wipe.md) - section: SYSTEM_AUDIT_LOG_UNCATEGORIZED, SYSTEM_AUDIT_LOG_WIPE
- [`USER_CHANGE_PASSWORD`](event-guidance/user_change_password.md) - section: USER_CHANGE_PASSWORD, USER_CHANGE_PERMISSIONS
- [`USER_CHANGE_PERMISSIONS`](event-guidance/user_change_permissions.md) - section: USER_CHANGE_PASSWORD, USER_CHANGE_PERMISSIONS
- [`USER_COMMUNICATION`](event-guidance/user_communication.md)
- [`USER_CREATION`](event-guidance/user_creation.md) - section: USER_CREATION, USER_DELETION
- [`USER_DELETION`](event-guidance/user_deletion.md) - section: USER_CREATION, USER_DELETION
- [`USER_LOGIN`](event-guidance/user_login.md) - section: USER_LOGIN, USER_LOGOUT
- [`USER_LOGOUT`](event-guidance/user_logout.md) - section: USER_LOGIN, USER_LOGOUT
- [`USER_RESOURCE_ACCESS`](event-guidance/user_resource_access.md)
- [`USER_RESOURCE_CREATION`](event-guidance/user_resource_creation.md) - section: USER_RESOURCE_CREATION, USER_RESOURCE_DELETION
- [`USER_RESOURCE_DELETION`](event-guidance/user_resource_deletion.md) - section: USER_RESOURCE_CREATION, USER_RESOURCE_DELETION
- [`USER_RESOURCE_UPDATE_CONTENT`](event-guidance/user_resource_update_content.md)
- [`USER_RESOURCE_UPDATE_PERMISSIONS`](event-guidance/user_resource_update_permissions.md)
- [`USER_UNCATEGORIZED`](event-guidance/user_uncategorized.md)
