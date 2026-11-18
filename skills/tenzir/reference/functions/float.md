---
title: "float"
canonical: https://tenzir.com/docs/v6.22.0/reference/functions/float
source: https://tenzir.com/docs/v6.22.0/reference/functions/float.md
section: "Docs"
---

# float

> Casts an expression to a float.

Casts an expression to a float.

```tql
float(x:any) -> float
```

## Description

The `float` function converts the given value `x` to a floating-point value.

## Examples

### Cast an integer to a float

```tql
from {x: float(42)}
```

```tql
{x: 42.0}
```

### Cast a string to a float

```tql
from {x: float("4.2")}
```

```tql
{x: 4.2}
```

## See Also

* [`int`](int.md)
* [`ip`](ip.md)
* [`string`](string.md)
* [`subnet`](subnet.md)
* [`time`](time.md)
* [`uint`](uint.md)
* [Transform values](../../guides/shape/transform-values.md)
