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

* fn[`float`](float.md)
* fn[`int`](int.md)
* fn[`ip_category`](ip_category.md)
* fn[`is_global`](is_global.md)
* fn[`is_link_local`](is_link_local.md)
* fn[`is_loopback`](is_loopback.md)
* fn[`is_multicast`](is_multicast.md)
* fn[`is_private`](is_private.md)
* fn[`is_v4`](is_v4.md)
* fn[`is_v6`](is_v6.md)
* fn[`string`](string.md)
* fn[`subnet`](subnet.md)
* fn[`time`](time.md)
* fn[`uint`](uint.md)