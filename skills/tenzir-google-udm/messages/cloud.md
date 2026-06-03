# Cloud

Metadata related to the cloud environment.

- **Full name**: `google.backstory.Cloud`
- **Fields**: `4`
- **Nested enums**: `1`

## Nested enums

- [Cloud.CloudEnvironment](../enums/cloud_cloud_environment.md)

## Fields

### `environment`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Cloud.CloudEnvironment`](../enums/cloud_cloud_environment.md)
- **JSON name**: `environment`

The Cloud environment.

### `vpc`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`Resource`](resource.md)
- **JSON name**: `vpc`
- **Deprecated**: `true`

The cloud environment VPC. Deprecated.

### `project`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`Resource`](resource.md)
- **JSON name**: `project`
- **Deprecated**: `true`

The cloud environment project information. Deprecated: Use Resource.resource_ancestors

### `availability_zone`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `availabilityZone`

The cloud environment availability zone (different from region which is location.name).
