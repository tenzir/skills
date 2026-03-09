# Entity Management (entity_management)

Entity Management events report activity by a managed client, a micro service, or a user at a management console. The activity can be a create, read, update, and delete operation on a managed entity.

- **UID**: `4`
- **Category**: Identity & Access Management
- **Extends**: `iam`

## Attributes

### `access_list`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The list of requested access rights.

### `access_mask`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: context

The access mask in a platform-native format.

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Create` - Create a new managed entity.
- `2`: `Read` - Read an existing managed entity.
- `3`: `Update` - Update an existing managed entity.
- `4`: `Delete` - Delete a managed entity.
- `5`: `Move` - Move or rename an existing managed entity.
- `6`: `Enroll` - Enroll an existing managed entity.
- `7`: `Unenroll` - Unenroll an existing managed entity.
- `8`: `Enable` - Enable an existing managed entity. Note: This is typically regarded as a semi-permanent, editor visible, syncable change.
- `9`: `Disable` - Disable an existing managed entity. Note: This is typically regarded as a semi-permanent, editor visible, syncable change.
- `10`: `Activate` - Activate an existing managed entity. Note: This is a typically regarded as a transient change, a change of state of the engine.
- `11`: `Deactivate` - Deactivate an existing managed entity. Note: This is a typically regarded as a transient change, a change of state of the engine.
- `12`: `Suspend` - Suspend an existing managed entity.
- `13`: `Resume` - Resume (unsuspend) an existing managed entity.

The normalized identifier of the activity that triggered the event.

### `comment`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The user provided comment about why the entity was changed.

### `entity`

- **Type**: `managed_entity`
- **Requirement**: required
- **Group**: primary

The managed entity that is being acted upon.

### `entity_result`

- **Type**: `managed_entity`
- **Requirement**: recommended
- **Group**: primary

The updated managed entity.
