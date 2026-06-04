# Metadata.EventType

An event type. Choose event type not based on the product that generated the event but the one that logged the event itself. So, for example, an antivirus (AV) scanning email on a client would generate an SMTP_PROXY event, not an AV event. A DLP device scanning a web upload would generate an HTTP_PROXY event and not a DLP or process activity event. Note: In the case of a HTTP_PROXY event, you might also include process details if this occurred on an endpoint. That would be optional, but there are a certain set of required fields and banned fields due to its status as an HTTP_PROXY event.

## Values

0. `EVENTTYPE_UNSPECIFIED`: Default event type
10000. `PROCESS_UNCATEGORIZED`: Activity related to a process which does not match any other event types.
10001. `PROCESS_LAUNCH`: Process launch.
10002. `PROCESS_INJECTION`: Process injecting into another process.
10003. `PROCESS_PRIVILEGE_ESCALATION`: Process privilege escalation.
10004. `PROCESS_TERMINATION`: Process termination.
10005. `PROCESS_OPEN`: Process being opened.
10006. `PROCESS_MODULE_LOAD`: Process loading a module.
11000. `REGISTRY_UNCATEGORIZED`: Registry event which does not match any of the other event types.
11001. `REGISTRY_CREATION`: Registry creation.
11002. `REGISTRY_MODIFICATION`: Registry modification.
11003. `REGISTRY_DELETION`: Registry deletion.
12000. `SETTING_UNCATEGORIZED`: Settings-related event which does not match any of the other event types.
12001. `SETTING_CREATION`: Setting creation.
12002. `SETTING_MODIFICATION`: Setting modification.
12003. `SETTING_DELETION`: Setting deletion.
13000. `MUTEX_UNCATEGORIZED`: Any mutex event other than creation.
13001. `MUTEX_CREATION`: Mutex creation.
14000. `FILE_UNCATEGORIZED`: File event which does not match any of the other event types.
14001. `FILE_CREATION`: File created.
14002. `FILE_DELETION`: File deleted.
14003. `FILE_MODIFICATION`: File modified.
14004. `FILE_READ`: File read.
14005. `FILE_COPY`: File copied. Used for file copies, for example, to a thumb drive.
14006. `FILE_OPEN`: File opened.
14007. `FILE_MOVE`: File moved or renamed.
14008. `FILE_SYNC`: File synced (for example, Google Drive, Dropbox, backup).
15000. `USER_UNCATEGORIZED`: User activity which does not match any of the other event types.
15001. `USER_LOGIN`: User login.
15002. `USER_LOGOUT`: User logout.
15003. `USER_CREATION`: User creation.
15004. `USER_CHANGE_PASSWORD`: User password change event.
15005. `USER_CHANGE_PERMISSIONS`: Change in user permissions.
15006. `USER_STATS` (deprecated): Deprecated. Used to update user info for an LDAP dump.
15007. `USER_BADGE_IN`: User physically badging into a location.
15008. `USER_DELETION`: User deletion.
15009. `USER_RESOURCE_CREATION`: User creating a virtual resource. This is equivalent to RESOURCE_CREATION.
15010. `USER_RESOURCE_UPDATE_CONTENT`: User updating content of a virtual resource. This is equivalent to RESOURCE_WRITTEN.
15011. `USER_RESOURCE_UPDATE_PERMISSIONS`: User updating permissions of a virtual resource. This is equivalent to RESOURCE_PERMISSIONS_CHANGE.
15012. `USER_COMMUNICATION`: User initiating communication through a medium (for example, video).
15013. `USER_RESOURCE_ACCESS`: User accessing a virtual resource. This is equivalent to RESOURCE_READ.
15014. `USER_RESOURCE_DELETION`: User deleting a virtual resource. This is equivalent to RESOURCE_DELETION.
23000. `GROUP_UNCATEGORIZED`: A group activity that does not fall into one of the other event types.
23001. `GROUP_CREATION`: A group creation.
23002. `GROUP_DELETION`: A group deletion.
23003. `GROUP_MODIFICATION`: A group modification.
19000. `EMAIL_UNCATEGORIZED`: Email messages
19001. `EMAIL_TRANSACTION`: An email transaction.
19002. `EMAIL_URL_CLICK` (deprecated): Deprecated: use NETWORK_HTTP instead. An email URL click event.
16000. `NETWORK_UNCATEGORIZED`: A network event that does not fit into one of the other event types.
16001. `NETWORK_FLOW`: Aggregated flow stats like netflow.
16002. `NETWORK_CONNECTION`: Network connection details like from a FW.
16003. `NETWORK_FTP`: FTP telemetry.
16004. `NETWORK_DHCP`: DHCP payload.
16005. `NETWORK_DNS`: DNS payload.
16006. `NETWORK_HTTP`: HTTP telemetry.
16007. `NETWORK_SMTP`: SMTP telemetry.
17000. `STATUS_UNCATEGORIZED`: A status message that does not fit into one of the other event types.
17001. `STATUS_HEARTBEAT`: Heartbeat indicating product is alive.
17002. `STATUS_STARTUP`: An agent startup.
17003. `STATUS_SHUTDOWN`: An agent shutdown.
17004. `STATUS_UPDATE`: A software or fingerprint update.
18000. `SCAN_UNCATEGORIZED`: Scan item that does not fit into one of the other event types.
18001. `SCAN_FILE`: A file scan.
18002. `SCAN_PROCESS_BEHAVIORS` (deprecated): Scan process behaviors. Please use SCAN_PROCESS instead.
18003. `SCAN_PROCESS`: Scan process.
18004. `SCAN_HOST`: Scan results from scanning an entire host device for threats/sensitive documents.
18005. `SCAN_VULN_HOST`: Vulnerability scan logs about host vulnerabilities (e.g., out of date software) and network vulnerabilities (e.g., unprotected service detected via a network scan).
18006. `SCAN_VULN_NETWORK`: Vulnerability scan logs about network vulnerabilities.
18007. `SCAN_NETWORK`: Scan network for suspicious activity
20000. `SCHEDULED_TASK_UNCATEGORIZED`: Scheduled task event that does not fall into one of the other event types.
20001. `SCHEDULED_TASK_CREATION`: Scheduled task creation.
20002. `SCHEDULED_TASK_DELETION`: Scheduled task deletion.
20003. `SCHEDULED_TASK_ENABLE`: Scheduled task being enabled.
20004. `SCHEDULED_TASK_DISABLE`: Scheduled task being disabled.
20005. `SCHEDULED_TASK_MODIFICATION`: Scheduled task being modified.
21000. `SYSTEM_AUDIT_LOG_UNCATEGORIZED`: A system audit log event that is not a wipe.
21001. `SYSTEM_AUDIT_LOG_WIPE`: A system audit log wipe.
22000. `SERVICE_UNSPECIFIED`: Service event that does not fit into one of the other event types.
22001. `SERVICE_CREATION`: A service creation.
22002. `SERVICE_DELETION`: A service deletion.
22003. `SERVICE_START`: A service start.
22004. `SERVICE_STOP`: A service stop.
22005. `SERVICE_MODIFICATION`: A service modification.
100000. `GENERIC_EVENT`: Operating system events that are not described by any of the other event types. Might include uncategorized Microsoft Windows event logs.
1. `RESOURCE_CREATION`: The resource was created/provisioned. This is equivalent to USER_RESOURCE_CREATION.
2. `RESOURCE_DELETION`: The resource was deleted/deprovisioned. This is equivalent to USER_RESOURCE_DELETION.
3. `RESOURCE_PERMISSIONS_CHANGE`: The resource had it's permissions or ACLs updated. This is equivalent to USER_RESOURCE_UPDATE_PERMISSIONS.
4. `RESOURCE_READ`: The resource was read. This is equivalent to USER_RESOURCE_ACCESS.
5. `RESOURCE_WRITTEN`: The resource was written to. This is equivalent to USER_RESOURCE_UPDATE_CONTENT.
25000. `DEVICE_FIRMWARE_UPDATE`: Firmware update.
25001. `DEVICE_CONFIG_UPDATE`: Configuration update.
25002. `DEVICE_PROGRAM_UPLOAD`: A program or application uploaded to a device.
25003. `DEVICE_PROGRAM_DOWNLOAD`: A program or application downloaded to a device.
24000. `ANALYST_UPDATE_VERDICT`: Analyst update about the Verdict (such as true positive, false positive, or disregard) of a finding.
24001. `ANALYST_UPDATE_REPUTATION`: Analyst update about the Reputation (such as useful or not useful) of a finding.
24002. `ANALYST_UPDATE_SEVERITY_SCORE`: Analyst update about the Severity score (0-100) of a finding.
24007. `ANALYST_UPDATE_STATUS`: Analyst update about the finding status.
24008. `ANALYST_ADD_COMMENT`: Analyst addition of a comment for a finding.
24009. `ANALYST_UPDATE_PRIORITY`: Analyst update about the priority (such as low, medium, or high) for a finding.
24010. `ANALYST_UPDATE_ROOT_CAUSE`: Analyst update about the root cause for a finding.
24011. `ANALYST_UPDATE_REASON`: Analyst update about the reason (such as malicious or not malicious) for a finding.
24012. `ANALYST_UPDATE_RISK_SCORE`: Analyst update about the risk score (0-100) of a finding.
26000. `ENTITY_RISK_CHANGE`: An update to an entity risk score. This event type is restricted to events published by Google Securit Operations Risk Analytics.
27000. `TRIAGE_AGENT_UPDATE_INVESTIGATION`: Triage Agent has investigated the finding.
