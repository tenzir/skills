# mean


Computes the mean of all grouped values.

```tql
mean(xs:list) -> float
```

## Description

The `mean` function returns the average of all numeric values in `xs`.

### `xs: list`

The values to average.

## Examples

### Compute the mean value

```tql
from {x: 1}, {x: 2}, {x: 3}
summarize avg=mean(x)
```

```tql
{avg: 2.0}
```

## See Also

* fn[`max`](/reference/functions/max.md)
* fn[`median`](/reference/functions/median.md)
* fn[`min`](/reference/functions/min.md)
* fn[`quantile`](/reference/functions/quantile.md)
* fn[`stddev`](/reference/functions/stddev.md)
* fn[`sum`](/reference/functions/sum.md)
* fn[`variance`](/reference/functions/variance.md)
* [Aggregate and summarize data](../../guides/analytics/aggregate-and-summarize.md)
* [Plot data with charts](../../tutorials/plot-data-with-charts.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)