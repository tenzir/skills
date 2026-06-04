# DOMAIN_NAME Entity Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- Proto enum: [EntityMetadata.EntityType](../enums/entity_metadata_entity_type.md)
- Entity root: [Entity](../messages/entity.md)

## Requirements

- `entity.hostname` must be present and represent a valid hostname.
- `Optional`: If `entity.domain.whois_server` is populated, the `entity.domain` message must have no more than 50 fields set.
