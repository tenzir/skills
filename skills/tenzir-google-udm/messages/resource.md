# Resource

Information about a resource such as a task, Cloud Storage bucket, database, disk, logical policy, or something similar.

- **Full name**: `google.backstory.Resource`
- **Fields**: `14`
- **Nested enums**: `1`

## Nested enums

- [Resource.ResourceType](../enums/resource_resource_type.md)

## Fields

### `type`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `type`
- **Deprecated**: `true`

Deprecated: use resource_type instead.

### `resource_type`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`Resource.ResourceType`](../enums/resource_resource_type.md)
- **JSON name**: `resourceType`

Resource type.

### `resource_subtype`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `resourceSubtype`

Resource sub-type (e.g. "BigQuery", "Bigtable").

### `id`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `id`
- **Deprecated**: `true`

Deprecated: Use resource.name or resource.product_object_id.

### `name`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

The full name of the resource. For example, Google Cloud: //cloudresourcemanager.googleapis.com/projects/wombat-123, and AWS: arn:aws:iam::123456789012:user/johndoe.

### `parent`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `parent`
- **Deprecated**: `true`

The parent of the resource. For a database table, the parent is the database. For a storage object, the bucket name. Deprecated: use resource_ancestors.name.

### `product_object_id`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productObjectId`

A vendor-specific identifier to uniquely identify the entity (a GUID, OID, or similar) This field can be used as an entity indicator for a Resource entity.

### `attribute`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: [`Attribute`](attribute.md)
- **JSON name**: `attribute`

Generic entity metadata attributes of the resource.

### `scheduled_task`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: [`ScheduledTask`](scheduled_task.md)
- **JSON name**: `scheduledTask`
- **Deprecated**: `true`

DEPRECATED: use windows_scheduled_task for Windows scheduled tasks or scheduled_cron_task for cron jobs. Information about a scheduled task associated with the resource.

### `scheduled_cron_task`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: [`ScheduledCronTask`](scheduled_cron_task.md)
- **JSON name**: `scheduledCronTask`

Information about a scheduled cron task associated with the resource.

### `scheduled_anacron_task`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: [`ScheduledAnacronTask`](scheduled_anacron_task.md)
- **JSON name**: `scheduledAnacronTask`

Information about a scheduled anacron task associated with the resource.

### `windows_scheduled_task`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: [`WindowsScheduledTask`](windows_scheduled_task.md)
- **JSON name**: `windowsScheduledTask`

Information about a Windows scheduled task associated with the resource.

### `volume`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: [`Volume`](volume.md)
- **JSON name**: `volume`

Information about a storage volume associated with the resource.

### `service`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: [`Service`](service.md)
- **JSON name**: `service`

Information about a Windows service associated with the resource.
