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

* [`float`](/reference/functions/float.md)
* [`int`](/reference/functions/int.md)
* [`ip_category`](/reference/functions/ip_category.md)
* [`is_global`](/reference/functions/is_global.md)
* [`is_link_local`](/reference/functions/is_link_local.md)
* [`is_loopback`](/reference/functions/is_loopback.md)
* [`is_multicast`](/reference/functions/is_multicast.md)
* [`is_private`](/reference/functions/is_private.md)
* [`is_v4`](/reference/functions/is_v4.md)
* [`is_v6`](/reference/functions/is_v6.md)
* [`string`](/reference/functions/string.md)
* [`subnet`](/reference/functions/subnet.md)
* [`time`](/reference/functions/time.md)
* [`uint`](/reference/functions/uint.md)