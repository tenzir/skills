# shift_left


Performs a bit-wise left shift.

```tql
shift_left(lhs:number, rhs:number) -> number
```

## Description

The `shift_left` function performs a bit-wise left shift of `lhs` by `rhs` bit positions. Each left shift multiplies the number by 2.

### `lhs: number`

The number to be shifted.

### `rhs: number`

The number of bit positions to shift to the left.

## Examples

### Shift bits to the left

```tql
from {x: shift_left(5, 2)}
```

```tql
{x: 20}
```

## See Also

* [`bit_and`](http://docs.tenzir.com/reference/functions/bit_and.md)
* [`bit_not`](http://docs.tenzir.com/reference/functions/bit_not.md)
* [`bit_or`](http://docs.tenzir.com/reference/functions/bit_or.md)
* [`bit_xor`](http://docs.tenzir.com/reference/functions/bit_xor.md)
* [`shift_right`](http://docs.tenzir.com/reference/functions/shift_right.md)