# subnet


Casts an expression to a subnet value.

```tql
subnet(x:string) -> subnet
```

## Description

The `subnet` function casts an expression to a subnet.

### `x: string`

The string expression to cast.

## Examples

### Cast a string to a subnet

```tql
from {x: subnet("1.2.3.4/16")}
```

```tql
{x: 1.2.0.0/16}
```

## See Also

* fn[`float`](float.md)
* fn[`int`](int.md)
* fn[`ip`](ip.md)
* fn[`ip_category`](ip_category.md)
* fn[`is_global`](is_global.md)
* fn[`is_link_local`](is_link_local.md)
* fn[`is_loopback`](is_loopback.md)
* fn[`is_multicast`](is_multicast.md)
* fn[`is_private`](is_private.md)
* fn[`is_v4`](is_v4.md)
* fn[`is_v6`](is_v6.md)
* fn[`string`](string.md)
* fn[`time`](time.md)
* fn[`uint`](uint.md)