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

* fn[`float`](/reference/functions/float.md)
* fn[`int`](/reference/functions/int.md)
* fn[`ip`](/reference/functions/ip.md)
* fn[`subnet`](/reference/functions/subnet.md)
* fn[`time`](/reference/functions/time.md)
* fn[`uint`](/reference/functions/uint.md)
* [Transform values](../../guides/transformation/transform-values.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)