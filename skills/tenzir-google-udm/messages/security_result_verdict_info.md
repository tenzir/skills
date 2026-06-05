# VerdictInfo

Describes the threat verdict provided by human analysts and machine learning models. These fields are used to model Mandiant sources.

## Fields

### `source_count` / `sourceCount`

- Type: `int32` (singular)

Number of sources from which intelligence was extracted.

### `response_count` / `responseCount`

- Type: `int32` (singular)

Total response count across all sources.

### `neighbour_influence` / `neighbourInfluence`

- Type: `string` (singular)

Describes the near neighbor influence of the verdict.

### `verdict_type` / `verdictType`

- Type: [`VerdictType`](../enums/security_result_verdict_type.md) (singular)

Type of verdict.

### `source_provider` / `sourceProvider`

- Type: `string` (singular)

Source provider giving the machine learning verdict.

### `benign_count` / `benignCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked as benign.

### `malicious_count` / `maliciousCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked as malicious.

### `confidence_score` / `confidenceScore`

- Type: `int32` (singular)

Confidence score of the verdict.

### `ioc_stats` / `iocStats`

- Type: [`IoCStats`](security_result_io_c_stats.md) (repeated)

List of IoCStats from which the verdict was generated.

### `verdict_time` / `verdictTime`

- Type: `timestamp` (singular)

Timestamp when the verdict was generated.

### `verdict_response` / `verdictResponse`

- Type: [`VerdictResponse`](../enums/security_result_verdict_response.md) (singular)

Details about the verdict.

### `global_customer_count` / `globalCustomerCount`

- Type: `int32` (singular)

Global customer count over the last 30 days

### `global_hits_count` / `globalHitsCount`

- Type: `int32` (singular)

Global hit count over the last 30 days.

### `pwn`

- Type: `bool` (singular)

Whether one or more Mandiant incident response customers had this indicator in their environment.

### `category_details` / `categoryDetails`

- Type: `string` (singular)

Tags related to the verdict.

### `pwn_first_tagged_time` / `pwnFirstTaggedTime`

- Type: `timestamp` (singular)

The timestamp of the first time a pwn was associated to this entity.
