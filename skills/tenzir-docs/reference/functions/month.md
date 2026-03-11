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

* fn[`year`](/reference/functions/year.md)
* fn[`day`](/reference/functions/day.md)
* fn[`hour`](/reference/functions/hour.md)
* fn[`minute`](/reference/functions/minute.md)
* fn[`second`](/reference/functions/second.md)
* [Work with time](../../guides/transformation/work-with-time.md)