# USER_CHANGE_PASSWORD Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Applies To

- `USER_CHANGE_PASSWORD`, `USER_CHANGE_PERMISSIONS`
- Usage-guide section: `USER_CHANGE_PASSWORD, USER_CHANGE_PERMISSIONS`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- principal: If the user account is modified from a remote location, populate principal with information about the machine from where the user modification originated.
- target: Populate target.user with information about the user that has been modified.
- intermediary: For SSO logins, intermediary must include at least one machine identifier for the SSO server if available.

## Optional Fields

No entries extracted.

## Notes

No entries extracted.
