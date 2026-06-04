# USER_RESOURCE_CREATION Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `USER_RESOURCE_CREATION`, `USER_RESOURCE_DELETION`
- Usage-guide section: `USER_RESOURCE_CREATION, USER_RESOURCE_DELETION`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- principal: Populate the principal.user field with details associated with the user created within a cloud resource (for example, a Salesforce case, Office 365 calendar, Google Doc, or ServiceNow ticket).
- target: Populate the target.resource field with information about the target cloud resource.

## Optional Fields

- target.application: (Recommended) Populate the target.application field with information about the target cloud application.

## Notes

No entries extracted.
