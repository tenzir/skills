# SERVICE_STOP Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `SERVICE_UNSPECIFIED`, `SERVICE_CREATION`, `SERVICE_DELETION`, `SERVICE_START`, `SERVICE_STOP`
- Usage-guide section: `SERVICE_UNSPECIFIED, SERVICE_CREATION, SERVICE_DELETION, SERVICE_START, SERVICE_STOP`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- target: Include the user identifier and specify either process or application.
- principal: Include at least one machine identifier (IP or MAC ADDRESS, hostname, or asset identifier).

## Optional Fields

No entries extracted.

## Notes

- The following example illustrates how an event of type SERVICE_UNSPECIFIED would be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Device and location details.
- target: Hostname and user identifier.
- application: Application name and resource type.

## Examples

### UDM example for SERVICE_UNSPECIFIED

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
