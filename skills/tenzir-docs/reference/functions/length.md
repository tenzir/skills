# length


Retrieves the length of a list.

```tql
length(xs:list) -> int
```

## Description

The `length` function returns the number of elements in the list `xs`.

## Examples

### Get the length of a list

```tql
from {n: [1, 2, 3].length()}
```

```tql
{n: 3}
```

## See Also

* fn[`is_empty`](/reference/functions/is_empty.md)
* fn[`length_bytes`](/reference/functions/length_bytes.md)
* fn[`length_chars`](/reference/functions/length_chars.md)
* [Shape lists](../../guides/transformation/shape-lists.md)