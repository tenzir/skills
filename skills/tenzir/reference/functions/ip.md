---
title: "ip"
canonical: https://tenzir.com/docs/v6.22.0/reference/functions/ip
source: https://tenzir.com/docs/v6.22.0/reference/functions/ip.md
section: "Docs"
---

# ip

> Casts an expression to an IP address.

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

* [`float`](float.md)
* [`int`](int.md)
* [`ip_category`](ip_category.md)
* [`is_global`](is_global.md)
* [`is_link_local`](is_link_local.md)
* [`is_loopback`](is_loopback.md)
* [`is_multicast`](is_multicast.md)
* [`is_private`](is_private.md)
* [`is_v4`](is_v4.md)
* [`is_v6`](is_v6.md)
* [`string`](string.md)
* [`subnet`](subnet.md)
* [`time`](time.md)
* [`uint`](uint.md)
