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

- `1`: `Create`
- `2`: `Read`
- `3`: `Delete`
- `4`: `Invoke`

The normalized identifier of the activity that triggered the event.

### `kernel`

- **Type**: `kernel`
- **Requirement**: required
- **Group**: primary

The target kernel resource.
