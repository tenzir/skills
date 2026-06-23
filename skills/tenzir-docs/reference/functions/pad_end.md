# pad_end


Pads a string at the end to a specified length.

```tql
pad_end(x:string, length:int, [pad_char:string]) -> string
```

## Description

The `pad_end` function pads the string `x` at the end with `pad_char` (default: space) until it reaches the specified `length`. If the string is already longer than or equal to the specified length, it returns the original string unchanged.

### `x: string`

The string to pad.

### `length: int`

The target length of the resulting string.

### `pad_char: string`

The character to use for padding. Must be a single character. Defaults to a space.

Defaults to `" "`.

## Examples

### Pad with spaces

```tql
from {x: "hello".pad_end(10)}
```

```tql
{x: "hello     "}
```

### Pad with custom character

```tql
from {x: "hello".pad_end(10, ".")}
```

```tql
{x: "hello....."}
```

### String already long enough

```tql
from {x: "hello world".pad_end(5)}
```

```tql
{x: "hello world"}
```

## See Also

* [`pad_start`](http://docs.tenzir.com/reference/functions/pad_start.md)
* [`trim`](http://docs.tenzir.com/reference/functions/trim.md)
* [`trim_end`](http://docs.tenzir.com/reference/functions/trim_end.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)
* [Mask sensitive data](../../guides/transformation/mask-sensitive-data.md)