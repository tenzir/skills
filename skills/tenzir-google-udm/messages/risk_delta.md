# RiskDelta

Describes the difference in risk score between two points in time.

- **Full name**: `google.backstory.RiskDelta`
- **Fields**: `4`

## Fields

### `previous_range_end_time`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `previousRangeEndTime`

End time of the previous time window.

### `risk_score_delta`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `riskScoreDelta`

Difference in the normalized risk score from the previous recorded value.

### `previous_risk_score`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `previousRiskScore`

Risk score from previous risk window

### `risk_score_numeric_delta`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `riskScoreNumericDelta`

Numeric change between current and previous risk score
