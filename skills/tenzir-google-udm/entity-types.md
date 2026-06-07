# Entity Types

Required fields from the Google UDM usage guide. Set
`metadata.entity_type` / `metadata.entityType` to the matching
[`EntityMetadata.EntityType`](enums/entity_metadata_entity_type.md) value.

The entity types below are values for the Entity record's
`metadata.entity_type` / `metadata.entityType`. In an
`entities.import` request, the surrounding `inlineSource.logType` is
separate: it names the source log type for the context data, for
example `AZURE_AD_CONTEXT`, not a UDM entity type such as `USER` or
`ASSET`. See Google's `entities.import` reference:
https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.entities/import

## `CIDR_BLOCK`

- `entity.network.ip_subnet_range` must be present and include a valid CIDR in the following format: `ip_address/prefix_length`.

## `DOMAIN_NAME`

- `entity.hostname` must be present and represent a valid hostname.
- `Optional`: If `entity.domain.whois_server` is populated, the `entity.domain` message must have no more than 50 fields set.

## `FILE`

- `entity.file` must be present and contain at least one field.

## `IP_ADDRESS`

- `entity.ip` must contain at least one valid IP address.

## `MUTEX`

- `entity.resource` must be present.
- `entity.resource.resource_type` must be `MUTEX`.
- `entity.resource.name` must be present and not empty.

## `RESOURCE`

- `entity.resource` must be present.
- `entity.resource.resource_type` must be either `MUTEX` or `STORAGE_OBJECT`.
  - If `resource_type` is `MUTEX`: See `MUTEX` requirements above.
  - If `resource_type` is `STORAGE_OBJECT`:
    - `entity.resource.resource_subtype` must be present and not empty.
    - At least one of the following must be present and not empty: `entity.registry.registry_key` `entity.registry.registry_value_data` `entity.registry.registry_value_name`

## `URL`

- `entity.url` must be present and not empty.

## `USER`

- `entity.user` must be present.
- `entity.user` must have at least one email address specified.
