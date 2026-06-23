# bit_xor


Computes the bit-wise XOR of its arguments.

```tql
bit_xor(lhs:number, rhs:number) -> number
```

## Description

The `bit_xor` function computes the bit-wise XOR (exclusive OR) of `lhs` and `rhs`. The operation is performed on each corresponding bit position of the two numbers.

### `lhs: number`

The left-hand side operand.

### `rhs: number`

The right-hand side operand.

## Examples

### Perform bit-wise XOR on integers

```tql
from {x: bit_xor(5, 3)}
```

```tql
{x: 6}
```

## See Also

* [`bit_and`](http://docs.tenzir.com/reference/functions/bit_and.md)
* [`bit_not`](http://docs.tenzir.com/reference/functions/bit_not.md)
* [`bit_or`](http://docs.tenzir.com/reference/functions/bit_or.md)
* [`shift_left`](http://docs.tenzir.com/reference/functions/shift_left.md)
* [`shift_right`](http://docs.tenzir.com/reference/functions/shift_right.md)