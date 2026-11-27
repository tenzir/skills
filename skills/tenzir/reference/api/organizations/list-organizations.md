---
title: "List organizations"
description: "Lists the organizations the given user is a member of"
canonical: https://tenzir.com/docs/reference/api/organizations/list-organizations
source: https://tenzir.com/docs/reference/api/organizations/list-organizations.md
section: "Docs"
---

# List organizations

> Lists the organizations the given user is a member of

`GET /api/users/{userId}/organizations`

Lists the organizations the given user is a member of

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `userId` (`string<uuid>`, required): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

## Responses

### `200`: Success

Media type: `application/json`

Array items:

* `id` (`string`, required): A UUID
* `slug` (`string`, required) Length: `<= 40`.
* `name` (`string`, required) Length: `>= 1`.
* `iconUrl` (`string | null`, optional)
* `createdAt` (`string`, required)
* `memberCount` (`integer`, required): How many members, including pending invitations, belong to the organization. Range: `>= 0, <= 9007199254740991`.
* `edition` (`enum`, required): The edition the organization is on, which decides what it can do, such as move to another slug. Allowed values: `community`, `enterprise`, `sovereign`, `provisioned`.

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
