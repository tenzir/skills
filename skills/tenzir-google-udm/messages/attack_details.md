# AttackDetails

MITRE ATT&CK details.

- **Full name**: `google.backstory.AttackDetails`
- **Fields**: `3`
- **Nested messages**: `2`

## Nested messages

- [AttackDetails.Tactic](attack_details_tactic.md)
- [AttackDetails.Technique](attack_details_technique.md)

## Fields

### `version`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `version`

ATT&CK version (e.g. 12.1).

### `tactics`

- **Number**: `2`
- **Cardinality**: `repeated`
- **Type**: [`AttackDetails.Tactic`](attack_details_tactic.md)
- **JSON name**: `tactics`

Tactics employed.

### `techniques`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: [`AttackDetails.Technique`](attack_details_technique.md)
- **JSON name**: `techniques`

Techniques employed.
