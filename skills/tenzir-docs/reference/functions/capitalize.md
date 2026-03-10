# capitalize


Capitalizes the first character of a string.

```tql
capitalize(x:string) -> string
```

## Description

The `capitalize` function returns the input string with the first character converted to uppercase and the rest to lowercase.

## Examples

### Capitalize a lowercase string

```tql
from {x: "hello world".capitalize()}
```

```tql
{x: "Hello world"}
```

## See Also

* fn[`to_upper`](to_upper.md)
* fn[`to_lower`](to_lower.md)
* fn[`to_title`](to_title.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)