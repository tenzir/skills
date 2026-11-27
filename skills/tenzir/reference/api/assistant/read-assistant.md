---
title: "Read assistant"
description: "Whether the assistant is available on this platform."
canonical: https://tenzir.com/docs/reference/api/assistant/read-assistant
source: https://tenzir.com/docs/reference/api/assistant/read-assistant.md
section: "Docs"
---

# Read assistant

> Whether the assistant is available on this platform.

`GET /api/assistant`

Whether the assistant is available on this platform.

Authentication: `bearer` + `session` + `apiKey`.

## Responses

### `200`: Whether this platform has the assistant switched on

Media type: `application/json`

* `enabled` (`boolean`, required)

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

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
