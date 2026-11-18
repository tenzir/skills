---
title: "is_v4"
canonical: https://tenzir.com/docs/reference/functions/is_v4
source: https://tenzir.com/docs/reference/functions/is_v4.md
section: "Docs"
---

# is_v4

> Checks whether an IP address has version number 4.

Checks whether an IP address has version number 4.

```tql
is_v4(x:ip) -> bool
```

## Description

The `ipv4` function checks whether the version number of a given IP address `x` is 4.

## Examples

### Check if an IP is IPv4

```tql
from {
  x: 1.2.3.4.is_v4(),
  y: ::1.is_v4(),
}
```

```tql
{
  x: true,
  y: false,
}
```

## See Also

* [`ip_category`](ip_category.md)
* [`is_global`](is_global.md)
* [`is_link_local`](is_link_local.md)
* [`is_loopback`](is_loopback.md)
* [`is_multicast`](is_multicast.md)
* [`is_private`](is_private.md)
* [`is_v6`](is_v6.md)
