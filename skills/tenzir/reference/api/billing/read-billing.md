---
title: "Read billing"
description: "How an organization is billed, its plan and currency, the plans it can switch to, any scheduled month-end downgrade to Community, and current Community downgrade cleanup blockers."
canonical: https://tenzir.com/docs/reference/api/billing/read-billing
source: https://tenzir.com/docs/reference/api/billing/read-billing.md
section: "Docs"
---

# Read billing

> How an organization is billed, its plan and currency, the plans it can switch to, any scheduled month-end downgrade to Community, and current Community downgrade cleanup blockers.

`GET /api/organizations/{org}/billing`

How an organization is billed, its plan and currency, the plans it can switch to, any scheduled month-end downgrade to Community, and current Community downgrade cleanup blockers. An organization without a currency gets one suggested from the region the request comes from. Requires Organization.readBilling

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

        * `prices` (`map<string, Prices>`, required): Per currency, in its smallest unit: one credit at list price, which PAYG always pays, and the monthly minimum spend, paid in money

          Map values:

          Any of:

          * **Option 1** (`object`)

            * `creditListPrice` (`integer`, required): One credit at list price, which PAYG always pays. Range: `> 0, <= 9007199254740991`.
            * `monthlyMinimum` (`integer`, required): The least an organization pays per calendar month, in arrears: paid usage (PAYG and purchased credits at what was paid for them) counts toward it, free credits never do, and nothing rolls over. Range: `>= 0, <= 9007199254740991`.

          * **Option 2** (`object`)

            * `creditListPrice` (`integer`, required): One credit at list price, which PAYG always pays. Range: `> 0, <= 9007199254740991`.
            * `platformFee` (`integer`, required): The monthly minimum, as plans published before it name it. Range: `>= 0, <= 9007199254740991`.

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

* `monthlyBudget` (`integer | null`, required): A threshold on the PAYG ingest and infrastructure spend of a billing month, in the smallest unit of the organization currency, such as cents: 150000 is 1,500. Only whole units of the currency, such as whole dollars, make a budget. It excludes the minimum-spend shortfall, taxes and credit purchases. It warns and enforces, but never caps the invoice. Range: `> 0, <= 9007199254740991`.

* `hosting` (`array<enum>`, required): The hosting kinds of its deployments, each once: what a budget, once reached, restricts differently

* `hasIngestEndpoints` (`boolean`, optional)

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

      * `prices` (`map<string, Prices>`, required): Per currency, in its smallest unit: one credit at list price, which PAYG always pays, and the monthly minimum spend, paid in money

        Map values:

        Any of:

        * **Option 1** (`object`)

          * `creditListPrice` (`integer`, required): One credit at list price, which PAYG always pays. Range: `> 0, <= 9007199254740991`.
          * `monthlyMinimum` (`integer`, required): The least an organization pays per calendar month, in arrears: paid usage (PAYG and purchased credits at what was paid for them) counts toward it, free credits never do, and nothing rolls over. Range: `>= 0, <= 9007199254740991`.

        * **Option 2** (`object`)

          * `creditListPrice` (`integer`, required): One credit at list price, which PAYG always pays. Range: `> 0, <= 9007199254740991`.
          * `platformFee` (`integer`, required): The monthly minimum, as plans published before it name it. Range: `>= 0, <= 9007199254740991`.

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

