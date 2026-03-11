# variance


Computes the variance of all grouped values.

```tql
variance(xs:list) -> float
```

## Description

The `variance` function returns the variance of all numeric values in `xs`.

### `xs: list`

The values to evaluate.

## Examples

### Compute the variance of values

```tql
from {x: 1}, {x: 2}, {x: 3}
summarize variance_value=variance(x)
```

```tql
{variance_value: 0.666}
```

## See Also

* fn[`stddev`](/reference/functions/stddev.md)
* fn[`mean`](/reference/functions/mean.md)
* [Aggregate and summarize data](../../guides/analytics/aggregate-and-summarize.md)