# import


Imports events into a Tenzir node.

```tql
import
```

## Description

The `import` operator persists events in a Tenzir node.

This operator is the dual to [`export`](export.md).

## Examples

### Import Zeek connection logs in TSV format

```tql
load_file "conn.log"
read_zeek_tsv
import
```

## See Also

* [`export`](export.md)
* [`publish`](publish.md)
* [Import into a node](../../guides/edge-storage/import-into-a-node.md)