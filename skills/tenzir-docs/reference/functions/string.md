# string


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

* fn[`float`](float.md)
* fn[`int`](int.md)
* fn[`ip`](ip.md)
* fn[`subnet`](subnet.md)
* fn[`time`](time.md)
* fn[`uint`](uint.md)
* [Transform values](../../guides/transformation/transform-values.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)