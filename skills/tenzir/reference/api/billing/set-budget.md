---
title: "Set budget"
description: "Sets, changes or removes an organization's monthly budget, in the smallest unit of its currency, in whole units of it: 150000 is 1,500."
canonical: https://tenzir.com/docs/reference/api/billing/set-budget
source: https://tenzir.com/docs/reference/api/billing/set-budget.md
section: "Docs"
---

# Set budget

> Sets, changes or removes an organization's monthly budget, in the smallest unit of its currency, in whole units of it: 150000 is 1,500.

`POST /api/organizations/{org}/billing/set-budget`

Sets, changes or removes an organization's monthly budget, in the smallest unit of its currency, in whole units of it: 150000 is 1,500. Only Enterprise can set one. It applies to PAYG ingest and infrastructure spend, not the minimum-spend shortfall, taxes or credit purchases, and warns and enforces but never caps the invoice. Requires Organization.setBudget

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Request body (`application/json`, required)

* `monthlyBudget` (`integer | null`, required): A threshold on the PAYG ingest and infrastructure spend of a billing month, in the smallest unit of the organization currency, such as cents: 150000 is 1,500. Only whole units of the currency, such as whole dollars, make a budget. It excludes the minimum-spend shortfall, taxes and credit purchases. It warns and enforces, but never caps the invoice. Range: `> 0, <= 9007199254740991`.

## Responses

### `200`: The monthly budget of an organization, in its currency

Media type: `application/json`

* `monthlyBudget` (`integer | null`, required): A threshold on the PAYG ingest and infrastructure spend of a billing month, in the smallest unit of the organization currency, such as cents: 150000 is 1,500. Only whole units of the currency, such as whole dollars, make a budget. It excludes the minimum-spend shortfall, taxes and credit purchases. It warns and enforces, but never caps the invoice. Range: `> 0, <= 9007199254740991`.
* `currency` (`string | null`, required): An ISO 4217 code. A plan offers the currencies it has prices for, and nothing converts between them

### `400`: InvalidBudget | CredentialConflict | Validation

Media type: `application/json`

Any of:

* **InvalidBudget** (`InvalidBudget`)

  * `_tag` (`"InvalidBudget"`, required)
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

### `409`: BudgetUnavailable

Media type: `application/json`

* `_tag` (`"BudgetUnavailable"`, required)
* `message` (`string`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
