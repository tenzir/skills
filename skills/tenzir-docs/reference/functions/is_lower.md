# is_lower


Checks if a string is in lowercase.

```tql
is_lower(x:string) -> bool
```

## Description

The `is_lower` function returns `true` if `x` is entirely in lowercase and `false` otherwise.

## Examples

### Check if a string is lowercase

```tql
from {x: "hello".is_lower()}
```

```tql
{x: true}
```

## See Also

* [`is_alpha`](http://docs.tenzir.com/reference/functions/is_alpha.md)
* [`is_upper`](http://docs.tenzir.com/reference/functions/is_upper.md)
* [`to_lower`](http://docs.tenzir.com/reference/functions/to_lower.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)