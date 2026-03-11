# load_stdin


Accepts bytes from standard input.

```tql
load_stdin
```

## Description

Accepts bytes from standard input. This is mostly useful when using the `tenzir` executable as part of a shell script.

## Examples

### Pipe text into `tenzir`

```sh
echo "Hello World" | tenzir
```

```tql
load_stdin
read_lines
```

```tql
{
  line: "Hello World",
}
```

## See Also

* [`load_file`](/reference/operators/load_file.md)
* [`save_stdout`](/reference/operators/save_stdout.md)
* [Map data to OCSF](../../tutorials/map-data-to-ocsf.md)