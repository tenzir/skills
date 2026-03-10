# count_distinct


Counts all distinct non-null grouped values.

```tql
count_distinct(xs:list) -> int
```

## Description

The `count_distinct` function returns the number of unique, non-null values in `xs`.

### `xs: list`

The values to count.

## Examples

### Count distinct values

```tql
from {x: 1}, {x: 2}, {x: 2}, {x: 3}
summarize unique=count_distinct(x)
```

```tql
{unique: 3}
```

## See Also

* fn[`count`](count.md)
* fn[`distinct`](distinct.md)
* [Aggregate and summarize data](../../guides/analytics/aggregate-and-summarize.md)