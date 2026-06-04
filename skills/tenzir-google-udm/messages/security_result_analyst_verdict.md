# SecurityResult.AnalystVerdict

Verdict provided by the human analyst. These fields are used to model Mandiant sources.

- **Full name**: `google.backstory.SecurityResult.AnalystVerdict`
- **Fields**: `3`

## Fields

### `confidenceScore`

- Type: `int32` (singular)

Confidence score of the verdict.

### `verdictTime`

- Type: `google.protobuf.Timestamp` (singular)

Timestamp at which the verdict was generated.

### `verdictResponse`

- Type: [`SecurityResult.VerdictResponse`](../enums/security_result_verdict_response.md) (singular)

Details of the verdict.
