# Entity Management (entity_management)

Entity Management events report activity by a managed client, a micro service, or a user at a management console. The activity can be a create, read, update, and delete operation on a managed entity.

- **Class UID**: `3004`
- **Category**: Identity & Access Management
- **Extends**: [Identity & Access Management (iam)](iam.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Create`
- `2`: `Read`
- `3`: `Update`
- `4`: `Delete`
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: optional
- **Group**: context

Use for when the entity acting upon another entity is a process or user.

### `comment`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The user provided comment about why the entity was changed.

### `entity`

- **Type**: [`managed_entity`](../objects/managed_entity.md)
- **Requirement**: required
- **Group**: primary

The managed entity that is being acted upon.

### `entity_result`

- **Type**: [`managed_entity`](../objects/managed_entity.md)
- **Requirement**: optional
- **Group**: primary

The updated managed entity.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `3004`: `Entity Management` - Entity Management events report activity by a managed client, a micro service, or a user at a management console. The activity can be a create, read, update, and delete operation on a managed entity.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `300400`: `Entity Management: Unknown`
- `300401`: `Entity Management: Create`
- `300402`: `Entity Management: Read`
- `300403`: `Entity Management: Update`
- `300404`: `Entity Management: Delete`
- `300499`: `Entity Management: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
