# Device Config State (config_state)

Device Config State events report device configuration data and CIS Benchmark results.

- **UID**: `2`
- **Category**: Discovery
- **Extends**: `discovery`

## Attributes

### `actor`

- **Type**: `actor`
- **Requirement**: optional
- **Group**: context

The actor object describes details about the user/role/process that was the source of the activity.

### `device`

- **Type**: `device`
- **Requirement**: required
- **Group**: primary

The device that is being discovered by an inventory process.

### `cis_benchmark_result`

- **Type**: `cis_benchmark_result`
- **Requirement**: recommended
- **Group**: primary

The CIS benchmark result.
