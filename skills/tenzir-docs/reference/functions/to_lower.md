# to_lower


Converts a string to lowercase.

```tql
to_lower(x:string) -> string
```

## Description

The `to_lower` function converts all characters in `x` to lowercase.

## Examples

### Convert a string to lowercase

```tql
from {x: "HELLO".to_lower()}
```

```tql
{x: "hello"}
```

## See Also

* fn[`capitalize`](capitalize.md)
* fn[`is_lower`](is_lower.md)
* fn[`to_title`](to_title.md)
* fn[`to_upper`](to_upper.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)