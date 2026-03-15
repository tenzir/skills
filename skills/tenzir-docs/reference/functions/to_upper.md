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

* [`capitalize`](/reference/functions/capitalize.md)
* [`is_upper`](/reference/functions/is_upper.md)
* [`to_lower`](/reference/functions/to_lower.md)
* [`to_title`](/reference/functions/to_title.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)