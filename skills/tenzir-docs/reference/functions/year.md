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

* [`month`](http://docs.tenzir.com/reference/functions/month.md)
* [`day`](http://docs.tenzir.com/reference/functions/day.md)
* [`hour`](http://docs.tenzir.com/reference/functions/hour.md)
* [`minute`](http://docs.tenzir.com/reference/functions/minute.md)
* [`second`](http://docs.tenzir.com/reference/functions/second.md)
* [Work with time](../../guides/transformation/work-with-time.md)
* [Mask sensitive data](../../guides/transformation/mask-sensitive-data.md)