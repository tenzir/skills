---
title: "List deployment secrets"
description: "Lists every secret a deployment may read, from its organization, its workspace and itself, and which of them a closer one with the same name shadows."
canonical: https://tenzir.com/docs/reference/api/secrets/list-deployment-secrets
source: https://tenzir.com/docs/reference/api/secrets/list-deployment-secrets.md
section: "Docs"
---

# List deployment secrets

> Lists every secret a deployment may read, from its organization, its workspace and itself, and which of them a closer one with the same name shadows.

`GET /api/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/secrets`

Lists every secret a deployment may read, from its organization, its workspace and itself, and which of them a closer one with the same name shadows. Values never come back

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

* `deploymentId` (`Id / Slug`, required): A deployment identified by its ID or slug within a workspace

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Responses

### `200`: Success

Media type: `application/json`

Array items:

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

* `shadowedBy` (`Organization Secret Owner / Workspace Secret Owner / Deployment Secret Owner | null`, optional): The organization, workspace, or deployment that holds the secret

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
