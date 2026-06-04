# EntityRisk

Stores information related to the risk score of an entity.

## Fields

### `riskVersion`

- Type: `string` (singular)

Version of the risk score calculation algorithm.

### `riskWindow`

- Type: `interval` (singular)

Time window used when computing the risk score for an entity, for example 24 hours or 7 days.

### `DEPRECATEDRiskScore`

- Type: `int32` (singular)
- Deprecated: `true`

Deprecated risk score.

### `riskDelta`

- Type: [`RiskDelta`](risk_delta.md) (optional)

Represents the change in risk score for an entity between the end of the previous time window and the end of the current time window.

### `detectionsCount`

- Type: `int32` (singular)

Number of detections that make up the risk score within the time window.

### `firstDetectionTime`

- Type: `timestamp` (singular)

Timestamp of the first detection within the specified time window. This field is empty when there are no detections.

### `lastDetectionTime`

- Type: `timestamp` (singular)

Timestamp of the last detection within the specified time window. This field is empty when there are no detections.

### `riskScore`

- Type: `float` (singular)

Raw risk score for the entity.

### `normalizedRiskScore`

- Type: `int32` (singular)

Normalized risk score for the entity. This value is between 0-1000.

### `riskWindowSize`

- Type: `duration` (singular)

Risk window duration for the entity.

### `rawRiskDelta`

- Type: [`RiskDelta`](risk_delta.md) (optional)

Represents the change in raw risk score for an entity between the end of the previous time window and the end of the current time window.

### `lastResetTime`

- Type: `timestamp` (singular)

Timestamp for UEBA risk score reset based deduplication. Used specifically for risk based meta rules.

### `detailUri`

- Type: `string` (singular)

Link to the Google Security Operations UI with information about the entity risk score. If the SecOps instance has multiple frontend paths configured, this will be a relative path that can be used to construct the full URL.

### `riskWindowHasNewDetections`

- Type: `bool` (singular)

Whether there are new detections for the risk window.
