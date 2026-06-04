# REGISTRY_CREATION Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `REGISTRY_CREATION`, `REGISTRY_MODIFICATION`, `REGISTRY_DELETION`
- Usage-guide section: `REGISTRY_CREATION, REGISTRY_MODIFICATION, REGISTRY_DELETION`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- principal: At least one machine identifier. If a user-mode process performs the registry modification, principal.process must include information about the process modifying the registry. If a kernel process performs the registry modification, the principal must not include process information.
- target: target.registry: If the target registry is remote, target must include at least one identifier for the target machine (for example, an IP address, MAC, hostname, or third party asset identifier). target.registry.registry_key: All registry events must include the affected registry key.

## Optional Fields

- security_result: Describe the malicious activity detected. For example, a bad registry key.
- principal.user: Populate if user information is available about the process.

## Notes

- The following example illustrates how you would format a REGISTRY_MODIFICATION event in Proto3 using the Google SecOps UDM syntax:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Device, user, and process details.
- target: Registry entry affected by the modification.

## Examples

### UDM example for REGISTRY_MODIFICATION

```text
metadata {
  event_timestamp: "2020-01-01T13:27:41+00:00"
  event_type: REGISTRY_MODIFICATION
  vendor_name: "Microsoft"
  product_name: "Windows"
}
principal {
  hostname: "test-win"
  user {
    userid: "test"
    windows_sid: "ABCDEFGH-123456789-1111111-1000"
  }
  process {
    pid: "0xc45"
    file {
      full_path: "C:\\Windows\\regedit.exe"
    }
  }
}
target {
  registry {
    registry_key: "\\REGISTRY\\USER\\TEST_USER\\Control Panel\\PowerCfg\\PowerPolicy"
    registry_value_name: "Description"
    registry_value_data: "For extending battery life."
  }
}
```
