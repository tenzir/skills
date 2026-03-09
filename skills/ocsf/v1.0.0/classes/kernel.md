# Kernel Activity (kernel)

Kernel Activity events report when an process creates, reads, or deletes a kernel resource.

- **UID**: `3`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `99`: `Other` - The event activity is not mapped.
- `0`: `Unknown` - The event activity is unknown.

The normalized identifier of the activity that triggered the event.

### `kernel`

- **Type**: `kernel`
- **Requirement**: required
- **Group**: primary

The target kernel resource.
