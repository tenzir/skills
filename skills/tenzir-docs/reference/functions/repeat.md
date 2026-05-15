# repeat


Repeats a string a specified number of times.

```tql
repeat(x:string, n:int) -> string
```

## Description

The `repeat` function returns a new string consisting of `x` repeated `n` times. If `n` is `0`, the function returns an empty string.

### `x: string`

The string to repeat.

### `n: int`

The number of times to repeat `x`. Must be non-negative.

## Examples

### Repeat a string

```tql
from {message: "na".repeat(8)}
```

```tql
{message: "nananananananana"}
```

### Repeat zero times

```tql
from {message: "na".repeat(0)}
```

```tql
{message: ""}
```

## See Also

* [`pad_end`](/reference/functions/pad_end.md)
* [`pad_start`](/reference/functions/pad_start.md)
* [`replace`](/reference/functions/replace.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)