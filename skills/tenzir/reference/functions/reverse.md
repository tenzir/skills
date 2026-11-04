---
title: "reverse"
canonical: https://tenzir.com/docs/v7.0.0/reference/functions/reverse
source: https://tenzir.com/docs/v7.0.0/reference/functions/reverse.md
section: "Docs"
---

# reverse

> Reverses the characters of a string.

Reverses the characters of a string.

```tql
reverse(x:string) -> string
```

## Description

The `reverse` function returns a new string with the characters of `x` in reverse order.

This function operates on Unicode codepoints, not grapheme clusters. Hence, it will not correctly reverse grapheme clusters composed of multiple codepoints.

## Examples

### Reverse a string

```tql
from {x: reverse("hello")}
```

```tql
{x: "olleh"}
```

## See Also

* [`slice`](https://tenzir.com/docs/v7.0.0/reference/functions/slice.md)
* [`length_chars`](https://tenzir.com/docs/v7.0.0/reference/functions/length_chars.md)
* [Manipulate strings](../../guides/shape/manipulate-strings.md)
