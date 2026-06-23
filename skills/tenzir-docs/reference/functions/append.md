# append


Inserts an element at the back of a list.

```tql
append(xs:list, x:any) -> list
```

## Description

The `append` function returns the list `xs` with `x` inserted at the end. The expression `xs.append(x)` is equivalent to `[...xs, x]`.

If `xs` is `null`, it is treated like an empty list, so `null.append(x)` returns `[x]`.

## Examples

### Append a number to a list

```tql
from {xs: [1, 2]}
xs = xs.append(3)
```

```tql
{xs: [1, 2, 3]}
```

### Append to a nullable list

```tql
from {xs: null}
xs = xs.append(3)
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
* [`concatenate`](http://docs.tenzir.com/reference/functions/concatenate.md)
* [`prepend`](http://docs.tenzir.com/reference/functions/prepend.md)
* [`remove`](http://docs.tenzir.com/reference/functions/remove.md)
* [Shape lists](../../guides/transformation/shape-lists.md)