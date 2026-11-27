---
title: "Read billing"
description: "How an organization is billed, its plan and currency, and the plans it can switch to."
canonical: https://tenzir.com/docs/reference/api/billing/read-billing
source: https://tenzir.com/docs/reference/api/billing/read-billing.md
section: "Docs"
---

# Read billing

> How an organization is billed, its plan and currency, and the plans it can switch to.

`GET /api/organizations/{org}/billing`

How an organization is billed, its plan and currency, and the plans it can switch to. An organization without a currency gets one suggested from the region the request comes from. Requires Organization.readBilling

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Responses

### `200`: How an organization is billed, its budget, and the plans on offer

Media type: `application/json`

* `asOf` (`string`, required)

* `subscription` (`Subscription`, required): The plan an organization is on, and what it pays in

  * `planId` (`string | null`, required): A UUID

  * `plan` (`Plan`, required): The pinned plan, or the Community plan in force

    Any of:

    * **Community Plan** (`Community Plan`)

      * `id` (`string`, required): A UUID

      * `effectiveFrom` (`string`, required)

      * `edition` (`"community"`, required)

      * `terms` (`Community Terms`, required): What Community gives and costs: credit rates, daily self-hosted allowance, warning thresholds, and signup grants

        * `ingestCapBytes` (`integer`, optional) Range: `> 0, <= 9007199254740991`.

        * `ingestCapWindowSeconds` (`integer`, optional) Range: `> 0, <= 9007199254740991`.

        * `capWarningPercent` (`integer`, optional): The share of the cap that warns, in percent. Range: `> 0, <= 100`.

        * `ingestCreditsPerGb` (`object`, optional): Per decimal GB of ingress; self-hosted ingress within the daily UTC allowance is free, and egress has no meter

          * `tenzir` (`string`, required)
          * `customer` (`string`, required)

        * `deploymentCreditsPerHour` (`object`, optional): Per running hour of a Tenzir-hosted deployment. A size without a rate is not offered; self-hosted deployments have no such charge

          * `tiny` (`string`, optional)
          * `small` (`string`, optional)
          * `medium` (`string`, optional)
          * `large` (`string`, optional)
          * `xlarge` (`string`, optional)

        * `selfHostedDailyAllowanceBytes` (`integer`, optional): Free self-hosted ingress per UTC day, in decimal bytes. Ingress beyond it draws credits; hosted ingress never counts toward it. Range: `> 0, <= 9007199254740991`.

        * `allowanceWarningPercent` (`integer`, optional): The share of the daily self-hosted allowance that warns when no credits remain, in percent. Range: `> 0, <= 100`.

        * `creditWarningPercent` (`integer`, optional): The share of active granted credits used at which the organization is warned that few credits remain, in percent. Range: `> 0, <= 100`.

        * `grantExpiryWarningDays` (`integer`, optional): How many days before the last active credit grant expires to warn the organization. Range: `> 0, <= 9007199254740991`.

        * `hostedEgressBytesPerCredit` (`integer | null`, optional): Maximum Cloud NAT internet egress per granted credit for Community hosted deployments, in decimal bytes; null disables the guardrail. Range: `> 0, <= 9007199254740991`.

        * `hostedAllowanceCredits` (`string | null`, required)

        * `signupGrant` (`Signup Grant Terms | null`, required): The free credits a new user gets once, on the default organization, for any usage

          * `credits` (`integer`, required): Whole credits per grant. Range: `> 0, <= 9007199254740991`.
          * `validityDays` (`integer`, required): How long the credits are valid, in days from the grant. Range: `> 0, <= 9007199254740991`.

    * **Enterprise Plan** (`Enterprise Plan`)

      * `id` (`string`, required): A UUID

      * `effectiveFrom` (`string`, required)

      * `edition` (`"enterprise"`, required)

      * `terms` (`Enterprise Terms`, required): What Enterprise costs: prices, rates, and volume tiers

        * `prices` (`map<string, object>`, required): Per currency, in its smallest unit: one credit at list price, which PAYG always pays, and the monthly platform fee, paid in money

          Map values:

          * `creditListPrice` (`integer`, required) Range: `> 0, <= 9007199254740991`.
          * `platformFee` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

        * `ingestCreditsPerGb` (`object`, required): Per decimal GB of ingress; egress has no meter

          * `tenzir` (`string`, required)
          * `customer` (`string`, required)

        * `deploymentCreditsPerHour` (`object`, required): Per running hour of a Tenzir-hosted deployment. A size without a rate is not offered; self-hosted deployments have no such charge

          * `tiny` (`string`, optional)
          * `small` (`string`, optional)
          * `medium` (`string`, optional)
          * `large` (`string`, optional)
          * `xlarge` (`string`, optional)

        * `purchaseValidityMonths` (`integer`, required) Range: `> 0, <= 9007199254740991`.

        * `purchasePresets` (`array<integer>`, required)

        * `volumeTiers` (`array<Volume Tier>`, required)

          Array items:

          * `termMonths` (`integer`, required) Range: `> 0, <= 9007199254740991`.
          * `minimumQuantity` (`integer`, required) Range: `> 0, <= 9007199254740991`.
          * `discountBps` (`integer`, required) Range: `>= 0, < 10000`.

        * `budgetWarningPercent` (`integer`, required): The share of the budget that warns, in percent. Range: `> 0, <= 100`.

        * `budgetGraceSeconds` (`object`, required): How long deployments go on after the budget is first reached in a billing period, by who hosts them: then a Tenzir-hosted one stops and a self-hosted one becomes locked

          * `tenzir` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
          * `customer` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

    * **Sovereign Plan** (`Sovereign Plan`)

      * `id` (`string`, required): A UUID
      * `effectiveFrom` (`string`, required)
      * `edition` (`"sovereign"`, required)

    * **Provisioned Plan** (`Provisioned Plan`)

      * `id` (`string`, required): A UUID
      * `effectiveFrom` (`string`, required)
      * `edition` (`"provisioned"`, required)

  * `currency` (`string | null`, required): An ISO 4217 code. A plan offers the currencies it has prices for, and nothing converts between them

