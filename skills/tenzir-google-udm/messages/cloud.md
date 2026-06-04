# Cloud

Metadata related to the cloud environment.

- **Full name**: `google.backstory.Cloud`
- **Fields**: `4`
- **Nested enums**: `1`

## Nested enums

- [Cloud.CloudEnvironment](../enums/cloud_cloud_environment.md)

## Fields

### `environment`

- Type: [`Cloud.CloudEnvironment`](../enums/cloud_cloud_environment.md) (singular)

The Cloud environment.

### `vpc`

- Type: [`Resource`](resource.md) (singular)
- Deprecated: `true`

The cloud environment VPC. Deprecated.

### `project`

- Type: [`Resource`](resource.md) (singular)
- Deprecated: `true`

The cloud environment project information. Deprecated: Use Resource.resourceAncestors

### `availabilityZone`

- Type: `string` (singular)

The cloud environment availability zone (different from region which is location.name).
