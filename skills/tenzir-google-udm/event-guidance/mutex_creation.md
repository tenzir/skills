# MUTEX_CREATION Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `MUTEX_CREATION`
- Usage-guide section: `MUTEX_CREATION`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- principal: At least one machine identifier. Populate principal.process with information about the process creating the mutex.
- target: Populate target.resource. Populate target.resource.type with MUTEX. Populate target.resource.name with the name of the mutex created.

## Optional Fields

- security_result: Describe the malicious activity detected.
- principal.user: Populate if user information is available about the process.

## Notes

- The following example illustrates how an event of type MUTEX_CREATION would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Device and process details.
- target: Information about the mutex.

## Examples

### UDM example for MUTEX_CREATION

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
