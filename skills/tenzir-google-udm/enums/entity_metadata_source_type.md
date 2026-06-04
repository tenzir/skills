# EntityMetadata.SourceType

Describes the source of an entity.

## Values

0. `SOURCE_TYPE_UNSPECIFIED`: Default source type
1. `ENTITY_CONTEXT`: Entities ingested from customers (e.g. AD_CONTEXT, DLP_CONTEXT)
2. `DERIVED_CONTEXT`: Entities derived from customer data such as prevalence, artifact first/last seen, or asset/user first seen stats.
3. `GLOBAL_CONTEXT`: Global contextual entities such as WHOIS or Safe Browsing.
