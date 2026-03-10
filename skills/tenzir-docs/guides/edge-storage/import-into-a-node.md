# Import into a node


Importing (or *ingesting*) data can be done by [running a pipeline](../basic-usage/run-pipelines.md) that ends with the [`import`](../../reference/operators/import.md) output operator. When managing a pipeline through the app or the API, all pipeline operators run within the node. When using the CLI, at least the `import` operator runs within the node.

Consider this example that takes a Zeek conn.log from our M57 dataset:

```tql
from_file "Zeek/conn.log" { read_zeek_tsv }
select id.orig_h, id.resp_h, orig_bytes, resp_bytes
where orig_bytes > 1 Mi
import
```

The [`import`](../../reference/operators/import.md) operator requires a running node. To run the above pipeline successfully, you need to first [setup a node](../node-setup/provision-a-node.md).

## Contents

- [Export-from-a-node](export-from-a-node.md)
- [Show-available-schemas](show-available-schemas.md)
- [Transform-data-at-rest](transform-data-at-rest.md)