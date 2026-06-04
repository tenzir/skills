# ThreatCollectionItem

Threat Collection that is either a threat campaign or a threat report.

## Fields

### `id`

- Type: `string` (singular)

The ID of the threat collection.

### `type`

- Type: [`ThreatCollectionType`](../enums/security_result_threat_collection_type.md) (singular)

The type of threat collection (e.g., "campaign").

### `alt_names` / `altNames`

- Type: `string` (repeated)

The name of the threat collection.
