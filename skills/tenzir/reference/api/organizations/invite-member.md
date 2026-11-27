---
title: "Invite member"
description: "Creates an invited organization member with a label and returns its invitation secret once."
canonical: https://tenzir.com/docs/reference/api/organizations/invite-member
source: https://tenzir.com/docs/reference/api/organizations/invite-member.md
section: "Docs"
---

# Invite member

> Creates an invited organization member with a label and returns its invitation secret once.

`POST /api/organizations/{org}/invitations`

Creates an invited organization member with a label and returns its invitation secret once. Requires Organization.inviteMember. No email is sent; store the secret securely.

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Request body (`application/json`, required)

* `label` (`string`, required) Length: `>= 1`.

## Responses

### `201`: Success

Media type: `application/json`

* `orgId` (`string`, required): The id of the organization the invitation admits to, which its link names

* `memberId` (`string`, required): A stable membership identifier

* `invitation` (`Organization Invitation`, required): An invitation summary that does not expose its secret

  * `id` (`string`, required): The identifier of an organization invitation
  * `label` (`string`, required) Length: `>= 1`.
  * `createdBy` (`string<uuid>`, required): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

* `secret` (`string`, required)

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
