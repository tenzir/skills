# UserAssist

The UserAssist extension captures details specific to Windows User Assist events.

## Fields

### `application_focus_count` / `applicationFocusCount`

- Type: `int64` (singular)

The number of times the application associated with the entry gained focus.

### `application_focus_duration` / `applicationFocusDuration`

- Type: `duration` (singular)

The total duration the application associated with the entry was in focus.

### `executions_count` / `executionsCount`

- Type: `int64` (singular)

The number of times the application associated with the entry has been executed.

### `entry_index` / `entryIndex`

- Type: `int64` (singular)

The index or identifier of the user assist entry, unique per user.
