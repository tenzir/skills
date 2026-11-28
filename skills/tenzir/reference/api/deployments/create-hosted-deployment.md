---
title: "Create hosted deployment"
description: "Registers a deployment in a workspace that the platform runs itself, and starts it."
canonical: https://tenzir.com/docs/reference/api/deployments/create-hosted-deployment
source: https://tenzir.com/docs/reference/api/deployments/create-hosted-deployment.md
section: "Docs"
---

# Create hosted deployment

> Registers a deployment in a workspace that the platform runs itself, and starts it.

`POST /api/organizations/{org}/workspaces/{workspace}/hosted-deployments`

Registers a deployment in a workspace that the platform runs itself, and starts it. It connects on its own, without an install. Refused when the platform hosts no deployments or no more of them, for a type not on offer for the organization (such as Large or X-Large on Community), for a cloud or region not on offer (such as AWS on Community), when the organization is restricted by a usage limit (including the Community hosted internet egress guardrail), for an image the registry does not have, and for a slug that another deployment in the workspace has or that the name cannot provide. Requires Workspace.createHostedDeployment.

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

* `workspace` (`Id / Slug`, required): A workspace identified by its ID or slug within an organization

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Request body (`application/json`, required)

* `name` (`string`, required) Length: `>= 1`.
* `slug` (`string`, optional) Length: `<= 40`.
* `branch` (`string | null`, optional)
* `autoDeploy` (`boolean | null`, optional): Whether to deploy Git changes automatically; defaults to true
* `image` (`string`, optional): A tenzir/tenzir image the deployment runs instead of the one the platform hosts deployments with
* `size` (`enum`, optional): The type it runs as, one of those `listDeploymentTypes` offers; its default if not given, `medium` where that is on offer. Allowed values: `tiny`, `small`, `medium`, `large`, `xlarge`.
* `cloud` (`enum`, optional): The cloud it runs in, one of the clouds of the locations `listDeploymentTypes` offers; that of `region` if not given, or else that of the first location. Allowed values: `gcp`, `aws`.
* `region` (`string`, optional): The region of the cloud it runs in, such as `europe-west3` on Google Cloud or `eu-central-1` on AWS, one of the locations `listDeploymentTypes` offers; the first of `cloud` if not given

## Responses

### `201`: Tenzir.Deployment.Deployment

Media type: `application/json`

* `id` (`string`, required): A UUID
* `workspaceId` (`string`, required): A UUID
* `name` (`string`, required)
* `slug` (`string`, required) Length: `<= 40`.
* `version` (`string | null`, optional)
* `lastSeen` (`string | null`, optional)

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

### `409`: HostedDeploymentRefused | SlugTaken | PaymentMethodRequired | UsageRestricted

Media type: `application/json`

Any of:

* **HostedDeploymentRefused** (`HostedDeploymentRefused`)

  * `_tag` (`"HostedDeploymentRefused"`, required)
  * `message` (`string`, required)

* **SlugTaken** (`SlugTaken`)

  * `_tag` (`"SlugTaken"`, required)
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

### `422`: ImageUnavailable

Media type: `application/json`

* `_tag` (`"ImageUnavailable"`, required)
* `message` (`string`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
