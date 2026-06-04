# Tags

Tags are event metadata which is set by examining event contents post-parsing. For example, a UDM event may be assigned a tenant_id based on certain customer-defined parameters.

## Fields

### `tenant_id` / `tenantId`

- Type: `bytes` (repeated)

A list of subtenant ids that this event belongs to.

### `data_tap_config_name` / `dataTapConfigName`

- Type: `string` (repeated)

A list of sink name values defined in DataTap configurations.
