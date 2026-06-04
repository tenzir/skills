# MUTEX Entity Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- Proto enum: [EntityMetadata.EntityType](../enums/entity_metadata_entity_type.md)
- Entity root: [Entity](../messages/entity.md)

## Requirements

- `entity.resource` must be present.
- `entity.resource.resource_type` must be `MUTEX`.
- `entity.resource.name` must be present and not empty.
