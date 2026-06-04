# Metric

Stores precomputed aggregated analytic data for an entity.

## Fields

### `firstSeen`

- Type: `timestamp` (singular)

Timestamp of the first time the entity was seen in the environment.

### `lastSeen`

- Type: `timestamp` (singular)

Time stamp of the last time last time the entity was seen in the environment.

### `sumMeasure`

- Type: [`Measure`](metric_measure.md) (singular)

Sum of all precomputed measures for the given metric.

### `totalEvents`

- Type: `int64` (singular)

Total number of events used to calculate the given precomputed metric.

### `metricName`

- Type: [`MetricName`](../enums/metric_metric_name.md) (singular)

Name of the analytic.

### `dimensions`

- Type: [`Dimension`](../enums/metric_dimension.md) (repeated)

All group by clauses used to calculate the metric.

### `exportWindow`

- Type: `int64` (singular)

Export window for which the metric was exported.

### `displayName`

- Type: `string` (singular)

Display name of the custom metric. Google-authored metrics do not have a display name.

### `outcomeVariables`

- Type: [`FindingVariable`](finding_variable.md) (repeated)

List of outcome variables used in the custom metric.

### `matchVariables`

- Type: [`FindingVariable`](finding_variable.md) (repeated)

List of match variables used in the custom metric.

### `timeRange`

- Type: `interval` (singular)

Time range for which the custom metric was calculated.
