# Tags

Tags are event metadata which is set by examining event contents post-parsing. For example, a UDM event may be assigned a tenant_id based on certain customer-defined parameters.

- **Full name**: `google.backstory.Tags`
- **Fields**: `2`

## Fields

### `tenant_id`

- **Number**: `1`
- **Cardinality**: `repeated`
- **Type**: `bytes`
- **JSON name**: `tenantId`

A list of subtenant ids that this event belongs to.

### `data_tap_config_name`

- **Number**: `2`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `dataTapConfigName`

A list of sink name values defined in DataTap configurations.
