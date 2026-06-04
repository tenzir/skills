# Event Types

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
## Guidance

Population guidance from the [Google UDM usage guide](https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en); Google last updated: `2026-06-03 UTC`.

<a id="email_transaction"></a>

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

<a id="file_creation"></a>
<a id="file_deletion"></a>
<a id="file_modification"></a>
<a id="file_read"></a>
<a id="file_open"></a>

### File Creation / Deletion / Modification / Read / Open Events

Applies to: `FILE_CREATION`, `FILE_DELETION`, `FILE_MODIFICATION`, `FILE_READ`, `FILE_OPEN`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. (Optional) Populate `principal.process` with information about the process accessing the file.
- `target`: If the file is remote (for example SMB share), the target must include at least one machine identifier for the target machine, otherwise all machine identifiers must be blank. Populate `target.file` with information about the file.

#### Optional Fields

- `security_result`: Describe the malicious activity detected.
- `principal.user`: Populate if user information is available about the process.

<a id="file_copy"></a>

### FILE_COPY

#### Required Fields

- `metadata`: Include the required fields as described.
- `principal`: At least one machine identifier. (Optional) Populate `principal.process` with information about the process performing the file copy operation.
- `src`: Populate `src.file` with information about the source file. If the file is remote (for example SMB share), src must include at least one machine identifier for the source machine storing the source file.
- `target`: Populate `target.file` with information about the target file. If the file is remote (for example SMB share), the `target` field must include at least one machine identifier for the target machine that holds the target file.

#### Optional Fields

- `security_result`: Describe the malicious activity detected.
- `principal.user`: Populate if user information is available about the process.

<a id="mutex_creation"></a>

### MUTEX_CREATION

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. Populate `principal.process` with information about the process creating the mutex.
- `target`: Populate `target.resource`. Populate `target.resource.type` with MUTEX. Populate `target.resource.name` with the name of the mutex created.

#### Optional Fields

- `security_result`: Describe the malicious activity detected.
- `principal.user`: Populate if user information is available about the process.

#### Notes

- The following example illustrates how an event of type MUTEX_CREATION would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Device and process details.
- `target`: Information about the mutex.

#### Examples

##### UDM example for MUTEX_CREATION

```text
metadata {
  event_timestamp: "2020-01-01T13:27:41+00:00"
  event_type: MUTEX_CREATION
  vendor_name: "Microsoft"
  product_name: "Windows"
}
principal {
  hostname: "test.altostrat.com"
  process {
    pid: "0xc45"
    file {
      full_path: "C:\\Windows\\regedit.exe"
    }
  }
}
target {
  resource {
    type: "MUTEX"
    name: "test-mutex"
  }
}
```

<a id="network_connection"></a>

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

<a id="network_http"></a>

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
- The following example illustrates how a Sophos antivirus event of type NETWORK_HTTP would be converted to the Google SecOps UDM format.
- The following is the original Sophos antivirus event:
- Here is how you would format the same information in Proto3 using the Google SecOps UDM syntax:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Security device that detected the event.
- `target`: Device that received the malicious software.
- `network`: Network information about the malicious host.
- `security_result`: Security details about the malicious software.
- `additional`: Vendor information outside the scope of the UDM.

#### Examples

##### UDM example for NETWORK_HTTP (1)

```text
date=2013-08-07 time=13:27:41 timezone="GMT" device_name="CC500ia" device_id= C070123456-ABCDE log_id=030906208001 log_type="Anti-Virus" log_component="HTTP" log_subtype="Virus" status="" priority=Critical fw_rule_id=0 user_name="john.smith" iap=7 av_policy_name="" virus="TR/ElderadoB.A.78" url="altostrat.fr/img/logo.gif" domainname="altostrat.fr" src_ip=10.10.2.10 src_port=60671 src_country_code= dst_ip=203.0.113.31 dst_port=80 dst_country_code=FRA
```

##### UDM example for NETWORK_HTTP (2)

