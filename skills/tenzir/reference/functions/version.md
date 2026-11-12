---
title: "version"
canonical: https://tenzir.com/docs/v7.0.0/reference/functions/version
source: https://tenzir.com/docs/v7.0.0/reference/functions/version.md
section: "Docs"
---

# version

> Returns the version of the Tenzir node.

Returns the version of the Tenzir node.

```tql
version() -> record
```

## Description

The `version` function returns a record with the version of the Tenzir node, its build configuration, and the versions of its dependencies.

The function returns the same value for every event, so you can use it anywhere in an expression, such as to annotate events with the version of the node that processed them.

### Fields

The returned record has the following fields:

| Field          | Type           | Description                                                                        |
| -------------- | -------------- | ---------------------------------------------------------------------------------- |
| `version`      | `string`       | The formatted version string.                                                      |
| `tag`          | `string`       | An optional identifier of the build.                                               |
| `major`        | `uint64`       | The major release version.                                                         |
| `minor`        | `uint64`       | The minor release version.                                                         |
| `patch`        | `uint64`       | The patch release version.                                                         |
| `features`     | `list<string>` | A list of feature flags that conditionally enable features in the Tenzir Platform. |
| `build`        | `record`       | Build-time configuration options.                                                  |
| `dependencies` | `list<record>` | A list of build-time dependencies and their versions.                              |

The `build` record has the following fields:

| Field        | Type     | Description                                                                |
| ------------ | -------- | -------------------------------------------------------------------------- |
| `type`       | `string` | The configured build type. One of `Release`, `Debug`, or `RelWithDebInfo`. |
| `assertions` | `bool`   | Whether potentially expensive run-time checks are enabled.                 |
| `sanitizers` | `record` | Contains information about additional run-time checks from sanitizers.     |

The `build.sanitizers` record has the following fields:

| Field                | Type   | Description                                          |
| -------------------- | ------ | ---------------------------------------------------- |
| `address`            | `bool` | Whether the address sanitizer is enabled.            |
| `undefined_behavior` | `bool` | Whether the undefined behavior sanitizer is enabled. |

Each record in `dependencies` has the following fields:

| Field     | Type     | Description                                                      |
| --------- | -------- | ---------------------------------------------------------------- |
| `name`    | `string` | The name of the dependency.                                      |
| `version` | `string` | The version of the dependency, or `null` if it is not available. |

## Examples

### Annotate events with the node version

```tql
from {x: 1}
tenzir_version = version().version
```

```tql
{
  x: 1,
  tenzir_version: "6.21.0",
}
```

## See Also

* [`config`](https://tenzir.com/docs/v7.0.0/reference/functions/config.md)
