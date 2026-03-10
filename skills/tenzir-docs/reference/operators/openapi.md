# openapi


Shows the node’s OpenAPI specification.

```tql
openapi
```

## Description

The `openapi` operator shows the current Tenzir node’s [OpenAPI specification](https://docs.tenzir.com/reference/node/api) for all available REST endpoint plugins.

## Examples

### Render the OpenAPI specification as YAML

```tql
openapi
write_yaml
```

## See Also

* [`api`](api.md)
* [`serve`](serve.md)