```text
metadata {
  event_timestamp: "2013-08-07T13:27:41+00:00"
  event_type: NETWORK_HTTP
  product_name: "Sophos Antivirus"
  product_log_id: "030906208001"
}

principal {
  hostname: "CC500ia"
  asset_id: "Sophos.AV:C070123456-ABCDE"
  ip: "10.10.2.10"
  port: 60671
  user {  userid: "john.smith" }
}

target {
  hostname: "altostrat.fr"
  ip: "203.0.113.31"
  port: 80
  url: "altostrat.fr/img/logo.gif"
}

network {
  ip_protocol: TCP
 }

security_result {
  about {
    url: "altostrat.fr/img/logo.gif"
    category: SOFTWARE_MALICIOUS
    category_details: "Virus"
    threat_name: "TR/ElderadoB.A.78"
    severity: HIGH                   # Google Security Operations-normalized severity
    severity_details: "Critical"    # Vendor-specific severity string
  }
}

additional { "dst_country_code" : "FRA", "iap" : "7" "fw_rule_id" : "0" }
```

<a id="process_injection"></a>
<a id="process_launch"></a>
<a id="process_open"></a>
<a id="process_termination"></a>
<a id="process_uncategorized"></a>

### Process Injection / Launch / Open / Termination / Uncategorized Events

Applies to: `PROCESS_INJECTION`, `PROCESS_LAUNCH`, `PROCESS_OPEN`, `PROCESS_TERMINATION`, `PROCESS_UNCATEGORIZED`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. For process injection and process termination events, if available, `principal.process` must include information about the process initiating the action (for example, for a process launch event, `principal.process` must include details about the parent process if available).
- `target`: `target.process`: Includes information about the process that is being injected, opened, launched, or terminated. If the target process is remote, target must include at least one machine identifier for the target machine (for example, an IP address, MAC, hostname, or third-party asset identifier).

#### Optional Fields

- `security_result`: Describe the malicious activity detected.
- `principal.user` and `target.user`: Populate the initiating process (principal) and the target process if the user information is available.

#### Notes

- The following example illustrates how you would format a PROCESS_LAUNCH event using the Google SecOps UDM syntax:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Device details.
- `target`: Process details.

#### Examples

##### UDM example for PROCESS_LAUNCH

```text
metadata {
  event_timestamp: "2020-01-01T13:27:41+00:00"
  event_type: PROCESS_LAUNCH
  vendor_name: "Microsoft"
  product_name: "Windows"
}
principal {
  hostname: "altostrat.com"
}
target {
  process {
    pid: "0xc45"
    file {
      full_path: "C:\\Windows\\regedit.exe"
    }
  }
}
```

<a id="process_module_load"></a>

### PROCESS_MODULE_LOAD

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. `principal.process`: Process loading the module.
- `target`: `target.process`: Includes information about the process. `target.process.file`: Module loaded (for example, the DLL or shared object).

#### Optional Fields

- `security_result`: Describe the malicious activity detected.
- `principal.user`: Populate if user information is available about the process.

#### Notes

- The following example illustrates how you would format a PROCESS_MODULE_LOAD event using the Google SecOps UDM syntax:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Details about the device and the process loading the module.
- `target`: Process and module details.

#### Examples

##### UDM example for PROCESS_MODULE_LOAD

```text
metadata {
  event_timestamp: "2020-01-01T13:27:41+00:00"
  event_type: PROCESS_MODULE_LOAD
  vendor_name: "Microsoft"
  product_name: "Windows"
}
principal {
  hostname: "example.com"
  process {
    pid: "0x123"
  }
}
target {
  process {
    pid: "0xc45"
    file {
      full_path: "C:\\Windows\\regedit.exe"
    }
  }
}
```

<a id="process_privilege_escalation"></a>

### PROCESS_PRIVILEGE_ESCALATION

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. `principal.process`: Process loading the module. `principal.user`: User loading the module.

#### Optional Fields

- `security_result`: Describe the malicious activity detected.

#### Notes

