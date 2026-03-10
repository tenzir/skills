# starts_with


Checks if a string starts with a specified substring.

```tql
starts_with(x:string, prefix:string) -> bool
```

## Description

The `starts_with` function returns `true` if `x` starts with `prefix` and `false` otherwise.

## Examples

### Check if a string starts with a substring

```tql
from {x: "hello".starts_with("he")}
```

```tql
{x: true}
```

## See Also

* fn[`ends_with`](ends_with.md)
* [Filter and select data](../../guides/transformation/filter-and-select-data.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)