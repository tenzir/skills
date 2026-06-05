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

### `risk_score` / `riskScore`

- Type: [`EntityRisk`](entity_risk.md) (optional)

Stores information related to the entity's risk score.

### `metric`

- Type: [`Metric`](metric.md) (singular)

Stores statistical metrics about the entity. Used if metadata.entity_type is METRIC.

## Entity Type Guidance

Required fields from the Google UDM usage guide. Set
`metadata.entity_type` / `metadata.entityType` to the matching
`EntityMetadata.EntityType` value.

### `CIDR_BLOCK`

- `entity.network.ip_subnet_range` must be present and include a valid CIDR in the following format: `ip_address/prefix_length`.

### `DOMAIN_NAME`

- `entity.hostname` must be present and represent a valid hostname.
- `Optional`: If `entity.domain.whois_server` is populated, the `entity.domain` message must have no more than 50 fields set.

### `FILE`

- `entity.file` must be present and contain at least one field.

### `IP_ADDRESS`

- `entity.ip` must contain at least one valid IP address.

### `MUTEX`

- `entity.resource` must be present.
- `entity.resource.resource_type` must be `MUTEX`.
- `entity.resource.name` must be present and not empty.

### `RESOURCE`

- `entity.resource` must be present.
- `entity.resource.resource_type` must be either `MUTEX` or `STORAGE_OBJECT`.
  - If `resource_type` is `MUTEX`: See `MUTEX` requirements above.
  - If `resource_type` is `STORAGE_OBJECT`:
    - `entity.resource.resource_subtype` must be present and not empty.
    - At least one of the following must be present and not empty: `entity.registry.registry_key` `entity.registry.registry_value_data` `entity.registry.registry_value_name`

### `URL`

- `entity.url` must be present and not empty.

### `USER`

- `entity.user` must be present.
- `entity.user` must have at least one email address specified.
