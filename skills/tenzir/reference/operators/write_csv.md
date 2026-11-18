---
title: "write_csv"
canonical: https://tenzir.com/docs/v6.22.0/reference/operators/write_csv
source: https://tenzir.com/docs/v6.22.0/reference/operators/write_csv.md
section: "Docs"
---

# write_csv

> Transforms event stream to CSV (Comma-Separated Values) byte stream.

Transforms event stream to CSV (Comma-Separated Values) byte stream.

```tql
write_csv [list_separator=str, null_value=str, no_header=bool]
```

## Description

The `write_csv` operator transforms an event stream into a byte stream by writing the events as CSV.

### `list_separator = str (optional)`

The string separating different elements in a list within a single field.

Defaults to `";"`.

### `null_value = str (optional)`

The string denoting an absent value.

Defaults to `" "`.

### `no_header = bool (optional)`

Whether to not print a header line containing the field names.

## Examples

Write an event as CSV.

```tql
from {x:1, y:true, z: "String"}
write_csv
```

```plaintext
x,y,z
1,true,String
```

## See Also

* [`parse_csv`](../functions/parse_csv.md)
* [`print_csv`](../functions/print_csv.md)
* [`read_csv`](read_csv.md)
* [`write_lines`](write_lines.md)
* [`write_ssv`](write_ssv.md)
* [`write_tsv`](write_tsv.md)
* [`write_xsv`](write_xsv.md)
* [Convert data formats](../../guides/shape/convert-data-formats.md)
