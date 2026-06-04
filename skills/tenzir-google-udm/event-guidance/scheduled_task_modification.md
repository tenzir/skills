# SCHEDULED_TASK_MODIFICATION Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `SCHEDULED_TASK_CREATION`, `SCHEDULED_TASK_DELETION`, `SCHEDULED_TASK_DISABLE`, `SCHEDULED_TASK_ENABLE`, `SCHEDULED_TASK_MODIFICATION`, `SCHEDULED_TASK_UNCATEGORIZED`
- Usage-guide section: `SCHEDULED_TASK_CREATION, SCHEDULED_TASK_DELETION, SCHEDULED_TASK_DISABLE, SCHEDULED_TASK_ENABLE, SCHEDULED_TASK_MODIFICATION, SCHEDULED_TASK_UNCATEGORIZED`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- principal: For all SCHEDULED_TASK events, principal must include a machine identifier and a user identifier.
- target: Target must include a valid resource and a resource type defined as "TASK".

## Optional Fields

- security_result: Describe the malicious activity detected.

## Notes

- The following example illustrates how an event of type SCHEDULED_TASK_CREATION could be formatted for the Google SecOps UDM:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Device that scheduled the suspicious task.
- target: Software targeted by the suspicious task.
- intermediary: Intermediary involved with the suspicious task.
- security_result: Security details about the suspicious task.

## Examples

### UDM example for SCHEDULED_TASK_CREATION

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
