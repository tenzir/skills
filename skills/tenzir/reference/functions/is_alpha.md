---
title: "is_alpha"
canonical: https://tenzir.com/docs/v6.22.0/reference/functions/is_alpha
source: https://tenzir.com/docs/v6.22.0/reference/functions/is_alpha.md
section: "Docs"
---

# is_alpha

> Checks if a string contains only alphabetic characters.

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

* [`is_alnum`](is_alnum.md)
* [`is_lower`](is_lower.md)
* [`is_numeric`](is_numeric.md)
* [`is_printable`](is_printable.md)
* [`is_upper`](is_upper.md)
* [Manipulate strings](../../guides/shape/manipulate-strings.md)
