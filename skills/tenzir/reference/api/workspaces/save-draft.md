---
title: "Save draft"
description: "Save changes made to a version of the current user's draft on a branch, rebased onto the branch tip."
canonical: https://tenzir.com/docs/reference/api/workspaces/save-draft
source: https://tenzir.com/docs/reference/api/workspaces/save-draft.md
section: "Docs"
---

# Save draft

> Save changes made to a version of the current user's draft on a branch, rebased onto the branch tip.

`POST /api/organizations/{org}/workspaces/{workspace}/users/{userId}/drafts/{branch}/save`

Save changes made to a version of the current user's draft on a branch, rebased onto the branch tip. If the draft changed since that version, the changes merge into it: a file only they changed takes them, and where both changed the same or neighbouring lines, both stand between conflict markers, as `git merge-file` merges and writes them. If the draft is gone, they start a new one.

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

* `headSha` (`string`, required): The `headSha` of the draft as read before editing: the snapshot the changes were made against

* `message` (`string`, optional): The commit message to propose for the draft. Left out, the draft keeps the message it has

* `editedMessage` (`string | null`, optional): The message the draft had when it was read, or null for none. A save from a snapshot the draft has moved past then keeps a message changed meanwhile, unless `message` differs from this. Left out, it is taken from the commit of `headSha`

* `changes` (`array<Configuration file change>`, required): The edits: `put` creates or replaces a text file, `delete` removes one. Paths are relative to the repository root. A rename is a `delete` and a `put`

  Array items:

  Any of:

  * **Option 1** (`object`)

    * `type` (`"put"`, required)
    * `path` (`string`, required) Length: `>= 1`.
    * `text` (`string`, required)

  * **Option 2** (`object`)

    * `type` (`"delete"`, required)
    * `path` (`string`, required) Length: `>= 1`.

## Responses

### `200`: Success

Media type: `application/json`

* `draft` (`Configuration draft`, required): Personal server-side configuration changes, not yet published.

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

* `merged` (`boolean`, required): Whether the draft held changes the edited version did not: the changes were merged into them, so files may differ from what was sent.

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
