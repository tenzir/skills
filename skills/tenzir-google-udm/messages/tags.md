# Tags

Tags are event metadata which is set by examining event contents post-parsing. For example, a UDM event may be assigned a tenantId based on certain customer-defined parameters.

- **Full name**: `google.backstory.Tags`
- **Fields**: `2`

## Fields

### `tenantId`

- Type: `bytes` (repeated)

A list of subtenant ids that this event belongs to.

### `dataTapConfigName`

- Type: `string` (repeated)

A list of sink name values defined in DataTap configurations.
