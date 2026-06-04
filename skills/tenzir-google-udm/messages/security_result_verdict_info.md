# VerdictInfo

Describes the threat verdict provided by human analysts and machine learning models. These fields are used to model Mandiant sources.

## Fields

### `sourceCount`

- Type: `int32` (singular)

Number of sources from which intelligence was extracted.

### `responseCount`

- Type: `int32` (singular)

Total response count across all sources.

### `neighbourInfluence`

- Type: `string` (singular)

Describes the near neighbor influence of the verdict.

### `verdictType`

- Type: [`VerdictType`](../enums/security_result_verdict_type.md) (singular)

Type of verdict.

### `sourceProvider`

- Type: `string` (singular)

Source provider giving the machine learning verdict.

### `benignCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked as benign.

### `maliciousCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked as malicious.

### `confidenceScore`

- Type: `int32` (singular)

Confidence score of the verdict.

### `iocStats`

- Type: [`IoCStats`](security_result_io_c_stats.md) (repeated)

List of IoCStats from which the verdict was generated.

### `verdictTime`

- Type: `google.protobuf.Timestamp` (singular)

Timestamp when the verdict was generated.

### `verdictResponse`

- Type: [`VerdictResponse`](../enums/security_result_verdict_response.md) (singular)

Details about the verdict.

### `globalCustomerCount`

- Type: `int32` (singular)

Global customer count over the last 30 days

### `globalHitsCount`

- Type: `int32` (singular)

Global hit count over the last 30 days.

### `pwn`

- Type: `bool` (singular)

Whether one or more Mandiant incident response customers had this indicator in their environment.

### `categoryDetails`

- Type: `string` (singular)

Tags related to the verdict.

### `pwnFirstTaggedTime`

- Type: `google.protobuf.Timestamp` (singular)

The timestamp of the first time a pwn was associated to this entity.
