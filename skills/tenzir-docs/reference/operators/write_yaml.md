# write_yaml


Transforms the input event stream to YAML byte stream.

```tql
write_yaml
```

## Description

Transforms the input event stream to YAML byte stream.

## Examples

### Convert a JSON file into a YAML file

```tql
from_file "input.json" {
  read_json
}
to_file "output.yaml" {
  write_yaml
}
```

## See Also

* [`parse_yaml`](http://docs.tenzir.com/reference/functions/parse_yaml.md)
* [`print_yaml`](http://docs.tenzir.com/reference/functions/print_yaml.md)
* [`read_yaml`](http://docs.tenzir.com/reference/operators/read_yaml.md)