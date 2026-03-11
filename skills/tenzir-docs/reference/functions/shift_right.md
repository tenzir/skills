# shift_right


Performs a bit-wise right shift.

```tql
shift_right(lhs:number, rhs:number) -> number
```

## Description

The `shift_right` function performs a bit-wise right shift of `lhs` by `rhs` bit positions. Each right shift divides the number by 2, truncating any fractional part.

### `lhs: number`

The number to be shifted.

### `rhs: number`

The number of bit positions to shift to the right.

## Examples

### Shift bits to the right

```tql
from {x: shift_right(20, 2)}
```

```tql
{x: 5}
```

## See Also

* fn[`bit_and`](/reference/functions/bit_and.md)
* fn[`bit_not`](/reference/functions/bit_not.md)
* fn[`bit_or`](/reference/functions/bit_or.md)
* fn[`bit_xor`](/reference/functions/bit_xor.md)
* fn[`shift_left`](/reference/functions/shift_left.md)