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

* [`float`](http://docs.tenzir.com/reference/functions/float.md)
* [`int`](http://docs.tenzir.com/reference/functions/int.md)
* [`ip_category`](http://docs.tenzir.com/reference/functions/ip_category.md)
* [`is_global`](http://docs.tenzir.com/reference/functions/is_global.md)
* [`is_link_local`](http://docs.tenzir.com/reference/functions/is_link_local.md)
* [`is_loopback`](http://docs.tenzir.com/reference/functions/is_loopback.md)
* [`is_multicast`](http://docs.tenzir.com/reference/functions/is_multicast.md)
* [`is_private`](http://docs.tenzir.com/reference/functions/is_private.md)
* [`is_v4`](http://docs.tenzir.com/reference/functions/is_v4.md)
* [`is_v6`](http://docs.tenzir.com/reference/functions/is_v6.md)
* [`string`](http://docs.tenzir.com/reference/functions/string.md)
* [`subnet`](http://docs.tenzir.com/reference/functions/subnet.md)
* [`time`](http://docs.tenzir.com/reference/functions/time.md)
* [`uint`](http://docs.tenzir.com/reference/functions/uint.md)