* `monthlyBudget` (`integer | null`, required): A threshold on the PAYG ingest and infrastructure spend of a billing month, in the smallest unit of the organization currency, such as cents: 150000 is 1,500. Only whole units of the currency, such as whole dollars, make a budget. It excludes the platform fee, taxes and credit purchases. It warns and enforces, but never caps the invoice. Range: `> 0, <= 9007199254740991`.

* `hosting` (`array<enum>`, required): The hosting kinds of its deployments, each once: what a budget, once reached, restricts differently

* `suggestedCurrency` (`string | null`, required): An ISO 4217 code. A plan offers the currencies it has prices for, and nothing converts between them

* `community` (`Community Plan | null`, required): The free edition and its limits

  * `id` (`string`, required): A UUID

  * `effectiveFrom` (`string`, required)

  * `edition` (`"community"`, required)

  * `terms` (`Community Terms`, required): What Community gives and costs: credit rates, daily self-hosted allowance, warning thresholds, and signup grants

    * `ingestCapBytes` (`integer`, optional) Range: `> 0, <= 9007199254740991`.

    * `ingestCapWindowSeconds` (`integer`, optional) Range: `> 0, <= 9007199254740991`.

    * `capWarningPercent` (`integer`, optional): The share of the cap that warns, in percent. Range: `> 0, <= 100`.

    * `ingestCreditsPerGb` (`object`, optional): Per decimal GB of ingress; self-hosted ingress within the daily UTC allowance is free, and egress has no meter

      * `tenzir` (`string`, required)
      * `customer` (`string`, required)

    * `deploymentCreditsPerHour` (`object`, optional): Per running hour of a Tenzir-hosted deployment. A size without a rate is not offered; self-hosted deployments have no such charge

      * `tiny` (`string`, optional)
      * `small` (`string`, optional)
      * `medium` (`string`, optional)
      * `large` (`string`, optional)
      * `xlarge` (`string`, optional)

    * `selfHostedDailyAllowanceBytes` (`integer`, optional): Free self-hosted ingress per UTC day, in decimal bytes. Ingress beyond it draws credits; hosted ingress never counts toward it. Range: `> 0, <= 9007199254740991`.

    * `allowanceWarningPercent` (`integer`, optional): The share of the daily self-hosted allowance that warns when no credits remain, in percent. Range: `> 0, <= 100`.

    * `creditWarningPercent` (`integer`, optional): The share of active granted credits used at which the organization is warned that few credits remain, in percent. Range: `> 0, <= 100`.

    * `grantExpiryWarningDays` (`integer`, optional): How many days before the last active credit grant expires to warn the organization. Range: `> 0, <= 9007199254740991`.

    * `hostedEgressBytesPerCredit` (`integer | null`, optional): Maximum Cloud NAT internet egress per granted credit for Community hosted deployments, in decimal bytes; null disables the guardrail. Range: `> 0, <= 9007199254740991`.

    * `hostedAllowanceCredits` (`string | null`, required)

    * `signupGrant` (`Signup Grant Terms | null`, required): The free credits a new user gets once, on the default organization, for any usage

      * `credits` (`integer`, required): Whole credits per grant. Range: `> 0, <= 9007199254740991`.
      * `validityDays` (`integer`, required): How long the credits are valid, in days from the grant. Range: `> 0, <= 9007199254740991`.

