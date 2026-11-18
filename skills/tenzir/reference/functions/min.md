---
title: "min"
canonical: https://tenzir.com/docs/v6.22.0/reference/functions/min
source: https://tenzir.com/docs/v6.22.0/reference/functions/min.md
section: "Docs"
---

# min

> Computes the minimum of all grouped values.

Computes the minimum of all grouped values.

```tql
min(xs:list) -> number
```

## Description

The `min` function returns the smallest numeric value in `xs`.

### `xs: list`

The values to evaluate.

## Examples

### Find the minimum value

```tql
from {x: 1}, {x: 2}, {x: 3}
summarize min_value=min(x)
```

```tql
{min_value: 1}
```

## See Also

* [`max`](max.md)
* [`mean`](mean.md)
* [`sum`](sum.md)
* [Aggregate event streams](../../guides/analyze/aggregate-event-streams.md)
