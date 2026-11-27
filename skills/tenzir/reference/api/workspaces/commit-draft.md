---
title: "Commit draft"
description: "Publish the current user's latest saved draft to its branch."
canonical: https://tenzir.com/docs/reference/api/workspaces/commit-draft
source: https://tenzir.com/docs/reference/api/workspaces/commit-draft.md
section: "Docs"
---

# Commit draft

> Publish the current user's latest saved draft to its branch.

`POST /api/organizations/{org}/workspaces/{workspace}/users/{userId}/drafts/{branch}/commit`

Publish the current user's latest saved draft to its branch. With a `revision`, only that version of it: if the draft changed since, the commit is refused as a conflict.

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

* `revision` (`integer`, optional): The `revision` of the draft as it was reviewed. If the draft changed since, in another window or by another client, the commit is refused rather than publish what was not reviewed. Left out, the latest saved draft is published. Range: `>= -9007199254740991, <= 9007199254740991`.

## Responses

### `200`: Success

Media type: `application/json`

* `branch` (`string`, required): The branch the draft was published to
* `commit` (`string`, required): The commit that now tips the branch

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

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
