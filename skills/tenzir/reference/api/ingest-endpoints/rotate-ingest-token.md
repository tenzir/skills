---
title: "Rotate ingest token"
description: "Replaces the token of an ingest endpoint."
canonical: https://tenzir.com/docs/reference/api/ingest-endpoints/rotate-ingest-token
source: https://tenzir.com/docs/reference/api/ingest-endpoints/rotate-ingest-token.md
section: "Docs"
---

# Rotate ingest token

> Replaces the token of an ingest endpoint.

`POST /api/organizations/{org}/ingest-endpoints/{endpointId}/rotate-token`

Replaces the token of an ingest endpoint. The old token stops working within seconds. Buffered events stay. Reading the new token is a permission of its own. Requires IngestEndpoint.rotateToken.

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

* `endpointId` (`string`, required): A UUID

## Responses

### `200`: A URL that turns every request sent to it with its token into one event for pipelines on the deployments of its organization that may read it

Media type: `application/json`

* `id` (`string`, required): A UUID

* `orgId` (`string`, required): A UUID

* `name` (`string`, required): The name pipelines refer to an ingest endpoint by, unique in its organization: lowercase letters, digits, and single dashes. Length: `>= 2, <= 21`.

* `description` (`string`, required)

* `region` (`string`, required): The cloud region whose broker buffers the events, such as `europe-west3`. Only deployments that Tenzir hosts there may read the endpoint, unless the platform offers no ingest regions. It never changes

* `readableBy` (`"everyone" / Ingest Endpoint Readers`, required): Every deployment of the organization, or only the listed ones. Empty lists mean no deployment

  Any of:

  * **Option 1** (`"everyone"`)

  * **Ingest Endpoint Readers** (`Ingest Endpoint Readers`)

    * `workspaces` (`array<string>`, required)
    * `deployments` (`array<string>`, required)

* `url` (`string | null`, optional)

* `tokenPrefix` (`string`, required): The first characters of the current token

* `tokenIssuedAt` (`string`, required)

* `createdAt` (`string`, required)

* `createdBy` (`string<uuid>`, required): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

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
