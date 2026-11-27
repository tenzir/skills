---
title: "Create conversation"
description: "Creates an empty conversation with the given ID, unless the platform has no assistant."
canonical: https://tenzir.com/docs/reference/api/assistant/create-conversation
source: https://tenzir.com/docs/reference/api/assistant/create-conversation.md
section: "Docs"
---

# Create conversation

> Creates an empty conversation with the given ID, unless the platform has no assistant.

`POST /api/users/{userId}/assistant-conversations`

Creates an empty conversation with the given ID, unless the platform has no assistant. Repeating the request returns the existing conversation.

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `userId` (`string<uuid>`, required): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

## Request body (`application/json`, required)

* `id` (`string<uuid>`, required): A UUID that the client chooses when it creates the conversation. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

## Responses

### `200`: A conversation in a list

Media type: `application/json`

* `id` (`string<uuid>`, required): A UUID that the client chooses when it creates the conversation. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.
* `title` (`string`, required) Length: `>= 1`.
* `turn` (`integer`, required): The number of questions and tool results the conversation has received. Asking a conversation requires its current turn. Range: `>= 0, <= 9007199254740991`.
* `createdAt` (`string`, required)
* `updatedAt` (`string`, required)

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

### `404`: NotFound | AssistantDisabled

Media type: `application/json`

Any of:

* **NotFound** (`NotFound`)
  * `_tag` (`"NotFound"`, required)

* **AssistantDisabled** (`AssistantDisabled`)

  * `_tag` (`"AssistantDisabled"`, required)
  * `message` (`string`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
