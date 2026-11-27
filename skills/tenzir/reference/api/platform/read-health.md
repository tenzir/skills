---
title: "Read health"
description: "Unauthenticated liveness probe, used by the dev topology and orchestrators."
canonical: https://tenzir.com/docs/reference/api/platform/read-health
source: https://tenzir.com/docs/reference/api/platform/read-health.md
section: "Docs"
---

# Read health

> Unauthenticated liveness probe, used by the dev topology and orchestrators.

`GET /api/health`

Unauthenticated liveness probe, used by the dev topology and orchestrators.

## Responses

### `200`: Success

Media type: `application/json`

* `status` (`string`, required)

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

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
