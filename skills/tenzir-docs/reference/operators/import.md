# import


Imports events into a Tenzir node.

```tql
import
```

## Description

The `import` operator persists events in a Tenzir node.

This operator is the dual to [`export`](http://docs.tenzir.com/reference/operators/export.md).

## Examples

### Import Zeek connection logs in TSV format

```tql
from_file "conn.log" {
  read_zeek_tsv
}
import
```

## See Also

* [`export`](http://docs.tenzir.com/reference/operators/export.md)
* [`publish`](http://docs.tenzir.com/reference/operators/publish.md)
* [Import into a node](../../guides/edge-storage/import-into-a-node.md)