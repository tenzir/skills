# WindowsEventLog

The WindowsEventLog extension captures details specific to Windows Event Log events.

- **Full name**: `google.backstory.WindowsEventLog`
- **Fields**: `3`
- **Nested enums**: `1`

## Nested enums

- [WindowsEventLog.Channel](../enums/windows_event_log_channel.md)

## Fields

### `channel`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`WindowsEventLog.Channel`](../enums/windows_event_log_channel.md)
- **JSON name**: `channel`

The channel of the event.

### `event_id`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `eventId`

A unique identifier for a specific type of event.

### `activity_id`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `activityId`

A GUID (Globally Unique Identifier) used to link a sequence of related events together.
