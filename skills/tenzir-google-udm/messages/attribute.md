# Attribute

Attribute is a container for generic entity attributes including common attributes across core entities (such as, user or asset). For example, Cloud is a generic entity attribute since it can apply to an asset (for example, a VM) or a user (for example, an identity service account).

## Fields

### `cloud`

- Type: [`Cloud`](cloud.md) (singular)

Cloud metadata attributes such as project ID, account ID, or organizational hierarchy.

### `labels`

- Type: [`Label`](label.md) (repeated)

Set of labels for the entity. Should only be used for product labels (for example, Google Cloud resource labels or Azure AD sensitivity labels. Should not be used for arbitrary key-value mappings.

### `permissions`

- Type: [`Permission`](permission.md) (repeated)

System permissions for IAM entity (human principal, service account, group).

### `roles`

- Type: [`Role`](role.md) (repeated)

System IAM roles to be assumed by resources to use the role's permissions for access control.

### `creationTime`

- Type: `google.protobuf.Timestamp` (singular)

Time the resource or entity was created or provisioned.

### `lastUpdateTime`

- Type: `google.protobuf.Timestamp` (singular)

Time the resource or entity was last updated.
