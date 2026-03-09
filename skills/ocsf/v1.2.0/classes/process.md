# Process Activity (process)

Process Activity events report when a process launches, injects, opens or terminates another process, successful or otherwise.

- **UID**: `7`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Launch`
- `2`: `Terminate`
- `3`: `Open`
- `4`: `Inject`
- `5`: `Set User ID`

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: `actor`

The actor that performed the activity on the target `process`. For example, the process that started a new process or injected code into another process.

### `actual_permissions`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The permissions that were granted to the in a platform-native format.

### `exit_code`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The exit code reported by a process when it terminates. The convention is that zero indicates success and any non-zero exit code indicates that some error occurred.

### `injection_type`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The process injection method, normalized to the caption of the injection_type_id value. In the case of 'Other', it is defined by the event source.

### `injection_type_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `injection_type`

#### Enum values

- `99`: `Other` - The injection type is not mapped. See the `injection_type` attribute, which contains a data source specific value.
- `0`: `Unknown` - The injection type is unknown.
- `1`: `Remote Thread`
- `2`: `Load Library`

The normalized identifier of the process injection method.

### `module`

- **Type**: `module`
- **Requirement**: recommended
- **Group**: primary

The module that was injected by the actor process.

### `process`

- **Type**: `process`
- **Requirement**: required
- **Group**: primary

The process that was launched, injected into, opened, or terminated.

### `requested_permissions`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The permissions mask that were requested by the process.
