# PROCESS_INJECTION Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `PROCESS_INJECTION`, `PROCESS_LAUNCH`, `PROCESS_OPEN`, `PROCESS_TERMINATION`, `PROCESS_UNCATEGORIZED`
- Usage-guide section: `PROCESS_INJECTION, PROCESS_LAUNCH, PROCESS_OPEN, PROCESS_TERMINATION, PROCESS_UNCATEGORIZED`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- principal: At least one machine identifier. For process injection and process termination events, if available, principal.process must include information about the process initiating the action (for example, for a process launch event, principal.process must include details about the parent process if available).
- target: target.process: Includes information about the process that is being injected, opened, launched, or terminated. If the target process is remote, target must include at least one machine identifier for the target machine (for example, an IP address, MAC, hostname, or third-party asset identifier).

## Optional Fields

- security_result: Describe the malicious activity detected.
- principal.user and target.user: Populate the initiating process (principal) and the target process if the user information is available.

## Notes

- The following example illustrates how you would format a PROCESS_LAUNCH event using the Google SecOps UDM syntax:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Device details.
- target: Process details.

## Examples

### UDM example for PROCESS_LAUNCH

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
