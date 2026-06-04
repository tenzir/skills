# EntityMetadata.SourceType

Describes the source of an entity.

## Values

- `SOURCE_TYPE_UNSPECIFIED` (0): Default source type
- `ENTITY_CONTEXT` (1): Entities ingested from customers (e.g. AD_CONTEXT, DLP_CONTEXT)
- `DERIVED_CONTEXT` (2): Entities derived from customer data such as prevalence, artifact first/last seen, or asset/user first seen stats.
- `GLOBAL_CONTEXT` (3): Global contextual entities such as WHOIS or Safe Browsing.
