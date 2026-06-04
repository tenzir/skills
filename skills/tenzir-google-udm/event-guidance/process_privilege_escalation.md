# PROCESS_PRIVILEGE_ESCALATION Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `PROCESS_PRIVILEGE_ESCALATION`
- Usage-guide section: `PROCESS_PRIVILEGE_ESCALATION`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- principal: At least one machine identifier. principal.process: Process loading the module. principal.user: User loading the module.

## Optional Fields

- security_result: Describe the malicious activity detected.

## Notes

- The following example illustrates how you would format a PROCESS_PRIVILEGE_ESCALATION event using the Google SecOps UDM syntax:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Details about the device, the user, and the process loading the module.
- target: Process and module details.

## Examples

### UDM example for PROCESS_PRIVILEGE_ESCALATION

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
