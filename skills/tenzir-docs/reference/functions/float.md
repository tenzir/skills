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

* [`int`](/reference/functions/int.md)
* [`ip`](/reference/functions/ip.md)
* [`string`](/reference/functions/string.md)
* [`subnet`](/reference/functions/subnet.md)
* [`time`](/reference/functions/time.md)
* [`uint`](/reference/functions/uint.md)
* [Transform values](../../guides/transformation/transform-values.md)