---
title: "Read cost"
description: "What the usage of an organization uses in the current billing period: on Community, today’s daily self-hosted allowance, credit balance, grants, and credit consumption by category and day (never invoiced, no PAYG); on Enterprise, credits an"
canonical: https://tenzir.com/docs/reference/api/billing/read-cost
source: https://tenzir.com/docs/reference/api/billing/read-cost.md
section: "Docs"
---

# Read cost

> What the usage of an organization uses in the current billing period: on Community, today’s daily self-hosted allowance, credit balance, grants, and credit consumption by category and day (never invoiced, no PAYG); on Enterprise, credits an

`GET /api/organizations/{org}/billing/cost`

What the usage of an organization uses in the current billing period: on Community, today’s daily self-hosted allowance, credit balance, grants, and credit consumption by category and day (never invoiced, no PAYG); on Enterprise, credits and PAYG by category, the cost to date, the estimated invoice, each credit grant’s balance, the projection at the current rate, and each day of the period and the last 30 days. Days the usage ledger has not closed are estimates from telemetry. Requires Organization.readCost

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Responses

### `200`: What the usage of an organization uses in the current period: credits and the daily self-hosted allowance on Community, or credits, PAYG, and the estimated invoice on Enterprise

Media type: `application/json`

Any of:

* **Community Credit Usage** (`Community Credit Usage`)

  * `edition` (`"community"`, required)

  * `asOf` (`string`, required)

  * `planId` (`string`, required): The Community plan that priced it

  * `period` (`object`, required): The UTC calendar month, half-open

    * `start` (`string`, required)
    * `end` (`string`, required)

  * `closedThrough` (`string | null`, required)

  * `allowance` (`Daily Self-Hosted Allowance`, required): Where today’s self-hosted ingress stands against the Community daily allowance

    * `day` (`string`, required)
    * `usedBytes` (`string`, required) Pattern: `^-?\d+$`.
    * `allowanceBytes` (`string`, required) Pattern: `^-?\d+$`.
    * `warningPercent` (`integer`, required): Share of the daily allowance that warns when no credits remain, in percent. Range: `>= -9007199254740991, <= 9007199254740991`.
    * `resetsAt` (`string`, required)

  * `credits` (`object`, required): The credits used in the period so far

    * `ingest` (`object`, required)

      * `tenzir` (`string`, required)
      * `customer` (`string`, required)

    * `infrastructure` (`string`, required)

    * `total` (`string`, required)

    * `fromGrants` (`string`, required)

    * `uncovered` (`string`, required)

  * `availableCredits` (`string`, required)

  * `creditWarningPercent` (`integer`, required): The share of active granted credits used at which the organization is warned that few credits remain, in percent. Range: `>= -9007199254740991, <= 9007199254740991`.

  * `grantExpiryWarningDays` (`integer`, required): How many days before the last active grant expires to warn. Range: `>= -9007199254740991, <= 9007199254740991`.

  * `nextExpiryAt` (`string | null`, required)

  * `projection` (`Community Credit Projection`, required): When active Community credits run out at the current burn rate

    * `creditsPerHour` (`string`, required)
    * `creditsExhaustedAt` (`string | null`, required)

  * `grants` (`array<Credit Grant Summary>`, required): Every credit grant, with what is left of it now

    Array items:

    * `grant` (`CreditGrant`, required)

      * `id` (`string`, required): A UUID
      * `orgId` (`string`, required): A UUID
      * `source` (`enum`, required): Where the credits of a grant came from: a purchase, or the free credits a new user gets once. Allowed values: `purchase`, `signup`.
      * `quantity` (`integer`, required) Range: `> 0, <= 9007199254740991`.
      * `amountPaid` (`integer`, required): What was paid for all of it; effective cost divides by quantity. Range: `>= 0, <= 9007199254740991`.
      * `currency` (`string`, required): An ISO 4217 code. A plan offers the currencies it has prices for, and nothing converts between them
      * `effectiveAt` (`string`, required)
      * `expiresAt` (`string`, required)
      * `createdAt` (`string`, required)

    * `remaining` (`string`, required)

    * `status` (`enum`, required): Derived from the dates and what is left, never stored. Allowed values: `active`, `upcoming`, `used`, `expired`.

  * `days` (`array<Community Day Usage>`, required): Every day from the earlier of the period start and 29 days ago through today, oldest first

    Array items:

    * `day` (`string`, required)

    * `closed` (`boolean`, required): Whether the usage ledger recorded the day, which is then final. Otherwise it is an estimate from telemetry that can still grow

    * `selfHostedBytes` (`string`, required) Pattern: `^-?\d+$`.

    * `allowanceUsedBytes` (`string`, required) Pattern: `^-?\d+$`.

    * `credits` (`string`, required)

    * `rows` (`array<Community Ingress Row / Community Runtime Row>`, required)

      Array items:

      Any of:

      * **Community Ingress Row** (`Community Ingress Row`)

        * `_tag` (`"Ingress"`, required)
        * `deploymentId` (`string`, required): A UUID
        * `workspaceId` (`string`, required): A UUID
        * `credits` (`string`, required)
        * `hosting` (`enum`, required): Who operates the deployment infrastructure: Tenzir or the customer. Allowed values: `tenzir`, `customer`.
        * `bytes` (`string`, required) Pattern: `^-?\d+$`.

      * **Community Runtime Row** (`Community Runtime Row`)

        * `_tag` (`"Runtime"`, required)
        * `deploymentId` (`string`, required): A UUID
        * `workspaceId` (`string`, required): A UUID
        * `credits` (`string`, required)
        * `size` (`enum`, required): The machine type a hosted deployment runs as. Allowed values: `tiny`, `small`, `medium`, `large`, `xlarge`.
        * `seconds` (`integer`, required): How long it ran as the type that day, in whole seconds. Range: `>= 0, <= 86400`.

