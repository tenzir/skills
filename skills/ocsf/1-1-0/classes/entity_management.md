# Entity Management (entity_management)

Entity Management events report activity by a managed client, a micro service, or a user at a management console. The activity can be a create, read, update, and delete operation on a managed entity.

- **UID**: `4`
- **Category**: Identity & Access Management
- **Extends**: `iam`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Create`
- `2`: `Read`
- `3`: `Update`
- `4`: `Delete`

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: `actor`
- **Group**: context

Use for when the entity acting upon another entity is a process or user.

### `comment`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The user provided comment about why the entity was changed.

### `entity`

- **Type**: `managed_entity`
- **Requirement**: required
- **Group**: primary

The managed entity that is being acted upon.

### `entity_result`

- **Type**: `managed_entity`
- **Requirement**: optional
- **Group**: primary

The updated managed entity.
