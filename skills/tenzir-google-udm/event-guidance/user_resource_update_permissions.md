# USER_RESOURCE_UPDATE_PERMISSIONS Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `USER_RESOURCE_UPDATE_PERMISSIONS`
- Usage-guide section: `USER_RESOURCE_UPDATE_PERMISSIONS`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- principal: Populate the principal.user field with details associated with the user whose permissions were updated within a cloud resource (for example, a Salesforce case, Office 365 calendar, Google Doc, or ServiceNow ticket).
- target: Populate the target.resource field with information about the target cloud resource.

## Optional Fields

- target.application: (Recommended) Populate the target.application field with information about the target cloud application.

## Notes

No entries extracted.
