# is_v4


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

* [`ip_category`](http://docs.tenzir.com/reference/functions/ip_category.md)
* [`is_global`](http://docs.tenzir.com/reference/functions/is_global.md)
* [`is_link_local`](http://docs.tenzir.com/reference/functions/is_link_local.md)
* [`is_loopback`](http://docs.tenzir.com/reference/functions/is_loopback.md)
* [`is_multicast`](http://docs.tenzir.com/reference/functions/is_multicast.md)
* [`is_private`](http://docs.tenzir.com/reference/functions/is_private.md)
* [`is_v6`](http://docs.tenzir.com/reference/functions/is_v6.md)