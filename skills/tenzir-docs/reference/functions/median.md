# median


Computes the approximate median of all grouped values using a t-digest algorithm.

```tql
median(xs:list) -> float
```

## Description

The `median` function returns an approximate median of all numeric values in `xs`, computed with a t-digest algorithm.

### `xs: list`

The values to evaluate.

## Examples

### Compute the median value

```tql
from {x: 1}, {x: 2}, {x: 3}, {x: 4}
summarize median_value=median(x)
```

```tql
{median_value: 2.5}
```

## See Also

* [`mean`](http://docs.tenzir.com/reference/functions/mean.md)
* [`mode`](http://docs.tenzir.com/reference/functions/mode.md)
* [`quantile`](http://docs.tenzir.com/reference/functions/quantile.md)
* [Aggregate event streams](../../guides/analytics/aggregate-event-streams.md)