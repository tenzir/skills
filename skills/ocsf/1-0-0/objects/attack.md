# Attack (attack)

The Attack object describes the technique and associated tactics related to an attack. See [MITRE ATT&CK®](https://attack.mitre.org).

- **Extends**: `object`

## Attributes

### `tactics`

- **Type**: `tactic`
- **Requirement**: required

The a list of tactic ID's/names that are associated with the attack technique, as defined by ATT&CK MatrixTM.

### `technique`

- **Type**: `technique`
- **Requirement**: required

The attack technique.

### `version`

- **Type**: `string_t`
- **Requirement**: required

The ATT&CK Matrix version.
