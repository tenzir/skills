# contains_null


Checks whether the input contains any `null` values.

```tql
contains_null(x:any) -> bool
```

## Description

The `contains_null` function checks if the input contains any `null` values recursively.

### `x: any`

The input to check for `null` values.

## Examples

### Check if list has null values

```tql
from {x: [{a: 1}, {}]}
contains_null = x.contains_null()
```

```tql
{
  x: [
    {
      a: 1,
    },
    {
      a: null,
    },
  ],
  contains_null: true,
}
```

### Check a record with null values

```tql
from {x: "foo", y: null}
contains_null = this.contains_null()
```

```tql
{
  x: "foo",
  y: null,
  contains_null: true,
}
```

## See Also

* fn[`contains`](contains.md)
* fn[`has`](has.md)
* fn[`is_empty`](is_empty.md)