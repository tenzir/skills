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

**`tags`**

* **Type**: [`key_value_object`](key_value_object.md)
* **Requirement**: optional

The list of tags; `{key:value}` pairs associated to the service.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`authentication`](../classes/authentication.md)
* [`service_query`](../classes/service_query.md)