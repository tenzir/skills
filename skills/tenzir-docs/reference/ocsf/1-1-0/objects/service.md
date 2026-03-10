# Service

> The Service object describes characteristics of a service, ` e.g.


The Service object describes characteristics of a service, `e.g. AWS EC2.`

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the service.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the service.

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The version of the service.

**`labels`**

* **Type**: `string_t`
* **Requirement**: optional

The list of labels associated with the service.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`authentication`](../classes/authentication.md)