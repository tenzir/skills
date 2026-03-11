# is_alpha


Checks if a string contains only alphabetic characters.

```tql
is_alpha(x:string) -> bool
```

## Description

The `is_alpha` function returns `true` if `x` contains only alphabetic characters and `false` otherwise.

## Examples

### Check if a string is alphabetic

```tql
from {x: "hello".is_alpha()}
```

```tql
{x: true}
```

## See Also

* fn[`is_alnum`](/reference/functions/is_alnum.md)
* fn[`is_lower`](/reference/functions/is_lower.md)
* fn[`is_numeric`](/reference/functions/is_numeric.md)
* fn[`is_printable`](/reference/functions/is_printable.md)
* fn[`is_upper`](/reference/functions/is_upper.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)