# Tactic (tactic)

The Tactic object describes the tactic IDs and/or name that are associated with the attack technique, as defined by [ATT&CK MatrixTM](https://attack.mitre.org/wiki/ATT&CK_Matrix).

- **Extends**: [Entity (_entity)](_entity.md)

## Constraints

- **At least one of**: `name`, `uid`

## Attributes

### `name`

- **Type**: `string_t`
- **Requirement**: recommended

The tactic name that is associated with the attack technique, as defined by [ATT&CK MatrixTM](https://attack.mitre.org/wiki/ATT&CK_Matrix).

### `uid`

- **Type**: `string_t`
- **Requirement**: recommended

The tactic ID that is associated with the attack technique, as defined by [ATT&CK MatrixTM](https://attack.mitre.org/wiki/ATT&CK_Matrix).
