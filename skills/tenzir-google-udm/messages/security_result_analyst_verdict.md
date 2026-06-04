# SecurityResult.AnalystVerdict

Verdict provided by the human analyst. These fields are used to model Mandiant sources.

- **Full name**: `google.backstory.SecurityResult.AnalystVerdict`
- **Fields**: `3`

## Fields

### `confidence_score`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `confidenceScore`

Confidence score of the verdict.

### `verdict_time`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `verdictTime`

Timestamp at which the verdict was generated.

### `verdict_response`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.VerdictResponse`](../enums/security_result_verdict_response.md)
- **JSON name**: `verdictResponse`

Details of the verdict.
