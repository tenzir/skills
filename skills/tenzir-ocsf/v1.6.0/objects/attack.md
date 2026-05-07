# MITRE ATT&CK® & ATLAS™ (attack)

The MITRE ATT&CK® & ATLAS™ object describes the tactic, technique, sub-technique & mitigation associated to an attack.

- **Extends**: [Object (object)](object.md)

## Attributes

### `mitigation`

- **Type**: [`mitigation`](mitigation.md)
- **Requirement**: optional

The Mitigation object describes the MITRE ATT&CK® or ATLAS™ Mitigation ID and/or name that is associated to an attack.

### `sub_technique`

- **Type**: [`sub_technique`](sub_technique.md)
- **Requirement**: recommended

The Sub-technique object describes the MITRE ATT&CK® or ATLAS™ Sub-technique ID and/or name associated to an attack.

### `tactic`

- **Type**: [`tactic`](tactic.md)
- **Requirement**: recommended

The Tactic object describes the MITRE ATT&CK® or ATLAS™ Tactic ID and/or name that is associated to an attack.

### `tactics`

- **Type**: [`tactic`](tactic.md)
- **Requirement**: optional

The Tactic object describes the tactic ID and/or tactic name that are associated with the attack technique, as defined by [ATT&CK® Matrix](https://attack.mitre.org/wiki/ATT&CK_Matrix).

### `technique`

- **Type**: [`technique`](technique.md)
- **Requirement**: recommended

The Technique object describes the MITRE ATT&CK® or ATLAS™ Technique ID and/or name associated to an attack.

### `version`

- **Type**: `string_t`
- **Requirement**: recommended

The ATT&CK® or ATLAS™ Matrix version.
