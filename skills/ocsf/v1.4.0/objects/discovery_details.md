# Discovery Details (discovery_details)

The Discovery Details object describes results of a discovery task/job.

- **Extends**: `object`

## Attributes

### `count`

- **Type**: `integer_t`
- **Requirement**: recommended

The number of discovered entities of the specified type.

### `occurrence_details`

- **Type**: `occurrence_details`
- **Requirement**: optional

Details about where in the target entity, specified information was discovered. Only the attributes, relevant to the target entity type should be populuated.

### `type`

- **Type**: `string_t`
- **Requirement**: recommended

The specific type of information that was discovered. e.g. `name, phone_number, etc.`

### `value`

- **Type**: `string_t`
- **Requirement**: optional

Optionally, the specific value of discovered information.
