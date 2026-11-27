---
title: "Read branches"
description: "The workspace repository branches, the origins of branches made from another, and forwards from renamed branch names to their current names, without reading a tree"
canonical: https://tenzir.com/docs/reference/api/workspaces/read-branches
source: https://tenzir.com/docs/reference/api/workspaces/read-branches.md
section: "Docs"
---

# Read branches

> The workspace repository branches, the origins of branches made from another, and forwards from renamed branch names to their current names, without reading a tree

`GET /api/organizations/{org}/workspaces/{workspace}/branches`

The workspace repository branches, the origins of branches made from another, and forwards from renamed branch names to their current names, without reading a tree

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

* `workspace` (`Id / Slug`, required): A workspace identified by its ID or slug within an organization

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Responses

### `200`: Success

Media type: `application/json`

* `branches` (`array<string>`, required)

* `origins` (`array<GitBranchOrigin>`, optional)

  Array items:

  * `branch` (`string`, required)
  * `origin` (`string`, required): The branch this one was made from

* `forwards` (`array<GitBranchForward>`, optional)

  Array items:

  * `from` (`string`, required): The former branch name that was renamed
  * `to` (`string`, required): The current branch name it forwards to

### `400`: CredentialConflict | Validation

Media type: `application/json`

Any of:

* **CredentialConflict** (`CredentialConflict`)

  * `_tag` (`"CredentialConflict"`, required)
  * `message` (`string`, required)

* **Validation** (`Validation`)

  * `_tag` (`"Validation"`, required)
  * `message` (`string`, required)

### `401`: Unauthenticated

Media type: `application/json`

* `_tag` (`"Unauthenticated"`, required)
* `message` (`string`, required)

### `403`: Unauthorized

Media type: `application/json`

* `_tag` (`"Unauthorized"`, required)
* `message` (`string`, required)

### `404`: NotFound

Media type: `application/json`

* `_tag` (`"NotFound"`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
