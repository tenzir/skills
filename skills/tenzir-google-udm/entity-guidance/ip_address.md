# IP_ADDRESS Entity Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- Proto enum: [EntityMetadata.EntityType](../enums/entity_metadata_entity_type.md)
- Entity root: [Entity](../messages/entity.md)

## Requirements

- `entity.ip` must contain at least one valid IP address.
