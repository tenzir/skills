# Feature (feature)

The Feature object provides information about the software product feature that generated a specific event. It encompasses details related to the capabilities, components, user interface (UI) design, and performance upgrades associated with the feature.

- **Extends**: [Entity (_entity)](_entity.md)

## Constraints

- **At least one of**: `name`, `uid`

## Attributes

### `name`

- **Type**: `string_t`
- **Requirement**: recommended

The name of the feature.

### `uid`

- **Type**: `string_t`
- **Requirement**: recommended

The unique identifier of the feature.

### `version`

- **Type**: `string_t`
- **Requirement**: recommended

The version of the feature.
