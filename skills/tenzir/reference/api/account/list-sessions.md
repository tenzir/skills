---
title: "List sessions"
description: "The target user’s browser sessions and CLI logins, the most recently used first."
canonical: https://tenzir.com/docs/reference/api/account/list-sessions
source: https://tenzir.com/docs/reference/api/account/list-sessions.md
section: "Docs"
---

# List sessions

> The target user’s browser sessions and CLI logins, the most recently used first.

`GET /api/users/{userId}/sessions`

The target user’s browser sessions and CLI logins, the most recently used first. The session asking is marked as current. Requires User.listSessions.

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `userId` (`string<uuid>`, required): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

## Responses

### `200`: Success

Media type: `application/json`

Array items:

* `id` (`string<uuid>`, required): Names a session to its user. It is not the session cookie, and does not let anyone use the session. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.
* `kind` (`enum`, required): Whether a browser signed in, or a terminal through a CLI login. A CLI login is always a user session, even when an agent drives the CLI. Allowed values: `browser`, `cli`.
* `userAgent` (`string | null`, optional)
* `ip` (`string | null`, optional)
* `createdAt` (`string`, required)
* `lastUsedAt` (`string | null`, optional)
* `current` (`boolean`, required)

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
