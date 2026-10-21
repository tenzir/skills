# MITRE D3FEND™ Tactic (d3f_tactic)

The MITRE D3FEND™ Tactic object describes the tactic ID and/or name that is associated to an attack.

- **Extends**: [Entity (_entity)](_entity.md)

## Constraints

- **At least one of**: `name`, `uid`

## Attributes

### `name`

- **Type**: `string_t`
- **Requirement**: recommended

The tactic name that is associated with the defensive technique. For example: `Isolate`.

### `src_url`

- **Type**: `url_t`
- **Requirement**: optional

The versioned permalink of the defensive tactic. For example: `https://d3fend.mitre.org/tactic/d3f:Isolate/`.

### `uid`

- **Type**: `string_t`
- **Requirement**: recommended

The unique identifier of the defensive tactic.
