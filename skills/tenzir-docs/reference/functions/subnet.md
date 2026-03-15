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

* [`float`](/reference/functions/float.md)
* [`int`](/reference/functions/int.md)
* [`ip`](/reference/functions/ip.md)
* [`ip_category`](/reference/functions/ip_category.md)
* [`is_global`](/reference/functions/is_global.md)
* [`is_link_local`](/reference/functions/is_link_local.md)
* [`is_loopback`](/reference/functions/is_loopback.md)
* [`is_multicast`](/reference/functions/is_multicast.md)
* [`is_private`](/reference/functions/is_private.md)
* [`is_v4`](/reference/functions/is_v4.md)
* [`is_v6`](/reference/functions/is_v6.md)
* [`string`](/reference/functions/string.md)
* [`time`](/reference/functions/time.md)
* [`uint`](/reference/functions/uint.md)