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

* [`to_upper`](http://docs.tenzir.com/reference/functions/to_upper.md)
* [`to_lower`](http://docs.tenzir.com/reference/functions/to_lower.md)
* [`to_title`](http://docs.tenzir.com/reference/functions/to_title.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)