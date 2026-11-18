---
title: "hour"
canonical: https://tenzir.com/docs/v6.22.0/reference/functions/hour
source: https://tenzir.com/docs/v6.22.0/reference/functions/hour.md
section: "Docs"
---

# hour

> Extracts the hour component from a timestamp.

Extracts the hour component from a timestamp.

```tql
hour(x: time) -> int
```

## Description

The `hour` function extracts the hour component from a timestamp as an integer (0-23).

### `x: time`

The timestamp from which to extract the hour.

## Examples

### Extract the hour from a timestamp

```tql
from {
  ts: 2024-06-15T14:30:45.123456,
}
hour = ts.hour()
```

```tql
{
  ts: 2024-06-15T14:30:45.123456,
  hour: 14,
}
```

## See Also

* [`year`](year.md)
* [`month`](month.md)
* [`day`](day.md)
* [`minute`](minute.md)
* [`second`](second.md)
* [Calculate with time](../../guides/shape/calculate-with-time.md)
