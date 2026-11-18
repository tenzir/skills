---
title: "string"
canonical: https://tenzir.com/docs/v6.22.0/reference/functions/string
source: https://tenzir.com/docs/v6.22.0/reference/functions/string.md
section: "Docs"
---

# string

> Casts an expression to a string.

Casts an expression to a string.

```tql
string(x:any) -> string
```

## Description

The `string` function casts the given value `x` to a string.

## Examples

### Cast an IP address to a string

```tql
from {x: string(1.2.3.4)}
```

```tql
{x: "1.2.3.4"}
```

## See Also

* [`float`](float.md)
* [`int`](int.md)
* [`ip`](ip.md)
* [`subnet`](subnet.md)
* [`time`](time.md)
* [`uint`](uint.md)
* [Transform values](../../guides/shape/transform-values.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)
