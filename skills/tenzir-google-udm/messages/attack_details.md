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

- Type: `string` (singular)

ATT&CK version (e.g. 12.1).

### `tactics`

- Type: [`AttackDetails.Tactic`](attack_details_tactic.md) (repeated)

Tactics employed.

### `techniques`

- Type: [`AttackDetails.Technique`](attack_details_technique.md) (repeated)

Techniques employed.
