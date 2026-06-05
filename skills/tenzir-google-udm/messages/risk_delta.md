# RiskDelta

Describes the difference in risk score between two points in time.

## Fields

### `previous_range_end_time` / `previousRangeEndTime`

- Type: `timestamp` (singular)

End time of the previous time window.

### `risk_score_delta` / `riskScoreDelta`

- Type: `int32` (singular)

Difference in the normalized risk score from the previous recorded value.

### `previous_risk_score` / `previousRiskScore`

- Type: `int32` (singular)

Risk score from previous risk window

### `risk_score_numeric_delta` / `riskScoreNumericDelta`

- Type: `int32` (singular)

Numeric change between current and previous risk score
