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

### `first_seen`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `firstSeen`

Timestamp of the first time the entity was seen in the environment.

### `last_seen`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `lastSeen`

Time stamp of the last time last time the entity was seen in the environment.

### `sum_measure`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`Metric.Measure`](metric_measure.md)
- **JSON name**: `sumMeasure`

Sum of all precomputed measures for the given metric.

### `total_events`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `totalEvents`

Total number of events used to calculate the given precomputed metric.

### `metric_name`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`Metric.MetricName`](../enums/metric_metric_name.md)
- **JSON name**: `metricName`

Name of the analytic.

### `dimensions`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: [`Metric.Dimension`](../enums/metric_dimension.md)
- **JSON name**: `dimensions`

All group by clauses used to calculate the metric.

### `export_window`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `exportWindow`

Export window for which the metric was exported.

### `display_name`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `displayName`

Display name of the custom metric. Google-authored metrics do not have a display name.

### `outcome_variables`

- **Number**: `9`
- **Cardinality**: `repeated`
- **Type**: [`FindingVariable`](finding_variable.md)
- **JSON name**: `outcomeVariables`

List of outcome variables used in the custom metric.

### `match_variables`

- **Number**: `10`
- **Cardinality**: `repeated`
- **Type**: [`FindingVariable`](finding_variable.md)
- **JSON name**: `matchVariables`

List of match variables used in the custom metric.

### `time_range`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `google.type.Interval`
- **JSON name**: `timeRange`

Time range for which the custom metric was calculated.
