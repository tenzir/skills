---
title: "Read logs"
description: "GET /api/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/logs"
canonical: https://tenzir.com/docs/reference/api/deployments/read-logs
source: https://tenzir.com/docs/reference/api/deployments/read-logs.md
section: "Docs"
---

# Read logs

> GET /api/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/logs

`GET /api/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/logs`

Authentication: `apiKey` + `bearer` + `session`.

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

## Query parameters

* `mode` (`enum`, required) Allowed values: `finite`, `follow`.
* `from` (`string`, optional)
* `to` (`string`, optional)
* `levels` (`string`, optional)
* `sources` (`string`, optional)
* `q` (`string`, optional) Length: `<= 4096`.
* `matchCase` (`enum`, optional) Allowed values: `true`, `false`.
* `limit` (`string`, optional)
* `beforeTime` (`string`, optional)
* `beforeBoot` (`string`, optional)
* `beforeSeq` (`string`, optional)

## Responses

### `200`: Success

Media type: `text/event-stream`

* `id` (`string | null`, optional)
* `event` (`string`, required)
* `data` (`string<json>`, required)

### `400`: InvalidLogQuery | CredentialConflict | Validation

Media type: `application/json`

Any of:

* **InvalidLogQuery** (`InvalidLogQuery`)

  * `_tag` (`"InvalidLogQuery"`, required)
  * `message` (`string`, required)

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
