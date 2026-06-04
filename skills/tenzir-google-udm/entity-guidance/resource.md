# RESOURCE Entity Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- Proto enum: [EntityMetadata.EntityType](../enums/entity_metadata_entity_type.md)
- Entity root: [Entity](../messages/entity.md)

## Requirements

- `entity.resource` must be present.
- `entity.resource.resource_type` must be either `MUTEX` or `STORAGE_OBJECT`. If `resource_type` is `MUTEX`: See `MUTEX` requirements above. If `resource_type` is `STORAGE_OBJECT`: `entity.resource.resource_subtype` must be present and not empty. At least one of the following must be present and not empty: `entity.registry.registry_key` `entity.registry.registry_value_data` `entity.registry.registry_value_name`
- If `resource_type` is `MUTEX`: See `MUTEX` requirements above.
- If `resource_type` is `STORAGE_OBJECT`: `entity.resource.resource_subtype` must be present and not empty. At least one of the following must be present and not empty: `entity.registry.registry_key` `entity.registry.registry_value_data` `entity.registry.registry_value_name`
- `entity.resource.resource_subtype` must be present and not empty.
- At least one of the following must be present and not empty: `entity.registry.registry_key` `entity.registry.registry_value_data` `entity.registry.registry_value_name`
