# float


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

* [`int`](http://docs.tenzir.com/reference/functions/int.md)
* [`ip`](http://docs.tenzir.com/reference/functions/ip.md)
* [`string`](http://docs.tenzir.com/reference/functions/string.md)
* [`subnet`](http://docs.tenzir.com/reference/functions/subnet.md)
* [`time`](http://docs.tenzir.com/reference/functions/time.md)
* [`uint`](http://docs.tenzir.com/reference/functions/uint.md)
* [Transform values](../../guides/transformation/transform-values.md)