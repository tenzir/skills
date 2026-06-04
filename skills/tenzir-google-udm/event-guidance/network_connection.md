# NETWORK_CONNECTION Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `NETWORK_CONNECTION`
- Usage-guide section: `NETWORK_CONNECTION`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: event_timestamp
- principal: Include detail about the machine that initiated the network connection (for example, source).
- target: Include details about the target machine if different from the principal machine.
- network: Capture details about the network connection (ports, protocol, etc.).

## Optional Fields

- principal.process and target.process: Include process information associated with the principal and target of the network connection (if available).
- principal.user and target.user: Include user information associated with the principal and target of the network connection (if available).

## Notes

- Note: For all network events, if the principal or target has a port specified, the ip and mac fields must include only one value each (if available), that is the IP address and MAC associated with the port. Otherwise, if no port is specified, you can specify any number of IP and MAC addresses associated with the device at the time of the event (no particular order is required).
