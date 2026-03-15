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

* [`is_alpha`](/reference/functions/is_alpha.md)
* [`is_lower`](/reference/functions/is_lower.md)
* [`to_upper`](/reference/functions/to_upper.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)