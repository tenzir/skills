---
title: "is_alnum"
canonical: https://tenzir.com/docs/v6.22.0/reference/functions/is_alnum
source: https://tenzir.com/docs/v6.22.0/reference/functions/is_alnum.md
section: "Docs"
---

# is_alnum

> Checks if a string is alphanumeric.

Checks if a string is alphanumeric.

```tql
is_alnum(x:string) -> bool
```

## Description

The `is_alnum` function returns `true` if `x` contains only alphanumeric characters and `false` otherwise.

## Examples

### Check if a string is alphanumeric

```tql
from {x: "hello123".is_alnum()}
```

```tql
{x: true}
```

## See Also

* [`is_alpha`](is_alpha.md)
* [`is_numeric`](is_numeric.md)
* [`is_printable`](is_printable.md)
* [Manipulate strings](../../guides/shape/manipulate-strings.md)
