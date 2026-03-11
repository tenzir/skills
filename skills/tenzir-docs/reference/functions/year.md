# year


Extracts the year component from a timestamp.

```tql
year(x: time) -> int
```

## Description

The `year` function extracts the year component from a timestamp as an integer.

### `x: time`

The timestamp from which to extract the year.

## Examples

### Extract the year from a timestamp

```tql
from {
  ts: 2024-06-15T14:30:45.123456,
}
year = ts.year()
```

```tql
{
  ts: 2024-06-15T14:30:45.123456,
  year: 2024,
}
```

## See Also

* fn[`month`](/reference/functions/month.md)
* fn[`day`](/reference/functions/day.md)
* fn[`hour`](/reference/functions/hour.md)
* fn[`minute`](/reference/functions/minute.md)
* fn[`second`](/reference/functions/second.md)
* [Work with time](../../guides/transformation/work-with-time.md)