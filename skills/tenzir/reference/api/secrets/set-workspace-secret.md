---
title: "Set workspace secret"
description: "Creates a secret in a workspace, or replaces its value."
canonical: https://tenzir.com/docs/reference/api/secrets/set-workspace-secret
source: https://tenzir.com/docs/reference/api/secrets/set-workspace-secret.md
section: "Docs"
---

# Set workspace secret

> Creates a secret in a workspace, or replaces its value.

`POST /api/organizations/{org}/workspaces/{workspace}/secrets/{name}/set`

Creates a secret in a workspace, or replaces its value. Nothing reads the value back but the deployments of the workspace that `readableBy` allows

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

* `name` (`unknown`, required): A path-safe identifier. Length: `<= 255`.

## Request body (`application/json`, required)

* `value` (`string`, optional) Length: `>= 1`.

* `readableBy` (`"everyone" / Readers`, optional)

  Any of:

  * **Option 1** (`"everyone"`)
  * **Readers** (`Readers`)
    * `deployments` (`array<string>`, optional)

## Responses

### `200`: What the platform tells a user about a secret. The value is never part of it: only a deployment the secret reaches can resolve that

Media type: `application/json`

* `id` (`string`, required): A UUID

* `name` (`unknown`, required): A path-safe identifier. Length: `<= 255`.

* `owner` (`Organization Secret Owner / Workspace Secret Owner / Deployment Secret Owner`, required): The organization, workspace, or deployment that holds the secret

  Any of:

  * **Organization Secret Owner** (`Organization Secret Owner`)

    * `_tag` (`"Organization"`, required)
    * `orgId` (`string`, required): A UUID

  * **Workspace Secret Owner** (`Workspace Secret Owner`)

    * `_tag` (`"Workspace"`, required)
    * `orgId` (`string`, required): A UUID
    * `workspaceId` (`string`, required): A UUID

  * **Deployment Secret Owner** (`Deployment Secret Owner`)

    * `_tag` (`"Deployment"`, required)
    * `orgId` (`string`, required): A UUID
    * `workspaceId` (`string`, required): A UUID
    * `deploymentId` (`string`, required): A UUID

* `readableBy` (`"everyone" / Secret Readers`, required): Every deployment the owner reaches, or only the listed ones. Empty lists mean no deployment

  Any of:

  * **Option 1** (`"everyone"`)

  * **Secret Readers** (`Secret Readers`)

    * `workspaces` (`array<string>`, required)
    * `deployments` (`array<string>`, required)

* `version` (`integer`, required) Range: `>= -9007199254740991, <= 9007199254740991`.

* `updatedBy` (`string`, required)

* `createdAt` (`string`, required)

* `updatedAt` (`string`, required)

* `lastAccessedAt` (`string | null`, optional)

### `400`: Validation | CredentialConflict

Media type: `application/json`

Any of:

* **Validation** (`Validation`)

  * `_tag` (`"Validation"`, required)
  * `message` (`string`, required)

* **CredentialConflict** (`CredentialConflict`)

  * `_tag` (`"CredentialConflict"`, required)
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

### `409`: SecretChanged | SecretNameConflict

Media type: `application/json`

Any of:

* **SecretChanged** (`SecretChanged`)

  * `_tag` (`"SecretChanged"`, required)
  * `message` (`string`, required)

* **SecretNameConflict** (`SecretNameConflict`)

  * `_tag` (`"SecretNameConflict"`, required)
  * `message` (`string`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
