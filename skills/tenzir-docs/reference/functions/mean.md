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

* [`max`](http://docs.tenzir.com/reference/functions/max.md)
* [`median`](http://docs.tenzir.com/reference/functions/median.md)
* [`min`](http://docs.tenzir.com/reference/functions/min.md)
* [`quantile`](http://docs.tenzir.com/reference/functions/quantile.md)
* [`stddev`](http://docs.tenzir.com/reference/functions/stddev.md)
* [`sum`](http://docs.tenzir.com/reference/functions/sum.md)
* [`variance`](http://docs.tenzir.com/reference/functions/variance.md)
* [Aggregate event streams](../../guides/analytics/aggregate-event-streams.md)
* [Plot data with charts](../../tutorials/plot-data-with-charts.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)