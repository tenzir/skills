---
title: "mean"
canonical: https://tenzir.com/docs/reference/functions/mean
source: https://tenzir.com/docs/reference/functions/mean.md
section: "Docs"
---

# mean

> Computes the mean of all grouped values.

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

* [`max`](max.md)
* [`median`](median.md)
* [`min`](min.md)
* [`quantile`](quantile.md)
* [`stddev`](stddev.md)
* [`sum`](sum.md)
* [`variance`](variance.md)
* [Aggregate event streams](../../guides/analyze/aggregate-event-streams.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)