* **Enterprise Cost** (`Enterprise Cost`)

  * `edition` (`"enterprise"`, required)

  * `asOf` (`string`, required)

  * `planId` (`string`, required): The plan that priced it

  * `currency` (`string`, required): An ISO 4217 code. A plan offers the currencies it has prices for, and nothing converts between them

  * `period` (`object`, required): The billing period, the UTC calendar month, half-open

    * `start` (`string`, required)
    * `end` (`string`, required)

  * `closedThrough` (`string | null`, required)

  * `listPrice` (`integer`, required): One credit at list price, which PAYG pays, in the smallest unit like every price of the plan. Range: `>= -9007199254740991, <= 9007199254740991`.

  * `platformFee` (`integer`, required): The monthly platform fee, paid in money, in the smallest unit like every price of the plan. Range: `>= -9007199254740991, <= 9007199254740991`.

  * `credits` (`object`, required): The credits used in the period so far

    * `ingest` (`object`, required)

      * `tenzir` (`string`, required)
      * `customer` (`string`, required)

    * `infrastructure` (`string`, required)

    * `total` (`string`, required)

    * `fromGrants` (`string`, required)

    * `payg` (`string`, required)

  * `payg` (`object`, required): PAYG so far, which the budget compares against: no platform fee, taxes or credit purchases. It is split by each category’s share of the credits used, since credits are fungible; the parts are rounded, so they may differ from the total in the last place

    * `ingest` (`object`, required)

      * `tenzir` (`string`, required)
      * `customer` (`string`, required)

    * `infrastructure` (`string`, required)

    * `total` (`string`, required)

  * `costToDate` (`string`, required)

  * `effectiveCost` (`string`, required)

  * `invoice` (`array<Invoice Line>`, required): The estimated invoice of the period, before taxes; its lines add up to the cost to date

    Array items:

    * `item` (`enum`, required) Allowed values: `platformFee`, `payg`.
    * `quantity` (`string`, required)
    * `unitPrice` (`string`, required)
    * `amount` (`string`, required)

  * `monthlyBudget` (`integer | null`, required): A threshold on the PAYG ingest and infrastructure spend of a billing month, in the smallest unit of the organization currency, such as cents: 150000 is 1,500. Only whole units of the currency, such as whole dollars, make a budget. It excludes the platform fee, taxes and credit purchases. It warns and enforces, but never caps the invoice. Range: `> 0, <= 9007199254740991`.

  * `budgetWarningPercent` (`integer`, required): The share of the budget at which the organization is warned, in percent, from the plan's terms. Range: `>= -9007199254740991, <= 9007199254740991`.

  * `projection` (`Cost Projection`, required): Where the billing period ends up at the current rate

    * `creditsPerHour` (`string`, required)
    * `payg` (`string`, required)
    * `budgetReachedAt` (`string | null`, required)

  * `grants` (`array<Credit Grant Summary>`, required): Every credit grant, with what is left of it now

    Array items:

    * `grant` (`CreditGrant`, required)

      * `id` (`string`, required): A UUID
      * `orgId` (`string`, required): A UUID
      * `source` (`enum`, required): Where the credits of a grant came from: a purchase, or the free credits a new user gets once. Allowed values: `purchase`, `signup`.
      * `quantity` (`integer`, required) Range: `> 0, <= 9007199254740991`.
      * `amountPaid` (`integer`, required): What was paid for all of it; effective cost divides by quantity. Range: `>= 0, <= 9007199254740991`.
      * `currency` (`string`, required): An ISO 4217 code. A plan offers the currencies it has prices for, and nothing converts between them
      * `effectiveAt` (`string`, required)
      * `expiresAt` (`string`, required)
      * `createdAt` (`string`, required)

    * `remaining` (`string`, required)

    * `status` (`enum`, required): Derived from the dates and what is left, never stored. Allowed values: `active`, `upcoming`, `used`, `expired`.

  * `days` (`array<Day Cost>`, required): Every day from the earlier of the period start and 29 days ago through today, oldest first

    Array items:

    * `day` (`string`, required)

    * `closed` (`boolean`, required): Whether the usage ledger recorded the day, which is then final. Otherwise it is an estimate from telemetry that can still grow

    * `credits` (`string`, required)

    * `pricePerCredit` (`string`, required)

    * `rows` (`array<Ingress Cost Row / Runtime Cost Row>`, required)

      Array items:

      Any of:

      * **Ingress Cost Row** (`Ingress Cost Row`)

        * `_tag` (`"Ingress"`, required)
        * `deploymentId` (`string`, required): A UUID
        * `workspaceId` (`string`, required): A UUID
        * `credits` (`string`, required)
        * `effectiveCost` (`string`, required)
        * `hosting` (`enum`, required): Who operates the deployment infrastructure: Tenzir or the customer. Allowed values: `tenzir`, `customer`.
        * `bytes` (`string`, required) Pattern: `^-?\d+$`.

      * **Runtime Cost Row** (`Runtime Cost Row`)

        * `_tag` (`"Runtime"`, required)
        * `deploymentId` (`string`, required): A UUID
        * `workspaceId` (`string`, required): A UUID
        * `credits` (`string`, required)
        * `effectiveCost` (`string`, required)
        * `size` (`enum`, required): The machine type a hosted deployment runs as. Allowed values: `tiny`, `small`, `medium`, `large`, `xlarge`.
        * `seconds` (`integer`, required): How long it ran as the type that day, in whole seconds. Range: `>= 0, <= 86400`.

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

### `409`: CostUnavailable

Media type: `application/json`

* `_tag` (`"CostUnavailable"`, required)
* `message` (`string`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)

### `503`: ServiceUnavailable

Media type: `application/json`

* `_tag` (`"ServiceUnavailable"`, required)
