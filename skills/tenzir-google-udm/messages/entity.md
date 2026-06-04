# Entity

An Entity provides additional context about an item in a UDM event. For example, a PROCESS_LAUNCH event describes that user 'abc@example.corp' launched process 'shady.exe'. The event does not include information that user 'abc@example.com' is a recently terminated employee who administers a server storing finance data. Information stored in one or more Entities can add this additional context.

## Fields

### `metadata`

- Type: [`EntityMetadata`](entity_metadata.md) (singular)

Entity metadata such as timestamp, product, etc.

### `entity`

- Type: [`Noun`](noun.md) (singular)

Noun in the UDM event that this entity represents.

### `relations`

- Type: [`Relation`](relation.md) (repeated)

One or more relationships between the entity (a) and other entities, including the relationship type and related entity.

### `additional`

- Type: `object` (singular)

Important entity data that cannot be adequately represented within the formal sections of the Entity.

### `riskScore`

- Type: [`EntityRisk`](entity_risk.md) (optional)

Stores information related to the entity's risk score.

### `metric`

- Type: [`Metric`](metric.md) (singular)

Stores statistical metrics about the entity. Used if metadata.entityType is METRIC.

## Entity Type Guidance

Required fields from the Google UDM usage guide. Set
`metadata.entityType` to the matching `EntityMetadata.EntityType` value.

### `CIDR_BLOCK`

- `entity.network.ipSubnetRange` must be present and include a valid CIDR in the following format: `ip_address/prefix_length`.

### `DOMAIN_NAME`

- `entity.hostname` must be present and represent a valid hostname.
- `Optional`: If `entity.domain.whoisServer` is populated, the `entity.domain` message must have no more than 50 fields set.

### `FILE`

- `entity.file` must be present and contain at least one field.

### `IP_ADDRESS`

- `entity.ip` must contain at least one valid IP address.

### `MUTEX`

- `entity.resource` must be present.
- `entity.resource.resourceType` must be `MUTEX`.
- `entity.resource.name` must be present and not empty.

### `RESOURCE`

- `entity.resource` must be present.
- `entity.resource.resourceType` must be either `MUTEX` or `STORAGE_OBJECT`.
  - If `resourceType` is `MUTEX`: See `MUTEX` requirements above.
  - If `resourceType` is `STORAGE_OBJECT`:
    - `entity.resource.resourceSubtype` must be present and not empty.
    - At least one of the following must be present and not empty: `entity.registry.registryKey` `entity.registry.registryValueData` `entity.registry.registryValueName`

### `URL`

- `entity.url` must be present and not empty.

### `USER`

- `entity.user` must be present.
- `entity.user` must have at least one email address specified.
