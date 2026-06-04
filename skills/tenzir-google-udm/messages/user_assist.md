# UserAssist

The UserAssist extension captures details specific to Windows User Assist events.

- **Full name**: `google.backstory.UserAssist`
- **Fields**: `4`

## Fields

### `application_focus_count`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `applicationFocusCount`

The number of times the application associated with the entry gained focus.

### `application_focus_duration`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration`
- **JSON name**: `applicationFocusDuration`

The total duration the application associated with the entry was in focus.

### `executions_count`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `executionsCount`

The number of times the application associated with the entry has been executed.

### `entry_index`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `entryIndex`

The index or identifier of the user assist entry, unique per user.
