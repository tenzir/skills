# SCAN_FILE Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `SCAN_FILE`, `SCAN_HOST`, `SCAN_PROCESS`, `SCAN_VULN_HOST`, `SCAN_VULN_NETWORK`
- Usage-guide section: `SCAN_FILE, SCAN_HOST, SCAN_PROCESS, SCAN_VULN_HOST, SCAN_VULN_NETWORK`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: event_timestamp and background information about the event.
- observer: Capture information about the scanner itself. If the scanner is remote, the machine details must be captured by the observer field. For a local scanner, leave empty.
- target: Capture information about the machine that holds the object being scanned. If a file is being scanned, target.file must capture information about the scanned file. If a process is being scanned, target.process must capture information about the scanned process.
- extensions: For SCAN_VULN_HOST and SCAN_VULN_NETWORK, define the vulnerability using the extensions.vuln field.

## Optional Fields

- principal: Represents the device initiating the connection and includes at least one machine identifier (for example, hostname, IP address, MAC address, proprietary asset identifier) or a user identifier.
- target: User detail about the target object (for example, file creator or process owner) should be captured in target.user.
- security_result: Describe the malicious activity detected.

## Notes

- The following example illustrates how an event of type SCAN_HOST would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- target: Device which received the malicious software.
- observer: Device which observes and reports on the event in question.
- security_result: Security details about the malicious software.
- The following example illustrates how an event of type SCAN_VULN_HOST would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Device that received the malicious software.
- extensions: Vulnerability details.

## Examples

### UDM example for SCAN_HOST (1)

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

### UDM example for SCAN_VULN_HOST (2)

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
