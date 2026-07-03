# is_numeric

> Checks if a string contains only numeric characters.

Checks if a string contains only numeric characters.

```tql
is_numeric(x:string) -> bool
```

## Description

The `is_numeric` function returns `true` if `x` contains only numeric characters and `false` otherwise.

## Examples

### Check if a string is numeric

```tql
from {x: "1234".is_numeric()}
```

```tql
{x: true}
```

## See Also

* [`is_alnum`](https://tenzir.com/docs/reference/functions/is_alnum.md)
* [`is_alpha`](https://tenzir.com/docs/reference/functions/is_alpha.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)
