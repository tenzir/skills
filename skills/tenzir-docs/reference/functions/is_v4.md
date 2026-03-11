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

* fn[`ip_category`](/reference/functions/ip_category.md)
* fn[`is_global`](/reference/functions/is_global.md)
* fn[`is_link_local`](/reference/functions/is_link_local.md)
* fn[`is_loopback`](/reference/functions/is_loopback.md)
* fn[`is_multicast`](/reference/functions/is_multicast.md)
* fn[`is_private`](/reference/functions/is_private.md)
* fn[`is_v6`](/reference/functions/is_v6.md)