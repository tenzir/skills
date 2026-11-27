---
title: "Create organization secret"
description: "Creates an organization secret, failing with a conflict when one of that name exists already"
canonical: https://tenzir.com/docs/reference/api/secrets/create-organization-secret
source: https://tenzir.com/docs/reference/api/secrets/create-organization-secret.md
section: "Docs"
---

# Create organization secret

> Creates an organization secret, failing with a conflict when one of that name exists already

`POST /api/organizations/{org}/secrets`

Creates an organization secret, failing with a conflict when one of that name exists already

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Request body (`application/json`, required)

* `name` (`unknown`, required): A path-safe identifier. Length: `<= 255`.

* `value` (`string`, optional) Length: `>= 1`.

* `readableBy` (`"everyone" / object`, optional)

  Any of:

  * **Option 1** (`"everyone"`)

  * **Option 2** (`object`)

    * `workspaces` (`array<string>`, optional)
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
