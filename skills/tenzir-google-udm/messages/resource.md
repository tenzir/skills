# Resource

Information about a resource such as a task, Cloud Storage bucket, database, disk, logical policy, or something similar.

## Fields

### `type`

- Type: `string` (singular)
- Deprecated: `true`

Deprecated: use resource_type instead.

### `resource_type` / `resourceType`

- Type: [`ResourceType`](../enums/resource_resource_type.md) (singular)

Resource type.

### `resource_subtype` / `resourceSubtype`

- Type: `string` (singular)

Resource sub-type (e.g. "BigQuery", "Bigtable").

### `id`

- Type: `string` (singular)
- Deprecated: `true`

Deprecated: Use resource.name or resource.product_object_id.

### `name`

- Type: `string` (singular)

The full name of the resource. For example, Google Cloud: //cloudresourcemanager.googleapis.com/projects/wombat-123, and AWS: arn:aws:iam::123456789012:user/johndoe.

### `parent`

- Type: `string` (singular)
- Deprecated: `true`

The parent of the resource. For a database table, the parent is the database. For a storage object, the bucket name. Deprecated: use resource_ancestors.name.

### `product_object_id` / `productObjectId`

- Type: `string` (singular)

A vendor-specific identifier to uniquely identify the entity (a GUID, OID, or similar) This field can be used as an entity indicator for a Resource entity.

### `attribute`

- Type: [`Attribute`](attribute.md) (singular)

Generic entity metadata attributes of the resource.

### `scheduled_task` / `scheduledTask`

- Type: [`ScheduledTask`](scheduled_task.md) (singular)
- Deprecated: `true`

DEPRECATED: use windows_scheduled_task for Windows scheduled tasks or scheduled_cron_task for cron jobs. Information about a scheduled task associated with the resource.

### `scheduled_cron_task` / `scheduledCronTask`

- Type: [`ScheduledCronTask`](scheduled_cron_task.md) (singular)

Information about a scheduled cron task associated with the resource.

### `scheduled_anacron_task` / `scheduledAnacronTask`

- Type: [`ScheduledAnacronTask`](scheduled_anacron_task.md) (singular)

Information about a scheduled anacron task associated with the resource.

### `windows_scheduled_task` / `windowsScheduledTask`

- Type: [`WindowsScheduledTask`](windows_scheduled_task.md) (singular)

Information about a Windows scheduled task associated with the resource.

### `volume`

- Type: [`Volume`](volume.md) (singular)

Information about a storage volume associated with the resource.

### `service`

- Type: [`Service`](service.md) (singular)

Information about a Windows service associated with the resource.
