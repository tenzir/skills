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

* fn[`capitalize`](/reference/functions/capitalize.md)
* fn[`is_lower`](/reference/functions/is_lower.md)
* fn[`to_title`](/reference/functions/to_title.md)
* fn[`to_upper`](/reference/functions/to_upper.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)