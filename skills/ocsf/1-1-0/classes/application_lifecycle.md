# Application Lifecycle (application_lifecycle)

Application Lifecycle events report installation, removal, start, stop of an application or service.

- **UID**: `2`
- **Category**: Application Activity
- **Extends**: `application`

## Attributes

### `$include`

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Install`
- `2`: `Remove`
- `3`: `Start`
- `4`: `Stop`

The normalized identifier of the activity that triggered the event.

### `app`

- **Type**: `product`
- **Requirement**: required
- **Group**: primary

The application that was affected by the lifecycle event.  This also applies to self-updating application systems.
