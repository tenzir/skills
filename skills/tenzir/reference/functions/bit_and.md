---
title: "bit_and"
canonical: https://tenzir.com/docs/v6.22.0/reference/functions/bit_and
source: https://tenzir.com/docs/v6.22.0/reference/functions/bit_and.md
section: "Docs"
---

# bit_and

> Computes the bit-wise AND of its arguments.

Computes the bit-wise AND of its arguments.

```tql
bit_and(lhs:number, rhs:number) -> number
```

## Description

The `bit_and` function computes the bit-wise AND of `lhs` and `rhs`. The operation is performed on each corresponding bit position of the two numbers.

### `lhs: number`

The left-hand side operand.

### `rhs: number`

The right-hand side operand.

## Examples

### Perform bit-wise AND on integers

```tql
from {x: bit_and(5, 3)}
```

```tql
{x: 1}
```

## See Also

* [`bit_not`](bit_not.md)
* [`bit_or`](bit_or.md)
* [`bit_xor`](bit_xor.md)
* [`shift_left`](shift_left.md)
* [`shift_right`](shift_right.md)
