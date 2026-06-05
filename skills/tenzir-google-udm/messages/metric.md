# Metric

Stores precomputed aggregated analytic data for an entity.

## Fields

### `first_seen` / `firstSeen`

- Type: `timestamp` (singular)

Timestamp of the first time the entity was seen in the environment.

### `last_seen` / `lastSeen`

- Type: `timestamp` (singular)

Time stamp of the last time last time the entity was seen in the environment.

### `sum_measure` / `sumMeasure`

- Type: [`Measure`](metric_measure.md) (singular)

Sum of all precomputed measures for the given metric.

### `total_events` / `totalEvents`

- Type: `int64` (singular)

Total number of events used to calculate the given precomputed metric.

### `metric_name` / `metricName`

- Type: [`MetricName`](../enums/metric_metric_name.md) (singular)

Name of the analytic.

### `dimensions`

- Type: [`Dimension`](../enums/metric_dimension.md) (repeated)

All group by clauses used to calculate the metric.

### `export_window` / `exportWindow`

- Type: `int64` (singular)

Export window for which the metric was exported.

### `display_name` / `displayName`

- Type: `string` (singular)

Display name of the custom metric. Google-authored metrics do not have a display name.

### `outcome_variables` / `outcomeVariables`

- Type: [`FindingVariable`](finding_variable.md) (repeated)

List of outcome variables used in the custom metric.

### `match_variables` / `matchVariables`

- Type: [`FindingVariable`](finding_variable.md) (repeated)

List of match variables used in the custom metric.

### `time_range` / `timeRange`

- Type: `interval` (singular)

Time range for which the custom metric was calculated.
