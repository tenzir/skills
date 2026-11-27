---
title: "Ask conversation"
description: "Asks a conversation a question, or answers its client-side tool calls, and streams the answer."
canonical: https://tenzir.com/docs/reference/api/assistant/ask-conversation
source: https://tenzir.com/docs/reference/api/assistant/ask-conversation.md
section: "Docs"
---

# Ask conversation

> Asks a conversation a question, or answers its client-side tool calls, and streams the answer.

`POST /api/users/{userId}/assistant-conversations/{conversationId}/ask`

Asks a conversation a question, or answers its client-side tool calls, and streams the answer. Pass the current `turn` of the conversation.

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `userId` (`string<uuid>`, required): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.
* `conversationId` (`string<uuid>`, required): A UUID that the client chooses when it creates the conversation. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

## Request body (`application/json`, required)

* `turn` (`integer`, required): The number of questions and tool results the conversation has received. Asking a conversation requires its current turn. Range: `>= 0, <= 9007199254740991`.

* `view` (`View`, optional): What the caller is looking at while asking

  * `path` (`string`, required): The full browser pathname, including context but excluding queries and fragments

  * `workspace` (`string`, optional): A UUID

  * `deployment` (`string`, optional): A UUID

  * `pipeline` (`string`, optional)

  * `navigation` (`object`, optional)

    * `org` (`string`, required) Length: `<= 40`.
    * `workspace` (`string`, optional) Length: `<= 40`.
    * `deployment` (`string`, optional) Length: `<= 40`.

* `clientTools` (`array<enum>`, required)

* `input` (`Assistant Conversation Question / Assistant Conversation Tool Results`, required): What to ask a conversation: a question or tool results

  Any of:

  * **Assistant Conversation Question** (`Assistant Conversation Question`)

    * `_tag` (`"Question"`, required)
    * `text` (`string`, required): A non-empty question of at most 20,000 UTF-16 code units. Length: `>= 1, <= 20000`.

  * **Assistant Conversation Tool Results** (`Assistant Conversation Tool Results`)

    * `_tag` (`"ToolResults"`, required)

    * `results` (`array<Assistant Conversation Tool Result>`, required)

      Array items:

      * `id` (`string`, required) Length: `>= 1`.
      * `isFailure` (`boolean`, required)
      * `result` (`unknown`, required)

## Responses

### `200`: Success

Media type: `text/event-stream`

* `id` (`string | null`, optional)
* `event` (`string`, required)
* `data` (`string<json>`, required)

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

### `409`: TurnConflict

Media type: `application/json`

* `_tag` (`"TurnConflict"`, required)
* `message` (`string`, required)
* `turn` (`integer`, required): The number of questions and tool results the conversation has received. Asking a conversation requires its current turn. Range: `>= 0, <= 9007199254740991`.

### `413`: ConversationTooLarge

Media type: `application/json`

* `_tag` (`"ConversationTooLarge"`, required)
* `message` (`string`, required)
* `limit` (`integer`, required) Range: `>= -9007199254740991, <= 9007199254740991`.

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)

### `502`: AssistantFailed

Media type: `application/json`

* `_tag` (`"AssistantFailed"`, required)
* `message` (`string`, required)
