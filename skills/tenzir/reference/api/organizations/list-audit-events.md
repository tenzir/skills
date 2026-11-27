---
title: "List audit events"
description: "A page of an organization's audit log, most recent first, filtered by an optional search over actor, action and resource"
canonical: https://tenzir.com/docs/reference/api/organizations/list-audit-events
source: https://tenzir.com/docs/reference/api/organizations/list-audit-events.md
section: "Docs"
---

# List audit events

> A page of an organization's audit log, most recent first, filtered by an optional search over actor, action and resource

`GET /api/organizations/{org}/audit`

A page of an organization's audit log, most recent first, filtered by an optional search over actor, action and resource

Authentication: `bearer` + `session`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Query parameters

* `search` (`string`, optional)
* `limit` (`string`, optional)
* `offset` (`string`, optional)
* `order` (`enum`, optional): Which events of the audit log come first. Allowed values: `newest`, `oldest`.

## Responses

### `200`: Tenzir.Audit.Page

Media type: `application/json`

* `events` (`array<Event>`, required)

  Array items:

  * `id` (`string`, required): A UUID

  * `timestamp` (`string`, required)

  * `action` (`string`, required)

  * `outcome` (`enum`, required) Allowed values: `success`, `failed`.

  * `resource` (`object`, required)

    Any of:

    * **Option 1** (`object`)

      * `_tag` (`"Some"`, required)
      * `value` (`string`, required)

    * **Option 2** (`object`)
      * `_tag` (`"None"`, required)

  * `org` (`object`, required)

    Any of:

    * **Option 1** (`object`)

      * `_tag` (`"Some"`, required)
      * `value` (`string`, required): A UUID

    * **Option 2** (`object`)
      * `_tag` (`"None"`, required)

  * `actor` (`Actor`, required)

    Any of:

    * **UserActor** (`UserActor`)

      * `_tag` (`"UserActor"`, required)

      * `id` (`string<uuid>`, required): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

      * `label` (`object`, required)

        Any of:

        * **Option 1** (`object`)

          * `_tag` (`"Some"`, required)
          * `value` (`string`, required)

        * **Option 2** (`object`)
          * `_tag` (`"None"`, required)

      * `name` (`string | null`, optional)

    * **DeploymentActor** (`DeploymentActor`)

      * `_tag` (`"DeploymentActor"`, required)
      * `id` (`string`, required): A UUID
      * `label` (`string`, required)

    * **AnonymousActor** (`AnonymousActor`)
      * `_tag` (`"AnonymousActor"`, required)

    * **PlatformActor** (`PlatformActor`)
      * `_tag` (`"PlatformActor"`, required)

  * `request` (`Request`, required)

    * `id` (`string`, required)

    * `userAgent` (`object`, required)

      Any of:

      * **Option 1** (`object`)

        * `_tag` (`"Some"`, required)
        * `value` (`string`, required)

      * **Option 2** (`object`)
        * `_tag` (`"None"`, required)

    * `ip` (`object`, required)

      Any of:

      * **Option 1** (`object`)

        * `_tag` (`"Some"`, required)
        * `value` (`string`, required)

      * **Option 2** (`object`)
        * `_tag` (`"None"`, required)

* `total` (`number / enum`, required)

  Any of:

  * **Option 1** (`number`)
  * **Option 2** (`enum`)

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
