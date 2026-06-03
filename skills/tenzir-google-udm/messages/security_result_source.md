# SecurityResult.Source

Deprecated. Information about the threat intelligence source. These fields are used to model Mandiant sources.

- **Full name**: `google.backstory.SecurityResult.Source`
- **Fields**: `7`

## Fields

### `name`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

Name of the IoC source.

### `benign_count`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `benignCount`

Count of responses where this IoC was marked benign.

### `malicious_count`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `maliciousCount`

Count of responses where this IoC was marked malicious.

### `quality`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.ProductConfidence`](../enums/security_result_product_confidence.md)
- **JSON name**: `quality`

Quality of the IoC mapping extracted from the source.

### `response_count`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `responseCount`

Total response count from this source.

### `source_count`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `sourceCount`

Number of sources from which intelligence was extracted.

### `threat_intelligence_sources`

- **Number**: `7`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.Source`](security_result_source.md)
- **JSON name**: `threatIntelligenceSources`

Different threat intelligence sources from which IoC info was extracted.
