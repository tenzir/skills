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

* fn[`float`](/reference/functions/float.md)
* fn[`int`](/reference/functions/int.md)
* fn[`ip`](/reference/functions/ip.md)
* fn[`ip_category`](/reference/functions/ip_category.md)
* fn[`is_global`](/reference/functions/is_global.md)
* fn[`is_link_local`](/reference/functions/is_link_local.md)
* fn[`is_loopback`](/reference/functions/is_loopback.md)
* fn[`is_multicast`](/reference/functions/is_multicast.md)
* fn[`is_private`](/reference/functions/is_private.md)
* fn[`is_v4`](/reference/functions/is_v4.md)
* fn[`is_v6`](/reference/functions/is_v6.md)
* fn[`string`](/reference/functions/string.md)
* fn[`time`](/reference/functions/time.md)
* fn[`uint`](/reference/functions/uint.md)