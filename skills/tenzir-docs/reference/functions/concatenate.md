# concatenate


Merges two lists.

```tql
concatenate(xs:list, ys:list) -> list
```

## Description

The `concatenate` function returns a list containing all elements from the lists `xs` and `ys` in order. The expression `concatenate(xs, ys)` is equivalent to `[...xs, ...ys]`.

## Examples

### Concatenate two lists

```tql
from {xs: [1, 2], ys: [3, 4]}
zs = concatenate(xs, ys)
```

```tql
{
  xs: [1, 2],
  ys: [3, 4],
  zs: [1, 2, 3, 4]
}
```

## See Also

* fn[`append`](append.md)
* fn[`merge`](merge.md)
* fn[`prepend`](prepend.md)
* fn[`zip`](zip.md)
* [Shape lists](../../guides/transformation/shape-lists.md)