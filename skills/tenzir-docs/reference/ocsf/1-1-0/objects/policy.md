# Policy

> The Policy object describes the policies that are applicable.


The Policy object describes the policies that are applicable.

Policy attributes provide traceability to the operational state of the security product at the time that the event was captured, facilitating forensics, troubleshooting, and policy tuning/adjustments.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The policy name. For example: `IAM Policy`.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

A unique identifier of the policy instance.

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The policy version number.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the policy.

**`group`**

* **Type**: [`group`](group.md)
* **Requirement**: optional

The policy group.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`account_change`](../classes/account_change.md)
* [`scan_activity`](../classes/scan_activity.md)