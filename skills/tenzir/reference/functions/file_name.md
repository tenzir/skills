# file_name

> Extracts the file name from a file path.

Extracts the file name from a file path.

```tql
file_name(x:string) -> string
```

## Description

The `file_name` function returns the file name component of a file path, excluding the parent directories.

## Examples

### Extract the file name from a file path

```tql
from {x: file_name("/path/to/log.json")}
```

```tql
{x: "log.json"}
```

## See Also

* [`parent_dir`](https://tenzir.com/docs/reference/functions/parent_dir.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)
