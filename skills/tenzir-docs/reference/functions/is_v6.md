# is_v6


Checks whether an IP address has version number 6.

```tql
is_v6(x:ip) -> bool
```

## Description

The `is_v6` function checks whether the version number of a given IP address `x` is 6.

## Examples

### Check if an IP is IPv6

```tql
from {
  x: 1.2.3.4.is_v6(),
  y: ::1.is_v6(),
}
```

```tql
{
  x: false,
  y: true,
}
```

## See Also

* fn[`ip_category`](ip_category.md)
* fn[`is_global`](is_global.md)
* fn[`is_link_local`](is_link_local.md)
* fn[`is_loopback`](is_loopback.md)
* fn[`is_multicast`](is_multicast.md)
* fn[`is_private`](is_private.md)
* fn[`is_v4`](is_v4.md)
* [Map data to OCSF](../../tutorials/map-data-to-ocsf.md)