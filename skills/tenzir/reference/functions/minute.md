---
title: "minute"
canonical: https://tenzir.com/docs/reference/functions/minute
source: https://tenzir.com/docs/reference/functions/minute.md
section: "Docs"
---

# minute

> Extracts the minute component from a timestamp.

Extracts the minute component from a timestamp.

```tql
minute(x: time) -> int
```

## Description

The `minute` function extracts the minute component from a timestamp as an integer (0-59).

### `x: time`

The timestamp from which to extract the minute.

## Examples

### Extract the minute from a timestamp

```tql
from {
  ts: 2024-06-15T14:30:45.123456,
}
minute = ts.minute()
```

```tql
{
  ts: 2024-06-15T14:30:45.123456,
  minute: 30,
}
```

## See Also

* [`year`](year.md)
* [`month`](month.md)
* [`day`](day.md)
* [`hour`](hour.md)
* [`second`](second.md)
* [Calculate with time](../../guides/shape/calculate-with-time.md)
