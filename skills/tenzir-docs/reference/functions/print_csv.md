# print_csv


Prints a record as a comma-separated string of values.

```tql
print_csv(input:record, [list_separator=str, null_value=str]) -> string
```

## Description

The `print_csv` function prints a record's values as a comma separated string.

### `input: record`

The record you want to print.

### `list_separator = str (optional)`

The string separating the elements in list fields.

Defaults to `";"`.

### `null_value = str (optional)`

The string denoting an absent value.

Defaults to `""`.

## Examples

```tql
from {
  x:1,
  y:true,
  z: "String"
}
output = this.print_csv()
```

```tql
{
  x: 1,
  y: true,
  z: "String",
  output: "1,true,String",
}
```

## See Also

* [`write_csv`](/reference/operators/write_csv.md)
* [`parse_csv`](/reference/functions/parse_csv.md)