# SYSTEM_AUDIT_LOG_UNCATEGORIZED Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `SYSTEM_AUDIT_LOG_UNCATEGORIZED`, `SYSTEM_AUDIT_LOG_WIPE`
- Usage-guide section: `SYSTEM_AUDIT_LOG_UNCATEGORIZED, SYSTEM_AUDIT_LOG_WIPE`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- principal: Include a user identifier for the user who performed the operation on the log and a machine identifier for the machine where the log is or was (in the case of wiping) stored.

## Optional Fields

No entries extracted.

## Notes

- The following example illustrates how an event of type SYSTEM_AUDIT_LOG_WIPE would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Device and user details.

## Examples

### UDM example for SYSTEM_AUDIT_LOG_WIPE

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