- The following example illustrates how you would format a PROCESS_PRIVILEGE_ESCALATION event using the Google SecOps UDM syntax:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Details about the device, the user, and the process loading the module.
- `target`: Process and module details.

#### Examples

##### UDM example for PROCESS_PRIVILEGE_ESCALATION

```text
metadata {
  event_timestamp: "2020-01-01T13:27:41+00:00"
  event_type: PROCESS_PRIVILEGE_ESCALATION
  vendor_name: "Microsoft"
  product_name: "Windows"
}
principal {
  hostname: "example.com"
  process {
    pid: "0x123"
  }
  user {
    userid: "test"
    windows_sid: "ABCDEFGH-123456789-1111111-1000"
  }
}
target {
  process {
    pid: "0xc45"
    file {
      full_path: "C:\\Windows\\regedit.exe"
    }
  }
}
```

<a id="registry_creation"></a>
<a id="registry_modification"></a>
<a id="registry_deletion"></a>

### Registry Creation / Modification / Deletion Events

Applies to: `REGISTRY_CREATION`, `REGISTRY_MODIFICATION`, `REGISTRY_DELETION`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier. If a user-mode process performs the registry modification, `principal.process` must include information about the process modifying the registry. If a kernel process performs the registry modification, the principal must not include process information.
- `target`: `target.registry`: If the target registry is remote, target must include at least one identifier for the target machine (for example, an IP address, MAC, hostname, or third party asset identifier). `target.registry.registry_key`: All registry events must include the affected registry key.

#### Optional Fields

- `security_result`: Describe the malicious activity detected. For example, a bad registry key.
- `principal.user`: Populate if user information is available about the process.

#### Notes

- The following example illustrates how you would format a REGISTRY_MODIFICATION event in Proto3 using the Google SecOps UDM syntax:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Device, user, and process details.
- `target`: Registry entry affected by the modification.

#### Examples

##### UDM example for REGISTRY_MODIFICATION

```text
metadata {
  event_timestamp: "2020-01-01T13:27:41+00:00"
  event_type: REGISTRY_MODIFICATION
  vendor_name: "Microsoft"
  product_name: "Windows"
}
principal {
  hostname: "test-win"
  user {
    userid: "test"
    windows_sid: "ABCDEFGH-123456789-1111111-1000"
  }
  process {
    pid: "0xc45"
    file {
      full_path: "C:\\Windows\\regedit.exe"
    }
  }
}
target {
  registry {
    registry_key: "\\REGISTRY\\USER\\TEST_USER\\Control Panel\\PowerCfg\\PowerPolicy"
    registry_value_name: "Description"
    registry_value_data: "For extending battery life."
  }
}
```

<a id="scan_file"></a>
<a id="scan_host"></a>
<a id="scan_process"></a>
<a id="scan_vuln_host"></a>
<a id="scan_vuln_network"></a>

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

#### Notes

- The following example illustrates how an event of type SCAN_HOST would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `target`: Device which received the malicious software.
- `observer`: Device which observes and reports on the event in question.
- `security_result`: Security details about the malicious software.
- The following example illustrates how an event of type SCAN_VULN_HOST would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Device that received the malicious software.
- `extensions`: Vulnerability details.

#### Examples

##### UDM example for SCAN_HOST (1)

```text
metadata: {
  event_timestamp: {
    seconds: 1571386978
  }
  event_type: SCAN_HOST
  vendor_name: "vendor"
  product_name: "product"
  product_version: "1.0"
}
target: {
  hostname: "testHost"
  asset_id: "asset"
  ip: "192.168.200.200"
}
observer: {
  hostname: "testObserver"
  ip: "192.168.100.100"
}
security_result: {
  severity: LOW
  confidence: HIGH_CONFIDENCE
}
```

##### UDM example for SCAN_VULN_HOST (2)

