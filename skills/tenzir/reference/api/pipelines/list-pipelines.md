---
title: "List pipelines"
description: "GET /api/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/pipelines"
canonical: https://tenzir.com/docs/reference/api/pipelines/list-pipelines
source: https://tenzir.com/docs/reference/api/pipelines/list-pipelines.md
section: "Docs"
---

# List pipelines

> GET /api/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/pipelines

`GET /api/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/pipelines`

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

* `id` (`string`, required): An identifier that may be a path
* `name` (`string`, required)
* `definition` (`string`, required)
* `state` (`enum`, required) Allowed values: `running`, `stopping`, `finished`, `failed`, `stopped`.
* `run` (`integer`, required) Range: `>= -9007199254740991, <= 9007199254740991`.
* `error` (`string | null`, required)

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
