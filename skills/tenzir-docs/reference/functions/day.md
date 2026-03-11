# day


Extracts the day component from a timestamp.

```tql
day(x: time) -> int
```

## Description

The `day` function extracts the day component from a timestamp as an integer (1-31).

### `x: time`

The timestamp from which to extract the day.

## Examples

### Extract the day from a timestamp

```tql
from {
  ts: 2024-06-15T14:30:45.123456,
}
day = ts.day()
```

```tql
{
  ts: 2024-06-15T14:30:45.123456,
  day: 15,
}
```

## See Also

* fn[`year`](/reference/functions/year.md)
* fn[`month`](/reference/functions/month.md)
* fn[`hour`](/reference/functions/hour.md)
* fn[`minute`](/reference/functions/minute.md)
* fn[`second`](/reference/functions/second.md)
* [Work with time](../../guides/transformation/work-with-time.md)