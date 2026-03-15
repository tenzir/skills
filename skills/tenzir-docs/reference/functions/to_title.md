# to_title


Converts a string to title case.

```tql
to_title(x:string) -> string
```

## Description

The `to_title` function converts all words in `x` to title case.

## Examples

### Convert a string to title case

```tql
from {x: "hello world".to_title()}
```

```tql
{x: "Hello World"}
```

## See Also

* [`capitalize`](/reference/functions/capitalize.md)
* [`is_title`](/reference/functions/is_title.md)
* [`to_lower`](/reference/functions/to_lower.md)
* [`to_upper`](/reference/functions/to_upper.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)