```text
metadata: {
  event_timestamp: "2025-05-09T12:59:52.45298Z",
  event_type: 18005,
  product_name: "TestProduct",
  vendor_name: "TestVendor"
  },
principal {
  asset_id: "TEST:Mwl8ABcd",
  ip: "127.0.0.3",
  hostname: "TEST-Localhost",
  mac: ["02:00:00:00:00:01"]
  },
extensions: {
  vulns: {
    vulnerabilities: [
      {
      cve_id: "CVE-6l9VxQmz",
      vendor_vulnerability_id: "TEST:7gmCmFWX",
      name: "CVE pA7DzwPU",
      severity: 2,
      vendor: "TestVendor",
      last_found: "2025-05-09T14:59:52.45300Z",
      first_found: "2025-05-09T13:59:52.45300Z"
       }
      ]
    }
  }
```

<a id="scheduled_task_creation"></a>
<a id="scheduled_task_deletion"></a>
<a id="scheduled_task_disable"></a>
<a id="scheduled_task_enable"></a>
<a id="scheduled_task_modification"></a>
<a id="scheduled_task_uncategorized"></a>

### Scheduled Task Creation / Deletion / Disable / Enable / Modification / Uncategorized Events

Applies to: `SCHEDULED_TASK_CREATION`, `SCHEDULED_TASK_DELETION`, `SCHEDULED_TASK_DISABLE`, `SCHEDULED_TASK_ENABLE`, `SCHEDULED_TASK_MODIFICATION`, `SCHEDULED_TASK_UNCATEGORIZED`

#### Required Fields

- `principal`: For all SCHEDULED_TASK events, principal must include a machine identifier and a user identifier.
- `target`: Target must include a valid resource and a resource type defined as "TASK".

#### Optional Fields

- `security_result`: Describe the malicious activity detected.

#### Notes

- The following example illustrates how an event of type SCHEDULED_TASK_CREATION could be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Device that scheduled the suspicious task.
- `target`: Software targeted by the suspicious task.
- `intermediary`: Intermediary involved with the suspicious task.
- `security_result`: Security details about the suspicious task.

#### Examples

##### UDM example for SCHEDULED_TASK_CREATION

```text
metadata: {
  event_timestamp: {
    seconds: 1577577998
  }
  event_type: SCHEDULED_TASK_CREATION
  vendor_name: "Microsoft"
  product_name: "Windows"
}
principal: {
  hostname: "fake-host.altostrat.com"
  user: {
    userid: "TestUser"
    windows_sid: "AB123CDE"
  }
  process {
    pid: "1234"
  }
}
target: {
  resource: {
    type: "TASK"
    name: "\\Adobe Acrobat Update Task"
  }
}
intermediary: {
  hostname: "fake-intermediary.altostrat.com"
}
security_result: {
  rule_name: "EventID: 6789"
  summary: "A scheduled task was created."
  severity: INFORMATIONAL
}
```

<a id="setting_uncategorized"></a>
<a id="setting_creation"></a>
<a id="setting_modification"></a>
<a id="setting_deletion"></a>

### Setting Uncategorized / Creation / Modification / Deletion Events

Applies to: `SETTING_UNCATEGORIZED`, `SETTING_CREATION`, `SETTING_MODIFICATION`, `SETTING_DELETION`

#### Required Fields

- `principal`: Must be present, non-empty, and include a machine identifier.
- `target`: Must be present, non-empty, and include a resource with its type specified as SETTING

#### Notes

- The following example illustrates how an event of type SETTING_MODIFICATION would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Information about the device on which the setting modification occurred.
- `target`: Resource details.

#### Examples

##### UDM example for event type SETTING_MODIFICATION

```text
metadata {
  event_timestamp: "2020-01-01T13:27:41+00:00"
  event_type: SETTING_MODIFICATION
  vendor_name: "Microsoft"
  product_name: "Windows"
}
principal {
  hostname: "test.win.com"
}
target {
  resource {
    type: "SETTING"
    name: "test-setting"
  }
}
```

<a id="service_unspecified"></a>
<a id="service_creation"></a>
<a id="service_deletion"></a>
<a id="service_start"></a>
<a id="service_stop"></a>

