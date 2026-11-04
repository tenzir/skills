---
title: "string"
canonical: https://tenzir.com/docs/v7.0.0/reference/functions/string
source: https://tenzir.com/docs/v7.0.0/reference/functions/string.md
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

* [`float`](https://tenzir.com/docs/v7.0.0/reference/functions/float.md)
* [`int`](https://tenzir.com/docs/v7.0.0/reference/functions/int.md)
* [`ip`](https://tenzir.com/docs/v7.0.0/reference/functions/ip.md)
* [`subnet`](https://tenzir.com/docs/v7.0.0/reference/functions/subnet.md)
* [`time`](https://tenzir.com/docs/v7.0.0/reference/functions/time.md)
* [`uint`](https://tenzir.com/docs/v7.0.0/reference/functions/uint.md)
* [Transform values](../../guides/shape/transform-values.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)
