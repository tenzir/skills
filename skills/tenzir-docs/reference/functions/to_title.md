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

* fn[`capitalize`](capitalize.md)
* fn[`is_title`](is_title.md)
* fn[`to_lower`](to_lower.md)
* fn[`to_upper`](to_upper.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)