# Attribute

Attribute is a container for generic entity attributes including common attributes across core entities (such as, user or asset). For example, Cloud is a generic entity attribute since it can apply to an asset (for example, a VM) or a user (for example, an identity service account).

- **Full name**: `google.backstory.Attribute`
- **Fields**: `6`

## Fields

### `cloud`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Cloud`](cloud.md)
- **JSON name**: `cloud`

Cloud metadata attributes such as project ID, account ID, or organizational hierarchy.

### `labels`

- **Number**: `2`
- **Cardinality**: `repeated`
- **Type**: [`Label`](label.md)
- **JSON name**: `labels`

Set of labels for the entity. Should only be used for product labels (for example, Google Cloud resource labels or Azure AD sensitivity labels. Should not be used for arbitrary key-value mappings.

### `permissions`

- **Number**: `705`
- **Cardinality**: `repeated`
- **Type**: [`Permission`](permission.md)
- **JSON name**: `permissions`

System permissions for IAM entity (human principal, service account, group).

### `roles`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: [`Role`](role.md)
- **JSON name**: `roles`

System IAM roles to be assumed by resources to use the role's permissions for access control.

### `creation_time`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `creationTime`

Time the resource or entity was created or provisioned.

### `last_update_time`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastUpdateTime`

Time the resource or entity was last updated.
