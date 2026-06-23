# prepend


Inserts an element at the start of a list.

```tql
prepend(xs:list, x:any) -> list
```

## Description

The `prepend` function returns the list `xs` with `x` inserted at the front. The expression `xs.prepend(y)` is equivalent to `[x, ...xs]`.

If `xs` is `null`, it is treated like an empty list, so `null.prepend(x)` returns `[x]`.

## Examples

### Prepend a number to a list

```tql
from {xs: [1, 2]}
xs = xs.prepend(3)
```

```tql
{xs: [3, 1, 2]}
```

### Prepend to a nullable list

```tql
from {xs: null}
xs = xs.prepend(3)
```

```tql
{
  xs: [
    3,
  ],
}
```

## See Also

* [`add`](http://docs.tenzir.com/reference/functions/add.md)
* [`append`](http://docs.tenzir.com/reference/functions/append.md)
* [`concatenate`](http://docs.tenzir.com/reference/functions/concatenate.md)
* [`remove`](http://docs.tenzir.com/reference/functions/remove.md)
* [Shape lists](../../guides/transformation/shape-lists.md)