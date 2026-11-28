---
title: "Create ingest endpoint"
description: "Creates an ingest endpoint in an organization, with the Kafka topic its events go to, and answers its token."
canonical: https://tenzir.com/docs/reference/api/ingest-endpoints/create-ingest-endpoint
source: https://tenzir.com/docs/reference/api/ingest-endpoints/create-ingest-endpoint.md
section: "Docs"
---

# Create ingest endpoint

> Creates an ingest endpoint in an organization, with the Kafka topic its events go to, and answers its token.

`POST /api/organizations/{org}/ingest-endpoints`

Creates an ingest endpoint in an organization, with the Kafka topic its events go to, and answers its token. Without `readableBy`, every deployment of the organization may read it. Without `region`, it lives in the first ingest region of the platform configuration that the organization may use. Refused with UpgradeRequired when a Community organization has reached its limit of 1 ingest endpoint, with UsageRestricted (409) while the usage limit of the organization suspends what Tenzir hosts, ingest endpoints included, with why and how to resolve it, and with IngestEndpointNameTaken when the organization already has an endpoint of the name. 400 if a reader is not in the organization or cannot read in its region, or if the platform does not offer the region, or not to the organization: regions of AWS, such as `eu-central-1`, require Enterprise, as deployments there do. Requires Organization.createIngestEndpoint.

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Request body (`application/json`, required)

* `name` (`string`, required): The name pipelines refer to an ingest endpoint by, unique in its organization: lowercase letters, digits, and single dashes. Length: `>= 2, <= 21`.

* `description` (`string`, optional)

* `region` (`string`, optional): One of the ingest regions that the platform configuration lists; the first of them if left out

* `readableBy` (`"everyone" / object`, optional): Every deployment of the organization, or only the listed workspaces and deployments

  Any of:

  * **Option 1** (`"everyone"`)

  * **Option 2** (`object`)

    * `workspaces` (`array<string>`, optional)
    * `deployments` (`array<string>`, optional)

## Responses

### `201`: An endpoint and its new token

Media type: `application/json`

* `endpoint` (`Ingest Endpoint`, required): A URL that turns every request sent to it with its token into one event for pipelines on the deployments of its organization that may read it

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

* `token` (`string`, required)

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

### `402`: UpgradeRequired

Media type: `application/json`

* `_tag` (`"UpgradeRequired"`, required)
* `message` (`string`, required)

### `403`: Unauthorized

Media type: `application/json`

* `_tag` (`"Unauthorized"`, required)
* `message` (`string`, required)

### `404`: NotFound

Media type: `application/json`

* `_tag` (`"NotFound"`, required)

### `409`: IngestEndpointNameTaken | PaymentMethodRequired | UsageRestricted

Media type: `application/json`

Any of:

* **IngestEndpointNameTaken** (`IngestEndpointNameTaken`)

  * `_tag` (`"IngestEndpointNameTaken"`, required)
  * `message` (`string`, required)

* **PaymentMethodRequired** (`PaymentMethodRequired`)

  * `_tag` (`"PaymentMethodRequired"`, required)
  * `message` (`string`, required)

* **UsageRestricted** (`UsageRestricted`)

  * `_tag` (`"UsageRestricted"`, required)
  * `message` (`string`, required)
  * `resolution` (`string`, required)
  * `state` (`enum`, required): The state of a deployment, from least to most restricted. `locked`: its pipelines keep running, but no configuration change reaches it, which includes starting, stopping, pausing and deleting pipelines, no ad-hoc pipeline starts on it, and it cannot run as a larger type; deleting it and downsizing it still work. It ends on its own once usage is back within limits. `suspended`: what a locked deployment refuses, and it runs no pipelines, and a Tenzir-hosted one does not run at all. It ends only when the deployment is resumed, which the usage limit allows once usage is back within limits. Allowed values: `active`, `locked`, `suspended`.
  * `operation` (`enum`, required): What the state of a deployment or an ingest endpoint admits or refuses on it: delivering a configuration to it, changing the branch it follows, starting an ad-hoc pipeline on it, creating it, running it as a larger type, resuming it from a suspension, accepting events at an ingest endpoint, and creating one. Allowed values: `deliverConfiguration`, `changeTracker`, `startAdhocPipeline`, `createDeployment`, `upsize`, `resume`, `ingest`, `createIngestEndpoint`.

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)

### `503`: ServiceUnavailable

Media type: `application/json`

* `_tag` (`"ServiceUnavailable"`, required)
