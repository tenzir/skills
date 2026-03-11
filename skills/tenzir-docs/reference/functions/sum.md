# sum


Computes the sum of all values.

```tql
sum(xs:list) -> int
```

## Description

The `sum` function computes the total of all number values.

### `xs: list`

The values to aggregate.

## Examples

### Compute a sum over a group of events

```tql
from {x: 1}, {x: 2}, {x: 3}
summarize n=sum(x)
```

```tql
{n: 6}
```

## See Also

* fn[`collect`](/reference/functions/collect.md)
* fn[`max`](/reference/functions/max.md)
* fn[`mean`](/reference/functions/mean.md)
* fn[`min`](/reference/functions/min.md)
* [Aggregate and summarize data](../../guides/analytics/aggregate-and-summarize.md)
* [Plot data with charts](../../tutorials/plot-data-with-charts.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)