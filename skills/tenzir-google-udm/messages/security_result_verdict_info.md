# SecurityResult.VerdictInfo

Describes the threat verdict provided by human analysts and machine learning models. These fields are used to model Mandiant sources.

- **Full name**: `google.backstory.SecurityResult.VerdictInfo`
- **Fields**: `16`

## Fields

### `source_count`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `sourceCount`

Number of sources from which intelligence was extracted.

### `response_count`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `responseCount`

Total response count across all sources.

### `neighbour_influence`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `neighbourInfluence`

Describes the near neighbor influence of the verdict.

### `verdict_type`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.VerdictType`](../enums/security_result_verdict_type.md)
- **JSON name**: `verdictType`

Type of verdict.

### `source_provider`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sourceProvider`

Source provider giving the machine learning verdict.

### `benign_count`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `benignCount`

Count of responses where this IoC was marked as benign.

### `malicious_count`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `maliciousCount`

Count of responses where this IoC was marked as malicious.

### `confidence_score`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `confidenceScore`

Confidence score of the verdict.

### `ioc_stats`

- **Number**: `9`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.IoCStats`](security_result_io_c_stats.md)
- **JSON name**: `iocStats`

List of IoCStats from which the verdict was generated.

### `verdict_time`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `verdictTime`

Timestamp when the verdict was generated.

### `verdict_response`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.VerdictResponse`](../enums/security_result_verdict_response.md)
- **JSON name**: `verdictResponse`

Details about the verdict.

### `global_customer_count`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `globalCustomerCount`

Global customer count over the last 30 days

### `global_hits_count`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `globalHitsCount`

Global hit count over the last 30 days.

### `pwn`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `pwn`

Whether one or more Mandiant incident response customers had this indicator in their environment.

### `category_details`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `categoryDetails`

Tags related to the verdict.

### `pwn_first_tagged_time`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `pwnFirstTaggedTime`

The timestamp of the first time a pwn was associated to this entity.
