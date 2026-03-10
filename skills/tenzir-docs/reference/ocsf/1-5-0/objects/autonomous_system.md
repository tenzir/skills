# Autonomous System

> An autonomous system (AS) is a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain that presents a common, clearly defined routing policy to the internet.


An autonomous system (AS) is a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain that presents a common, clearly defined routing policy to the internet.

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

Organization name for the Autonomous System.

**`number`**

* **Type**: `integer_t`
* **Requirement**: recommended

Unique number that the AS is identified by.

## Constraints

At least one of: `number`, `name`