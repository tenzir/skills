# month


Extracts the month component from a timestamp.

```tql
month(x: time) -> int
```

## Description

The `month` function extracts the month component from a timestamp as an integer (1-12).

### `x: time`

The timestamp from which to extract the month.

## Examples

### Extract the month from a timestamp

```tql
from {
  ts: 2024-06-15T14:30:45.123456,
}
month = ts.month()
```

```tql
{
  ts: 2024-06-15T14:30:45.123456,
  month: 6,
}
```

## See Also

* [`year`](http://docs.tenzir.com/reference/functions/year.md)
* [`day`](http://docs.tenzir.com/reference/functions/day.md)
* [`hour`](http://docs.tenzir.com/reference/functions/hour.md)
* [`minute`](http://docs.tenzir.com/reference/functions/minute.md)
* [`second`](http://docs.tenzir.com/reference/functions/second.md)
* [Work with time](../../guides/transformation/work-with-time.md)