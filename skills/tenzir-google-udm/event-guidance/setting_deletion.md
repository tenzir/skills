# SETTING_DELETION Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `SETTING_UNCATEGORIZED`, `SETTING_CREATION`, `SETTING_MODIFICATION`, `SETTING_DELETION`
- Usage-guide section: `SETTING_UNCATEGORIZED, SETTING_CREATION, SETTING_MODIFICATION, SETTING_DELETION`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- principal: Must be present, non-empty, and include a machine identifier.
- target: Must be present, non-empty, and include a resource with its type specified as SETTING

## Optional Fields

No entries extracted.

## Notes

- The following example illustrates how an event of type SETTING_MODIFICATION would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Information about the device on which the setting modification occurred.
- target: Resource details.

## Examples

### UDM example for event type SETTING_MODIFICATION

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
