# STATUS_UPDATE Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `STATUS_HEARTBEAT`, `STATUS_STARTUP`, `STATUS_SHUTDOWN`, `STATUS_UPDATE`
- Usage-guide section: `STATUS_HEARTBEAT, STATUS_STARTUP, STATUS_SHUTDOWN, STATUS_UPDATE`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- principal: At least one machine identifier (IP or MAC ADDRESS, hostname, or asset identifier).

## Optional Fields

No entries extracted.

## Notes

- The following example illustrates how an event of type STATUS_HEARTBEAT would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Device and location details.
- intermediary: Device IP address.
- security_result: Security result details.

## Examples

### UDM example for STATUS_HEARTBEAT

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
