# file_contents


Reads a file’s contents.

```tql
file_contents(path:string, [binary=bool]) -> blob|string
```

## Description

The `file_contents` function reads a file’s contents.

### `path: string`

Absolute path of file to read.

### `binary = bool (optional)`

Whether to read the file contents as a `blob`, instead of a `string`.

Defaults to `false`.

## Examples

### Read a text file

```tql
from {hostname: file_contents("/etc/hostname")}
```

## See Also

* [`file_name`](/reference/functions/file_name.md)
* [`parent_dir`](/reference/functions/parent_dir.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)