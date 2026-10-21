# Query Evidence (query_evidence)

The resulting evidence information that was queried.

- **Extends**: [Query Evidence (query_evidence)](../../../objects/query_evidence.md)

## Constraints

- **Exactly one of**: `connection_info`, `file`, `folder`, `group`, `job`, `kernel`, `module`, `network_interfaces`, `peripheral_device`, `process`, `reg_key`, `reg_value`, `service`, `session`, `startup_item`, `user`

## Inherited attributes

**From Query Evidence:**
- `query_type_id` (required)
- `connection_info` (recommended)
- `file` (recommended)
- `folder` (recommended)
- `group` (recommended)
- `job` (recommended)
- `kernel` (recommended)
- `module` (recommended)
- `network_interfaces` (recommended)
- `peripheral_device` (recommended)
- `process` (recommended)
- `service` (recommended)
- `session` (recommended)
- `startup_item` (recommended)
- `user` (recommended)

## Attributes

### `reg_key`

- **Type**: `win/reg_key`
- **Requirement**: recommended
- **Group**: primary

The registry key object describes a Windows registry key.

### `reg_value`

- **Type**: `win/reg_value`
- **Requirement**: recommended
- **Group**: primary

The registry value object describes a Windows registry value.
