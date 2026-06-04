# USER_UNCATEGORIZED Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `USER_UNCATEGORIZED`
- Usage-guide section: `USER_UNCATEGORIZED`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: event_timestamp
- principal: Include information about the machine where the request to create or delete the user originated from. For a local user creation or deletion, principal must include at least one machine identifier for the originating machine.
- target: Location where the user is being created. Must also include user information (for example, target.user).

## Optional Fields

- principal: User and process details for the machine where the user creation or deletion request was initiated.
- target: Information about the target machine (if different than the principal machine).

## Notes

No entries extracted.
