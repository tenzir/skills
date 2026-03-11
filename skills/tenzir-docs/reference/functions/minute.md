# minute


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

* fn[`year`](/reference/functions/year.md)
* fn[`month`](/reference/functions/month.md)
* fn[`day`](/reference/functions/day.md)
* fn[`hour`](/reference/functions/hour.md)
* fn[`second`](/reference/functions/second.md)
* [Work with time](../../guides/transformation/work-with-time.md)