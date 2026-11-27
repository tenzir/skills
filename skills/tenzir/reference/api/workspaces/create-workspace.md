---
title: "Create workspace"
description: "Creates a workspace in an organization"
canonical: https://tenzir.com/docs/reference/api/workspaces/create-workspace
source: https://tenzir.com/docs/reference/api/workspaces/create-workspace.md
section: "Docs"
---

# Create workspace

> Creates a workspace in an organization

`POST /api/organizations/{org}/workspaces`

Creates a workspace in an organization

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Request body (`application/json`, required)

* `slug` (`string`, required) Length: `<= 40`.
* `name` (`string | null`, optional) Length: `>= 1`.
* `iconUrl` (`string | null`, optional)

## Responses

### `201`: The unit a user works in, holding the deployments, pipelines, and secrets that belong together

Media type: `application/json`

* `id` (`string`, required): A UUID
* `slug` (`string`, required) Length: `<= 40`.
* `name` (`string`, required) Length: `>= 1`.
* `iconUrl` (`string | null`, optional)
* `orgId` (`string`, required): A UUID
* `createdAt` (`string`, required)
* `protectedBranches` (`array<string>`, required): The patterns naming the protected branches of a workspace. A branch is protected when any pattern matches its whole name. Items: `<= 100`.

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

### `409`: SlugTaken

Media type: `application/json`

* `_tag` (`"SlugTaken"`, required)
* `message` (`string`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
