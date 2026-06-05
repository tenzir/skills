# AnalystVerdict

Verdict provided by the human analyst. These fields are used to model Mandiant sources.

## Fields

### `confidence_score` / `confidenceScore`

- Type: `int32` (singular)

Confidence score of the verdict.

### `verdict_time` / `verdictTime`

- Type: `timestamp` (singular)

Timestamp at which the verdict was generated.

### `verdict_response` / `verdictResponse`

- Type: [`VerdictResponse`](../enums/security_result_verdict_response.md) (singular)

Details of the verdict.
