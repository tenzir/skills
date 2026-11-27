---
title: "Read usage state"
description: "Where an organization stands against its usage limit, and the state of each of its deployments: active, locked or suspended."
canonical: https://tenzir.com/docs/reference/api/billing/read-usage-state
source: https://tenzir.com/docs/reference/api/billing/read-usage-state.md
section: "Docs"
---

# Read usage state

> Where an organization stands against its usage limit, and the state of each of its deployments: active, locked or suspended.

`GET /api/organizations/{org}/usage/state`

Where an organization stands against its usage limit, and the state of each of its deployments: active, locked or suspended. On Community, running out of credits or exceeding the hosted internet egress guardrail (`credits.hostedEgressExceeded`) suspends Tenzir-hosted deployments immediately, while self-hosted deployments keep running within the daily UTC allowance and suspend beyond it until 00:00 UTC (`resumableAt`). On Enterprise with a budget, reaching it suspends Tenzir-hosted deployments and makes self-hosted ones locked once the grace of the plan, by default 24 hours and 7 days, has passed since it was first reached in the billing period. A suspended deployment stays suspended until it is resumed. It has no amounts. Requires Organization.readUsageState

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Responses

### `200`: What the usage limit of an organization means for it now, and the state of each of its deployments, from how far its limit was used when last evaluated, with the terms of its plan that explain it. It has no amounts, so every member can read it

Media type: `application/json`

* `asOf` (`string`, required)

* `limit` (`enum`, required): What limits the usage: nothing, the credits and daily self-hosted allowance of Community, or the monthly budget of Enterprise. Allowed values: `none`, `credits`, `budget`.

* `state` (`enum`, required): The state of its limit, or of its most restricted deployment if that is more restricted: for display, never for enforcement. Allowed values: `ok`, `warning`, `exceeded`, `locked`, `suspended`.

* `budgetExceededAt` (`string | null`, required)

* `deadlines` (`Usage Deadlines`, required): When grace ends for each kind of hosting the organization has. They stay after a recovery until the billing period ends: reaching the budget again in the period keeps them. Past ones are included

  * `tenzirHostedSuspendAt` (`string | null`, required)
  * `selfHostedLockedAt` (`string | null`, required)

* `warningPercent` (`integer | null`, required) Range: `>= -9007199254740991, <= 9007199254740991`.

* `budgetGraceSeconds` (`object | null`, required)

  * `tenzir` (`integer`, required) Range: `>= -9007199254740991, <= 9007199254740991`.
  * `customer` (`integer`, required) Range: `>= -9007199254740991, <= 9007199254740991`.

* `credits` (`Community Credit Status | null`, required): Where a Community organization stands on credits and its daily self-hosted allowance, without credit amounts or byte totals

  * `exhausted` (`boolean`, required): Whether active credits are exhausted (zero remaining). When true, Tenzir-hosted deployments are suspended and self-hosted deployments stop once they exceed the daily allowance
  * `low` (`boolean`, required): Whether few active credits remain (at or beyond the plan credit warning share)
  * `expiresAt` (`string | null`, required)
  * `allowanceWarning` (`boolean`, required): Whether today’s self-hosted ingress is approaching the daily allowance while no credits remain
  * `allowanceExceeded` (`boolean`, required): Whether today’s self-hosted ingress has reached the daily allowance while no credits remain
  * `hostedEgressExceeded` (`boolean`, optional)

* `resumableAt` (`string | null`, required)

* `deployments` (`array<Deployment Usage State>`, required)

  Array items:

  * `deploymentId` (`string`, required): A UUID
  * `workspaceId` (`string`, required): The workspace the deployment belongs to, which the API names it under
  * `hosting` (`enum`, required): Who operates the deployment infrastructure: Tenzir or the customer. Allowed values: `tenzir`, `customer`.
  * `size` (`enum | null`, optional): The machine type a hosted deployment runs as. Allowed values: `tiny`, `small`, `medium`, `large`, `xlarge`.
  * `state` (`enum`, required): The state of a deployment, from least to most restricted. `locked`: its pipelines keep running, but no configuration change reaches it, which includes starting, stopping, pausing and deleting pipelines, no ad-hoc pipeline starts on it, and it cannot run as a larger type; deleting it and downsizing it still work. It ends on its own once usage is back within limits. `suspended`: what a locked deployment refuses, and it runs no pipelines, and a Tenzir-hosted one does not run at all. It ends only when the deployment is resumed, which the usage limit allows once usage is back within limits. Allowed values: `active`, `locked`, `suspended`.
  * `resumable` (`boolean`, required): Whether the deployment is suspended and the usage limit allows resuming it now. Nothing resumes on its own
  * `resuming` (`boolean`, required): Whether resuming the suspended deployment was asked for and is under way: a Tenzir-hosted one starts again, and resumes once it connects

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
