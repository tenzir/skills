# EntityRisk

Stores information related to the risk score of an entity.

- **Full name**: `google.backstory.EntityRisk`
- **Fields**: `14`

## Fields

### `risk_version`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `riskVersion`

Version of the risk score calculation algorithm.

### `risk_window`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `google.type.Interval` (imported)
- **JSON name**: `riskWindow`

Time window used when computing the risk score for an entity, for example 24 hours or 7 days.

### `DEPRECATED_risk_score`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `DEPRECATEDRiskScore`
- **Deprecated**: `true`

Deprecated risk score.

### `risk_delta`

- **Number**: `4`
- **Cardinality**: `optional`
- **Type**: [`RiskDelta`](risk_delta.md)
- **JSON name**: `riskDelta`

Represents the change in risk score for an entity between the end of the previous time window and the end of the current time window.

### `detections_count`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `detectionsCount`

Number of detections that make up the risk score within the time window.

### `first_detection_time`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `firstDetectionTime`

Timestamp of the first detection within the specified time window. This field is empty when there are no detections.

### `last_detection_time`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastDetectionTime`

Timestamp of the last detection within the specified time window. This field is empty when there are no detections.

### `risk_score`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `float`
- **JSON name**: `riskScore`

Raw risk score for the entity.

### `normalized_risk_score`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `normalizedRiskScore`

Normalized risk score for the entity. This value is between 0-1000.

### `risk_window_size`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration` (imported)
- **JSON name**: `riskWindowSize`

Risk window duration for the entity.

### `raw_risk_delta`

- **Number**: `11`
- **Cardinality**: `optional`
- **Type**: [`RiskDelta`](risk_delta.md)
- **JSON name**: `rawRiskDelta`

Represents the change in raw risk score for an entity between the end of the previous time window and the end of the current time window.

### `last_reset_time`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastResetTime`

Timestamp for UEBA risk score reset based deduplication. Used specifically for risk based meta rules.

### `detail_uri`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `detailUri`

Link to the Google Security Operations UI with information about the entity risk score. If the SecOps instance has multiple frontend paths configured, this will be a relative path that can be used to construct the full URL.

### `risk_window_has_new_detections`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `riskWindowHasNewDetections`

Whether there are new detections for the risk window.
