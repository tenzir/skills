# hour


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

* [`year`](/reference/functions/year.md)
* [`month`](/reference/functions/month.md)
* [`day`](/reference/functions/day.md)
* [`minute`](/reference/functions/minute.md)
* [`second`](/reference/functions/second.md)
* [Work with time](../../guides/transformation/work-with-time.md)