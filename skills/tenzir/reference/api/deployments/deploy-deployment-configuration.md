---
title: "Deploy deployment configuration"
description: "Makes the deployment run an immutable commit from the workspace repository."
canonical: https://tenzir.com/docs/reference/api/deployments/deploy-deployment-configuration
source: https://tenzir.com/docs/reference/api/deployments/deploy-deployment-configuration.md
section: "Docs"
---

# Deploy deployment configuration

> Makes the deployment run an immutable commit from the workspace repository.

`POST /api/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/configuration/deploy`

Makes the deployment run an immutable commit from the workspace repository. Refused as a conflict while automatic deployment is on: turn it off first, or change the tracker with a commit to do both at once. Refused as a conflict when the deployed generation is no longer expectedDeployedGeneration, unless the deployment has since accepted this commit. A commit whose files cannot become a configuration is refused as invalid. A connected deployment gets the configuration right away, and the answer waits for it to accept or reject it, for a while; one that is not connected gets it once it connects. Does not change Git history.

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

* `deploymentId` (`Id / Slug`, required): A deployment identified by its ID or slug within a workspace

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Request body (`application/json`, required)

* `commit` (`string`, required): A full lowercase SHA-1 commit ID
* `expectedDeployedGeneration` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

## Responses

### `200`: Success

Media type: `application/json`

* `generation` (`integer`, required) Range: `> 0, <= 9007199254740991`.
* `commit` (`string | null`, required): A full lowercase SHA-1 commit ID
* `digest` (`string`, required)
* `accepted` (`boolean`, required): Whether the deployment accepted it already. A deployment that is not connected receives it once it connects.

### `400`: InvalidDeploymentConfiguration | CredentialConflict | Validation

Media type: `application/json`

Any of:

* **InvalidDeploymentConfiguration** (`InvalidDeploymentConfiguration`)

  * `_tag` (`"InvalidDeploymentConfiguration"`, required)
  * `message` (`string`, required)

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

### `409`: DeploymentConfigurationConflict | UsageRestricted

Media type: `application/json`

Any of:

* **DeploymentConfigurationConflict** (`DeploymentConfigurationConflict`)

  * `_tag` (`"DeploymentConfigurationConflict"`, required)
  * `message` (`string`, required)

* **UsageRestricted** (`UsageRestricted`)

  * `_tag` (`"UsageRestricted"`, required)
  * `message` (`string`, required)
  * `resolution` (`string`, required)
  * `state` (`enum`, required): The state of a deployment, from least to most restricted. `locked`: its pipelines keep running, but no configuration change reaches it, which includes starting, stopping, pausing and deleting pipelines, no ad-hoc pipeline starts on it, and it cannot run as a larger type; deleting it and downsizing it still work. It ends on its own once usage is back within limits. `suspended`: what a locked deployment refuses, and it runs no pipelines, and a Tenzir-hosted one does not run at all. It ends only when the deployment is resumed, which the usage limit allows once usage is back within limits. Allowed values: `active`, `locked`, `suspended`.
  * `operation` (`enum`, required): What the state of a deployment admits or refuses on it: delivering a configuration to it, changing the branch it follows, starting an ad-hoc pipeline on it, creating it, running it as a larger type, and resuming it from a suspension. Allowed values: `deliverConfiguration`, `changeTracker`, `startAdhocPipeline`, `createDeployment`, `upsize`, `resume`.

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
