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

* fn[`mean`](/reference/functions/mean.md)
* fn[`mode`](/reference/functions/mode.md)
* fn[`quantile`](/reference/functions/quantile.md)
* [Aggregate and summarize data](../../guides/analytics/aggregate-and-summarize.md)