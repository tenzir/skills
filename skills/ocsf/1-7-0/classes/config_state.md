# Device Config State (config_state)

Device Config State events report device configuration data, device assessments, and/or CIS Benchmark results.

- **UID**: `2`
- **Category**: Discovery
- **Extends**: `discovery`

## Attributes

### `actor`

- **Type**: `actor`
- **Requirement**: optional
- **Group**: context

The actor object describes details about the user/role/process that was the source of the activity. Note that this is not the threat actor of a campaign but may be part of a campaign.

### `assessments`

- **Type**: `assessment`
- **Requirement**: optional
- **Group**: context

A list of assessments associated with the device.

### `cis_benchmark_result`

- **Type**: `cis_benchmark_result`
- **Requirement**: recommended
- **Group**: primary

The CIS Benchmark Result object captures results generated from benchmark evaluations as defined by the Center for Internet Security ([CIS](https://www.cisecurity.org/cis-benchmarks/)).

### `device`

- **Type**: `device`
- **Requirement**: required
- **Group**: primary

The device that is being discovered by an inventory process.