* `offers` (`array<Plan>`, required): The plans the organization can be pinned to now, besides the one it is on

  Array items:

  Any of:

  * **Community Plan** (`Community Plan`)

    * `id` (`string`, required): A UUID

    * `effectiveFrom` (`string`, required)

    * `edition` (`"community"`, required)

    * `terms` (`Community Terms`, required): What Community gives and costs: credit rates, daily self-hosted allowance, warning thresholds, and signup grants

      * `ingestCapBytes` (`integer`, optional) Range: `> 0, <= 9007199254740991`.

      * `ingestCapWindowSeconds` (`integer`, optional) Range: `> 0, <= 9007199254740991`.

      * `capWarningPercent` (`integer`, optional): The share of the cap that warns, in percent. Range: `> 0, <= 100`.

      * `ingestCreditsPerGb` (`object`, optional): Per decimal GB of ingress; self-hosted ingress within the daily UTC allowance is free, and egress has no meter

        * `tenzir` (`string`, required)
        * `customer` (`string`, required)

      * `deploymentCreditsPerHour` (`object`, optional): Per running hour of a Tenzir-hosted deployment. A size without a rate is not offered; self-hosted deployments have no such charge

        * `tiny` (`string`, optional)
        * `small` (`string`, optional)
        * `medium` (`string`, optional)
        * `large` (`string`, optional)
        * `xlarge` (`string`, optional)

      * `selfHostedDailyAllowanceBytes` (`integer`, optional): Free self-hosted ingress per UTC day, in decimal bytes. Ingress beyond it draws credits; hosted ingress never counts toward it. Range: `> 0, <= 9007199254740991`.

      * `allowanceWarningPercent` (`integer`, optional): The share of the daily self-hosted allowance that warns when no credits remain, in percent. Range: `> 0, <= 100`.

      * `creditWarningPercent` (`integer`, optional): The share of active granted credits used at which the organization is warned that few credits remain, in percent. Range: `> 0, <= 100`.

      * `grantExpiryWarningDays` (`integer`, optional): How many days before the last active credit grant expires to warn the organization. Range: `> 0, <= 9007199254740991`.

      * `hostedEgressBytesPerCredit` (`integer | null`, optional): Maximum Cloud NAT internet egress per granted credit for Community hosted deployments, in decimal bytes; null disables the guardrail. Range: `> 0, <= 9007199254740991`.

      * `hostedAllowanceCredits` (`string | null`, required)

      * `signupGrant` (`Signup Grant Terms | null`, required): The free credits a new user gets once, on the default organization, for any usage

        * `credits` (`integer`, required): Whole credits per grant. Range: `> 0, <= 9007199254740991`.
        * `validityDays` (`integer`, required): How long the credits are valid, in days from the grant. Range: `> 0, <= 9007199254740991`.

  * **Enterprise Plan** (`Enterprise Plan`)

    * `id` (`string`, required): A UUID

    * `effectiveFrom` (`string`, required)

    * `edition` (`"enterprise"`, required)

    * `terms` (`Enterprise Terms`, required): What Enterprise costs: prices, rates, and volume tiers

      * `prices` (`map<string, object>`, required): Per currency, in its smallest unit: one credit at list price, which PAYG always pays, and the monthly platform fee, paid in money

        Map values:

        * `creditListPrice` (`integer`, required) Range: `> 0, <= 9007199254740991`.
        * `platformFee` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

      * `ingestCreditsPerGb` (`object`, required): Per decimal GB of ingress; egress has no meter

        * `tenzir` (`string`, required)
        * `customer` (`string`, required)

      * `deploymentCreditsPerHour` (`object`, required): Per running hour of a Tenzir-hosted deployment. A size without a rate is not offered; self-hosted deployments have no such charge

        * `tiny` (`string`, optional)
        * `small` (`string`, optional)
        * `medium` (`string`, optional)
        * `large` (`string`, optional)
        * `xlarge` (`string`, optional)

      * `purchaseValidityMonths` (`integer`, required) Range: `> 0, <= 9007199254740991`.

      * `purchasePresets` (`array<integer>`, required)

      * `volumeTiers` (`array<Volume Tier>`, required)

        Array items:

        * `termMonths` (`integer`, required) Range: `> 0, <= 9007199254740991`.
        * `minimumQuantity` (`integer`, required) Range: `> 0, <= 9007199254740991`.
        * `discountBps` (`integer`, required) Range: `>= 0, < 10000`.

      * `budgetWarningPercent` (`integer`, required): The share of the budget that warns, in percent. Range: `> 0, <= 100`.

      * `budgetGraceSeconds` (`object`, required): How long deployments go on after the budget is first reached in a billing period, by who hosts them: then a Tenzir-hosted one stops and a self-hosted one becomes locked

        * `tenzir` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
        * `customer` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

  * **Sovereign Plan** (`Sovereign Plan`)

    * `id` (`string`, required): A UUID
    * `effectiveFrom` (`string`, required)
    * `edition` (`"sovereign"`, required)

  * **Provisioned Plan** (`Provisioned Plan`)

    * `id` (`string`, required): A UUID
    * `effectiveFrom` (`string`, required)
    * `edition` (`"provisioned"`, required)

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
