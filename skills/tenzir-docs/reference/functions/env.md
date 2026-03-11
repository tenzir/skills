# env


Reads an environment variable.

```tql
env(x:string) -> string
```

## Description

The `env` function retrieves the value of an environment variable `x`. If the variable does not exist, it returns `null`.

## Examples

### Read the `PATH` environment variable

```tql
from {x: env("PATH")}
```

```tql
{x: "/usr/local/bin:/usr/bin:/bin"}
```

## See Also

* fn[`config`](/reference/functions/config.md)
* fn[`secret`](/reference/functions/secret.md)