---
title: "Add draft package"
description: "Add a package to the current user's draft on a branch, or change which versions of it the draft accepts."
canonical: https://tenzir.com/docs/reference/api/workspaces/add-draft-package
source: https://tenzir.com/docs/reference/api/workspaces/add-draft-package.md
section: "Docs"
---

# Add draft package

> Add a package to the current user's draft on a branch, or change which versions of it the draft accepts.

`POST /api/organizations/{org}/workspaces/{workspace}/users/{userId}/drafts/{branch}/packages`

Add a package to the current user's draft on a branch, or change which versions of it the draft accepts. Without a requirement, it accepts the newest release and those after it that promise to stay compatible, and a package the draft uses already is refused. The change is resolved against the package repositories, and the package.yaml and package.lock it leaves are saved into the draft, started if there is none. Changes to one draft run one at a time, each from what the one before left. Nothing is committed. Requires WorkspaceBranch.changeDraftPackages

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

* `userId` (`string<uuid>`, required): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

* `branch` (`string`, required)

## Request body (`application/json`, required)

* `id` (`string`, required)
* `requirement` (`string | null`, optional)

## Responses

### `200`: Personal server-side configuration changes, not yet published.

Media type: `application/json`

* `workspaceId` (`string`, required): A UUID
* `ownerId` (`string<uuid>`, required): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.
* `branch` (`string`, required)
* `headSha` (`string`, required): A full lowercase SHA-1 commit ID
* `revision` (`integer`, required): Grows with every write to any draft, so of two versions of a draft, even across one committed or discarded and started anew, the one with the higher revision is newer. Range: `>= -9007199254740991, <= 9007199254740991`.
* `message` (`string | null`, optional)
* `status` (`enum`, required) Allowed values: `ready`, `conflicting`.
* `conflictingPaths` (`array<string>`, required)
* `createdAt` (`string`, required)
* `updatedAt` (`string`, required)

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

### `409`: DraftConflict

Media type: `application/json`

* `_tag` (`"DraftConflict"`, required)
* `message` (`string`, required)

### `422`: PackageProblem

Media type: `application/json`

* `_tag` (`"PackageProblem"`, required)
* `message` (`string`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
