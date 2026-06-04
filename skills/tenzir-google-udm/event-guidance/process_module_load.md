# PROCESS_MODULE_LOAD Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `PROCESS_MODULE_LOAD`
- Usage-guide section: `PROCESS_MODULE_LOAD`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- principal: At least one machine identifier. principal.process: Process loading the module.
- target: target.process: Includes information about the process. target.process.file: Module loaded (for example, the DLL or shared object).

## Optional Fields

- security_result: Describe the malicious activity detected.
- principal.user: Populate if user information is available about the process.

## Notes

- The following example illustrates how you would format a PROCESS_MODULE_LOAD event using the Google SecOps UDM syntax:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Details about the device and the process loading the module.
- target: Process and module details.

## Examples

### UDM example for PROCESS_MODULE_LOAD

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
