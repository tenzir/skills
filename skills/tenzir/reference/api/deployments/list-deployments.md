---
title: "List deployments"
description: "Lists the deployments of a workspace, naming the organization and the workspace by slug or by id."
canonical: https://tenzir.com/docs/reference/api/deployments/list-deployments
source: https://tenzir.com/docs/reference/api/deployments/list-deployments.md
section: "Docs"
---

# List deployments

> Lists the deployments of a workspace, naming the organization and the workspace by slug or by id.

`GET /api/organizations/{org}/workspaces/{workspace}/deployments`

Lists the deployments of a workspace, naming the organization and the workspace by slug or by id. Requires Workspace.listDeployments.

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

## Responses

### `200`: Success

Media type: `application/json`

Array items:

* `deployment` (`Deployment`, required)

  * `id` (`string`, required): A UUID
  * `workspaceId` (`string`, required): A UUID
  * `name` (`string`, required)
  * `slug` (`string`, required) Length: `<= 40`.
  * `version` (`string | null`, optional)
  * `lastSeen` (`string | null`, optional)

* `reachable` (`boolean`, required)

* `hosting` (`enum`, required): Who operates the deployment infrastructure: Tenzir or the customer. Allowed values: `tenzir`, `customer`.

* `size` (`enum | null`, optional): The machine type a hosted deployment runs as. Allowed values: `tiny`, `small`, `medium`, `large`, `xlarge`.

* `region` (`string | null`, optional): The cloud region of a deployment Tenzir runs

* `source` (`string | null`, optional): The source tag of the build the deployment ran when it last connected, such as `src-<hash>`. Absent for one whose build has none

* `runtime` (`enum | null`, optional): What runs a deployment, as it reported when it connected: Kubernetes, Amazon ECS, the Docker Compose project of the install command, another Docker container, a systemd service, or nothing it could tell. Allowed values: `kubernetes`, `ecs`, `compose`, `docker`, `systemd`, `unmanaged`.

* `update` (`Deployment Update | null`, optional): Whether a deployment runs an older build than the image the platform starts deployments on, hosted or not. A deployment on that image, or on a build after it, is current

  Any of:

  * **Option 1** (`object`)
    * `_tag` (`"Current"`, required)

  * **Option 2** (`object`)

    * `_tag` (`"Available"`, required)
    * `image` (`string`, required): The image the platform starts deployments on, which an update runs it on
    * `version` (`any`, required): The engine version of that image, as a deployment that runs it reports it, such as `7.0.0`

* `createdAt` (`string`, required)

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