### Service Unspecified / Creation / Deletion / Start / Stop Events

Applies to: `SERVICE_UNSPECIFIED`, `SERVICE_CREATION`, `SERVICE_DELETION`, `SERVICE_START`, `SERVICE_STOP`

#### Required Fields

- `target`: Include the user identifier and specify either process or application.
- `principal`: Include at least one machine identifier (IP or MAC ADDRESS, hostname, or asset identifier).

#### Notes

- The following example illustrates how an event of type SERVICE_UNSPECIFIED would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Device and location details.
- `target`: Hostname and user identifier.
- `application`: Application name and resource type.

#### Examples

##### UDM example for SERVICE_UNSPECIFIED

```text
metadata: {
 event_timestamp: {
   seconds: 1595656745
   nanos: 832000000
    }
 event_type: SERVICE_UNSPECIFIED
   vendor_name: "Preempt"
   product_name: "PREEMPT_AUTH"
   product_event_type: "SERVICE_ACCESS"
   description: "Remote Procedures (RPC)"
   }
 principal: {
   hostname: "XXX-YYY-ZZZ"
   ip: "10.10.10.10"
   }
 target: {
   hostname: "TestHost"
   user: {
      userid: "ORG\\User"
      user_display_name: "user name"
   }
 application: "application.name"
   resource: {
      type: "Service Type"
      name: "RPC"
   }
 }
```

<a id="status_heartbeat"></a>
<a id="status_startup"></a>
<a id="status_shutdown"></a>
<a id="status_update"></a>

### Status Heartbeat / Startup / Shutdown / Update Events

Applies to: `STATUS_HEARTBEAT`, `STATUS_STARTUP`, `STATUS_SHUTDOWN`, `STATUS_UPDATE`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: At least one machine identifier (IP or MAC ADDRESS, hostname, or asset identifier).

#### Notes

- The following example illustrates how an event of type STATUS_HEARTBEAT would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Device and location details.
- `intermediary`: Device IP address.
- `security_result`: Security result details.

#### Examples

##### UDM example for STATUS_HEARTBEAT

```text
metadata: {
  event_timestamp: {
    seconds: 1588180305
  }
  event_type: STATUS_HEARTBEAT
  vendor_name: "DMP"
  product_name: "ENTRE"
}
principal: {
  hostname: "testHost"
  location: {
    name: "Building 1"
  }
}
intermediary: {
  ip: "8.8.8.8"
}
security_result: {
  summary: "Event - Locked"
  description: "description"
  severity: LOW
  severity_details: "INFO"
}
```

<a id="system_audit_log_uncategorized"></a>
<a id="system_audit_log_wipe"></a>

### System Audit Log Uncategorized / Wipe Events

Applies to: `SYSTEM_AUDIT_LOG_UNCATEGORIZED`, `SYSTEM_AUDIT_LOG_WIPE`

#### Required Fields

- `principal`: Include a user identifier for the user who performed the operation on the log and a machine identifier for the machine where the log is or was (in the case of wiping) stored.

#### Notes

- The following example illustrates how an event of type SYSTEM_AUDIT_LOG_WIPE would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- `metadata`: Background information about the event.
- `principal`: Device and user details.

#### Examples

##### UDM example for SYSTEM_AUDIT_LOG_WIPE

```text
metadata {
  event_timestamp: "2020-01-01T13:27:41+00:00"
  event_type: SYSTEM_AUDIT_LOG_WIPE
  vendor_name: "Microsoft"
  product_name: "Windows"
}
principal {
  hostname: "altostrat.com"
  user {
    userid: "test"
    windows_sid: "ABCDEFGH-123456789-1111111-1000"
  }
}
```

<a id="user_change_password"></a>
<a id="user_change_permissions"></a>

### User Change Password / Permissions Events

Applies to: `USER_CHANGE_PASSWORD`, `USER_CHANGE_PERMISSIONS`

#### Required Fields

