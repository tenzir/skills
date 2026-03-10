# to_upper


Converts a string to uppercase.

```tql
to_upper(x:string) -> string
```

## Description

The `to_upper` function converts all characters in `x` to uppercase.

## Examples

### Convert a string to uppercase

```tql
from {x: "hello".to_upper()}
```

```tql
{x: "HELLO"}
```

## See Also

* fn[`capitalize`](capitalize.md)
* fn[`is_upper`](is_upper.md)
* fn[`to_lower`](to_lower.md)
* fn[`to_title`](to_title.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)