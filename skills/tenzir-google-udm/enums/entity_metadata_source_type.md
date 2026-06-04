# EntityMetadata.SourceType

Describes the source of an entity.

- **Full name**: `google.backstory.EntityMetadata.SourceType`
- **Values**: `4`

## Values

### `SOURCE_TYPE_UNSPECIFIED`

- **Number**: `0`

Default source type

### `ENTITY_CONTEXT`

- **Number**: `1`

Entities ingested from customers (e.g. AD_CONTEXT, DLP_CONTEXT)

### `DERIVED_CONTEXT`

- **Number**: `2`

Entities derived from customer data such as prevalence, artifact first/last seen, or asset/user first seen stats.

### `GLOBAL_CONTEXT`

- **Number**: `3`

Global contextual entities such as WHOIS or Safe Browsing.
