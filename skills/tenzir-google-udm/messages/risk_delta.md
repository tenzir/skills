# RiskDelta

Describes the difference in risk score between two points in time.

- **Full name**: `google.backstory.RiskDelta`
- **Fields**: `4`

## Fields

### `previousRangeEndTime`

- Type: `google.protobuf.Timestamp` (singular)

End time of the previous time window.

### `riskScoreDelta`

- Type: `int32` (singular)

Difference in the normalized risk score from the previous recorded value.

### `previousRiskScore`

- Type: `int32` (singular)

Risk score from previous risk window

### `riskScoreNumericDelta`

- Type: `int32` (singular)

Numeric change between current and previous risk score
