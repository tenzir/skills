# SecurityResult.IoCStats

Information about the threat intelligence source. These fields are used to model Mandiant sources.

- **Full name**: `google.backstory.SecurityResult.IoCStats`
- **Fields**: `8`

## Fields

### `ioc_stats_type`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.IoCStatsType`](../enums/security_result_io_c_stats_type.md)
- **JSON name**: `iocStatsType`

Describes the source of the IoCStat.

### `first_level_source`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `firstLevelSource`

Name of first level IoC source, for example Mandiant or a third-party.

### `second_level_source`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `secondLevelSource`

Name of the second-level IoC source, for example Crowdsourced Threat Analysis or Knowledge Graph.

### `benign_count`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `benignCount`

Count of responses where the IoC was identified as benign.

### `quality`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.ProductConfidence`](../enums/security_result_product_confidence.md)
- **JSON name**: `quality`

Level of confidence in the IoC mapping extracted from the source.

### `malicious_count`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `maliciousCount`

Count of responses where the IoC was identified as malicious.

### `response_count`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `responseCount`

Total number of response from the source.

### `source_count`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `sourceCount`

Number of sources from which information was extracted.
