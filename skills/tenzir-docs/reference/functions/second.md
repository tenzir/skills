# second


Extracts the second component from a timestamp with subsecond precision.

```tql
second(x: time) -> float
```

## Description

The `second` function extracts the second component from a timestamp as a floating-point number (0-59.999…) that includes subsecond precision.

### `x: time`

The timestamp from which to extract the second.

## Examples

### Extract the second from a timestamp

```tql
from {
  ts: 2024-06-15T14:30:45.123456,
}
second = ts.second()
```

```tql
{
  ts: 2024-06-15T14:30:45.123456,
  second: 45.123456,
}
```

### Extract only the full second component without subsecond precision

```tql
from {
  ts: 2024-06-15T14:30:45.123456,
}
full_second = ts.second().floor()
```

```tql
{
  ts: 2024-06-15T14:30:45.123456,
  full_second: 45,
}
```

## See Also

* fn[`year`](/reference/functions/year.md)
* fn[`month`](/reference/functions/month.md)
* fn[`day`](/reference/functions/day.md)
* fn[`hour`](/reference/functions/hour.md)
* fn[`minute`](/reference/functions/minute.md)
* [Work with time](../../guides/transformation/work-with-time.md)