- `metadata`: Include the required fields.
- `principal`: If the user account is modified from a remote location, populate principal with information about the machine from where the user modification originated.
- `target`: Populate `target.user` with information about the user that has been modified.
- `intermediary`: For SSO logins, intermediary must include at least one machine identifier for the SSO server if available.

<a id="user_communication"></a>

### USER_COMMUNICATION

#### Required Fields

- `principal`: Populate the `principal.user` field with details associated with user-initiated (sender) communication, such as a chat message in Google Chat or Slack, a video or voice conference in Zoom or Google Meet, or a VoIP connection.

#### Optional Fields

- `target`: (Recommended) Populate the `target.user` field with information about the target user (receiver) of the cloud communication resource. Populate the `target.application` field with information about the target cloud communication application.

<a id="user_creation"></a>
<a id="user_deletion"></a>

### User Creation / Deletion Events

Applies to: `USER_CREATION`, `USER_DELETION`

#### Required Fields

- `metadata`: `event_timestamp`.
- `principal`: Include information about the machine where the request to create or delete the user originated from. For a local user creation or deletion, principal must include at least one machine identifier for the originating machine.
- `target`: Location where the user is being created. Must also include user information (for example, `target.user`).

#### Optional Fields

- `principal`: User and process details for the machine where the user creation or deletion request was initiated.
- `target`: Information about the target machine (if different than the principal machine).

<a id="user_login"></a>
<a id="user_logout"></a>

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

<a id="user_resource_access"></a>

### USER_RESOURCE_ACCESS

#### Required Fields

- `principal`: Populate the `principal.user` field with details about attempts to access a cloud resource (for example, a Salesforce case, Office365 calendar, Google Doc, or ServiceNow ticket).
- `target`: Populate the `target.resource` field with information about the target cloud resource.

#### Optional Fields

- `target.application`: (Recommended) Populate the `target.application` field with information about the target cloud application.

<a id="user_resource_creation"></a>
<a id="user_resource_deletion"></a>

### User Resource Creation / Deletion Events

Applies to: `USER_RESOURCE_CREATION`, `USER_RESOURCE_DELETION`

#### Required Fields

- `principal`: Populate the `principal.user` field with details associated with the user created within a cloud resource (for example, a Salesforce case, Office 365 calendar, Google Doc, or ServiceNow ticket).
- `target`: Populate the `target.resource` field with information about the target cloud resource.

#### Optional Fields

- `target.application`: (Recommended) Populate the `target.application` field with information about the target cloud application.

<a id="user_resource_update_content"></a>

### USER_RESOURCE_UPDATE_CONTENT

#### Required Fields

- `principal`: Populate the `principal.user` field with details associated with the user whose content was updated within a cloud resource (for example, a Salesforce case, Office365 calendar, Google Doc, or ServiceNow ticket).
- `target`: Populate the `target.resource` field with information about the target cloud resource.

#### Optional Fields

- `target.application`: (Recommended) Populate the `target.application` field with information about the target cloud application.

<a id="user_resource_update_permissions"></a>

### USER_RESOURCE_UPDATE_PERMISSIONS

#### Required Fields

- `principal`: Populate the `principal.user` field with details associated with the user whose permissions were updated within a cloud resource (for example, a Salesforce case, Office 365 calendar, Google Doc, or ServiceNow ticket).
- `target`: Populate the `target.resource` field with information about the target cloud resource.

#### Optional Fields

- `target.application`: (Recommended) Populate the `target.application` field with information about the target cloud application.

<a id="user_uncategorized"></a>

### USER_UNCATEGORIZED

#### Required Fields

- `metadata`: `event_timestamp`
- `principal`: Include information about the machine where the request to create or delete the user originated from. For a local user creation or deletion, principal must include at least one machine identifier for the originating machine.
- `target`: Location where the user is being created. Must also include user information (for example, `target.user`).

#### Optional Fields

- `principal`: User and process details for the machine where the user creation or deletion request was initiated.
- `target`: Information about the target machine (if different than the principal machine).