* `scheduledDowngrade` (`Scheduled Downgrade | null`, optional): A pending Enterprise to Community downgrade scheduled for the end of the current UTC calendar month

  * `targetEdition` (`"community"`, required): The edition the organization will switch to at effectiveAt

  * `effectiveAt` (`string`, required)

  * `requestedAt` (`string`, required)

  * `blockedReason` (`string | null`, optional)

  * `blockedAt` (`string | null`, optional)

  * `blockers` (`Community Downgrade Blockers`, required): Current blockers to clear before the scheduled downgrade can execute

    * `missingOwner` (`boolean`, optional): No active organization member holds the built-in Owner role
    * `workspaces` (`integer`, required): Number of workspaces above the Community limit (0 when within the limit of 1). Range: `>= 0, <= 9007199254740991`.
    * `deployments` (`integer`, required): Number of deployments above the Community limit (0 when within the limit of 1). Range: `>= 0, <= 9007199254740991`.
    * `ingestEndpoints` (`integer`, required): Number of ingest endpoints above the Community limit (0 when within the limit of 1). Range: `>= 0, <= 9007199254740991`.
    * `oversizedHostedDeployments` (`integer`, required): Number of Tenzir-hosted deployments larger than Community supports (or any hosted deployment when Community offers none). Range: `>= 0, <= 9007199254740991`.

* `downgradeBlockers` (`Community Downgrade Blockers | null`, optional): Missing ownership and excess resources that prevent a downgrade to Community

  * `missingOwner` (`boolean`, optional): No active organization member holds the built-in Owner role
  * `workspaces` (`integer`, required): Number of workspaces above the Community limit (0 when within the limit of 1). Range: `>= 0, <= 9007199254740991`.
  * `deployments` (`integer`, required): Number of deployments above the Community limit (0 when within the limit of 1). Range: `>= 0, <= 9007199254740991`.
  * `ingestEndpoints` (`integer`, required): Number of ingest endpoints above the Community limit (0 when within the limit of 1). Range: `>= 0, <= 9007199254740991`.
  * `oversizedHostedDeployments` (`integer`, required): Number of Tenzir-hosted deployments larger than Community supports (or any hosted deployment when Community offers none). Range: `>= 0, <= 9007199254740991`.

* `billingMode` (`enum`, optional): How an organization settles Enterprise charges: self-serve card billing through Stripe, invoiced contract, or partner contract. Allowed values: `self_serve`, `invoiced`, `partner`.

* `paymentProvider` (`enum`, optional): Which payment backend this installation uses for self-serve billing. Allowed values: `stripe`, `fake`, `unavailable`.

* `paymentMethod` (`Payment Method Summary`, optional): Summary of the organization’s saved payment method

  * `brand` (`string | null`, required)
  * `last4` (`string | null`, required)
  * `expMonth` (`integer | null`, required) Range: `>= 1, <= 12`.
  * `expYear` (`integer | null`, required) Range: `>= 2000, <= 9007199254740991`.
  * `status` (`enum`, required): Current authentication and usability state of the organization’s saved payment method. Allowed values: `none`, `active`, `requires_action`, `failed`.

* `pendingSetup` (`Billing Setup Session Summary | null`, optional): Current state of a Stripe card setup session

  * `id` (`string`, required): Unique identifier of a Stripe card setup session
  * `purpose` (`enum`, required): Why the organization started a Stripe payment method setup session. Allowed values: `upgrade`, `replace_payment_method`.
  * `status` (`enum`, required): Lifecycle status of a Stripe payment method setup session. Allowed values: `pending`, `completed`, `failed`, `canceled`, `expired`.
  * `currency` (`string | null`, required): An ISO 4217 code. A plan offers the currencies it has prices for, and nothing converts between them
  * `failureReason` (`string | null`, required)
  * `createdAt` (`string`, required)

* `pendingPurchase` (`Pending Credit Purchase Summary | null`, optional): Non-secret summary of a pending prepaid credit purchase on the billing overview

  * `id` (`string`, required): Unique identifier of a prepaid credit purchase
  * `quantity` (`integer`, required) Range: `> 0, <= 9007199254740991`.
  * `quotedAmount` (`integer`, required): Quoted pre-tax amount in minor units. Range: `> 0, <= 9007199254740991`.
  * `currency` (`string`, required): An ISO 4217 code. A plan offers the currencies it has prices for, and nothing converts between them
  * `status` (`enum`, required): Lifecycle status of a prepaid credit purchase. Allowed values: `pending`, `paid`, `failed`, `canceled`, `expired`, `refunded`, `disputed`.
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
