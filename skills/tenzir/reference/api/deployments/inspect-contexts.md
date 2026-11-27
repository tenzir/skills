---
title: "Inspect contexts"
description: "The contexts on a deployment, sorted by name."
canonical: https://tenzir.com/docs/reference/api/deployments/inspect-contexts
source: https://tenzir.com/docs/reference/api/deployments/inspect-contexts.md
section: "Docs"
---

# Inspect contexts

> The contexts on a deployment, sorted by name.

`GET /api/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/contexts`

The contexts on a deployment, sorted by name.

Authentication: `bearer` + `session` + `apiKey` + `key`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

* `workspace` (`Id / Slug`, required): A workspace identified by its ID or slug within an organization

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

* `deploymentId` (`Id / Slug`, required): A deployment identified by its ID or slug within a workspace

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Responses

### `200`: Success

Media type: `application/json`

Array items:

* `name` (`string`, required)
* `type` (`string`, required)
* `details` (`object`, required)

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

### `503`: ServiceUnavailable

Media type: `application/json`

* `_tag` (`"ServiceUnavailable"`, required)
