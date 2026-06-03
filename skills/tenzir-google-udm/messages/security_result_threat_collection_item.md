# SecurityResult.ThreatCollectionItem

Threat Collection that is either a threat campaign or a threat report.

- **Full name**: `google.backstory.SecurityResult.ThreatCollectionItem`
- **Fields**: `3`

## Fields

### `id`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `id`

The ID of the threat collection.

### `type`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.ThreatCollectionType`](../enums/security_result_threat_collection_type.md)
- **JSON name**: `type`

The type of threat collection (e.g., "campaign").

### `alt_names`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `altNames`

The name of the threat collection.
