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

* [`float`](http://docs.tenzir.com/reference/functions/float.md)
* [`int`](http://docs.tenzir.com/reference/functions/int.md)
* [`ip`](http://docs.tenzir.com/reference/functions/ip.md)
* [`subnet`](http://docs.tenzir.com/reference/functions/subnet.md)
* [`time`](http://docs.tenzir.com/reference/functions/time.md)
* [`uint`](http://docs.tenzir.com/reference/functions/uint.md)
* [Transform values](../../guides/transformation/transform-values.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)