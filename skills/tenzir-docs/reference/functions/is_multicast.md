# is_multicast


Checks whether an IP address is a multicast address.

```tql
is_multicast(x:ip) -> bool
```

## Description

The `is_multicast` function checks whether a given IP address `x` is a multicast address.

For IPv4, multicast addresses are in the range 224.0.0.0 to 239.255.255.255 (224.0.0.0/4).

For IPv6, multicast addresses start with the prefix ff00::/8.

## Examples

### Check if an IP is multicast

```tql
from {
  ipv4_multicast: 224.0.0.1.is_multicast(),
  ipv6_multicast: ff02::1.is_multicast(),
  not_multicast: 8.8.8.8.is_multicast(),
}
```

```tql
{
  ipv4_multicast: true,
  ipv6_multicast: true,
  not_multicast: false,
}
```

## See Also

* fn[`ip_category`](ip_category.md)
* fn[`is_global`](is_global.md)
* fn[`is_link_local`](is_link_local.md)
* fn[`is_loopback`](is_loopback.md)
* fn[`is_private`](is_private.md)
* fn[`is_v4`](is_v4.md)
* fn[`is_v6`](is_v6.md)