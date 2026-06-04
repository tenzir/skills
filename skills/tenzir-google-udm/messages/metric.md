# Metric

Stores precomputed aggregated analytic data for an entity.

- **Full name**: `google.backstory.Metric`
- **Fields**: `11`
- **Nested messages**: `1`
- **Nested enums**: `3`

## Nested messages

- [Metric.Measure](metric_measure.md)

## Nested enums

- [Metric.AggregateFunction](../enums/metric_aggregate_function.md)
- [Metric.MetricName](../enums/metric_metric_name.md)
- [Metric.Dimension](../enums/metric_dimension.md)

## Fields

### `firstSeen`

- Type: `google.protobuf.Timestamp` (singular)

Timestamp of the first time the entity was seen in the environment.

### `lastSeen`

- Type: `google.protobuf.Timestamp` (singular)

Time stamp of the last time last time the entity was seen in the environment.

### `sumMeasure`

- Type: [`Metric.Measure`](metric_measure.md) (singular)

Sum of all precomputed measures for the given metric.

### `totalEvents`

- Type: `int64` (singular)

Total number of events used to calculate the given precomputed metric.

### `metricName`

- Type: [`Metric.MetricName`](../enums/metric_metric_name.md) (singular)

Name of the analytic.

### `dimensions`

- Type: [`Metric.Dimension`](../enums/metric_dimension.md) (repeated)

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

- Type: `google.type.Interval` (singular)

Time range for which the custom metric was calculated.
