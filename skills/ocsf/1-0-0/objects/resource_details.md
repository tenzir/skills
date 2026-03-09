# Resource Details (resource_details)

The Resource Details object describes details about resources that were affected by the activity/event.

- **Extends**: `_resource`

## Attributes

### `cloud_partition`

- **Type**: `string_t`
- **Requirement**: optional

The canonical cloud partition name to which the region is assigned (e.g. AWS Partitions: aws, aws-cn, aws-us-gov).

### `criticality`

- **Type**: `string_t`
- **Requirement**: optional

The criticality of the resource as defined by the event source.

### `group`

- **Type**: `group`
- **Requirement**: optional

The name of the related resource group.

### `owner`

- **Type**: `user`
- **Requirement**: recommended

The identity of the service or user account that owns the resource.

### `region`

- **Type**: `string_t`
- **Requirement**: optional

The cloud region of the resource.

### `version`

- **Type**: `string_t`
- **Requirement**: optional

The version of the resource. For example `1.2.3`.
