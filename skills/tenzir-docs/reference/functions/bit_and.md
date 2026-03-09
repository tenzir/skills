# bit_and


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

* fn[`bit_not`](bit_not.md)
* fn[`bit_or`](bit_or.md)
* fn[`bit_xor`](bit_xor.md)
* fn[`shift_left`](shift_left.md)
* fn[`shift_right`](shift_right.md)