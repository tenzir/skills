# MITRE Sub-technique (sub_technique)

The MITRE Sub-technique object describes the ATT&CK® or ATLAS™ Sub-technique ID and/or name associated to an attack.

- **Extends**: `_entity`

## Attributes

### `name`

- **Type**: `string_t`

The name of the attack sub-technique. For example: `Scanning IP Blocks` or `User Execution: Unsafe ML Artifacts`.

### `src_url`

- **Type**: `url_t`
- **Requirement**: optional

The versioned permalink of the attack sub-technique. For example: `https://attack.mitre.org/versions/v14/techniques/T1595/001/`.

### `uid`

- **Type**: `string_t`

The unique identifier of the attack sub-technique. For example: `T1595.001` or `AML.T0011.000`.
