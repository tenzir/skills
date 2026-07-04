---
title: "package::remove"
canonical: https://tenzir.com/docs/reference/operators/package/remove
source: https://tenzir.com/docs/reference/operators/package/remove.md
section: "Docs"
---

# package::remove

> Uninstalls a package.

Uninstalls a package.

```tql
package::remove package_id:string
```

## Description

The `package::remove` operator uninstalls a previously installed package.

### `package_id : string`

The unique ID of the package as in the package definition.

## Examples

### Remove an installed package

```tql
package::remove "suricata-ocsf"
```

## See Also

* [`package::add`](https://tenzir.com/docs/reference/operators/package/add.md)
* [`package::list`](https://tenzir.com/docs/reference/operators/package/list.md)
* [Install a package](../../../guides/packages/install-a-package.md)
* [Write a package](../../../tutorials/write-a-package.md)
