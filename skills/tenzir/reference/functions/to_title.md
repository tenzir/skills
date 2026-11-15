---
title: "to_title"
canonical: https://tenzir.com/docs/reference/functions/to_title
source: https://tenzir.com/docs/reference/functions/to_title.md
section: "Docs"
---

# to_title

> Converts a string to title case.

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

* [`capitalize`](capitalize.md)
* [`is_title`](is_title.md)
* [`to_lower`](to_lower.md)
* [`to_upper`](to_upper.md)
* [Manipulate strings](../../guides/shape/manipulate-strings.md)
