# Entity Management (entity_management)

Entity Management events report activity by a managed client, a micro service, or a user at a management console. The activity can be a create, read, update, and delete operation on a managed entity.

- **Class UID**: `3004`
- **Category**: Identity & Access Management
- **Extends**: [Identity & Access Management (iam)](iam.md)
- **Profiles**: [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Identity & Access Management:**
- `actor` (recommended)
- `src_endpoint` (recommended)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

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
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
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
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `comment`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The user provided comment about why the entity was changed.

### `entity`

- **Type**: [`managed_entity`](../objects/managed_entity.md)
- **Requirement**: required
- **Group**: primary

The managed entity that is being acted upon.

### `entity_result`

- **Type**: [`managed_entity`](../objects/managed_entity.md)
- **Requirement**: recommended
- **Group**: primary

> **Deprecated since v1.9.0.** Use the `updated_entity` attribute instead.

The updated managed entity.

### `updated_entity`

- **Type**: [`managed_entity`](../objects/managed_entity.md)
- **Requirement**: recommended
- **Group**: primary

The intended state of the `entity` after the update. On `Success`, represents the actual post-update state.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `3004`: `Entity Management` - Entity Management events report activity by a managed client, a micro service, or a user at a management console. The activity can be a create, read, update, and delete operation on a managed entity.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `300400`: `Entity Management: Unknown`
- `300401`: `Entity Management: Create` - Create a new managed entity.
- `300402`: `Entity Management: Read` - Read an existing managed entity.
- `300403`: `Entity Management: Update` - Update an existing managed entity.
- `300404`: `Entity Management: Delete` - Delete a managed entity.
- `300405`: `Entity Management: Move` - Move or rename an existing managed entity.
- `300406`: `Entity Management: Enroll` - Enroll an existing managed entity.
- `300407`: `Entity Management: Unenroll` - Unenroll an existing managed entity.
- `300408`: `Entity Management: Enable` - Enable an existing managed entity. Note: This is typically regarded as a semi-permanent, editor visible, syncable change.
- `300409`: `Entity Management: Disable` - Disable an existing managed entity. Note: This is typically regarded as a semi-permanent, editor visible, syncable change.
- `300410`: `Entity Management: Activate` - Activate an existing managed entity. Note: This is a typically regarded as a transient change, a change of state of the engine.
- `300411`: `Entity Management: Deactivate` - Deactivate an existing managed entity. Note: This is a typically regarded as a transient change, a change of state of the engine.
- `300412`: `Entity Management: Suspend` - Suspend an existing managed entity.
- `300413`: `Entity Management: Resume` - Resume (unsuspend) an existing managed entity.
- `300499`: `Entity Management: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
