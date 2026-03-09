# is_upper


Checks if a string is in uppercase.

```tql
is_upper(x:string) -> bool
```

## Description

The `is_upper` function returns `true` if `x` is entirely in uppercase; otherwise, it returns `false`.

## Examples

### Check if a string is uppercase

```tql
from {x: "HELLO".is_upper()}
```

```tql
{x: true}
```

## See Also

* fn[`is_alpha`](is_alpha.md)
* fn[`is_lower`](is_lower.md)
* fn[`to_upper`](to_upper.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)