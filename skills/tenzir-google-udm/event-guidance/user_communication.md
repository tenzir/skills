# USER_COMMUNICATION Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `USER_COMMUNICATION`
- Usage-guide section: `USER_COMMUNICATION`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- principal: Populate the principal.user field with details associated with user-initiated (sender) communication, such as a chat message in Google Chat or Slack, a video or voice conference in Zoom or Google Meet, or a VoIP connection.

## Optional Fields

- target: (Recommended) Populate the target.user field with information about the target user (receiver) of the cloud communication resource. Populate the target.application field with information about the target cloud communication application.

## Notes

No entries extracted.
