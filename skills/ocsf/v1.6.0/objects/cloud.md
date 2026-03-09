# Cloud (cloud)

The Cloud object contains information about a cloud or Software-as-a-Service account or similar construct, such as AWS Account ID, regions, organizations, folders, compartments, tenants, etc.

- **Extends**: `object`

## Attributes

### `account`

- **Type**: [`account`](account.md)
- **Requirement**: optional

The account object describes details about the account that was the source or target of the activity.

### `cloud_partition`

- **Type**: `string_t`
- **Requirement**: optional

The canonical cloud partition name to which the region is assigned (e.g. AWS Partitions: aws, aws-cn, aws-us-gov).

### `org`

- **Type**: [`organization`](organization.md)
- **Requirement**: optional

Organization and org unit relevant to the event or object.

### `project_uid`

- **Type**: `string_t`
- **Requirement**: optional

The unique identifier of a Cloud project.

### `provider`

- **Type**: `string_t`
- **Requirement**: required

The unique name of the Cloud services provider, such as AWS, MS Azure, GCP, etc.

### `region`

- **Type**: `string_t`
- **Requirement**: recommended

The name of the cloud region, as defined by the cloud provider.

### `zone`

- **Type**: `string_t`
- **Requirement**: optional

The availability zone in the cloud region, as defined by the cloud provider.
