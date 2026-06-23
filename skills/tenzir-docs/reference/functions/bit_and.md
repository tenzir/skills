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

* [`bit_not`](http://docs.tenzir.com/reference/functions/bit_not.md)
* [`bit_or`](http://docs.tenzir.com/reference/functions/bit_or.md)
* [`bit_xor`](http://docs.tenzir.com/reference/functions/bit_xor.md)
* [`shift_left`](http://docs.tenzir.com/reference/functions/shift_left.md)
* [`shift_right`](http://docs.tenzir.com/reference/functions/shift_right.md)