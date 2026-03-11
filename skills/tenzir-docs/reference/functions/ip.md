# ip


Casts an expression to an IP address.

```tql
ip(x:string) -> ip
```

## Description

The `ip` function casts the provided string `x` to an IP address.

## Examples

### Cast a string to an IP address

```tql
from {x: ip("1.2.3.4")}
```

```tql
{x: 1.2.3.4}
```

## See Also

* fn[`float`](/reference/functions/float.md)
* fn[`int`](/reference/functions/int.md)
* fn[`ip_category`](/reference/functions/ip_category.md)
* fn[`is_global`](/reference/functions/is_global.md)
* fn[`is_link_local`](/reference/functions/is_link_local.md)
* fn[`is_loopback`](/reference/functions/is_loopback.md)
* fn[`is_multicast`](/reference/functions/is_multicast.md)
* fn[`is_private`](/reference/functions/is_private.md)
* fn[`is_v4`](/reference/functions/is_v4.md)
* fn[`is_v6`](/reference/functions/is_v6.md)
* fn[`string`](/reference/functions/string.md)
* fn[`subnet`](/reference/functions/subnet.md)
* fn[`time`](/reference/functions/time.md)
* fn[`uint`](/reference/functions/uint.md)